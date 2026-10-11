#!/usr/bin/env python3
"""Format scanner, step 2: classify every pulled ad against our format catalog with the Claude Batch API.

usage:
  python3 classify.py submit [--limit N]   # build + submit a batch (start with --limit 20 to measure cost)
  python3 classify.py status               # show batch progress
  python3 classify.py collect              # download results -> results.jsonl, print token usage + cost

Needs ANTHROPIC_API_KEY in the environment. Reads catalog.json (our 100 video + 92 image formats) and
W/ads_*.jsonl (written by the pull agents); images come from W/sheets (video contact sheets) and W/images (statics).
"""
import base64, glob, json, os, sys, time
import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

R = os.path.dirname(os.path.abspath(__file__))
W = os.environ.get("SCAN_DIR", "/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/scan")
STATE = f"{R}/batch_state.json"
MODEL = "claude-opus-5-5"
PRICE_IN, PRICE_OUT, PRICE_CACHE_READ = 4.00 / 2, 20.00 / 2, 0.20 / 2  # $/MTok, batch = 50% off

catalog = json.load(open(f"{R}/catalog.json"))
CAT_TEXT = "\n".join(f"{c['id']} [{c['medium']}] {c['name']}: {c['definition']}" for c in catalog)
SYSTEM = [
    {"type": "text", "text": (
        "You classify paid social ads (Meta) into AD FORMATS. A format is the structure/concept of the WHOLE ad "
        "(e.g. street interview, fake podcast, text on skin, reddit post screenshot), not the product, niche, offer or hook. "
        "For a video you get a contact sheet: 12 frames spread across the whole ad, each labelled with its timestamp. "
        "For a static image ad you get the image itself. You also get the ad copy and how long it has been running.\n\n"
        "Pick the single best matching format id from the catalog below. Video ads should normally match [video] formats and "
        "static ads [image] formats. Only answer NEW when the overall structure is clearly none of the catalog formats - a new "
        "product, niche, hook or nicer production is NOT a new format. When NEW, give it a short name (2-5 words), a 1-2 "
        "sentence definition of the whole-ad structure (what you see, beat by beat for video), the closest catalog id and "
        "how it differs.\n\nCATALOG:\n" + CAT_TEXT),
     "cache_control": {"type": "ephemeral", "ttl": "1h"}},
]
SCHEMA = {
    "type": "object",
    "properties": {
        "format_id": {"type": "string", "description": "catalog id like V012 / I034, or NEW"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "what_you_see": {"type": "string", "description": "one sentence describing the ad"},
        "new_name": {"type": "string"},
        "new_definition": {"type": "string"},
        "closest_id": {"type": "string"},
        "why_different": {"type": "string"},
    },
    "required": ["format_id", "confidence", "what_you_see", "new_name", "new_definition", "closest_id", "why_different"],
    "additionalProperties": False,
}


def load_ads():
    ads, seen = [], set()
    for f in sorted(glob.glob(f"{W}/ads_*.jsonl")):
        for line in open(f):
            try:
                a = json.loads(line)
            except json.JSONDecodeError:
                continue
            if a.get("file") and a["id"] not in seen and os.path.exists(f"{W}/{a['file']}"):
                seen.add(a["id"]); ads.append(a)
    return ads


def image_block(path):
    ext = path.rsplit(".", 1)[-1].lower()
    mt = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp", "gif": "image/gif"}.get(ext, "image/jpeg")
    return {"type": "image", "source": {"type": "base64", "media_type": mt,
                                        "data": base64.standard_b64encode(open(path, "rb").read()).decode()}}


def request_for(a):
    kind = "VIDEO ad (contact sheet of 12 frames)" if a["media_type"].startswith("video") else "STATIC image ad"
    text = (f"{kind} from {a['brand']}. Running {a.get('days')} days (started {a.get('started')}, last seen {a.get('last_seen')}), "
            f"{a.get('dup') or 1} ad(s) using this creative.\nAd copy: {a.get('ad_text') or '(none)'}")
    return Request(custom_id=str(a["id"]), params=MessageCreateParamsNonStreaming(
        model=MODEL, max_tokens=4000, system=SYSTEM,
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": [image_block(f"{W}/{a['file']}"), {"type": "text", "text": text}]}]))


def submit(limit=None):
    done = set()
    if os.path.exists(f"{R}/results.jsonl"):
        done = {json.loads(l)["id"] for l in open(f"{R}/results.jsonl")}
    ads = [a for a in load_ads() if str(a["id"]) not in done]
    if limit: ads = ads[:limit]
    if not ads: print("nothing to submit"); return
    client = anthropic.Anthropic()
    batch = client.messages.batches.create(requests=[request_for(a) for a in ads])
    st = json.load(open(STATE)) if os.path.exists(STATE) else {"batches": []}
    st["batches"].append({"id": batch.id, "n": len(ads), "collected": False})
    json.dump(st, open(STATE, "w"), indent=1)
    print(f"submitted {batch.id} with {len(ads)} ads")


def status():
    client = anthropic.Anthropic()
    for b in json.load(open(STATE))["batches"]:
        x = client.messages.batches.retrieve(b["id"])
        print(b["id"], x.processing_status, x.request_counts)


def collect():
    client = anthropic.Anthropic()
    st = json.load(open(STATE)); meta = {str(a["id"]): a for a in load_ads()}
    tin = tout = tcache = 0
    with open(f"{R}/results.jsonl", "a") as out:
        for b in st["batches"]:
            if b["collected"]: continue
            if client.messages.batches.retrieve(b["id"]).processing_status != "ended":
                print(b["id"], "still running"); continue
            for r in client.messages.batches.results(b["id"]):
                if r.result.type != "succeeded":
                    print(r.custom_id, r.result.type); continue
                m = r.result.message; u = m.usage
                tin += u.input_tokens; tout += u.output_tokens; tcache += (u.cache_read_input_tokens or 0) + (u.cache_creation_input_tokens or 0)
                if m.stop_reason == "refusal":
                    print(r.custom_id, "refusal"); continue
                txt = next((c.text for c in m.content if c.type == "text"), "")
                try:
                    res = json.loads(txt)
                except json.JSONDecodeError:
                    print(r.custom_id, "bad json"); continue
                a = meta.get(r.custom_id, {})
                out.write(json.dumps({"id": r.custom_id, "brand": a.get("brand"), "media_type": a.get("media_type"),
                                      "days": a.get("days"), "dup": a.get("dup"), "file": a.get("file"), **res}) + "\n")
            b["collected"] = True
    json.dump(st, open(STATE, "w"), indent=1)
    cost = tin / 1e6 * PRICE_IN + tout / 1e6 * PRICE_OUT + tcache / 1e6 * PRICE_CACHE_READ
    print(f"tokens in {tin:,} out {tout:,} cache {tcache:,}  ~= ${cost:.2f} (cache writes counted at read price; real cost slightly higher)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    lim = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    {"submit": lambda: submit(lim), "status": status, "collect": collect}[cmd]()

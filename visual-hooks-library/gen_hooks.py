#!/usr/bin/env python3
"""gen_hooks.py -> hooks_data.json, hooks_img/<slug>.jpg (composite of example 3s strips), hboard/frame_<cat>.svg, hboard/plan.json
Sources: taxonomy.json, cls_meta_all.json + meta.json (Meta ads), cls_tt_all.json + tt_pool.json (TikTok ads), K*.json hunts."""
import json, glob, os, re, html
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__))
MAXEX = 6
tax = json.load(open(f"{H}/taxonomy.json"))
meta = json.load(open(f"{H}/meta.json"))
tt = {str(x["productid"]): x for x in json.load(open(f"{H}/tt_pool.json"))}
EXCL = set(json.load(open(f"{H}/exclude.json"))) if os.path.exists(f"{H}/exclude.json") else set()
DRIVE = json.load(open(f"{H}/drive_hooks.json")) if os.path.exists(f"{H}/drive_hooks.json") else {}

def clean(i): return re.sub(r"^N_", "", str(i))
from datetime import date
def span(e):
    try:
        a = date.fromisoformat(str(e.get("started"))[:10]); b = date.fromisoformat(str(e.get("last_seen"))[:10]); return (b - a).days + 1
    except Exception: return None
def ex_meta(i, v):
    m = meta.get(clean(i), {})
    return {"id": clean(i), "platform": "meta", "advertiser": m.get("adv", ""), "strip": f"strips/{i}.jpg",
            "link": f"https://app.winninghunter.com/ad/{clean(i)}?platform=meta", "likes": None, "days": m.get("days"),
            "video_url": m.get("video", ""), "what_you_see": v.get("what_you_see", "")}
def ex_tt(i, v):
    m = tt.get(str(i), {})
    return {"id": str(i), "platform": "tiktok", "advertiser": m.get("pageName", ""), "strip": f"tt_strips/{i}.jpg",
            "link": f"https://app.winninghunter.com/ad/{i}?platform=tiktok", "likes": m.get("likeCount"), "days": m.get("daysrunning"),
            "video_url": m.get("video_url", ""), "what_you_see": v.get("what_you_see", "")}

ex = {x["name"]: [] for x in tax}
seen = {x["name"]: set() for x in tax}
def add(fmt, e):
    if fmt in ex and e["id"] not in seen[fmt] and e["id"] not in EXCL and os.path.exists(f"{H}/{e['strip']}"):
        ex[fmt].append(e); seen[fmt].add(e["id"])
# hunted (targeted, verified) first
for f in sorted(glob.glob(f"{H}/K*.json")):
    if not re.fullmatch(r"K\d+[ab]?\.json", os.path.basename(f)): continue
    for fmt, lst in json.load(open(f)).items():
        for e in lst:
            e = dict(e); e["id"] = str(e["id"]); e.setdefault("strip", f"hunt_strips/{e['id']}.jpg")
            e["days"] = e.get("days_running") or e.get("days") or span(e); e["hunted"] = True
            if e.get("platform") == "tiktok" and e.get("likes"): e["days"] = None
            add(fmt, e)
for i, v in json.load(open(f"{H}/cls_tt_all.json")).items():
    if v.get("confidence") == "high": add(v.get("format"), ex_tt(i, v))
for i, v in json.load(open(f"{H}/cls_meta_all.json")).items():
    if v.get("confidence") == "high":
        e = ex_meta(i, v)
        if (e.get("days") or 0) >= 30: add(v.get("format"), e)
# rank: real product brands first, then likes/days
def score(e):
    return (e.get("likes") or 0) / 1000 + (e.get("days") or 0)
for k in ex: ex[k] = sorted(ex[k], key=score, reverse=True)
# cross-format dedupe: same ad under several formats -> drop it from the richer format unless that pushes it below 3
from collections import defaultdict
where = defaultdict(list)
for k, lst in ex.items():
    for e in lst: where[e["id"]].append(k)
dropped = []
for i, fmts in where.items():
    fmts = sorted(fmts, key=lambda k: len(ex[k]))
    for k in fmts[1:]:
        if len(ex[k]) > 3:
            ex[k] = [e for e in ex[k] if e["id"] != i]; dropped.append((i, k))
print("cross-format dupes dropped:", len(dropped), "kept multi:", sum(1 for f in where.values() if len(f) > 1) - len({d[0] for d in dropped}))

data = []
for x in tax:
    d = dict(x); d["kallaway"] = "Kallaway" in x.get("source", ""); d["examples"] = ex[x["name"]]; data.append(d)
json.dump(data, open(f"{H}/hooks_data.json", "w"), indent=1)

# composite images
os.makedirs(f"{H}/hooks_img", exist_ok=True)
try: FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except Exception: FONT = ImageFont.load_default()
IW = 1400
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def fmt_num(n):
    return f"{n/1e6:.1f}M" if n >= 1e6 else f"{n/1e3:.0f}k"
def label(e, n):
    bits = [f"{n}", e.get("advertiser") or "", ("TikTok " + fmt_num(e["likes"]) + " likes") if e.get("likes") else (f"{e['days']} days live" if e.get("days") else "")]
    return "  ·  ".join(b for b in bits if b)
for d in data:
    exs = d["examples"][:MAXEX]
    if not exs: continue
    rows = []
    for n, e in enumerate(exs, 1):
        im = Image.open(f"{H}/{e['strip']}").convert("RGB")
        im = im.resize((IW, int(im.height * IW / im.width)))
        rows.append((label(e, n), im))
    Ht = sum(34 + im.height + 10 for _, im in rows)
    c = Image.new("RGB", (IW, Ht), "white"); dr = ImageDraw.Draw(c); y = 0
    for lab, im in rows:
        dr.rectangle([0, y, IW, y + 32], fill="#1a1a1a"); dr.text((10, y + 4), lab, fill="#ffd84d", font=FONT)
        c.paste(im, (0, y + 34)); y += 34 + im.height + 10
    d["img"] = f"hooks_img/{slug(d['name'])}.jpg"; d["img_size"] = c.size
    c.save(f"{H}/{d['img']}", quality=82)
json.dump(data, open(f"{H}/hooks_data.json", "w"), indent=1)
print("formats", len(data), "with examples", sum(1 for d in data if d["examples"]), "examples shown", sum(min(len(d["examples"]), MAXEX) for d in data),
      ">=3:", sum(1 for d in data if len(d["examples"]) >= 3))

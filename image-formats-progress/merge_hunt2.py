#!/usr/bin/env python3
"""merge_hunt2.py video|image -> formats2_<kind>.json (+ copies creatives into imgs2/)"""
import json, sys, os, glob, shutil, re
from PIL import Image
S = os.path.dirname(os.path.abspath(__file__)); kind = sys.argv[1]
H = f"{S}/hunt2"; I2 = f"{S}/imgs2"; os.makedirs(I2, exist_ok=True)
base = json.load(open(f"{S}/formats_{kind}.json"))
pref = "V" if kind == "video" else "I"
disc = "D" if kind == "video" else "E"
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
EXCL = set(json.load(open(f"{S}/exclude_{kind}.json"))) if os.path.exists(f"{S}/exclude_{kind}.json") else set()
ORDER = ["TOF", "TOF,MOF", "MOF", "MOF,BOF", "BOF", ""]

def stage_code(s):
    s = (s or "").upper()
    has = [c for c in ("TOF", "MOF", "BOF") if c in s]
    if not has or "ANY" in s: return ""
    if len(has) == 3: return ""
    return ",".join(has)

def ref_from(m, src_dir, pick=False):
    fn = m.get("file") or ""
    src = os.path.join(src_dir, fn)
    if not fn or not os.path.exists(src):
        return None
    dst = f"{I2}/{fn}"
    im = Image.open(src)
    if im.format != "JPEG" or im.mode != "RGB":
        im.convert("RGB").save(dst, "JPEG", quality=92)
    else:
        shutil.copy(src, dst)
    return {"id": m["id"], "file": fn, "wh_link": m.get("wh_link") or f"https://app.winninghunter.com/ad/{m['id']}?platform=meta",
            "fb_page": m.get("fb_page", ""), "days": m.get("days_running"), "advertiser": m.get("advertiser", ""), "pick": pick}

hunted, new, issues = {}, [], []
for f in sorted(g for g in glob.glob(f"{H}/{pref}*.json") if re.fullmatch(pref+r"\d+\.json", os.path.basename(g))):
    for e in json.load(open(f)):
        if e["format"] == "NEW_SIGHTINGS": continue
        hunted.setdefault(norm(e["format"]), []).extend(e.get("matches", []))
for f in sorted((g for g in glob.glob(f"{H}/{disc}*.json") if re.fullmatch(disc+r"\d+\.json", os.path.basename(g)))):
    for e in json.load(open(f)):
        new.append(e)

picks = {}
if kind == "video" and os.path.exists(f"{S}/concepts/concepts.json"):
    for c in json.load(open(f"{S}/concepts/concepts.json")):
        c["days_running"] = c.get("days_running")
        picks.setdefault(norm(c["primary_format"]), []).append(c)

out = []
def build(name, stages, why, links, fid, isnew, matches):
    refs, seen = [], set()
    for c in picks.get(norm(name), []):
        r = ref_from(c, f"{S}/concepts", pick=True)
        if r and r["id"] not in seen: refs.append(r); seen.add(r["id"])
    firsts, repeats, advs = [], [], set()
    for m in matches:
        if m.get("id") in EXCL: continue
        a = norm(m.get("advertiser", ""))
        (repeats if a in advs else firsts).append(m); advs.add(a)
    for m in firsts + repeats:
        r = ref_from(m, H)
        if r and r["id"] not in seen: refs.append(r); seen.add(r["id"])
        elif not r: issues.append(f"{name}: missing file for {m.get('id')}")
    winners = [r for r in refs if not r["pick"]]
    if len(winners) < 5: issues.append(f"{name}: only {len(winners)} winners")
    return {"id": fid, "name": name, "stages": stages, "status": "", "why": why, "links": links, "new": isnew, "refs": refs}

for b in base:
    out.append(build(b["name"], b["stages"], b["why"], b["links"], b["id"], False, hunted.get(norm(b["name"]), [])))
for e in new:
    nm = e["format"]
    if norm(nm) in {norm(b["name"]) for b in base}: continue
    why = (e.get("definition", "") + " " + e.get("why_it_works", "")).strip()
    out.append(build(nm, stage_code(e.get("stage")), why, [], None, True, e.get("matches", [])))
# concept picks whose primary format is a new one that discovery did not confirm -> fall back to secondary format
known = {norm(o["name"]) for o in out}
for k, cs in picks.items():
    if k not in known:
        for c in cs:
            sec = norm(c.get("secondary_format") or "")
            tgt = next((o for o in out if norm(o["name"]) == sec), None)
            if tgt:
                r = ref_from(c, f"{S}/concepts", pick=True)
                if r: tgt["refs"].insert(0, r)
            else:
                issues.append(f"pick {c['id']} ({c['primary_format']}) has no home")
# cross-format dedupe: one ad lives in one format. Keep it where it is most specific:
# new formats win over old ones, then the format with fewer refs; never drop a format below 5 winners.
from collections import defaultdict
where = defaultdict(list)
for oi, o in enumerate(out):
    for r in o["refs"]:
        if not r["pick"]: where[r["id"]].append(oi)
for aid, ois in where.items():
    if len(ois) < 2: continue
    ois = sorted(set(ois), key=lambda oi: (not out[oi]["new"], len(out[oi]["refs"])))
    keep = ois[0]
    for oi in ois[1:]:
        nw = sum(not r["pick"] for r in out[oi]["refs"])
        if nw > 5:
            out[oi]["refs"] = [r for r in out[oi]["refs"] if r["id"] != aid]
            issues.append(f"dedupe {aid}: kept in {out[keep]['name']}, removed from {out[oi]['name']}")
        else:
            issues.append(f"dedupe {aid}: in {out[keep]['name']} AND {out[oi]['name']} (kept both, {out[oi]['name']} has only {nw})")
W = f"{S}/new_format_whys_{kind}.json"
if os.path.exists(W):
    ov = json.load(open(W))
    for o in out:
        if o["name"] in ov: o["why"] = ov[o["name"]]
json.dump(out, open(f"{S}/formats2_{kind}.json", "w"), indent=1)
print("formats", len(out), "new", sum(o["new"] for o in out), "refs", sum(len(o["refs"]) for o in out))
for i in issues: print("ISSUE", i)

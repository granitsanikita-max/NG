import json, glob, os
from datetime import date
W = os.path.dirname(os.path.abspath(__file__))
ads = {}
for f in glob.glob(f"{W}/F*_ads.json"):
    t = os.path.basename(f).split("_")[0]; d = json.load(open(f))
    for i, a in (d.items() if isinstance(d, dict) else [(x["id"], x) for x in d]): ads[(t, str(i))] = a
cands = {}
for k, lst in json.load(open(f"{W}/cands.json")).items():
    for c in lst: cands[(c["task"], c["id"])] = c
def span(a, b):
    try: return (date.fromisoformat(str(b)[:10]) - date.fromisoformat(str(a)[:10])).days
    except Exception: return None
OVERRIDE = {"Meme Caption Loop": ("KEEP", "Meme Caption Loop (Relatable Joke Clip)"), "Panic Restock Reaction": ("DROP", "")}
fmts = {}
for f in sorted(glob.glob(f"{W}/verify/[A-G].json")):
    for k, v in json.load(open(f)).items():
        dec, name = v["decision"], k
        if k in OVERRIDE: dec, name = OVERRIDE[k]
        if not dec.startswith("KEEP"): continue
        refs = []
        for t in v["top5"]:
            a = ads.get((t["task"], t["id"]), {}); c = cands.get((t["task"], t["id"]), {})
            st = a.get("started") or c.get("started"); ls = a.get("last_seen") or c.get("last")
            refs.append({"id": t["id"], "task": t["task"], "brand": t["brand"], "started": st, "last": ls,
                         "days": t.get("days") or a.get("days") or span(st, ls), "what_you_see": t.get("what_you_see", ""),
                         "video_url": a.get("video_url"), "file": f"vids/{t['task']}_{t['id']}.mp4", "src": "verify"})
        fmts[name] = {"name": name, "orig": v.get("orig", k), "stage": v["stage"], "definition": v["definition"], "why": v["why"],
                      "how": v["how"], "closest_existing": v["closest_existing"], "refs": refs}
for f in [f"{W}/fill/{x}.json" for x in ("A","B","DE","F","G1","G2","X","R2a","R2b") if os.path.exists(f"{W}/fill/{x}.json")]:
    for k, lst in json.load(open(f)).items():
        if k not in fmts: print("FILL name mismatch:", f, k); continue
        have = {r["id"] for r in fmts[k]["refs"]}
        for e in lst:
            if str(e["id"]) in have: continue
            fmts[k]["refs"].append({"id": str(e["id"]), "task": e["task"], "brand": e["brand"], "started": e.get("started"), "last": e.get("last"),
               "days": e.get("days") or span(e.get("started"), e.get("last")), "what_you_see": e.get("what_you_see", ""),
               "video_url": e.get("video_url"), "file": f"vids/{e['task']}_{e['id']}.mp4", "src": "fill", "platform": e.get("platform", "meta"), "likes": e.get("likes")})
import subprocess
def resolve(r):
    g = glob.glob(f"{W}/vids/*_{r['id']}.mp4")
    if g: r["file"] = os.path.relpath(g[0], W); return True
    if not r.get("video_url"): return False
    out = f"{W}/{r['file']}"
    subprocess.run(["curl", "-sSL", "--max-time", "180", "-o", out, r["video_url"]])
    ok = os.path.exists(out) and os.path.getsize(out) > 20000 and open(out, "rb").read(12)[4:8] == b"ftyp"
    if not ok and os.path.exists(out): os.remove(out)
    print("download", r["id"], ok); return ok
for k, v in fmts.items():
    for r in v["refs"]: r["has_file"] = resolve(r)
    # best winners first; cap 2 per brand; keep 5
    rs = sorted(v["refs"], key=lambda r: -(r["days"] or 0)); out, cnt = [], {}
    for r in rs:
        b = r["brand"].split(" (")[0]
        if cnt.get(b, 0) >= 2 or not r["has_file"]: continue
        cnt[b] = cnt.get(b, 0) + 1; out.append(r)
    v["refs"] = out[:5]
json.dump(list(fmts.values()), open(f"{W}/final.json", "w"), indent=1)
for v in sorted(fmts.values(), key=lambda v: len(v["refs"])):
    print(len(v["refs"]), len({r['brand'] for r in v['refs']}), v["stage"], v["name"])
print(len(fmts), "formats", sum(len(v["refs"]) for v in fmts.values()), "refs")

import json, re, os, glob
exec(open("cluster_map.py").read())
M.update({
 "Stop-Motion Product Build": ["Flat-Lay Build Stop-Motion","Object Stop-Motion"],
 "De-Influencing (Don't Buy That, Buy This)": ["De-Influencing Swap Routine"],
 "Brand Blunder Confession": ["Brand Blunder Confession (Pricing Mistake)"],
 "Callout Montage (If You're X, This Is For You)": ["Age-Gated Callout Montage"],
 "Good-Deed Vlog (Giving It Away)": ["Good-Deed Donation Vlog"],
})
DROP = {"Occasion Matchmaker","History Lesson Timeline"}
rows = json.load(open("new_rows.json"))
ads = {}
for f in glob.glob("F*_ads.json"):
    t = f.split("_")[0]
    d = json.load(open(f))
    for i, a in (d.items() if isinstance(d, dict) else [(x["id"], x) for x in d]): ads[(t, str(i))] = a
inv = {c: k for k, v in M.items() for c in v}
out = {}
for r in rows:
    k = inv.get(r["name"])
    if not k or k in DROP: continue
    a = ads.get((r["task"], str(r["id"])), {})
    sheet = f"sheets/{r['task']}_{r['id']}.jpg"; vid = f"vids/{r['task']}_{r['id']}.mp4"
    out.setdefault(k, []).append({"id": str(r["id"]), "task": r["task"], "cand_name": r["name"], "def": r["definition"], "brand": r["brand"],
      "days": r["days"], "started": r["started"], "last": r["last"], "rank": a.get("rank"), "dup": a.get("dup"), "page_active_ads": a.get("page_active_ads"),
      "domain": a.get("domain"), "ad_text": (a.get("ad_text") or "")[:200], "sheet": sheet if os.path.exists(sheet) else None, "video": vid if os.path.exists(vid) else None,
      "wh_link": f"https://app.winninghunter.com/ad/{r['id']}?platform=meta", "stage": r["stage"]})
json.dump(out, open("cands.json","w"), indent=1)
for k, v in sorted(out.items(), key=lambda x: -len(x[1])): print(len(v), len({x['brand'] for x in v}), k)
print(len(out), sum(map(len, out.values())))

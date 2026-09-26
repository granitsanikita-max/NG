#!/usr/bin/env python3
"""img_drive_jobs.py TASK... -> appends jobs to img_drive_jobs.json: [folder, filename, url, id] (skips ids already queued)"""
import json, sys, os, re
S = os.path.dirname(os.path.abspath(__file__))
fn = f"{S}/img_drive_jobs.json"
jobs = json.load(open(fn)) if os.path.exists(fn) else []
have = {j[3] for j in jobs}
for t in sys.argv[1:]:
    for e in json.load(open(f"{S}/hunt2/{t}.json")):
        for m in e.get("matches", []):
            if m["id"] in have: continue
            safe = lambda s: re.sub(r'[\\/:*?"<>|]', '-', s)
            jobs.append([safe(e["format"]), safe(f"{m.get('days_running','')}d - {m.get('advertiser','')} - {m['id']}.jpg"), m.get("image_url", ""), m["id"]])
            have.add(m["id"])
json.dump(jobs, open(fn, "w"), indent=0)
print(len(jobs), "jobs;", sum(1 for j in jobs if not j[2]), "without url;", sum('fbcdn' in j[2] for j in jobs), "fbcdn")

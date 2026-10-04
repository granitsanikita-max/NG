import json, re, os
W = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(f"{W}/final.json")); jobs = []
def clean(s): return re.sub(r'[\\/:*?"<>|]+', '-', s).strip()
for f in F:
    for r in f["refs"]:
        if r.get("video_url"):
            jobs.append([clean(f["name"]), f"{clean(r['brand'])[:40]} - {r['id']}.mp4", r["video_url"], r["id"], False])
json.dump(jobs, open("/home/user/NG/video-formats-hunt/drive_jobs.json", "w"), indent=0)
print(len(jobs))

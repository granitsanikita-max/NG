# Runs INSIDE the Composio sandbox. Backs up hook example videos to Google Drive (resumable, restart-safe).
import os, json, time, subprocess, requests, re
from concurrent.futures import ThreadPoolExecutor
BK = os.environ.get("BACKEND_URL", "https://backend.composio.dev") + "/api/v3/tool_router/internal/proxy_execute"
KEY = os.environ["COMPOSIO_WORKBENCH_ACCESS_KEY"]
JOBS_URL = "https://raw.githubusercontent.com/granitsanikita-max/NG/claude/vigilant-franklin-axtubn/visual-hooks-library/board/drive_jobs.json"
ROOT_NAME = "Visual Hooks Library - Saved Videos"
ST = "/mnt/files/vh_state.json"; LOG = "/mnt/files/vh_log.txt"
TMP = "/home/user/vhtmp"; os.makedirs(TMP, exist_ok=True)
def px(method, url, body=None, headers=None, query=None):
    params = [{"name": k, "value": str(v), "type": "header"} for k, v in (headers or {}).items()]
    params += [{"name": k, "value": str(v), "type": "query"} for k, v in (query or {}).items()]
    p = {"toolkit_slug": "googledrive", "endpoint": url, "method": method}
    if params: p["parameters"] = params
    if body is not None: p["body"] = body
    for a in range(4):
        r = requests.post(BK, json=p, headers={"x-session-access-key": KEY, "Content-Type": "application/json"}, timeout=120)
        if r.status_code < 500: return r.json()
        time.sleep(3 * (a + 1))
    return r.json()
def log(s):
    with open(LOG, "a") as f: f.write(time.strftime("%H:%M:%S ") + s + "\n")
def load():
    return json.load(open(ST)) if os.path.exists(ST) else {"root": None, "folders": {}, "done": {}, "fail": {}}
def save(st): json.dump(st, open(ST + ".tmp", "w")); os.replace(ST + ".tmp", ST)
def q(query):
    out, tok = [], None
    while True:
        qp = {"q": query, "fields": "nextPageToken,files(id,name,size)", "pageSize": "1000"}
        if tok: qp["pageToken"] = tok
        d = px("GET", "https://www.googleapis.com/drive/v3/files", query=qp).get("data") or {}
        out += d.get("files", []); tok = d.get("nextPageToken")
        if not tok: return out
def mkfolder(name, parent=None):
    body = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    if parent: body["parents"] = [parent]
    return px("POST", "https://www.googleapis.com/drive/v3/files", body=body)["data"]["id"]
def sync(st):
    """Rebuild state from Drive itself (survives resets, never duplicates)."""
    if not st["root"]:
        r = q(f"name = '{ROOT_NAME}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false and 'root' in parents")
        st["root"] = r[0]["id"] if r else mkfolder(ROOT_NAME)
    for f in q(f"'{st['root']}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"):
        st["folders"][f["name"]] = f["id"]
    for name, fid in list(st["folders"].items()):
        for f in q(f"'{fid}' in parents and trashed = false"):
            m = re.search(r"- (\d+)\.mp4$", f["name"])
            if m and int(f.get("size") or 0) > 20000: st["done"][m.group(1)] = f["id"]
    save(st)
def fetch(src, organic, out):
    if organic:
        subprocess.run(["yt-dlp", "-q", "-f", "b[height<=1080]/b", "-o", out, src], capture_output=True, timeout=240)
    else:
        with requests.get(src, stream=True, timeout=180) as r:
            if r.status_code != 200: return False
            with open(out, "wb") as f:
                for c in r.iter_content(1 << 20): f.write(c)
    return os.path.exists(out) and os.path.getsize(out) > 20000
def upload(path, name, parent):
    d = px("POST", "https://www.googleapis.com/upload/drive/v3/files", body={"name": name, "parents": [parent]},
           headers={"X-Upload-Content-Type": "video/mp4"}, query={"uploadType": "resumable"})
    loc = (d.get("headers") or {}).get("location")
    if not loc: raise Exception("no session: " + str(d)[:200])
    with open(path, "rb") as f:
        r = requests.put(loc, data=f, headers={"Content-Type": "video/mp4"}, timeout=600)
    r.raise_for_status(); return r.json()["id"]
def one(job, st):
    folder, name, src, vid, organic = job
    if vid in st["done"]: return vid, "have"
    out = f"{TMP}/{vid}.mp4"
    try:
        if not fetch(src, organic, out): return vid, "fetch-fail"
        fid = upload(out, name, st["folders"][folder])
        st["done"][vid] = fid; return vid, "ok"
    except Exception as e:
        return vid, "err " + str(e)[:150]
    finally:
        if os.path.exists(out): os.remove(out)
def run():
    jobs = requests.get(JOBS_URL, timeout=60).json()
    st = load(); sync(st)
    for fname in sorted({j[0] for j in jobs}):
        if fname not in st["folders"]: st["folders"][fname] = mkfolder(fname, st["root"])
    save(st)
    todo = [j for j in jobs if j[3] not in st["done"]]
    log(f"start: {len(jobs)} jobs, {len(todo)} to do")
    with ThreadPoolExecutor(6) as ex:
        for vid, res in ex.map(lambda j: one(j, st), todo):
            if res != "ok": st["fail"][vid] = res
            else: st["fail"].pop(vid, None)
            save(st); log(f"{vid} {res}")
    log(f"END done={len(st['done'])} fail={len(st['fail'])}")
if __name__ == "__main__":
    run()

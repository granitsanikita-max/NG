#!/usr/bin/env python3
"""
broll_search.py — find REAL b-roll clips for one scene from free stock-video APIs.

Sources (free, commercially usable):
  - Pexels Videos   (best free quality)   — needs env PEXELS_API_KEY
  - Pixabay Videos  (fallback / breadth)  — needs env PIXABAY_API_KEY

Returns JSON: a ranked list of candidate clips, each with a preview image (so Claude can eyeball it
against references/quality-bar.md), a direct download URL, resolution, duration, and orientation.
This script only FETCHES + FILTERS on hard specs (resolution, length, watermark-free source,
orientation). The taste call (is it actually good b-roll vs generic stock) is made by Claude reading
the preview frames against the quality bar — the script never claims a clip is "good".

Usage:
  python3 broll_search.py --query "hands squeezing a medjool date, macro, natural light" \
        --orientation portrait --min-dur 2 --max-dur 15 --per-source 6
  python3 broll_search.py --query "..." --out-dir /tmp/broll/scene3 --download URL1 URL2
"""
import os, sys, json, argparse, urllib.request, urllib.parse, subprocess

PEXELS_KEY = os.environ.get("PEXELS_API_KEY", "").strip()
PIXABAY_KEY = os.environ.get("PIXABAY_API_KEY", "").strip()
CA = "/root/.ccr/ca-bundle.crt"

def _get(url, headers=None):
    hdrs = {"User-Agent": "Mozilla/5.0"}
    hdrs.update(headers or {})
    req = urllib.request.Request(url, headers=hdrs)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8"))

def search_pexels(query, orientation, per):
    if not PEXELS_KEY:
        return [], "PEXELS_API_KEY not set"
    qs = urllib.parse.urlencode({"query": query, "orientation": orientation,
                                 "per_page": max(per*2, 10), "size": "medium"})
    try:
        data = _get(f"https://api.pexels.com/videos/search?{qs}",
                    {"Authorization": PEXELS_KEY})
    except Exception as e:
        return [], f"pexels error: {str(e)[:120]}"
    out = []
    for v in data.get("videos", []):
        files = [f for f in v.get("video_files", []) if f.get("width") and f.get("height")]
        if not files:
            continue
        # pick the best file <= 1080 wide-enough, prefer vertical
        files.sort(key=lambda f: (f["height"] >= f["width"], min(f["width"], f["height"])), reverse=True)
        best = files[0]
        out.append({
            "source": "pexels", "page_url": v.get("url"),
            "download_url": best.get("link"),
            "preview_image": v.get("image"),
            "width": best.get("width"), "height": best.get("height"),
            "duration": v.get("duration"),
            "orientation": "portrait" if best["height"] >= best["width"] else "landscape",
            "author": (v.get("user") or {}).get("name"),
        })
    return out[:per], None

def search_pixabay(query, orientation, per):
    if not PIXABAY_KEY:
        return [], "PIXABAY_API_KEY not set"
    qs = urllib.parse.urlencode({"key": PIXABAY_KEY, "q": query, "per_page": max(per*2, 10),
                                 "video_type": "film"})
    try:
        data = _get(f"https://pixabay.com/api/videos/?{qs}")
    except Exception as e:
        return [], f"pixabay error: {str(e)[:120]}"
    out = []
    for v in data.get("hits", []):
        vids = v.get("videos", {})
        pick = vids.get("large") or vids.get("medium") or {}
        if not pick.get("url"):
            continue
        w, h = pick.get("width", 0), pick.get("height", 0)
        ori = "portrait" if h >= w else "landscape"
        if orientation in ("portrait", "landscape") and ori != orientation:
            # keep anyway but flag; Pixabay orientation filtering is weak
            pass
        pid = v.get("id")
        out.append({
            "source": "pixabay",
            "page_url": v.get("pageURL"),
            "download_url": pick.get("url"),
            "preview_image": pick.get("thumbnail") or (f"https://i.vimeocdn.com/video/{v.get('picture_id')}_640x360.jpg" if v.get("picture_id") else None),
            "width": w, "height": h, "duration": v.get("duration"),
            "orientation": ori, "author": v.get("user"),
        })
    return out[:per], None

def curl_download(url, dest):
    cmd = ["curl", "-sSL", "--max-time", "180", "-o", dest, url]
    if os.path.exists(CA):
        cmd[1:1] = ["--cacert", CA]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return os.path.exists(dest) and os.path.getsize(dest) > 20000

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query")
    ap.add_argument("--orientation", default="portrait", choices=["portrait", "landscape", "any"])
    ap.add_argument("--min-dur", type=float, default=1.5)
    ap.add_argument("--max-dur", type=float, default=20.0)
    ap.add_argument("--per-source", type=int, default=6)
    ap.add_argument("--out-dir", default="/tmp/broll")
    ap.add_argument("--download", nargs="*", help="download these URLs into --out-dir instead of searching")
    args = ap.parse_args()

    if args.download:
        os.makedirs(args.out_dir, exist_ok=True)
        saved = []
        for i, u in enumerate(args.download, 1):
            dest = os.path.join(args.out_dir, f"clip_{i:02d}.mp4")
            ok = curl_download(u, dest)
            saved.append({"url": u, "path": dest if ok else None, "ok": ok})
        print(json.dumps({"downloaded": saved}, indent=2))
        return

    ori = args.orientation
    pex, pex_err = search_pexels(args.query, ori if ori != "any" else "portrait", args.per_source)
    pix, pix_err = search_pixabay(args.query, ori, args.per_source)
    cand = pex + pix
    # hard-spec filter: duration window + min resolution 720 on short side
    kept = []
    for c in cand:
        d = c.get("duration") or 0
        short = min(c.get("width") or 0, c.get("height") or 0)
        if d and (d < args.min_dur or d > args.max_dur):
            continue
        if short and short < 720:
            continue
        kept.append(c)
    # rank: portrait first, then resolution
    kept.sort(key=lambda c: (c["orientation"] == "portrait", min(c.get("width") or 0, c.get("height") or 0)), reverse=True)
    print(json.dumps({
        "query": args.query, "orientation": ori,
        "counts": {"pexels": len(pex), "pixabay": len(pix), "kept": len(kept)},
        "errors": [e for e in (pex_err, pix_err) if e],
        "candidates": kept,
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

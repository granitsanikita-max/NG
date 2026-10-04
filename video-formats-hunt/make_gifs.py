import json, os, subprocess
W = os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{W}/gifs", exist_ok=True)
def mk(src, out, t, fps, w, colors):
    vf = f"fps={fps},scale={w}:-2:flags=lanczos,split[a][b];[a]palettegen=max_colors={colors}:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-t", str(t), "-i", src, "-vf", vf, "-loop", "0", out], check=True)
    return os.path.getsize(out)
for f in json.load(open(f"{W}/final.json")):
    for r in f["refs"]:
        out = f"{W}/gifs/{r['id']}.gif"
        if os.path.exists(out) and os.path.getsize(out) < 5_800_000: continue
        for cfg in [(8, 10, 300, 128), (8, 8, 270, 96), (6, 8, 240, 64)]:
            if mk(f"{W}/{r['file']}", out, *cfg) < 5_800_000: break
        print(r["id"], os.path.getsize(out))

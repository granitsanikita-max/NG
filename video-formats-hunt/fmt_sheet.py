#!/usr/bin/env python3
"""fmt_sheet.py <video.mp4> <out.jpg>  -> 12 frames spread across the WHOLE ad (3 rows x 4), timestamps labelled; prints duration."""
import sys, subprocess, json, os
from PIL import Image, ImageDraw
v, out = sys.argv[1], sys.argv[2]
dur = float(json.loads(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","json",v],capture_output=True,text=True).stdout)["format"]["duration"])
ts = [min(dur-0.1, 0.3 + i*(dur-0.6)/11) for i in range(12)]
fr = []
for t in ts:
    p = subprocess.run(["ffmpeg","-v","error","-ss",f"{t:.2f}","-i",v,"-frames:v","1","-vf","scale=240:-2","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
    if p:
        import io; fr.append((t, Image.open(io.BytesIO(p)).convert("RGB")))
if not fr: sys.exit("no frames")
w = 240; h = max(i.height for _, i in fr)
c = Image.new("RGB", (4*w, 3*(h+18)), "white"); d = ImageDraw.Draw(c)
for k, (t, im) in enumerate(fr):
    x, y = (k % 4)*w, (k//4)*(h+18)
    d.text((x+4, y+2), f"{t:.1f}s / {dur:.0f}s", fill="red"); c.paste(im, (x, y+18))
c.save(out, quality=72); print(f"{dur:.1f}")

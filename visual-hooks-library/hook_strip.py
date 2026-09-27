#!/usr/bin/env python3
"""hook_strip.py <video> <out.jpg> [height] : 7 frames at 0,0.5,...,3.0s side by side, labelled (the visual hook window)."""
import sys, subprocess, os, tempfile
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]; H = int(sys.argv[3]) if len(sys.argv) > 3 else 300
ts = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
tiles = []
with tempfile.TemporaryDirectory() as td:
    for t in ts:
        fn = f"{td}/{t}.jpg"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-vf", f"scale=-2:{H}", "-q:v", "4", fn])
        if os.path.exists(fn): tiles.append((t, Image.open(fn).convert("RGB")))
if not tiles: sys.exit(2)
W = sum(i.width for _, i in tiles) + 4 * (len(tiles) - 1)
sh = Image.new("RGB", (W, H + 18), "white"); d = ImageDraw.Draw(sh); x = 0
for t, im in tiles:
    sh.paste(im, (x, 18)); d.text((x + 3, 3), f"{t:.1f}s", fill="black"); x += im.width + 4
sh.save(out, quality=78)

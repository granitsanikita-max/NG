#!/usr/bin/env python3
"""contact_sheet.py <video.mp4> <out.jpg> [opening_frame_out.jpg]
Grabs frames at 0.5s, 2s, 5s, 10s and mid-point into one labeled sheet (for visual verification)."""
import sys, subprocess, json, os, imageio_ffmpeg
from PIL import Image, ImageDraw
ff = imageio_ffmpeg.get_ffmpeg_exe(); src, out = sys.argv[1], sys.argv[2]
r = subprocess.run([ff, '-i', src], capture_output=True, text=True).stderr
dur = 0.0
import re
m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
if m: dur = int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))
ts = [t for t in [0.5, 2, 5, 10, dur/2] if t < max(dur - 0.2, 0.6)]
frames = []
for t in ts:
    fn = out + f'.{t:.1f}.jpg'
    subprocess.run([ff, '-y', '-ss', str(t), '-i', src, '-frames:v', '1', '-q:v', '4', fn], capture_output=True)
    if os.path.exists(fn): frames.append((t, Image.open(fn).convert('RGB')))
if not frames: sys.exit(2)
H = 480
tiles = [(t, im.resize((int(im.width * H / im.height), H))) for t, im in frames]
W = sum(im.width for _, im in tiles) + 10 * (len(tiles) - 1)
sheet = Image.new('RGB', (W, H + 30), 'white'); d = ImageDraw.Draw(sheet); x = 0
for t, im in tiles:
    sheet.paste(im, (x, 30)); d.text((x + 5, 8), f'{t:.1f}s', fill='black'); x += im.width + 10
sheet.save(out, quality=80)
if len(sys.argv) > 3: frames[0][1].save(sys.argv[3], quality=90)
for t, _ in frames: os.remove(out + f'.{t:.1f}.jpg')
print(f'ok dur={dur:.1f}s frames={len(frames)}')

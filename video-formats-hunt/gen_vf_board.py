#!/usr/bin/env python3
"""final.json + gifs/ + vf_drive.json -> vfboard/frame_<key>.svg, header.svg, plan.json, frames.json
New-format section of the Video Ad Formats board, placed right of the existing frames (x >= 10600)."""
import json, os, html, math, re
from PIL import Image
W = os.path.dirname(os.path.abspath(__file__)); OUT = f"{W}/vfboard"; os.makedirs(OUT, exist_ok=True)
F = json.load(open(f"{W}/final.json"))
DRIVE = json.load(open(f"{W}/vf_drive.json")) if os.path.exists(f"{W}/vf_drive.json") else {}
STAGES = [("TOF", "n_TOF", "NEW · Top of Funnel", "Cold audiences. Stop the scroll and earn attention.", "#c6dcff", "#305bab"),
          ("TOF→MOF", "n_TOF_MOF", "NEW · Top to Middle", "Cold-to-warm. Entertain or inspire, then start selling.", "#e3d7ff", "#5a3aa8"),
          ("MOF", "n_MOF", "NEW · Middle of Funnel", "Warm audiences. Show the product, build desire and trust.", "#fff6b6", "#8a6300"),
          ("MOF→BOF", "n_MOF_BOF", "NEW · Middle to Bottom", "Warm-to-hot. Product + offer, push to buy.", "#ffe0c2", "#a14d00"),
          ("BOF", "n_BOF", "NEW · Bottom of Funnel", "Hot / retargeting. Offer, urgency, proof, close.", "#f8d3af", "#9b4a08")]
INK, BODY, CARD = "#1a1a1a", "#595959", "#f7f7f7"
FONT = 'font-family="noto_sans"'
X0, Y0, PAD, GAP = 10600, 380, 64, 64
CW = 1964; FW = PAD * 2 + 2 * CW + GAP
SLOTW, SLOTGAP, SLOTH, LABH = 360, 24, 640, 120
TXW = CW - 64
def esc(s): return html.escape(str(s or ""), quote=True)
def est_h(h, font, width=TXW):
    paras = re.findall(r"<p>(.*?)</p>", h) or [h]; cpl = width / (font * 0.52)
    return int(sum(max(1, math.ceil(len(re.sub(r"<[^>]+>", "", html.unescape(p))) / cpl)) for p in paras) * font * 1.45 + len(paras) * font * 0.9) + 10
def stat(r):
    if r.get("platform") == "tiktok" and r.get("likes"): return f"TikTok ad · {r['likes']/1000:.0f}k likes"
    return f"Meta ad · {r['days']} days live" if r.get("days") else "Meta ad · still running"
def card(x, y, f, n, bg, fg, plan, key):
    L = [f'<text x="{x+32}" y="{y+70}" {FONT} font-size="38" font-weight="bold" fill="{INK}">N{n}  {esc(f["name"])}</text>']
    cx, cy = x + 32, y + 92
    nb = len({r['brand'] for r in f['refs']})
    for label, b, c, w in [(f["stage"], bg, fg, 40 + len(f["stage"]) * 13), ("NEW · from 7-10 fig brands", "#1a1a1a", "#ffffff", 300),
                           (f"{len(f['refs'])} winning ad{'s' if len(f['refs'])!=1 else ''} · {nb} brand{'s' if nb!=1 else ''}", "#ffffff", "#595959", 290)]:
        L.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="38" rx="19" fill="{b}" stroke="{"#e7e7e7" if b=="#ffffff" else "none"}" data-content="&lt;b&gt;{esc(label)}&lt;/b&gt;" data-text-color="{c}" data-font-size="18" data-font-family="noto_sans" />')
        cx += w + 12
    how = " ".join(f"{i+1}) {esc(s)}" for i, s in enumerate(f["how"]))
    body = (f"<p><b>What it is:</b> {esc(f['definition'])}</p><p><b>Why it works:</b> {esc(f['why'])}</p>"
            f"<p><b>How to make one:</b> {how}</p><p><b>Closest format already on the board:</b> {esc(f['closest_existing'])}</p>")
    bh = est_h(body, 21)
    L.append(f'<textArea x="{x+32}" y="{cy+56}" width="{TXW}" height="{bh}" {FONT} font-size="21" fill="{BODY}">{html.escape(body, quote=False)}</textArea>')
    gy = cy + 56 + bh + 24
    for k, r in enumerate(f["refs"]):
        sx = x + 32 + k * (SLOTW + SLOTGAP)
        L.append(f'<rect x="{sx}" y="{gy}" width="{SLOTW}" height="{SLOTH}" rx="8" fill="#1a1a1a" stroke="none" />')
        gif = f"gifs/{r['id']}.gif"; w0, h0 = Image.open(f"{W}/{gif}").size
        h = min(SLOTH, round(h0 * SLOTW / w0)); w = round(w0 * h / h0) if h == SLOTH else SLOTW
        plan.append({"frame": key, "file": gif, "cx": sx + SLOTW // 2, "cy": gy + SLOTH // 2, "width": w, "fmt": f["name"], "id": r["id"]})
        wh = f'https://app.winninghunter.com/ad/{r["id"]}?platform={"tiktok" if r.get("platform")=="tiktok" else "meta"}'
        links = (f'<a href="{wh}">▶ Watch (WH)</a>' if r.get("platform") == "tiktok" else
                 f'<a href="https://www.facebook.com/ads/library/?id={r["id"]}">▶ Ad Library</a>  ·  <a href="{wh}">WH</a>')
        if r["id"] in DRIVE: links += f'  ·  <a href="{esc(DRIVE[r["id"]])}">💾 Saved copy</a>'
        lab = f"<p><b>{k+1}  {esc(r['brand'][:30])}</b></p><p>{esc(stat(r))}</p><p>{links}</p>"
        L.append(f'<textArea x="{sx}" y="{gy+SLOTH+8}" width="{SLOTW}" height="{LABH-16}" {FONT} font-size="16" fill="{INK}">{html.escape(lab, quote=False)}</textArea>')
    return L, gy + SLOTH + LABH - y + 24
plan, frames, y0, n = [], [], Y0, 0
for st, key, title, desc, bg, fg in STAGES:
    items = sorted([f for f in F if f["stage"] == st], key=lambda f: (-len(f["refs"]), f["name"]))
    if not items: continue
    cards, y = [], 300
    for i in range(0, len(items), 2):
        hs, rl = [], []
        for c, f in enumerate(items[i:i + 2]):
            n += 1; x = PAD + c * (CW + GAP); ls, ch = card(x, y, f, n, bg, fg, plan, key); hs.append(ch); rl.append((x, ls))
        rh = max(hs)
        for x, ls in rl: cards.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{rh}" rx="16" fill="{CARD}" stroke="none" />'); cards += ls
        y += rh + GAP
    FH = y + PAD - GAP + 40
    out = ['<svg xmlns="http://www.w3.org/2000/svg">', f'<g id="{key}" transform="translate({X0},{y0})" data-frame="{esc(title)}">',
           f'<rect data-type="frame" x="0" y="0" width="{FW}" height="{FH}" fill="#ffffff" data-title="{esc(title)}" />',
           f'<text x="{PAD}" y="{PAD+67}" {FONT} font-size="67" font-weight="bold" fill="{INK}">{esc(title)}</text>',
           f'<text x="{PAD}" y="{PAD+127}" {FONT} font-size="32" fill="{BODY}">{esc(desc)}  ({len(items)} new formats)</text>'] + cards + ['</g></svg>']
    open(f"{OUT}/frame_{key}.svg", "w").write("\n".join(out))
    frames.append({"key": key, "title": title, "x": X0, "y": y0, "w": FW, "h": FH, "cards": len(items), "images": sum(1 for p in plan if p["frame"] == key)})
    y0 += FH + 320
head = ['<svg xmlns="http://www.w3.org/2000/svg">',
        f'<text x="{X0}" y="150" {FONT} font-size="80" font-weight="bold" fill="{INK}">NEW: {n} formats from 7-10 figure brands</text>',
        f'<textArea x="{X0}" y="190" width="{FW}" height="120" {FONT} font-size="28" fill="{BODY}">Found by going through the winning video ads of ~250 brands doing $1M-$100M+/yr (Winning Hunter, Oct 2026). Only formats that are NOT already in the board on the left. Every example is a winner: Meta video ad running 30+ days and still live (late Sept 2026). Each clip loops the first 8 seconds silently right on the board; click 💾 Saved copy for the full ad with sound (permanent copy in your Google Drive), ▶ Ad Library for the live ad, WH for the Winning Hunter page.</textArea>', '</svg>']
open(f"{OUT}/header.svg", "w").write("\n".join(head))
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=0); json.dump(frames, open(f"{OUT}/frames.json", "w"), indent=1)
print("cards", n, "gifs", len(plan), "drive", sum(1 for p in plan if p["id"] in DRIVE)); print([(f["key"], f["cards"], f["images"], f["h"]) for f in frames])

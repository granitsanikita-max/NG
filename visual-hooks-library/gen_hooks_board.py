#!/usr/bin/env python3
"""gen_hooks_board.py -> hboard/header.svg, hboard/frame_<key>.svg, hboard/plan.json, hboard/frames.json (reads hooks_data.json)"""
import json, os, html
H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/hboard"; os.makedirs(OUT, exist_ok=True)
data = json.load(open(f"{H}/hooks_data.json"))
DRIVE = json.load(open(f"{H}/drive_hooks.json")) if os.path.exists(f"{H}/drive_hooks.json") else {}
CATS = [("Graphic & text overlays", "g_text", "Graphic & Text Overlays", "Text, graphics and on-screen elements that stop the thumb before a word is said.", "#c6dcff", "#305bab"),
        ("Pattern interrupts", "g_pattern", "Pattern Interrupts", "A switch, cut or clash that breaks what the viewer expected to see.", "#fde2e4", "#9d1c3a"),
        ("Subject motion", "g_motion", "Subject Motion", "The person or product physically does something in frame (throw, drop, grab, move into lens).", "#fff6b6", "#8a6300"),
        ("Visual effects", "g_fx", "Visual Effects", "Editing/camera effects: zooms, speed ramps, transitions, CGI, green screen.", "#e3d7ff", "#5a3aa8"),
        ("Unique visual selection", "g_unique", "Unique Visual Selection", "An unusual subject, setting or shot choice that is instantly different from the feed.", "#adf0c7", "#0b6b34")]
INK, BODY, CARD = "#1a1a1a", "#595959", "#f7f7f7"
FONT = 'font-family="noto_sans"'
X0, PAD, GAP = 0, 64, 64
TXW, IMW = 900, 1000
CW = 32 + TXW + 40 + IMW + 32
FW = PAD * 2 + 2 * CW + GAP
MAXEX = 6
def esc(s): return html.escape(str(s or ""), quote=True)
import math, re as _re
def est_h(html_str, font, width=TXW):
    paras = _re.findall(r"<p>(.*?)</p>", html_str) or [html_str]
    cpl = width / (font * 0.52)
    lines = sum(max(1, math.ceil(len(_re.sub(r"<[^>]+>", "", html.unescape(p))) / cpl)) for p in paras)
    return int(lines * font * 1.45 + len(paras) * font * 1.2) + 10
def num(n): return f"{n/1e6:.1f}M" if n >= 1e6 else f"{n/1e3:.0f}k"

def card(x, y, d, n, bg, fg, plan, fid):
    exs = d["examples"][:MAXEX]
    ih = int(d["img_size"][1] * IMW / d["img_size"][0]) if exs else 300
    lines = []
    ty = y + 32
    lines.append(f'<text x="{x+32}" y="{ty+40}" {FONT} font-size="40" font-weight="bold" fill="{INK}">{n:02d}  {esc(d["name"])}</text>')
    cx = x + 32; cy = ty + 64
    chips = [(d["category"].title() if False else d["category"], bg, fg, 20 + len(d["category"]) * 11)]
    if d.get("kallaway"): chips.append(("Kallaway collection", "#1a1a1a", "#ffffff", 230))
    chips.append((f"{len(d['examples'])} example{'s' if len(d['examples']) != 1 else ''}", "#ffffff", "#595959", 150))
    for label, b, f, w in chips:
        lines.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="38" rx="19" fill="{b}" stroke="{"#e7e7e7" if b=="#ffffff" else "none"}" data-content="&lt;b&gt;{esc(label)}&lt;/b&gt;" data-text-color="{f}" data-font-size="18" data-font-family="noto_sans" />')
        cx += w + 12
    body = (f"<p><b>What you see (0-3s):</b> {esc(d['what_you_see'])}</p>"
            f"<p><b>Why it works:</b> {esc(d.get('why_it_works'))}</p>"
            f"<p><b>Use it for your product:</b> {esc(d.get('how_to_shoot'))}</p>")
    if d.get("aliases"): body += f"<p><b>Also called:</b> {esc(', '.join(d['aliases'][:5]))}</p>"
    bh = est_h(body, 22)
    lines.append(f'<textArea x="{x+32}" y="{cy+60}" width="{TXW}" height="{bh}" {FONT} font-size="22" fill="{BODY}">{html.escape(body, quote=False)}</textArea>')
    ey = cy + 60 + bh + 40
    if exs:
        ex_lines = []
        for k, e in enumerate(exs, 1):
            stat = (f"TikTok · {num(e['likes'])} likes") if e.get("likes") else (f"Meta ad · {e['days']} days live" if e.get("days") else ("TikTok" if e.get("platform") == "tiktok" else "Meta ad"))
            adv = esc((e.get("advertiser") or "").strip()[:32])
            s = f'<b>{k}</b>  <a href="{esc(e["link"])}">▶ Watch</a>  ·  ' + (f'{adv}  ·  ' if adv else '') + stat
            if e.get("platform") == "tiktok" and "media.winninghunter.com" in (e.get("video_url") or ""):
                s += f'  ·  <a href="{esc(e["video_url"])}">🎬 Video</a>'
            dl = DRIVE.get(e["id"])
            if dl: s += f'  ·  <a href="{esc(dl)}">💾 Saved copy</a>'
            ex_lines.append(s)
        exh = "<p><b>Examples</b> (numbers match the strips on the right)</p>" + "".join("<p>"+l+"</p>" for l in ex_lines)
        eh = est_h(exh, 20)
        lines.append(f'<textArea x="{x+32}" y="{ey}" width="{TXW}" height="{eh}" {FONT} font-size="20" fill="{INK}">{html.escape(exh, quote=False)}</textArea>')
        ey += eh
        ix = x + 32 + TXW + 40; iy = y + 32
        lines.append(f'<rect x="{ix}" y="{iy}" width="{IMW}" height="{ih}" rx="6" fill="#ffffff" stroke="none" />')
        plan.append({"frame": fid, "file": d["img"], "cx": round(ix + IMW / 2), "cy": round(iy + ih / 2), "width": IMW, "name": d["name"]})
    else:
        lines.append(f'<rect x="{x+32+TXW+40}" y="{y+32}" width="{IMW}" height="300" rx="6" fill="#ffffff" stroke="none" data-content="No verified viral example found yet." data-text-color="#b0b0b0" data-font-size="24" data-font-family="noto_sans" />')
    ch = max(ey - y + 40, ih + 64, 700)
    return lines, ch

head = ['<svg xmlns="http://www.w3.org/2000/svg">',
        f'<text x="{X0}" y="90" {FONT} font-size="90" font-weight="bold" fill="{INK}">Visual Hooks Library</text>',
        f'<textArea x="{X0}" y="130" width="{FW}" {FONT} font-size="30" fill="{BODY}">Every visual hook format we could find for the first 3 seconds of a video ad, sorted into Kallaway\'s 5 categories. Each card: what you see, why it works, how to use it for your product, and real viral / long-running examples shown frame by frame (0.0s to 3.0s). Click ▶ Watch to open the example.</textArea>']
lx = X0
for cat, key, title, desc, bg, fg in CATS:
    w = 40 + len(title) * 14
    head.append(f'<rect x="{lx}" y="230" width="{w}" height="52" rx="26" fill="{bg}" stroke="none" data-content="&lt;b&gt;{esc(title)}&lt;/b&gt;" data-text-color="{fg}" data-font-size="22" data-font-family="noto_sans" />')
    lx += w + 20
head.append('</svg>'); open(f"{OUT}/header.svg", "w").write("\n".join(head))

plan, frames = [], []
y0, n = 420, 0
for cat, key, title, desc, bg, fg in CATS:
    items = [d for d in data if d["category"] == cat]
    items.sort(key=lambda d: (-min(len(d["examples"]), MAXEX), not d.get("kallaway"), d["name"]))
    out_cards, rows_h, cur = [], [], []
    y = 300
    for i in range(0, len(items), 2):
        row = items[i:i + 2]; hs = []; row_lines = []
        for c, d in enumerate(row):
            n += 1
            x = PAD + c * (CW + GAP)
            ls, ch = card(x, y, d, n, bg, fg, plan, key)
            hs.append(ch); row_lines.append((x, ls))
        rh = max(hs)
        for x, ls in row_lines:
            out_cards.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{rh}" rx="16" fill="{CARD}" stroke="none" />')
            out_cards += ls
        y += rh + GAP
    FH = y + PAD - GAP + 40
    out = ['<svg xmlns="http://www.w3.org/2000/svg">', f'<g id="{key}" transform="translate({X0},{y0})" data-frame="{esc(title)}">',
           f'<rect data-type="frame" x="0" y="0" width="{FW}" height="{FH}" fill="#ffffff" data-title="{esc(title)}" />',
           f'<text x="{PAD}" y="{PAD+67}" {FONT} font-size="67" font-weight="bold" fill="{INK}">{esc(title)}</text>',
           f'<text x="{PAD}" y="{PAD+67+60}" {FONT} font-size="32" fill="{BODY}">{esc(desc)}  ({len(items)} formats)</text>'] + out_cards + ['</g></svg>']
    open(f"{OUT}/frame_{key}.svg", "w").write("\n".join(out))
    frames.append({"key": key, "title": title, "x": X0, "y": y0, "w": FW, "h": FH})
    y0 += FH + 320
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=0); json.dump(frames, open(f"{OUT}/frames.json", "w"), indent=1)
print("cards", n, "images", len(plan), [(f["key"], f["h"]) for f in frames])

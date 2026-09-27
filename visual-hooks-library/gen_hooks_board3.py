#!/usr/bin/env python3
"""gen_hooks_board3.py -> hboard3/: header.svg, frame_<key>.svg, plan.json (GIF + Kallaway-still uploads), frames.json
Cards: text column left, grid of looping 0-3s GIF clips right (3 per row) with per-clip links (original + Drive full video)."""
import json, os, html, math, re
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/hboard3"; os.makedirs(OUT, exist_ok=True)
data = [d for d in json.load(open(f"{H}/hooks_data.json")) if not d.get("dropped")]
SHOWN = json.load(open(f"{H}/play_shown.json"))
DRIVE = json.load(open(f"{H}/drive_hooks.json")) if os.path.exists(f"{H}/drive_hooks.json") else {}
EXTRA = {}  # R3 refs merged via hooks_data already
CATS = [("Graphic & text overlays", "g_text", "Graphic & Text Overlays", "Text, graphics and on-screen elements that stop the thumb before a word is said.", "#c6dcff", "#305bab"),
        ("Pattern interrupts", "g_pattern", "Pattern Interrupts", "A switch, cut or clash that breaks what the viewer expected to see.", "#fde2e4", "#9d1c3a"),
        ("Subject motion", "g_motion", "Subject Motion", "The person or product physically does something in frame (throw, drop, grab, move into lens).", "#fff6b6", "#8a6300"),
        ("Visual effects", "g_fx", "Visual Effects", "Editing/camera effects: zooms, speed ramps, transitions, CGI, green screen.", "#e3d7ff", "#5a3aa8"),
        ("Unique visual selection", "g_unique", "Unique Visual Selection", "An unusual subject, setting or shot choice that is instantly different from the feed.", "#adf0c7", "#0b6b34")]
INK, BODY, CARD = "#1a1a1a", "#595959", "#f7f7f7"
FONT = 'font-family="noto_sans"'
X0, PAD, GAP = int(os.environ.get("X0", "12000")), 64, 64
TXW, GW = 900, 1000
CW = 32 + TXW + 40 + GW + 32
FW = PAD * 2 + 2 * CW + GAP
CELLW, CELLGAP, CLIPH, LABH = 300, 50, 533, 150
def esc(s): return html.escape(str(s or ""), quote=True)
def num(n): return f"{n/1e6:.1f}M" if n >= 1e6 else f"{n/1e3:.0f}k"
def est_h(html_str, font, width=TXW):
    paras = re.findall(r"<p>(.*?)</p>", html_str) or [html_str]
    cpl = width / (font * 0.52)
    lines = sum(max(1, math.ceil(len(re.sub(r"<[^>]+>", "", html.unescape(p))) / cpl)) for p in paras)
    return int(lines * font * 1.45 + len(paras) * font * 1.2) + 10
def stat(e):
    if e.get("platform") == "tiktok_organic": return "TikTok organic · " + (f"{num(e['views'])} views" if e.get("views") else f"{num(e['likes'])} likes")
    if e.get("likes"): return f"TikTok ad · {num(e['likes'])} likes"
    return f"Meta ad · {e['days']} days live" if e.get("days") else ("TikTok ad" if e.get("platform") == "tiktok" else "Meta ad")
def card(x, y, d, n, bg, fg, plan, fid):
    L = []
    byid = {e["id"]: e for e in d["examples"]}
    exs = [byid[i] for i in SHOWN.get(d["name"], []) if i in byid]
    L.append(f'<text x="{x+32}" y="{y+72}" {FONT} font-size="40" font-weight="bold" fill="{INK}">{n:02d}  {esc(d["name"])}</text>')
    cx = x + 32; cy = y + 96
    chips = [(d["category"], bg, fg, 20 + len(d["category"]) * 11)]
    if d.get("kallaway"): chips.append(("Kallaway collection", "#1a1a1a", "#ffffff", 230))
    if exs: chips.append((f"{len(exs)} playable example{'s' if len(exs) != 1 else ''}", "#ffffff", "#595959", 250))
    if d.get("kallaway_stills"): chips.append(("+ Kallaway refs", "#ffffff", "#595959", 170))
    for label, b, f, w in chips:
        L.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="38" rx="19" fill="{b}" stroke="{"#e7e7e7" if b=="#ffffff" else "none"}" data-content="&lt;b&gt;{esc(label)}&lt;/b&gt;" data-text-color="{f}" data-font-size="18" data-font-family="noto_sans" />')
        cx += w + 12
    body = (f"<p><b>Kallaway's definition:</b> {esc(d['kallaway_def'])}</p>" if d.get("kallaway_def") else "")
    body += (f"<p><b>What you see (0-3s):</b> {esc(d['what_you_see'])}</p><p><b>Why it works:</b> {esc(d.get('why_it_works'))}</p>"
             f"<p><b>Use it for your product:</b> {esc(d.get('how_to_shoot'))}</p>")
    if d.get("aliases"): body += f"<p><b>Also called:</b> {esc(', '.join(d['aliases'][:5]))}</p>"
    if exs: body += "<p><b>How to watch:</b> the clips on the right loop the first 3 seconds. Click 💾 Full video for the whole ad with sound (saved in your Google Drive), or ▶ Original for the source.</p>"
    bh = est_h(body, 22)
    L.append(f'<textArea x="{x+32}" y="{cy+60}" width="{TXW}" height="{bh}" {FONT} font-size="22" fill="{BODY}">{html.escape(body, quote=False)}</textArea>')
    text_bottom = cy + 60 + bh
    gx0 = x + 32 + TXW + 40; gy = y + 32
    for k, e in enumerate(exs):
        r, c = divmod(k, 3)
        sx = gx0 + c * (CELLW + CELLGAP); sy = gy + r * (CLIPH + LABH)
        gif = f"gifs/{e['id']}.gif"
        w0, h0 = Image.open(f"{H}/{gif}").size
        h = min(CLIPH, round(h0 * CELLW / w0)); w = round(w0 * h / h0) if h == CLIPH else CELLW
        L.append(f'<rect x="{sx}" y="{sy}" width="{CELLW}" height="{CLIPH}" rx="6" fill="#1a1a1a" stroke="none" />')
        plan.append({"frame": fid, "file": gif, "cx": sx + CELLW // 2, "cy": sy + CLIPH // 2, "width": w, "name": d["name"], "id": e["id"], "kind": "gif"})
        adv = esc((e.get("advertiser") or "").strip()[:26]) or ("TikTok" if "tiktok" in e.get("platform", "") else "Meta")
        links = f'<a href="{esc(e["link"])}">▶ Original</a>'
        if e["id"] in DRIVE: links += f'  ·  <a href="{esc(DRIVE[e["id"]])}">💾 Full video</a>'
        lab = f"<p><b>{k+1}  {adv}</b></p><p>{esc(stat(e))}</p><p>{links}</p>"
        L.append(f'<textArea x="{sx}" y="{sy+CLIPH+8}" width="{CELLW}" height="{LABH-16}" {FONT} font-size="16" fill="{INK}">{html.escape(lab, quote=False)}</textArea>')
    rows = math.ceil(len(exs) / 3)
    gb = gy + rows * (CLIPH + LABH)
    if d.get("kallaway_stills"):
        kp = f"../figma/kref/{d['kallaway_num']:02d}.jpg"
        kw0, kh0 = Image.open(f"{H}/{kp}").size
        kw = min(GW, kw0 * 2); kh = round(kh0 * kw / kw0)
        L.append(f'<textArea x="{gx0}" y="{gb+8}" width="{GW}" height="30" {FONT} font-size="18" fill="{BODY}">{html.escape("<p><b>K</b>  Kallaway&#x27;s reference stills from his board (no links)</p>", quote=False)}</textArea>')
        L.append(f'<rect x="{gx0}" y="{gb+48}" width="{kw}" height="{kh}" rx="6" fill="#ffffff" stroke="none" />')
        plan.append({"frame": fid, "file": kp, "cx": gx0 + kw // 2, "cy": gb + 48 + kh // 2, "width": kw, "name": d["name"], "id": f"K{d['kallaway_num']}", "kind": "kref"})
        gb += 48 + kh
    ch = max(text_bottom - y + 40, gb - y + 32, 600)
    return L, ch
head = ['<svg xmlns="http://www.w3.org/2000/svg">',
        f'<text x="{X0}" y="90" {FONT} font-size="90" font-weight="bold" fill="{INK}">Visual Hooks Library</text>',
        f'<textArea x="{X0}" y="130" width="{FW}" height="90" {FONT} font-size="30" fill="{BODY}">{len(data)} visual hook formats for the first 3 seconds of a video, sorted into Kallaway&#x27;s 5 categories (all 47 from his Short-Form Lego Bricks board included). Every example clip loops its first 3 seconds right on the board; click 💾 Full video for the whole ad with sound (a permanent copy in your Google Drive), or ▶ Original for the source. Proven only: TikTok ads 50k+ likes, Meta ads live 30+ days, or viral organic TikToks (50k+ likes or 1M+ views).</textArea>']
head.append('</svg>'); open(f"{OUT}/header.svg", "w").write("\n".join(head))
plan, frames = [], []
y0, n = 420, 0
for cat, key, title, desc, bg, fg in CATS:
    items = [d for d in data if d["category"] == cat]
    items.sort(key=lambda d: (-len(SHOWN.get(d["name"], [])), not d.get("kallaway"), d["name"]))
    out_cards = []; y = 300
    for i in range(0, len(items), 2):
        row = items[i:i + 2]; hs = []; rl = []
        for c, d in enumerate(row):
            n += 1; x = PAD + c * (CW + GAP)
            ls, ch = card(x, y, d, n, bg, fg, plan, key); hs.append(ch); rl.append((x, ls))
        rh = max(hs)
        for x, ls in rl:
            out_cards.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{rh}" rx="16" fill="{CARD}" stroke="none" />'); out_cards += ls
        y += rh + GAP
    FH = y + PAD - GAP + 40
    out = ['<svg xmlns="http://www.w3.org/2000/svg">', f'<g id="{key}" transform="translate({X0},{y0})" data-frame="{esc(title)}">',
           f'<rect data-type="frame" x="0" y="0" width="{FW}" height="{FH}" fill="#ffffff" data-title="{esc(title)}" />',
           f'<text x="{PAD}" y="{PAD+67}" {FONT} font-size="67" font-weight="bold" fill="{INK}">{esc(title)}</text>',
           f'<text x="{PAD}" y="{PAD+127}" {FONT} font-size="32" fill="{BODY}">{esc(desc)}  ({len(items)} formats)</text>'] + out_cards + ['</g></svg>']
    open(f"{OUT}/frame_{key}.svg", "w").write("\n".join(out))
    frames.append({"key": key, "title": title, "x": X0, "y": y0, "w": FW, "h": FH, "cards": len(items), "images": sum(1 for p in plan if p["frame"] == key)})
    y0 += FH + 320
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=0); json.dump(frames, open(f"{OUT}/frames.json", "w"), indent=1)
print("cards", n, "uploads", len(plan), "gifs", sum(1 for p in plan if p["kind"] == "gif"), "drive links", sum(1 for d in data for i in SHOWN.get(d["name"], []) if i in DRIVE))
print([(f["key"], f["cards"], f["images"], f["h"]) for f in frames])

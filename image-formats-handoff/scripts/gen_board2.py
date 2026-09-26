#!/usr/bin/env python3
"""v2 board generator: wide cards, up to 6 winning refs each.
usage: gen_board2.py video|image  (reads formats2_<kind>.json, writes board2_<kind>/frame_<n>.svg + header.svg + plan.json)
formats2 entry: {id, name, stages, status, why, links:[...], new:bool,
                 refs:[{file, wh_link, fb_page, days, advertiser, pick:bool}]}"""
import json, sys, os, html
from PIL import Image
S = os.path.dirname(os.path.abspath(__file__))
kind = sys.argv[1]
fm = json.load(open(f"{S}/formats2_{kind}.json"))
DRIVE = json.load(open(f"{S}/drive_done.json")) if os.path.exists(f"{S}/drive_done.json") else {}
OUT = f"{S}/board2_{kind}"; os.makedirs(OUT, exist_ok=True)

SECTIONS = [
  ("TOF",     "Top of Funnel",    "Cold, stranger-facing. Stop the scroll and earn attention."),
  ("TOF,MOF", "Top to Middle",    "Works cold and warm. Hooks strangers, educates the curious."),
  ("MOF",     "Middle of Funnel", "Warm, solution-aware. Compare options, explain the mechanism, build trust."),
  ("MOF,BOF", "Middle to Bottom", "Proof that also closes. For warm-to-hot audiences."),
  ("BOF",     "Bottom of Funnel", "Hot / retargeting. Offer, urgency, proof, close."),
  ("ANY",     "Any Funnel Stage", "Pure style or distribution method. Judge each ad by its copy, not the format."),
]
CHIP = {"TOF": ("#c6dcff", "#305bab"), "MOF": ("#fff6b6", "#af7e04"), "BOF": ("#f8d3af", "#9b4a08"), "ANY": ("#e7e7e7", "#313131")}
INK, BODY, CARD, MATTE = "#1a1a1a", "#595959", "#f7f7f7", "#ffffff"
FONT = 'font-family="noto_sans"'
X0 = 6000                      # new content sits to the right of the old board; old items are deleted afterwards
COLS, PAD, GAP = 2, 64, 64
NS, SW, SH, SG = 6, 300, 520, 20
CW = 32 * 2 + NS * SW + (NS - 1) * SG          # 1964
TOPH = 220                                     # title, chips, why
CH = TOPH + SH + 16 + 44 + 8 + 30 + 20 + 80    # slots + button + advertiser + links
HEADER_H = 300
FW = PAD * 2 + COLS * CW + (COLS - 1) * GAP

def esc(s): return html.escape(str(s), quote=True)

groups = {k: [] for k, _, _ in SECTIONS}
for f in fm:
    groups[f["stages"] or "ANY"].append(f)

head = ['<svg xmlns="http://www.w3.org/2000/svg">']
title = "Video Ad Formats" if kind == "video" else "Image Ad Formats"
sub = (f"Every {'video' if kind=='video' else 'static / image'} format, sorted by funnel stage. "
       "Each card: why it works + 5-6 proven winning ads (still live, longest-running first). Click ▶ Watch to open the ad.")
head.append(f'<text x="{X0}" y="90" {FONT} font-size="90" font-weight="bold" fill="{INK}">{esc(title)}</text>')
head.append(f'<textArea x="{X0}" y="130" width="{FW}" {FONT} font-size="33" fill="{BODY}">{esc(sub)}</textArea>')
lx = X0
for code, label in [("TOF", "TOF  Top of funnel"), ("MOF", "MOF  Middle of funnel"), ("BOF", "BOF  Bottom of funnel"), ("ANY", "ANY  Any stage")]:
    bg, fg = CHIP[code]; w = 40 + len(label) * 13
    head.append(f'<rect x="{lx}" y="200" width="{w}" height="52" rx="26" fill="{bg}" stroke="none" data-content="&lt;b&gt;{esc(label)}&lt;/b&gt;" data-text-color="{fg}" data-font-size="22" data-font-family="noto_sans" />')
    lx += w + 20
for code, label in [("NEW", "NEW  format found in this hunt"), ("PICK", "YOUR PICK  ad you sent me")]:
    bg, fg = ("#adf0c7", "#0b6b34") if code == "NEW" else ("#dedaff", "#4a3ea8")
    w = 40 + len(label) * 13
    head.append(f'<rect x="{lx}" y="200" width="{w}" height="52" rx="26" fill="{bg}" stroke="none" data-content="&lt;b&gt;{esc(label)}&lt;/b&gt;" data-text-color="{fg}" data-font-size="22" data-font-family="noto_sans" />')
    lx += w + 20
head.append('</svg>')
open(f"{OUT}/header.svg", "w").write("\n".join(head))

plan, frames, advs = [], [], []
y0, num = 380, 0
for code, name, desc in SECTIONS:
    items = groups[code]
    if not items: continue
    rows = (len(items) + COLS - 1) // COLS
    FH = HEADER_H + rows * CH + (rows - 1) * GAP + PAD
    fid = "f_" + code.replace(",", "_")
    out = ['<svg xmlns="http://www.w3.org/2000/svg">', f'<g id="{fid}" transform="translate({X0},{y0})" data-frame="{esc(name)}">',
           f'<rect data-type="frame" x="0" y="0" width="{FW}" height="{FH}" fill="#ffffff" data-title="{esc(name)}" />',
           f'<text x="{PAD}" y="{PAD+67}" {FONT} font-size="67" font-weight="bold" fill="{INK}">{esc(name)}</text>']
    cx = PAD + int(len(name) * 38) + 40
    for c in code.split(","):
        bg, fg = CHIP[c]
        out.append(f'<rect x="{cx}" y="{PAD+12}" width="120" height="60" rx="30" fill="{bg}" stroke="none" data-content="&lt;b&gt;{c}&lt;/b&gt;" data-text-color="{fg}" data-font-size="33" data-font-family="noto_sans" />')
        cx += 140
    out.append(f'<text x="{PAD}" y="{PAD+67+63}" {FONT} font-size="33" fill="{BODY}">{esc(desc)}  ({len(items)} formats)</text>')
    for i, f in enumerate(items):
        num += 1
        r, c = divmod(i, COLS)
        x = PAD + c * (CW + GAP); y = HEADER_H + r * (CH + GAP)
        out.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="16" fill="{CARD}" stroke="none" />')
        out.append(f'<text x="{x+32}" y="{y+65}" {FONT} font-size="36" font-weight="bold" fill="{INK}">{num:02d}  {esc(f["name"])}</text>')
        chx = x + 32
        for st in (f["stages"] or "ANY").split(","):
            bg, fg = CHIP[st]
            out.append(f'<rect x="{chx}" y="{y+88}" width="80" height="36" rx="18" fill="{bg}" stroke="none" data-content="&lt;b&gt;{st}&lt;/b&gt;" data-text-color="{fg}" data-font-size="18" data-font-family="noto_sans" />')
            chx += 92
        if f.get("new"):
            out.append(f'<rect x="{chx}" y="{y+88}" width="90" height="36" rx="18" fill="#adf0c7" stroke="none" data-content="&lt;b&gt;NEW&lt;/b&gt;" data-text-color="#0b6b34" data-font-size="18" data-font-family="noto_sans" />')
            chx += 102
        n = len(f["refs"])
        lab = f"{n} winning refs" if n else "no verified winner yet"
        out.append(f'<rect x="{chx}" y="{y+88}" width="{40+len(lab)*11}" height="36" rx="18" fill="#ffffff" stroke="#e7e7e7" stroke-width="2" data-content="{esc(lab)}" data-text-color="#595959" data-font-size="18" data-font-family="noto_sans" />')
        out.append(f'<textArea x="{x+32}" y="{y+140}" width="{CW-64}" {FONT} font-size="22" fill="{BODY}">{esc(f["why"])}</textArea>')
        sy = y + TOPH
        refs = f["refs"][:NS]
        if not refs:
            out.append(f'<rect x="{x+32}" y="{sy}" width="{CW-64}" height="{SH}" rx="8" fill="{MATTE}" stroke="none" data-content="No live winning example verified yet." data-text-color="#b0b0b0" data-font-size="26" data-font-family="noto_sans" />')
        for k, ref in enumerate(refs):
            sx = x + 32 + k * (SW + SG)
            out.append(f'<rect x="{sx}" y="{sy}" width="{SW}" height="{SH}" rx="8" fill="{MATTE}" stroke="none" />')
            iw, ih = Image.open(f"{S}/imgs2/{ref['file']}").size
            w = min(SW - 16, (SH - 16) * iw / ih)
            plan.append({"frame": fid, "file": ref["file"], "cx": round(sx + SW / 2), "cy": round(sy + SH / 2), "width": round(w)})
            by = sy + SH + 16
            verb = "▶ Watch" if kind == "video" else "↗ View"
            days = "  ·  your pick" if ref.get("pick") else (f"  ·  {ref['days']} days live" if ref.get("days") else "")
            fill, stroke = ("#dedaff", "#4a3ea8") if ref.get("pick") else ("#ffffff", "#1a1a1a")
            content = f'<a href="{ref["wh_link"]}">{verb}</a>{days}'
            out.append(f'<rect x="{sx}" y="{by}" width="{SW}" height="44" rx="22" fill="{fill}" stroke="{stroke}" data-content="{esc(content)}" data-text-color="#1a1a1a" data-font-size="18" data-font-weight="bold" data-font-family="noto_sans" />')
            advl = ("YOUR PICK · " if ref.get("pick") else "") + ref.get("advertiser", "")
            if ref.get("fb_page"):
                advl = f'<a href="{esc(ref["fb_page"])}">{esc(advl[:34])}</a>'
            else:
                advl = esc(advl[:34])
            dl = DRIVE.get(ref["id"], {}).get("link")
            if dl:
                advl += f'  ·  <a href="{esc(dl)}">💾 Saved copy</a>'
            out.append(f'<textArea x="{sx}" y="{by+52}" width="{SW}" {FONT} font-size="16" fill="{BODY}" text-align="center">{advl}</textArea>')
            advs.append({"frame": fid, "x": sx, "y": by + 52, "id": ref["id"], "content": advl})
        # links row: extra winners + original swipe links + notion
        parts = []
        extra = f["refs"][NS:]
        if extra:
            parts.append("More winners: " + " ".join(f'<a href="{esc(e["wh_link"])}">{j+1}</a>' for j, e in enumerate(extra)))
        orig = [l for l in f.get("links", []) if "notion.so" not in l]
        if orig:
            parts.append("Original swipes: " + " ".join(f'<a href="{esc(l)}">{j+1}</a>' for j, l in enumerate(orig)))
        if f.get("id"):
            parts.append(f'<a href="https://www.notion.so/{f["id"]}">Notion page</a>')
        ly = sy + SH + 16 + 44 + 8 + 30 + 20
        out.append(f'<textArea x="{x+32}" y="{ly}" width="{CW-64}" {FONT} font-size="18" fill="{BODY}"><b>Links:</b>  {"   ·   ".join(parts) if parts else "none"}</textArea>')
    out.append('</g></svg>')
    open(f"{OUT}/frame_{fid}.svg", "w").write("\n".join(out))
    frames.append({"key": fid, "title": name, "x": X0, "y": y0, "w": FW, "h": FH, "chars": sum(map(len, out))})
    y0 += FH + 320
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=0)
json.dump(frames, open(f"{OUT}/frames.json", "w"), indent=1)
json.dump(advs, open(f"{OUT}/adv.json", "w"), indent=0)
print("cards", num, "images", len(plan), [(f["key"], f["chars"]) for f in frames])

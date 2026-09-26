#!/usr/bin/env python3
"""usage: patch_saved.py <lines.txt> <board2_dir>  ; each line: <textAreaId> <parentFrameId> <localX> <localY> <shown name...>
Prints ONE canvas_update_from_svg document updating those textAreas with the Saved-copy link. Exits 1 on any mismatch."""
import json, sys, html, os
D = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
ids = json.load(open(f"{D}/frame_ids.json")); key = {v: k for k, v in ids.items()}
fr = {f["key"]: f for f in json.load(open(f"{D}/frames.json"))}
adv = {(a["frame"], a["x"], a["y"]): a for a in json.load(open(f"{D}/adv.json"))}
groups, bad = {}, []
for ln in open(sys.argv[1]):
    p = ln.split(None, 4)
    if len(p) < 4: continue
    tid, fid, x, y = p[0], p[1], round(float(p[2])), round(float(p[3]))
    name = p[4].strip() if len(p) > 4 else ""
    k = key.get(fid)
    a = adv.get((k, x, y)) or adv.get((k, x, y + 1)) or adv.get((k, x, y - 1))
    if not a: bad.append(f"no slot for {ln.strip()}"); continue
    if name and html.escape(name, quote=True)[:20] not in a["content"] and name[:20] not in html.unescape(a["content"]):
        bad.append(f"name mismatch {tid}: board '{name}' vs {a['content'][:120]}"); continue
    groups.setdefault(k, []).append(f'<textArea data-miro-id="{tid}" x="{a["x"]}" y="{a["y"]}" width="300" font-family="noto_sans" font-size="16" fill="#595959" text-align="center">{html.escape(a["content"], quote=False)}</textArea>')
if bad:
    print("\n".join(bad), file=sys.stderr); sys.exit(1)
out = ['<svg xmlns="http://www.w3.org/2000/svg">']
for k, items in groups.items():
    f = fr[k]
    out.append(f'<g data-miro-id="{ids[k]}" transform="translate({f["x"]},{f["y"]})" data-frame="{html.escape(f["title"])}"><rect data-type="frame" x="0" y="0" width="{f["w"]}" height="{f["h"]}" fill="#ffffff" data-title="{html.escape(f["title"])}" />')
    out += items; out.append('</g>')
out.append('</svg>')
print("".join(out))
print(f"# {sum(len(v) for v in groups.values())} textAreas", file=sys.stderr)

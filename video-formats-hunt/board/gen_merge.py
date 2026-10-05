import json, re, os
D = os.path.dirname(os.path.abspath(__file__)); M = f"{D}/merge"
OLD = [  # key, old frame id, title, old height, new key
 ("TOF", "3458764685036396164", "Top of Funnel", 12324, "n_TOF"),
 ("T2M", "3458764685036783919", "Top to Middle", 3306, "n_TOF_MOF"),
 ("MOF", "3458764685036864639", "Middle of Funnel", 5310, "n_MOF"),
 ("M2B", "3458764685037213673", "Middle to Bottom", 3306, "n_MOF_BOF"),
 ("BOF", "3458764685037400959", "Bottom of Funnel", 1302, None),
 ("ANY", "3458764685036353090", "Any Funnel Stage", 1302, None)]
NEWH = {f["key"]: f["h"] for f in json.load(open(f"{D}/frames.json"))}
SEC = 220; X = 6000; y = 380; layout = []
plan = json.load(open(f"{D}/plan.json")); mplan = []
for key, fid, title, oh, nk in OLD:
    base = oh + SEC if nk else None
    h = base + NEWH[nk] - 300 if nk else oh
    layout.append({"key": key, "id": fid, "title": title, "x": X, "y": y, "h": h, "old_h": oh, "base": base, "nk": nk})
    if nk:
        dy = base - 300
        lines = open(f"{D}/frame_{nk}.svg").read().split("\n")
        body = [l for l in lines if l.startswith("<rect x=") or l.startswith("<text x=") or l.startswith("<textArea x=")]
        body = [l for l in body if 'font-size="67"' not in l and 'font-size="32"' not in l]  # drop new-frame title/desc
        shift = lambda l: re.sub(r' y="(\d+)"', lambda m: f' y="{int(m.group(1)) + dy}"', l, count=1)
        body = [shift(l) for l in body]
        n_new = sum(1 for l in body if 'width="1964"' in l)
        head = [f'<text x="64" y="{oh + 60}" font-family="noto_sans" font-size="56" font-weight="bold" fill="#1a1a1a">NEW: {n_new} more {title} formats from 7-10 figure brands</text>',
                f'<text x="64" y="{oh + 120}" font-family="noto_sans" font-size="28" fill="#595959">Found Oct 2026 in the winning ads of ~250 brands doing $1M+/yr. Each clip loops the first 8s; 💾 Saved copy = full ad with sound in your Drive.</text>']
        g = f'<g data-miro-id="{fid}" transform="translate({X},{y})" data-frame="{title}">'
        fr = f'<rect data-type="frame" x="0" y="0" width="4120" height="{h}" fill="#ffffff" data-title="{title}" />'
        starts = [i for i, l in enumerate(body) if 'width="1964"' in l]
        cards = [body[a:b] for a, b in zip(starts, starts[1:] + [len(body)])]
        chunks = [head]  # chunk 0 = section header
        for i in range(0, len(cards), 2): chunks.append(sum(cards[i:i + 2], []))
        for n, c in enumerate(chunks):
            open(f"{M}/chunk_{key}_{n}.svg", "w").write("\n".join(['<svg xmlns="http://www.w3.org/2000/svg">', g, fr] + c + ['</g></svg>']))
        for e in plan:
            if e["frame"] == nk: mplan.append(dict(e, frame=key, frame_id=fid, cy=e["cy"] + dy))
        layout[-1]["chunks"] = len(chunks); layout[-1]["cards"] = n_new
    y += h + 320
json.dump(layout, open(f"{M}/layout.json", "w"), indent=1); json.dump(mplan, open(f"{M}/plan.json", "w"), indent=0)
for l in layout: print(l["key"], l["y"], l["h"], l.get("chunks"), l.get("cards"))
print("images", len(mplan))

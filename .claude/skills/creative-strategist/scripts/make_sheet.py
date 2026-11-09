#!/usr/bin/env python3
"""Build the creative-strategy spreadsheet (the skill's main outcome) from the run files.

usage: python3 make_sheet.py <run_dir> [<brand name>]

Reads  <run>/desires.json   [{"n":1,"desire":"I want ...","segment":"..."}, ...]  (written after Step 4)
       <run>/05-angles-D<n>.md  (one per desire, the Prompt 05 output)
       <run>/ads/D#A#/image.md + prompt.md  (optional, only if images were made)
Writes <run>/creative-strategy-<brand>.xlsx  (tabs: "Testing Grid" = BBA Mass Desire output spread,
                                               "Angles" = full angle detail)
       <run>/creative-strategy-<brand>.csv   (the Angles tab, for Google Sheets / no-Excel users)
Copies text exactly from the files; it writes nothing new. Missing fields are reported, not invented.
"""
import csv, json, pathlib, re, sys

if len(sys.argv) < 2:
    sys.exit(__doc__)
run = pathlib.Path(sys.argv[1])
brand = sys.argv[2] if len(sys.argv) > 2 else run.name
dj = run / "desires.json"
if not dj.is_file():
    sys.exit(f"missing {dj}: write it after Step 4")
desires = json.loads(dj.read_text())

FIELDS = ["Angle Name", "Target Audience", "Story Arc", "Unique Problem Mechanism",
          "Unique Solution Mechanism", "Key Emotional Moment", "Headline options",
          "Awareness Level", "Funnel Stage", "Static Format", "Key Objections"]

def field(sec, name):
    m = re.search(r"\*\*%s:\*\*\s*(.*?)(?=\s*(?:·\s*)?\*\*[A-Z][A-Za-z ()0-9]*:\*\*|\n\*Pipeline|\n### |\Z)" % re.escape(name), sec, re.S)
    return m.group(1).strip() if m else ""

def headlines(sec):
    m = re.search(r"\*\*Headline options[^*]*\*\*\s*(.*?)(?=\n\*\*[A-Z]|\Z)", sec, re.S)
    if not m:
        return ""
    items = re.findall(r"^\s*\d+\.\s*(.+)$", m.group(1), re.M)
    return "\n".join(f"{i+1}. {t.strip()}" for i, t in enumerate(items)) or m.group(1).strip()

rows, problems = [], []
for d in desires:
    n = d["n"]
    f = run / f"05-angles-D{n}.md"
    if not f.is_file():
        problems.append(f"D{n}: no angle file")
        continue
    text = f.read_text()
    secs = re.split(r"^### (D%dA\d)\b.*$" % n, text, flags=re.M)
    pairs = list(zip(secs[1::2], secs[2::2]))
    if len(pairs) != 5:
        problems.append(f"D{n}: found {len(pairs)} angles, expected 5")
    for aid, sec in pairs:
        r = {"Ad ID": aid, "Desire #": n, "Mass Desire": d["desire"], "Segment": d.get("segment", "")}
        for k in FIELDS:
            r[k] = headlines(sec) if k == "Headline options" else field(sec, k)
            if not r[k] and k != "Headline options":
                problems.append(f"{aid}: missing '{k}'")
        img = run / "ads" / aid / "image.md"
        r["Image"] = re.findall(r"https?://\S+\.(?:png|jpg|jpeg|webp)", img.read_text())[-1] if img.is_file() and re.findall(r"https?://\S+\.(?:png|jpg|jpeg|webp)", img.read_text()) else ""
        sw = run / "ads" / aid / "swipe.md"
        r["Swipe source"] = (re.findall(r"https?://\S+", sw.read_text()) or [""])[0] if sw.is_file() else ""
        rows.append(r)

cols = ["Ad ID", "Desire #", "Mass Desire", "Segment"] + FIELDS + ["Swipe source", "Image",
        "Ad name", "Spend", "CTR", "CPC", "ROAS", "Winner?"]
slug = re.sub(r"[^a-z0-9]+", "-", brand.lower()).strip("-")
for r in rows:
    r["Ad name"] = f"{slug}_{r['Ad ID']}"

out_csv = run / f"creative-strategy-{slug}.csv"
with out_csv.open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    wb = Workbook()
    g = wb.active
    g.title = "Testing Grid"
    bold, fill = Font(bold=True), PatternFill("solid", fgColor="FFF2CC")
    r_i = 1
    for d in desires:
        g.cell(r_i, 1, f"MASS DESIRE {d['n']}").font = bold
        g.cell(r_i, 2, d["desire"]).font = bold
        for j, h in enumerate(["SPEND", "CTR", "CPC", "ROAS"], start=3):
            g.cell(r_i, j, h).font = bold
        for c in range(1, 7):
            g.cell(r_i, c).fill = fill
        r_i += 1
        for r in [x for x in rows if x["Desire #"] == d["n"]]:
            g.cell(r_i, 1, f"ANGLE {r['Ad ID'][-1]}")
            g.cell(r_i, 2, r["Angle Name"])
            r_i += 1
        r_i += 1
    g.column_dimensions["A"].width = 16
    g.column_dimensions["B"].width = 70
    a = wb.create_sheet("Angles")
    a.append(cols)
    for c in a[1]:
        c.font = bold
    for r in rows:
        a.append([r.get(c, "") for c in cols])
    widths = {"Mass Desire": 40, "Target Audience": 50, "Story Arc": 80, "Unique Problem Mechanism": 50,
              "Unique Solution Mechanism": 50, "Key Emotional Moment": 40, "Headline options": 50,
              "Static Format": 35, "Key Objections": 45, "Angle Name": 30}
    for i, c in enumerate(cols, start=1):
        a.column_dimensions[a.cell(1, i).column_letter].width = widths.get(c, 14)
    for row in a.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    a.freeze_panes = "C2"
    out_x = run / f"creative-strategy-{slug}.xlsx"
    wb.save(out_x)
    print("ok ->", out_x)
except ImportError:
    print("openpyxl not installed: CSV only")
print("ok ->", out_csv, f"({len(rows)} angles)")
if problems:
    print("CHECK:", "; ".join(problems))

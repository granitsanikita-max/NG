#!/usr/bin/env python3
"""Build one pass's prompt file.

usage: python3 fill.py <prompt.md> <vars.json[,more.json,...]> <out_pass_file> <output_path> [extra_note]
  (later JSON files override earlier ones: run-wide vars.json, then per-pass values)
- replaces every {{KEY}} with vars[KEY]
- drops the leading <!-- source comment -->
- appends the footer from templates/subagent-brief.md (with OUTPUT_PATH)
- exits 1 (and writes nothing) if any {{PLACEHOLDER}} is left
"""
import json, re, sys, pathlib
prompt, varsf, out, outpath = sys.argv[1:5]
extra = sys.argv[5] if len(sys.argv) > 5 else ""
skill = pathlib.Path(__file__).resolve().parent.parent
s = pathlib.Path(prompt).read_text()
s = re.sub(r"^<!--.*?-->\s*", "", s, flags=re.S)
v = {}
for f in varsf.split(","):
    v.update(json.loads(pathlib.Path(f).read_text()))
for k, val in v.items():
    s = s.replace("{{%s}}" % k, str(val))
foot = (skill / "templates/subagent-brief.md").read_text().split("## Footer (append verbatim)\n", 1)[1]
foot = foot.replace("{{OUTPUT_PATH}}", outpath)
s = s.rstrip() + "\n\n" + (extra.strip() + "\n" if extra else "") + foot
left = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", s)))
if left:
    sys.exit("UNFILLED PLACEHOLDERS: " + ", ".join(left))
pathlib.Path(out).write_text(s)
print("ok ->", out)

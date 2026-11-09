#!/usr/bin/env python3
"""Build one pass's prompt file for the creative-strategist skill.

usage: python3 fill.py <prompt.md> <vars.json>[,<more.json>...] <out_pass_file> <output_path> ["extra note"]

- merges the JSON files left to right (run-wide vars.json first, then per-pass values)
- replaces every {{KEY}} with its value
- drops the prompt file's leading <!-- source comment -->
- appends the optional extra note, then the Footer from templates/subagent-brief.md
  (with {{OUTPUT_PATH}} = <output_path>)
- exits 1 and writes nothing if any {{UPPERCASE_PLACEHOLDER}} is left unfilled
  (lowercase markers such as <n> are intentional and ignored)
"""
import json, pathlib, re, sys

if len(sys.argv) < 5:
    sys.exit(__doc__)
prompt, varsf, out, outpath = sys.argv[1:5]
extra = sys.argv[5] if len(sys.argv) > 5 else ""
skill = pathlib.Path(__file__).resolve().parent.parent

p = pathlib.Path(prompt)
if not p.is_file():
    sys.exit(f"prompt file not found: {prompt}")
s = re.sub(r"^<!--.*?-->\s*", "", p.read_text(), flags=re.S)

values = {}
for f in [x for x in varsf.split(",") if x.strip()]:
    fp = pathlib.Path(f.strip())
    if not fp.is_file():
        sys.exit(f"vars file not found: {fp}")
    values.update(json.loads(fp.read_text()))

# fill in the prompt body only (values may legitimately contain braces)
left = sorted(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", s)) - set(values))
if left:
    sys.exit("UNFILLED PLACEHOLDERS: " + ", ".join("{{%s}}" % k for k in left))
for k, v in values.items():
    s = s.replace("{{%s}}" % k, str(v))

foot = (skill / "templates" / "subagent-brief.md").read_text()
if "## Footer (append verbatim)\n" not in foot:
    sys.exit("footer section missing in templates/subagent-brief.md")
foot = foot.split("## Footer (append verbatim)\n", 1)[1].replace("{{OUTPUT_PATH}}", outpath)

s = s.rstrip() + "\n\n" + (extra.strip() + "\n" if extra else "") + foot
o = pathlib.Path(out)
o.parent.mkdir(parents=True, exist_ok=True)
o.write_text(s)
print("ok ->", o)

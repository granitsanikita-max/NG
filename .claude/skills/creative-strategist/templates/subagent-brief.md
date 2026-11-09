# Pass brief: how the orchestrator dispatches each one-by-one pass

Agent call: `subagent_type: "general-purpose"`, `model: "opus"`, `run_in_background: false`.
Prompt = the filled prompt file + this footer.

## Placeholders (fill ALL; source)
| Placeholder | Source |
|---|---|
| {{RUN_DIR}} | `<run>` absolute path |
| {{BRAND_DOCS}} | `<run>/00-intake.md`, `<run>/00-brief.md` (absolute paths) |
| {{PRODUCT}} / {{PRODUCT_SHORT}} | intake 1 (full description / 2–4 word name) |
| {{NICHE}} | brief |
| {{COMPETITOR}} / {{COMPETITOR_URL}} / {{COMPETITOR_DEMOGRAPHIC}} | intake 3 |
| {{PROBLEM_SPACE_EXAMPLES}} | intake 4 |
| {{DESIRE_NUMBER}} / {{DESIRE_TEXT}} | `04-desires.md` (the full "I want…" + segment) |
| {{PREVIOUS_ANGLE_FILES}} | already-written `05-angles-D*.md`, or "none" |
| {{AD_ID}} | D#A# |
| {{ANGLE_FILE}} / {{ANGLE_NAME}} / {{ANGLE_HEADLINE}} | `05-angles-D#.md`; headline = the chosen one of the 3 options |
| {{COMPETITOR_AD}} | `<run>/ads/D#A#/competitor.<ext>` |
| {{PRODUCT_PHOTO}} | `<run>/product.<ext>` |
| {{FUNNEL_STAGE}} | the angle's Funnel Stage (TOFU/MOFU/BOFU) |

## Footer (append verbatim)
---
You are doing ONE unit of a creative-strategy run. Give it your full attention. Other units are handled separately; don't do them.
- Read every file listed above in full before writing. Ground everything in them, plus, for web-research passes, the live sources you cite with URLs. If a product fact isn't in them, write "NOT IN DOCS" instead of inventing it.
- Product claims, offers, prices, numbers and proof: ONLY those listed in 00-brief.md.
- Write your complete output to: {{OUTPUT_PATH}}
- Then reply with only: the output path, a 3-line summary, and any NOT IN DOCS flags.

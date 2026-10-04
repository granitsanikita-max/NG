# Verify new video-ad formats + pick top-5 winners

Working dir: $S/vf2 (S = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad)
Input: cands.json = {final_format_name: [candidate ads]}. Each candidate has id, brand, days (days live), started, last (last seen),
rank, dup (duplicate count = brand scaling it), page_active_ads, def (the hunter's one-line description), sheet (12-frame contact sheet
across the WHOLE ad, path relative to vf2), video (local mp4), wh_link.
All candidates already pass the "winning" rule (Meta video, live 30+ days, still running in late Sept 2026) from 7-10 figure brands.
EXISTING_FORMATS.md = the 47 formats ALREADY on the board. A new format must be a different WHOLE-AD STRUCTURE from all 47
(not just a different hook, product or niche).

## For each format you are assigned
1. Sort candidates by strength: days desc, then dup desc, then rank asc. Read (view) the contact sheets with the Read tool,
   strongest first. For clusters with >25 candidates view at least the strongest 25; otherwise view ALL.
2. Decide per candidate: IN (the whole ad clearly is this format), or OUT (it's another format / an existing one / mixed).
   Be strict: an ad that is a plain UGC testimonial with a nicer camera is OUT.
3. Decide the format itself:
   - KEEP if it's a distinct whole-ad structure a dropshipper could copy.
   - MERGE_INTO:<other format name> if it is really the same as another new format in cands.json (say which).
   - EXISTING:<name> if it's really one of the 47 existing formats -> drop.
   You may rename to a clearer name (short, plain, "Name (Clarifier)" style).
4. Pick top5: up to 5 IN ads, best winners first (days, dup, rank). Brand diversity: max 2 per brand, prefer 1 when the
   cluster has enough brands. Only pick ads with a video file. Prefer clean, obvious examples of the format.
5. Write the format card text:
   - definition: 1-2 sentences, what the whole ad IS, beat by beat (open -> middle -> close).
   - why: 1 sentence, why it works / when to use it.
   - how: 3 short steps to make one for a dropshipping product.
   - stage: TOF / MOF / BOF / TOF→MOF / MOF→BOF / ANY.
   - closest_existing: the closest of the 47 + how this differs (1 line).
   - per top5 ad a 6-12 word "what_you_see" note.

## Output
Write vf2/verify/<AGENT_ID>.json:
{ "<final format name>": {"orig": "<name in cands.json>", "decision": "KEEP|MERGE_INTO:x|EXISTING:x",
   "definition": "...", "why": "...", "how": ["..","..",".."], "stage": "...", "closest_existing": "...",
   "in_ids": [all IN ids, best first], "out_ids": [...],
   "top5": [{"id": "...", "task": "F?", "brand": "...", "days": n, "what_you_see": "..."}],
   "need_fill": <5 - len(top5), min 0>, "fill_hint": "WH keyword / brand ideas to find more if need_fill>0" } }
Save the file incrementally after each format (so nothing is lost). Final message: one line per format: name | decision | IN count | top5 count.
Do NOT post anywhere, do not use Miro/Drive. Read-only on everything except your output file.

# Classify the VISUAL HOOK (first 3 seconds) of each video
H=/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hooks
Taxonomy (152 formats in 5 categories, with what-you-see + detection cues): $H/taxonomy_brief.txt  (read it fully first; full detail in $H/taxonomy.json).
Each grid image in your task shows 6 strips; each strip = one video's frames at 0.0s,0.5s,1.0s,...,3.0s (labels at top of each tile), headed by "#k id <ID>".
Grid -> id list mapping: $H/cgrid_index.json (or tt_cgrid_index.json for TikTok grids).
For EVERY strip decide:
- the PRIMARY visual hook format it shows in the first 3s (exact "name" from the taxonomy), and optionally a secondary one;
- confidence: "high" (clearly that hook, a textbook example someone could copy) or "medium" (it's there but not the main thing). If the opening is a plain static talking head / plain product shot with nothing visually stopping, use format "NONE".
- what_you_see: one short line describing the actual first 3 seconds (concrete, e.g. "hand throws phone at lens, cut to product").
Judge only what you SEE (motion across frames, text on screen, effects). Be strict: better NONE than a wrong label. A label only counts as high if the hook happens in the first ~1.5s and is obvious.
Write results incrementally (after every grid) with python to $H/cls_<TASK>.json as {id: {"format":..., "secondary":..., "confidence":..., "what_you_see":...}}.
View grids with the Read tool (one or two at a time). If a strip is unclear you may extract more frames: ffmpeg -ss <t> -i <video> ... (videos: ../hunt2/<id>.mp4, ../hunt/<id>.mp4, ../concepts/<id>.mp4, or $H/tt/<id>.mp4).
Keep text output minimal. Final report: counts of high / medium / NONE and the top 10 formats found.

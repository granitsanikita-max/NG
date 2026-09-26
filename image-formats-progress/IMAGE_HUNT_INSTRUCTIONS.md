# Image-format hunt: 5+ PROVEN WINNING static ads per format, visually verified
/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad = the work folder the lead session set up (it holds formats_image.json, scripts, hunt2/). Your task file is /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hunt2/<TASK>_task.json.
TODAY = 2026-09-26 (so live = lastSeen >= 2026-09-19; run length = started <= 2026-08-12, prefer <= 2026-06-28). Goal: for EACH format in your task, deliver AT LEAST 5 (aim 6-7) live static ads that
(a) visually ARE that format and (b) are proven WINNERS. Quality over speed.
Never modify Notion or Miro. Work only inside /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hunt2/. Prefix every helper file with your task name (e.g. I3_parse.py)
so parallel agents never collide. Keep text output minimal.

## WINNER test (hard numbers from Winning Hunter fields)
Run length is the #1 signal: nobody keeps paying for a losing ad.
- STILL LIVE: lastSeen within the last 7 days of TODAY.
- RUN LENGTH: started >= 45 days before TODAY. Strongly prefer 90+ days.
  Only for genuinely rare formats may you accept 30-44 days, and only with strong scale signals; flag it in "notes".
- SCALE (at least one): countActive/activeSeen (duplicates) >= 3, OR total_active_ads_on_page >= 30, OR ad_rank <= 5.
- A real, established brand/DTC operator (no spam, gambling, romance-novel apps, crypto, one-ad dropship junk).
- Max 2 ads per brand per format. Rank by run length -> duplicates -> page scale -> ad_rank.
- Never invent numbers. Store revenue via mcp__winning_hunters__get_store_details is optional; else "unconfirmed".

## Search (mcp__winning_hunters__search_facebook_ads; load with ToolSearch)
media_type="images", ad_created_from="2024-01-01", ad_created_to=<TODAY-45d>, sort_by="longestrunning", sort_order="desc".
IMPORTANT: the last_seen_from/to filter matches the record UPDATE date, not the real lastSeen, so always re-check
started/lastSeen yourself from the result fields. min_days_running=45 works. Try min_duplicates=3 or min_active_ads=30 when noisy.
keyword matches ad TEXT (searchkeyword="adtext") or page names (searchkeyword="pagename"). Static ads often carry little text,
so brainstorm MANY phrasings the ad copy/headline of that format would contain, and also try niches
(HE health, BY beauty, PS pets, SK skincare, KS kitchen, FT fitness...). At least 8-10 different searches per format.
Results are big and get saved to a file: parse with python (fields: productid, pageName, page_id, started, lastSeen, countActive,
activeSeen, total_active_ads_on_page, ad_rank, image, poster, copy, urlStore, display_format).
Carousel/"DCO" ads count if the first card is the format. Skip video ads.

## LOOK at every candidate (mandatory)
Download `image` (media.winninghunter.com) -> /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hunt2/img_<ID>.jpg; convert webp/png to a real RGB JPEG with PIL.
If it 404s, use mcp__winning_hunters__scan_ad(<ID>) for fresh URLs.
Batch 6-12 candidates into one labeled grid with PIL and view it with the Read tool. MATCH only if what you SEE is the format
(format name + its "why" from your task). Copy alone never counts. The Instagram/Notion screenshots from the old board are NOT
acceptable references: every ref must be a real, live Winning Hunter ad.

## Output: /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hunt2/<TASK>.json (update after each format so progress is never lost)
[{"format": "<exact format name from task>", "matches": [{"id": "<productid>", "advertiser": "<pageName>", "file": "img_<ID>.jpg",
  "wh_link": "https://app.winninghunter.com/ad/<ID>?platform=meta",
  "fb_page": "https://www.facebook.com/ads/library/?view_all_page_id=<page_id>",
  "image_url": "<the media.winninghunter.com image url you downloaded>",
  "started": "YYYY-MM-DD", "last_seen": "YYYY-MM-DD", "days_running": N, "duplicates": N, "page_active_ads": N, "ad_rank": N,
  "store_revenue": "... or unconfirmed", "why_format": "what you SAW", "why_winner": "one line with the numbers"}],
  "rejected": [{"id": "...", "reason": "..."}], "searched": ["..."], "notes": "..."}]
Order matches best-first. Final report: per format, number of verified winners + shortest run length. If a format truly cannot
reach 5, say exactly how many and what you tried; never pad with non-matching or non-winning ads.

## Discovery task (E1 only): NEW image formats
While scanning long-running static winners across niches, spot recurring static formats that are NOT in /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/formats_image.json
(compare by meaning, not just name). For each new format with 5+ winners: same output schema, plus top-level fields
"definition", "why_it_works" (ONE short line each; they are shown on the board) and "stage" (TOF / MOF / BOF / TOF,MOF / MOF,BOF / ANY).

## Seeing what each format looks like
/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/formats_image.json lists, per format, "refs": old example screenshots (Instagram/Notion) stored in /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/imgs/<file>.
LOOK at those first to understand the format visually. They are ONLY a visual guide: never output them as references.

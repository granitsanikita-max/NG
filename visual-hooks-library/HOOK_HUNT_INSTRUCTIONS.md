# Targeted hunt: real VIRAL / WINNING examples of specific VISUAL HOOK formats (first 3 seconds)
H=/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hooks
Your task file lists formats (from $H/taxonomy.json: what_you_see, detection_cues, search_keywords) and how many verified examples each already has ("have"). Goal: bring EVERY format to >= 3 verified HIGH-confidence examples (aim 4-5). Never re-deliver an id already in $H/cls_meta_all.json or $H/cls_tt_all.json with the same format.
Prefix every helper file with your task name. Keep text output minimal.

## What counts
- It must be a VIDEO whose first 3 seconds clearly show that visual hook (textbook example someone can copy).
- And it must be proven: EITHER a TikTok ad/video with likeCount >= 50,000, OR a Meta ad that ran >= 30 days (started <= 2026-08-28) with scale (duplicates >= 3 or page active ads >= 30 or ad_rank <= 5). Prefer real products/brands; apps/games/dramas are OK only if the hook is exceptional and nothing better exists (max 1 per format).

## Where to search (load with ToolSearch)
- mcp__winning_hunters__search_tiktok_ads(keyword=..., sort_by="likes", sort_order="desc", limit=50, min_likes=50000) - description text match. Video url: field video (bare hash => https://media.winninghunter.com/tiktok/video/<hash>).
- mcp__winning_hunters__search_facebook_ads(keyword=..., searchkeyword="adtext", media_type="videos", ad_created_from="2024-01-01", ad_created_to="2026-08-28", min_days_running=30, sort_by="longestrunning" or "toprank", include_filter_reference=true) - field video = media.winninghunter.com url (fallback videos[0].video_hd_url).
- Also re-screen the already classified pools: medium-confidence items in $H/cls_meta_all.json / $H/cls_tt_all.json whose format or secondary is yours (their strips: $H/strips/<id>.jpg or $H/tt_strips/<id>.jpg) - upgrade them to high only if they truly are textbook.
Visual hooks rarely appear in ad text, so search by: the format's search_keywords, typical caption words ("wait for it", "watch till the end", "pov", "satisfying", "asmr", "transition", "magic", "watch this", "you won't believe", "trick", "hack"), niches where the hook is common, and product types that naturally produce it (e.g. drop test -> phone case, pour -> drinks, squeeze -> slime/stress toy, x-ray -> supplements). Run 8+ searches per format before concluding.

## Verify (mandatory)
Download: curl -sS -L -f -o $H/hunt/<id>.mp4 "<url>"  then  python3 $H/hook_strip.py $H/hunt/<id>.mp4 $H/hunt_strips/<id>.jpg 260  (7 frames 0-3s). LOOK at strips (stack several into one image with PIL to save calls). Accept only textbook matches.

## Output: $H/<TASK>.json (update after each format)
{"<format name>": [{"id": "<id>", "platform": "tiktok"|"meta", "advertiser": "...", "strip": "hunt_strips/<id>.jpg", "video_url": "...", "link": "https://app.winninghunter.com/ad/<id>?platform=meta (or tiktok)", "likes": N or null, "days_running": N or null, "started": "...", "last_seen": "...", "what_you_see": "concrete first-3s description"}], ...}
Final report: per format, verified count; list formats that could not reach 3 and what you tried.

## Known quirks (learned already)
- TikTok ads whose `video` field is a bare hash can NOT be downloaded (404). Only use TikTok results whose video field is a full https URL. Adding days_max=1 to search_tiktok_ads returns mostly full URLs; results are capped ~19 per call; date filters don't work on TikTok search.
- Meta: always check started/lastSeen yourself; media.winninghunter.com URLs sometimes 404 -> fall back to videos[0].video_hd_url / video_sd_url, or scan_ad(id).
- Keep downloads under $H/hunt/ and delete mp4s > 40MB after stripping. Disk is limited.

### Added quirk (from K2a)
- Meta: ~80% of older video links fail (media.winninghunter.com 404, fbcdn expired). Add a recent last-seen filter (last ~2 weeks) to search_facebook_ads: those results come with working video links. Skip scan_ad for verification (30k tokens, links still expired).

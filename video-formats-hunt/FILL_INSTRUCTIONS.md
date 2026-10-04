# Fill hunt: find more WINNING examples for thin new formats
W = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2
You get a list of formats (in your task message) with: definition, how many more verified examples are needed (need), a hint,
and ids already chosen (don't re-add those). Goal: find `need` MORE ads per format that clearly ARE this format and are WINNING.
Tools (ToolSearch): "select:mcp__winning_hunters__search_facebook_ads,mcp__winning_hunters__search_shopify_stores".
WINNING = Meta video ad started <= 2026-09-04 (30+ days live) AND last seen >= 2026-09-20 (still running), from a real brand
at scale (page has >= 15 active ads, or is a known 7+ figure brand; no dropship one-product pages with 2 ads, no apps/agencies).
Prefer different brands from the ones already chosen (max 2 per brand overall).

## How to search (be creative, run MANY searches, ~15-30 per format if needed)
- search_facebook_ads(keyword=<phrase likely in the ad copy or page name>, media_type="videos", last_seen_from="2026-09-20",
  last_seen_to="2026-10-04", ad_created_to="2026-09-04", sort_by="lastseen", sort_order="desc", size 20-50). Try phrases typical
  of the format (e.g. GRWM -> "get ready with me", "grwm"; This-or-That -> "which one", "pick one", "this or that"; pricing
  mistake -> "pricing mistake", "we messed up", "our mistake").
- Brands known to run the format: keyword=<domain>, searchkeyword="landingurl" (same date filters).
- Rows are big: only extract id, page name, started, last seen, active ads, ad text (first 200 chars), video url.
## Verify by looking
Video URL: media.winninghunter.com video field, else videos[0].video_hd_url / video_sd_url. Download to W/vids/X<ID>_<adid>.mp4
(curl -sSL, max 60MB, must contain 'ftyp' at bytes 4..8 else delete). Then python3 W/fmt_sheet.py W/vids/X<ID>_<adid>.mp4
W/sheets/X<ID>_<adid>.jpg and READ the sheet. Only accept if the WHOLE ad clearly is the format. Delete mp4s you reject.
## Output
W/fill/<ID>.json (save after each accepted ad): {"<format name exactly as given>": [{"id","task":"X<ID>","brand","domain",
 "started","last","days","page_active_ads","ad_text","video_url","what_you_see" (6-12 words)}]}
If after a real effort a format can't reach the need, say so; never pad with weak examples. Final message: per format: found/need.
Read-only everywhere except your output file and your own vids/sheets. Do not post anything anywhere.

## ROUND 2 additions (IDs R2a / R2b)
Round 1 used Meta ad-text search and mostly failed (WH text search is loose). Use these routes instead:
1. TikTok ads in WinningHunter: ToolSearch "select:mcp__winning_hunters__search_tiktok_ads,mcp__winning_hunters__get_tiktok_ad".
   A TikTok ad counts as WINNING if it has >= 20,000 likes (or WH shows it ran 30+ days). Brand must be a real brand, not a
   one-product dropship store with no brand. Record platform "tiktok", likes, and use task "X<ID>". Save its video like Meta ones.
2. Mine our own classified pool: W/F*_class.json (2,500 ads, each with format + notes/new_def) and W/F*_ads.json: grep notes/defs
   for words matching your format (e.g. prank, song, jingle, quiz, photoshop, mistake, google, donate, smash, drop test, meme).
   Videos for non-NEW ads were deleted: re-download via video_url in F*_ads.json.
3. Meta brand scans (keyword=<domain>, searchkeyword="landingurl", winning date filters) of brands that you know or find
   (firecrawl_search is allowed for ideas, e.g. "brand ad prank tiktok") run the format; check thumbnails/videos.
For TikTok refs add fields: "platform":"tiktok","likes":n. Output W/fill/<ID>.json same schema.

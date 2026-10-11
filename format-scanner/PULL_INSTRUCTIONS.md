# Format scanner - step 1: pull every validated winning ad (video + image) from big brands
W = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/scan   (work dir)
R = /home/user/NG/format-scanner   (repo dir: fmt_sheet.py lives here)
Tools (ToolSearch): "select:mcp__winning_hunters__search_facebook_ads,mcp__winning_hunters__search_shopify_stores".
Today is 2026-10-11. WINNING = Meta ad started <= 2026-09-11 (30+ days live) AND last seen >= 2026-10-01 (still running).

For each brand in your task:
1. Find its domain + Facebook page name (search_shopify_stores keyword=<brand>, or your own knowledge; verify the ads you get are really that brand).
2. search_facebook_ads(keyword=<domain>, searchkeyword="landingurl", media_type="videos", last_seen_from="2026-10-01",
   last_seen_to="2026-10-11", ad_created_to="2026-09-11", sort_by="lastseen", sort_order="desc", size 50), paging until you have
   all winners or 150 video ads. If landingurl gives few results, also try keyword=<page name>, searchkeyword="pagename".
   Then the same with media_type="images" (up to 150 image ads). Re-check every row's dates yourself (the filter is loose).
   Skip near-identical duplicates of a creative you already have, but count them: dup = number of ads using the same creative
   (same video/image URL or same ad text + same visual). High dup / long run = brand is scaling it.
3. Rows are huge: extract only id, page_name, started, last_seen, days, dup, ad_text (first 300 chars), media url
   (media.winninghunter.com field first, else videos[0].video_hd_url / video_sd_url / image url), media_type.
4. Media:
   - video: curl -sSL --max-time 120 to W/raw/<id>.mp4 (must contain b'ftyp' at bytes 4..8), then
     python3 R/fmt_sheet.py W/raw/<id>.mp4 W/sheets/<id>.jpg ; then DELETE the mp4 (disk is limited; we re-download winners later).
   - image: curl to W/images/<id>.<ext> (check it opens as an image with PIL; delete html/error pages).
5. Append each ad as one JSON line to W/ads_<TASK>.jsonl: {"id","brand","domain","page_name","media_type","started","last_seen",
   "days","dup","ad_text","media_url","file"} where file = "sheets/<id>.jpg" or "images/<id>.<ext>" (or null if download failed).
   Write as you go so nothing is lost if you are interrupted; on resume skip ids already in the file.
No classification in this step - just collect. Do not post anywhere. Final message: per brand: domain, videos kept, images kept.

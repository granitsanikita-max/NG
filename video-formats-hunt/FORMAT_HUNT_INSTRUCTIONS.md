# New video-ad FORMAT hunt across 7-10 figure brands (task names F1..F10)
W = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2
Goal: stalk the winning VIDEO ads of big brands and find ad FORMATS that are NOT already on our board. A format = the structure/concept of the WHOLE ad (e.g. "street interview", "fake podcast", "claymation story"), not the hook and not the product. Read W/EXISTING_FORMATS.md first: those 47 are already covered.
Tools (ToolSearch): "select:mcp__winning_hunters__search_shopify_stores,mcp__winning_hunters__search_facebook_ads,mcp__winning_hunters__get_store_top_ads". Credits are fine (~20k) but don't waste: no scan_ad, no transcript calls unless a candidate's format truly can't be judged from frames + ad text.

## 1. Brands (your niches are in your task)
search_shopify_stores(niche=<your category> or keyword=<sub-niche>, min_annual_revenue=1000000, sort_by="revenue_1y", sort_order="desc", size=20, pages 1-3). Keep brands with active_ad_count >= 40 (they test lots of creatives) and 30d_rev_estimated_min >= 85000. Aim for 25-30 brands per task (go deep: page through search results and use many sub-niche keywords), varied sub-niches, real brands (skip marketplaces, apps). Save W/<TASK>_brands.json [{domain,name,rev30_min,active_ads}]. Responses are huge: extract only these fields.

## 2. Their winning video ads (per brand)
search_facebook_ads(keyword=<domain>, searchkeyword="landingurl", media_type="videos", sort_by="longestrunning", sort_order="desc", last_seen_from="2026-09-20", last_seen_to="2026-10-04"), 1-2 pages. If 0 results try keyword=<brand name>, searchkeyword="pagename". Also get_store_top_ads(domain) for their top-ranked ads (merge, dedupe by ad id).
WINNING = video ad with started <= 2026-09-04 (30+ days live) AND last seen >= 2026-09-20 (still running). Rank and duplicate count help pick the best. Take up to 20 winning video ads per brand, preferring different-looking creatives (skip near-identical duplicates of the same video).
Video URL: the media.winninghunter.com video field, else videos[0].video_hd_url / video_sd_url. Download to W/vids/<TASK>_<adid>.mp4 (curl -sSL, max 60MB; check file starts with an mp4 'ftyp' box, delete html/error pages).
Record every ad in W/<TASK>_ads.json as you go: {id, brand, domain, page_name, started, last_seen, days, rank, dup, page_active_ads, ad_text (first 300 chars), video_url, file}.

## 3. Look at each WHOLE ad
python3 W/fmt_sheet.py W/vids/<TASK>_<id>.mp4 W/sheets/<TASK>_<id>.jpg  -> 12 frames across the full ad + duration. Read the sheets (you may tile 2 sheets per Read to save tokens) together with the ad text.
Classify each ad: format = one of the 47 EXISTING names (exact name), or NEW. Be strict: NEW only when the overall structure is clearly none of the 47. A new product, niche or hook is NOT a new format. Unusual production (puppets, miniatures, stop-motion, game-show set, fake news broadcast, ASMR, POV skits, split-screen debates, music video, mockumentary, cartoon, etc.) can be NEW if not covered.
For NEW: give a short working format name (2-5 words), a 1-2 sentence definition of the whole-ad structure (beats), what it is closest to among the 47 and why it is different, and a funnel stage guess (TOF/MOF/BOF/ANY).
Write W/<TASK>_class.json {ad_id: {format, new_name, new_def, closest, stage, confidence: high|medium, notes}} as you go.
Keep the mp4 only for ads classified NEW (needed later); delete the others after sheeting. Keep all sheets.

## 4. Final report (short)
Brands covered, ads screened, then a list of NEW format candidates: name, definition, and the ad ids (brand, days live) that show it. Prefix helper files with <TASK>_. Never touch other tasks' files.

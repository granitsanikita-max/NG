# Reference-ad hunt (Winning Hunter + Facebook Ad Library), VISUALLY VERIFIED
S=/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad
Goal: for each format in your task, find 2 (minimum 1) REAL, currently-live ads that VISUALLY are that format.
A match is judged on what you SEE in the frames (and the on-screen text), never on the ad copy/script alone.

Tools (load via ToolSearch): mcp__winning_hunters__search_facebook_ads, mcp__Firecrawl__firecrawl_scrape.
Keep text output minimal. Never modify Notion or Miro. Work only inside $S/hunt/.

## Search
- mcp__winning_hunters__search_facebook_ads with: keyword=<phrase>, media_type="videos" (or "images" for image formats),
  last_seen_from="2026-09-10", last_seen_to="2026-09-24" (so the ad is still live), country="US", sort_by="adspend" or "longestrunning" or "relevance".
  Results are large and get saved to a file; parse that file with python (fields: productid = FB Ad Library id, pageName, caption, copy, lastSeen, display_format).
- Keyword matches ad TEXT only. Brainstorm MANY phrasings a real ad of this format would contain (hooks, on-screen words, CTA words), 
  plus try searchkeyword="pagename" for creator/brand names typical of the format. Try at least 6 different searches per format before giving up.
- Skip obvious spam (novel/romance apps, gambling), and prefer established ecommerce/DTC advertisers.

## Get the actual video / image of a candidate (only live ads work)
1. mcp__Firecrawl__firecrawl_scrape(url="https://www.facebook.com/ads/library/?id=<ID>", formats=["rawHtml"], waitFor=5000, maxAge=0)
   -> result is saved to a file (path in the error message).
2. python3 $S/extract_ad.py <that file> <ID>  -> JSON {video, poster, images}
3. Video: curl -sS -L -o $S/hunt/<ID>.mp4 "<video>"; then python3 $S/contact_sheet.py $S/hunt/<ID>.mp4 $S/hunt/<ID>_sheet.jpg $S/hunt/vf_<ID>.jpg
   Image ad: curl images[0] -> $S/hunt/img_<ID>.jpg
4. LOOK at the contact sheet / image with the Read tool. Decide: MATCH or NO, with a one-line reason describing what you see.
Run at most 2-3 Firecrawl calls at once (rate limits).

## Visual definitions (what must be SEEN)
- Street Interviews: an interviewer with a mic stopping real people outdoors/in public; handheld street footage.
- Myth Buster: on-screen "myth"/"fact"/"true or false" style text or a creator explicitly debunking, with visual myth-vs-fact framing.
- Crochet Story: the story is told with crocheted/knitted yarn figures or yarn craft visuals (NOT drawings).
- Claymation: stop-motion clay/plasticine figures (NOT 2D drawings or 3D CGI).
- Personal Story: a single creator on camera telling their own journey with the problem (selfie/talking-head, personal footage).
- Scenarios: opens on a hypothetical ("imagine if…", "POV:", "what happens when…") acted out/visualized on screen.
- Personal Learning / Epiphany: creator on camera sharing one lesson ("I wish I knew this sooner", "the one thing that changed…").
- Q&A: the hook is a question shown on screen (often a comment-reply bubble or big question text) then answered.
- Levels: on-screen "Level 1 / Level 2 / Level 3" escalation.
- Ranking / Tier List: an S/A/B/C tier board or explicit on-screen ranking of options.
- Challenge: "I tried X for N days" / "Day 1 … Day 7" on-screen progression.
- AI UGC Avatar: a presenter that is visibly an AI-generated avatar (uncanny lipsync/skin, often HeyGen/Arcads style).
- Personal Update: founder/creator talking to camera giving a casual update to followers ("quick update", "big news").
- Goal / Dream Journey: founder documenting progress toward a goal ("day X of building…", "road to $1M").
- Lesson From Others (Mentor Story): the speaker tells someone ELSE's story/lesson (grandma, mentor, doctor told me…), third-person narrative.
- Win (Victory Announcement): a milestone shown on screen (sales numbers, "we sold out", "1 million customers", celebration).
- Problem-Agitate-Solve: clear 3-beat visual: problem shown, pain agitated, product shown as the fix.
- Image formats: judge the static image itself against the format name + its "why" (given in your task).

## Output
Write $S/hunt/<taskname>.json: [{"format": "...", "matches": [{"id": "<FB id>", "advertiser": "...", "file": "vf_<ID>.jpg" or "img_<ID>.jpg",
  "fb_link": "https://www.facebook.com/ads/library/?id=<ID>", "wh_link": "https://app.winninghunter.com/ad/<ID>?platform=meta", "why": "what you saw"}],
  "searched": ["phrases tried"], "notes": "..."}]
Report briefly: per format, number of verified matches.

## More visual definitions (replacement hunt)
- Talking Objects / Characters / Body Parts: an object, product, organ or body part with a face/mouth that TALKS (animated or puppet), narrating the ad.
- Case Studies: breaks down ONE real person's/customer's result step by step (before -> what they did -> result), on camera or with on-screen proof.
- Animated Mechanism Explainer (Clinical VSL): medical/3D anatomical animation showing HOW the product works inside the body (clinical explainer look).
- Fake Doctor: a presenter styled as a doctor (white coat/scrubs/stethoscope, clinic setting) giving the pitch.
- UGC Science Backed: creator on camera citing studies/research, usually with on-screen study screenshots/stats.
- Podcast: looks like a podcast clip — mics in frame, 2+ people or host at a podcast set, podcast framing.
- Product Comparison Video: explicit side-by-side / A-vs-B comparison of the product vs competitor or old method, on screen.
- 5 Reasons Why: on-screen numbered reasons ("5 reasons…", "reason #1…").
- UGC Testimonial Mashup: several DIFFERENT real customers' testimonial clips cut together.
- Educational UGC: a creator on camera teaching something useful, with the product woven in.
- Founder Story Ads: the founder on camera telling how/why they started the company.
- Breakdown / Explainer: a creator dissecting a news event/trend/thing (e.g. green-screen over a news clip) and explaining why it matters.
- UGC Listicle: a creator on camera running through a numbered list.
- UGC Reviews: a real customer/creator on camera reviewing the product.
- Day In The Life: vlog-style footage of someone's day with the product appearing naturally.

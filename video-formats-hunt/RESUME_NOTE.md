# Resume note: new video formats hunt (paused 2026-10-04 at user's request)
Done: 10 niche agents (F1-F10) stalked winning Meta video ads (live 30+ days, still running Sept 20+) of ~250 brands at $1M+/yr.
2,526 ads classified vs the 47 existing formats (EXISTING_FORMATS.md); 694 flagged NEW. Data: F*_brands.json, F*_ads.json, F*_class.json.
Scratch (may be wiped on container reset): vf2/vids/F*_<id>.mp4 = 693 NEW-ad videos (1.2GB), vf2/sheets = 12-frame sheets.
If the mp4s are gone, re-download from video_url in F*_ads.json (Meta links expire within days -> re-pull via search_facebook_ads with a recent last_seen filter).

## Preliminary cross-niche clusters (merge + verify by eye next)
Strong, seen in several niches:
- Cinematic Brand Film / Editorial Lookbook / TV-style spot (F1,F2,F5,F6,F7,F8,F9)
- Animated Packshot / Motion-Graphic Poster / Video Static (F1,F3,F5,F6,F8,F9,F10)
- Offer Stack Breakdown / Walkthrough / Escalation (F3,F5,F10)
- Fit Check single-outfit (F5,F6, also F1)
- Sale Flipbook Countdown "won't do this again" (F1,F4)
- Animated Pixar/cartoon character story incl. fairy-tale storybook (F1,F3,F4,F5,F9,F10)
- Partner POV / wife sells his product / partner-observed testimonial (F1,F3,F6,F10)
- Recipe Reel (product as ingredient) (F3,F10)
- Don't-Buy-If / Not For Everyone reverse qualifier (F1,F7)
- This-or-That picker (F2,F5); Celebrity spokesperson spot (F7,F9,F10)
- Comedy sketch / scripted parody / infomercial sketch (F4,F6,F7,F9,F10); POV comedy skit (F3,F7,F10)
- IRL brand stunt / hidden-camera public stunt (F1,F2,F9); Meme caption loop (F4,F9,F6)
- Photoshop "Fixed it for you" (F7,F9); Room tour / makeover reveal (F7); Factory tour (F4,F3)
Distinct but fewer ads: Input vs Result Pairs, Pack My Bag, Mini-Doc Portrait, Prop Analogy Explainer, AI Before/After Morph,
Slapstick Hard-Way Gag, Product ASMR, Review Read-Aloud, Micro Bumper, Usage Timeline Countdown, YouTube Reviewer Clip,
BTS vs Final Shot, Trade-Show Booth Demo, Jingle Music Video, Torture Test, Brand Anthem Montage, IP Collab Drop Trailer,
Party Game Play-Along, Jubilee-style debate, Quiz walkthrough, Phone-screen investigation, Barber-chair glow-up, Family duo GRWM.

## Next steps
1. Merge clusters into final formats (strict: whole-ad structure, not just production style), verify each by viewing sheets.
2. Each final format: top 5 winning ads (days live, scale); targeted WH searches to fill formats with <5.
3. Back up full videos to Drive (Composio sandbox uploader pattern: visual-hooks-library/board/vh_uploader.py).
4. Add a "NEW formats from 7-10 figure brands" section to the video board https://miro.com/app/board/uXjVHjf0Xlk=/
   with playable GIF previews + Watch + Saved copy, then audit.

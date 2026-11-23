# GAPFILL — 4 paste-ready blocks (gap-fill agent, 2026-11-23)

Closes RESULT-C gaps 1 (TikTok + Google per region), 2 (§10B tail), 4 (AU/NZ keyword totals) and 7 (TikTok Shop rung).
Every claim has URL + date + solidity. "NEW SOURCE" means the URL isn't in the doc's Sources list yet, so the orchestrator assigns the next S-number.
Raw evidence lives in /tmp/claude-0/-home-user-NG/7e294311-f113-54e1-bb5f-02ca3c896260/scratchpad/gapfill/: gat3_*.json (Google ad text), all_*.png (Google page screenshots), cc_out1.json and cc_out2.json (TikTok Creative Center API lists), tt_lib_gb_snoring.json (TikTok library captcha), snap_aunz.txt (Meta ad bodies).

---

## BLOCK 1 · TikTok + Google ad sweep per region → Doc 1 §0B / §1 TAKEN map / §2 gate

**Tools used:** headless Playwright (Chromium) on adstransparency.google.com (8 domains × AU + GB, plus "See all ads" pages with ad text read from rendered frames) · `firecrawl_scrape` for the one GB page where the local browser hit Google's "unusual traffic" check (not bypassed; Firecrawl fetched it normally) · headless Playwright on TikTok Creative Center Top Ads (logged out; 7 keywords × AU + GB; results read from the page's own `top_ads/v2/list` response) · headless Playwright on the TikTok Commercial Content Library (GB). Logs: Google ✅ (🔁 Firecrawl for 1 page) · TikTok Creative Center ✅ partial (logged-out view only) · TikTok Commercial Content Library ❌ (captcha). Winning Hunter `search_tiktok_ads` / `search_google_ads` remain ❌ (sign-in refused).

### 1A · Google Ads Transparency Center (all-time ad counts per domain, read 2026-11-23) [DATA]

URL pattern: `https://adstransparency.google.com/?region=<AU|GB>&domain=<domain>` (NEW SOURCE, one row per domain)

| Domain (brand) | AU ads | GB ads | Verified advertiser | Formats seen | Women-first copy? |
|---|---|---|---|---|---|
| honexcompany.com (Honex) | **~200** | **~200** | Ecom Beavers LLC | Video-heavy (AU: 135 video icons on the "all ads" page; GB: 93), plus Shopping and Search text | **No.** Text ads are unisex comfort/fit lines: "Over 243K Users Love This Mouthpiece", "Custom-Fit & Adjustable Mouthpiece", "The quickest and easiest way to stop snoring for you or your partner", "Sleep Apnea Relief Mouthpiece". The "Women Edition" seen on Meta doesn't appear in any rendered Google text ad |
| snoremd.com.au (SnoreMD) | **91** | 0 | APAC HEALTH & MEDICAL DISTRIBUTORS PTY LTD | Video (40), Search, Shopping, Maps | **No.** "Stop Snoring or Your Money Back. 30 Day Money Back Guarantee." · "Australian made, dental-grade, BPA-free. Afterpay available." · "Try it 30 days. Not for you? Full refund, no return postage required." |
| snoremedic.com.au (SnoreMedic) | **64** | **16** | DK ECOMM GROUP PTY LTD | Search with images, some video | **No**, partner framing: "Put an end to annoying snoring, frustrated partners, and restless nights" · "Quiet, restful nights bring couples closer." Images show a man snoring |
| goodsleepco.health (Good Sleep Co / Hushd Avera) | **41** | 0 | DIGITAL SLEEP DEVICES PTY LTD | Search, video (6) | **No**, partner framing: "No More Midnight Elbow Jabs - Hushd Avera Snoring Mouthguard" · "Your Partner Will Thank You - No More Sleeping On The Couch" · "TGA-approved anti-snoring mouthpiece" |
| beautysleepclub.com (Beauty Sleep) | **15** | **3** | The One Percent Group PTY LTD | Shopping, image, video | **Yes, but tape:** Shopping title "…Nasal Breathing Sleep Strips **for Women**, 30 Strips" (AU + GB). Search: "Firm Your Jawline Naturally While You Sleep With Beauty Sleep Mouth Tape" |
| happysleep.au (Happy Sleep) | 2 | 0 | SLEEP SOUND PTY. LTD | Shopping | No. Both are for nasal strips ("Happy Fit - Performance Nasal Strips") |
| airvex.shop (AirVex) | 0 | **0** | — | — | n/a. AirVex runs its GB menopause angle on Meta only |
| feliorauk.com (Feliora) | 0 | 0 | — | — | n/a |

- SnoreMD's domain is **snoremd.com.au** (confirmed by its 91 AU ads under APAC HEALTH & MEDICAL DISTRIBUTORS).
- **Limit:** Google shows image and video creatives as pictures, so only text, Shopping and image-with-text ads could be read. Video ads (Honex 135 AU, SnoreMD 40) weren't watched. "Women-first: No" therefore means none in the readable ads.
- GB beautysleepclub.com: the local browser hit Google's "unusual traffic" page. That page wasn't bypassed; the same URL was read through `firecrawl_scrape` → 3 ads.

### 1B · TikTok

**Creative Center Top Ads** (`https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?period=180&region=<AU|GB>`, keyword typed into the search box, last 180 days, read 2026-11-23, NEW SOURCE) [DATA]
- Keywords run in AU and GB: snoring · anti snoring · mouth tape · snoring women · menopause snoring · snoring mouthpiece. That's 12 searches with 16–19 ads each, except "snoring mouthpiece" at 2. The logged-out view shows page 1 only, and only ads that advertisers have authorised for the Creative Center.
- **Mouthpiece ads: 0 in AU, 0 in GB.** "snoring mouthpiece" returned only a toe-nail patch and a nebuliser.
- **Women-first snoring ads: 0 in AU, 0 in GB.** "snoring women" and "menopause snoring" returned women's clothing, a "Bible for Women" app, or the generic snoring set.
- What does run (snoring-related, AU/GB): magnetic nasal strips ("Say goodbye to snoring and improve your breathing efficiency! #MagneticNosePatches", Trendz, ID 7492082160686415873; "I thought nasal strips were all the same—then I tried this.", Wellness With Emma, 7455532247149887505; Matt Long, 54K likes, 7518338793113567233). Partner-of-snorer and male-snorer hooks also run: "Tired of **his** snoring ruining your sleep?" (GB, 7648083619537371143) · "I mean seriously whose **dad** doesn't snore?" (AU, 7416481485241581569) · "Snoring doesn't only affect one side of the bed 😴" (nozey, AU, 7673037893073551381) · "Being proactive about your partner's #snoring…" (AU, 7386627058132631569).
- **Region filter is loose:** Malay- and Arabic-language ads appear under AU and GB. Treat this as "ads TikTok surfaces for the region", not a per-country census.

**Commercial Content Library** (`https://library.tiktok.com/ads?region=GB&…`, 2026-11-23) **❌ BLOCKED.** The page put up a "Select 2 objects that are the same shape" captcha, and the search API returned an empty body. It wasn't bypassed. The library's own region list covers EU/EEA countries plus CH, GB, TR and BR, with **no AU or NZ** (`/api/v1/support-regions`, DATA). So for AU/NZ only the Creative Center applies.

### 1C · Bonus from the Meta AU/NZ pass (Block 2): women-addressed hooks on NON-mouthpiece products [VERBATIM, ad pages rendered headless 2026-11-23]
- **Somma (anti-snoring spray, already in the TAKEN map as "unisex")**, AU, started 22 Nov 2026: "Think nose strips help with snoring? Think again. 😨 / **Most women don't know this** but snoring has nothing to do with your nose, pillow placement, sleeping position or even weight… There is a hidden muscle that is responsible for 97% of snoring." → sommacompany.com/products/somma-anti-snoring-spray · https://www.facebook.com/ads/library/?id=1121490487426936. **Correction:** Somma's angle is no longer purely unisex; it now tests a women-addressed hook.
- **Hushlea (NEW; chin-worn throat-pulse device, A$154 per og:price, "100-night money-back promise"; its product page shows a man as the snorer)**, NZ, started 19 Nov 2026: "Think nose strips stop snoring? Think again. 😨 / **Most women don't know this**, but snoring has nothing to do with your nose, your pillow, how you lie or even your weight… A hidden muscle in your throat is behind most snoring." → https://www.facebook.com/ads/library/?id=1608609907238117 · hushlea.com/products/hushlea-pro (NEW SOURCE).
- Also new in AU/NZ, none women-first: HiZuu SnoreSnoozer (tongue device; "Why people try it after pillows, sprays and chin straps", 4147770232190757) · Slublonin Gritmultlades / "Waxlify" (slim mouthpiece, US-made claim, male testimonial "and so did my wife", 1173471572286858) · Winkystar / "Restova Anti-Snoring Mouthpiece" (general store, 1447553204203064) · Try Respire tape with Michael Chernow and Dr Clay Moss (unisex, 1486378596735339 / 2316910665551850) · Luelle collagen mouth tape (beauty-coded, 2657576531353351).

### Verdict (paste into §2 gate + TAKEN map)
**TikTok and Google do not change the call.** In AU/NZ, a women-first mouthpiece is still **partly open**. The only women-coded mouthpiece claim is Honex's Meta "Women Edition". On Google, Honex (~200 ads), SnoreMD (91), SnoreMedic (64) and Good Sleep Co (41) all run unisex or partner-framed copy ("frustrated partners", "No More Midnight Elbow Jabs"). TikTok Top Ads shows no mouthpiece ad and no women-first snoring ad in AU or GB. In GB a women-first mouthpiece stays **taken**, because the verdict rests on AirVex's Meta menopause ads; AirVex has 0 Google ads, which doesn't loosen it on Meta, the only channel we use. Two caveats for §2:
- (a) Google is a busy **unisex** mouthpiece channel in AU: 4 MAD brands with 41–200 ads each. There's search demand, but none of it is women-first.
- (b) The women-addressed hook itself ("Most women don't know this…") is now being used in AU/NZ by **non-mouthpiece** sellers: Somma (spray) since 22 Nov and Hushlea (chin device) since 19 Nov. The open space is a women-first **mouthpiece with her story**, not just the word "women" in a hook.

**TAKEN-map line to add:** "TikTok (Creative Center Top Ads, AU+GB, 6 keywords): 0 mouthpiece ads, 0 women-first snoring ads; TikTok Library GB captcha-blocked, AU/NZ not covered. Google (Ads Transparency): AU Honex ~200 · SnoreMD 91 · SnoreMedic 64 · Good Sleep Co 41 · Beauty Sleep 15 · Happy Sleep 2 · AirVex 0 · Feliora 0; GB Honex ~200 · SnoreMedic 16 · Beauty Sleep 3 · others 0. Women-first readable copy: Beauty Sleep TAPE only."

**So What → do this:** keep AU first. On Google, a women-first mouthpiece would have no copy competition, but stay Meta-only per the business lens. Our hook must carry her specific story (menopause onset, girls' trip, the spare room), because a generic "most women don't know" line is already being run by a spray and a chin device.

---

## BLOCK 2 · AU + NZ Meta keyword totals → Doc 1 §0B.3 (ad demand)

**Tools used:** `mcp__facebook__ads_library_search` (Meta Ad Library API; ACTIVE; limit 50 = the 50 newest; read 2026-11-23) + headless Playwright render of 10 ad pages (snap_aunz.txt). The API's `estimated_total_count` is Meta's estimate [DATA]. The API returns only the 50 newest ads per query and wasn't paged to exhaustion (stated limit). Source: Meta Ad Library API, https://www.facebook.com/ads/library/ (country AU / NZ, active, keyword). Existing [S11] can cover this.

| Keyword | AU est. total | AU de-duped advertisers in 50 newest | NZ est. total | NZ de-duped advertisers in 50 newest |
|---|---|---|---|---|
| anti snoring mouthpiece | **456** | **7**: Honex 26 · Happy Sleep 9 · Winkystar 5 · Pillow Haven 4 · Somma 3 · Slublonin Gritmultlades 2 · Modern Health Lab 1 | **204** | **6**: Honex 25 · Chemist Warehouse NZ 12 (incl. "Happy Sleep Anti-Snoring Mouthpiece \| … Online Only", 1613681710087373) · Modern Health Lab 7 · Hiquo 3 · Slublonin 2 · Somma 1 |
| snoring | **5,276** | 23 (mostly noise: fiction/drama apps, health advertorials). Snoring-product: **Loop** earplugs 12 · **Ozlo** sleepbuds 5 · **HiZuu** SnoreSnoozer 1. Others: Midlife Queens Magazine 5 (leg cramps, already logged), Midlife Wellness Tips 4 (magnesium), Lilly Australia 3 (weight) | **2,731** | 17 (noise-heavy). Snoring-product: Loop 11 · Ozlo 6 · HiZuu 1 |
| stop snoring | **2,402** | 20: noise except Loop 9 | **1,310** | 21: noise except Loop 7 |
| mouth tape snoring | **734** | **8**: Somma 25 · Chapter 1 12 (fiction) · The GOAT 6 · Honex 3 · Velorosa 1 ("Stop Snoring Night 1") · Luelle 1 (tape) · Diane Mercer, RRT 1 (CPAP advertorial) · Pelican Dog Rescue 1 | **363** | **12**: Honex 14 · Chapter 1 10 · Somma 6 · Snoring Health Forum 5 ("It's Not Just Menopause", wedge pillow, already logged) · Michael Chernow / Try Respire 4 (tape) · Hushlea 3 · Try Respire 2 · Slublonin 2 · Beauty Sleep 1 ("No more tape that pulls your lips") · Dr Clay Moss / Respire 1 · Modern Health Lab 1 · Diane Mercer, RRT 1 |
| snoring mouth guard | **146** | **8**: Somma 14 · Storyflow-N4 14 (fiction) · Little Life Hacks 6 ("1 Weird Stop Snoring Trick") · Honex 5 · Ray Whitfield 4 ("Fix Sleep Apnea At The Root") · Pridola's Design 3 · Drama Groove 2 · Readbox 2 | **115** | **7**: Storyflow-N4 19 · Readbox 11 (fiction) · Little Life Hacks 6 · Dr-Rachel Cole 5 (apnoea advertorial) · Ray Whitfield 4 · Somma 3 · Honex 2 |

- **Read:** the keyword API matches words anywhere in the ad, so "snoring" and "stop snoring" totals are inflated by fiction and drama apps. The demand signal is "anti snoring mouthpiece": **AU 456 · NZ 204 active**, with Honex taking about half of the 50 newest in both. That's in line with Honex's AU 235 / NZ 216 page counts already in §15.
- **New AU/NZ advertisers not in the long-list:** Hushlea (chin device; women hook, see Block 1C), Slublonin Gritmultlades / "Waxlify" (mouthpiece), Winkystar (general store selling the "Restova" mouthpiece), Luelle (collagen tape), Michael Chernow and Dr Clay Moss (Respire creator ads), Little Life Hacks / Ray Whitfield / Dr-Rachel Cole (advertorials). None runs a women-first mouthpiece.

**§0B.3 line to paste:** "Meta Ad Library API, ACTIVE, 23 Nov 2026 [DATA]: 'anti snoring mouthpiece' AU 456 / NZ 204 · 'snoring mouth guard' AU 146 / NZ 115 · 'mouth tape snoring' AU 734 / NZ 363 · 'snoring' AU 5,276 / NZ 2,731 and 'stop snoring' AU 2,402 / NZ 1,310 (both noise-inflated by fiction apps). Of the 50 newest 'anti snoring mouthpiece' ads, 7 AU / 6 NZ advertisers; Honex is about half."

**So What → do this:** AU has proven paid demand (456 active mouthpiece ads) held by one dominant unisex operator. NZ is about 45% of AU's volume, so launch AU and add NZ as a country in the same ad set rather than a separate build (INFERENCE).

---

## BLOCK 3 · Doc 2 §10B tail (#14–#18 + "Doing nothing") → replace the current #14–#18 blocks

**Tools used:** python over data/databank.csv (479 rows; failed_solution tag + quote text search), with a substring check against docs/doc1–4_body.md so no quote repeats one already in the docs. Pulled by product-pulse / Firecrawl collectors V1–V3 (see §2C).
Counts are "n of 479 tagged" plus "+m untagged text mentions". Source numbers are existing Doc 2 S-numbers where the URL already exists.

**Correction to report:** the current #14 "Likes" quote [S109] ("…plus intake nose strips now to stop snoring 😅") is from a **38-year-old** in r/perimenopause_under45 (bank row v1-007, age_signal "38"). She's outside the 40–60 ICP, and the quote is a current-use mention, not a like. Replace it as below.

### 14 · Nasal dilator: 4 tagged (+1 untagged mention); burned 3 of 4
- **Likes:** works only as a helper next to a mouthguard. "A mouth guard plus nasal dilators that fit inside the nose worked for me." Mumsnet Chat, GB, *I fixed snoring* (NEW SOURCE: https://www.mumsnet.com/talk/_chat/5238569-i-fixed-snoring?page=2 · date not shown · SNIPPET)
- **Dislikes:** goes on the list of things tried and dropped. "I have tried nasal sprays, sleeping sitting up, nasal strips, nose appliances, mouthpieces that were either too big for my mouth and left me in pain all day, or were completely ineffective." [S92 · Trustpilot vitalsleep.com · 5★ · 2020-01-24 · VERBATIM]
- **Horror:** "I was at the end of my rope, ready to consider paying out of pocket for surgery that has no guarantee of success. My husband and I were sleeping in separate rooms." [S92 · 5★ · 2020-01-24 · VERBATIM] (written after nose appliances failed)
- **Believe it works?** **No, not on its own.** 0 of 4 tagged rows say a dilator alone worked; 3 of 4 list it among failures. The only positive is a dilator **plus** a mouthguard. In bank-label terms she thinks of it as "its_my_nose" (12). INFERENCE: it fails because it never touches the jaw/throat.

### 15 · Cutting alcohol: 4 tagged (+7 untagged mentions = 11 of 479 mention drink/alcohol); non-product
- **Likes:** none found. 0 of 11 rows say stopping drinking stopped the snoring. The closest is the belief behind it: "Drinking exacerbates my snoring and, like many people, I'm having an extra glass or two during lockdown." [S10 · Telegraph · GB · midlife · 2020-04-16 · VERBATIM]
- **Dislikes:** she already doesn't drink, and still snores. "Me and DH have separate rooms 🫣 I'm not over weight and I haven't smoked for 10+yrs, don't drink." [S16 · Mumsnet · GB · 2024-09-22 · VERBATIM]
- **Horror:** "It is so bad I don't stay overnight with relatives any more because of the snoring." (from a woman who opens with "I don't drink") (NEW SOURCE: https://www.mumsnet.com/talk/am_i_being_unreasonable/2269234-To-be-embarrassed-by-my-snoring · date not shown · SNIPPET) · "I also avoid situations where I may need to sleep near other people. It's very frustrating 😑" [S16 · 2024-09-22 · VERBATIM]
- **Believe it works?** **Split, and mostly no.** 3 rows believe alcohol makes it worse (v1-038 "100x worse" [S103]; Telegraph [S10]; Daily Mail "Steven winces" [S18]). 5 rows say they **don't drink and still snore** (v1-080, v1-089, v1-126, v1-176, v2-125). Counter-proof that a jaw device beats the wine: "I've just had a remark from my husband that my snoring was remarkably better ( even after a few glasses of wine)." (NEW SOURCE: https://uk.trustpilot.com/reviews/662e0507403890ea182f039e · Trustpilot (Snoreeze mouthguard) · 5★ · GB · 2024-04-28 · VERBATIM)
- **So What:** never tell her to give up her glass of wine. Use "Still snore when you haven't had a drop?" (INFERENCE; hook built on 5 "don't drink" rows).

### 16 · Supplements / oils / vapours / lozenges: 3 tagged
- **Likes:** one believer. "When my snoring starts, I take 5000 ui of Vitamin D every day for a month." [S111 · r/Menopause · 2022-11-03 · VERBATIM] (her result line is already quoted in §10B). Compliance: anecdote only; never echo it as a claim.
- **Dislikes:** they taste odd and do nothing. "I've also tried nasal strips, lubricating lozenges and strange-tasting throat sprays." [S10 · Telegraph · GB · 2020-04-16 · VERBATIM] (lozenge price complaint: see §10 "price" [S34 · already used])
- **Horror:** after "pillows, vapours, different positions, nose strips, mouth guards": "It seems all the muscles in my throat go to jelly once I'm asleep and I'm just honking the night away and annoying the hell out of anyone in earshot." [S40 · Mumsnet AIBU · GB · 'as I get older' · 2022-09-22 · VERBATIM]
- **Believe it works?** **1 of 3 yes** (vitamin D), **2 of 3 no** (vapours, lozenges "complete waste of money"). Low belief, low spend.

### 17 · Chin strap: 1 tagged (+1 untagged mention by a third party)
- **Likes:** none. **Only 1 row of her own, and no like or horror quote that is specifically about the chin strap.** Say so, don't pad.
- **Dislikes:** bought alongside everything else, and none of it worked. "I've ordered mouldable mouth guards, chin straps and curved anti-snore pillows to change the position of my head and mouth during the night." [S10 · Telegraph · GB · midlife · 2020-04-16 · VERBATIM] (her next line, "Nothing has worked.", is already in §10B #8)
- **How others see it:** it's a list item people suggest to the husband. "If she doesn't have OSA, nasal strips, mouth tape, a chin strap.... sleeping in separate rooms, weight loss...." (r/GenX reply about a "post menopausal woman who now snores", 2024-02-06 · VERBATIM · comment URL https://www.reddit.com/r/GenX/comments/1ak3e65/wife_snores_need_suggestions/kp6ge3h/ = [S143] thread)
- **Believe it works?** **No** (1 of 1 tried → failed). Competitor HiZuu already uses it as a failed alternative in AU ads: "Why people try it after pillows, sprays and chin straps" (Meta 4147770232190757, 2026-11-23, VERBATIM).

### 18 · Anti-snore ring: 1 tagged
- **Why she had one:** her partner bought it, and it's a great self-deprecating line. "So far the only ring he's given me is the Good Night Anti-Snoring Ring, (£29.99) which stimulates acupressure points on your finger to keep your airways open." [S10 · Telegraph · GB · 2020-04-16 · VERBATIM]
- **Likes:** none (0 of 1).
- **Dislikes / horror:** already quoted ("mine keeps falling off and the roars continue" [S10]).
- **Believe it works?** **No** (1 of 1). Paid £29.99, the same as the GB DTC mouthpiece going rate.

### Doing nothing / work-arounds: add the missing "Believe it works?" line
- **Believe it works?** **As a truce, yes; as a fix, no.** Separate rooms are the most common work-around (separate bedrooms 23 · he wears earplugs 7 · she books her own room 7 · she sleeps on the sofa 7 [S1]). The likes in §10B (#S15) come from couples who've made peace with it. The dislikes and horror (#S16, #S10) show she still feels it's unfair on others and dreads trips (INFERENCE from the counts above; no new quote needed).

**So What → do this:** #14–#18 together are 13 tagged rows (2.7% of the bank). These are minor detours, not the main enemy. Use only two of them in copy: "don't drink and still snore" (#15) and the ring line as humour (#18). Keep the fight on boil-and-bite fit (95) and tape/strip let-downs.

---

## BLOCK 4 · TikTok Shop rung of the price ladder → Doc 4 §15 Price ladder

**Tools used:** `firecrawl_search` (site:shop.tiktok.com/gb, 2 queries; TikTok Shop markets search) · `firecrawl_scrape` on 3 GB PDPs (refused: "Firecrawl can't scrape this site") · headless Playwright on 4 GB TikTok Shop pages (all redirected `region_not_match` to /us and showed a "Drag the puzzle piece" captcha, not bypassed). Logged as 🔁 SNIPPET-only; Winning Hunter `search_tiktok_products` still ❌.

**AU row:** "TikTok Shop AU: **n/a, TikTok Shop is not live in Australia**" ("Australia | Asia-Pacific | Not available | No domestic seller programme | No confirmed date", leapbuzz.com, *TikTok Shop countries 2026: 20 live markets (October list)*, https://leapbuzz.com/blog/tiktok-shop-availability-markets/ · Oct 2026 · SNIPPET). TikTok's own discover pages say it is "launching in Australia in 2026" with no date (https://www.tiktok.com/discover/is-tik-tok-shop-launching-in-australia-launch-2026 · SNIPPET). The same applies to NZ: it's not in the live-market list (INFERENCE from that list).

**GB row:** "TikTok Shop GB: **£6.59–£19.99** for unisex adjustable/silicone mouthpieces (search snippets; sold counts tiny)"

| Listing (GB TikTok Shop) | Price | Sold | Women? | Source (all 2026-11-23, SNIPPET) |
|---|---|---|---|---|
| "Anti Snoring Devices for Sleep, Adjustable Mouth Guard, Snoring Mouthpiece… Snoring Aids for Men and Women" | **£9.99** (was £14.99) | 19 sold | Unisex | https://shop.tiktok.com/gb/pdp/1729593233414003016 (snippet of a related-items carousel); listing https://shop.tiktok.com/gb/pdp/1729932012431186248 |
| "Anti Snoring Mouthpiece" (category page) | **£6.59** | 0 sold | Unisex | https://shop.tiktok.com/gb/c/body-beauty-devices/601664 |
| "Anti Snoring Mouth Guard Oral Silicone Case" (Gozen) | **£19.99** | 1–5 sold | Unisex | https://shop.tiktok.com/gb/pdp/anti-snoring-mouth-guard-by-gozen-soft-silicone-with-travel-case/1729423609037884983 |
| "Adjustable Anti Snore Mouth Guard for Men & Women" | price not in snippet | — | Unisex | https://shop.tiktok.com/gb/pdp/1729454804945439891 |
| Context: mouth tape | £0.95–£9.49 (best seller "Deep Sleep Mouth Tape and Nose Strips… 9714 sold £9.49") | — | "for Men" | category page above; existing £2.64 tape [Doc 1 marketplaces] |

- **Read:** the GB TikTok Shop sits **below Amazon UK** (£8.84–£31.99). It's a sub-£20 unisex bargain bin with almost no sales, and no women-first mouthpiece listing. It doesn't move our £49 anchor; it's another "cheap, built for him" rung to contrast against.
- **Solidity:** snippets only. Prices and sold counts must be confirmed on the page before any live use; the PDPs are captcha-walled.

**So What → do this:** put "TikTok Shop GB £6.59–£19.99 (unisex, ≤19 sold) · TikTok Shop AU n/a (not launched)" in the §15 ladder. Change nothing in the offer.

---

## Tools-used summary (for §20 A)
- Job 1: Playwright (Google Ads Transparency ✅; TikTok Creative Center ✅ logged-out; TikTok Commercial Content Library ❌ captcha) · firecrawl_scrape 🔁 (1 Google page after the local browser was rate-checked) · Winning Hunter ❌.
- Job 2: Meta Ad Library API (`ads_library_search`, 10 queries) ✅ + Playwright ad-page render (10 ads) ✅.
- Job 3: python on data/databank.csv ✅ (no new collection).
- Job 4: firecrawl_search ✅ (snippets) · firecrawl_scrape ❌ (site unsupported) · Playwright ❌ (region redirect + puzzle captcha) · Winning Hunter ❌.

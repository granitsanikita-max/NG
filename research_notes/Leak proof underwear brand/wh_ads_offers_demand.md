# Ads, Offers & Demand — Women's Leak-Proof / Stress-Incontinence Underwear (US)

Research run: **2026-10-10**. Region: United States / English (noted where a figure is global or AU/UK).
Tools: WinningHunter MCP (Meta ad library, Shopify store intelligence, Exploding Topics, TikTok Shop), Firecrawl (Amazon + AliExpress + Shopify product `.js`).
Solidity tags on every figure: **VERBATIM** (page/field opened) · **SNIPPET** (search excerpt) · **DATA** (tool estimate/model) · **INFERENCE** (my reasoning).
WinningHunter credits at start: 17,612 remaining of 20,000 (check_credits, 2026-10-10) [DATA]. Revenue/traffic are third-party SimilarWeb-style models — directional, not reported financials.

---

## §0B — DEMAND & SEASONALITY

### 1. Search trend (Exploding Topics substitute — NOT country-filtered / global)
Google Trends was not pulled via a live browser session this run; per the fallback rule I used WinningHunter **search_exploding_topics** (global volume, not US-filtered — treat as directional). Firecrawl/Trends direct is bot-blocked. [tool substitution noted]

| Topic | Abs. search volume | Growth (ET index) | Trajectory & peak | Tag |
|---|---|---|---|---|
| **Period underwear** | **201,000** | +1.43 (rising) | **RISING.** 15-yr index hit all-time peak 100 in **Feb–Mar 2026** (99 Mar–Apr), secondary summer bump (Jun–Jul ~60–63); troughs Sep–Nov. | DATA |
| Modibodi (brand) | 60,500 | +0.21 | Flat-to-up; peaked 100 in **Mar 2026**, easing since. | DATA |
| Wuka (UK brand) | 14,800 | +2.33 | Strongly rising, all-time high May 2026. | DATA |
| Period aisle | 1,600 | +4.85 | Small but exploding. | DATA |
| Pelvic trainer (incontinence device) | 2,400 | +1.50 | Rising, peaked **Feb 2026**. | DATA |
| "leak proof underwear" exact | — | — | No dedicated ET topic; folds into "Period underwear". | DATA |
| "bladder leaks" / "stress incontinence" | — | — | **No ET topic found** (searched both). | DATA |

**Read:** category search demand is **rising** (period-underwear +143% on ET index, all-time peak early 2026). **Peak months = Jan–Mar** (New-Year "fresh start" + resolution buying), secondary **Jun–Jul**. Incontinence-specific search terms are thinner than period terms, consistent with incontinence buyers being driven more by paid ads than organic search. [INFERENCE]

### 2. Marketplace demand
**Amazon — "leak proof underwear women" & "incontinence underwear women washable"** (firecrawl_scrape, query mode, 2026-10-10) [VERBATIM from SERP]:

| Listing | Price | Rating (n) | "Bought past month" |
|---|---|---|---|
| **Everdries** Comfort Plus Incontinence, 5-Pack | $59.95 | 3.6★ (789) | **500+** |
| WBEAUTALLOVE Mesh Period/Incontinence Panties | $17.98 | 3.9★ (**4.4K**) | 100+ |
| Wearever Cotton Comfort 3-Pack (150 ml) | $36.99 | 3.8★ (**2.5K**) | — |
| ZJHTK 6-Pack (over-60 positioning) | $26.99 | 3.7★ (**1.4K**) | 200+ |
| BATTEWA Washable 5-Pack (50 ml) | $59.90 | 4.0★ (656) | 200+ |
| Generic "Washable Elastic Leak-Proof" | $11.89 | 3.3★ (348) | 300+ |
| ACEJUNE Period Cotton 4-Pack | $26.99 | 4.3★ (132) | 300+ |
| YESWEL Washable 60 ml 5-Pack | $56.98 | 4.3★ (33) | 300+ |
| SUNCHIRI 50 ml 5-Pack | $53.99 | 4.7★ (26) | 200+ |

Amazon demand is **real and broad**: 4–5 listings at **200–500+ units/month**, several with **1,400–4,400 ratings** (years of sales). Everdries itself runs an Amazon listing (789 ratings, 500+/mo). Price band $11.89–$59.90; branded 5-packs cluster $54–$60, generics $12–$30. [VERBATIM/INFERENCE]

**TikTok Shop (US)** — search_tiktok_products, 2026-10-10 [DATA]:
- "leak proof underwear" → returns **snorkel gear only** (matched "leak-proof underwater"). The apparel category essentially does not exist on TikTok Shop.
- "incontinence underwear" → top items are **disposable/washable underPADS**, not underwear: Graphene Incontinence Underpads $9.78 ($4.87k rev/30d, 2,071 sold lifetime, +40% MoM); Washable Incontinence Underpads $11.99 ($74k lifetime rev, 6,205 sold, but −37% MoM, declining).
- **Verdict: TikTok Shop is a weak/pad-dominated channel for this product** ($10–12 pads, modest revenue, declining). Not a launch channel for premium washable underwear. [INFERENCE]

### 3. Ad demand (Meta) — WinningHunter search_facebook_ads, countries=["US"], 2026-10-09/10
Total ad creatives indexed per keyword (US):

| Keyword (US) | Total ads indexed | Sort used | Tag |
|---|---|---|---|
| period underwear | **15,809** (pageactiveads) / 3,824 (longestrunning) | both | DATA |
| bladder leak underwear women | **10,052** | pageactiveads | DATA |
| leak proof underwear | **5,484** | relevance | DATA |
| leak proof underwear incontinence | 5,223 | longestrunning | DATA |
| leakproof underwear | 3,813 | longestrunning | DATA |
| bladder leak underwear | 3,502 | longestrunning | DATA |
| incontinence underwear | 2,880 | longestrunning | DATA |
| pee proof underwear | 482 | longestrunning | DATA |
| washable incontinence underwear women | 142 | longestrunning | DATA |

**Distinct advertisers:** de-duping advertiser page_ids across all category keyword/sort samples (jq over 12 WinningHunter result files, page-1 samples ~20 ads each) yields **54 distinct advertiser pages** active on the category in the US — a crowded, well-funded lane. Queries used: the 9 above plus "leak proof underwear incontinence", "bladder leak underwear women", "Vera Underwear leakproof". [DATA; sample of page-1 results, not full pagination — true advertiser count is higher]

**Longest-running ads (how long top spenders have run):**
- **Everdries** page (101183732574129) has an ad creative indexed since **2023-06-12** → **~1,216 days / ~40 months** still live (re-uploaded creatives reuse the hook). [DATA]
- **Carerspk** (incontinence boxer brief) since **2023-06-30** (~40 months). [DATA]
- Mid-tier evergreen: Parentgiving (Oct 2023), DesignComfort (Nov 2023), The Period Company (Mar 2024), Thinx (Jul 2024), Saalt (Nov 2024). [DATA]

### §0B VERDICT
**GROWING.** Search (period-underwear +143% ET, all-time peak early 2026), Amazon (multiple listings 200–500+/mo, 1.4–4.4K ratings), and Meta (10 category keywords, 5k–16k active creatives each, 54+ distinct US advertisers, 40-month evergreen winners) all confirm durable, growing demand. **Peak months Jan–Mar** (resolution/fresh-start), secondary Jun–Jul. **Launch-timing call:** build creative + funnel through Q4, **go hard Dec–Feb** to catch the New-Year peak; TikTok Shop is not a priority channel (pad-dominated); Meta DR + Amazon are the demand pools. [INFERENCE]

---

## §1 — COMPETITOR SCAN & AD LOG

### A. LONG-LIST (every advertiser/store surfaced — name · domain · #active ads · longest-running ad · region)
Sources: find_similar_shops, get_store_details, and de-duped Meta advertiser set (WinningHunter, 2026-10). Active-ad counts are store-level where a store record exists, else page-sample.

| # | Advertiser / Store | Domain | Active Meta ads | Longest-running ad (start) | Region | Tag |
|---|---|---|---|---|---|---|
| 1 | **Everdries** (DR king) | everdries.com | **2,441** (Oct 9) | 2023-06-12 (~40 mo) | US, global | DATA |
| 2 | Everdries International | shop.everdries.com | 1,678 | — | US | DATA |
| 3 | **Knix** (giant) | knix.com | not on Meta DR (TV/retention) | — | US/CA | DATA |
| 4 | **Thinx / Speax** | thinx.com | ~4 in sample (Tatari TV-led) | 2024-07-16 | US | DATA |
| 5 | **Modibodi** | modibodi.com | present, AU-led | — | AU/US | DATA |
| 6 | **Saalt** | saalt.com | ~10 in sample | 2024-11-28 | US | DATA |
| 7 | **attn:grace** | attngrace.com | small | — | US | DATA |
| 8 | **Jude** | wearejude.com | present (Taboola/Meta) | — | UK (US nascent) | DATA |
| 9 | **Vera's Undies / Vera Cares** (clone) | shopvera / vera-ca / vera-undies | burst (12 in Mar-2026 sample) | 2025-09-30 | US/CA | DATA |
| 10 | **Miriano** (clone, shares PID 7082150330417) | miriano.com | burst | — | US/AU | DATA |
| 11 | **NESLEMY** template (personas "Emma", "Dr. Emberly Reed", Pawjoystore) | swiftbasketc.com, jangoodstore.com | 156 ads 1-mo growth on one page | 2025-12-16 | US/CA | DATA |
| 12 | **Mindsparkl** cluster (Mindsparkl, De-Mindsparkl, .33, 97kk) | ffwn3c-0f.myshopify.com | ~22 in sample | 2026-08-04 | US | DATA |
| 13 | **TryFluxe** | (advertorial) | ~10 in sample | 2025-10-02 | US | DATA |
| 14 | **Orykas** (men's) | orykas.com | ~3 | 2025-08-11 | US/EU | DATA |
| 15 | **Boody** | boody.com / .com.au | ~8 | 2025-09-05 | AU/US | DATA |
| 16 | **The Period Company** | theperiodcompany.com | present | 2024-03-08 | US | DATA |
| 17 | Carerspk (incontinence boxer) | carerspk | ~44 in sample | 2023-06-30 (~40 mo) | US | DATA |
| 18 | Parentgiving | parentgiving | present | 2023-10-10 | US | DATA |
| 19 | NEIWAI | neiwailife | present | 2024-05-24 | US/CN | DATA |
| 20 | Knicked | knickedaustralia | present | 2024-05-29 | AU | DATA |
| 21 | Reddrop (tween period) | reddropco | present | 2024-05-03 | US | DATA |
| 22 | AWWA Period care | — | present | 2024-05-19 | NZ/US | DATA |
| 23 | Uresta (bladder-support device, adjacent) | — | present | 2025-10-02 | US/CA | DATA |
| 24 | Flowelle, Fri Period, Cheeky Cherry, DesignComfort, Worryfree, Forever Yours, Rudie, Apon, Upbri, Instruxo, Substantiag, Respectivelk | various dropship | low-mid each | 2023–2024 | US | DATA |
| + | Supplement/advertorial funnels riding the keyword (NOT underwear): "Susan Coleman", "Laura McKinney", "Women's Bladder Talk", "Dr. Anastasia Chamberlen", "Dr. Lisa Downing", "Nutritionist Katherine Davis PhD", "American Health Support Community", BB Company | — | — | 2025–2026 | US | DATA |

≥25 genuine underwear advertisers + a tail of supplement/advertorial funnels. (find_similar_shops on everdries.com was polluted by the "ever/dries" string match — returned EverDrive/drink/gaming stores; disregarded for category expansion.) [DATA/INFERENCE]

### B. THREE DIRECT COMPETITORS — DEEP SIGNALS
(Most proven spend: Everdries + strongest credible brand on Meta DR + the recurring clone template.)

**B1. EVERDRIES — everdries.com** [DATA, get_store_details + top_ads 2026-10-10]
- Monthly traffic: **239,714** (Sep 2026); collapsed from **1,373,485 (Dec 2025)** → 173k (Jun) → recovering (+1.25% MoM, +38.5% 3-mo off the June floor, but −60% 6-mo). 87.5% US. VERBATIM-field.
- Revenue (modeled): **$1.6M–$2.8M / 30d**; $57k–$100k / 1d. **AOV $91.11.** 
- Time in business: store created **2022-05-17** (~3.4 yrs). Charlotte NC; myshopify = incontinencepanties.myshopify.com.
- Active Meta ads: **2,441** (Oct 9, 2026), up from 1,386 (May) — **still ramping spend while traffic falls** = rising CAC / creative-fatigue churn curve.
- Longest-running ad: since **2023-06-12** (~40 mo).
- Trustpilot **2.5 / 560**, 0% reply rate to 196 negatives. Dominant complaints (WH gap analysis): "leak protection fails even for light leaks" (multiple clusters), "company tells you to still wear a pad", refund/return friction, odor, sizing.
- Stack/upsell (apps): **Slide Cart Drawer (AMP), EG Auto-Add-to-Cart Free Gift (order bump/gift), Intelligems A/B testing**, Klaviyo, Postscript SMS, Loox reviews, Triple Whale, Google/YouTube. Pixels: TT/GO/AD/FB/BN/AX/KV/WP/SA/SP/3W/PS.

**B2. SAALT — saalt.com** (strongest credible brand actively on Meta DR this run) [DATA]
- Traffic **232,250** (Aug 2026), stable (peaked 350k Jan); 64% US. Rev **$900k–$1.6M/30d**, **AOV $49.28**. In business since **2018**. Trustpilot 3.0/18 (tiny sample).
- ~10 active ads in sample; longest-running ad 2024-11-28. Stack: Yotpo, Klaviyo, Postscript, Triple Whale — **no bundle/upsell app surfaced** (lean offer). B-Corp.

**B3. VERA'S UNDIES / NESLEMY clone template** (recurring dropship clone) [DATA]
- Burst-and-die pattern: Vera pages showed 0 persistent ads at times, 12 in a Mar-2026 sample; NESLEMY personas ("Emma"/swiftbasketc.com, "Dr. Emberly Reed"/jangoodstore.com) had **+156 active-ad 1-month growth** on a single page; Mindsparkl cluster (ffwn3c-0f.myshopify.com) ~22 ads. Prices $39.99–$64.54 5-pack. Shares Shopify product ID 7082150330417 (Vera↔Miriano). Vera Underwear Trustpilot 3.5/505; Ultradries 3.5/245 (Everdries competitors list).
- Most-duplicated hook: the NESLEMY "4-Layer Leak-Lock / holds 8oz / not pads, not diapers" advertorial and the "I was a nurse, pads nearly killed me" fear advertorial — reused across many personas/domains. [DATA]

### C. AD LOG — top creatives (one row each: start · days running @2026-10-10 · format · leads-with · verbatim hook)

**EVERDRIES (top 10 Meta creatives, get_store_top_ads 2026-10-10):**
| Start | Days | Format | Leads with | Hook (verbatim first line) |
|---|---|---|---|---|
| 2026-09-10 | 30 | video | upgraded mechanism | "Everdries Have Been Redesigned With Cotton!👇 If you LOVE Everdries but struggle with skin irritation…" |
| 2026-09-11 | 29 | video | upgraded mechanism | "Everdries Have Been Redesigned With Cotton!👇…" (caption: "Finally… Leakproof Underwear Made With Real Cotton") |
| 2026-04-18 | 175 | video | upgraded mechanism | "Everdries just released a new design specifically created for nighttime leaks!!" |
| 2026-04-16 | 177 | video | upgraded mechanism | "Everdries just released a new design specifically created for nighttime leaks!!" |
| 2026-04-20 | 173 | video | upgraded mechanism | (same nighttime hook) |
| 2026-05-18 | 145 | image | upgraded mechanism | (same nighttime hook) |
| 2026-05-18 | 145 | image | upgraded mechanism | (same nighttime hook) |
| 2026-09-10 | 30 | video | upgraded mechanism | "Everdries just released their new Leakproof Highrise Shorts👇 full-coverage…" (caption: "Everdries changed my life") |
| 2026-05-28 | 135 | image | upgraded mechanism | "NEW RELEASE: Everdries Leakproof Shapewear!! Gentle compression…" |
| 2026-05-27 | 136 | image | identity (founder) | "Hi, it's Jess, the founder of Everdries. I want to share a little story about why we created…" |

**CATEGORY AD LOG (one representative/longest-running creative per advertiser; WinningHunter Meta, de-duped):**
| Start | Format | Advertiser | Leads with | Hook (verbatim first line) |
|---|---|---|---|---|
| 2023-06-01 | image | Respectivelk | bigger claim | "😫 90% of women suffer from urine leakage…" |
| 2023-06-12 | image | Everdries (OG) | identity/offer | "Black Friday is here! Grab 5 pairs…made specifically for women 60+" |
| 2023-06-30 | — | Carerspk | mechanism | "This water-proof panel…4 specially created absorbent…" |
| 2023-08-17 | video | Upbri | bigger claim | "😫 90% of women will face the embarrassing problem of urinary incontinence…" |
| 2023-10-10 | image | Parentgiving | plain claim | "Tired of Leaks? This is the BEST Incontinence Solution!" |
| 2023-11-10 | video | DesignComfort | identity | "I'm ditching the bulky pads for good!" |
| 2024-02-22 | video | Cheeky Cherry | plain claim | "FINALLY!! Leakproof undies that are cute, comfy, AND ACTUALLY absorbent🤩" |
| 2024-03-08 | image | The Period Company | identity | "If you flow, you know." |
| 2024-05-03 | video | Reddrop | identity | "Your tween doesn't deserve to wear oversized…pads" |
| 2024-05-24 | dco | NEIWAI | plain claim | "Better Protection, Period. Secure absorbency, so you can go with the flow." |
| 2024-05-29 | carousel | Knicked | identity | "Attention dancers! Knicked™ Period Undies are game-changers…" |
| 2024-07-16 | dco | Thinx | plain claim | "Comfortable & Washable Bladder Leak Underwear…Essential Collection…absorbs leaks" |
| 2024-11-28 | video | Saalt | bigger claim | "Replace your daily panty liners. 9/10 people never go back!" |
| 2025-08-11 | video | Orykas (men) | mechanism | "All men with bladder leaks make the same mistakes ❌…ultra-absorbent solution" |
| 2025-09-05 | dco | Boody | plain claim | "Boody Period & Leak-Proof Underwear. Make the switch…30-day risk-free" |
| 2025-09-30 | video | Vera's Undies | identity | "I'm Closing 70% OFF EVERYTHING. After 34 years of helping women feel confident…" |
| 2025-10-02 | image | TryFluxe | identity | "Discover The Truth About Leak Protections…If you're over 55 and tired of peeing…" |
| 2025-11-08 | image | Laura McKinney (NESLEMY) | identity | "Read This If You Wear Pads for Leaks 👆…I never thought a disposable pad could almost kill me." |
| 2025-12-16 | video | Dr. Emberly Reed (NESLEMY) | upgraded mechanism | "Real Leak Protection—Not Pads, Not Diapers…built for bladder leaks…holds up to 8oz…4-Layer Leak-Lock" |
| 2026-03-06 | video | Vera Cares | plain claim/offer | "Better Than Pads…Vera's Everyday Confidence Sale…Buy 5 pairs, get 1 FREE" |
| 2026-08-04 | video | Mindsparkl | identity | "I'm Eleanor, a Community Health Worker, 73…" (100% Leak-Proof Underwear 4-pack) |
| 2026-09-07 | image | Susan Coleman | upgraded mechanism | "Finally, Organic Underwear that actually works for incontinence…warn every woman who uses disposable pads" |
| 2026-09-19 | video | Perpetualing | mechanism | "Say goodbye to leaks 👋! Vera Underwear…3-layer protection" |

### D. TAKEN MAP (one line per incumbent — owned angle · region · status)
- **Everdries** — "redesigned with cotton / nighttime leaks / 100% leakproof, bulk bundle at fake 50% off" · US+global · **ACTIVE (scaling ad volume, falling traffic)**.
- **Vera / Miriano / NESLEMY / Mindsparkl clones** — "better than pads, 4-layer/8oz, fake founder/nurse testimonial, buy-5-get-1" · US/CA · **ACTIVE but ephemeral (burst-and-die)**.
- **Jude** — "clinical bladder authority + supplement subscription, 1 in 3 women, backed by 3000+ studies" · UK (US nascent) · **ACTIVE**.
- **attn:grace** — "skin-safe / sustainable / B-Corp bladder-leak, pads+bags+underwear" · US · **ACTIVE (small, recovering)**.
- **Knix** — "period-proof + everyday intimates, body-positive, retention/upsell + TV" · US/CA · **ACTIVE but ceded Meta DR**.
- **Thinx / Speax** — "period pioneer; Essential bladder-leak collection; thin/discreet" · US · **ACTIVE on TV (Tatari), abandoned aggressive Meta DR**.
- **Modibodi** — "the original period underwear & swimwear, widest range, permanent 50% off" · AU/US/EU · **ACTIVE but softening**.
- **Saalt** — "sustainable period underwear + cups, eco, risk-free" · US · **ACTIVE (stable, lean offer)**.
- **Boody / NEIWAI / The Period Company / Knicked / Reddrop** — niche period angles (bamboo, tween, dancers, budget) · US/AU · **ACTIVE (small)**.
- **Orykas** — "men's bladder-leak bamboo boxers" · US/EU · **ACTIVE (men only — open flank on women's premium)**.
- **Un-owned / abandoned:** a *trustworthy, real-brand, incontinence-positioned* washable underwear sold on Meta DR with retention economics — the exact lane Everdries/clones occupy but with none of their 2.5-star liabilities, and that period brands have vacated. [INFERENCE]

---

## §8 — MARKET SOPHISTICATION (lead classification & tally)
Classified every captured competitor **underwear** ad (Everdries top-10 creatives + 39 de-duped category representatives = **49 ads**). Excluded: romance-novel click-bait, male catheters, bladder/pelvic **supplement** advertorials, recovery devices (they ride the keyword but aren't the product).

| Leads with | Count | Share | Who |
|---|---|---|---|
| **Upgraded mechanism** (cotton redesign, 4-layer, 8oz, nighttime, organic, shapewear) | **11** | 22% | Everdries (×9), NESLEMY/Dr. Emberly Reed, Susan Coleman |
| **Identity / experience** (founder story, "women 60+", "if you flow you know", nurse/anti-pad fear advertorial) | **15** | 31% | Everdries OG, DesignComfort, The Period Co, Reddrop, Knicked, Vera's, TryFluxe, Laura McKinney, Mindsparkl, Everdries "Jess", etc. |
| **Plain claim** ("leakproof underwear", "comfy & absorbent", "better protection") | **12** | 24% | Thinx, Boody, Vera Cares, NEIWAI, Cheeky Cherry, Flowelle, Fri Period, Parentgiving, Mindsparkl.33/97kk, OffersDaily, Rudie |
| **Bigger claim** (quantified: "90% of women", "#1 worldwide", "9/10 never go back") | **6** | 12% | Respectivelk, Upbri, Instruxo, Substantiag, Worryfree, Saalt |
| **Mechanism** (how it works, un-upgraded) | **5** | 10% | Carerspk, Apon, Orykas, De-Mindsparkl, Perpetualing |

**Tally headline: mechanism-led (mechanism + upgraded) = 16 of 49 (33%); identity/experience-led = 15 of 49 (31%); plain-claim = 12 (24%); bigger-claim = 6 (12%).**

**Sophistication read (bimodal):** The **scaled DR spenders** (Everdries, NESLEMY/Mindsparkl clones) have pushed to **Stage 4–5** — *upgraded mechanism* ("redesigned with cotton", "4-layer leak-lock, holds 8oz", "nighttime design") **and** *identity/experience* fear-advertorials ("I was a nurse, pads nearly killed me", "women 60+"). The **smaller/period brands** (Thinx, Boody, NEIWAI, Cheeky Cherry) still lead with **Stage 2 plain claims**. A new entrant **cannot win at the plain-claim level** — the top of the market is already at upgraded-mechanism + identity. Entry wedge = a **credible, verifiable upgraded mechanism** (named founder, real testing, real reviews) that neutralizes the clones' biggest liability (fake testimonials + 2.5-star absorbency failures). [INFERENCE]

---

## §15 — COMPETITOR OFFERS, PRICE LADDER & GAPS

> **Cart walk note:** A live headless PDP→cart→checkout walk was **not executed this run**; offer structures were captured instead via Shopify product `.js` (exact variant/compare-at), `get_store_details` (installed apps → upsell inference, AOV), and Amazon/ad copy. Non-Shopify stores (Jude) and burst-dead clones (Vera/Miriano currently dark) — "cart not walked — captured from `.js`/store-intel/prior ad copy."

### Per-competitor blocks

**EVERDRIES** (everdries.com) [VERBATIM `.js` + get_store_details, 2026-10-10]
- Hero bundles (Comfy & Discreet): **5-Pack $59.95 / compare $124.75 (−52%, $11.99/unit)**; **10-Pack $99.95 / $249.50 ($10.00/unit)**; **15-Pack $129.95 / $374.25 ($8.66/unit)**. Bikini 5-pack $39.95; Comfort Plus 5-pack $53.99/$124.75.
- **No subscription** (confirmed in `.js`: "No variant is a subscription or selling plan"). Compare-at is a permanent fake anchor.
- Upsell/bumps (INFERENCE from apps): Slide Cart Drawer + **EG Auto-Add-to-Cart Free Gift** (gift-with-purchase bump) + Intelligems A/B. Free gifts advertised in ad copy. Guarantee/returns: restrictive — not returnable once washed/used; buyer pays return shipping; no prepaid labels (Trustpilot complaints). Discount mechanics: "50% off" sitewide + bundle ladder + urgency ("sale ends"). Weak/missing: no subscription, no genuine guarantee, 2.5★ trust.

**VERA'S UNDIES / VERA CARES / MIRIANO** (clone template) [prior notes + ad copy 2026]
- "Signature Leakproof 5-Pack" ~$39.99–$64.54. Offer ladder: **Buy 5 get 1 free / Buy 10 get 2 free / Buy 15 get 4 free**; "Up to 60% OFF + Free Gifts"; "closing 70% off everything" scarcity. Shares PID 7082150330417 (Vera↔Miriano). No subscription. Stack: bundle app + Convertful popup + Klaviyo. Guarantee thin; burst-and-die brand equity. Cart not walked — pages intermittently dark.

**KNIX** (knix.com) [DATA, get_store_details]
- Apparel one-time purchase, **AOV $109.50**; traffic 732k (Aug), rev **$3.1M–$6.2M/30d**; 83% US; Trustpilot **4.5/674**, 92.6% reply. Leakproof underwear ~$23–$38/pair; bundles via **AIOD automatic discounts** (buy-more-save-more); **Rebuy** post-cart upsell engine; **Northbeam** attribution; Okendo+Trustpilot reviews; Klaviyo. No subscription core. Guarantee: generous but final-sale friction on promos (complaint theme). Weak/missing: **not incontinence-positioned**; premium price; ceded Meta DR.

**THINX / SPEAX** (thinx.com) [DATA]
- Rev **$821k–$1.37M/30d**, traffic 157k (Sep, declining), 59% US. Prices (no compare-at = no discounting): Everyday Comfort Brief/Hi-Waist **$20**, Basic Brief/Hi-Waist **$27**, Thong $31, Bladder Hiphugger **$41**, Lace Hi-Waist $43, Sleep Shorts $61. Bladder SKUs are top sellers. Stack: Attentive SMS, Yotpo, **SwellRewards loyalty**, Loop Returns, **Tatari (TV)**, Friendbuy referral, Global-e (intl). No subscription, no bundle-discount app. Weak/missing: no urgency/offer, abandoned Meta DR, PFAS reputation scar.

**MODIBODI** (modibodi.com) [DATA]
- Rev **$1.0M–$1.7M/30d** (AUD), traffic 254k (Sep, softening from 345k Jul); AU 36.5% / US 31.6%. Trustpilot **3.5/1,191**, only 21.7% reply (service decline). **Permanent ~50%-off** posture (every SKU PROMO-tagged): underwear AUD $18.50–$28 (compare $37–$56), activewear $35–$53, laundry bag $7.19. No subscription. Stack: Criteo, Emarsys, Nosto, Okendo+Yotpo+Reviews.io, SwellRewards, smsbump, Triple Whale, Upfluence, Loop Returns, Gorgias. Weak/missing: service responsiveness, "received used hygiene product" complaints, permanent discounting erodes margin/price integrity.

**JUDE** (wearejude.com) [prior notes, Oct 2026]
- Supplement-LED subscription model (not Shopify — custom Next.js). Underwear **£16.60** (£24.95 high-waist at Boots/H&B); supplements £25–£26.63/mo. Bundles Day&Night Duo £99 / Strength&Sleep Duo £99 ("SAVE 30%"). **Subscribe & save up to 33%**; 20% off first order (quiz); £10 referral both sides; **90-day first-order refund**. Trustpilot 4.5/~5,565. Strongest recurring-revenue model; underwear is an attach item. UK-centric. Cart not walked (non-Shopify).

**attn:grace** (attngrace.com) [DATA]
- Rev **$180k–$360k/30d**, traffic 35k (Sep, recovering), 79% US. Now **pads + body-care led** (washable underwear de-emphasized in current bestsellers): Heavy/Moderate/Light Pads ~$17, Disposable Odor-Proof Bags 50ct $17.50 / 150ct $45, deodorant $14, body oil $28, calm spray $19.99; **Custom Bundle builder**. **Recharge Subscriptions = core** (subscription-led). Stack: Klaviyo, Okendo, Gorgias, **RevenueHunt Shop Quiz**, **Intelligems A/B**. B-Corp, Good Housekeeping award. Weak/missing: small scale, eco-niche TAM, underwear now secondary to pads.

**SAALT** (saalt.com) [DATA]
- Rev **$900k–$1.6M/30d**, AOV **$49.28**, traffic 232k, 64% US. Leakproof Cotton Brief **$29**, Comfort Brief **$39**, Comfort CloudShort **$47**; cups/discs $32–$35, wash $14. No compare-at discounting, **no bundle/upsell app** (lean). Stack: Yotpo, Klaviyo, Postscript, Triple Whale. B-Corp. Weak/missing: no offer/urgency, period-first (not incontinence), thin reviews.

### 4-column summary table
| Competitor | Entry price | Best offer | Biggest gap |
|---|---|---|---|
| Everdries | 5-pk $59.95 ($12/unit) | 15-pk $129.95 ($8.66/unit) at fake −52% + free gift | No subscription, no real guarantee, 2.5★ absorbency failures |
| Vera/Miriano clones | ~$40–$65 5-pk | Buy-5-get-1 / up to 60% off + gifts | No brand/retention, fake testimonials, burst-and-die |
| Knix | ~$23–$38/pair | AIOD buy-more-save + Rebuy upsell | Not incontinence-positioned; premium; off Meta DR |
| Thinx/Speax | $20–$41 | (none — flat pricing) | No offer/urgency; abandoned DR; PFAS scar |
| Modibodi | AUD $18.50–$28 | Permanent ~50% off | Service decline; discounting erodes margin |
| Jude | £16.60 underwear | Subscribe & save 33%; 90-day refund | UK-only scale; underwear is an attach item |
| attn:grace | pads ~$17 | Recharge subscription + custom bundle | Small; underwear de-emphasized vs pads |
| Saalt | $29–$47 | (none — lean) | No offer/urgency; period-first |

### Table stakes / Best-in-class / Nobody offers
- **Table stakes:** bundle/multipack pricing (3/5/10-pack), reviews widget (Loox/Okendo/Yotpo), Klaviyo+SMS, free shipping over a threshold, "better than pads / 100% leakproof" promise.
- **Best-in-class:** Knix's **Rebuy + AIOD** post-cart upsell/auto-discount engine (drives $109 AOV); Jude's **subscribe-&-save 33% + 90-day refund** recurring model; Everdries' **free-gift order bump + Intelligems A/B** on a fake-anchor bundle ladder.
- **Nobody offers (white space):** a **credible incontinence brand with a genuine money-back guarantee + a replenishment subscription on washable underwear** sold on Meta DR. No incumbent pairs real trust (named founder, real reviews, real absorbency testing) with retention economics in the incontinence lane. [INFERENCE]

### PRICE LADDER (same/closest product: washable leak-proof incontinence underwear, ~5-pack)
| Tier | Source | Real price (NOT welcome-teaser) | Per-unit | Tag |
|---|---|---|---|---|
| **Floor** | AliExpress wholesale | 5-pack listings **$3.71–$13**; singles $6.34–$7.05 | **~$0.75–$2.60/unit** | SNIPPET (AliExpress SERP, 2026-10-10) |
| Amazon generic | Amazon US | $11.89–$29.99 (3–6 pack) | ~$2–$6/unit | VERBATIM |
| Amazon branded | Amazon US (BATTEWA/SUNCHIRI/YESWEL/Everdries 5-pk) | $53.99–$59.95 | ~$11–$12/unit | VERBATIM |
| TikTok Shop | TikTok Shop US (pads/underpads, not apparel) | $9.78–$11.99 | — | DATA |
| Clone DTC | Vera/Miriano/NESLEMY | $39.99–$64.54 5-pk | ~$8–$13/unit | DATA/prior |
| **Everdries DTC** | everdries.com | $59.95 5-pk / $129.95 15-pk | **$8.66–$12/unit** | VERBATIM |
| Period-brand DTC | Saalt / Thinx | $20–$47 **per pair** | $20–$47/unit | DATA |
| **Ceiling** | Knix / Jude | Knix $23–$38/pair (AOV $109); Jude underwear £16.60 + £25/mo supplement | highest effective basket | DATA |

**Floor-to-ceiling:** product costs **<$2.60/unit at AliExpress**; the market sells it DTC at **$8.66–$47/unit** (3.3×–18× markup). Everdries/clones occupy the $8–$13/unit bundle floor on a fake anchor; period brands hold the $20–$47/unit premium per-pair ceiling. A credible incontinence brand can price at **$12–$18/unit in bundles** (above the clone floor, below the period-brand ceiling) and still hold 85%+ gross margin. [INFERENCE]

---

## TOOLS RUN
- ✅ `check_credits` — 17,612 credits remaining.
- ✅ `search_exploding_topics` (period/bladder/incontinence) — used as the **Google-Trends substitute** (🔁 global, NOT country-filtered; live Trends via browser not run — ET fallback per instructions).
- ✅ `search_facebook_ads` ×6+ this run (+ reused prior-session category files), countries US, de-duped advertisers via `jq` across 12 result files.
- ✅ `get_store_details` — everdries, saalt, knix, thinx, modibodi, attngrace.
- ✅ `get_store_top_ads` — everdries (meta).
- ✅ `find_similar_shops` (everdries) — 🔁 polluted by name-string match; disregarded for expansion.
- ✅ `brief_competitor` (everdries) — store candidates + opportunities.
- ✅ `search_tiktok_products` — "leak proof underwear" (snorkels only) & "incontinence underwear" (pads/underpads) → category weak on TikTok Shop.
- ✅ Firecrawl `firecrawl_scrape` — Amazon ×2 (query mode, review counts + bought-past-month), Everdries hero `.js` (exact variant/compare-at), AliExpress via `firecrawl_search` (price floor).
- 🔁 **Cart walk (playwright headless PDP→cart→checkout)** — NOT executed; offer structures captured via Shopify `.js` + `get_store_details` apps + ad copy instead (labeled per competitor).
- ❌ Live Google Trends 5-yr US — not run (Trends/Firecrawl bot-blocked; used Exploding Topics substitute, labeled not-country-filtered).
- ❌ `get_tiktok_product` metric slices — skipped (category has no real leak-proof-underwear TikTok Shop products worth slicing; pads only).
- ❌ Full Meta advertiser pagination (5 pages/keyword) — used page-1 samples across 12 keyword/sort files instead; **54 distinct advertisers is a floor, true count higher**.

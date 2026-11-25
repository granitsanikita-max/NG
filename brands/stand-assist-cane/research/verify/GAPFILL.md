# GAPFILL — paste-ready blocks (gap-fill agent, 2026-11-25)

Tools: Winning Hunter MCP (connected; credits 13,834 at start; ≈2 credits per call, ~35 calls used) · Firecrawl. Raw JSON + notes: `verify/gap/` (advertisers_dedup.json, *_p*.json, store_details_notes.md, blockC_notes.md, shoplc_lp_dup2.json, brief_naxir.json). Exact text edits: `verify/fix_GAP.json`.
Solidity tags: DATA = tool estimate/index · VERBATIM = page or ad text read · SNIPPET = search-result text · INFERENCE.
Source tags proposed: Doc 1 **[S70]–[S73]**, Doc 2 **[S20]**, Doc 4 **[S70]**. They are numbered high to avoid clashing with K1/K2/K3. Renumber if needed.

---

## Block A — §0B ad demand: advertiser count (Winning Hunter `search_facebook_ads`)

**Method.** `searchkeyword=adtext` is needed. With the default "All" field, any single word matches, so "stand up cane" in AU returned 114,245 ads, mostly novels and apps. Filters: `countries=AU`, ads last seen **2026-10-26 → 2026-11-25** (running in the last 30 days), `sort_by=longestrunning`. Pages fetched with the `scroll` cursor, at most 5 pages. Advertisers de-duplicated by (page name, page_id) in Python. DATA [S70].

| Query (ad text) | AU ads, last 30 d | Read | Note |
|---|---|---|---|
| "stand up cane" | **0** (also 0 all-time) | — | nobody uses this phrase in ad copy |
| "walking cane" | **146** | 100 (5 pages) | CA 128 · GB 192 (page 1 read) |
| "walking stick" | **475** | 60 (3 pages; page 4 timed out twice) | mostly advertorial noise |
| "mobility aid" | **32** | 32 (all) | — |
| "folding cane" | 141 all-time | 20 | page 1 = advertorial noise only, not paged |

**66 distinct advertiser pages. The AU-targeted ones fall into these groups:**
- **9 stand-assist / second-handle canes:** Naxir · Swarous-C · Audenora · HomWarmer-J · Ahlwo Nature · Lavenao-Store · Zavrlyprime · Second.Vibrantnice · Merancoria.es style (clarioy.com).
- **9 LED/SOS "smart canes" with no stand claim:** LuvianPros · Thegiftnorth · Rrighodew · Londyx · SimpleLife Supply and Warm Living Space (both on vantinolf.com) · AGEasy (India) · Margie Osborne (telescopic) · Noomoriey.
- **15 cane-seat / stool sellers.**
- **4 other mobility:** Handly AU · Woobiliy crutches · Mobility and Wellness · Lumbowrap.
- **3 décor canes.**
- **21 advertorial / arbitrage pages.**

**Longest-running in AU:** Swarous-C "✨ Standing Mobility Aid – Adjustable, Stable & Easy to Use! ✨", ad id 4489805514498935, **2026-04-20 → 2026-11-23 (~217 d)**. Its LED + alarm + 4-leg folding stick ad 1939521313313117 has run since 2026-07-09 (VERBATIM ad text, DATA dates).

**Freshness.** Apart from Naxir and Swarous, every stand-assist cane page started on or after 2026-10-21. **6 of the 9 started in Nov 2026:**
- Ahlwo Nature: 23 ads since Nov 4.
- Lavenao: 7 ads since Nov 13.
- Zavrlyprime: Nov 10.
- HomWarmer-J: Nov 2.
- Second.Vibrantnice: Nov 18.
- Merancoria: US$119.99, Nov 24.

Ahlwo, Lavenao, Thegiftnorth, Noomoriey and Zvorna all use the same product handle, `every-step-matters-smart-walking-cane`, so they look like one supplier template (INFERENCE). → **A clone wave is entering AU this month (INFERENCE from DATA).**

**⚠ Correction for Doc 1 §0B/§1.** "Naxir is the only verified Meta advertiser for this product in AU" is **wrong** under this sweep: 8 other second-handle canes targeted AU in the last 30 days. Naxir is still the biggest by ad count and traffic. Edit E1 in fix_GAP.json fixes the line.

Copy from the stand-assist clones (ad text, VERBATIM, DATA dates):
- **Ahlwo Nature** (ahlwoplus.com, US$45.99, AU/CA/NZ/GB, Nov 4–23): "🤲 Dual‑handle ergonomic grip, easier to stand up from sitting" … "🎁 Thoughtful practical gift for elderly family members". Lavenao uses identical copy.
- **Audenora** (audenora.com, US$59.90, AU/CA/NZ/US, Oct 21–25): "50% OFF Smart Walking Cane – Today Only! Make standing up easier and feel more confident with every step. … 🪑 Second support handle for easier standing 💡 Built-in LED light + SOS alarm".
- **Merancoria.es style** (clarioy.com, US$119.99, AU only, Nov 24): "STANDING UP SHOULD NOT FEEL LIKE A FULL-BODY NEGOTIATION. … The dual-handle ergonomic design gives helpful leverage when standing".
- **Zavrlyprime** (US$22.99, AU only, Nov 10–11): "🤝 Stand-Up Handle — Extra support when getting up 🚨 SOS Alarm".
- **HomWarmer-J** (€40.95, AU/GB + EU, Nov 2): "Wait... a walking cane with a flashlight, alarm, TWO handles, and more?! … From getting up from a chair to navigating dim spaces".

**Family-buyer / gift lines in AU-targeted ads (wedge pressure-test; K1 owns the wedge call).** All are ad text, VERBATIM:
- **Handly AU** (car-door handle, A$49, AU-only, 84 active ads; ad 1872910727820144, Nov 14–24). It leads with the adult child: "\"I've been getting out of cars for 60 years.\" Sound familiar? That's the answer, every time you offer to help. He doesn't want a cushion. He doesn't want your arm. He definitely doesn't want anything that looks like a mobility aid. … Let him say no. Then let him try it."
- **SimpleLife Supply** (vantinolf.com smart cane, US$25, AU/US/GB, ad 1645653010380305, Nov 12–21). It leads with the gift: "🎁 You want the people you care about to keep their independence … This smart walking cane is that practical gift."
- **Ahlwo / Lavenao.** Gift appears only as a bullet ("Thoughtful practical gift for elderly family members").

None of the second-handle canes in AU *leads* with the adult child. Two non-stand-assist products do.

---

## Block B — §1 shop signals

**Shop LC (shoplc.com).** `get_store_details` (DATA [S71]):
- **Monthly visits:** Oct 2026 **1,246,933**. Mar–Oct range 1.24M–2.04M. 97.75% US · 0.21% CA.
- **Shipping:** Shopify ships to **US + CA only (not AU)**.
- **Store age:** the Shopify store was created 2026-04-16 (a replatform). Shop LC itself is an established TV retailer in Austin, TX, with 25,001 products.
- **Revenue:** whole site US$8.8M–16.2M per 30 days.
- **#1 bestseller in both Oct and Nov 2026:** "Soulsmart Black 2 Handles Foldable Smart Easy Up Cane with LED Light", US$49.99. Tags include `meta-cane`, `fb-campign`, `last-3days-aired`.
- **Apps:** FoxCart, Attentive, Intelligems A/B, Klaviyo, Northbeam, TikTok, Yotpo.
- **Trustpilot:** 4.5 from 34,524 reviews.

**Shop LC cane ads.** `search_facebook_ads` with keyword "shoplc.com/pages/soulsmart", searchkeyword=landingurl, min_duplicates 2, sort longestrunning → **22 ads, all US-only** (DATA + VERBATIM ad text) [S71]:
- **Most-duplicated:** ad 2270049840416976, dup 4, DCO, **Jun 26 → Aug 31 2026 (66 d)**: "I got this for my mom and she hasn't stopped talking about it — folds into her purse, lights her path, and gives me peace of mind knowing she has that SOS alarm."
- **Longest-running (66 d, tied):** that ad, plus 2068219457097222 "Say goodbye to ordinary canes! Soulsmart has a self-standing base, dual handles & built-in light. … Get it now for $39.99" and 1927937161209994 "POV: you finally found a cane with an LED light, an SOS button, and a 60% off price tag."
- **Earliest cane ad:** 4001090643522215, **May 21 2026**: "If you have a parent, grandparent, or loved one who deserves to feel safe and independent, they need this cane." → ⚠ Doc 1's "cane ads since Oct 7 2026 (50 d)" undercounts. Shop LC has run cane ads since at least May 2026.
- **Other family lines (US):** 1002043872712399 "The man who gave you everything deserves a walk without worry. 💙" (Jun 29–Jul 21) · 1453527230158116, landing page /pages/soulsmart-give-them-more-independence: "Forget the candles and gift cards. Get them something that actually changes their day, every day." (Sep 3–Oct 9).
- **Stand-up line:** 1429893519022512 "Standing up is the hard part. The second handle makes it the easy part." (Sep 19–Oct 1).
- **So what:** in the US, the adult-child angle is already run by a 1.2M-visit retailer. That backs AU-first.

**StrongArm (strongarmcanes.com).** `get_store_details` returned **not_found** (with and without www.). Firecrawl on similarweb.com/website/strongarmcanes.com failed on every engine. → Traffic stays **not available**. It was tried, not skipped.

**`find_similar_shops` naxir.co** → 19 results, matched only on "name/domain + category heuristic", all with similarity_score 0 (Nadir, Nazir, Navir, Noxir: jewellery, fashion, perfume). **0 cane stores** (DATA [S73]).
**`brief_competitor` naxir.co** → store candidates naxir.co plus name noise (shopkaxi, nait.co, nakie.co). For Naxir: owner GB, Shopify created 2023-02-17, 33,948 visits, 304 active ads. Top scaling ads are all Naxir / Healthy Living (K1's area). **No new names** [S73].
→ Long-list expansion came from the Block A keyword sweep instead. fix_GAP edit E4b adds **14 long-list lines (15a–15n)**. None of these advertisers were in Doc 1 or Doc 4, except that the BalanceGuard product is already #7 (Vyvras).

---

## Block C — TikTok + Google + TikTok Shop (DATA [S72])
- **TikTok ads, "cane", AU:** 2 ads in total, a candy-cane chocolate (2025) and a PAYME folding cane-seat (2024). **0 stand-up cane ads.**
- **TikTok ads, "walking stick", AU/GB/CA:** 25 ads, top 10 all irrelevant (survival stick, Insta360, pillowcases). **No family-buyer or post-op cane angle on TikTok ads** in AU, GB or CA.
- **Google ads, "walking cane", AU:** 10,889 hits from a loose word match, top 10 unrelated. This can't be used as a count.
- **Google ads, domain naxir.co:** **89 creatives**; advertiser NAXIR LTD (AR08311189599581896705), **40 active**. Shopping/display headlines include "Naxir StandSecure Cane | Walking Stick With Support Handle | LED Flashlight & Alarm" (from Sep 8 2026, US) and "StandSecure - Orthopedic Support Cane" (Aug 26, US). One search creative since 2024-10-31 lists AU, US, GB, CA and IE. No family or post-op headline in the 5 read. Transparency: https://adstransparency.google.com/advertiser/AR08311189599581896705?region=anywhere
- **TikTok Shop (`search_tiktok_products`, 30 d, sorted by units):**
  - **AU:** "stand up cane" **0**, "cane" **0**. No AU listings are indexed, so **the AU rung stays empty (tool coverage, not proof of absence).**
  - **US:** "stand up cane" 0. "walking cane" → **Shop LC Soulsmart 2-handle LED/SOS quad cane: US$49.99–61.09 (avg $55.54), 35 sold in 30 d, 307 lifetime, US$17,051 lifetime revenue, 19 reviews, score 3.8**, launched 2026-05-10. REHAND self-standing folding canes: $32.99–42.89, 46 sold/30 d; $46.79, 33 sold/30 d. Top seller by units is a $52.78 skull décor cane (337/30 d). https://app.winninghunter.com/tiktok-shop/product/1732312039907430795?period=30

---

## Block D — Demographics (SimilarWeb)
`firecrawl_scrape https://www.similarweb.com/website/naxir.co/` with formats ["query"], 2026-11-25. Result: "Total Visits Last 3 Months … <100K" · "Age Distribution … **No Data to Display**" · "Gender Distribution … **No Data to Display** · Female-- · Male--" (VERBATIM).
- Similarweb's own page has no age or gender data for naxir.co because the site is too small.
- The Alexandria similarweb provider has no demographics capability.
- StrongArm's Similarweb page is blocked.
→ **Doc 2 §3 demographics stay INFERENCE.** This is now a documented attempt (edit E9).

---

## Job 5 — X quotes v3-080 / v3-081 / v3-082
Firecrawl searched each exact quote, then retried with `inurl:status` and handle variants. **Every hit is the profile URL only.** No status URL was found:
- v3-080: x.com/Bigdai100. The snippet adds the date "**Oct 9, 2024**".
- v3-081: x.com/shitCayleVsays, plus sotwe.com/shitcaylevsays. ⚠ The real text ends "…it's the goddamn **marathon of hope**". The bank and doc truncate it.
- v3-082: x.com/JacquiG_Author. Fuller snippet: "She's all skin and bone & eats next to nothing. Gets exhausted just walking a few metres. But so freaking stubborn! Won't use her walker unless I tell her to."

→ **Mark v3-080, v3-081 and v3-082 as `UNVERIFIED`** in databank.csv (solidity column). They are removed from Doc 2 by edits X1–X4. They appear in no other doc.
- Bank counts are left as they are; the rows stay in the bank, flagged.
- If the orchestrator excludes UNVERIFIED rows from counts: hard_to_stand_from_couch 29→28 (AC 2→1) · lost_spouse_now_alone 4→3 (AC 3→2) · parent_refuses_help 34→33 and parent_stubborn_pride 34→33 (AC 31→30) · fall_happened, worry_about_parent and lives_alone each −1.

Replacements (all VERBATIM rows not used elsewhere in the docs):
- **Swipe #18** → "dread low chairs" [v3-027](https://www.youtube.com/watch?v=MmHaz1wYxyA&lc=Ugwzi0oRHq2j17LHd4V4AaABAg) (2).
- **Swipe #30** → ★ "the stubborn incapacitated parent" [v1-036](https://www.reddit.com/r/AgingParents/comments/1wi4hnw/comment/pa9ewjw/) (4).
- **Trigger 9 (lost_spouse) quote** → v3-046 (YouTube, VERBATIM, widow): "Shouting for help would be useless since I am a widow and have no neighbours near enough to hear anything."

---

## Job 6 — §10B "none in bank" cells (python over all 664 rows; failed_solution tag + text regex; quotes already in Doc 1–3 excluded)
| Alternative | Cell | Result |
|---|---|---|
| 12 Lift chair | Horror | **none in 664 rows**. 13 rows mention lift chairs; the only negatives (v1-221, v1-224) are already used. |
| 13 Sit-to-stand technique | Horror | **none in 664 rows**. 25 rows checked; negatives v3-001, v3-025, v3-036 and v3-009 are already used. **New Like:** "I was able to get up quickly from a deep couch without using my hands at all!" [v3-002](https://www.youtube.com/watch?v=_Rl0DG_p4Yg&lc=UgwXU2CxsjVitzHAdhl4AaABAg) (YouTube, VERBATIM; the poster is 57 and "terribly obese") |
| 14 Crutches | Like | **none in 664 rows**. 6 crutch rows; v2-082 calls crutches "almost disposable" (a dislike, already used). |
| 15 Couch cane / stander | Horror | **none in 664 rows**. Only dislike left: v1-228 "I saw they make a couch cane but none of them are made for heavy people." The row is already used in §10B walker, so it was not added. |
| 16 Smartwatch | Horror | **none in 664 rows**. v1-191 is a shower fall where the wearer's son got them up, not a watch failure. |
| 17 LegXercise | Like | **none in 664 rows**. All 4 LegXercise rows are 1–3★. |
| 18 Furniture risers | Dislike / horror | **none in 664 rows**. 3 tagged rows, all positive; v1-001 and v1-026 are toilet risers. |

Edits T1–T7 in fix_GAP.json replace "none in bank" with these results.

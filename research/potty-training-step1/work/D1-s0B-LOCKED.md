# §0B · Demand & Seasonality — LOCKED-market addendum (2026-10-06, after the §11 lock)

**Adds to, does not replace:** work/D1-s0B.md. Its category numbers still stand: "potty training" flat-to-up, the product term "potty training underwear" rising, Amazon reusables ≥14K units/month on page 1, TikTok Shop ~$134K/30d. This addendum tests the **locked segment** (5–9-year-olds, daytime accidents): its own search terms, the **Aug–Sep school-start** hypothesis, big-size marketplace demand, and the new Meta proof from supplement brands.

**Verdict (segment):**
- **Demand is real but invisible in search.** Every school-age term runs at ≈0–7 where "potty training underwear" = 100. She does not Google it; she asks other parents.
- **School-start peak: NOT confirmed in search.** "potty training" and "potty training underwear" bottom out in **Sep–Oct**. Aug is elevated only as the tail of the Jun–Jul peak. The segment's own posts *do* cluster in Aug–Oct (22 of 54 dated school-age posts = 41% vs 25% expected), so the school-start moment is real in conversation, not in search (INFERENCE; post dates are estimates).
- **Launch timing (unchanged from the lock):** creator seeding + story pre-sell in **Nov–Dec**, scale for **January**. Add a **"back to school" creative wave from late July to September**, aimed at the conversation spike, not at search.

## 1 · Search trend — Google Trends, US, 5 years (playwright-skill ✅)
Method: Playwright headless Chromium (global install, proxy CA trusted via the NSS store; no TLS bypass) loaded trends.google.com and saved the `widgetdata/multiline` JSON. Weekly index, Oct 2021 → Oct 2026. The `search_exploding_topics` fallback was not needed (➖).

**Comparison A** [U30] (same chart, so values are comparable):

| Term (US) | 2022 | 2023 | 2024 | 2025 | 2026 YTD | Peak week | Read |
|---|---|---|---|---|---|---|---|
| potty training underwear (category reference) | 20.4 | 25.7 | 32.5 | 48.3 | **68.5** | May 17–23, 2026 (100) | Category still rising |
| sensory underwear | 0.2 | 0.2 | 0.9 | 0.8 | **9.1** | Apr 12–18, 2026 (40) | New in 2026, tiny |
| training pants size 8 | 0.2 | 0.0 | 0.2 | 0.3 | 6.8 | Apr 12–18, 2026 (43) | Spike in spring 2026 only |
| daytime wetting | 0.0 | 0.0 | 0.3 | 0.0 | 2.4 | Jun 21–27, 2026 (19) | Near zero |
| big kid training underwear | 0.0 | 0.2 | 0.2 | 0.0 | 0.0 | May 2023 (10) | Effectively zero |

**Comparison B** [U31]:

| Term (US) | 2022 | 2023 | 2024 | 2025 | 2026 YTD | Read |
|---|---|---|---|---|---|---|
| potty training | 70.7 | 70.5 | 69.2 | 71.6 | **79.4** | Problem term up ~11% in 2026 (matches wave 1) |
| wetting pants | 1.0 | 1.1 | 1.0 | 1.0 | 0.9 | Flat, ~1% of "potty training" |
| pull ups 5t | 0.1 | 0.4 | 0.4 | 0.7 | 0.7 | Tiny, slowly up |
| kids incontinence underwear | 0.0 | 0.0 | 0.0 | 0.0 | 0.3 | Effectively zero |
| daytime accidents | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | Effectively zero |

**Month profile (5-year averages) — the school-start test:**

| Month | potty training [U31] | potty training underwear [U30] | sensory underwear (solo) [U32] | daytime wetting (solo) [U32] | wetting pants (solo) [U32] |
|---|---|---|---|---|---|
| Jan | **80.2** | 37.0 | 1.9 | 0.0 | 51.7 |
| May | 73.5 | 39.2 | 12.4 | 4.5 | 51.5 |
| Jun | 79.4 | 44.1 | 4.5 | **13.4** | 53.7 |
| Jul | **81.5** | **46.5** | 1.2 | 2.2 | 54.7 |
| **Aug** | 76.0 | 44.5 | 2.3 | 2.0 | 49.0 |
| **Sep** | **63.6** | 35.1 | 3.1 | 0.8 | 53.8 |
| Oct | **58.8** (trough) | **23.3** (trough) | 1.8 | 0.0 | 57.7 |
| Apr | 70.9 | 35.1 | **15.7** | 2.2 | **58.1** |

- **Result: Aug–Sep does NOT beat Jan or May–Jul in search** for any term. Sep–Oct is the trough for the category terms.
- Solo low-volume terms are noisy (many zero weeks below Google's threshold). "sensory underwear" peaks Apr–May 2026 (a single 2026 surge drives the average); "daytime wetting" has one Jun 2026 spike; "wetting pants" is flat all year. No school-start pattern in any of them.
- **Conversation test (INFERENCE):** of the 54 locked-segment rows with an estimated Reddit date, **22 fall in Aug–Oct** (Aug 11, Sep 5, Oct 6) vs 13.5 expected if spread evenly, and 16 in May–Jul, 1 in Jan (tally on work/2C-databank.csv; dates are ±1 month estimates from post IDs, and search ranking is not random).

## 2 · Marketplace demand for big sizes
### Amazon (US) — `firecrawl_scrape` `formats:["query"]`, 2026-10-06
| Listing | Size / type | Price | Ratings | Bought past month | Tag |
|---|---|---|---|---|---|
| MooMoo Baby 10-pack **9T** (B0CZ34MF49) | 2T–9T trainer | $29.74 (**$2.97/pair**) | 3,290; 72% 5★ / **9% 1★** | not shown | DATA [U9][U10] |
| MooMoo Baby **2T-9Y** (B0C36FXQRL) | trainer | $35.99 | 3,290 | not shown today (wave 1: 900+) | DATA [U9]; [M17] |
| "Potty Training Underwear … Dinosaur **8-10Years**" (B0H1HL64KX) | trainer to 10 | $18.99 | 330; 65% 5★ / **16% 1★** | not shown | DATA [U9][U11] |
| EZ Moms 10-pack **5T-6T** (B0BWXH5T5D) | trainer | $31.99 | 373 | **100+** | DATA [U9] |
| TIICHOO boys incontinence boxer briefs 5-pack | big-kid absorbent | $31.99 | 122 | **100+** | DATA [U8] |
| FUVVRVAL boys incontinence briefs (day & night) | big-kid absorbent | $29.99 | 89 | **100+** | DATA [U8] |
| Carer boys washable incontinence, age 4–18 (3-pack; size 10 4-pack) | big-kid absorbent | $41.24 / $39.99 | 25 / 29 | not shown | DATA [U8] |
| Hanes boys overnight underwear 3-pack | night | $17.30 | 116 | 50+ | DATA [U8] |

- **Read:** big-size reusable demand on Amazon is **real but small**: hundreds of units a month per listing, against 2K–3K+ for toddler reusables and 10K+ for disposables (wave 1 [M17]).
- **The quality gap is visible in the big sizes:** MooMoo 9T leakage mentions are **116 negative of 180** and absorbency 65 of 156; the 8–10Y Dinosaur pair has **16% 1★** and 30 of 43 leakage mentions negative ("These are not leak proof Not even slight accident it all comes out") [U10][U11] (DATA / SNIPPET).

### TikTok Shop (US) — Winning Hunter `search_tiktok_products`, 30d, 2026-10-06
- "training underwear big kids": the relevant results are **all toddler-sized** (BIG ELEPHANT 10-pack $40.99, 722 units / $24.1K; PeekabooCo 1–5T 624 units, +115%; BIG ELEPHANT girls / boys; Snug Cub 1–5T). **No 5–9 / size 6–12 listing** in the results. The rest are adult shapewear and gym "training underwear" (noise) [U29].
- "incontinence underwear kids": only adult underpads (no children's product) [U29].
- **Read:** the big-kid shelf on TikTok Shop is **empty** (open), consistent with 0 US TikTok ads for "training underwear" [W6].

## 3 · Ad demand — new Meta proof: supplement brands scale on school-age wetting
Winning Hunter, US, 2026-10-06 (DATA):

| Advertiser | What they sell | Ads / scale | Traffic & revenue | Read |
|---|---|---|---|---|
| **Saphire** (trysaphire.com) | Kids' mood / focus gummies + a bedwetting page and an e-book "From Wet Sheets to Sleepovers" | **103** ads to the domain in the WH US index; persona pages "Sarah Mitchell" (**419** active), "Dr. James Harper" (178), "Try Saphire" (98). Wave-1 snapshot: 684 + 226 + 149 [W3][W4] | 188,362 visits (Aug 2026, from 15,289 in Dec 2025); 30d revenue est. **$870K–$1.6M**; AOV $39.08; US 65.6% [U20][U26] | The same parent of a 7-year-old, reached at scale with **first-person story** copy ("My 7-year-old wakes up happy…") |
| **Bloomwise / Hello Bloom Kids** (hellobloomkids.com) | Kids' "meltable" supplements | 420 active on page ("He had accidents at school at six years old") [W5] | 139,388 visits (Aug 2026, from 828 in Jan); 30d revenue est. **$748K–$1.35M**; AOV $58.12; US 90.8% [U21] | Fastest-growing advertiser on this parent: ×168 traffic in 7 months |
| "accidents at school" (adtext, US) | — | 9 ads, **all supplements**, 0 underwear [W5] | — | The school-accident pain is being bought on Meta, by people who don't sell underwear |

**Read:** the parent of a school-age child with accidents is **reachable and buying on Meta right now**, at ~$0.8–1.6M/month per brand (DATA estimates). Nobody sells her underwear there.

## 4 · Verdict (segment)
| Question | Answer | Evidence |
|---|---|---|
| Growing / stable / declining? | **Category growing** ("potty training underwear" 20 → 69 since 2022). **Segment search ≈ flat at near zero**; "sensory underwear" and "training pants size 8" appeared only in 2026 | [U30][U31] |
| Peak months | Category: **Jan; May–Jul**; trough Sep–Oct. Segment conversation: **Aug–Oct** (22 of 54 dated posts) | [U30][U31]; tally |
| Does Aug–Sep school start beat the toddler peaks? | **No, not in search.** Yes in forum conversation (weak, INFERENCE) | §1 |
| Money proven? | Yes, indirectly: big-size reusables 100+/month per Amazon listing; supplements on the same parent at ~$0.75–1.6M/month | [U8][U9][U20][U21] |
| Competition in the segment | **Thin:** 0 big-kid listings on TikTok Shop; 0 underwear ads on "accidents at school"; big-size Amazon listings with 9–16% 1★ | [U29][W5][U10][U11] |
| Launch timing | **Nov–Dec** seeding → **Jan** scale (unchanged). **Late Jul–Sep "back to school" creative wave**, aimed at the conversation, not search | — |

## So What → do this
1. **Don't buy search as the main channel.** School-age terms have ≈0 volume. Keep a small exact-match Google campaign for "training underwear size 8 / 10" and "sensory underwear" only.
2. **Reach her where the supplement brands do:** Meta broad + first-person story pre-sell (real creators only, §2B), and TikTok creators and TikTok Shop, where the big-kid shelf is empty.
3. **Calendar:** Nov–Dec seed → Jan scale → **late-Jul–Sep "school-day" wave** (spare pair in the backpack, teacher note). Don't expect a search spike in September; expect a conversation spike.
4. **Win Amazon's big-size complaint:** the MooMoo 9T / 8–10Y listings fail on leakage. The stated, pour-tested capacity per size is the answer (§13).

## Sources
- [U8] Amazon search "kids incontinence underwear boys washable": https://www.amazon.com/s?k=kids+incontinence+underwear+boys+washable, firecrawl_scrape query, 2026-10-06 (DATA).
- [U9] Amazon search "training underwear big kids size 8 10": https://www.amazon.com/s?k=training+underwear+big+kids+size+8+10, 2026-10-06 (DATA).
- [U10] Amazon MooMoo Baby 9T 10-pack: https://www.amazon.com/dp/B0CZ34MF49 ("Customers say" aspects + star split), firecrawl_scrape `maxAge:0`, 2026-10-06 (DATA / SNIPPET).
- [U11] Amazon "Potty Training Underwear … Dinosaur 8-10Years": https://www.amazon.com/dp/B0H1HL64KX, 2026-10-06 (DATA / SNIPPET).
- [U20] Winning Hunter `get_store_details` trysaphire.com, 2026-10-06 (DATA).
- [U21] Winning Hunter `get_store_details` hellobloomkids.com, 2026-10-06 (DATA).
- [U26] Winning Hunter `search_facebook_ads` keyword trysaphire.com, `searchkeyword: landingurl`, countries US, `sort_by: longestrunning`: total 103, 2026-10-06 (DATA; saved to a file and read with `jq`).
- [U29] Winning Hunter `search_tiktok_products` keywords "training underwear big kids" and "incontinence underwear kids", country US, 30d, 2026-10-06 (DATA).
- [U30] Google Trends US 5y comparison A: https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=daytime%20wetting,sensory%20underwear,big%20kid%20training%20underwear,potty%20training%20underwear,training%20pants%20size%208, Playwright headless, 2026-10-06 (DATA).
- [U31] Google Trends US 5y comparison B: https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=potty%20training,daytime%20accidents,kids%20incontinence%20underwear,pull%20ups%205t,wetting%20pants, 2026-10-06 (DATA).
- [U32] Google Trends US 5y solo: https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=daytime%20wetting · …&q=wetting%20pants · …&q=sensory%20underwear, 2026-10-06 (DATA).
- [W3][W4][W5][W6] Winning Hunter searches, 2026-10-06 (DATA), defined in work/D2-s3A.md.
- [M17] Amazon "potty training underwear" (wave 1), work/D1-s0B.md.
- Conversation-month tally: inline Python on work/2C-databank.csv (locked cut, `~YYYY-MM (est. from post ID)` rows), 2026-10-06.

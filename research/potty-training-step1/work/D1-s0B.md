# §0B · Demand & Seasonality (real numbers)

**Verdict:**
- **Demand is stable and growing.** The problem term is flat-to-up; the product term is rising off a small base.
- **Peak months:** January and May–July. **Trough:** September–October, which is where we are now (2026-10-06).
- **Launch timing:** build and test in Oct–Nov while it's quiet. Be scaled by late December for the January peak. Run a second push Apr–Jul ahead of fall daycare and preschool deadlines.

## 1 · Search trend — Google Trends, 5 years, US
Method: `playwright-skill` (headless Chromium) loaded trends.google.com and captured the `widgetdata/multiline` JSON. ✅ It was not blocked, so the `search_exploding_topics` fallback was not needed.

| Term (US, weekly index, yearly avg) | 2022 | 2023 | 2024 | 2025 | 2026 YTD | Read |
|---|---|---|---|---|---|---|
| potty training (the problem) | 55.1 | 54.9 | 54.0 | 55.8 | **61.9** | Flat 4 years, then **+11% in 2026**. 5-year peak week May 17–23, 2026 (index 78) [M13] |
| potty training underwear (the product) | 1.0 | 1.2 | 1.7 | 2.4 | **3.5** | **3.5× since 2022.** Small but steadily rising (the category is being created) [M13] |
| potty training pants | 1.2 | 1.2 | 1.2 | 1.5 | **4.1** | Rising sharply in 2026 [M14] |
| toddler training underwear | 0.7 | 0.8 | 0.9 | 1.1 | 1.6 | Rising [M14] |
| bedwetting (adjacent, night) | 31.4 | 30.7 | 31.7 | 34.6 | **53.3** | **+54% in 2026** [M16] |
| "training pants" | 8.0 | 7.2 | 7.8 | 9.8 | 32.1 | Spike Mar–Jun 2026 to 100. **Excluded**: the term is ambiguous (TikTok Shop "training pants" results are mostly men's work and gym pants [M20]) — INFERENCE |

**Month profile, "potty training", US 5-year average** [M13] (DATA):
- **Jan 62.5** (peak)
- Feb 56.1 · Mar 55.5 · Apr 55.3 · May 57.3
- **Jun 61.8 · Jul 63.7** (peak)
- Aug 59.4
- **Sep 49.6 · Oct 45.7** (trough)
- Nov 48.7 · Dec 53.5

The product term "potty training underwear" peaks **Apr–Jun** (2.4–2.7).

**Expansion markets** (same method, terms "potty training, toilet training, potty training pants"; DATA [M15]):

| Country | Trend | Peak months |
|---|---|---|
| **UK** | "potty training" up 39.9 → 50.0 → 52.5 → 55.4 → 57.1 → **62.6** (2021→2026): fastest growth of the four | **Jul (68.0), Aug (66.7)**, around the Reception start in September |
| **AU** | "toilet training" is the local term (57.8 vs "potty training" 37.1) | **Jan (45.5)**, Dec, Feb (school year starts late Jan) |
| **CA** | "potty training" stable at ~57–65 | **Jan (69.4), Jul (68.8), Aug (66.8)** |

## 2 · Marketplace demand
### Amazon (US) — `firecrawl_scrape`, `formats:["query"]`, 2026-10-06
**"potty training underwear"** [M17]: 57 of 77 results show a "bought in past month" badge (DATA).

| Listing | Type | Price | Ratings | Bought in past month |
|---|---|---|---|---|
| Pampers Easy Ups Size 5 / Size 6 (124 / 104 ct) | Disposable | $36.90 | 46.6K | **10K+ / 10K+** |
| Goodnites Boys Nighttime S/M 44 ct | Disposable (night) | $24.23 | 28.2K | **10K+** |
| Pull-Ups Boys / Girls 3T-4T 112 ct | Disposable | $38.15 | 25.3K / 33.7K | **8K+ / 7K+** |
| Easy Ups Size 4 (140 ct) | Disposable | $36.90 | 46.6K | 7K+ |
| Hanes Boys' Potty Training Underwear, Light Leaks 7-pk | Reusable | $13.85 | 811 | **3K+** |
| MooMoo Baby Potty Training Pants (cotton) | Reusable | $32.99 | 17.7K | **2K+** |
| Hanes Toddler Girls' Potty Trainer, Light Leaks 6-pk | Reusable | $15.00 | 2.4K | 2K+ |
| "Toddler Potty Training Underwear for Boys Girls" 10-pk | Reusable | $32.99 | 3.4K | 1K+ |
| Hanes (3 other SKUs) | Reusable | $11.72–$19.00 | 149–2K | 1K+ each |
| MooMoo 2T-9Y | Reusable | $35.99 | 3.2K | 900+ |
| Bluey 7-pk w/ chart (Amazon exclusive) | Reusable | $22.99 | 668 | 700+ |
| Disney Pixar Cars 7-pk / Minnie | Reusable | $16.39 / $26.00 | 3.1K / 21.3K | 500+ / 400+ |
| BIG ELEPHANT | Reusable | $28.89–$31.49 | 10.7K | 200+–300+ |

- **Read:** reusable training underwear on page 1 sums to a **floor of ≈14K+ units a month** across its biggest distinct listings. Disposable training pants sum to **≈52K+ a month** (badge lower bounds; INFERENCE).
- Reusables are a real, proven, mass category.
- **Disposables still outsell them roughly 3–4× by listing badge**. That's the pool to convert.

**"reusable training pants toddler"** [M18]: 47 badges.
- Gerber 8-pk cover + trainer: 700+.
- "Toddler Potty Training Underwear" 10-pk: 1K+.
- Upairy's own Amazon listings show **no badge at a 10-pack $27.19 (76 ratings)**, and 100+ at $33.99 (163 ratings).
- So the DTC leader is weak on Amazon.

### TikTok Shop (US) — Winning Hunter `search_tiktok_products` country US → `get_tiktok_product` metrics + history, 2026-10-06
| Product | Price | 30-day units / revenue | Trend | Lifetime | Tag |
|---|---|---|---|---|---|
| BIG ELEPHANT "Helps Kids Feel Wetness Cues" (1729569671740888020) | $25.49 | **2,093 / $52.36K** | −39.4% (30d). Revenue 90d $187.2K, 180d $329.3K. Daily units 38–137 through Sep 2026 | 25,647 units / $653.7K | DATA [M21] |
| BIG ELEPHANT 10-pack "NOT Diapers… Limited Absorbency… Daytime Use Only" | $40.99 | 722 / $24.10K | −20.8% | 8,464 | DATA [M20] |
| BIG ELEPHANT Boys 10-pack | $25.49 | 657 / $16.27K | −21.0% | 5,466 | DATA [M20] |
| **PeekabooCo 6PCS (launched 2026-06-29)** (1732439062662713947) | $18.42 | 624 / $11.64K | **+115%**. 7d $4.4K; 3 creators | 946 | DATA [M22] |
| "Plain Solid… Waterproof Diaper Training Pants" 6-pk | $18.81 | 373 / $7.34K | −11.6% | 3,379 | DATA [M20] |
| BIG ELEPHANT 6/10 "Light Absorb" | $26.99 | 343 / $9.57K | +1.8% | 4,839 | DATA [M20] |
| BIG ELEPHANT Girls 10-pack | $31.29 | 307 / $9.72K | −36.7% | 599 | DATA [M20] |
| BIG ELEPHANT 2-in-1 detachable liner (new Jun 2026) | $29.99 | 98 / $2.90K | — | 160 | DATA [M20] |

- **Read:** training underwear on TikTok Shop US does about **$134K in 30 days across the top 8 listings**, and BIG ELEPHANT is ~86% of it ($114.9K).
- The September dip matches the Trends trough.
- A no-name newcomer (PeekabooCo) doubled in 30 days, which shows **the shelf is open** (INFERENCE).
- The adjacent potty-seat category is bigger: the Orzbow 2-in-1 seat did $71.7K in 30 days [M20].
- TikTok Shop country filter used: US only. UK, CA and AU were not checked in this run (➖, not needed for the US launch decision).

## 3 · Ad demand — advertisers running this right now
**Winning Hunter `search_facebook_ads`, `countries: US`, 2026-10-06.** Four keywords (product, problem, 2 synonyms) plus a landing-URL pass:

| # | Keyword | Settings | Pages | Stop reason |
|---|---|---|---|---|
| k1 | "potty training underwear" (product) | lastseen ↓ | 2 | No new advertiser on p2: 39/40 rows were UpAiry's "Emma's Mom Hacks" |
| k2 | "potty training" (problem) | lastseen ↓ | 3 | p2–p3 were pet pads, odor, adult supplements |
| k3 | "training pants" (synonym) | `searchkeyword: adtext` | 2 | No new advertiser (UpAiry personas + Legends gym pants) |
| k4 | "training underwear" (synonym) | adtext, `max_active_ads: 290` to step below UpAiry | 1 | 100% Kereisa Collens (UpAiry) |
| k5 | "potty" | `landingurl`, `max_active_ads: 70` | 1 | Small players appear |

- The fresh pulls were merged with the 1,006-row same-day corpus from 45 prior searches (A-paid-ads-map method).
- All files were de-duplicated with `jq` + Python: 75 result files, **1,316 unique ad IDs** [M23].
- **Correction to the prior file:** A-paid-ads-map said "`country=US` returned 0 rows". Today it works (k1: total 3,389 ads).

**De-duplicated advertisers (page = advertiser) with a relevant ad last seen 2026-09-06 → 10-06** (DATA [M23]):

| Group | Count | Who |
|---|---|---|
| **Reusable training underwear / pants sellers** | **19 brands** (27 Facebook pages) | **UpAiry** (6 pages: UpAiry, Emma's Mom Hacks, Raising Toddlers with Bec, Motherhood with Kate, Kereisa Collens, The Potty Training Guide; plus Tina Tabellen seen in the Ad Library), **Kid Confident** (+ Mom Hacks with Kara), BrightKidCo, Tiny Tots Undies, Rudie Baby (AU), My Carry Potty (UK), Drynimo, Sevona, Kidsmegaworld, Jackie's Kids UK, Fvaulity, Smart Bottoms, Brilliant Kids, Fig For Kids, Mirovanta/ProudPants, Sculptara ("Audrey Miller"), BlossomNest, shopnola ("Raising Toddlers With Emma"), Brolly Sheets |
| ↳ of which US-targeted (WH country field) | **12** | UpAiry, Kid Confident, BrightKidCo, Drynimo, Kidsmegaworld, Fvaulity, Smart Bottoms, Brilliant Kids, Fig For Kids, Mirovanta, Sculptara, BlossomNest |
| Disposable training pants (DTC) | 1 | Alppi Baby |
| Adjacent potty-training advertisers | ≥16 | Leyadoll book (591 page ads), Big Little Feelings course, nematyta potty watch, Begin Health prebiotics, Noa Nest / Cuoeo / Voalsz / Totallyluxe / Suzvo / Scerich / Noomoriey / Viqzes / Lovesmoothhue seats & ladders, vizoyarewards / Mylovely-baby portable potties, Towel Society car-seat covers |
| Excluded noise | — | Potty Buddy (dog), PuppyPad, CloBombs, mynovapaw, Porch Potty, Legends (gym), Emmafy, StimRelief (FR) |

**Longest-running (= proven) US ads, still live** (DATA [M23], ad log):

| Ad | Start | Days | Note |
|---|---|---|---|
| UpAiry 1018072326966650 "My toddler had 7 accidents in one day…" | 2025-05-03 | **519** | |
| UpAiry 1084202340357288 (same hook) | 2025-06-14 | 477 | **Most-duplicated** (3 live copies) |
| Kid Confident "7 accidents" family | 2025-08-01 → 2026-09-25 | **420** | |
| Emma's Mom Hacks 1393921261712863 | 2025-08-22 | 410 | |

**Facebook Ad Library** (browsed headless with `playwright-skill`, "Active ads", 2026-10-06):

| Query | Country | Results | First rendered ads | Tag |
|---|---|---|---|---|
| "potty training underwear" | US | **~950** active | 26 of 28 from the UpAiry network; 1 Pampers Easy Ups; 1 Coterie | DATA [M35] |
| "potty training pants" | GB | **~460** | 28 of 30 UpAiry personas; Nappy Gurus; Rascals | DATA [M37] |
| "daycare potty" | US | ~210 | — | [M36] |
| "potty training underwear" / "toilet training pants" | CA / AU | "No ads match your search criteria" | Low confidence: first US attempts also returned 403 / empty before succeeding on retry | [M38] |

**Other platforms:**
- **Google:** UpAiry Limited runs **56 Google ads** in the US (Search, Display, YouTube). The longest live one has run since 2025-10-15 (354 days) [M31]. **Correction:** A-paid-ads-map said Google was "unverifiable". It is now verified.
- **TikTok ads, US, "potty training":** only 5 ads total. They come from Millie Moon × Ms Rachel (2), Pampers Easy Ups (2, from 2024) and a Newton mattress. **No reusable DTC brand** [M32].

## 4 · Verdict
| Question | Answer | Evidence |
|---|---|---|
| Growing / stable / declining? | **Growing.** Problem +11% YoY, product term 3.5× since 2022, bedwetting +54% YoY | [M13][M14][M16] |
| Peak months | **Jan; May–Jul.** Trough Sep–Oct | [M13] |
| Money proven? | **Yes.** Disposables 10K+/month per listing; reusables ≥14K units/month on Amazon page 1; TikTok Shop ~$134K/30d; the leader is at $1.8–3.4M per month | [M17][M20][M24] |
| Competition | Saturated on Meta (UpAiry ≈1,684 ads, 26/28 of Ad Library page 1). **Thin on TikTok ads** (0 reusable DTC), **thin on TikTok Shop** (one brand + newcomers) | [M23][M32][M35] |
| Launch timing | Build now (Oct trough). Soft-launch Nov–Dec. **Scale for Jan.** Second wave **Apr–Jul** | — |
| Expansion | **UK** fastest-growing search (+57% since 2021) but UpAiry personas already run there. **CA** looks thin in the Ad Library (low confidence). **AU** = "toilet training"; Rudie Baby owns paid | [M15][M37][M38] |

## So What → do this
1. The market is real and growing. Don't spend time re-proving demand.
2. Plan the calendar around **Jan + May–Jul**. Use Oct–Nov (now) to test creatives cheaply before the January surge.
3. Meta is a UpAiry wall: about 26 of every 28 Ad Library results.
   - Plan a **TikTok Shop / creator** leg from day one (open shelf, a newcomer doubled in 30 days).
   - Do not assume Google is open: UpAiry runs 56 ads there.
4. Hold UK/CA/AU for a second wave. Re-check CA with a logged-in Ad Library before betting on it.

## Sources
- [M13] Google Trends US 5y "potty training underwear, potty training, training pants": https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=potty%20training%20underwear,potty%20training,training%20pants. Playwright headless, 2026-10-06 (DATA).
- [M14] Google Trends US 5y "potty training pants, toddler training underwear, reusable training pants, pull ups": https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=potty%20training%20pants,toddler%20training%20underwear,reusable%20training%20pants,pull%20ups. 2026-10-06 (DATA).
- [M15] Google Trends GB / AU / CA 5y "potty training, toilet training, potty training pants": https://trends.google.com/trends/explore?date=today%205-y&geo=GB&q=potty%20training,toilet%20training,potty%20training%20pants (and geo=AU, geo=CA), 2026-10-06 (DATA).
- [M16] Google Trends US 5y "bedwetting, goodnites, night training pants, potty training underwear": https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=bedwetting,goodnites,night%20training%20pants,potty%20training%20underwear. 2026-10-06 (DATA).
- [M17] Amazon search "potty training underwear": https://www.amazon.com/s?k=potty+training+underwear. Firecrawl `formats:["query"]`, 2026-10-06 (DATA).
- [M18] Amazon search "reusable training pants toddler": https://www.amazon.com/s?k=reusable+training+pants+toddler. Firecrawl query, 2026-10-06 (DATA).
- [M20] Winning Hunter `search_tiktok_products` keyword "potty training underwear" and "training pants", country US, 30d, 2026-10-06 (DATA).
- [M21] Winning Hunter `get_tiktok_product` 1729569671740888020, slices metrics + history: https://app.winninghunter.com/tiktok-shop/product/1729569671740888020. 2026-10-06 (DATA).
- [M22] Winning Hunter `get_tiktok_product` 1732439062662713947, slice metrics: https://app.winninghunter.com/tiktok-shop/product/1732439062662713947. 2026-10-06 (DATA).
- [M23] Winning Hunter `search_facebook_ads` pulls k1–k5 (US) + the prior same-day corpus. 75 result files, 1,316 unique ad IDs, de-duplicated with jq/Python, 2026-10-06 (DATA). Ad URLs are in work/ad-log.csv.
- [M24] Winning Hunter `get_store_details` upairy.com, 2026-10-06 (DATA).
- [M31] Winning Hunter `search_google_ads` domain upairy.com, country US: https://adstransparency.google.com/advertiser/AR10820652197935579137?region=anywhere. 2026-10-06 (DATA).
- [M32] Winning Hunter `search_tiktok_ads` keyword "potty training", countries US, 2026-10-06 (DATA).
- [M35] Facebook Ad Library, US, "potty training underwear", Active: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=potty%20training%20underwear&search_type=keyword_unordered&media_type=all. Playwright headless, 2026-10-06 (DATA).
- [M36] Facebook Ad Library, US, "daycare potty", Active: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=daycare%20potty&search_type=keyword_unordered&media_type=all. 2026-10-06 (DATA/VERBATIM).
- [M37] Facebook Ad Library, GB, "potty training pants", Active: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=GB&q=potty%20training%20pants&search_type=keyword_unordered&media_type=all. 2026-10-06 (DATA).
- [M38] Facebook Ad Library, CA "potty training underwear" and AU "toilet training pants", Active, 2026-10-06. Returned "No ads match" (low confidence).

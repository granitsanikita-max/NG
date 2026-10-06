# A: Paid Ads Map of Reusable Potty Training Underwear (US first, then UK/AU/CA)

Prepared 2026-10-06 from Winning Hunter (WH) data: Meta ad search, store details, store top ads, similar shops, TikTok ads and Google ads.

**How to read the numbers**
- Every revenue and traffic figure is a WH estimate. WH reports it as a range, and the report keeps the range.
- "Active ads" is WH's `total_active_ads_on_page` at the time of the snapshot. It moves day to day; for example, Kid Confident showed 177 and later 79.
- Ad IDs are WH `productid` values, which are Meta Ad Library IDs. You can open any of them at `https://www.facebook.com/ads/library/?id=<ID>`.
- Quotes are verbatim from ad copy that WH indexed. Anything I inferred, such as the target avatar, is labelled *(inferred)*.

---

## 0. Method, coverage and data limits (read first)

**Meta searches.** I ran about 45 searches. The ad rows are saved in `scratchpad/potty/fb.jsonl` and my raw notes in `notes.md`.
- **Keywords:** potty training, potty training underwear, training pants, training underwear, toddler underwear, potty, toilet training, still in diapers, pull-ups, bedwetting, padded underwear, big kid underwear, night training, potty training pants.
- **Search fields (`searchkeyword`):** adtext, landingurl, productname, pagename.
- **Sorting:** relevance, pageactiveads (desc), longestrunning, mostrecent.
- **Date windows:** last-seen 2026-07-08→10-06 (90 days), 2026-04-01→10-06, 2026-01-01→10-06, and 2026-03/06-01→10-06.
- **Countries:** GB, AU and CA filters. The `country=US` filter returned 0 rows on every query, so I couldn't use it. US was covered with unfiltered searches.
- **Pagination:** I used scroll on the best queries.
- **Getting past UpAiry:** UpAiry floods every query. To surface smaller players I sorted the `productname` search by page active ads and stepped `max_active_ads` down (650 → 280 → 198 → 128 → 84 → 76 → 55 → 48 → 36 → 20 → 16 → 8).

**Other tools.**
- `get_store_details`: run on 16 domains. Not in the WH DB: raisecalm.com, reviflora.com, mummybuddy.shop, tinytotsundies.com.
- `get_store_top_ads(upairy.com)`: returned UpAiry's full page network.
- `find_similar_shops(upairy.com)`: **useless.** It matched by name only and returned 39 "fairy"/"dairy" stores. UpAiry isn't categorised as a seed, so it could not be run usefully on other competitors either.
- **TikTok** (`search_tiktok_ads`: potty training, training pants, potty): only 11–45 ads in total. **None came from a reusable training-underwear DTC brand in US/UK/AU/CA.**
- **Google** (`search_google_ads`): the keyword search returns unrelated advertisers (fuzzy matching). The `domain=upairy.com` query reports `total: 110` but returns 0 rows. `get_store_top_ads(platform=google)` fell back to Meta. **I could not verify Google Ads for any competitor.** Treat Google as unmapped.
- **Excluded:** pet potty products (PuppyPad, Potty Buddy, pet sprays, PetsWorld), adult incontinence (Dryora, OENKO, Invizi), and non-English stores (Puddleez FR, Miliumia SE, Mijn Hummeltje NL, StimRelief FR).

---

## 1. Market at a glance

**1. UpAiry dominates paid social.**
- About 1,684 active Meta ads across 7 pages, as of the WH snapshot of 2026-10-06.
- 30-day revenue estimate $1.8M–$3.4M; 356k visits in August 2026; 95% of traffic from the US.
- No one else is within 10× on ad volume in this exact product.

**2. Tier 2 brands (real but small, each with roughly 80–310 active ads at their peak):**
- Kid Confident (US)
- BrightKidCo (US; an autism/sensory variant)
- Rudie Baby (AU)
- Tiny Tots Undies (no store data)
- My Carry Potty (UK; potty-first, but also sells training pants)
- Big Little Feelings (a $25 course, not underwear)
- Alppi Baby (disposable training pants)

**3. A "clone ring" of dropshippers copies UpAiry and Kid Confident word for word.**
- "My toddler had 7 accidents in one day": RaiseCalm, Reviflora, Drynimo, Sevona, Mirovanta.
- UpAiry's persona advertorials: Sculptara, shopnola.store, MummyBuddy.
- Fake mom pages: Amelia Leverett, Audrey Miller, Raising Toddlers With Emma/Kate, Mia's/Marcie's Mama Diaries, Theresa Bakker, Mom Hacks with Kara.
- Most of these stores have $0–$38k in estimated revenue or have since pivoted.

**4. The core mechanism claim is fully commoditised.** "They feel the wetness → brain makes the connection; the outer layer stops the mess" appears in at least 10 advertisers under different trademark-style names:
- UpAiry "inner layer lets them feel wet"
- BrightKidCo "Body-Signal Learning Layer™"
- RaiseCalm "TrueFeel™"
- Sculptara "3-layer Feel & Learn"
- ProudPants "Feel-and-Contain"
- Brilliant Kids "Three layers: she feels it"
- Pottiply, Fvaulity, BlossomNest, SunloveKids

**5. The core enemy is also commoditised:** "pull-ups/diapers are why your toddler isn't learning."

**6. Outside Meta, there is almost nothing:**
- TikTok shows only big brands (Pampers Easy Ups, Millie Moon × Ms Rachel) and UK night mats (JOIZI).
- Google is unverifiable (see section 0).

---

## 2. Competitor profiles

### 2.1 UpAiry (market leader)

**Store, landing pages and sample ads**
- **Store:** upairy.com. Shopify; owner in NZ (Wellington); USD; 51 products; store created 2024-03-27. Facebook page "UpAiry" created 2023-09-22.
- **Landing pages:**
  - PDP `/products/potty-training-underwear`, plus variants `-v5`, `-xl` and `potty-training-underwear-preschool`.
  - Advertorial page `/pages/training-underwear`. Persona pages (Bec, Kate, Emma) send traffic here.
- **Sample ads (Meta IDs):** 1003401808796436 and 1010643218000915 (Emma's Mom Hacks, last seen 2026-10-06); 2252948892152220 (UpAiry "UP TO 6 PAIRS FREE").

**Revenue and traffic** *(WH estimates)*
- 30-day revenue $1.8M–$3.4M; 1-day revenue $64k–$121k.
- WH AOV $18.48.
- Visits: 2026-08 356,447 (peak 528,766 in 2026-03). Countries: US 95.4%, CA 3.2%, GB 0.6%, AU 0.4%.

**Active ads (WH page network snapshot)**

| Page | Active ads | Page created |
|---|---|---|
| UpAiry | 762 | — |
| Emma's Mom Hacks | 295 | 2025-08-20 |
| Raising Toddlers with Bec | 287 | 2025-12-06 |
| Motherhood with Kate | 137 | 2026-01-14 |
| The Potty Training Guide | 86 | 2026-07-16 |
| Kereisa Collens | 77 | 2025-03-18 |
| Tina Tabellen | 40 | 2022-08-22 |
| **Total** | **≈1,684** | |

**Longest-running ads**
- Earliest UpAiry ad seen: 2024-04-09.
- Oldest still-live ads: UpAiry page ad started 2025-05-03, last seen 2026-10-04. Emma's Mom Hacks ad started 2025-08-22, last seen 2026-10-06.
- Long runners from 2025-03-29 and 2025-06/07 appear in the relevance results.

**Price and offers**
- Potty Training Underwear $21 (compare-at $29.99). "Original" version $17 (compare-at $35.98).
- Cross-sells: Waterproof Bed Mat $29.99, Bed Wetting Alarm $39.99, Extra Absorbent Inserts $32.99, Banana Potty $24.99, and "UpAiry Tummy Gummies" (a constipation product currently among their top-ranked ads).
- Offers seen in ads: "UP TO 6 PAIRS FREE", "Up to 6 FREE pairs + 68% off with our three step bundle", "Get 3 Pairs Free When you Buy 2".
- Seasonal drops: Back to School, Halloween prints, Mother's Day, Father's Day.
- Subscription: Trustpilot reviewers report a "hidden subscription for free gift gummies" (19 reviews).

**Avatar** *(inferred from copy)*
- Mostly moms of **late trainers aged 2.5–4.5**, under outside pressure: preschool or daycare deadlines, mother-in-law, "Lululemon mom at the playground".
- Also a stay-at-home-mom variant, a budget variant, a dad variant ("Dads — the diaper is the reason it's not working") and a diaper-rash variant (Kereisa Collens).

**Angle and core claim**
- Diapers and pull-ups are the problem ("You're not the problem. The equipment is."). The underwear lets the child feel wetness.
- "Potty Train in Weeks, Not Months"; "potty trained in 3 days" stories; "preschool won't take them in diapers".
- Pseudo-science and history: "92% of children in 1957 were potty trained by 18 months"; "In Vietnam, the average age of potty training is 9 months old"; "Interoceptive delay… fewer than 1 in 10 pediatricians ever check for it"; "Most pediatricians don't tell you how diapers delay potty training".

**Hooks (verbatim)**
- "My son is 4 and a half and he's STILL in diapers full-time." (Emma's Mom Hacks)
- "F*CK POTTY TRAINING (respectfully)." (Emma's Mom Hacks / Raising Toddlers with Bec)
- "My daughter's daycare is kicking her out in 30 days." (Bec)
- "My Chinese mother-in-law laughed when she saw me buying disposables for my 2-year-old." (Bec)
- "My son (26mo) potty trained in 3 days, while his older sister took almost a year." (Emma)
- "My toddler had 7 accidents in one day—it was exhausting and stressful for both of us..." (UpAiry main page, the single most-used copy)
- "How can a pair of toddler underwear cost $21?" (Emma)
- "I've worked in early childhood education for 11 years." / "As a preschool director…" (Kate, authority personas)

**Creative format**
- Of ~320 indexed ads: 212 video, 80 image, 15 carousel, 13 DCO.
- Main page: UGC-style video plus sale statics.
- Persona pages: long-form first-person "story" advertorials, mostly static image with very long copy, plus listicle-style "Ranking the best ways to potty train…" (The Potty Training Guide).

**Funnel:** persona story ad → advertorial page (`/pages/training-underwear`) or PDP → Kaching bundle tiers → UpCart upsell. Apps: GemPages, Klaviyo, Triple Whale.

**Tone and identity:** confessional, raw, profanity-tolerant, high urgency and shame relief ("You're not failing"). The brand presents as a mom-hack product, not a premium brand.

**Reviews:** Trustpilot 3.5 from 435 reviews; replies to only 32% of 124 negative reviews. WH "gaps":
- Hidden subscription for free gummies (19)
- "Training pants leak and do not hold urine as advertised" (12) and "Leakage and poor absorbency" (10)
- Poor communication on delayed orders (7)
- Refunds delayed (5)
- Pads too bulky (4)
- "Made in China, no UpAiry branding" (4)
- Sizing too tight or inconsistent (3+3)
- Shrinks after washing (2+1)
- Urine smell persists (2)
- "Fake marketing and deceptive online presence" (1)
- eBook vs physical book confusion (1)

### 2.2 Kid Confident (closest "real brand" challenger in the US)

- **Store:** kidconfident.co. US (Secaucus NJ); 3 products.
- **Landing pages:**
  - PDP `/products/potty-training-underwear`
  - Listicle advertorial `/pages/5-reasons-they-dont-care-about-accidents` (ads from 2026-06-13)
  - Back-to-school offer page `/pages/btsof-01` (Jun–Sep 2026)
- **Sample ads:** 1022825803911892, 1064748242711473 (last seen 2026-10-06); 1527417952473915.
- **Revenue and traffic** *(WH estimates)*: 30-day revenue $9k–$16k. Visits rose from about 4k to 17,087 in August 2026. AOV about $19.75. WH lists the top country as VN 100%, which looks like a data artifact.
- **Active ads:** 177 on the main page, later 79 (it fluctuates). Plus a new persona page "Mom Hacks with Kara" (15 ads, started 2026-10-04).
- **Longest-running:** earliest ad 2024-11-20. Ads started 2025-03-26/27 and 2025-04-17 were still seen 2026-09-25.
- **Price and offers:** Potty Training Underwear $19.50–$22.99 (102 variants); Big Kid Sizes $19.50; Leakproof Undie Covers for Bedtime, 4-pack $23.99 (compare-at $47.98); Potty Training Playbook ebook $29. Kaching bundles; Intelligems A/B testing. Ad descriptions read "Low Stock Alert".
- **Avatar** *(inferred)*: US parents in the middle of training who are worn out by accidents.
- **Angle:** "the feeling of underwear without the mess of accidents"; mocks the 3-day promise.
- **Hooks (verbatim):**
  - "Ditch the diapers in 3 days? Yeah, right."
  - "My kid had 7 accidents in 1 day while potty training…"
  - "These finally made it click.."
  - "The biggest mistake parents make when potty training their kiddos"
- **Format:** image 35, video 15, DCO 1. Testimonial-style UGC.
- **Funnel:** PDP plus listicle plus offer page.
- **Tone and identity:** plain, helpful, low-drama.
- **Reviews:** no Trustpilot profile.
- **Note:** this "7 accidents in 1 day" copy is the template the whole clone ring later adopted. UpAiry itself ran the identical "Ditch the diapers in 3 days? Yeah, right." copy in Apr–May 2024.

### 2.3 BrightKidCo (mechanism and special-needs challenger)

- **Store:** brightkidco.com. US (Fort Lauderdale FL); 21 products. First product 2026-02-28. The theme file is named "theme-export-muniosa-de-potty-training-underwe…", which suggests it was cloned from a German store.
- **Landing page and sample ad:** PDP `/products/potty-training-underwear`. Sample ad 1121207980499176.
- **Revenue and traffic** *(WH estimates)*: 30-day revenue $115k–$230k. Visits grew from 5,463 in May to 19,689 in August; 100% US.
- **Active ads:** 107, later 37 and then 0 in the latest snapshots (cooling). All 16 indexed ads are video.
- **Longest-running:** first seen 2026-03-24. Latest seen 2026-09-21.
- **Price and offers:** $24.99–$34.99 (PDP $29.99); "40% off today"; "30 Days Potty Trained Promise™ — or your money back"; "Over 100,000 families".
- **Product line:**
  - Standard PTU
  - **"Potty training underwear for sensory-sensitive toddlers… Help Your Child Become Potty Trained in 4–6 Weeks"** ($29.99)
  - "Happy Poop™ Gummies… for Autistic Kids" ($49.99)
  - Mesh wash bags 3× $34.99; Magic Potty Targets + chart $17.98; 2-in-1 Toilet Stairs $69.99; Waterproof Blanket $59.99; Wet bags 3× $39.99
- **Avatar:** parents facing a preschool deadline; toddlers whose "body doesn't send the signal"; autistic/sensory children (product line).
- **Angle:** a named mechanism ("Body-Signal Learning Layer™"); "That's not a readiness problem. That's a product problem."; a time-bound guarantee.
- **Hooks (verbatim):**
  - "You think you still have time to potty train your toddler before school starts. You don't. And if your toddler still isn't trained, the spot is gone."
  - "Beat the preschool deadline!"
  - "If your toddler is still in pull-ups — this is probably why they're not learning."
- **Format:** video (all 16 indexed).
- **Funnel:** PDP.
- **Tone:** urgent and clinical-ish.
- **Reviews:** Trustpilot 3.0 from 2 reviews ("no exchange for wrong size", "ineffective", "unresponsive support").

### 2.4 Rudie Baby (AU leader)

- **Store:** rudiebaby.com.au. WH lists the owner as HK, but the site says "Australian-owned". AUD; 28 products. Afterpay, Judge.me, Klaviyo, Triple Whale.
- **Landing pages:** `/products/toilet-training-underwear`, `/products/toilet-training-pants`, `/collections/bobby-the-bear`, `/products/training-diapers`.
- **Sample ads:** 1070706875529065, 1086124080440356 (last seen 2026-09-29).
- **Revenue and traffic** *(WH estimates)*: 30-day revenue $75k–$135k. Visits grew from 9.1k in April to 14.4k in August; 100% AU.
- **Active ads:** 288 at peak (WH page snapshot).
- **Longest-running:** training-diapers ad from 2024-05-21 (productname search); Black Friday 2025-11-08; current underwear ads since 2026-02-11, seen to 2026-09-29.
- **Price and offers (AUD):** Toilet Training Underwear 24.95; Training Pants 29; 10-pack 101 (compare-at 290); Leakproof Bed Guard 69 (2-pack 129); Plush Leakproof Fitted Sheets 98; Sheet + Guard set 159; "Bobby's Big Potty Adventure" hardcover book 26. Free shipping over $60; "Up to 60% OFF Bobby Bear Bundles" at Black Friday.
- **Avatar:** Aussie parents of kids who are **"nearly there"** (light absorbency) and kids who fight nappies.
- **Angle:** stage-specific product (too trained for pull-ups, not ready for undies); soft bamboo; OEKO-TEX; eco; a storybook mascot (Bobby the Bear).
- **Hooks (verbatim):**
  - "They're doing great. Except for that one accident a day. Sound familiar?"
  - "Is your toddler too trained for pull-ups but not quite ready for regular undies?"
  - "Does your toddler fight you every time you try to put a nappy on? Yeah. Ours too."
- **Format:** image 44, video 14, DCO 7.
- **Funnel:** PDP and collection.
- **Tone:** warm, local ("Aussie-owned"), gentle.
- **Reviews:** no Trustpilot data.

### 2.5 Tiny Tots Undies

- **Store:** tinytotsundies.com (not in WH DB; WH product currency shows CAD/USD). Landing page `/products/bamboo-training-pants-🍭`. Sample ads 1552463912752751, 1594239821730363.
- **Active ads:** 199.
- **Longest-running:** ads started 2025-11-05 and 2025-11-30, still seen 2026-09-27.
- **Price:** not exposed. Offer: "Special offers available — bundles with exclusive gifts".
- **Angle and core claim:** product-spec superiority: "Tiny Tots Undies V2… 4x more absorbent than leading brands", "5 smart layers (including organic bamboo & natural cotton)", "Exclusive hand-drawn designs", "REACH-certified & gentle on sensitive skin", "gently, naturally, without stress"; "Loved by 10,000+ happy parents".
- **Format:** video (4 indexed).
- **Funnel:** PDP.
- **Tone:** soft, design-led and gentle — the only design-led player at scale.

### 2.6 My Carry Potty (UK; potty brand that also sells training pants)

- **Store:** mycarrypotty.com. UK (Poole); 195 products; Klarna, ReCharge, Reviews.io, Gorgias.
- **Landing pages:** `/collections/my-potty-training-pants/products/cow-my-little-training-pants` (£19.99), the potty collection, `/pages/bundles`.
- **Sample ad:** 1063994076808192 (seen 2026-10-04).
- **Revenue and traffic** *(WH estimates)*: 30-day revenue $106k–$163k (whole store). About 54–60k visits per month; US 40.8%, GB 29.7%, CA 12.7%, AU 5.1%.
- **Active ads:** 312 (page); also pages "My Carry Potty USA" and "homelifewithkay".
- **Longest-running:** ads since 2024-04-04 ("SPRING10"). Current training-pants ad started 2026-06-01, seen 2026-10-04.
- **Price and offers:** carry potty £29.99; stickers £4.99 (free over £35–40); "Save up to 30%" bundles.
- **Avatar:** UK parents, including **very early starters**.
- **Angle:** portable, train-anywhere; expert-designed; retail credibility.
- **Hooks (verbatim):**
  - "Am I crazy for potty training my 13 month old?"
  - "Wish I'd bought this on Day 1… 😩"
  - "Designed by ITV's potty training expert Amanda Jenner"
  - "Stocked in John Lewis, Tesco & Target"
  - "Trusted by 1M+ families"
- **Format:** video and DCO.
- **Funnel:** collection and bundles page.
- **Tone:** cheerful, expert, retail-brand.

### 2.7 Big Little Feelings (course, not underwear; owns the "plan/expert" angle)

- **Product:** biglittlefeelings.com/products/potty-training-made-simple, a $25 digital course (25% off sale). Sample ads 1291714636403836, 1057613250196692.
- **Active ads:** 189, 75, 54 or 21 depending on snapshot. Ads seen 2025-11-24 to 2026-10-05.
- **Claims:** "trusted by 500,000+ families", "potty trained over 200,000 kids", "Lifetime access, 30-day money-back guarantee".
- **Hooks (verbatim):**
  - "You bring the undies. We'll bring the plan. 🩲"
  - "THIS IS NOT A DRILL: You *can* potty train your child in three days!"
  - "Another accident. Another refusal. … (We've screamed into many throw pillows.)"
- **Format:** DCO and carousel.
- **Tone:** warm, funny, expert-mom.
- **Relevance:** they explicitly leave the product slot ("the undies") open.

### 2.8 Alppi Baby (premium disposable training pants)

- **Store:** alppibaby.com. HK-owned; disposable diaper DTC.
- **Revenue and traffic** *(WH estimates)*: 30-day revenue $200k–$340k (whole store). Visits 44.7k in August; US 62.8%.
- **Product and offer:** "Alppi Training Pants Bundles" $53.70 (compare-at $63.40), launched 2026-05. Ads: "Buy 1 Alppi Training Pants sample, get 1 free" (`/products/bogo-training-pants-sample`). Appstle subscriptions and memberships.
- **Active ads:** 110–156. Ads started 2026-08-04 and 2026-08-21, seen to 2026-10-04. Sample ads 2174571696451623, 2913338862342397.
- **Angle:** "360° stretch waist, double leg cuffs, Cloudfresh™ fabric"; low-commitment sampling.
- **Format:** static.
- **Reviews:** Trustpilot 3.5 from 7 (chemical odor; inaccurate absorbency).

### 2.9 The clone ring (dropship and persona stores copying UpAiry or Kid Confident)

| Brand / store | Page(s) | Price | Ads / dates | Signature copy (verbatim) | Store data |
|---|---|---|---|---|---|
| **RaiseCalm** shop.raisecalm.com | RaiseCalm (151) | $21 | started 2026-05-30, seen to 2026-08-03; ID 1036123492323043 | "Potty Train in Weeks, Not Months"; "My toddler had 7 accidents in one day…"; "TrueFeel™ Reusable Training Pants"; "UP TO 6 PAIRS FREE — BACK TO SCHOOL"; "⚠️ SALE ENDS IN 2 HOURS"; "★★★★★ Excellent 4.87/5" | not in WH |
| **Reviflora** reviflora.com | "Amelia Leverett" (129) | n/a | 2026-09-04→09-05, IE/GB/NZ/CA; ID 1042346141972864 | "My toddler had 7 accidents in one day…"; "Is potty training going backwards?" | not in WH |
| **Sculptara** shopsculptara.com | "Audrey Miller" (38–53) | $29.99 | started 2026-09-26/10-01, live; ID 1019240321133815 | "BEFORE you buy potty training pants from Amazon, PLEASE read this."; "Do NOT buy potty training pants from Amazon!!"; "3-layer Feel & Learn"; plus UpAiry's "best friend… Melissa… THREE days" story | AU general store; Recharge installed; 30d $0–1k pre-launch |
| **shopnola.store** | "Raising Toddlers With Emma" (10) | $17 | 2026-10-04 | verbatim UpAiry: "92% of children in 1957…", "We lost my daughter's preschool spot.", "**Please STOP using diapers…**" | — |
| **MummyBuddy** mummybuddy.shop | "Raising Toddlers With Kate" | A$53 | 2025-12-25; ID 2073953326693120 | "F*CK POTTY TRAINING (respectfully)." + preschool-letter story (UpAiry clone) | not in WH |
| **buybumkins.com** (uses the Bumkins name; looks separate from the real Bumkins at bumkins.com, unverified) | "Mia's Mama Diaries", "Marcie's Mama Diaries" | $22 | 2026-04-02→05-08; ID 1504713158107104 | "☝️Read if potty training isn't working for your autistic child"; "My level 2 daughter is going to be in diapers until she is 60 years old." | WH: created 2026-04, 0 traffic |
| **Drynimo** | Drynimo (85) | $21 | 2025-10-20→11-20 (dead test) | "My toddler had 5-6 accidents in one day…" | now a beauty store |
| **Sevona** shopsevona.com | Sevona | $25 | 2025-12-15, seen 2026-10-02 | "💦 7 accidents in one day… and I was DONE."; "No More Pee Puddles!" | — |
| **Mirovanta** ProudPants | Mirovanta (3) | $52.95 (8 for $59) | 2026-09-25/26 | "Add up what pull-ups cost you last month."; "Eight pairs are $59, about $7.38 a pair"; "Feel-and-Contain" | — |
| **Pottiply** | Pottiply | n/a; offer Buy 1 Get 2 Free | 2026-03-27→04 (dead) | "A toddler peeing everywhere isn't a phase. It's a home management crisis."; "Pull-ups delay training. The Little Underwear accelerates it." | HK; pivoted to sea-moss gummies |
| **Mezely** | Mezely (0–9) | "Free Today (shipping cost applies)" | 2025-05→12, 2026-06→07 | "Grab a Free Pair… potty train your child in just 2 weeks!" | PL general baby store, 30d $19–33k |
| **Wrapango** | "Theresa Bakker" (35) | n/a | 2026-06-24/26 (portable potty) | "This is what a UV light shows on a public porta-potty seat." | US general store (245 SKUs) |
| **Brilliant Kids** brilliant.kids | Brilliant Kids | n/a | 2026-09-18 | "It's not her. A Pull Up pulls the wet away in seconds…"; "you stop spending over $1,000 a year on Pull Ups"; "They're giving away 100 underwear for free and 70 are already gone." | — |

### 2.10 Small, regional and inactive players

**Active in the past 90 days**
- **Jackie's Kids UK** (jackies-kids.uk/products/pottypants)
  - £14.90; video; started 2026-04-29/30, seen 2026-10-01.
  - Hooks: "🚼 Fewer Accidents, More Confident Steps!" and "😊 From Diapers to Independence Made Simple!"
  - Generic feature list.
- **Fvaulity** (fvaulity.com)
  - $27.99–$29.99; 3–33 ads; started 2026-06-02 / 07-02, seen 2026-10-04.
  - Targets UK/EU and US.
  - Hook: "Potty training got SO much easier once we switched from diapers to training underwear 👶✨"; "100% cotton".
- **Kidsmegaworld** "TootLoo" (kidsmegaworld.com/products/tootloo)
  - $16.90; 109 page ads; started 2026-04-15, seen 2026-09-25.
  - Hook: "🌟 Easy Peasy Potty Training Awaits!"
- **BlossomNest** EasyPotty™ (blossom-nest.com)
  - $13.95; 5–7 ads; started 2026-09-26.
  - Calm, educational tone: "Diapers and potty-training underwear serve two different purposes. Here's what parents should know."
  - Eco and reusable: "Still buying disposable training pants again and again?"
- **SunloveKids** (sunlovekids.com)
  - $32.99; carousel; Jul 2026.
  - Hook: "100% pure cotton… sense wetness".
- **Smart Bottoms** (smartbottoms.com, US cloth-diaper brand; whole-store 30-day revenue est $53k–$95k)
  - **Nighttime trainers.** Comparison demo: "Watch what happens when we put Smart Bottoms Training Pants head-to-head with the 'other brand.'"
  - 13 ads, Aug 2026.
- **Fig For Kids** (figforkids.com; 30-day revenue $10k–$18k)
  - "Fig Potty Training Kit": GOTS organic cotton, 4 pairs + tote + rewards chart.
  - Hook: "The non-toxic journey doesn't stop at diapers." (2026-09-19)
- **Staydry Kids** (AU; staydry.com.au)
  - Bundles; "20% off"; "Up to 30% off EOFY"; Feb/Jun 2026.
- **Brolly Sheets** (NZ/AU)
  - "Snazzi Day Training Pants" + car-seat protection; carousel; 2026-09-03.
  - Hook: "Ready to move on from nappies faster?"
- **My little Darling** (my-little-darling-shop.com)
  - "🎁 Offer: 2+1 FREE"; May 2026.

**Inactive (2024)**
- **Peekaa** (AU): "🇦🇺 100% Aussie Owned & Operated"; Oct–Dec 2024.
- **Blooming Kids**: "End Bedwetting for Good!" with leakproof underwear; Sep–Oct 2024.

**Adjacent products (they compete for the same potty-training budget)**
- **Leyadoll** "Hello Potty" personalised soft book: 591 page ads; long-runners from 2025-10-17 still live 2026-09-26. Hooks: "Potty Training the Playful Way", "Trusted by 16,000+ parents | Featured in British Vogue".
- **Bedwetting alarms:** Unikor "NightGuard™" (455 ads, Oct 2025); Night Ollie (quiz funnel and free ebook); Tinkaly.
- **Night mats:** JOIZI Peapod mats (UK, TikTok).
- **Potty training watch:** nematyta.com, $29.99. Daycare angle: "Potty trained at home… but still stuck in pull-ups at daycare?"
- **Flip-down toilet seat dropshippers:** Suzvo, Noomoriey, Scerich, Viqzes, Lovesmoothhue.
- **Big brands on TikTok:** Pampers Easy Ups ("100% leakproof protection"; "Dads - you don't have to sit on the sidelines…", 2024) and Millie Moon × Ms Rachel training pants (Jan 2026, creator-led, 7.1k likes).

---

## 3. TAKEN map (who owns what)

### 3.1 Angles and claims

| Angle / claim | Owner(s) | Evidence |
|---|---|---|
| "Diapers/pull-ups are why they're not learning" (enemy = diaper) | **UpAiry** (dominant); also BrightKidCo, Pottiply, Brilliant Kids, Mirovanta, Sculptara, BlossomNest, My Carry Potty | "You're not the problem. The equipment is."; "Pull-ups delay training." |
| "Feel the wetness" layered mechanism | **Everyone** (10+): UpAiry, BrightKidCo (Body-Signal Learning Layer™), RaiseCalm (TrueFeel™), Sculptara (Feel & Learn), ProudPants (Feel-and-Contain), Brilliant Kids, Fvaulity, SunloveKids, BlossomNest | section 1, point 4 |
| "Weeks, not months" / "3 days" / "2 weeks" speed | UpAiry, RaiseCalm, Drynimo, Mezely ("just 2 weeks"), Sculptara, BrightKidCo ("1-2 weeks", "7 Days"), Big Little Feelings ("three days") | headlines "Potty Train in Weeks, Not Months" |
| Mocking the 3-day method | Kid Confident ("Ditch the diapers in 3 days? Yeah, right.") | — |
| Preschool/daycare deadline | **UpAiry** (Bec: "daycare is kicking her out in 30 days"; back-to-school copy), BrightKidCo ("the spot is gone"), shopnola, MummyBuddy, Kid Confident (BTS page) | — |
| Late trainer aged 4–4.5 "still in diapers" shame | **UpAiry** (Emma/Bec/Kate), shopnola | "My son is 4 and a half…" |
| Social/MIL pressure, generational stats (1957, Vietnam, Chinese MIL) | **UpAiry** (Bec), copied by shopnola | — |
| Pediatrician-doesn't-tell-you / interoception pseudo-science | **UpAiry** (Kate) | "fewer than 1 in 10 pediatricians…" |
| Authority personas (preschool director, 11-year educator) | UpAiry (Motherhood with Kate) | — |
| Profanity / "F*CK potty training" humour | UpAiry; MummyBuddy clone; Sculptara ("three f*cking days") | — |
| Autism / sensory / special needs | **BrightKidCo** (sensory PDP + autistic gummies); buybumkins.com persona ads ("level 2") — both small and recent | — |
| Accidents / "7 accidents in a day" exhaustion | Kid Confident (origin), UpAiry, RaiseCalm, Reviflora, Drynimo, Sevona, ProudPants | — |
| Money saved vs pull-ups | Brilliant Kids ("over $1,000 a year"), ProudPants ("$7.38 a pair"), Sculptara ("Save $100+ per month") | — |
| Anti-Amazon / "cheap ones don't work" | Sculptara (Audrey Miller) | — |
| "Nearly there / one accident a day" stage | **Rudie Baby** (AU) | — |
| Night-time / bedwetting | Kid Confident (bedtime undie covers), Smart Bottoms (nighttime trainers), UpAiry (bed mat, alarm cross-sell), Rudie (bed guards), JOIZI, Unikor, Night Ollie | — |
| Eco / non-toxic / organic | Fig For Kids (GOTS), Tiny Tots (organic bamboo, REACH), Rudie (OEKO-TEX bamboo), BlossomNest (reusable) | — |
| Design / prints as the hero | Tiny Tots Undies ("hand-drawn designs"); UpAiry seasonal prints | — |
| Expert-designed / retail-credible | My Carry Potty (Amanda Jenner, ITV, John Lewis) | — |
| Plan / scripts / temperament (method, not product) | Big Little Feelings course; Kid Confident ebook; Puddleez (FR) "plan included" | — |
| Very early start (13 months) | My Carry Potty | — |
| On-the-go / car / public toilets | My Carry Potty; Wrapango (Theresa Bakker) | — |
| Diaper rash | UpAiry (Kereisa Collens) | — |
| Dads | UpAiry ("Dads — the diaper is the reason…"); Pampers (TikTok, 2024) | — |
| Licensed character | Millie Moon × Ms Rachel (TikTok) | — |

### 3.2 Avatars

| Avatar | Owner(s) |
|---|---|
| Stressed mom of a 3–4.5 y.o. late trainer under deadline/pressure | **UpAiry** network (by far), clones |
| Mom mid-training, drowning in accidents | Kid Confident, RaiseCalm/clone ring |
| Parent of an autistic or sensory child | BrightKidCo, buybumkins.com (small) |
| Almost-trained kid with 1 accident a day | Rudie Baby (AU only) |
| Eco/organic "clean" mom | Fig For Kids, Tiny Tots, Rudie |
| UK parent wanting portable/early training | My Carry Potty |
| Budget mom wanting cheap/free | Mezely, Pottiply, RaiseCalm (6 free pairs), UpAiry (6 free pairs) |
| Dad | UpAiry (few ads), Pampers |

### 3.3 Tones, formats, funnels and price points

- **Tones taken:**
  - Raw/confessional/sweary (UpAiry)
  - Urgent clinical (BrightKidCo)
  - Plain helpful (Kid Confident)
  - Warm Aussie (Rudie)
  - Soft whimsical design (Tiny Tots)
  - Funny expert-mom (Big Little Feelings)
  - Cheerful retail-expert (My Carry Potty)
- **Formats taken:**
  - UGC/testimonial video (UpAiry, Kid Confident, BrightKidCo)
  - **Fake persona long-form advertorial** (UpAiry plus 8+ clone pages)
  - Sale statics (UpAiry, Rudie)
  - Comparison/demo video (Smart Bottoms only)
  - Listicle (UpAiry "Ranking the best ways…", Kid Confident "5 reasons…")
- **Funnels taken:** persona advertorial → PDP (UpAiry `/pages/training-underwear`); listicle (Kid Confident); offer page (Kid Confident BTS); quiz funnel only in bedwetting (Night Ollie); course (BLF).
- **Price points (single pair or unit):**

| Price point | Who |
|---|---|
| $13.95–$17 | BlossomNest $13.95, shopnola $17, Kidsmegaworld $16.90, UpAiry Original $17, Jackie's £14.90 |
| ~$19.50–$22 (the main cluster) | UpAiry $21, Kid Confident $19.50–22.99, RaiseCalm $21, Drynimo $21, buybumkins $22 |
| $25–$35 | Sevona $25, Rudie A$24.95–29, Fvaulity $27.99, BrightKidCo $29.99, Sculptara $29.99, SunloveKids $32.99 |
| $50+ bundles/kits | ProudPants 8 for $59, Alppi $53.70 (disposable), Rudie 10-pack A$101, Fig kit |

  Offer mechanic everyone uses: "Buy X get Y free" / "up to 6 pairs free".

---

## 4. White space (angles, avatars and identities nobody is running), with evidence

1. **A real, named, trustworthy brand.**
   - The leader has a 3.5★ Trustpilot score from 435 reviews, with complaints of hidden gummy subscriptions, leaks, missing branding and "fake marketing". Its ads come from 6 fake-mom pages, and the clone ring copies the same stories.
   - No one runs an "honest brand" identity: transparent, no fake personas, no hidden subscription, clearly labelled absorbency, real founder or real customers.
   - *Evidence:* UpAiry Trustpilot gaps (section 2.1); persona pages created 2025-08 to 2026-07 (section 2.1); clone table (section 2.9).

2. **Absorbency proof and "it actually holds a pee."**
   - The #1 complaint against the leader is leaking: 12 + 10 reviews plus 2 "leak-proof claim false".
   - Only Smart Bottoms runs a head-to-head absorbency demo, and only for nighttime trainers (13 ads).
   - No one shows a measured pour test with ml or oz, or a "full pee" guarantee for daytime underwear.
   - *Evidence:* UpAiry gaps; Smart Bottoms ad 1095906002779175.

3. **Sizing and fit specialists, including bigger kids aged 4–7.**
   - Complaints: sizing runs small or tight, shrinkage after washing.
   - Only Kid Confident lists "Big Kid Sizes", and it doesn't advertise them.
   - No ad leads with "true-to-size, pre-shrunk, sizes up to age 7/8". This matters because UpAiry's own avatar is the 4.5-year-old.
   - *Evidence:* UpAiry gaps (sizing 3+3, shrink 2+1); Kid Confident bestsellers.

4. **Dads as the buyer and lead.**
   - Only 1 UpAiry ad ("Dads — the diaper is the reason it's not working") and a 2024 Pampers TikTok target dads. No brand identity is built around dads or a "dad-led weekend".
   - *Evidence:* UpAiry copy list (section 2.1); TikTok notes.

5. **Daycare/nanny/grandparent "consistency kit" (training that transfers between homes).**
   - Daycare appears only as a deadline threat (UpAiry, BrightKidCo) or as a watch gadget (nematyta).
   - No one sells a multi-caregiver kit (labelled packs for daycare, grandma's house and the car, plus a caregiver instruction card).
   - *Evidence:* Cindy Perez/nematyta ad "Potty trained at home… but still stuck in pull-ups at daycare?" is the only one.

6. **Regression and second-child/sibling scenarios.**
   - Regression is mentioned only inside Big Little Feelings course copy and one Reviflora line ("Is potty training going backwards?").
   - No underwear brand owns "new-baby regression", "after-illness regression" or "starting over after a failed 3-day attempt" as a primary avatar.
   - *Evidence:* BLF and Reviflora copy.

7. **Poop-specific training (withholding, fear of pooping in the potty).**
   - Every underwear ad is about pee and wetness. Poop appears only as gummies (UpAiry Tummy Gummies, BrightKidCo "Happy Poop™" for autistic kids) and as BLF's "Yes, even the poop stuff."
   - No underwear brand addresses poop accidents or skid-mark containment and cleanup.
   - *Evidence:* UpAiry top-ads list; BrightKidCo bestsellers.

8. **Calm, anti-pressure, "no-deadline" brand voice.**
   - The leader and its clones sell fear: deadlines, shame, "4 and a half and STILL in diapers", MIL ridicule.
   - Only BlossomNest (5–7 ads, launched 2026-09-26) and Tiny Tots ("gently, naturally, without stress") lean gentle, and neither has persona content.
   - A respectful, child-led, "your kid isn't behind" identity is effectively unowned in the US.

9. **UK, CA and AU-specific brands.**
   - UpAiry traffic is 95% US; GB 0.6%, AU 0.37%.
   - UK: only Jackie's Kids (generic), Fvaulity and My Carry Potty's side SKU.
   - AU: Rudie Baby (288 ads at peak) and small Staydry/Brolly.
   - CA: no dedicated advertiser found in any CA-filtered search, only clones and Pee Pals (a mat, 2024–25).
   - Localised language ("nappies", "toilet training", "pants"), £/A$/C$ pricing, local shipping and a "made for UK/Canadian parents" identity are open, especially CA and UK.
   - *Evidence:* UpAiry country split; GB/AU/CA filtered searches (notes).

10. **Subscription done honestly ("size-up club" / grow-with-me replacement).**
    - UpAiry's subscription is the source of 19 complaints. No one advertises a transparent size-up or replacement subscription.
    - Sculptara has Recharge installed but doesn't advertise it.
    - *Evidence:* UpAiry Trustpilot gap; Sculptara apps.

11. **Physical "complete kit" positioned as a system with a plan.**
    - Big Little Feelings explicitly says "You bring the undies. We'll bring the plan." Only Fig For Kids (organic, 1.6k visits) and Rudie (Bobby bundles, AU) bundle product with a guide or chart.
    - No US mass-market brand sells underwear + day-by-day plan + chart + travel kit as the hero offer.
    - *Evidence:* BLF ads; Fig For Kids kit ad.

12. **Platforms: TikTok (and likely Google) are open for this exact product.**
    - WH TikTok ads for "potty training" (13), "training pants" (11) and "potty" (45) show zero reusable-training-underwear DTC brands in US/UK/AU/CA. Only Pampers, Millie Moon × Ms Rachel and JOIZI mats appear.
    - Google could not be verified (section 0), so it is unknown, not proven empty.

13. **Special needs done credibly (not via fake "level 2 autism" moms).**
    - The autism/sensory angle is only touched by BrightKidCo (one PDP, 0–37 ads lately) and a store using the Bumkins name with fake "Mama Diaries" personas (April 2026, dead).
    - A therapist/OT-informed, honest special-needs line is open, but it needs real credibility.

14. **Comparison and value transparency vs pull-ups as the hero.**
    - The cost-per-pair argument exists only in 3 small advertisers (ProudPants, Brilliant Kids, Sculptara), none at scale.
    - A "pull-up cost calculator" or "pays for itself in X weeks" brand identity is unclaimed.

**Hard-to-win spaces** *(my judgment)*
- "Feel the wetness" mechanism
- "Weeks not months / 3 days" speed claim
- Preschool-deadline fear
- Fake mom-persona advertorials
- $21 price point with "up to 6 free pairs"
- "My toddler had 7 accidents in one day" UGC

UpAiry plus 8+ clone pages saturate these; a new entrant would be clone #9.

# NAXIR "StandSecure" — full teardown (P1B, collected 2026-11-25)

Never reuse Naxir's name, photos or videos in our creative (Nikita's rule). This file documents what they do so we can beat it.

## Sources (numbered — tags used below)
- [N1] PDP https://naxir.co/products/standsecure — Firecrawl scrape 2026-11-25 (cache 2026-11-25) — VERBATIM
- [N2] Sales page https://naxir.co/pages/standsecure-sales-page — Firecrawl 2026-11-25 (cache 2026-11-23) — VERBATIM
- [N3] Advertorial A "Disruptor" https://offer.naxir.co/ss-disruptor-to-pdp (CTA → PDP) — Firecrawl 2026-11-25 — VERBATIM. Raw: data/raw_P1B/adv_ss-disruptor-to-pdp.md
- [N4] Advertorial A' https://offer.naxir.co/ss-disruptor-adv-1 (same text, CTA → funnelish "#next-step" order step; price line "$69 (thanks to a 50% promo ending soon)") — VERBATIM. Raw: data/raw_P1B/adv_ss-disruptor-adv-1.md
- [N5] Advertorial B "FAQ / About" https://offer.naxir.co/about-standsecure-cane (masthead "Healthy Living") — Firecrawl 2026-11-25 — VERBATIM
- [N6] Trustpilot https://www.trustpilot.com/review/naxir.co (4.5★, 451 reviews, claimed May 2024, contact country United Kingdom) — VERBATIM
- [N7] Trustpilot 1–3★ filter https://www.trustpilot.com/review/naxir.co?stars=1&stars=2&stars=3 — VERBATIM (directQuote extraction)
- [N8] Gethookd brand/shop data (search_brands, get_shop 35569, get_shop_traffic, search_ads, get_ad transcripts) — DATA. Log: data/gethookd_log.md; transcripts: data/raw_P1B/transcripts.md
- [N9] Meta Ad Library API (mcp facebook ads_library_search, page_ids 107352052289186 Naxir + 777560318771009 "Healthy Living", ACTIVE) 2026-11-25 — DATA
- [N10] Meta Ad Library page views scraped via Firecrawl: Healthy Living page https://www.facebook.com/ads/library/?id=2149258669312002 (~59 results header) and Naxir page https://www.facebook.com/ads/library/?id=1847535443340013 (~100 results header) — VERBATIM ad copy. Raw: data/raw_P1B/meta_snapshot_*.md

## 1 · Shop signals
| Signal | Value | Tag |
|---|---|---|
| Ad pages | 2: "Naxir" (FB page 107352052289186, Gethookd id 32152, 197 active ads at 2026-11-24 spy) + "Healthy Living" (FB 777560318771009, Gethookd id 156710, 109 active) — both land on naxir.co / offer.naxir.co. 3rd record "Naxir Healthy Living" 0 active. | [N8] DATA |
| Active ads now (Meta API, both pages, ACTIVE) | GB 164 · US 162 · CA 77 · AU 76 · NZ 69 (estimated_total_count) | [N9] DATA |
| Gethookd live ads (shop) | 306 (109 to own domain; rest via 2 official pages); active-ads growth −19.9% vs 2026-09-30 | [N8] DATA |
| Monthly visits | Dec-25 6,809 · Jan-26 1,768 · Mar 5,803 · Apr 5,239 · May 5,069 · Jun 12,428 · Jul 31,439 · Aug 37,622 · **Sep 59,273 (peak)** · Oct 33,948 (−42.7% m/m) | [N8] DATA |
| Visitor countries | US 74.3% · CA 16.7% · IL 6.1% · TR 5.6% · GB 5.2% · AU 4.1% · BR 2.5% (avg share) | [N8] DATA |
| Time in business | Trustpilot profile claimed May 2024 [N6]; StandSecure advertorial images uploaded to Funnelish with Unix-time names 1715712084–1716394454 = 14–22 May 2024 [N4 image URLs] → StandSecure funnel existed since ~May 2024 (INFERENCE from file timestamps). Earlier product FootRevive (neuropathy) ran 2025-06-14→2026-02-05 [N8]. Current StandSecure ad wave first seen 2026-04-15 [N8]. | mixed |
| Longest-running StandSecure ads | 154 days (2026-04-15→2026-09-15, now inactive): retarget statics "Forgot to checkout? 50% OFF Sale Ends Today!" (ad 92326495, 6 variants; 92326497) + video "Your cane helps you walk. But can it help you stand up?" (92326499, 6 variants) → LP ss-disruptor-adv-1; 114 days: same video → about-standsecure-cane | [N8] DATA |
| Longest-running ACTIVE | 80 days (since 2026-09-07): "We owe you an apology" (Winning), "Built To Travel", "Overstock", "Still thinking…", "Get The Real StandSecure" (fakes) | [N8] DATA |
| Most-duplicated (variant_count in Gethookd) | FootRevive neuropathy video 17 (old product); StandSecure: "3 Walking Canes Ranked" 8, "Founder note/overproduced batch" 8, "Your cane helps you walk…" 6, retarget static 6, "Here's how to get out of any low chair…" 5 | [N8] DATA |
| Ad survival | 3-day 100% (1583/1583); 30-day 18.2% (212/1168) → heavy testing, ~1 in 5 ads kept past a month | [N8] DATA |
| Stack | Shopify (theme Refresh 15.4.0), GemPages (sales page), Funnelish (offer.naxir.co advertorials + order step), Kaching Bundle Quantity Breaks, UpCart cart-drawer upsell, Vitals (reviews/bundles), Klaviyo email+SMS, Trackify pixel, Shop Pay, Truemed HSA/FSA widget | [N8][N1] |
| Business base | Trustpilot lists United Kingdom; returns go to UK (reviews) | [N6][N7] |

## 2 · Funnel (where the click goes + the one job each page does)
1. **Advertorial A "This Startup Is Disrupting The Entire Multi-Billion Dollar Mobility Aid Industry"** (offer.naxir.co/ss-disruptor-to-pdp & /ss-disruptor-adv-1) — fake news/"Mobility Insider" style review by "RICHARD HARPER", dated today. Job: pre-sell the *category disruption + "secret" second handle* to a cold, problem-aware reader, then push to PDP. Most active ads point here. [N3][N4][N8]
2. **Advertorial B "Stand Up From Any Chair Or Couch Without Asking For A Hand"** (offer.naxir.co/about-standsecure-cane; "Healthy Living" masthead) — Q&A/FAQ advertorial that answers objections one by one (weight, height, ease, vs other canes, price, fakes, guarantee). Job: objection-handling for solution-aware readers. [N5]
3. **Sales page** (naxir.co/pages/standsecure-sales-page, GemPages) — long-form VSL-less sales letter with buy box. Headline = customer quote. Job: emotional pain → mechanism → offer in one scroll. Used by "Winning" ads 181333445 & 183218743. [N2][N8]
4. **PDP** (naxir.co/products/standsecure) — Kaching bundle buy box. Job: close. Retargeting statics "Forgot to checkout?" land here or on advertorial. [N1][N8]

## 3 · FULL advertorial structure
### Advertorial A — "Disruptor" (news-review format) [N3][N4] VERBATIM excerpts
| Block | What it does | Verbatim |
|---|---|---|
| Kicker | Social proof/urgency | "TRENDING INTERNET OFFER" |
| Headline | Category-disruption + curiosity quote | "This Startup Is Disrupting The Entire Multi-Billion Dollar Mobility Aid Industry "I've Never Seen A Cane Like This Before"" |
| Byline | Fake editorial authority, dated today | "by RICHARD HARPER • November 23rd, 2026" |
| Sub-head | Bandwagon | "See why this cane is gaining popularity quickly worldwide and selling out everywhere..." |
| Lead (common enemy) | Industry villain | "For a long time, the mobility aid industry had been providing outdated and ineffective products to those suffering with poor mobility. But now, one healthcare startup is turning the $11 billion mobility aid industry on its head." |
| What is it | 4-in-1 positioning + expert | "StandSecure cane combines the benefits of a standing aid, LED flashlight, emergency alarm system, and a cane all into one." · "Their engineers combined forces with some of the top orthopedists in the world" |
| Mechanism ("secret") | Second handle | "The innovative second support handle is the secret. It was designed and expertly placed by orthopedists to allow you to stand up from couches, chairs, and beds all on your own, without having to rely on others! It can even help you sit down too!" |
| Emotional core | Burden | "Many people start to feel like a burden to their loved ones when they have to keep asking for help every time they want to stand up." |
| Proof claim | Unverified superlative | "the best selling mobility aid of 2025. No other cane is this advanced!" |
| Feature stack 1 | Night + alarm | "midnight trip to the bathroom… bright LED flashlight" · "With just the press of a button a loud alarm sound plays out" · humour: "Or you can even use it to tell your partner you want your morning coffee!" |
| Feature stack 2 (✅ list) | Self-standing · adjustable height · ergonomic grip · collapsible | "no longer have to keep bending down to pick up fallen canes!" |
| Testimonials (3, first name + initial) | Burden → independence | "I started to feel like a burden to those around me as I always needed their help." — Joan H. |
| Price anchor | $200 / "$500" | "it wouldn't be surprising to see a price tag of up to $200… (some cost over $500)… selling this cane for just $64 in their Black Friday Sale" (A') "just $69 (thanks to a 50% promo ending soon)" |
| "How can they charge so little?" | DTC logic | "they spend no money on advertising" (sic) |
| "Why discounted?" | Review-seeding excuse | "They give a certain amount of customers a big discount, to try and get a lot of positive reviews" |
| Buy now or wait | Urgency + **gift line** + first-cane line | "It also makes an amazing present from family, friends, or coworkers" · "If you have never owned a mobility aid - the StandSecure is the perfect first time cane." |
| How to get a real one | Anti-fake + date-stamped 50% | "one-time, first‑time‑buyer 50% discount" |
| CTA (×6+) | "Apply 50% Discount & Check Availability" | — |
| Fake FB comments block (~20) | Objection handling via "comments": shipping ~1 week, "Can anybody vouch for this?", son buying for dad, "Hey Lois, this is what you need for your mom", stroke recovery, "bought for full price and now 50% off? That's not fair!" | e.g. "As a son whose dad has been using the StandSecure cane…" |

### Advertorial B — "About StandSecure" (FAQ format, "Healthy Living") [N5]
Headline: "Stand Up From Any Chair Or Couch Without Asking For A Hand" · authority line "Designed by Orthopedists and Trusted by Top Mobility Experts Nationwide".
Q-sequence (order = their objection ranking): What is it? → How does the Standing Support Handle help? ("You grip it, push down, and your legs do the rest. No rocking. No pulling on furniture.") → Will it support my weight? ("rated to support up to 250 pounds… It doesn't slide, it doesn't tip") → Will it fit my height? ("88cm to 98cm… 5'2" and 6'2"") → Easy to use? → What else (night 2am light + alarm) → How is it different from other canes ("A standard cane wobbles… A quad cane is more stable, but it's bulky… You get the stability of a quad cane, with the smooth walking of a single-tip cane.") → Cost ($139.99 retail; "$59.99 each when you order the 2-pack"; single $69.99; "Most people get one for the house and one to keep in the car, by the bedroom, or at a relative's house") → Where to buy ("Cheaper knockoffs… place the second handle at the wrong height") → Guarantee ("Use it on your own couch. Take it to your daughter's house.") → 4-step how-to-order → 3 testimonials (one post-op: "I had two knee replacements and my regular cane just couldn't help me get off the couch." — Mary P) → date-stamped "SAVE 50% OFF UNTIL November 25th, 2026". Note: testimonial image file names "RejuvaSeat Product Photos", "RejuvaRelief Product Photos" = recycled from Naxir's other products (INFERENCE from URLs).

### Sales page [N2]
Headline (customer-quote): **"I Used To Ask My Husband To Pull Me Up 4 Or 5 Times A Day. Now I Just Stand Up."** → sub: "StandSecure is a cane with a second handle, added by an orthopedist. You grip it, push down, and stand up on your own. No rocking. No grabbing the armrest. No waiting for anyone to pull you up." → Pain story "Some Days You Can't Get Out Of The Chair At All… That's the part that wears you down. Not the effort — the asking." → future-pace decline "Every month you spend waiting for a hand, your legs get a little weaker." → mechanism blocks (stand-up handle; 250 lb no slide/tip; folds; self-standing "A cane on the floor is a cane you can't reach") → **cost-of-asking math** "1,600 Times A Year, Somebody Has To Stop What They're Doing" → 3 free gifts → buy box → risk reversal "You're not deciding today. You're deciding in two months, after you've used it in your own chairs." → colour identity "It should feel like something you picked, not something that was prescribed." → FAQ → reviews → medical disclaimer.

## 4 · Offer (PDP) [N1][N2]
- Price: **$64.99** (compare-at $139.99, "Save $75"); Buy 2 **$54.99 each** ("Most Popular", "One for home, one for on the go", + FREE shipping); Buy 3 **$46.99 each** ("Best Value", "Share with a spouse or family"). Black Friday banner: "Up to 65% Off… Lowest price of the year"; BF ad: "The sale ends November 30" [N10].
- Gifts: FREE Cane Carry Bag ($19.99 value) per cane + 2 e-books "Balance Building Handbook" + "Preventing Falls At Home & Beyond" ($39.98) → "Over $50 In Free Bonuses". "User guide + gift-ready packaging".
- Guarantee: "60-day money-back guarantee… full refund, no questions asked."
- Shipping: "Tracked shipping… Average delivery time is 9-12 business days." Free shipping threshold: cart says "You're $70.00 away from free shipping!" (single cane does NOT get free shipping on PDP; advertorial B says free shipping on every order — inconsistent).
- Variants: Black/Blue/Purple; Short (75–87 cm, under 5'9") / Standard (85–97 cm). Specs: under 1 lb (0.45 kg), 250 lb (113 kg), 2×AAA **not included**, 5 height settings.
- Payment: HSA/FSA via Truemed ("Save an average of 30%"). Upsells: UpCart cart drawer (apps [N8]); no visible post-purchase upsell captured (checkout not walked — no orders placed).
- Social-proof numbers are inconsistent across assets: "17,500" / "20,000+" / "15,000" / "30,000+ Customers" / "Rated 4.8/5" with 613 on-page reviews (526×5, 55×4, 18×3, 8×2, 6×1).

## 5 · Reviews
- On-site (Vitals) 4.8 / 613 reviews [N1]. Reviewer names follow a Faker-library pattern ("Maurice Huels", "Nyasia O'Conner", "Otho Schaden", "Gennaro Schimmel", "Jaleel Brakus") and several review texts are word-identical to the advertorial "comments" (e.g. "Superb walking stick, me and my wife both got one…", "Most of the other canes I tried were quite heavy…") → on-site reviews likely seeded (INFERENCE; do not quote as real customer voice).
- Trustpilot 4.5 / 451 reviews; "No recent history of asking for reviews"; "Hasn't replied to negative reviews" [N6]. AI summary: "Some reviewers were not happy with the overall quality, noting that certain items arrived damaged or experienced frustrating issues with non-working lights and alarms." [N6]
- Real complaints (1–3★) [N7] VERBATIM:
  - Too short / height: "The cane doesn't go low enough for my 5'4" height. The foldable extra handle isn't long enough to really help me get up from a chair, the cane is too expensive." (Aug 31 2026) · "The cane/product will NOT lower to work for anyone 5 feet or shorter." (Aug 10 2026) · "This cane was way too short… I am 5'5"" (Oct 15 2026) · daughter: "The height is adjustable, but still too tall for her." (Oct 5 2026)
  - Returns to UK / partial refunds: "If you want to return the item, CUSTOMER has to pay return shipping to UK." · "my only recourse is to accept their 25% returned to my card" (Sep 10 2026) · "they stated they would refund 25% and we could keep product" (Jul 28 2026)
  - Light/alarm fail: "The light and alarm did not work, despite changing the batteries three rimes." (Aug 25 2026) · "Neither the light or alarm work. No instructions…" (Oct 5 2026)
  - Flimsy / not stable: "I'd call it, rickety… It snapped and creaked… the rubber foot fell off." (Aug 19 2026) · "bends on full weight to get up i didnt feel secure with it" (Jul 28 2026) · "It wants to keep falling over. The foot seems to be too small. On carpet it needs to be leaned against something" (Sep 28 2026) · "It rattles in use mainly at base." · "Cushion is too thin"
  - Doesn't stand-assist for some: "As soon as I received the cane… I realised that it would never achieve this." (Oct 2026)
  - Shipping delays: "landed in Toronto on September 1, 2026, it hasn't moved since" · "Purchased a walking stick for my father on 13th September… still not received it."
  - Positive real buyer groups seen: wife/husband ("The cane helps my wife get up and walk. The alarm is very helpful"), disabled veteran, "Have one for both cars." [N6]

## 6 · Ad angles — every repeated angle (from 40+ distinct creatives read in [N8][N9][N10])
| # | Angle / hook family | Example first line (VERBATIM) | Leads with | Status / evidence |
|---|---|---|---|---|
| A1 | **"Cane that helps you STAND, not just walk"** (core mechanism) | "Your cane helps you walk. But can it help you stand up?" | mechanism | longest-run 154 d (92326499) + still active variants — their #1 proven angle |
| A2 | **Sit-to-stand demo / how-to** ("rocking, armrest, waiting for a hand") | "Here's how to get out of any low chair or deep couch without rocking, grabbing the armrest, or waiting on anyone to pull you up." | mechanism + demo | Winning (179218237, 181333445); transcript: husband pulls her up "Four or five times a day"; "It got worse after my knee surgery" |
| A3 | **Retarget static "Forgot to checkout? 50% OFF Sale Ends Today!" + Julia T. burden quote** | "I used to really feel like a burden because of my mobility issues…" | offer + identity | 154 d (2026-04-15→09-15) + Winning active 183218743 |
| A4 | **"Cheap fakes are everywhere" / Spot the fake** | "Seeing this cane everywhere? Watch out for cheap fakes." · "Seen StandSecure for cheap on Amazon or some random website? That's not us." | trust/fear | Winning (192380650, 56 d); started 2026-09-07 & 10-17 |
| A5 | **Overstock / we made a mistake / over-ordered** | "We over-ordered — and it's good news for you." · "We made a mistake in our warehouse…" | offer excuse | 80 d active + new 2026-11-23 |
| A6 | **"We owe you an apology" (biggest sale ever)** | "If you own a Stand Secure, we owe you an apology." | offer | Winning, 80 d |
| A7 | **Founder story ("for my mom")** | "I originally helped develop StandSecure for my mom." / "A quick note from the founder of StandSecure" | identity/story | new Nov 14 & 23 (8 variants) |
| A8 | **Travel** | "This is the cane that's actually built to travel with you." | use-case | 80 d active |
| A9 | **New colours / not-prescribed look** | "The StandSecure cane is now available in Blue and Purple!" | identity | 108 d + 71 d |
| A10 | **Listicle "3 Walking Canes Ranked From Worst To Best"** (base + handle) | "Unsteady on your feet, or struggling to get up from chairs? Not all walking canes help with both." | comparison/mechanism | Nov 6+ (8 variants), GB/US/AU/CA/NZ |
| A11 | **Balance: furniture-walking / shuffling / tiny steps** (NEW, walking not standing) | "Do You Hold Onto Furniture to Walk Across the Living Room?… There is even a name for it: furniture walking." · "Taking Shuffling Steps to Protect Your Balance?" · "Notice Yourself Taking Tiny Steps Lately?" | problem (walking/balance) | Nov 18–22, testing |
| A12 | **Age-risk education "Why Getting Out of a Chair Gets So Risky After 75"** | "If you find yourself rocking back and forth just to stand up from your chair, please do not brush it off." | bigger claim / education | Nov 23, testing |
| A13 | **Hate asking for a hand / deep chairs** | titles "Hate Asking for a Hand Just to Stand Up?" · "Struggling to Get Out of Deep Chairs on Your Own?" | pain/identity | Nov 24, testing |
| A14 | **New facility / demand** | "We never expected this many seniors to switch to StandSecure." | social proof | Nov 19 |
| A15 | **Black Friday up to 65%** | "Our Black Friday Sale is live: up to 65% off StandSecure." | offer | since Nov 2 (AU/CA/NZ too) |
| A16 | **Cost of waiting / next fall** (inside A2 scripts) | "Don't let the next fall be the thing that makes this decision for you." | fear | inside Winning video |

Repeated proof devices: "orthopedist-designed" (every ad), customer counts 17,500→20,000→30,000, 250 lb, 60-day guarantee, free carry bag. Format mix: UGC-style "street demo" with real-looking seniors (Gethookd: "Customer", "semi_polished", no AI evidence), founder-voice text, statics with stars. Avatar: the senior USER herself (65–85, often a woman whose husband pulls her up), secondary = spouse; adult-child appears only in fake comments + "ship to a loved one" line.

## 7 · What Naxir misses / does weakly (our openings) — evidence-based
1. **Post-op knee/hip avatar is a footnote, not a market** — mentioned only inside scripts/testimonials ("It got worse after my knee surgery", "I had two knee replacements", PDP review "After my knee op"); no ad, page or offer built for the 6-week post-op window. [N1][N5][N8] (Verified across all 40+ ad bodies read: none leads with surgery.)
2. **Adult-child / gift buyer not targeted in ads** — only one advertorial line ("amazing present from family") + fake comments; no ad addresses the son/daughter, no gift box/card, no "ship to Mum" flow beyond one PDP line. Christmas angle absent (they run Black Friday only). [N3][N1][N10]
3. **Short users (<5'2"–5'4") excluded** — repeated 1–3★ complaints; their Short size starts 75 cm. Opening: a size that genuinely fits petite women + honest size guide. [N7]
4. **Returns to the UK / 25% partial refunds** destroy the 60-day guarantee in US/CA/AU — opening: local returns (AU address) and "full refund, return to an Australian address". (Record only — trust lines are not our lever per Nikita; use as offer mechanics, not headline.) [N7]
5. **Slow delivery 9–12 business days**, CA parcels stuck in Toronto → local stock / faster shipping is a real offer edge in AU. [N1][N7]
6. **Batteries not included** + light/alarm failures → include batteries + spare tip. [N1][N7]
7. **No local-market version**: everything is US $, lb, US English ("couch", "pounds"), even in AU/GB/NZ ads (same creative served globally; GB ads billed in GBP but copy says "250 pounds"/"$"). AU/NZ get the same global ads (76 / 69 active). No metric, no AU words (lounge, loo, Mum), no NDIS/My Aged Care angle. [N9][N10]
8. **Night/2am bathroom (alone_night)** is a feature line, never a lead angle; no "lives alone" ad. [N3][N5][N10]
9. **Proof is thin/inconsistent**: four different customer counts, seeded-looking on-site reviews, no real OT/physio, "orthopedist" never named. A named-expert or real-customer-video approach would out-trust them (record, not our headline lever). [N1][N2][N3]
10. **Formats**: all "semi-polished" demo/talking + text statics; no animation/explainer of *why* sit-to-stand fails (sit-to-stand biomechanics), no carer/OT POV, no side-by-side "regular cane tips over vs this" test. [N8]
11. **Balance angle is new for them (Nov 18–23, testing)** — they are drifting from the stand-up mechanism toward walking/balance; stand-up remains their owned core.

## So What → do this
Naxir OWNS "the cane that helps you stand up" for the senior user in the US (and serves the same global ads in GB/CA/AU/NZ). Don't fight A1/A2 head-on with the same avatar in the US. Attack where they are absent: (a) post-op knee/hip first-6-weeks market, (b) adult-child Christmas gift buyer, (c) local AU version (metric, AU words, AU returns, fast local shipping, batteries included, petite size). Copy their proven structure (customer-quote headline → "the asking" pain → push-down mechanism → self-standing → risk-free in your own chairs) but never their name, photos or claims we can't prove.

# 15 · Competitor Offers + Price Ladder — FINAL (locked market)

*Doc 4 — Brand, Offer & Funnel. Writer B, 2026-10-06. Replaces work/D4-s15.md for decisions (kept for the record). Locked market: "Big kids still learning" — US parents of 5–9-year-olds with DAYTIME accidents (work/LOCK-decision.md). Mechanism: the* **Big-Kid Hold** *(work/D3-s13.md).*

**What changed vs work/D4-s15.md (said plainly):**
1. **Added every big-kid / older-child competitor** named in work/D1-s1-LOCKED.md: BrightKidCo Autism & Sensory Edition, Kid Confident Big Kid Sizes, Super Undies, Peejamas, MooMoo 2T-9Y / 9T, BIG ELEPHANT 9-10Y, Goodnites, "Dinosaur 8-10Years", Carer / TIICHOO / FUVVRVAL / EZ Moms, Lucky & Me, SmartKnitKIDS, WunderUndies, and the two indirect supplement brands that sell to the same parent (Saphire, Bloomwise). Section **E** below.
2. **"Home + Daycare Kit" is dead.** It is now the **"School-Day Kit"**: pairs + wet bag + discreet spare pouch for the backpack + a teacher note card. No daycare identity anywhere.
3. **Price point re-set** from "$79 for 10 ($7.90/pair)" to the locked **$11–14/pair** ladder: 1 pair $19 · 6 for $84 · **10-pair School-Day Kit $119 (pre-selected)** · 15 for $159. Pre-0 re-run at this price: work/D1-Pre0-rerun.md.
4. **Offer inputs for Step 2 are filled** from the locked §10 / §11 counts (601-row bank). No placeholders left.
5. Sections A–D (toddler-category competitors, captured earlier the same day) are **carried over unchanged** below section E, because the page asks for *every* competitor named earlier. Their numbers stand; their *conclusions* (daycare kit, $79 price) are superseded by this file.

## How this was captured
- **Price data:** Shopify `/products.json` for every big-kid Shopify store (brightkidco.com, kidconfident.co, superundies.com, trysaphire.com, hellobloomkids.com, luckyandme.com); raw files in `work/15-captures/B/*.products.json`. smartknitkids.com returned an empty body and moomoobaby.com a 16-byte non-JSON reply, so those two were priced on Amazon instead [B44][B26].
- **Cart walk:** one headless Playwright script (globally installed Playwright, through the session proxy; TLS left on) walked product page → add to cart → cart → checkout for 8 big-kid / same-parent stores and **stopped at the payment step**. No address, no personal data, no payment, no order. Files: `work/15-captures/B/[slug]-[1-pdp|2-after-atc|3-cart|4-checkout].txt/.png`; run log `work/15-captures/B/walk-log-B.json`.
  - Kid Confident Big Kid and Peejamas: the add-to-cart button timed out, so a retry added one variant through Shopify's public `/cart/add` link, then walked cart → checkout.
  - Goodnites: goodnites.com answered **403** to the headless browser (this run, `work/15-captures/B/goodnites-1-pdp.txt`) and is not a Shopify store; it sells through retailers. **Cart not walked — 403 + no own cart.** Priced from retailer listings [B45].
  - Marketplace-only brands (MooMoo, BIG ELEPHANT, "Dinosaur 8-10Years", Carer, TIICHOO, FUVVRVAL, EZ Moms, SmartKnitKIDS): **cart not walked — they have no DTC offer stack; the "offer" is the Amazon / Walmart listing price + platform returns.** Priced from listing scrapes.
- **Policies:** `work/15-captures/B/pol-[domain].html` (Lucky & Me, Saphire, Bloomwise, WunderUndies); BrightKidCo / Kid Confident / Super Undies / Peejamas policies from the same-day wave-1 capture [O10][O6][O35][O37].
- **Post-purchase upsells** only show after payment, so they are **INFERENCE** from Winning Hunter `get_store_details` installed apps [B35][B37][B39][B41][B43][O8][O11].
- **Pop-ups:** the script dismisses overlays; a pop-up offer is recorded only where its text was on the page.

---

## E. Big-kid / older-child competitors (the locked market) — captured 2026-10-06

### E1 · Direct: big-kid absorbent underwear sold DTC

**BrightKidCo — Autism & Sensory Edition** (0 live ads; underwear ad last seen 2026-08-31 [U24]) [B18][B47][O10][O11]
- **One-time:** 1 pair **$29.99**, no compare-at [B47].
- **Bundles/tiers:** Standard Pack 4 pairs **$59.99** ($15.00/pr) · Potty Progress Pack 8 pairs "Buy 5, get 3 free!" **$89.99** (compare-at $159.99, $11.25/pr) · **Complete Training Bundle 12 pairs "Buy 6, get 6 free!" $119.99** (compare-at $219.99, **$10.00/pr**). The 12-pack is the default: add to cart put "BKC 12-PACK (-$239.89)" $119.99 in the cart [B18 cart]. No subscription.
- **Sizes:** S / M / L only [B47]; max L ≈ 4–6+ (lock). PDP: "Built for Autistic Kids · Levels 1–3" [B18].
- **Free gifts:** "FREE E-Book — Potty Training Guide $24.99" + "FREE Shipping $4.95" [B18].
- **Upsells:** cart cross-sells the 2-in-1 Toilet Stairs $69.99 and TPU Mattress Protector $39.99 [B18 cart]; catalogue: waterproof bag 3× $39.99, mesh bags $34.99, Clean-Up Kit $29.99 (compare-at $49.99), blanket $59.99, Anywhere Toilet Seat $49.99, Happy Poop™ Gummies $29.99–39.99 [B47]. Post-purchase app: none detected (INFERENCE [O11]). No protection fee at checkout.
- **Guarantee + returns:** headline "100-Day Money-Back Guarantee", but the body text reads "100-Day Calm Progress Guarantee… If you don't feel it has been the right fit for your family, simply contact our support team within 100 days of delivery, and **we'll help make it right**" [B18] — no refund is spelled out. The store policy: underwear "cannot be returned or refunded once worn, tried on, washed, or used in any manner" [O10]. "Free Size Exchange ✓" on the PDP vs Trustpilot "No exchange for wrong size" [O11].
- **Shipping:** "Free Shipping on orders $70+"; cart "Free shipping in 2-4 days" [B18].
- **Discount mechanics:** "Our offer ends in 04h 10m 53s" countdown; "**526 sold in the last 2 hours**"; "#1 Potty Training Underwear in the US" [B18]. Pop-up not captured.
- **Weak / missing:** toddler sizes only (S–L) on an "autism" page aimed at older kids; a speed claim in the product title ("Potty Trained in 4–6 Weeks"); a guarantee that promises nothing concrete and a policy that refuses worn underwear; fake-looking urgency; **no capacity number**.

**Kid Confident — Potty Training Underwear (Big Kid Sizes)** (big-kid ad paused 2026-09-12 [M30]) [B20][B46][O6][O8]
- **One-time:** 1 pair **$19.99 + $5.99 shipping**; 2 pairs $39.98 + $5.99 shipping [B20].
- **Bundles:** **"Buy 3, Get 4 Free" 7 pairs $59.97** (compare-at $139.93, "Save $79.96") = **$8.57/pr**; "Prefer to build your own pack?" option [B20]. Sizes SM / MD / LG; 2 colours only (Dark Blue, Light Green) [B46]. The size chart's ages / waists are **not stated in page text** (Firecrawl query returned nothing; chart is an image) [B46]. "Shop Toddler Sizes 2T–7T →" sits under it [B20].
- **Free gifts:** "Free Gifts Today Only — $51 VALUE": Express Shipping $5.99, Playbook $29.99, Reward Chart $14.99 [B20][B46].
- **Upsells:** Leakproof Undie Covers for Bedtime 4-pack $23.99 (compare-at $47.98, sizes to 7T) [B46]. ReConvert + Zipify OCU signatures; Intelligems price testing (INFERENCE [O8][O74]).
- **Guarantee:** "Backed By Our 60-Day Money Back Guarantee"; "Less than 1% of customers claim"; cart: "Results or Refund, 60 Day Money-back Guarantee" [B20]. **The refund-policy page 404s** [O6].
- **Shipping:** paid ($5.99) below the 7-pair tier; express free in the 7-pack [B20].
- **Discounts:** "BUY 3, GET 4 FREE | ENDING SOON"; "**89% already reserved. Miss this batch and the next one ships November 15th.**" [B20].
- **Walk:** add-to-cart timed out; retry via `/cart/add` → cart $19.99 (1 × SM) → checkout reached, stopped [B20 cart/checkout].
- **Weak / missing:** the big-kid page reuses toddler proof ("pretty much toilet trained at 18 months") and speed copy ("Noticeable progress within days", "Makes It Click In Just Days"); 2 colours; no stated ages or capacity ("8-Layer Protection helps contain leaks"); paid shipping on small orders; no written refund policy.

**Super Undies** ("the big kid diaper experts"; 0 ads since 2025 [U25]) [B34][B35][O34][O35]
- **One-time:** 3-in-1 Diaper / Trainer / Swim "for Kids with Disabilities" **$34.99** (pull-on or snaps, S–XL; "toddler through 50" waist") · Brain Training Bedwetting Underwear $44.99 · Fearless Trainers (toddler S–L) $24.95 [B34 products.json].
- **Bundles:** "(5 Pack) 3-in-1 Diapers for Big Kids & 3 Liners" **$219.60** (no compare-at) = **$43.92 per pair incl. liners** — *more* than 5 singles ($174.95) + 3 liners bought apart (INFERENCE arithmetic from [B34]). Brain Training 3-pack $134.99 (compare-at $164.85); "10 Pairs of Undies, Plus More — Save $120!" $194.50–279 (toddler sizes) [B34].
- **Free gifts:** cart / checkout line "**($99) Free Laundry Bag ($149) Free Shipping!**" (−$9.95 laundry bag applied) [B34 cart/checkout].
- **Upsells:** absorbency boosters 5-pack $49.75–74.75, Super Soaker Bomb $9.95, Step-up Insert $9.95, Bedwetting Breakthrough Course $29.95, ebook $9.99 [B34]. Theme "Canopy w/navidium" and a "Shipping Protection" product among its best-sellers → Navidium protection is installed; **not seen pre-ticked** at our checkout (INFERENCE [B35]). WH lists no post-purchase app [B35].
- **Guarantee + returns:** "Easy Returns" banner; policy = within 14 days, unused; store credit +$5 or a $9 label deduction on refunds [O35].
- **Shipping:** "Easy $3.95 Domestic Shipping, Everyday!"; 5-pack "Orders typically ship within 2 weeks" [B34].
- **Capacity:** states absorbency in ml on its special-needs line (150–300 ml, B-map via [O34]); 5-pack page says "2 layers of built-in microfiber absorbency" + "Internal pocket to add more absorbency" [B34].
- **Discounts:** "Get 10% Off" marquee (pop-up / sign-up) [B34].
- **Weak / missing:** sold as a **diaper** ("3-in-1 Diapers for Big Kids") with a condition list (autism, spina bifida, neurogenic bladder…) → clinical, "Health - Other" [W2]; bundle priced *above* singles; 14-day unused-only returns; 2-week ship time; 13,098 visits, AOV **$90.81** [B35].

**Peejamas** (night-first brand with a daytime line) [B25][O36][O37]
- **One-time:** Overnight Booster Insert 3-pack $19.99 (2T–4T shown) — "Each insert absorbs up to 4 ounces of urine"; Nighttime Jammies "hold ~10 oz" [B25].
- **Bundles:** Daytime Underwear 6-Pack Bundle **$29.99** (~$5/pr); Absorbent Mattress Protector "40 oz!" $29.99 [B25].
- **Upsells:** cart cross-sells (protector, daytime 6-pack) and a $4.99 item [B25]; "25% OFF IVORY BOTTOMS - USE CODE PJIVORY25" bar.
- **Guarantee:** unused within 30 days of shipping; restocking fees possible [O37].
- **Shipping:** "Free Shipping on US orders above $75" ("$75.00 away") [B25].
- **Walk:** ATC timed out → retry via `/cart/add` → checkout displayed "Your order is free. No payment is required" at $0.00 for a $19.99 item [B25 checkout] — a store-side pricing glitch or auto-discount (INFERENCE; not exploited, stopped there). Earlier the daytime 6-pack redirected to `/stock-problems` [O36].
- **Weak / missing:** daytime line is toddler-sized and out of stock; the brand's numbers (oz) are on **night** products only.

### E2 · Direct: big sizes on marketplaces (no DTC stack — cart not walked, see method)

**MooMoo Baby 2T-9Y / 9T** [B26][U10]
- **Price:** 2T-9Y 10-pack **$35.99 = $3.60/count** (4T variant, "Lowest price in 30 days") [B26]; 9T 10-pack $29.74 = **$2.97/pr** [U10].
- **Offer:** Prime shipping (free over $35), "FREE 30-day refund/replacement" [B26]. No bundles, gifts or guarantee beyond Amazon.
- **Claims:** "OEKO-TEX, Absorbent Layers, Wetness Awareness"; "Designed to contain small accidents", **no ml** [B26].
- **Weak:** leakage 116 of 180 mentions negative on 9T [U10]; title says "for Toddler Potty Training" even at 9Y [B26].

**BIG ELEPHANT 9-10Y** [B28][U29]
- **Price:** Walmart "BIG ELEPHANT **Toddler** Potty Training Pants… 10-Pack, 9-10Y" **$25.49, was $33.99** ($2.55/pr); 7–8 years $24.93 [B28]. TikTok Shop 10-pack: 722 units / $24.1K in 30 days ≈ $33.38/pack ≈ $3.34/pr (DATA ÷ arithmetic) [U29].
- **Offer:** a struck-through "was" price; platform returns only.
- **Claims:** "thickened cotton absorbent layer that effectively locks in urine leaks" [B28] vs its TikTok title "NOT Diapers… Limited Absorbency… Daytime Use Only" [U29].
- **Weak:** "Toddler" in the title of a 9–10-year-old size; contradictory absorbency claims; no number.

**"Dinosaur 8-10Years" trainer** [U11] — Amazon $18.99, 330 ratings, **16% 1★**; leakage 30 of 43 mentions negative. No offer beyond Amazon.

**Carer · TIICHOO · FUVVRVAL · EZ Moms** (absorbent big-kid "incontinence" boxers / trainers, ages 4–18) [U8][U9]
- **Price:** Carer boys size 10 4-pack **$39.99 ($10.00/pr)**; Carer 3-pack $41.24 (**$13.75/pr**); TIICHOO 5-pack $31.99 ($6.40/pr, 100+ bought/mo); FUVVRVAL $29.99 (100+/mo); EZ Moms 5T-6T 100+/mo [U8][U9].
- **Offer:** Amazon price + returns; no bundles / gifts / guarantee.
- **Weak:** "incontinence" naming (clinical); no brand, no stated capacity in the captured listings (INFERENCE from listing text).

**Goodnites** (Kimberly-Clark, disposable **night** pants; Autism Society partner) [B45][U27]
- **Price:** Walmart XL 28 ct **$31.97 = $1.14/pant**; Target "Bestseller $32.49 – $68.99"; Sam's Club XL 46 ct $53.98 [B45] (SNIPPET).
- **Offer:** retailer promos only. Its 2023 Meta ad stated "holds the equivalent of 2 water bottles… 16 oz. in total" [U27].
- **Weak (for our market):** night-only disposable; a recurring cost; S–XXL by weight with "L, XL, and XXL do not feature character design" [B45]. Not a daytime school solution. **Cart not walked — goodnites.com 403 + retailer-only.**

### E3 · Sensory underwear (non-absorbent) — same ND parent, adjacent need

**Lucky & Me** (organic / sensory-friendly kids' underwear; 35,294 visits Aug 2026, 30d est. $184K–$295K) [B40][B41]
- **One-time / packs:** Lucas Boys GOTS Organic Cotton Briefs 6-pack **$38** ($6.33/pr); boys' and girls' packs $30–44; sizes **2/3y → 9/10y and tween 11/12y–13/14y** [B40 products.json].
- **Bundles:** pack = the unit; no tiers. Loyalty: "Claim Free 250pts — Comfy Cozy Club" (LoyaltyLion) [B40][B41].
- **Upsells:** cart cross-sells socks 5-packs $35–38; "Add $12.00 more to unlock FREE shipping" progress bar (slide cart) [B40 cart]. Post-purchase app: none in WH list; ReturnGO for returns (INFERENCE [B41]).
- **Guarantee + returns:** "**Our 30 Day Comfiness Guarantee** — If you're not in love with your purchase… we'll happily exchange your purchase or give you a full refund **with free return shipping within the US**." Policy: items must arrive within 45 days; "For hygiene reasons, we never resell returned items once they are opened" — i.e. opened pairs are accepted back [B40 policy]. **Best risk reversal in the big-kid set.**
- **Shipping:** "Free US Shipping On orders $50+" [B40].
- **Discounts:** none visible; no countdown.
- **Weak / missing:** **zero absorbency** — it solves the sensory complaint, not the accident.

**WunderUndies** (bamboo, flat-seam sensory underwear; 1,941 visits) [B42][B43]
- **One-time:** kids' briefs / boxers **$8–13 per pair**; "Find My Size Trial Packs" $25 [B42][B43].
- **Upsells:** cart shipping line $5.95 + "You are $37.00 away from FREE SHIPPING" (free over $50) [B42 cart]; OptiMonk pop-ups, Dr. Discount on Cart, Slide Cart, GoAffPro affiliates (INFERENCE [B43]).
- **Guarantee + returns:** "WunderUndies are **final sale and are non-returnable once opened**"; unopened 30 days, buyer pays shipping [B42 policy].
- **Discounts:** SMS opt-in; sizing trial pack as the risk reducer.
- **Weak / missing:** no absorbency; no returns once opened.

**SmartKnitKIDS Seamless Sensitivity Undies** [B44]
- **Price:** Amazon **$18.50 per pair**; sizes S 4-5 · M 6-8 · **L 10-12**; 3.3★ (96) [B44]. smartknitkids.com returned an empty products.json and **0 Meta ads** to its domain [U28].
- **Offer:** Amazon "Return this item for free" [B44].
- **Weak:** no absorbency; 3.3★.

### E4 · Indirect: supplement brands selling to the same parent (same pain, different product)

**Saphire** (kids' saffron gummies + a bedwetting advertorial + dry-nights e-book; 188,362 visits Aug 2026; 30d est. $870K–$1.6M; AOV $39.08) [B36][B37]
- **One-time:** 1 pack **$35** (compare-at $65); singles in products.json $49.95–54.95 [B36].
- **Bundles:** "Buy 2 Get 1 Free" **$69** ($25/pack, compare-at $165) + FREE "Chaos to Calm" ($15) · "Buy 3 Get 2 Free" $103 ($21/pack, compare-at $275) + "Meltdown Survival" ($25) [B36]. Site bar: "**Back to School** - Buy 2 Get 1 Free".
- **Subscription:** "Save 40% with automatic refills — Shipped every month. No Commitment, Cancel Anytime" [B36].
- **Upsells:** cart auto-adds a free item (CartBot "gift with purchase"); e-books $14.99–45.95 with $49–130 compare-ats ("From Wet Sheets to Sleepovers" $29.99 / $79); a $3.99 Shipping Protection product exists; AfterSell post-purchase, Kaching tiers, UpCart, Intelligems (INFERENCE [B37]).
- **Guarantee:** "60-Day Money-Back Guarantee… Less than 1% of buyers ever request a refund" — policy: product returned "**unopened and unused**", "Return shipping is paid by the customer" [B36 policy].
- **Shipping:** free over $70; "Ships By Tomorrow" [B36].
- **Discounts:** "SELLING FAST! Offer reserved for 02:54 minutes" timer [B36].
- **Weak:** Trustpilot 3.0 / 74 reviews — "Difficult subscription cancellation process" 7, "Unauthorized or unexpected subscription charges" 5, "Subscription charges despite no subscription opt-in" 2, "Use of fake profiles and AI-generated content" 1 [B37]; a guarantee that needs the gummies unopened.

**Bloomwise / Hello Bloom Kids** (kids' "meltables"; 139,388 visits Aug 2026; 30d est. $748K–$1.35M; AOV $58.12) [B38][B39]
- **One-time:** 30-day supply **$34.95** (compare-at $67) [B38].
- **Bundles:** "Buy 2, Get 1 Free" 90-day supply **$59.42** (compare-at $201) + FREE shipping + FREE "Calm Kids Protocol"; "Buy 3, Get 2 Free" 150-day $89.13 (compare-at $335) + Sleep Buddy [B38].
- **Subscription — hidden in the default:** after one add-to-cart click the cart read "One or more of the items in your cart is a deferred, subscription, or recurring purchase" and checkout showed "**$59.42 every 60 days**" (Recharge) [B38 cart/checkout][B39].
- **Upsells:** "Mystery Gift" $0 (compare-at $34.99); Sleep Buddy $27.99; sensory swing $129.99 [B38 products.json].
- **Guarantee:** "60-Day Money-Back Guarantee" — policy: "sealed, unopened, and unused"; "one approved Money-Back Guarantee claim is permitted per household" [B38 policy].
- **Shipping:** free over $50 [B38]. **Discounts:** "50% OFF + FREE Gifts!" with a days countdown [B38].
- **Weak:** ADHD-medication testimonials ("Off His Vyvanse") — health-claim risk; a subscription the shopper didn't pick; a guarantee that can't be used once tried.


---

## A–D · Toddler-category competitors (carried over unchanged from work/D4-s15.md, captured 2026-10-06)

*These blocks are the wave-1 capture of every §1 long-list store. Their prices and gaps stand. Where a store also sells a big-kid line (BrightKidCo, Kid Confident, Super Undies, Peejamas), its big-kid offer is in section E above. Superseded in these blocks: nothing in the facts; the daycare-kit and $79 conclusions now live only in the old file's Offer inputs, which are replaced below.*

### A. Direct DTC competitors (reusable training underwear)

**UpAiry** (market leader, US 95% of traffic) [O1][O2][O3][O4][O5]
- **One-time:** 1 pair $21, compare-at $29.99. The "Original" line is $17, compare-at $35.98 [O1][O5].
- **Bundles/tiers** (Kaching):
  - 1 pair $21.
  - **"BUY 2, GET 3 FREE" = 5 pairs $35 ($7.00/pair), badged "🔥 Most Popular".**
  - "BUY 4, GET 6 FREE" = 10 pairs $68 ($6.80/pair) [O1].
  - Separate kits: Daytime Kit $59–69 (compare-at $89–99), Nighttime Kit $59 (compare-at $106), Starter Kit $65 (compare-at $99), Tummies & Trainers Pack $53 [O1 products.json].
  - Subscription: a `potty-training-underwear-sub-offer` product exists, but the PDP shows no selling plan [O1 .js].
- **Free gifts:** they unlock with quantity.
  - 5+ pairs: "Ultimate Potty Printable Pack" ($20 claimed) and "The Secrets Of Potty Training" ($25).
  - 10+ pairs: free shipping ($5) and reward chart & stickers ($20) [O1].
- **Upsells:**
  - Checkout pre-adds **"Shipping Protection $5.99"**. A $21 cart becomes $26.99 at checkout [O1 checkout capture].
  - Cart drawer is UpCart.
  - Cross-sells: bed mat $29.99, bed-wetting alarm $39.99, inserts $32.99, banana potty $24.99, Tummy Gummies $32–49.99 [O5].
  - Trustpilot shows 19 complaints of a "Hidden subscription for free gift gummies" [O5].
  - Post-purchase app: none of ReConvert/Zipify/AfterSell detected (INFERENCE [O5][O74]).
- **Guarantee/returns:**
  - "75-day money back guarantee" and "75-day fit guarantee… exchange it for free".
  - A return label is provided, but "Original shipping charges are non-refundable", and the item must be "unworn or unused, with tags" [O1][O3].
- **Shipping:**
  - "Ships within 1 business day"; US 4–7 business days.
  - Free shipping only at 10+ pairs [O1][O4].
- **Discount mechanics:**
  - HALLOWEEN SALE bar with a countdown (00:00:00 at capture).
  - "LIMITED TIME OFFER • FREE EBOOK & STICKER CHART"; "3 NEW DESIGNS ADDED • LIMITED STOCK".
  - "One discount code per order".
  - Pop-up not captured [O1].
- **Weak / missing:**
  - Guarantee requires "unworn" product, which contradicts a results guarantee.
  - The protection fee is pre-ticked.
  - Social proof is inconsistent: "4.82 (1844+ happy parents)" vs "350,000+".
  - No absorbency number on the page.
  - Trustpilot 3.5 from 435 reviews; replies to 32% of negative reviews [O5].

**Kid Confident** [O6][O7][O8]
- **One-time:** 1 pair $19.99 **+ $5.99 shipping**. Big Kid Sizes $19.99 [O6][O7].
- **Bundles:**
  - 1 pair $19.99 / 2 pairs $39.98 (both "Standard Price", + shipping).
  - **7 pairs "Buy 3, Get 4 Free" $59.97 (compare-at $139.93, "Save $79.96") = $8.57/pair.**
  - There is also a "Pick A Curated Kit" path [O6].
- **Free gifts:** "$51 VALUE" at 7 pairs: free express shipping $5.99, Potty Training Playbook $29.99, reward chart $14.99 [O6].
- **Upsells:**
  - Leakproof Undie Covers for Bedtime, 4-pack $23.99 (compare-at $47.98) [O7].
  - Post-purchase: **ReConvert + Zipify OCU signatures** in the page HTML (INFERENCE [O74]).
  - Intelligems price testing installed [O8].
  - No shipping protection at checkout [O6 checkout].
- **Guarantee:** "60-Day Money Back Guarantee", "Results or Refund", "Less than 1% of customers claim". "Parent Promise: …full refund with no questions asked" [O6].
  - **The /policies/refund-policy page returns 404** [O6 policy fetch].
- **Shipping:** "Ships in 24hrs"; express shipping is free only in the 7-pair tier [O6].
- **Discounts:**
  - "BUY 3, GET 4 FREE | ENDING SOON"; "Limited Time Sale Ends On October 6th" (the capture date — a rolling date).
  - "LOW STOCK… RESERVE MY PACK".
  - Pop-up not captured [O6].
- **Weak / missing:**
  - Paid shipping below 7 pairs.
  - The middle tier (2 pairs) has no discount at all.
  - No written refund policy page.

**BrightKidCo** [O9][O10][O11]
- **One-time:** 1 pair $29.99 (product .js) [O9].
- **Bundles:**
  - "Standard Pack (4 Pairs)" $49.99.
  - "Potty Progress Pack (8 Pairs) Buy 5, get 3 free" $69.99 (compare-at $159.99).
  - **"Complete Training Bundle (12 Pairs) Buy 6, get 6 free" $99.99** (compare-at $219.99) = $8.33/pair.
  - The **12-pack was pre-selected**: add to cart put 12 pairs at $99.99 in the cart ("BKC 12-PACK (-$259.89)") [O9 cart/checkout].
- **Free gifts:** "FREE E-Book — Potty Training Guide $24.99" and "FREE Shipping $4.95" [O9].
- **Upsells:**
  - Cart shows the 2-in-1 Toilet Stairs $69.99 and a Waterproof Bag 3× $39.99 [O9 cart].
  - Catalogue cross-sells: mesh bags $34.99, mattress protector $39.99, blanket $59.99, Happy Poop™ Gummies $29.99–49.99 [O9 products.json].
  - Post-purchase app: none detected (INFERENCE).
- **Guarantee:**
  - The PDP sells "100-Day Money-Back Guarantee… email us within 100 days for a full refund. No pressure."
  - **But the refund policy says underwear "cannot be returned or refunded once worn, tried on, washed, or used in any manner"** [O9][O10].
  - The PDP promises a free size exchange; Trustpilot has "No exchange for wrong size" [O11].
- **Shipping:** "Free Shipping on orders $70+"; "Free shipping in 2-4 days" in the cart [O9].
- **Discounts:** "Our offer ends in" countdown; savings shown as "You save $120.00". Pop-up not captured [O9].
- **Weak / missing:** a headline guarantee that its own policy contradicts. Pre-selecting the biggest tier pushes AOV but risks refunds (INFERENCE).

**RaiseCalm** (clone ring, US) [O24][O25]
- **One-time:** 1 pair **$49.99** (a deliberately high anchor) [O24].
- **Bundles:**
  - 5 pairs "BUY 2, GET 3 FREE" $89.99 (compare-at $249.95).
  - **10 pairs "BUY 4, GET 6 FREE" $129.99 (compare-at $499.90), badged "⭐️ RECOMMENDED" and default in the cart** = $13/pair [O24 cart/checkout].
- **Free gifts:** Printable Pack ($27), Potty Training Guide ($37), Reward Chart ($17), free shipping [O24 checkout].
- **Upsells:** Rebuy and Seal Subscriptions signatures (INFERENCE [O74]). No protection fee seen at checkout.
- **Guarantee:** "90 Day Money Back Guarantee". The policy text covers only decks and digital products, and says **"Return shipping is the customer's responsibility"** [O24][O25].
- **Shipping:** "FREE SHIPPING OVER $45" [O24].
- **Discounts:** "BUNDLE & SAVE • LIMITED STOCK". Pop-up not captured.
- **Weak / missing:**
  - Per-pair price is the highest of all the clones.
  - The store is mostly parenting decks.
  - The refund policy does not cover underwear.

**ProudPants (Mirovanta)** [O19][O20][O21]
- **One-time:** single pair $19.99 (29 single-print SKUs) [O19 products.json].
- **Bundles:**
  - 5-Pack $39 (compare-at $99.95, "$7.80/pc").
  - **10-Pack $59 ("Full-time training + free Star Chart", "$5.90/pc") — the CTA reads "Add to Cart · $59", so it is the default.**
  - 15-Pack $79 ("$5.27/pc", "Most designs + 2 free bonus gifts").
  - "Savings shown vs. buying single pairs at $19.99 each" [O19].
- **Free gifts:** 5-Day Potty Training Jumpstart ($29), Free Insured Shipping ($9), plus a $39 gift at 15-pack [O19].
- **Upsells:** Waterproof Seat Liner $19.99 (compare-at $39.99) [O19 products.json]. Rebuy signature (INFERENCE).
- **Guarantee:**
  - "60 days to see progress, or your money back".
  - Standard 30-day returns are unworn only, with **"Customers are responsible for return shipping costs"** [O19][O20].
- **Shipping:** free insured shipping on bundles [O19].
- **Discounts:** "SAVE 61/70/74%" vs singles. Pop-up not captured.
- **Weak / missing:**
  - The store was created 2026-05; WH shows 0 visits/revenue [O21].
  - Sizes run only 2T–4T.
  - Its cost-per-pair transparency is the best in the set, but it sits on a no-name store.

**Sculptara** (Audrey Miller persona; AU-run, AUD at checkout) [O22][O23]
- **One-time:** 1 pair $29.99 ("38% OFF") [O22].
- **Bundles:** **5 pairs $69.99 ("One For Every Day Of The Week", MOST POPULAR — default in the cart)**; 10 pairs $109.99 ("Best Value Pack") [O22 cart].
- **Gifts/upsells:**
  - The cart shows "FREE Emergency Flashlight" (a leftover from a dropship template), Reward Chart & Stickers $9.99 and **Shipping Protection $3.99** [O22 cart].
  - Ebook $24.99 and printables $19.99 are sold separately.
  - Post-purchase app: none detected.
- **Guarantee:** the page shows both "60 Day Money Guarantee" and "30 DAY MONEY GUARANTEE". The policy is a 30-day, unworn-only return [O22][O23].
- **Shipping:** "fast & free shipping on all orders"; "FREE SHIPPING ENDS IN 24 HOURS" [O22].
- **Discounts:** "HALLOWEEN SALE 38% OFF". The checkout line is "SALE ENDS MIDNIGHT (-$79.96)" [O22 checkout].
- **Weak / missing:**
  - Contradicting guarantees.
  - Charges in AUD on a US-targeted page.
  - Junk gift.

**shopnola.store** (UpAiry copy) [O47][O48]
- **One-time:** 1 pair $23 on the page (compare-at $34; products.json says $17) [O47].
- **Bundles:** 5 pairs "BUY 2, GET 3 FREE" **$30.54** (pre-selected; $6.11/pair); 10 pairs "BUY 4, GET 6 FREE" $57.10 [O47 cart].
- **Gifts:** Printable Pack ($27) and "Secrets Of Potty Training" ($34) are free with the bundle [O47 cart].
- **Upsells:** the cart offers "Add 'Shipping Protection' For $3.31" and a $4.00 add-on [O47 cart]. Monster Cart signature.
- **Guarantee:**
  - The page copies "75 day guarantee" from UpAiry.
  - **The policy says "We do not accept returns or provide refunds for: Change-of-mind purchases"** [O47][O48].
- **Weak / missing:** the copied guarantee is false against its own policy.

**Brilliant Kids** [O43][O44]
- **One-time:** 1 pair $21.95 (compare-at **$105**, "Save 79%").
- **Free offer:** "Potty Training Underwear (FREE Today)" at $0, "Just Cover Shipping" [O43].
- **Bundles:** "3 Extra Potty Training Pairs 2.0" $19.50 (compare-at $65.85); **"Full Week Set (6 Pairs)" $39** ($6.50/pair, compare-at $131.70) [O43 products.json].
- **Gifts/upsells:** Playbook + bedtime ebook at $0 (compare-at $30). Bed mat $29.99 and portable potties $49.95 [O43 products.json].
- **Guarantee:** **"75-Day Potty Progress Guarantee (for used product)… full refund… even if the underwear [was used]… keep it or dispose of it"**. This is the only fully worn-product-friendly policy found [O44].
- **Discounts:** "FREE For Today Only!"; the "giving away 100 underwear" mechanic [O43].
- **Weak / missing:** a 79% "discount" anchor against a $105 compare-at strains credibility.

**Mezely** (PL general baby store) [O28][O29]
- **One-time:** "Potty Training Panties (Free Today)" $0 (compare-at $19.99), "Just Cover Shipping"; paid version $29.99 [O28].
- **Tiers:** Mystery Box "$30+ VALUE" $9.95–12.95 [O28 products.json].
- **Upsells:** cart drawer adds a Wash Bag $9.99 (compare-at $19.99), Anti-Slip Socks $8.99, Knee Pads $7.99 [O28]. **Zipify OCU + Rebuy signatures** (INFERENCE [O74]).
- **Guarantee:** 30 days, unworn, **"You will be responsible for paying for your shipping costs to return your item"** [O29].
- **Discounts:** "Anniversary Sale Ends In" countdown; "ONLY 6 LEFT IN STOCK, HURRY!"; "Only 6 Free Pairs left!" [O28].
- **Weak / missing:** fake scarcity; shipping cost is hidden until an address is entered (checkout subtotal $0.00) [O28 checkout].

**BlossomNest — EasyPotty™** [O45][O46]
- **One-time:** $14.99 (compare-at $29.99).
- **Bundles:** 3-pack $24.99 / **6-pack $36.99 "MOST POPULAR"** / 12-pack $72.99 ($8.33 / $6.17 / $6.08 per pair) [O45].
- **Shipping:** "FREE TRACKED SHIPPING ON ALL ORDERS". **Guarantee:** 30-day unworn returns with a label [O46].
- **Discounts:** "SUMMER FLASH SALE: UP TO 50% OFF - Today Only" (still running in October); "Scratch more special offers" gamification [O45].
- **Weak / missing:** no results guarantee and no gifts; the cheapest single pair among DTC sellers.

**Fvaulity** (general store) [O51]
- **Price:** $29.99 per pair (compare-at $60) [O51].
- **Upsell:** **Shipping Protection $3.50 is auto-added at checkout** ($29.99 → $33.49) [O51 checkout].
- **Shipping/returns:** free over $49.99; "30 Day Risk-Free Returns". No bundle tiers were visible.
- **Weak / missing:** a general store with no brand and no bundles.

**SunloveKids** [O52]
- **Price:** $32.99 (compare-at $37.99).
- **Discounts:** tiered codes SUN8 (8% over $99.99), SUN15 (15% over $199.99), SUN18 (18% over $299.99); "Sign up to unlock 5% off". Free shipping over $69.99 [O52].
- **Weak / missing:** the code ladder is a spend-more mechanic aimed at a whole-store basket; there is no underwear bundle.

**Kidsmegaworld "TootLoo"** [O49] and **Jackie's Kids "PottyPants" (UK)** [O50]
- **Prices (.js):**
  - TootLoo 4-pack $16.90–21.90, compare-at up to $31.90.
  - PottyPants 4-pack £14.90, compare-at £24.90.
  - Both offer quantity options 1–3 sets.
- **Walk result:** both storefronts render "**Store Currently Unavailable**". Checkout still opened via the cart link (TootLoo $16.90; PottyPants £14.90).
- **Weak / missing:** effectively dead storefronts.

**Tiny Tots Undies** [O15] — **cart not walked: the store is unreachable.** tinytotsundies.com fails the TLS handshake (curl, Firecrawl and the browser all failed), yet WH still logged ads up to 2026-09-27 [O72]. Price was never exposed; the ads say "bundles with exclusive gifts".

**Dead or pivoted (skipped, noted):**
- **Sevona:** shopsevona.com returns "This store is unavailable" [O26].
- **Pottiply:** redirects to seagumi.com, which sells gummies/orbs [O27].
- **Reviflora:** now sells towels [O75].
- **Drynimo:** no potty SKUs [O75].
- **MummyBuddy:** TLS failure [O75].
- **nematyta:** now sells bed-bug repellers [O75].
- **buybumkins.com:** redirects [O75].
- **Peekaa:** HTTP 402 [O75].
- **Brolly Sheets:** proxy 502 [O75].

---

### B. Premium, cloth and regional DTC (reusable)

**Rudie Baby (AU)** [O12][O13][O14]
- **One-time:** Toilet Training Underwear A$24.95; Training Pants A$29 [O12].
- **Bundles:**
  - 1 pair A$24.95 / "Weekday pack" 5 pairs A$99.95 (20% OFF) / "Family pack" 10 pairs A$169.95 (30% OFF).
  - 10× Training Pants A$101 (compare-at A$290).
  - Bobby's Complete Toilet Training Bundle A$120–140 (compare-at A$260–280).
  - Starter Kit A$169–199 [O12].
- **Gifts:** Bobby's Big Potty Adventure book A$26 is sold in a bundle (Pants + Book A$49). Bed guards A$69 and sheets A$98 are cross-sells [O12 products.json].
- **Upsells:** **AfterSell (post-purchase) signature** (INFERENCE [O74]). No protection fee at checkout [O12 checkout].
- **Guarantee:** **"strict no-returns policy for hygiene reasons"**. There is a "60-Day Risk-Free Trial" for first-time customers on **one item only**, with **no refunds or exchanges for wrong sizes** [O13].
- **Shipping:** free over A$60; Afterpay [O12][O14].
- **Weak / missing:** wrong sizes are not exchanged, and the trial covers one item.

**My Carry Potty (UK)** [O16][O17][O18]
- **Price:** Reusable Training Pants 3-pack £19.99; **6-pack £34.99** (£5.83/pair). Carry Potty + 3 pants £45.99; Ultimate bundles £85.99 (compare-at £107.99) [O16].
- **Gifts:** stickers "Free with £40 Order"; flashcards and a Potty Training Pack "Free with £65 Order" [O16 products.json].
- **Upsells:** UpCart. **Discounts:** "SIGN UP FOR 10% OFF"; free shipping over £50 [O16].
- **Returns:** "**My Little Training Pants cannot be returned (unless faulty)**"; other items within 14 days [O17].
- **Weak / missing:** no guarantee on the pants; ships to GB only [O18].

**Fig For Kids** [O30][O31]
- **Kit:** "girls/boys potty training kit" **$55** = 4 pairs GOTS-organic underwear + organic tote + rewards chart. The 2-4 size was sold out at capture [O30].
- **Singles and packs:** $10–15; starter set $54 (compare-at $60); 6-pack bundles $81 (compare-at $90) [O30 products.json].
- **Discounts:** "sign up for 15% off — free shipping on orders over $50 — buy 3 get 15% off" [O30].
- **Returns:** within 21 days, unworn. "Favorite Pair Guarantee". Free exchanges; **$8 handling fee on returns** [O31].
- **Weak / missing:** the gusset is only "2 layers" (light absorbency); out of stock.

**Smart Bottoms (cloth, US)** [O32][O33]
- **Price:** Daytime Trainer $16; Nighttime Trainer $18 (singles, 18/24M–4/5) [O32].
- **No bundles on the PDP.** Seal Subscriptions and Bundler signatures (INFERENCE).
- **Shipping/returns:** free shipping over $85; 30-day unused returns, sent to Kentwood MI [O32][O33].
- **Weak / missing:** no offer stack at all; sold as a cloth-diaper staple.

**Kanga Care — Lil Learnerz 2.0** [O53]
- **Price:** $15.99 single, sizes XS–XXL.
- **Upsell:** **Route Shipping Protection $1.95 auto-added** ($15.99 → $17.94) [O53 checkout]. Recharge and Redo signatures (INFERENCE). Free shipping over $150.

**Super Undies (special needs)** [O34][O35]
- **Price:** $34.99 per pair (snap or pull-on, S–XL) [O34].
- **Shipping:** "Easy $3.95 Domestic Shipping, Everyday!"; "Low stock - 7 in stock".
- **Returns:** within 14 days, unused. Store credit +$5, or a $9 label deduction on refunds [O35].
- **Weak / missing:** premium price with no bundles.

**Peejamas** [O36][O37]
- **Price:** Daytime Underwear 6-Pack $29.99 (~$5/pair). Overnight Booster Insert 3-Pack $19.99; Bottoms $35; Mattress Protector "40 oz!" $29.99–40; eBook $4.99 [O36].
- **Shipping:** "Free Shipping on US orders above $75" (cart shows "$75.00 away") [O36].
- **Walk result:** the checkout redirected to `/stock-problems`, so the 6-pack is out of stock or on pre-order [O36 checkout].
- **Returns:** unused, within 30 days of shipping; restocking fees possible [O37].

**Staydry (AU)** [O54] — Girls Toilet Training Bundle (bedding + pants) $169 (compare-at $211), AU. Out of US scope; noted.

**Bambino Mio (UK)** [O55] — bambinomio.com redirects to bambinomio.co.uk ("UP TO 40% OFF SELECTED FAVOURITES"). There is **no US storefront**. In the US it appears only as a Walmart third-party listing at $42.50 per 5-pack ($8.50/pair) [O55]. Cart not walked (UK-only site).

**Hanna Andersson** [O58] — **cart not walked: blocked by a bot wall** ("Press & Hold to confirm you are a human"). Same-day B-map price: $40 per 5-pack, $8/pair [O73].

**Thirsties** [O57] — **cart not walked: thirsties.com redirects to a parked-domain ad page.** Retail price is $21.65/pair at Green Mountain Diapers [O57][O73].

---

### C. Marketplace brands (sell on Amazon / Walmart / Target / TikTok Shop; no DTC cart walked)

The prices below are search-result or /dp/ prices on 2026-10-06.

- **MooMoo Baby:** $28.04–$35.99 per 8–10 pack ($2.97–4.12/pair), 17.7K ratings. A 4-pack is $19.99 [O59][O60].
  - Offer: none beyond Prime.
  - Gap: "value… mixed" per Amazon AI (144 of 327 value mentions negative) [O73].
- **BIG ELEPHANT:**
  - Amazon: 10-pack $19.79; core SKU $27.19 "Save 6%" [O59].
  - Walmart: 10-pack "Now $25.49 was $33.99" [O66].
  - TikTok Shop: $25.49/$33.99 SKUs (2,093 units in 30 days) and 10-pack $40.99 [O68].
  - No DTC store reachable (bigelephantshop.com proxy 502).
  - Gap: de-claimed ("NOT Diapers… Limited Absorbency") [O68].
- **Hanes:** Amazon $13.02 per 7-pack; Walmart "Now $10.12 was $15.00" per 6-pack; Target $13.99 per 6-pack with "Buy 1, get 1 50% off Hanes clothing" [O59][O66][O67].
- **Gerber:** Amazon $13.95 per 3-pack ($4.65/pair) [O63][O73].
- **Fruit of the Loom:** Walmart $12.98 per 6-pack [O66].
- **Licensed character packs (Target):** Mickey 6-pack $21.99 "with Bonus Sticker Chart"; Minnie 6-pack $15.99 [O67].
- **Pull-Ups (disposable):** $38.15 per 112 ($0.34/pant) [O64][O73].
- **Easy Ups (disposable):**
  - Amazon $36.90 per 124 ($0.30) [O65].
  - Target $10.49–49.49 with "Buy 1 get 1 40% off diapers, training pants & wipes" [O67].
  - Walmart $29.97 per 62 [O66].
- **Millie Moon (disposable):** "Luxury Training Pants From $26.99" on its own site [O56]. Target lists $24.99 per 72 (B-map) [O73].
- **Alppi (disposable DTC)** [O38][O39][O40]:
  - Training Pants Bundles $53.70 (compare-at $63.40); Weekly Bag $31.70; Monthly Box $105.
  - **BOGO sample $8.90 (compare-at $17.80)**.
  - "25% OFF for First Subscription Order"; "FREE Dry Wipes Over $30"; free shipping over $50.
  - Appstle subscriptions and memberships, Kaching, UpCart.
  - Returns: 30 days, unopened only.

### D. Method sellers (indirect)

- **Big Little Feelings — Potty Training Made Simple:** **$34** (sale history $25), "30-DAY MONEY-BACK GUARANTEE", "LIFETIME ACCESS". Potty + Toddler bundle $123; "get both… save $10". Checkout $34.00 [O41].
  - Gap: no product. Their ads say "You bring the undies" [O72].
- **Oh Crap! (Jamie Glowacki):** courses and live classes such as "The Boundary Clinic… $99". The site has "Product Recommendations" (affiliate) and a free guide lead magnet [O42]. Book $16.78 on Amazon [O73]. Not a cart product; no walk.

---

---

## Summary table (4 columns: competitor · price · best offer · gap)

**Big-kid / same-parent set (the locked market)**

| Competitor | Price (single → best tier) | Best offer | Gap |
|---|---|---|---|
| BrightKidCo Sensory [B18] | $29.99 → 12 for $119.99 ($10.00/pr) | 12-pack default, ebook + free ship, "100-day" headline, free size exchange | Sizes S–L only; "help make it right" ≠ refund; worn = no refund; 0 live ads |
| Kid Confident Big Kid [B20] | $19.99 + $5.99 ship → 7 for $59.97 ($8.57) | B3G4 + "$51 value" gifts + 60-day results promise | 2 colours, ages not stated, toddler proof, refund policy 404, fake "89% reserved" |
| Super Undies [B34] | $34.99 → 5 + 3 liners $219.60 ($43.92) | Free laundry bag at $99, free ship at $149, $3.95 flat ship | Sold as "diapers"; bundle costs more than singles; 14-day unused returns; 2-week ship |
| Peejamas [B25] | $19.99 boosters / $29.99 day 6-pack | Oz stated (4 oz booster, ~10 oz jammies) | Numbers on night products only; daytime toddler-size, out of stock |
| MooMoo 2T-9Y / 9T [B26][U10] | $2.97–3.60/pr (10-pack) | Price + Prime + 30-day returns | "small accidents", no ml; leakage 116/180 negative |
| BIG ELEPHANT 9-10Y [B28] | $2.55/pr (10 for $25.49, was $33.99) | Low price, 7–8 and 9–10 sizes | "Toddler" on a 9–10Y pack; "Limited Absorbency" |
| Carer / TIICHOO / FUVVRVAL [U8] | $6.40–13.75/pr | Big sizes to 18, absorbent | "Incontinence" naming, no brand, no number |
| Goodnites [B45] | $1.14/pant (disposable) | Retail ubiquity; "16 oz" (2023 ad) | Night only; recurring cost; not school-day |
| Lucky & Me [B40] | $38 per 6 ($6.33/pr) | 30-day guarantee incl. opened pairs + free US return shipping | No absorbency |
| WunderUndies / SmartKnitKIDS [B42][B44] | $8–13 / $18.50 per pair | Size trial pack $25 / sizes to 10-12 | No absorbency; final sale once opened / 3.3★ |
| Saphire (indirect) [B36] | $35 → B3G2 $103 ($21/pack) | B2G1 + ebook gifts + 40% sub + AfterSell | Subscription complaints; unopened-only refunds; fake-profile complaint |
| Bloomwise (indirect) [B38] | $34.95 → B3G2 $89.13 | B2G1 90-day default + free ship + protocol + mystery gift | Default tier silently = subscription every 60 days; one claim per household |

**Toddler-category set (sections A–D, carried over)** — unchanged rows: UpAiry $21 → 10 for $68 · Kid Confident $19.99 → 7 for $59.97 · BrightKidCo $29.99 → 12 for $99.99 · RaiseCalm $49.99 → 10 for $129.99 · ProudPants $19.99 → 15 for $79 · Sculptara $29.99 → 10 for $109.99 · shopnola $23 → 10 for $57.10 · Brilliant Kids free + ship → 6 for $39 · Mezely free + ship · BlossomNest $14.99 → 12 for $72.99 · Fvaulity / SunloveKids $29.99 / $32.99 · TootLoo / PottyPants (dead) · Rudie A$24.95 → 10 for A$169.95 · My Carry Potty £34.99/6 · Fig $55 kit · Smart Bottoms / Kanga $16–18 / $15.99 · Amazon toddler leaders $1.86–4.65/pr · disposables $0.30–0.84/pant · BLF $34 course / Oh Crap $99 class. Full table + gaps: section A–D blocks above and work/D4-s15.md.

**Table stakes** (at least half of the 8 walked big-kid / same-parent DTC stores — BrightKidCo, Kid Confident, Super Undies, Peejamas, Lucky & Me, WunderUndies, Saphire, Bloomwise — do it, so we must match it):
- **Multi-pair packs with a lower per-unit price** — 8 of 8 (tiers or packs as the unit).
- **A free-shipping threshold of $50–$75** (or free shipping inside the bundle) — 8 of 8 (BKC $70, Saphire $70, Peejamas $75, Bloomwise / Lucky & Me / WunderUndies $50, Kid Confident 7-pack, Super Undies $149).
- **A money-back / satisfaction guarantee headline (30–100 days)** — 5 of 8 (BKC 100, KC 60, Saphire 60, Bloomwise 60, Lucky & Me 30).
- **"Buy X, get Y free" framing with free digital gifts** — 4 of 8 (BKC, KC, Saphire, Bloomwise). Exactly half: match the *"free"* framing, not the fake anchors.
- **Urgency devices** (countdown, "sold in last 2 hours", "89% reserved", "reserved for 02:54") — 4 of 8. **We refuse this one by policy (§4 / §4B)** and say so on the page.

**Best-in-class:**
- **Stack:** BrightKidCo Sensory — 12 pairs for $119.99 pre-selected, free ebook + free shipping, a 100-day headline, free size exchange [B18]. It's the exact AOV we target ($119), on a page now abandoned in paid.
- **Risk reversal:** **Lucky & Me's 30-day Comfiness Guarantee** — full refund *or* exchange, opened pairs accepted, free US return shipping [B40].
- **AOV machinery:** Saphire — Kaching tiers + CartBot free gift + UpCart + AfterSell post-purchase + Intelligems price tests [B37].

**Nobody offers** (open slots → Offer inputs):
1. **A printed, per-size capacity (ml) on daytime big-kid underwear that looks like underwear.** Super Undies states ml but sells a "diaper"; Peejamas / Goodnites state oz on *night* products; every big-kid daytime pant (BKC, KC, MooMoo, BIG ELEPHANT, Carer) states none.
2. **A school-day kit**: pairs + wet bag + discreet backpack spare pouch + teacher note. BKC sells wet bags as $39.99 add-ons; Super Undies gives a laundry bag at $99; nobody frames school.
3. **A guarantee tied to the number and usable after wearing**: "holds what the label says, or your money back — keep the pants." Every absorbent seller refuses worn returns (BKC, Super Undies, Peejamas) or 404s its policy (KC); only Lucky & Me (non-absorbent) accepts opened pairs.
4. **Daytime sizes 4 → 12 in one line with a size chart by weight + waist + thigh.** BKC stops at L, KC states no ages, MooMoo / BIG ELEPHANT are marketplace toddler pants scaled up, Lucky & Me goes to 14 but holds nothing.
5. **Free size swaps for a growing kid + an opt-in size-up reminder, with no subscription.** Subscriptions here are a complaint source (Saphire 7 + 5 + 2 [B37]; Bloomwise defaults to one [B38]).
6. **Nothing pre-ticked, no timer, per-pair price shown.** 4 of 8 run urgency; Bloomwise pre-selects a subscription; UpAiry / Fvaulity / Kanga pre-add protection (section A).

**So What → do this:** match the four table stakes we can honestly match (multi-pair tiers, free shipping at the kit tier, a long guarantee, "free" framing on real items), refuse the fifth (fake urgency) out loud, and build the offer on Nobody-offers #1–#3. The guarantee is the weapon: the absorbent sellers all refuse worn pants.

---

## Price ladder — big-kid daytime absorbent underwear, per pair (the $11–14 zone)

| Level | Real price (per pair) | Source |
|---|---|---|
| **AliExpress / Alibaba (floor)** | **No dropship big-kid (6–12) daytime trainer with an underwear look exists on AliExpress** (only $0.99 "New shoppers" teasers + a 2–7Y pocket diaper — rejected) [U6]. Alibaba: toddler stock trainer $1.05–1.20 [U2]; "Big Xl Cloth Diapers for Older Children Aged 6-10" $2.30 [U3]; adult "Maximum Absorbency 200ml" brief $6–7 (MOQ 100) [U1]. **Our OEM placeholder: $4.00 FOB + $0.60 freight = $4.60 landed (PROVISIONAL)** | [U1]–[U6] |
| **CJ Dropshipping** | Not captured — human-verification wall | [O70] |
| **Amazon** | MooMoo 9T $2.97 · MooMoo 2T-9Y $3.60 · TIICHOO $6.40 · Carer size 10 **$10.00** / 3-pack **$13.75** · "Dinosaur 8-10Years" $18.99 per listing (pack size not captured) · SmartKnitKIDS (non-absorbent) $18.50 · Goodnites (disposable) $1.14/pant via Walmart | [U10][B26][U8][U11][B44][B45] |
| **Walmart** | BIG ELEPHANT 9-10Y **$2.55** (10 for $25.49, was $33.99); 7–8Y $2.49 | [B28] |
| **TikTok Shop** | BIG ELEPHANT 10-pack ≈ **$3.34** (722 units / $24.1K, 30d) | [U29] |
| **DTC big-kid bundle tier** | Peejamas day 6-pack $5.00 · Lucky & Me $6.33 (no absorbency) · Kid Confident Big Kid **$8.57** · BrightKidCo Sensory **$10.00** (12) / **$11.25** (8) / **$15.00** (4) | [O36][B40][B20][B18] |
| **DTC single (anchor)** | WunderUndies $8–13 (no absorbency) · Kid Confident $19.99 + $5.99 ship · BrightKidCo $29.99 · Super Undies $34.99 · Brain Trainers $44.99 · Super Undies 5-pack $43.92 incl. liners | [B42][B20][B18][B34] |
| **Ours (test)** | **10-pair School-Day Kit $119 = $11.90** (pre-selected) · 6 for $84 = $14.00 · 15 for $159 = $10.60 · single $19 | Offer inputs below |

**What the ladder says:**
- **Floor:** $2.55–3.60/pr for big sizes on marketplaces (BIG ELEPHANT, MooMoo) — toddler pants scaled up, no number. Source cost for a real big-kid spec is unknown; our $4.00 FOB is a placeholder.
- **Ceiling:** $34.99–44.99 per pair (Super Undies singles), sold as special-needs "diapers".
- **Our zone ($10–15/pr) is already proven by two sellers to this exact parent:** BrightKidCo Sensory ($10–15/pr) and Carer ($10–13.75/pr). $11.90 sits between BKC's 8-pack ($11.25) and its 4-pack ($15.00), next to Carer's $10–13.75, and is **≈4× MooMoo**.
- **What has to justify the 4× premium** (INFERENCE from the gaps above): a **visible ml difference on camera vs a MooMoo 9T** (lock risk #4), sizes to 12, the School-Day Kit, and a guarantee you can use after wearing. Without the pour-test number, we're a $3 product priced at $12 — **don't launch the price without the number.**

---

## Offer inputs for Step 2 (matched to the Offer Build reference [O71], opened via the Notion connector this run)

*Reference input list, in its order: offer TYPE → bundle rules → first-order pop-up → always-on components (anchor, reason, guarantee, protect margin, target AOV) → measure first order AND 90-day LTV. Each is filled below. Counts = §2C bank, 601 rows (work/2C-tally.md); "school-age" = the 79-row locked cut.*

**1 · Problems the offer stack must solve (top of §10 + §11, with counts)**
| Problem (her words / tag) | Count | Offer element that solves it |
|---|---|---|
| "It won't hold the pee / it leaks" (objection) | **47** (+ "holds only one small accident" **14**; need "absorbency that holds a pee" **104**) | Per-size ml printed on the pack + pour video on the PDP + the Number Guarantee (below) |
| Daily accidents at school (pain) | **38** bank · **34 of 79** school-age (#1) | The **School-Day Kit**: enough pairs for a week + backpack spare pouch + wet bag + teacher note |
| Scam / hidden subscription (objection) | **16** (+ honest-checkout need **13**) | No subscription, nothing pre-ticked, one price per tier, checkout screenshot on the PDP |
| Waste of money (objection) | **15** (+ "waste of money" burned **34**) | Worn-product guarantee + sourced cost math vs disposables ($0.30–0.35/pant [M47-B]; Goodnites $1.14 [B45]) |
| Sizing / fit uncertain (objection) | **13** (+ bigger sizes need **24**; sizing / fit pain **17**; size / big-kid products pain **18**) | Sizes 4–12, chart by weight + waist + thigh, **free size swaps for 100 days** |
| Price (objection) | **10** | Per-pair price shown; honest head-to-head vs MooMoo 9T ("more per pair; here's the ml difference") |
| Judgment / shame (pain) | **30** (+ parent guilt **19**, child shame **13**) | No-shame voice on every surface; discreet packaging; teacher note written for the kid's dignity |
| Feels like a diaper / sensory (objection + pain) | **5** + sensory discomfort **17** (+ sensory-friendly need **16**) | Flat seams, tagless printed label, low-bulk core; "would you know?" photo test |
| Shipped from China / slow (objection) | **5** (+ slow shipping pain **4**) | US 3PL stock, 2–5-day promise, honest origin label |
| Routine / reminder (need) | **14** bank · **7** school-age | Teacher note card with a bathroom-reminder line; printable school-day checklist (inside the kit, not a "free ebook" anchor) |

**2 · Offer TYPE** (reference Step 1): **Type 2 — Bundle** (same product, different designs / sizes) **+ Type 3 — First-Order pop-up**.
- **Type 1 (front-loaded subscription) is rejected** — not a consumable; the market's subscriptions are a complaint source (Saphire, Bloomwise, UpAiry). The repeat lever is an **opt-in size-up reminder email** + free size swaps, not a subscription.

**3 · Bundle build (reference Type 2 rules, applied)**
| Tier (named by result) | Contents | Price | $/pair | Role |
|---|---|---|---|---|
| Single "Try a pair" | 1 pair | **$19** | $19.00 | Anchor only (CM $6.83 can't carry paid traffic) |
| **"School Week"** | 6 pairs | **$84** | $14.00 | Entry tier; free shipping starts here |
| **"School-Day Kit" — pre-selected** | 10 pairs + wet bag + discreet backpack spare pouch + teacher note card | **$119** | $11.90 | **Target AOV** (middle option, auto-selected) |
| "Full Term" | 15 pairs + the kit extras | **$159** | $10.60 | Value / two-size households |
- **Same-product multi-packs only** (reference): designs and sizes vary inside, no mixed product types.
- **Anchor to the single:** "$19 a pair alone → $11.90 a pair in the kit."
- **"Free," not "% off," on real items:** "Wet bag, spare pouch and teacher note **free** in the kit · **free** shipping from 6 pairs · **free** size swaps." No "Buy 6 get 6" against an inflated compare-at (§4B: no fake anchors).
- **Flash-Deals page (reference suggests one): NOT at launch.** Its countdown + "79% claimed" mechanic contradicts the locked attitude (§4 #4: no timer). Use a **real, dated drop** only (new size / design restock), never a perpetual timer.

**4 · Natural bundles (the evidence-led ones)**
- **School-Day Kit** (above) — from need "spare-clothes kit for school" **7** bank / **4** school-age, and the teacher's own instruction: "We send extra clothes and she keeps them in her backpack and changes herself" [C:N313].
- **Two-size pack for a growing kid** (e.g. 5 × size 8 + 5 × size 10) at kit price — answers sizing **13** + bigger sizes **24**.
- **No day + night bundle.** Night is out of scope and TAKEN (Saphire, Goodnites, Super Undies); the PDP points night needs to disposables (§2 lock).

**5 · Guarantee gap → "The Number Guarantee"** (always-on component)
- Wording to test: **"100 days. If a pair doesn't hold the number printed for its size — or it just doesn't work for your kid — full refund. Keep the pants. Free size swaps for 100 days."**
- Why: every absorbent competitor refuses worn pants (BKC [O10], Super Undies [O35], Peejamas [O37]) or has no policy page (KC [O6]); Lucky & Me proves an opened-pair refund is workable [B40]. The policy text must match the headline word for word (§11 #13).
- Confidence stat: add "x% of families asked for a refund" **only once real** (reference rule; competitors' "less than 1%" claims are unverifiable).

**6 · Price point to test:** **10-pair School-Day Kit at $119 ($11.90/pair), pre-selected**, with 6 for $84 as the entry tier.
- Pre-0 re-run at this price (work/D1-Pre0-rerun.md, PROVISIONAL costs): **CM $59.93 (50.4%) · break-even ROAS 1.99 · kill line CPA $36.13 · scale line CPA $24.23.**
- **Duty switch:** with ~35% duty (landed $6.00), the kit's scale CPA falls to $10.23 → push **6 for $84** as hero instead (scale CPA $13.28). The broker's duty quote decides.
- **Price-match stress test:** cutting the kit to $99 to sit under BrightKidCo's $10/pr drops CM to $40.53 (no duty) and to **26.8% CM with duty — below 30%**. **Don't price-match; win on the number.**

**7 · First-order pop-up (reference Type 3)**
- Target AOV is **$119 > $100 → dollar-off wins** (reference rule). Test **"$15 off your first kit"** vs **"$15 store credit"** (store credit framing won the reference's 8-way test). For the $84 tier (<$100) the same pop-up reads as "**18% off**" (odd-number specificity).
- **One number only:** no site-wide sale stacked on top (reference rule: never run conflicting offers).
- Margin check: kit at $104 after $15 off → CM ≈ $45.38 (INFERENCE, same formulas).
- **Don't run:** a giveaway or a "free guide" pop-up (reference: low-intent leads).

**8 · Always-on components (reference list)**
- **Price anchor:** "A box of big-kid disposables is $1.14 a pant [B45]; 10 pairs you wash and reuse are $119 (wash life to be tested and stated, not assumed)." Show the math, no "save $100s/month" (§2B).
- **Reason for the discount:** "**Founding families: the first 500 kits**" (a real cap; publish the counter).
- **Guarantee:** The Number Guarantee (5).
- **Protect margin:** list price $19/pair is the honest single price; tiers discount down from it.
- **Target AOV:** **$119** — the whole PDP (pre-selected tier, free-shipping bar at 6 pairs, cart add-ons) is built to hit it.
- **No pre-ticked fees, no shipping protection pre-added, no subscription, no timer** — stated in the cart (Nobody-offers #6).

**9 · Measure both (reference rule):** first-order CVR **and** 90-day LTV. Repeat levers to watch: size-up reorders (kids grow out in ~12 months — INFERENCE), second-child orders, extra spare-pouch packs.

**10 · Post-purchase upsell candidates** (leaders use AfterSell / ReConvert / Zipify OCU [B37][O8]): one click "**+3 pairs in the next size up, $33**" (sized for growth); "extra backpack spare pouch + wet bag, $14". Nothing for night.

---

## Sources (Doc 4, §15 FINAL)

**New this run (B-series; continues after B33)** — all 2026-10-06:
- [B34] Super Undies "(5 Pack) 3-in-1 Diapers for Big Kids & 3 Liners": https://superundies.com/products/5-pack-waterproof-undies (+ cart, checkout) and https://superundies.com/products.json · Playwright + curl · `work/15-captures/B/superundies-bigkid5-*`, `superundies.com.products.json` · VERBATIM
- [B35] Winning Hunter `get_store_details` superundies.com (theme "Canopy w/navidium", no apps listed, AOV $90.81, 13,098 visits) · DATA
- [B36] Saphire: https://trysaphire.com/products/saphire-saffron-gummies (+ cart, checkout), advertorial https://trysaphire.com/pages/bed-wetting-5rw, policy https://trysaphire.com/policies/refund-policy, https://trysaphire.com/products.json · Playwright · `work/15-captures/B/saphire-*`, `pol-trysaphire.com.html` · VERBATIM
- [B37] Winning Hunter `get_store_details` trysaphire.com (apps: AfterSell, Kaching, UpCart, CartBot, Intelligems, Judge.me, Klaviyo, Triple Whale; Trustpilot 3.0 / 74 and gap counts) · DATA
- [B38] Bloomwise: https://hellobloomkids.com/products/give-your-child-the-calm-theyve-been-missing (+ cart, checkout), policy https://hellobloomkids.com/policies/refund-policy, https://hellobloomkids.com/products.json · Playwright · `work/15-captures/B/bloomwise-pdp-*`, `pol-hellobloomkids.com.html` · VERBATIM
- [B39] Winning Hunter `get_store_details` hellobloomkids.com (Recharge Subscriptions, Kaching; AOV $58.12) · DATA
- [B40] Lucky & Me: https://luckyandme.com/products/lucas-boys-organic-cotton-briefs (+ cart, checkout), policy https://luckyandme.com/policies/refund-policy, https://luckyandme.com/products.json · Playwright · `work/15-captures/B/luckyandme-*`, `pol-luckyandme.com.html` · VERBATIM
- [B41] Winning Hunter `get_store_details` luckyandme.com (LoyaltyLion, ReturnGO, Slide Cart, Klaviyo; 35,294 visits; 30d $184K–$295K) · DATA
- [B42] WunderUndies: https://wunderundies.com/products/kids-briefs-flat-seams (+ cart, checkout), policy https://wunderundies.com/policies/refund-policy · Playwright · `work/15-captures/B/wunderundies-*`, `pol-wunderundies.com.html` · VERBATIM
- [B43] Winning Hunter `get_store_details` wunderundies.com (OptiMonk, Dr. Discount on Cart, Slide Cart, GoAffPro; 1,941 visits) · DATA
- [B44] Amazon SmartKnitKIDS Seamless Sensitivity Undies: https://www.amazon.com/dp/B09BN3YPSS (resolved to /dp/B01MUXPA54) · Firecrawl `query` · VERBATIM ($18.50; S 4-5 / M 6-8 / L 10-12; 3.3★ 96)
- [B45] Goodnites retail prices: https://www.walmart.com/ip/Goodnites-Bedwetting-Underwear-for-Boys-S-M-43-68-lbs-44-Ct-Select-for-More/35511656 · https://www.target.com/p/goodnites-boys-39-nighttime-bedwetting-underwear-l-xl-34ct/-/A-15417310 · https://www.samsclub.com/ip/Goodnites-Nighttime-Bedwetting-Underwear-for-Boys-Sizes-Extra-Small-Extra-Extra-Large/3600045083 · `firecrawl_search` · SNIPPET. Plus goodnites.com PDP → 403 to Playwright (`work/15-captures/B/goodnites-1-pdp.txt`)
- [B46] Kid Confident: https://kidconfident.co/products.json (Big Kid Sizes $19.99, SM/MD/LG, 2 colours; undie covers $23.99) + Firecrawl `query` on the Big Kid PDP for the size chart → no ages / waists in page text · VERBATIM / DATA
- [B47] BrightKidCo catalogue: https://www.brightkidco.com/products.json (sensory edition $29.99, sizes S/M/L; cross-sell prices) · `work/15-captures/B/brightkidco.com.products.json` · VERBATIM

**Re-used B (defined earlier by Writer B):** [B18] BrightKidCo Sensory PDP / cart / checkout · [B20] Kid Confident Big Kid PDP / cart / checkout · [B25] Peejamas Overnight Booster PDP / cart / checkout · [B26] Amazon MooMoo 2T-9Y https://www.amazon.com/dp/B0C36DDD2B (re-scraped this run: $35.99 / 10, $3.60/count) · [B28] Walmart BIG ELEPHANT 9-10Y https://www.walmart.com/ip/17438769713 (re-scraped: $25.49 was $33.99; 7–8Y $24.93). Full lines in work/D3-s13.md.

**Re-used U / W / M (Pre-0 LOCKED, §1 LOCKED):** [U1]–[U6] Alibaba / AliExpress cost evidence · [U8][U9] Amazon big-kid absorbent searches · [U10] MooMoo 9T · [U11] "Dinosaur 8-10Years" · [U24] BrightKidCo ads · [U25] Super Undies ads · [U27] Goodnites ads · [U28] SmartKnitKIDS ads · [U29] TikTok Shop big-kid products · [W2] SimilarWeb superundies.com · [M30] Kid Confident paused ad · [M47-B] disposables $/pant. URLs in work/D1-Pre0-LOCKED.md, work/D1-s1-LOCKED.md, work/D4-s2B-LOCKED.md.

**Re-used O (sections A–D, wave 1, same day):** [O1]–[O75] exactly as listed in work/D4-s15.md "Sources (Doc 4, §15)". Key ones used here: [O6] Kid Confident (refund policy 404) · [O8] WH kidconfident.co · [O10] BrightKidCo refund policy · [O11] WH brightkidco.com · [O34][O35] Super Undies PDP / policy · [O36][O37] Peejamas PDP / policy · [O70] CJ blocked · [O71] **Notion "💰 Reference — Offer Build (Grand Slam Offer)" https://app.notion.com/p/3d9d53123cd681dabc18f09e90184c44 — re-fetched via the Notion connector this run (last edited 2026-09-20)** · VERBATIM · [O74] app signatures.

### Data-bank rows cited (§2C)
- [C:N313] https://www.reddit.com/r/kindergarten/comments/1gobdc0/son_keeps_having_potty_accidents/ · Reddit r/kindergarten · ~2024-11 (est. from post ID) · SNIPPET

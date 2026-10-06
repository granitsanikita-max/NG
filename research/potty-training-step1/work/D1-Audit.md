# Audit first — UpAiry, the control we're modelling (no store of our own yet)

**Why UpAiry:**
- It is the highest-traffic competitor in this category: 356,447 visits in Aug 2026, 95.4% US (DATA [M24]).
- Its estimated 30-day revenue is $1.8M–$3.4M (DATA [M24]).
- §1 re-checked this: no other competitor comes within 10× on traffic (Kid Confident 17,087; BrightKidCo 19,689 [M25][M26]).

**How:**
- Both pages were walked with `playwright-skill`: headless Chromium, mobile 390×844 viewport, plus a desktop pass for the buy box.
- Prices came from the store's product JSON [M3]. The bundle tiers came from the page's Kaching config [M4].
- Date: 2026-10-06.

---

## Page 1 — PDP: https://www.upairy.com/products/potty-training-underwear [M1]
**What it does:**
- Hero headline: "Potty Training Underwear… Feel & Learn™ Technology helps toddlers recognize when it's time to use the potty — with many families seeing progress in just days." (VERBATIM [M1])
- Benefit bullets: "potty trained in WEEKS not MONTHS · save $100+ on disposables monthly · 3-layer Feel & Learn™ Technology · visible progress in just 2-3 weeks · backed by a 75 day guarantee".
- Gift ladder: free printables at 5+ pairs, free shipping at 10+.
- Long FAQ: "Is this better than disposables?", "How does it actually work?", "Are they worth the price?"
- Reviews block: "4.9 out of 5, Based on 4,326 reviews".
- Price $21, compare-at $29.99 [M3]. Tiers: 1 pair $21 · 5 pairs $35 · 10 pairs $68 [M4].

**What's weak (each is an opening):**
1. **The social proof contradicts itself on one page** (VERBATIM [M1]). It shows five different "customer" counts:
   - "4.82 (1844+ happy parents)"
   - "Join 350,000+ parents"
   - "100k+ families and counting"
   - "4.8/5 stars by 30,000+ parents"
   - "Based on 4,326 reviews"

   Off-site, Trustpilot rates it 3.5★ from 435 reviews, and it replies to only 32% of 124 negative reviews (DATA [M24]).
2. **It calls its own product a diaper.**
   - The page says "We're not diapers. We're not pull-ups."
   - Its own meta description says "Our special diapers help them feel when they're wet" (VERBATIM, og:description [M1]). That's sloppy and erodes trust.
3. **It contradicts itself on layers.**
   - "3-layer Feel & Learn™ System" vs "six layers of eco-friendly materials" vs "our potty training underwear stands out with its innovative 2-layer design" (VERBATIM [M1]).
   - The mechanism story isn't even consistent.
4. **It contradicts itself on night use.**
   - "Can I use them overnight? Yes! … designed to keep your child dry and comfortable all night."
   - Then: "designed primarily for daytime training… there may still be some leakage" and "they're not leakproof in the way a diaper is" (VERBATIM [M1]).
   - Leakage is the #1 Trustpilot complaint: 12 + 10 reviews, plus 2 "leak proof claim false" (DATA [M24]).
5. **The speed claims conflict with its own legal disclaimer.**
   - Hero and ads: "potty trained in WEEKS not MONTHS", "results in days instead of months".
   - Footer: "UpAiry makes no guarantee of specific results or timeline… Timelines and outcomes shown in testimonials are exceptional results and are not guaranteed" (VERBATIM [M1]).
   - That is an FTC substantiation exposure (see §2B) and a credibility gap we can exploit by stating capacity and time honestly.
6. **It never quantifies absorbency.** It says "holds up to 3x more liquid than regular underwear" but gives no ml or oz anywhere on the page [M1]. No competitor shows a measured pour test either (0 of 908 unique corpus ads mention ml or oz [M23]).
7. **The buy box is broken or fake-urgent.**
   - The "HALLOWEEN SALE" countdown rendered **00:00:00** in both mobile and desktop captures.
   - No price or quantity tier rendered in the headless capture. Only "Add to Cart" and four locked "FREE GIFTS TODAY ONLY" tiles showed [screenshot, M1]. (INFERENCE: the Kaching widget is slow to load or blocked by bots, so real users may also see a delay.)
8. **The sizing is narrow and toddler-coded.**
   - S/M/L by weight (7–55 lb) on this PDP; XL (55–70 lb) only on a separate PDP [M42].
   - The copy is "Specifically engineered for children aged 18 months to 4 years" (VERBATIM [M1]), yet its ads target 4.5–5-year-olds (§1 ad log).
9. **Subscription trust debt.** The footer links "Subscription Policy · Manage Subscription". Trustpilot lists 19 complaints of a "hidden subscription for free gift gummies" (DATA [M24]).
10. **Fake "sold only here" scarcity.**
    - It says "UpAiry products are ONLY sold through our official website… Products found on Amazon… are counterfeit" (VERBATIM [M1]).
    - Yet "Upairy" listings run Amazon ads at $27.19 per 10-pack and $33.99 [M18].
    - An informed shopper sees a contradiction.

## Page 2 — persona advertorial: https://www.upairy.com/pages/training-underwear [M2]
**What it does:** it's the landing page for the persona pages (Bec, Emma, Kate).
- Headline: "The Child Psychology-Backed Training Pants Designed To Get Toddlers Potty Trained In Weeks" (VERBATIM).
- It then runs a cause → solution → results block, a "3 Simple Stages" timeline ("Day 1-3 Learning Begins… Week 2+ Fully Trained… Complete potty independence"), and the same PDP body below.

**What's weak:**
1. **The page has a fourth and fifth count:** "Trusted by 60,000+ Parents" and "92,352+ Happy Customers… Based on 1,342 Reviews" (VERBATIM [M2]). That adds to the five on the PDP.
2. **It gives a hard timeline ("Week 2+ Fully Trained").** The PDP disclaimer says no timeline is guaranteed [M1][M2]. That's the strongest FTC-exposure line in the funnel.
3. **"Child Psychology-Backed" names no study, expert or source** anywhere on the page [M2].
4. **It already speaks to working parents.** The page says "traditional methods weren't designed for families with full-time schedules. Disposables seem necessary because daycare needs containment" (VERBATIM [M2]). **This matters for §2:** the working-parent / daycare positioning hypothesis is already on UpAiry's own landing page.
5. **It sends a "persona" story to a corporate page.** The advertorial reads as the brand, not as the mom in the ad, so the persona-to-page handoff breaks the story (INFERENCE).
6. **The CTA says "Out of stock" next to "Add to Cart"** in the capture (VERBATIM [M2]). That's either a stock-out on the default variant or a fake-scarcity widget. Either way it causes friction.

## A third page found in the audit — https://www.upairy.com/pages/daycare-mandate [M5]
- It's a news-style advertorial: "THE DAILY PARENT — Schools Are Sending Unpotty-Trained Kids Home — And One Paediatric OT Says the Real Problem Isn't Readiness" (VERBATIM).
- The byline is "Allen Jahiger, Parenting Researcher". It claims "pediatric OTs are recommending UpAiry training pants" without naming one.
- The layer copy says "Layer 3 - Leak-Resistant Barrier: Protects car seats, daycare mats, grandma's couch" and "Safe for car rides, daycare, errands, grandma's house" (VERBATIM).
- **Weak:**
  - Fabricated-looking authority: an unnamed OT and a "Parenting Researcher" byline. That's exposure under the 16 CFR 465 fake-testimonial rule [M54].
  - "100% cotton" is printed on a 3-layer product with a TPU waterproof layer [M1].
- **Why it matters:** UpAiry already owns the daycare / school-mandate story in paid traffic (Kereisa Collens ad 2180542355823055 links here; ad log).

## So What → do this
UpAiry wins on volume and persona storytelling, not on trust or proof. Our page must beat it on the six weak spots it can't fix without contradicting itself:
1. **One** consistent, real review count.
2. A **measured capacity** in ml/oz, with a pour-test video.
3. **One** layer story, matching the actual spec.
4. Honest day/night guidance.
5. No hidden subscription.
6. No fake timelines.

Never copy its persona or "Daily Parent" formats: they carry FTC fake-testimonial risk [M54]. The daycare / working-parent story is **already on its pages** (see [M2], [M5]), so §2 must not assume it's open.

## Sources
- [M1] UpAiry PDP: https://www.upairy.com/products/potty-training-underwear. Playwright headless (mobile + desktop), 2026-10-06 (VERBATIM). Screenshots saved locally in the session scratchpad.
- [M2] UpAiry advertorial: https://www.upairy.com/pages/training-underwear. Playwright headless, 2026-10-06 (VERBATIM).
- [M3] UpAiry product JSON: https://www.upairy.com/products/potty-training-underwear.js. 2026-10-06 (DATA).
- [M4] UpAiry PDP Kaching `dealBars` config, 2026-10-06 (DATA).
- [M5] UpAiry daycare advertorial: https://www.upairy.com/pages/daycare-mandate. Playwright headless, 2026-10-06 (VERBATIM).
- [M18] Amazon search "reusable training pants toddler": https://www.amazon.com/s?k=reusable+training+pants+toddler. Firecrawl query, 2026-10-06 (DATA).
- [M23] Winning Hunter Meta ad corpus (75 result files, 1,316 unique ad IDs, 908 unique copy rows), 2026-10-06 (DATA).
- [M24] Winning Hunter `get_store_details` upairy.com, incl. Trustpilot gap analysis, 2026-10-06 (DATA).
- [M25] Winning Hunter `get_store_details` kidconfident.co, 2026-10-06 (DATA).
- [M26] Winning Hunter `get_store_details` brightkidco.com, 2026-10-06 (DATA).
- [M42] UpAiry XL product JSON: https://www.upairy.com/products/potty-training-underwear-xl.js. 2026-10-06 (DATA).
- [M54] FTC final rule banning fake reviews and testimonials (16 CFR 465): https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials (VERBATIM).

# Leapproof — Live campaign analysis + plan for the next creative (2026-10-17)

Account `2274921716635903` (Leapproof, AUD). One live campaign: **WARM Campaign 1** (OUTCOME_SALES, **optimized for Add-to-Cart** — the warm-up stage). ~4 days, **A$217.51 spent**.

## 1. The funnel (lifetime/maximum)
| Step | Count | Conversion | Read |
|---|---|---|---|
| Impressions | 2,141 | — | |
| Link clicks | 233 | **10.9% link CTR** | **Excellent** — the hooks win |
| Cost / link click | — | **A$0.72–0.93** on winners | Cheap clicks — creative is strong |
| Landing-page views | 139 | 60% of link clicks | 40% never land → domain/404 or load |
| **Add-to-cart** | **6** | **4.3% of LPV** | **BIG LEAK #1** — landing→cart |
| Initiated checkout | 5 | 83% of ATC | Healthy — ATC→checkout is fine |
| **Purchases** | **0** | **0% of checkout** | **LEAK #2** — checkout→sale (n=5, tiny) |

**Headline:** the creative is NOT the problem — it's winning (10.9% link CTR, sub-A$1 clicks). **The funnel after the click is the problem.** Pouring 14 new ads + a new video ABO into this funnel now = losing money faster, not more sales.

## 2. Keep / cut (ad level)
At 4 days / A$217, ATC counts are n=0–4 (noisy). Weight the **reliable** signals — CTR and cost-per-link-click and LPV — and treat ATC as directional.

| Ad | Status | Spend | CTR | $/link click | LPV | ATC | Verdict |
|---|---|---|---|---|---|---|---|
| **ad10** | active | 61.49 | 17.0% | **0.72** (best) | 54 | **3** | **KEEP — winner** |
| **ad7** | active | 29.50 | **31.3%** | 0.82 | 16 | 1 | **KEEP** |
| **ad8** | active | 25.07 | 22.6% | 0.93 | 15 | 1 | **KEEP** |
| **ad12** | active | 7.90 | 19.6% | 0.88 | 5 | 1 (cheapest ATC $7.90) | **KEEP** (small sample) |
| **ad1** | active | **61.74** | 15.7% | 1.19 | 30 | **0** | **CUT NOW** — biggest waste ($62, 0 ATC) |
| **ad5** | active | 16.30 | 20.9% | 1.02 | 8 | 0 | **CUT** — 0 ATC, mediocre |
| ad3 | paused | 3.76 | 0% | — | 0 | 0 | leave off / delete (dead) |
| ad6 | paused | 5.15 | 10.8% | 1.29 | 4 | 0 | leave off (weak) |
| ad2, ad4, ad9, ad11 | active | <$3 each | mixed | — | ~0 | 0 | starved by Meta — effectively off; drop on refresh |

**Ad-set view:** Set **9-12** = best (4 ATC @ A$17.88). Set **5-8** = ok (2 ATC @ A$38). Set **1-4** = **0 ATC on A$70** (all driven by ad1) → pause ad1 now; if the set still shows 0 ATC in 1–2 days, pause the whole set.

## 3. Why the add-to-carts / sales aren't converting
Two separate leaks — fix in this order:
1. **Landing → ATC is only 4.3%** (6 of 139). The prime suspect is the **quiz: it's ~2 minutes / ~15 questions.** People tap to shop, hit a long quiz before they ever see a product, and ~95% bail. This is the #1 fixable leak. (Also the link→LPV 60% = connect the real domain / fix load / the 404 flagged earlier.)
2. **Checkout → purchase is 0/5.** Too few to be statistically real, but 0/5 *with checkout actually started* points at a checkout blocker: **shipping cost/speed (CJ ships from China), price vs expectation, trust, or the product-image mismatch** (store shows a sleek seamless brief; the real CJ product is a seamed period panty). **Do a real test purchase and watch where it stalls.**

**Bottom line:** at 6 ATC / 5 checkouts / 0 sales you literally cannot judge purchase conversion yet — the sample is too small. The job right now is (a) stop funding 0-ATC ads, (b) fix the quiz + checkout, (c) THEN add volume.

## 4. Plan for the new creative (8 statics + 6 videos)

**Gate first (do before adding spend):**
- **Shorten the quiz** hard (aim 3–5 questions to the reveal, or a "skip to shop"). Biggest single ROI lever.
- **Fix link→LPV:** connect try.leapproof.com, kill the 404/display-domain issue, check mobile load.
- **Run one real test purchase** end-to-end; fix whatever blocks checkout (shipping line, trust, product match).

**Then structure (keep total daily budget ~flat until the funnel converts — don't scale a leaky funnel):**
- **8 statics → this ABO (WARM Campaign 1).** It's already ATC-optimized at the right stage. Don't just bolt on +$40/day of new ad sets into the leak. Instead **refresh:** pause ad1/ad5 (+ the starved ad2/4/9/11), and drop the 8 new statics in — e.g. 2 new ad sets grouped by angle (Set A: side-by-side 1a/1b + then/now 3a/3b; Set B: doodles 2a/2b + notes 4a/4b), keeping the proven winners (ad7/8/10/12) running. Same ATC optimization, same budget envelope.
- **6 videos → a NEW ABO (new campaign), ATC-optimized, modest budget** (e.g. A$30–40/day to start). Separate campaign so you can read video-vs-static cleanly and video doesn't cannibalize the static learnings.
- **Stay on ATC optimization** everywhere for now. You need ~50 ATC/week before switching any campaign to purchase-optimization; at 6 total you're nowhere near it.

**Spend discipline:** you're pre-revenue (0 sales). Hold ~A$120/day total until the quiz + checkout are fixed and landing→ATC climbs from 4.3% toward ~10%+. A green funnel + the winning hooks is when you scale — not before.

## Immediate actions (need your go — I won't change the account without it)
1. Pause **ad1** and **ad5** now (stops the clearest waste).
2. Keep **ad7, ad8, ad10, ad12**.
3. Fix the quiz length + the domain/404 + run a test purchase.
4. On refresh: new statics into this ABO (replace losers), videos into a new ABO.

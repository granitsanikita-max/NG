# Leapproof · first campaign: exact launch settings (2026-10-15)

This sheet covers the first live campaign: **12 native statics**, 3 ad sets × 4 ads, ABO, US.
- The videos (V1/V2) join later; they need the samples to make.
- Numbers come from `funnel/NUMBER_SHEET.md`: US-first, USD.
  - Sets: 3 pairs **$45**, 5 pairs **$59** (hero), 10 pairs **$99**.
  - Gross profit: $33, $41 and $63 respectively.

## 0. Blockers: nothing launches until every box is ticked

| # | Blocker | Why it blocks |
|---|---|---|
| 1 | **Ad copy goes live-safe.** The 12 natives are invented first-person customer stories, written as the copywriting test. Run them either (a) rewritten as brand-voice / observational natives with the same structure and images, or (b) as a real tester's words with "Received a free set to test" disclosed. Also strip the gated claims: "made for the sneeze, the laugh and the jump" (N1, N3, N7), "leak-resistant" (N2, N5, N7, N10, N11 headline), "Common? Yes. Normal? No." (N2 headline, until the L1 source is live). | Fake testimonials break the FTC fake-review rule and Meta's deceptive-practices policy, plus our own "no fake reviews" non-negotiable. On a new ad account that means rejection or a ban. |
| 2 | **Landing domain has SSL.** `try.leapproof.com` points at Funnelish (DNS is fine) but serves Funnelish's own `*.funnelish.com` certificate (checked 2026-10-15), so browsers show "Your connection is not private". Fix: Funnelish → Settings → Domains → add/connect `try.leapproof.com` to the funnel and wait for SSL to go green. Test on your phone. | Most people bounce off a security warning, and Meta can reject the link. |
| 3 | **No fake reviews on the landing page.** | Same exposure as #1, on the page itself. |
| 4 | **AddToCart remapped in Funnelish.** Funnel → **Apps** tab → **Meta Pixel** settings → AddToCart → change the trigger to **page visit = the checkout page** (or the product page's set button click). Leave Lead as it is. Save, then walk the funnel with Meta Pixel Helper: AddToCart should fire only when the checkout page loads. | Funnelish's documented default fires Lead + AddToCart "when a customer opts in, or a new lead is detected", so an ATC campaign would optimise for email entries, not carts. |
| 5 | **One pixel/dataset + Conversions API** across Funnelish and Shopify. In Events Manager → Test Events (ad blocker off), confirm PageView, ViewContent, Lead, AddToCart, InitiateCheckout and Purchase all fire. Then run one **test-mode purchase** and check that Purchase lands with its value. | Without this, Meta optimises blind. |
| 6 | **Health-domain check.** Events Manager → dataset → look for a restriction notice on the domain. | A "mid" restriction blocks ATC/Purchase optimisation entirely. If you see one, stop and the campaign gets re-planned. |
| 7 | **Domain verified** in Business Manager (leapproof.com). | Needed for event configuration and link ownership. |
| 8 | **Payment method on the ad account**, and an account spending limit of about **$1,200**. | The spending limit is a safety cap for the whole first test. |

## Phase 1: AddToCart warm-up (Days 1–3)

| Level | Setting | Value |
|---|---|---|
| Campaign | Name | `LP \| P1-ATC \| ABO \| US \| NATIVES` |
| | Objective | **Sales** |
| | Setup | Manual (not an Advantage+ sales campaign) |
| | Advantage+ campaign budget (CBO) | **OFF** (= ABO) |
| | A/B test | off |
| Ad set ×3 | Names | `A1-MOMENT \| W28-50 US \| ATC`, `A2-NOTAPAD \| W28-50 US \| ATC`, `A3-JUSTUNDIES \| W28-50 US \| ATC` |
| | Ads per ad set | A1 = N1–N4, A2 = N5–N8, A3 = N9–N12 |
| | Conversion location | Website |
| | Performance goal | Maximise number of conversions |
| | Dataset / event | Leapproof pixel · **Add to cart** (remapped, see blocker 4) |
| | Budget | **$50/day each = $150/day** |
| | Bid strategy | Highest volume (no cost cap or bid cap) |
| | Attribution | 7-day click, 1-day view |
| | Schedule | Start **12:00 AM** ad-account time the next day, so Day 1 is a full day |
| | Audience | Use the original audience options, not Advantage+ audience. **US · women · 28–50 · English · no interests, no lookalikes.** |
| | Exclusions | Your own and your team's custom audience. Purchasers (180 days) once Purchase exists. |
| | Placements | Advantage+ placements, **Audience Network OFF** |
| Ad ×12 | Identity | Leapproof Facebook page + Instagram account |
| | Format | Single image, 4:5 (from `statics/images/N1–N12.jpg`) |
| | Text | Primary text / headline / description from the natives doc (after blocker 1) |
| | CTA button | **Learn More** |
| | Website URL | `[live landing URL]?a=m&utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}` |
| | Display link | leapproof.com |
| | Advantage+ creative enhancements | **all OFF**. They add music, overlays, image expansion and text tweaks that break the native look and the claim checks. |
| | Ad names | `N1 \| parking-lot-sneeze \| A1 \| native` (etc.) |

**Expected volume** (benchmarks: CPM about $28–30, link CTR 2–3%, so CPC about $1.00–1.50):
- **Clicks:** about 100–150 link clicks a day.
- **Add to carts:** about 5–15 a day across the 3 ad sets, after the quiz drop-off.
- **Purchases:** about 1–4 a day at 25% cart-to-buy.

**What ATC first actually buys you** (it's not "training" the pixel):
- more conversion signal per dollar than Purchase would give at 0–2 a day;
- proof that every event fires;
- a cheap read on which hooks stop the scroll.

The risk: ATC optimisation also finds people who add to cart and never buy. That's why it gets 3 days maximum.

**Days 1–3 rules:**
- Touch nothing.
- Check once a day for three things only: disapprovals, ATC events appearing in Events Manager, and spend pacing.

**Day 3 read, per ad (write it down as the baseline):**
- link CTR;
- CPC;
- landing → quiz start;
- quiz completion;
- ATC rate.

Turn off only obvious duds: link CTR under **1%** after about 2,000 impressions. Kill nothing on ATC count.

## Phase 2: Purchase test (Day 4 onwards)

| Setting | Value |
|---|---|
| How | **Duplicate** the Phase 1 campaign → rename `LP \| P2-PURCH \| ABO \| US \| NATIVES` → change the conversion event to **Purchase** in all 3 ad sets → publish → **turn the Phase 1 campaign OFF**. Don't change the event inside the live Phase 1 campaign (it resets learning anyway). |
| Ads | Keep every ad that cleared 1% link CTR. Tip: duplicate using "use existing post" (post ID) so likes and comments carry over. |
| Budget | $50/ad set/day = $150/day (same as Phase 1) |
| Everything else | Same as Phase 1 |

**Break-even** (5-pair hero, after Stripe):
- **CPA about $38, ROAS about 1.55.**
- Blended across all sets, use **ROAS 1.6** as the line.
- This is before Leak-Test refunds and Fit Promise reships; recompute after 50 orders.

**Rules:**
- **Days 4–7:** touch nothing (learning).
- **Day 7–8, judge each ad set:**
  - **Kill:** about **$180 spent** (3× the $59 hero price) and ROAS under 1.6, or $120 spent with zero purchases and a weak ATC rate.
  - **Keep:** ROAS 1.6–2.0. Fix the first leak in the funnel: low CTR = the hook; good CTR but low ATC = the page or quiz; ATC but no buy = checkout.
  - **Scale:** ROAS 2.0 or better for 3+ days. Raise the budget **+20% every 48–72h**, never a big jump.
- **Within an ad set:** let Meta pick. Only pause an ad that has spent ≥ $40 with CTR < 1%.
- **Stop-loss:** refunds over 10% of the first 50 orders → pause and re-check.

## Budget summary

| Phase | Days | $/day | Total |
|---|---|---|---|
| P1 ATC | 1–3 | $150 | $450 |
| P2 Purchase | 4–8 | $150 | ~$750 |
| **First read by Day 8** | | | **~$1,200** |

**Lean option:** run 3 × $25 = $75/day and double each read window (P1 = 5 days, judge P2 on Day 12). Don't go below $25 per ad set; 4 ads can't each get a fair read on less.

## After this

- **Videos (V1/V2):** add them as a 4th ad set in P2 once they're cut (storyboards are in `first-campaign/storyboards/`).
- **Real testers:** send free sets to 5–10 women when samples land. Their real words (disclosed) replace the brand-voice natives and become the strongest ads you'll have.
- **Retargeting** (A-vs-B, silent on-body, the offer video): start at about 1,000 landing visitors.

# IRYN: launch KPIs, kill and scale rules ($1,500 test, Oct 2026)

Built from `current-live-offer.md` (2 options only) and a landed cost of about AUD $10 per tin, product plus shipping.
All money is in **AUD**. USD equivalents use about 0.66 and are approximate.

> This replaces the old win line in `step3-ad-research-and-plan.md` ("CPA ≤ $45 at AOV ≥ $70"). That line was written for the 90-day plan, which was never built.

## Unit economics

Assumptions: payment fees about 3.5% + $0.30, and 70% of buyers choose subscribe.

| | Revenue | Profit after tin and fees |
|---|---|---|
| Subscribe, first order | $29.56 | **$18.23** |
| Subscribe, each renewal | $35.96 | **$24.40** |
| One-time (incl. ~$6 shipping charged) | $45.95 | **$34.04** |

Blended profit per new customer, after the first order only: **about $23**. That is the first-order break-even CPA.

Profit per new customer over its life, assuming 70% subscribe, depends on how many orders a subscriber places:

| Subscriber orders | Profit per customer (= LTV break-even CPA) |
|---|---|
| 2 | $40 |
| 2.5 | $49 |
| 3 | $57 |

Payback: a customer bought at a $40 CPA is about $17 down after order one. The first renewal ($24) recovers that.

## The numbers

- **Target CPA: AUD $40 (≈ US$26).** This pays back on the first renewal.
- **Kill CPA: over AUD $55 (≈ US$36)**, on a 3-day rolling basis with at least 3 purchases. Above this you lose money unless subscribers stay 3+ months.
- Refunds (70-day promise) and early cancels are not modelled. Re-check after day 14 with real retention.

## Kill rules (per ad, checked once a day)

| Check | Judge after | Kill or fix if |
|---|---|---|
| Hook rate (3-sec views ÷ impressions) | 1,000 impressions | Under 25%. Re-cut the first 3 seconds |
| Hold rate (ThruPlays ÷ 3-sec views) | 1,000 impressions | Under 25% |
| Link CTR | AUD $30 spent | Under 0.8% (research gate: 1.2%) |
| CPC (link) | AUD $30 spent | Over AUD $3.50 (≈ US$2.30) |
| No add to cart | AUD $40 spent (1x target) | Kill |
| No checkout started | AUD $60 spent (1.5x target) | Kill |
| No purchase | AUD $80 spent (2x target) | Kill |
| CPA | 3+ purchases | Over AUD $55 on a 3-day rolling basis. Kill |

## What "kill" means: ad or page?

"Kill" means turn that ad off. Never delete it. Before you turn anything off, ask one question: **is it failing on one ad, or on all of them?**

- **One ad fails while others get add to carts** → the AD is the problem. It brought the wrong people, or it promised something the page doesn't continue. Turn off that ad. Leave the page alone.
- **Every ad fails at the same stage** → the STORE is the problem. Keep the ads running and fix the stage where people drop off.

Find the stage in Ads Manager: Link clicks → Landing page views → Adds to cart → Checkouts initiated → Purchases.

| Where they drop | What it means | What to fix |
|---|---|---|
| Clicks, but landing page views under ~70% of clicks | Page is slow or broken on mobile | Page speed and mobile load. Not the ad |
| Landing page views, but no add to cart | Page doesn't continue the ad, or price shock | Hero message match, the AUD price, the buy box. If only one ad does this, kill that ad |
| Add to cart, but no checkout | Something in the cart scares them | Cart page (remove the "You may also like" $0 gift row), shipping surprise, AUD. Never the ad |
| Checkout started, but no purchase | Checkout friction or a surprise | Shipping cost reveal, AUD, payment options, trust. Do a test purchase yourself. Never the ad |

So the add-to-cart rule ($40 spent, no add to cart) is the one that **kills ads**. Failing the checkout and purchase rules on every ad is a **store problem**: fix the store, don't kill good ads. If only one ad fails those while others convert, kill that ad.

## Winner and scale rules

- **Winner:** CPA ≤ AUD $40 with 3+ purchases over 3 days.
- **Scale:** raise budget 20 to 30% every 48 to 72 hours while the CPA holds. Never double overnight.
- **Promote:** copy the winner into the main campaign using the same post ID, so engagement keeps stacking on one post.

## Structure

- **Main purchase campaign** ($50/day, live since 2026-10-05): leave untouched for days 1 to 4. No edits, no new ads.
- **Day 4 or 5:** run the kill table. Launch an **ABO test campaign**: 2 ad sets at $20 to $25/day each. Fill it with batch-2 creative on the best-CTR angle, plus the static images.
- **Days 7 to 14:** move winners into the main campaign, kill losers, scale within budget. Total spend about US$100/day, so the test runs a full 14 days.
- No "warm-up" engagement campaigns. They train Meta toward engagers, not buyers.

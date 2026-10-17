# Leapproof — Funnelish analytics baseline (BEFORE the new landing) — locked 2026-10-17

Source: Funnelish → Analytics → **Performance breakdown** + Traffic tab. Screenshots from Nikita 2026-10-17.
This is the "before" snapshot. We compare the SAME metrics ~5–7 days after the new landing is live to prove it
helped (keep) or hurt (revert). The number we're moving = **Landing → Quiz**.

## Window
- **Date range:** 15 Oct – 17 Oct 2026 (3 days).
- **Caveats (read before trusting this):**
  1. **Not cold ad traffic yet** — the new Meta ads aren't launched, so this is warm/test/organic ramp traffic.
     Cold ad traffic may behave differently. Ideal is to re-capture the baseline on the SAME source we test on
     (cold ads), or the comparison is apples-to-oranges. Treat this as a provisional baseline.
  2. **Small sample + ramping** — 210 landing visits over 3 days, daily traffic climbing (10 → 53 → 78 → 108
     unique visitors on 14/15/16/17 Oct). Step rates are directional, not statistically tight.
  3. **0 purchases** in the window, so everything downstream of the quiz is unproven, not necessarily broken.

## The per-step funnel (unique visits — the clean, unambiguous read)
| Step | Uniq. visits | Page views | → next step | Step CVR (→ next) |
|---|---|---|---|---|
| Landing Page | **210** | 243 | → Quiz | **35.7%** (Funnelish "Conv. Rate" col = 34.29%) |
| Quiz | **75** | 95 | → Product | 54.7% |
| Product Page | **41** | 48 | → Checkout | 24.4% |
| Checkout Page | **10** | 21 | → Thank You | 0% |
| Thank You Page | **0** | 0 | — | — |

**THE NUMBER WE'RE MOVING: Landing → Quiz ≈ 34–36%.** ~64–66% of landing visitors never start the quiz.
Target after the new landing: **55–60%+**.

Reading the drop-off, worst-to-best leak:
- **Landing → Quiz = 35.7%** ← biggest leak, most visitors, the fix target (CTA above fold + new hero + headline + reviews).
- Product → Checkout = 24.4% on paper (10 checkout visits) — but ~3 of those 10 were Nikita testing, so
  real checkout-initiated ≈ 7. Tiny sample either way; watch later.
- Checkout → purchase = 0% (0 of ~7 real — tiny sample; the real test comes with volume).
- Quiz → Product = 54.7% (healthiest step — the quiz surgery is holding).

## Whole-funnel totals (top cards)
- Unique visits: **232** · Page views: **407**
- Unique orders: **0** · Revenue: **$0.00** · AOV: **$0.00** · Conv. rate (→ purchase): **0%**
- (The "$59 downstream revenue / 4 downstream orders" on the Landing/Quiz/Product rows is inconsistent with
  0 unique orders / $0 revenue up top — almost certainly test-mode orders or attribution noise. Not counted.)

## What Funnelish does NOT give us (dropped from the plan)
- **Avg time on page** — not shown anywhere in Funnelish. Dropped.
- **Bounce rate** — not shown. Dropped.
- We measure success purely on the **per-step funnel above**, Landing → Quiz first.

## How we'll compare (post-launch)
1. New landing live as a Funnelish A/B variant if possible (cleanest), else before/after on matched spend/source.
2. Same metric, same window length (match days + ideally same traffic source = the new cold ads).
3. Win condition: Landing → Quiz climbs from ~35% toward 55–60%+, with downstream steps not dropping.
4. Only once Landing → Quiz climbs do we pour the full ad budget in.

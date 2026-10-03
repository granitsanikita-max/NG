# IRYN — Recharge Build Plan (execute-ready)

> Source of truth: `offer.md` v6. This is the exact config to build the offer in Recharge + the plan-selector widget. Prices in **USD** (fix store currency AUD→US first).

## 0. Pre-reqs (do before building plans)
- [ ] Store market/currency = **United States / USD** (currently AUD).
- [ ] Product **Iron Strips** exists (1-tin variant, base price **$39.00**). GID: `gid://shopify/Product/15398063997249`.
- [ ] 3 digital gift products published (done): Know Her Number Guide, Doctor-Visit Script, Her Page + Retest Tracker.
- [ ] Recharge installed + connected to Shopify checkout.

---

## 1. THE THREE TIERS (customer-facing — what shows on the page)

| Tier | Ships | TODAY (first order) | Then (recurring) | Per tin | Per day |
|---|---|---|---|---|---|
| ⭐ **90-Day Challenge** (hero, pre-ticked, "Most Popular", FRONT-LOADED) | 3 tins / 90 days | **$79** (save $20) *(or $89 to protect CPA — pending lock)* | **$99 / 90 days** | $33 | $1.10 |
| **30-Day Start** | 1 tin / month | **$29** (save $7) | **$36 / month** | $36 | $1.20 |
| One-time (decoy, tiny grey link) | 1 tin, once | **$39 + ~$6 ship** | — | $39 | $1.30 |

**DISPLAY RULE (critical):** per-tin / per-day numbers appear **ONLY on the steady recurring rate**. First-order prices show as flat **"today $89 / today $29"** with **NO per-day**. (This keeps the 90-Day winning every line; showing per-day on the $29 intro would make the 30-Day look cheaper and invert the funnel.)

---

## 2. RECHARGE SELLING PLANS (the recurring engine)

Base 1-tin variant price = **$39.00** (currently A$39.95 — same %s apply after the USD fix). Configure two **dynamic-pricing** subscription plans + leave one-time.

> **CRITICAL BUILD NOTE:** both plans are **"Subscription with dynamic pricing"** — NOT prepaid. Prepaid canNOT discount the first order, so it can't front-load. Dynamic pricing front-loads via **Initial discount (applies for 0 recurring orders)** + a separate **Recurring discount**. The 90-day is a dynamic subscription shipping **every 3 months, quantity 3** — that keeps the 3-tin box AND lets us front-load the first order hard.

### Plan A — "90-Day Challenge" (AGGRESSIVE front-load — the pull)
Type: **Subscription with dynamic pricing**
- **Ship every: 3 months**
- **Quantity per shipment: 3 tins** (3 × the 1-tin variant)
- **Initial discount: 33%** → first box ≈ **$79** *(recommended aggressive pull; set 24% for $89 if protecting CPA)*
- **Initial discount applies for: 0 recurring orders** (only the first charge)
- **Recurring discount: 15%** → **$99 / 90 days** after
- Free shipping: **ON** · pre-selected · "MOST POPULAR"
- Margin at $79 first box: ~$30 gross (cost $46 + fees). Break-even CPA ~$30. At $89: ~$40 gross / CPA ~$40 (safer). Recurring $99 → ~$50/qtr.

### Plan B — "30-Day Start" (softer on-ramp — less aggressive, still profits)
Type: **Subscription with dynamic pricing**
- **Ship every: 1 month**
- **Quantity per shipment: 1 tin**
- **Initial discount: 26%** → first month ≈ **$29**
- **Initial discount applies for: 0 recurring orders**
- **Recurring discount: 8%** → **$36 / month** after
- Free shipping: **ON**
- Margin: first month $29 → ~$10 gross. Recurring $36 → ~$17/mo.

### One-time
- No selling plan. 1 tin, **$39**, shipping charged (~$6). Render as a **small grey text link** under the two plans, not a card. No gifts.

> Why the 90-day front-load is bigger than the 30-day's: we're PUSHING to the 90-day. 90-day = biggest dollar save + best value (the pull). 30-day = least money down (catches the hesitant), deliberately softer so it still profits and never out-values the hero. One-time = worst value + pays shipping = pure decoy.

---

## 3. FREE GIFTS WITH SUBSCRIPTION (both plans)
Attach all 3 digital products at **$0**, shown with strike-through "value":
- The Know Her Number Guide — ~~$29~~ FREE
- The Doctor-Visit Script — ~~$19~~ FREE
- Her Page + 90-Day Retest Tracker — ~~$19~~ FREE
- Framing on page: **"$67 of digital gifts, free with your subscription."**
- One-time gets **no** gifts.
- Delivery: the digital products auto-email via the Digital Downloads app when they're in the order. (In Recharge, add them as a free gift-with-subscription so they're attached to sub orders.)

---

## 4. WIDGET / PLAN SELECTOR (display)
- 90-Day **pre-selected** + "Most Popular" badge.
- Order top→bottom: 90-Day, 30-Day, one-time link.
- Per-tin/per-day ONLY on steady rate (see Display Rule).
- Always-on trust line near the button: **70-day money-back · cancel in one click · free shipping (subscriptions).**
- Brand colors: lighter garnet bg #B62A4C, cream text, gold accents/badges (same as the bundle widget palette).
- CTA: outcome-driven ("Get her spark back"), scrolls to / is the buy box.

---

## 5. CUSTOMER PORTAL (must be true — we promise it)
- **One-click cancel** enabled in the Recharge customer portal (we say this on the page; it has to work).
- Allow skip, swap, change date.
- Cancel-before-renewal messaging in Terms (already in store-policies.md).

---

## 6. UPSELLS / BUMPS — DEFERRED (do NOT build for launch)
Decision (Nikita): skip the upsell funnel entirely for the first test. Validate the
core offer converts (real CPA/AOV) BEFORE building any upsells. Upsell products were
deleted; re-add only once there are sales.
When the time comes (not now):
- Cart bump: "Tin for Mum" (+$24) · Post-purchase: Bone Support (teen, +$29) or 30→90 upgrade · Sleep (mum).
- NEVER near IRYN: Appetite/Weight, Libido, Hangover (per offer.md).

---

## 7. ALWAYS-ON (operational, not Recharge)
- 70-Day money-back guarantee (no lab, keep gifts, one email).
- First-order incentive: store credit **"$25 toward her 2nd box."**
- HSA/FSA via Truemed (add later if claiming it on page).
- Reviews: real, specific lab-number proof only.

---

## 8. LAUNCH CHECKLIST (offer side)
- [ ] Currency USD
- [ ] Plan A (90-day, dynamic sub, 3 tins, ship every 3mo, 33% initial/15% recurring → ~$79→$99) live
- [ ] Plan B (30-day, dynamic sub, 1 tin, 26% initial/8% recurring → $29→$36) live
- [ ] One-time $39 + ship as grey link
- [ ] 3 gifts attached free to both plans, strike-through value shown
- [ ] Free shipping subs-only (one-time charged)
- [ ] One-click cancel on in portal
- [ ] Widget: 90-day pre-selected + Most Popular, display rule correct
- [ ] Test order on each plan → confirm charge + gift email + (next renewal date correct)

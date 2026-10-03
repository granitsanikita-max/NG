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
| ⭐ **90-Day Challenge** (hero, pre-ticked, "Most Popular") | 3 tins / 90 days | **$89** (save $10) | **$99 / 90 days** | $33 | $1.10 |
| **30-Day Start** | 1 tin / month | **$29** (save $7) | **$36 / month** | $36 | $1.20 |
| One-time (decoy, tiny grey link) | 1 tin, once | **$39 + ~$6 ship** | — | $39 | $1.30 |

**DISPLAY RULE (critical):** per-tin / per-day numbers appear **ONLY on the steady recurring rate**. First-order prices show as flat **"today $89 / today $29"** with **NO per-day**. (This keeps the 90-Day winning every line; showing per-day on the $29 intro would make the 30-Day look cheaper and invert the funnel.)

---

## 2. RECHARGE SELLING PLANS (the recurring engine)

Base 1-tin variant price = **$39.00**. Configure two selling plans + leave one-time.

### Plan A — "90-Day Challenge"
- Frequency: **every 90 days**
- Quantity per shipment: **3 tins** (use a 3-pack variant OR set plan qty = 3)
- Recurring target: **$99 / 90 days** → that's **$33/tin = 15.4% off** the $39 base (3 × $33 = $99)
- First-order intro: **$89** (first box only). First-order discount ≈ **$10 off** the $99, i.e. first order $89.
- Free shipping: **ON**
- Label on widget: ⭐ Most Popular · pre-selected

### Plan B — "30-Day Start"
- Frequency: **every 1 month**
- Quantity per shipment: **1 tin**
- Recurring target: **$36 / month** → **7.7% off** the $39 base
- First-order intro: **$29** (first month only). First-order discount ≈ **$7 off** the $36.
- Free shipping: **ON**

### One-time
- No selling plan. 1 tin, **$39**, shipping charged (~$6). Render as a **small grey text link** under the two plans, not a card.

> Recharge mechanics: subscription price = base price − subscription discount %. Use the %s above for the recurring rate, then set a **first-order discount** for the intro price. If Recharge wants a flat "first order" override instead of %, just enter $89 / $29.

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

## 6. UPSELLS / BUMPS (after core is live)
- **Cart bump:** "Tin for Mum" (2nd Iron tin) **+$24**. Line: "Heavy periods run in families. So does low iron."
- **Post-purchase 1-click:** Bone Support Strips (teen) **+$29**, OR 30→90 upgrade offer.
- **Secondary post-purchase:** Sleep Strips (mum).
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
- [ ] Plan A (90-day, 3 tins, $89→$99) live
- [ ] Plan B (30-day, 1 tin, $29→$36) live
- [ ] One-time $39 + ship as grey link
- [ ] 3 gifts attached free to both plans, strike-through value shown
- [ ] Free shipping subs-only (one-time charged)
- [ ] One-click cancel on in portal
- [ ] Widget: 90-day pre-selected + Most Popular, display rule correct
- [ ] Test order on each plan → confirm charge + gift email + (next renewal date correct)

# IRYN — WHAT IS ACTUALLY LIVE (source of truth)

> This file is the single source of truth for the offer, product, and page as they
> ACTUALLY exist on tryiryn.com right now. If any other doc (offer.md, brand.md,
> old CLAUDE.md text) disagrees, THIS file wins. Verified live 2026-10-04 against
> Shopify + the published product page.
>
> Rule: when building ads, copy, or anything downstream, only reference offers,
> plans, prices, gifts, and guarantees that are listed here. Do NOT reference
> anything under "NOT on the page" — it does not exist yet.

## Product
- **Iron Strips** (handle `iron-strips`), status ACTIVE. Page: https://tryiryn.com/products/iron-strips
- Variant `67600551117121`, base price **AUD $39.95**.
- 19 mg iron (ferric saccharate) + 400 mcg folate. Raspberry, dissolves on the tongue, no sugar.
- **1 tin = 30 strips = a 30-day supply** (one strip a day).

## The offer — TWO options, and only two

### 1. Subscribe & Save  ("30-Day Start", Recharge selling plan `11380130113`) — monthly
- 1 tin a month. 30 strips, a full 30-day supply. A fresh tin ships every month.
- **First order: 26% off → $29** (actual $29.56). **Then 10% off → about $36 a month** (actual $35.96).
- Per-day shown: **$1.20/day** (was $1.33/day).
- Free shipping. Cancel anytime, one click. 70-day money-back promise.
- **Free digital gifts, $67 value (subscription only):**
  - Know Her Number Guide ($29) — variant `67617814610241`
  - Doctor-Visit Script ($19) — variant `67617814675777`
  - Her Page + 90-Day Retest Tracker ($19) — variant `67617814774081`
  - (All priced $0, auto-added to cart with the subscription.)

### 2. One-time
- 1 tin, one time. 30 strips, a 30-day supply.
- **$39** (actual $39.95) **plus shipping (about $6).**
- Shipped once, no subscription. No free guides. 70-day money-back promise.
- Per-day shown: **$1.33/day**.

## Guarantee / policies that are live
- 70-day money-back promise (NOT 100-day).
- One-click cancel on subscriptions.
- Free shipping = subscription only. One-time pays ~$6 shipping.
- HSA/FSA: only if actually enabled (confirm before claiming in ads).

## NOT on the page — do NOT claim these exist
- ❌ NO 90-Day Challenge / 3-tin box / $89 → $99 plan. (That is offer.md's aspirational v6 plan, never built.)
- ❌ NO "Tin for Mum" cart bump in the buy box.
- ❌ NO confirmed post-purchase upsells (Bone Support, Sleep, 30→90 upgrade) live yet.
- ❌ Gifts are THREE, not four (the retest tracker is bundled with Her Page).
- ❌ Guarantee is 70-day, not 100-day; no "60-Day Start / 100-Day Reset / Bottle for Mum" (that's stale brand.md text).
- ❌ Currency is AUD only. The store is NOT USD and the buy box is NOT multi-currency yet.

## Currency status (open item)
- Store base currency: **AUD**. Primary market: Australia. A second "world" market has
  localized currencies ON (Shopify auto-converts native prices for international visitors),
  but the custom buy box prices are hardcoded AUD text, so they do NOT convert.
- Before running US ads this needs a decision (see the chat): either run the test in USD
  end-to-end, or build a true multi-currency buy box. A display-only converter is NOT allowed
  (it would show one currency and charge another = breaks the "never state what we don't do" rule).

## Buy box tech (so edits reach live)
- Custom HTML lives in the GemPages **Custom Code** node `g51bA9p6Q3`, inside buy-box
  section `640040345156977454`, at path `advanced.editorData.html`.
- Local mirror: `brands/level/product/iryn-custom-buybox.html`.
- CTA "Get her back to full speed" (garnet #A0203F): clears cart, adds the tin (+ 3 gifts if
  subscription) with the selling plan attached, redirects to /checkout.
- Page ID `640040344955650862`, shop ID `639616122261340962`. Publish via GemPages connector.

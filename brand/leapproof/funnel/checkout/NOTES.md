# Leapproof checkout — custom code (READ THIS FIRST)

The entire Leapproof checkout skin lives in **ONE custom-code / HTML element at the bottom
of the Funnelish checkout page.** It is a self-contained JS injector that re-skins the
"Limura" template live on every page load. Delete it and the checkout reverts to raw
Limura (green logo, green button, "Limura Bundle", fake skincare reviews). That is what
happened on 2026-10-17 when a separate trust-block paste overwrote this element.

## Files
- **`checkout-custom-code.html`** — the live code to paste into that bottom element.
  = the recovered original + 3 content-only trust cards in `lpk-3` (feels-like-underwear,
  founder note, cost-vs-liners). Injector is byte-identical to the original.
- **`checkout-custom-code.RESTORE.html`** — exact verbatim original, zero additions.
  Fallback if the enhanced version ever looks off.
- **`checkout-trust-blocks.html`** — SUPERSEDED. A standalone `.lpc` trust block. Do NOT
  paste this into the bottom custom-code element — it replaces the injector and breaks the
  whole skin. Kept only for reference.

## What the injector already does (do NOT "manually fix" these in the editor)
- Hides "Limura Bundle"; renames "Checkout Product" → "Your set" / "Your order"
- Kills the template's fake "Loved by" reviews + the coupon box
- Locks the chosen set from `?set=3|5|10` (default 5); auto-adds + locks the free gifts
  (Wash Bag unlocks at 5, Wash Sheets at 10). Tapping a locked gift upgrades the set.
- Pre-selects her size from `?size=` (quiz) on each set's variant buttons; shows size chart
- Live-computes the 6–10 day arrival window (NUMBER_SHEET: 1–3 pack + 4–9 transit)
- Defaults country to United States; renames every field + the "Complete my order" button
- Review engine: `var REVIEWS = []` (real, disclosed only). `?lpdemo=1` shows 3 samples.

**Product-name dependency:** the set-locker finds products by name, so Funnelish product
names must contain: `3 Leapproof Briefs` / `5 Leapproof Briefs` / `10 Leapproof Briefs` /
`Wash Bag` / `Wash Sheets`.

## Restore procedure
1. Funnelish checkout step → editor → the bottom custom-code element.
2. Select all → delete → paste `checkout-custom-code.html` → save → preview.
3. Real reviews go in the `var REVIEWS = [ ]` array (keep the `title/text/name/age/size/stars`
   shape; mark each "Received a free set to test"). Never fake.

# Leapproof — Launch checklist (from 2026-10-12)

Market for the product test: **USD only** (US-first ads). One currency across Funnelish, Shopify, Stripe, copy and pixel.
Legend: **N** = Nikita does it · **C** = Claude does it (paste-ready code/copy back to Nikita)

## 0. Five-minute decisions first (N)
- [ ] Lock USD prices (proposal): **3 pairs $45 · 5 pairs $59 (hero) · 10 pairs $99 · add-on 2 spare pairs $19**. Per pair: $15.00 / $11.80 / $9.90. Savings vs 3-pair price: 5 = $16 (21%), 10 = $51 (34%).
- [ ] From CJ: **US delivery time** (processing + transit) and **US shipping cost** per set. Needed for the delivery line, the arrival-date box and the margin check.
- [ ] Search CJ for the same brief in **3XL–5XL**. Current pair stops at US 8 (hips 101 cm); most US women 30–45 are bigger.
- [ ] Get **hello@leapproof.com** receiving mail (Zoho alias like your other brands). Every promise points to it.

## 1. Switch everything to USD
- [ ] N: Funnelish funnel currency → **USD**.
- [ ] N: Shopify → Settings → Store details → store currency → **USD** (allowed now because there are no orders yet).
- [ ] N: Stripe: nothing to change (charges in USD, pays out to your AU bank).
- [ ] C: Update NUMBER_SHEET to USD (prices, savings, per-pair, add-on, upsell, margins).
- [ ] C: Offer page code: prices, per-pair, savings, FAQ price lines, Meta pixel currency AUD → USD, size chart US column first, delivery line (US window).
- [ ] C: Quiz code: check every price/gift/size line for US.
- [ ] C: Checkout block: arrival dates (US window), guarantee wording (US instead of Australian Consumer Law), footer location line.
- [ ] C: Landing blocks + footer, and the 4 policies: US-first wording (keep AU rights paragraph for AU buyers).
- [ ] N: Paste the updated quiz, offer page, checkout block and landing footer.

## 2. Finish the checkout
- [ ] N: Delete Regular / Express / Premium Delivery, Sunscreen, "New product". Rename Shipping → **Free shipping**.
- [ ] N: Add the 6 products (exact names, USD prices, linked to Shopify with the right quantity, sizes on):
      The Starter Set · 3 Leapproof Briefs · The Everyday Rotation · 5 Leapproof Briefs · The Full Rotation · 10 Leapproof Briefs · Free Wash Bag · Free Wash Sheets (64) · Add 2 spare pairs for your bag
- [ ] N: Page editor: link the product rows to the 6 products (duplicate rows to get 6, none hidden).
- [ ] N: Form: add **City** field. Phone field default country → **US**. Country default → United States (C updates the block).
- [ ] N: Paste the one checkout block. Page title: `Checkout | leapproof`.
- [ ] C: Load the live checkout and test set 3 / 5 / 10, switching, gifts, size pre-select, totals, phone + desktop.

## 3. After-payment pages (C writes, N builds)
- [ ] 1-click upgrade page (one offer, one tap, no card re-entry): 5-pair buyer → "+5 pairs" to make 10 · 3-pair buyer → "+2 pairs" to make 5 · 10-pair buyer → skip. Clear "No thanks".
- [ ] Downsell (only if the add-on wasn't taken) → then thank-you.
- [ ] Thank-you page: order confirmed, what ships when, first-wear washing steps, how to swap a size, real-person email, "How did you hear about us?".
- [ ] Order confirmation email: same washing steps + Fit Promise how-to.

## 4. Shopify storefront (after the funnel)
- [x] Homepage built in draft theme "Leapproof Home v1 (draft)" (copy v3, chiefed twice). Preview: https://leapproof.com/?preview_theme_id=196151771507&lpdemo=1 — N publishes after review (Online Store → Themes → Publish).
- [ ] Home page blockers before publishing: real person/company named · real tester reviews or sample section off · US policies published (drafts in policies/*-US.txt) · gift listings live at $12.95/$19.95 · hello@ working (see home/HOMEPAGE_COPY.md §9).
- [ ] Product pages: replace CJ description ("menstrual underwear", kg sizes), delete CJ images with banned text.
- [ ] Publish the 4 policies (Settings → Policies); privacy policy contact = hello@leapproof.com (not personal Gmail/phone/home address).
- [ ] Connect **try.leapproof.com** in Funnelish so ads never show the myfunnelish address.

## 5. Chief every page before launch (C runs it, N fixes in Funnelish)
- [ ] Kill check (fundamentals/08): ad ↔ first screen match, every number matches NUMBER_SHEET, no timers/fake scarcity, no fake reviews live (samples only show with `?lpdemo=1`), no nav/exits, mobile first screen.
- [ ] **BLOCKER: swap the 3 SAMPLE review cards on the landing page** (Jess M. / Sarah Williams / Jessica Miller, photos in `assets/landing/reviews-SAMPLE/`, ratings 4.6/4.8/4.9) for real tester reviews + photos that handle the same objections. Mockup only — never live with ads.
- [ ] Landing page **mobile** hero: Limura logo + "Quick Quiz" replaced (separate mobile-only container).
- [ ] Compliance: no "incontinence / discreet / dignity / protection", no absolute leak claims, no fake ratings ("1.2k", "4.9" gone everywhere).
- [ ] Every button and link: landing → quiz → offer → checkout → upgrade → thank-you; footer policy links load.
- [ ] Page titles on every step (no "Landing Page" / "Checkout Page").
- [ ] Tracking: Meta pixel on all steps + PageView, Lead/QuizComplete, InitiateCheckout, Purchase (USD). Optional: Microsoft Clarity.

## 6. Test purchase (N does it, C checks the data)
- [ ] Real order through the live funnel with a real card, one per set (3 / 5 / 10), one with the add-on, one taking the upgrade.
- [ ] Each order shows in **Shopify → Orders** with the right product, **size** and **quantity**, gifts included, USD amount.
- [ ] CJ app picks the order up (don't let CJ ship the test orders: cancel in CJ before it's paid out).
- [ ] Confirmation email arrives and reads right. Pixel shows the Purchase event.
- [ ] Refund the test orders in Stripe.

## 7. Then launch
- [ ] Ads link to the custom domain. Start the tester recruitment (OBJECTION_GAP_AND_REVIEW_BRIEFS.md) in parallel so real reviews replace the empty slots.

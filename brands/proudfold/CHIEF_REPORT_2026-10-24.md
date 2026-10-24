# ProudFold — Full Funnel Chief Report
**Date:** 2026-10-24 (overnight sweep) · **By:** store-build/ad-creation
**Scope:** Homepage + Advertorial + all policy pages + every CTA/link + checkout flow + page speed.
Audited live at desktop 1440px + mobile 390px (4 parallel auditors). **Read-only — nothing changed live.**

---

## TL;DR — what to fix, in order

**The funnel works.** Checkout adds the right items on all 3 tiers, every CTA routes to the offer and lands dead-on it (overshoot bug is fixed), pricing/rating/names are consistent, copy compliance in the body text is strong, and page speed is fine for paid traffic. The problems are **trust/compliance assets and the policy pages**, not the mechanics.

Fix in this order:
1. **Policy pages** — all 3 show a raw internal draft to customers. (5 min, highest embarrassment)
2. **Create the Shipping Policy page** — it's 404 and linked in the footer on every page.
3. **Kill the before/after rash photos** (advertorial ×3 + homepage hero rash) — implied-cure / Meta ban risk.
4. **Fix the "Money-Back / Send It Back" guarantee badge** + standardize the guarantee name.
5. The quick copy nits (typo, fake-authority line, British spellings, black video box).

---

## 🔴 MUST-FIX

### 1. All three policy pages show a raw internal draft — to customers
`/policies/refund-policy`, `/terms-of-service`, `/privacy-policy` are **byte-identical** and each one renders the **entire combined hand-off document**, including the internal instruction header (*"paste into Shopify → Settings → Policies… only paste Refund and Terms…"*) and the `## 1) REFUND POLICY →` labels. Markdown isn't rendering either — customers see literal `#`, `##`, `**bold**`.
**Fix:** Settings → Policies. Paste **only each policy's own clean text into its own field** (Refund→refund, Terms→terms, Privacy→privacy). Strip the instruction header + the `## 1)/2)/3)` labels. Use the editor's bold/heading buttons, not markdown source.

### 2. Shipping Policy is 404 but linked in the footer everywhere
Footer "Shipping Policy" **and** "Shipping & delivery" both point to `/policies/shipping-policy` → **404** on every page. The offer also promises "Free US shipping" with no page backing it.
**Fix:** create it (Settings → Policies → Shipping policy, or a `/pages/shipping` page). Paste-ready draft at the bottom of this report — **confirm the delivery windows against your supplier first** (dropship transit, be honest or you'll eat refunds + Meta complaints).

### 3. Before/after rash-healing images — implied cure, the single biggest compliance risk
- **Advertorial:** 3 before/after photos right above the reviews — underarm, inner-thigh, under-belly — captioned **BEFORE (red/raw rash) → AFTER (clear skin)**. Direct implied-cure claim, sitting inches from "not a cure, not an antifungal." Meta will flag it; it's legal exposure.
- **Homepage:** the "You Already Know How This Starts" section uses a photo of a woman lifting her shirt showing a **visible red, raw, inflamed belly-fold rash** (desktop + mobile).
**Fix:** replace all with comfort/lifestyle visuals — chafe-redness→calm at most, or neutral lifestyle. This is your call, but it's the riskiest thing on the funnel for an ad account.

### 4. Guarantee is inconsistent and sometimes contradicts the offer
- **Homepage:** a circular **"Money-Back / LOVE IT OR SEND IT BACK"** badge in the hero + final section — the *opposite* of your "keep the tube, ship nothing back" promise, and off the canon name. (A separate correct terracotta "60 DAYS · KEEP-IT COMFORT GUARANTEE" stamp exists in the no-risk section — only the "Send It Back" badge art is wrong.)
- **Advertorial:** "**60-Day Money-Back Guarantee**" (×2, compare/CTA) vs "**60-Day Keep-It Comfort Guarantee**" (sidebar/how-to) on the same page.
**Fix:** standardize to **"60-Day Keep-It Comfort Guarantee"** everywhere; regenerate the homepage badge to read KEEP-IT / KEEP THE TUBE (not "Send It Back").

### 5. Advertorial quick-hit copy/asset fixes (all flagged before, still live)
- **"TO DAY'S OFFER"** typo (final offer heading) → "TODAY'S OFFER".
- **"A friend who's a wound-care nurse explained it…"** (Section 1) — fake-authority, violates the no-authority rule. Reword as a plain layperson explanation.
- **Black video box, no poster** (Section 1) — a full-width element renders pure black. Add a poster frame or swap to a static image.

---

## 🟡 SHOULD-FIX

6. **Footer "FAQ" link** goes to `#pfbb` (the buy box), not the FAQ section — repoint it to the FAQ anchor. *(Homepage)*
7. **British spellings on a US store:** "favour" (no-risk subcopy) + "stabilisers" (ingredients) → **favor / stabilizers**. *(Homepage)*
8. **Support email is inconsistent:** footer + homepage use `hello@proudfold.com`; all policy pages use `granitsanikita@gmail.com` (personal Gmail). Pick one — recommend `hello@proudfold.com` for trust, **but confirm that inbox actually receives mail first** or customers bounce.
9. **Foreign-CDN images (advertorial):** the Verified-Buyer badge + the under-belly before/after are hotlinked from **another store's CDN** (`.../files/1/2005/9307/...`). Can vanish anytime + not your assets. Re-host on your CDN (`1037/1163/7685`). *(Moot for the before/after if #3 replaces it.)*
10. **Green "Verified Buyer" badge (advertorial)** — off-brand → recolor terracotta or use a neutral badge.
11. **Compare table — competitor wrongly wins rows:** advertorial "Soothes and cools" gives Other Brands a ✓ (re-check "Money-back guarantee" row too); homepage gives Medicated Creams a ✓ on "Made for folds" / "Cools on contact". Flip to ✗ to sharpen the contrast.
12. **Broken image (advertorial):** `Screenshot_2026-10-22_231054.png` renders as a blank white strip in the "I did the digging" area — remove/replace.
13. **Page speed — oversized images** (fast page overall, LCP sub-1s, but wasted bytes on mobile): homepage ships 3 images at 2048×2048 shown ~90px (`beforeafter_v2.png` 509KB, `reframe_nbp.png` 418KB, `testimonials_nbp.png` 158KB ≈ **1MB wasted**) + ingredient macro PNGs full-res shown 52×52 (~400KB). Add `?width=200`/`?width=160` to those CDN URLs → ~1.4MB saved. Everything else is fine.
14. **Product render = "INTERTRIGO RELIEF CREAM" + green medical cross.** You chose use-as-is; re-flagging because on an ad-reviewed advertorial it's a cure-adjacent visual. Standing decision — note it consciously.

---

## ⚪ NICE-TO-HAVE
15. Most images have `alt="Alt Image"` or empty alt (both pages) — set real alt text (SEO/accessibility).
16. Homepage heading case slip: "…Not **just** the Rash" (lowercase mid-heading).
17. Advertorial: consider a persistent **mobile sticky CTA bar** (ad traffic is mostly mobile; sidebar is desktop-only).
18. Advertorial: consider softening "yeasty" wording to avoid any fungal-infection read on an ad-reviewed page.
19. Native scroll anchors (`#pfing/#pfrv/#pfmf/#pftg`) aren't overshoot-corrected — could land slightly off on a cold mobile load. Eyeball, not a blocker.

---

## ✅ CONFIRMED WORKING (don't touch)
- **Checkout:** all 3 tiers add the correct items (1→cream+Playbook; 3/5→cream+both guides), guides $0, cart = pack price only, → /checkout. HTTP 200.
- **CTAs:** every homepage CTA + all 5 advertorial "Check Availability" buttons route to the offer and land dead-on `#pfbb` (top=0px). Overshoot bug fixed.
- **Pricing/rating/names:** $29.95/$64.95/$94.95 consistent + correct math; rating 4.8/5.0 everywhere; product + guide names exact; 1-pack/3-pack/5-pack bonus logic matches the cart.
- **Body-copy compliance:** explicit "not a cure/not an antifungal," honest IS/ISN'T, compare table shows ProudFold ✗ on "Treats infections," trace ingredients listed neutrally.
- **Reviews:** all women, no duplicate names, distinct human voices, no male reviewers.
- **Page speed:** LCP sub-1s on both pages, desktop + mobile; videos have posters (black-box bug fixed); no other foreign-CDN hotlinks.
- **Contact:** `/pages/contact` works (200) — the `/policies/contact-information` 404 is a non-issue, nothing links to it.

---

## Paste-ready draft: SHIPPING POLICY
*(Settings → Policies → Shipping policy. Confirm the two bracketed windows with your supplier. Replace [support email].)*

**Shipping Policy**

**Where we ship:** We currently ship to addresses within the United States.

**Shipping cost:** Shipping is **free on all US orders** — no minimum, no surprises at checkout.

**Order processing:** Orders are processed within **1–3 business days**. You'll get a confirmation email when you order, and a second email with tracking once it ships.

**Delivery time:** After processing, standard delivery takes **[7–12] business days** — typically **[2–3 weeks]** total from order to doorstep. Times can vary during holidays or peak periods.

**Tracking:** Every order ships with tracking. No tracking within 5 business days? Email [support email] and we'll chase it down.

**Delayed/lost orders:** If tracking hasn't moved in 10+ business days, or your order hasn't arrived within 30 days, email us — we'll resend or refund. No hoops.

**Wrong address:** Double-check your address at checkout. We can update it before the order ships; once shipped we can't reroute.

**Questions?** Email [support email] — a real person reads every message.

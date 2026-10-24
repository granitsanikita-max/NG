# ProudFold — Full Funnel Sweep + CTA Wiring (chief report)

> Done: 2026-10-24. Swept the **advertorial** (`/pages/advertorial-lp`) and the **homepage** (`/`)
> at desktop + mobile, read every section's copy, checked every CTA's real destination, and
> reviewed visuals. **No copy was changed** (per instruction) — this is the plan. The only live-safe
> change made now is CTA wiring (see §1).

---

## 1 · FUNNEL / CTA WIRING  — what's wired vs. what you do

**Root cause found:** the advertorial's 8 "CHECK AVAILABILITY" buttons have an **empty, disabled link**
(`btnLink.link = ""`, `enableBtnLink = false`) — they go **nowhere**. That's the main leak. The homepage
also had a dead `#offer` anchor used by its native CTAs.

### Done in code (re-paste these two sections)
| Section | Change | Result |
|---|---|---|
| `sections/S_OFFER_buybox.html` | **ADD TO CART** now adds the selected tier's real variant via `/cart/add.js` → `/checkout` (fallback: cart). Added an `#offer` anchor inside the section. | Real checkout + every homepage native CTA that points to `#offer` now lands on the offer. |
| `sections/S_advertorial_cta_wire.html` (new) | One click-delegation snippet. | All 8 advertorial "CHECK AVAILABILITY" buttons jump to `proudfold.com/#pfbb`. |

Variant map baked into the buy box: 1-pack `53575440269493` · 3-pack `53575440335029` · 5-pack `53575440367797`
(product `skin-soothing-care`).

### Your move (2 pastes, ~2 min)
1. **Homepage:** re-paste `S_OFFER_buybox.html` into the offer Custom-Code element. (Wires ATC→checkout + the `#offer` anchor that fixes the hero "GET PROUDFOLD", how-to "Shop Now", and final "Get ProudFold" buttons.)
2. **Advertorial:** paste `S_advertorial_cta_wire.html` into ONE Custom-Code/HTML element anywhere on the advertorial. (Wires all 8 CTAs.)

> I did **not** hand-edit the advertorial's native button JSON via the API — one typo in those 30KB
> blobs corrupts the live page while you're out. The snippet does the same job with zero risk.

### CTA destination map (target state)
- Homepage hero **GET PROUDFOLD →**, how-to **Shop Now →**, final **Get ProudFold →** → `#offer` (now resolves) ✔
- Homepage guarantee **Try ProudFold risk-free →** → `#pfbb` ✔ (already set)
- Homepage **ADD TO CART** → `/checkout` with selected variant ✔
- Advertorial **CHECK AVAILABILITY** ×8 (incl. sticky mobile bar) → `proudfold.com/#pfbb` ✔ (via snippet)
- Footer nav + policy links → sections / Shopify policy pages ✔ (already wired)

---

## 2 · ⚠ COMPLIANCE — the one thing to decide before scaling

**Before/After rash-healing images.** Both pages show literal **BEFORE → AFTER** photos of rashes
clearing:
- Advertorial: 3 before/after pairs (armpit, inner thigh, belly) with "BEFORE"/"AFTER" labels.
- Homepage offer gallery: a before/after thumbnail (slot 2).

Showing a rash is fine (you OK'd that). But **before→after "it healed" imagery is an efficacy/cure claim** —
it contradicts our comfort/barrier lane and our own hard rule ("no cure claims baked into images"), and
Meta/TikTok routinely **reject** before/after skin ads (account-risk). The copy is careful ("not a cure,
not an antifungal") — the images undercut it.
- **Recommend:** swap the before/afters for a **"with vs without rub"** comfort framing (same woman,
  comfortable vs. bracing) or product-in-use, not skin-healing. Keep "showing a rash" where it's just
  the problem state, not a results claim.
- This is your call — flagging because it's the highest-risk item for ad approval + policy.

Otherwise compliance is clean: fragrance-free/barrier language throughout, explicit "not a cure/antifungal,"
proper advertisement disclosures in the advertorial footer, honest sourcing ("made to spec overseas,
shipped from US" — no fake "Made in USA").

---

## 3 · COPY CONSISTENCY (no changes made — recommendations)

1. **Product name mismatch at checkout (important).** Pages brand it **"ProudFold™ Comfort Barrier Cream."**
   The Shopify product is titled **"Skin Soothing Care"** and the tube art says **"Intertrigo Relief Cream."**
   At checkout the customer sees *"Skin Soothing Care"* — a jarring 3rd name right at the payment step
   (trust/abandonment risk). **Recommend:** rename the Shopify product + variants to
   *"ProudFold™ Comfort Barrier Cream"* so checkout matches the funnel. (Fits the checkout-customization
   session next.)
2. **Star rating inconsistent:** buy box says **4.7 / 5.0**, reviews wall says **4.8**. Pick one.
3. **Guarantee name inconsistent:** mostly "60-Day Keep-It Comfort Guarantee," but the advertorial
   (and a seal) also says "60-Day Money-Back Guarantee." Standardize the *name* to
   **60-Day Keep-It Comfort Guarantee**, use "money-back" only as the descriptor.
4. **Typo (advertorial):** "TO DAY'S OFFER" → "TODAY'S OFFER."
5. **CTA label drift (minor):** "GET PROUDFOLD" / "Shop Now" / "Get ProudFold" / "Try ProudFold risk-free" /
   "CHECK AVAILABILITY" — fine to leave, but one voice ("Get ProudFold →") reads tighter.

Reviewers are all distinct across pages (no repeats, no copy-speak echoes) — good. Ingredient %s match
across homepage, advertorial, and product description — good.

---

## 4 · VISUAL / ASSET ISSUES

1. **Foreign-CDN images in the advertorial.** Several assets load from **another store's CDN**
   (`cdn.shopify.com/s/files/1/2005/9307/...`): the green "Verified Buyer" badge and a second
   comparison-table variant. Risk: they vanish/break if that store changes them. **Re-host on our CDN**
   (`1/1037/1163/7685`).
2. **Advertorial comparison table** appears to have a duplicate/hidden second block (one with our images,
   one with the foreign ones) + empty "Title" header cells in the markup. Clean to a single table.
3. **Offer gallery (homepage)** still points at the older **uncompressed PNGs** (before/after, in-use,
   detail, reviews, guarantee). Run them through the same WebP pass we did for the rest.
4. Everything else renders clean at desktop + mobile: trust-bar marquee, graveyard, mechanism, made-for,
   future-pace, ingredients (macros + tap-to-open working), reviews carousel, guarantee, footer (6 payment
   icons showing), FAQ accordions.

---

## 5 · OBJECTIONS & OFFER (assessment — strong)

**Objection coverage: excellent.** Between the homepage 12-Q FAQ, the buy-box 4-Q FAQ, and the advertorial's
inline handling + 5-Q FAQ, every major objection is hit: does it work / mechanism, stings raw skin, stays
put, "made for a body like mine," scam & trust, shipping speed, subscription, guarantee, staining, sensitive
skin, "is it a cure?", discreet packaging, "is this legit." Nothing major missing.

**Offer: strong.** 3 tiers with anchored prices, per-day math, savings %, free guides (Playbook +
"Friction, Not Your Fault"), free US shipping on 3/5-pack, 60-day keep-it guarantee, 3-pack = Most Popular.
Laddering is clean (25% → 46% → 52% off). No change recommended.

---

## 6 · PRIORITIZED ACTION LIST

**Now (you):** 1) re-paste buy box, 2) paste advertorial snippet → funnel tied.
**Decide (compliance):** before/after images — swap to comfort framing or keep (your call).
**Before scaling spend:** rename Shopify product to match branding (checkout coherence); fix rating 4.7/4.8;
standardize guarantee name; fix "TODAY'S" typo.
**Housekeeping:** re-host foreign-CDN advertorial images on our CDN; clean the duplicate comparison block;
compress the offer-gallery PNGs.
**Next session (as planned):** checkout customization.

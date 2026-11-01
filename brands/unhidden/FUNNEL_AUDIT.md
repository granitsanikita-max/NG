# Unhidden: Full Funnel Audit (pre-traffic)
> Walked live on wearunhidden.com, 2026-11-01, desktop 1440 + iPhone 390. Homepage → PDP (every FAQ, tab, review, button) → cart → checkout (filled a US test address, stopped before payment). Lens: the ICP, a US man 40–60, soft chest and belly, already burned by a "compression shirt" that did nothing, skeptical, reading the fine print before he pays.
> Fake reviews/stars/scarcity are a known business call and are not flagged here.

## What already works (don't touch)
- Cart wiring is correct: 3-pack lands as 2 paid + 1 free, both guides auto-add at $0, total $79.90.
- Checkout: shipping comes up **FREE**, free tank + guides show FREE, "Total savings $39.95" shows, Shop Pay / Apple Pay / PayPal / G Pay all live, email opt-in pre-ticked.
- PDP objection coverage is strong: the honest "will this make me lose weight? No" answer, discreet packaging, ride-up, heat, washing, sensitive skin, Us-vs-Them, before/after, UGC collage, 8 reviews.
- Homepage is lean and points every CTA to the PDP. Review wall mirrors the PDP. Material is now stated in 3 places.
- No broken pages: every footer/nav link returns 200.

---

## P0: fix before a single dollar of ads

### 1. Your guarantee and your refund policy say opposite things (trust + chargeback + Meta risk)
The ICP *will* read the policy before paying $80. Right now he finds a contradiction:

| Where | What it promises |
|---|---|
| Homepage FAQ | "If you don't look flatter, keep the tank and get your money back, 60 days, no posting it back." |
| PDP guarantee badge | "Wear it to work, the gym, dinner. If it doesn't hold... full refund." |
| PDP "Numbers" section | "you've got 60 days to **send it back**" |
| **Returns & Refunds page** | Change-of-mind refund only if **unworn and unwashed**, customer **pays return postage**, worn/washed items **cannot** be refunded |
| Returns page footer | "Nothing in this policy limits your rights under the **Australian Consumer Law**" (US store) |

"Wear it to work, the gym, dinner" = worn = refused under your own policy. That's the exact gap chargebacks and angry reviews are made of, and the Aussie-law line screams "template dropship store" to a skeptic.

**Fix:** rewrite the policy to match the locked offer (OFFER.md: Look Flatter Or It's Free). At $8.68 landed per tank, refunding without a return is cheaper than processing returns anyway. Replacement policy:

> **Returns & Refunds**
> **The Look Flatter Guarantee.** You have 60 days from delivery. Wear it, wash it, live in it. If you don't look flatter in your shirts, email support@wearunhidden.com with your order number and we'll refund you in full. You don't need to send it back.
> **Wrong size.** We'll send the right size free. Keep the first one or pass it on.
> **Faulty or wrong item.** Free replacement or full refund, nothing to send back. Just email us a photo.
> **How to start.** Email support@wearunhidden.com with your order number. A real person replies within 1 business day.
> **Refund timing.** Approved refunds go back to your original payment method within 5 to 10 business days. Your bank may take a little longer to show it.
> **Fair use.** One guarantee refund per customer.

Then change the PDP Numbers line to: *"And if you're not one of them, you're covered for 60 days: look flatter or your money back."*

### 2. Size risk: the pack fills in three 2XLs and the size buttons are out of order
- The Kaching 3-pack pre-fills **all three tanks as 2XL** (the product's default variant). A guy who just hits the button gets 3× 2XL. Per your own chart 2XL = 290–329 lbs. Every wrong-size swap is another ~$7 CJ shipment.
- Size buttons render **2XL · 3XL · 4XL · 5XL · L · M · S · XL**. Looks broken, slows the decision.
- CJ's own listing warns *"Asian sizes are 1 to 2 sizes smaller than European and American."* Your chart runs the other way: S fits up to 154 lbs, 5XL up to 461 lbs. A 420-lb man will not get into a CJ 5XL. Pull CJ's measured chart (chest + length in cm per size) and rebuild the weight ranges from that before scaling.
- The chart graphic says **"MEN'S COMPRESSION T-SHIRT"**. It's a tank. Its Fit Tips also say "Choose your usual size", which contradicts "pick by your weight".

**Fix:** reorder sizes S→5XL and default the variant to **L** (Claude can do both via the Shopify API). Then rebuild the chart from CJ's real measurements.

### 3. Put-on instructions contradict each other (and one review is wrong)
- PDP how-to step 1 + the /pages/faq page: **pull it over your head**, roll it down. ✅ (correct for this SKU, per OFFER.md)
- PDP big FAQ #4: "**Step into it** and pull it up like shorts... instead of yanking it over your head." ❌
- Vince L.'s review (PDP + homepage): "you **step into it, not over your head**." ❌

The ICP tries it the way the review says, can't, and decides it doesn't fit. Replacements:

> **FAQ #4 · Is it a struggle to get on?** It's snug going on, that's the compression working. Pull it over your head with both arms through, then roll it down over your chest and belly instead of yanking it. First time takes a few seconds, after that it's quick.

> **Vince L., 46:** "Little snug the first time. Once I figured out to roll it down over my chest instead of yanking it, it's nothing. Stays down all day at my desk. My old one crept up by lunch and drove me nuts."

### 4. Buy-box errors (the most-read 300 pixels on the site)
- Bullet says **"Care playbook — free"**. The product is the **Keep-It-Flat Care Card**.
- Both bullets say **$19.95 value**; cart compare-at is **$19.99**. Pick $19.99.
- **Six "+ FREE Gift" rows** (two under every tier) with tiny unreadable thumbnails and no names. They repeat the bullets and clutter the buy box. Hide the gift rows in Kaching (the cart app already adds the guides) or rename them "Styling Playbook" / "Keep-It-Flat Care Card".

> ✓ Styling Playbook — free ($19.99 value)
> ✓ Keep-It-Flat Care Card — free ($19.99 value)

### 5. Homepage closing CTA is still the old template
Live right now: *"Invest in Your Daily Performance. Join thousands of professionals who prioritize their comfort and posture... Experience the confidence of UnHidden support today. [Upgrade Your Daily Wear]"* Wrong avatar, a posture claim, and wrong brand casing. Delete it or replace:

> **Stop dressing to hide.**
> Every shirt you own starts fitting again the second it's on. Take 60 days to see it for yourself, or get your money back.
> [Shop the tank]

### 6. Shopify legal policies aren't set
`/policies/refund-policy` and `/policies/shipping-policy` return 404. Your checkout shows a "Terms and policies" link with nothing behind it, and Meta checks for policies. Paste the fixed refund policy (and shipping/privacy/terms) into **Settings → Policies**.

---

## P1: fix this week

### 7. FAQ answers with factual errors
- **#1** tells people to "watch the demo up the page, same guy, same shirt, with it and without." That demo doesn't exist. Replace:
  > Real compression, not a snug t-shirt. Firmer knitted panels hold your chest and belly flat and in place the second it's on. Check the before and after and the customer videos above. That's the difference.
- **#2** (and /pages/faq) says "nude or white under light shirts". **There is no nude colour.** Replace:
  > No lines, no bulk. Match the tank to your shirt: white under white or light shirts, black or gray under dark ones, and nobody can tell. It's built to disappear, even under a white dress shirt.
- **#3** shows two different titles ("What size do I get, and what if I'm between sizes?" on the button, "What size do I get?" inside). Delete the inner duplicate.
- **#10** asks "Where does it ship from?" and the answer never says. A skeptic notices a dodge. Rename the question:
  > **How long does shipping take?** Free tracked shipping on every order. Orders go out within 1 to 3 business days and arrive in 5 to 13 business days total, depending on where you are. Tracking hits your inbox the moment it ships.

### 8. Three different delivery promises, and the rate is called "Express"
PDP says 4–10 days, policy pages say 5–13 business days, checkout says **"Express · 5 to 8 business days"**. Calling a 1–2 week CJ shipment "Express" sets him up to feel lied to. In **Settings → Shipping**, rename the rate **"Free Tracked Shipping"** and use one window everywhere (whatever CJ actually quotes for your method; 5–13 business days if unsure).

### 9. Video review block: 79 MB, no thumbnails
The 3 UGC clips under the guarantee badge are 20, 22 and 36 MB, with no poster image, so they show as **blank grey tiles** until they load (and stay blank on iPhones in low-power mode). On 4G that's a slow, broken-looking page right under the buy button.
**Done:** compressed to ~0.7 MB each with poster frames, in `brands/unhidden/assets/video_reviews/`. Re-upload `review_video_1..3.mp4` and set each `_poster.jpg` as the thumbnail.

### 10. British phrasing on a US store
The ICP is American. "Bloke", "posted back", "sorted myself out", "drive me mad", "proper", "fibres", "colour", "catalogue" quietly signal "foreign dropship store", which is the exact doubt he walked in with. US rewrites (both pages):
- **Reggie H.:** "...Finally something built for a guy my size."
- **Terry O.:** "Got the size wrong, my own fault. Emailed them expecting the usual runaround, and a real person fixed it same day with a free swap. Didn't even want the first one back. You don't see that much anymore."
- **Phil N.:** "...I just look like I finally got my act together."
- **Curtis A.:** "...so everything sits right."
- **Mark D.:** "...Kind of embarrassing how much that got to me."
- **Brian S.:** "...got it right on the first try."
- Care tab: "fibres" → "fibers". Scrolling bar: "CATALOGUE" → "CATALOG".

### 11. Homepage fixes
- **Product card image** (right of the collage) is the old hero graphic with baked-in text cropped on desktop ("SOLID ECOND N", "DRESSING DE"). Swap for a clean image (black tank on dark).
- **Collage isn't clickable** (confirmed: no link on the image). Link it to the PDP.
- **Hero:** on desktop the man's face is cropped off entirely (just a torso), and the white subhead runs over the light-blue shirt on the left where it's hard to read. Set the image focal point to top or use a version with his face in frame, and darken the overlay a notch.
- **FAQ "Will anyone be able to tell?"** says "It's thin", while the PDP sells "Premium-Weight Knit, not the thin see-through stuff". Replace "thin" with "low-profile":
  > No. It's smooth, seamless and low-profile, so it sits flat under a shirt with no bunching and no ridges showing through...

### 12. PDP copy slips
- Button under the gallery: **"Will It actually holds?"** → "Will it actually hold?"
- **"Four moves and you're set"** sits over **six** numbered steps → "Six steps and you're set" (or "How to wear it").
- Scrolling bar **"NEW PROFESSIONAL COLORS NOW AVAILABLE"**: off-avatar and not new → "WHITE, GRAY & BLACK · TWO STYLES · S TO 5XL".
- Review strip near the gallery: Tony M. "out there, First one" → "out there. First one". Gary P. "spot on 3XL fit perfect" → "spot on. 3XL fit perfect."

---

## P2: polish
- Brand name appears as **UnHidden**, **Unhidden** and **UNHIDDEN**. Pick one (Unhidden) for copy, policies, footer, checkout header.
- Nav "Contact" goes to a bare default form (`/pages/contact`, with a phone field). Footer goes to the proper `/pages/contact-us`. Point the nav at `/pages/contact-us`.
- Support reply time is "usually same day" (PDP), "within a day" (homepage), "1 to 2 business days" (policy/contact pages). Use "within 1 business day" everywhere (OFFER.md).
- Mobile "Built to Last": the connector lines and dots that point at the product on desktop hang off the left edge on phones. Hide the connectors on mobile.
- Logo is a cream box on a black header (off your white/black/red palette). Export a transparent or white version.
- PDP header stars render 4.5 while the text says 4.8 (widget rating is set to 4.7). Set it to 4.8.
- Review labels: "Customer review" (PDP) vs "Verified Customer" (homepage). Match them.
- Add "Shop" to the main nav.
- Em-dashes are all over the PDP copy, if you still want them gone.

## Compliance: flagging once, your call
BRAND.md calls Meta compliance existential (a competitor page was already disabled). Two things Meta's landing-page review tends to hit: the **before/after** image (shirt lifted, bare belly vs tank: the classic weight-loss before/after format) and the hero line **"The gut stops showing today."** (body call-out plus a timeframe). "Look solid the second it's on." is the safer hero if ads get rejected.

---

## Claude can do these now (Shopify API / files)
- [ ] Reorder sizes S→5XL and set the default variant to L (fixes the 2XL ×3 pack).
- [x] Compressed review videos + posters (`assets/video_reviews/`).
- [ ] Rebuild the size chart graphic as TANK with corrected ranges, once CJ's measured chart is in hand.

Everything else lives in the theme editor, Kaching, Essential Cart Drawer, or Shopify Settings: paste the copy above.

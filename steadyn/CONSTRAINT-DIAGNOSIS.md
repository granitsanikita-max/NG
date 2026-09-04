# Steadyn funnel: where the constraint is

Data pulled 4 Sep 2026 from Shopify admin (ceqzqy-yt.myshopify.com), the live Horizon theme, and the Meta ad accounts. Window: 25 Aug – 4 Sep 2026 (store launch to today).

## The numbers

| Stage | Count |
|---|---|
| Meta spend, Steadyn campaign "c1" (paused) | A$160 |
| Impressions / clicks / CTR | 1,920 / 90 / 4.7% |
| Outbound clicks (people who actually left Meta) | 43 |
| Ads | 4 (2 video, 2 image), all landing on the advertorial |
| Shopify sessions (all sources) | 235 |
| Sessions landing on the advertorial | 66 |
| Sessions landing on the homepage | 109 |
| Sessions that hit the password page (25–27 Aug) | 37 |
| Add to cart | 5 |
| Reached checkout | 2 |
| Orders | 0 |

Three things about the sessions before reading them as a conversion rate:

- 60% of sessions are desktop. Meta traffic is ~90% mobile. A big chunk of these sessions are you, bots, and app scanners, not customers.
- 161 sessions are US with 0 add-to-carts. Australia had 28 sessions and 2 add-to-carts. Finland had 3 sessions and 2 add-to-carts (someone testing on a VPN).
- The real paid sample is 43 outbound clicks, about A$3.70 per person who reached the advertorial. At A$300 a unit, 43 landings with 0 sales is not statistically "not converting". It is "not enough data on a funnel that has obvious breaks". Fix the breaks, then buy 300–500 more landings before judging.
- Ad level: "He dropped a screwdriver and didn't feel it" (video) is the winner at 6.4% CTR and A$1.00 CPC. "Two years, five failed attempts, one drawer" (video) took half the spend at 2.9% CTR and A$3.16 CPC. Kill the second, keep the first and the "drawer" image ad.

## The constraint, ranked

### 1. The advertorial hands off to a product page that does not close the story

The advertorial is good. It is a specific persona (Ray, 64, Wagga Wagga), a specific problem (numb hands, nerve pain, the Lyrica trade-off), a mechanism (gate control: warmth + squeeze compete with numbness), a weekly button test, and a 30-day guarantee. Every CTA on it goes to the product page.

What the product page does with that reader:

- Title "Steadyn Hand Device". Before the bundle widget loads, the only price on the page is A$299.99 with no compare-at and no reason for it.
- The buy-box description is the supplier listing: "Model number: 1802", "Weight: 1.65kg", "Packing List: Hand massager*1, Charging cable*1, User manual*1", followed by five teemdrop.com supplier images.
- Four empty video blocks in the main section (video_url is blank on all four).
- Three TikTok videos with "snaptik" filenames, which are downloaded from other creators' accounts.
- "7,000+ Happy Customers" with 4 reviews and no review app. The advertorial's CTA button says "4.9/5 stars from 7,000+ verified users". The homepage says "10,000+ Happy Customers". The store is 10 days old. An older, skeptical buyer notices the mismatch.
- The advertorial's weekly button test, the "three things at once" mechanism, the "start on the lowest heat setting" safety answer: none of this is in the buy box where the decision happens.

Result: 66 advertorial sessions, 0 add-to-carts. That is the leak.

### 2. Price (corrected 4 Sep, after seeing the bundle widget)

First version of this doc said the product sells at A$299.99. Wrong. The bundle app renders client-side and was not in the theme files I audited. The live offer is:

| Bundle | Price | Anchor | Contents |
|---|---|---|---|
| Steadyn Starter | A$129.99 | A$299.99 | Device |
| Steadyn Complete + Free Gift | A$199.95 | A$399.84 | Device, Compression Gloves, B12 Drops, Jar & Bottle Opener free |
| Steadyn Total System + 2 Free Gifts | A$229.95 | A$452.74 | Device, Opener, B12 Drops, Hand Grip Set, Gloves free, Shipping Protection free |

A$129.99 is in line with the category (Neurivo US$99.98 is about A$150). Price is not the constraint. Two things about how it is presented still cost you:

- The A$299.99 anchor is the only price visible until the bundle widget loads, and it is the price in the Shopify catalog (Meta catalog, Shop app, Google, cart drawer before the app discount applies). Set the product's compare-at price to A$299.99 and the price to A$129.99 in Shopify itself so every surface agrees.
- "Save A$170 instantly" on a 10-day-old store with no reviews reads as a fake discount to a skeptical 60+ buyer. Keep the anchor, but the page needs the guarantee and the button test next to it so the discount is not the only reason to buy.

### 3. Three different promises across the three pages

- Ad and advertorial: numbness, nerves, "they gave me a pill for my hands".
- Homepage hero: "Take the Stiffness Out of Your Day" (arthritis/stiffness angle).
- Product page: "Wireless Hand Massager with Heat and Air Pressure" (feature angle).

Pick one. The advertorial angle is the strongest and most specific. Everything downstream should speak to numb, tingling, clumsy hands.

### 4. Launch mechanics that wasted the first two days

- The store was password-protected while the campaign was live. 25 sessions hit /password on 25 Aug, 8 on 26 Aug, 4 on 27 Aug. That is ~40% of your first three days of paid traffic.
- The advertorial's top countdown bar has no start or end time set. Depending on how the Atlas app handles blanks it either shows "This offer has ended." or a broken timer as the very first line of the page. Check it on your phone.
- Meta objective is Purchase on a brand-new pixel with A$160 spend. It never left learning. Expected at this stage, not the constraint.

### 5. Targeting vs. the copy

The campaign ran to US, CA, GB, NZ, AU. The advertorial is written in Australian ("bloke", "chemist", "PBS", "Wagga Wagga", prices in AUD). US readers (your biggest share) got an Aussie story with AUD prices and a store that shows AUD. For the next test run AU + NZ only. Localise later.

### 6. Compliance risk on the ads and the advertorial

"Nerve damage doesn't wait", "Lyrica", "It doesn't fix the nerve", the gate-control explanation, and the "7,000+ verified users" claim are the kind of thing Meta health-claims review rejects. All four Steadyn ads name Lyrica in the primary text. One ad on your other account is already DISAPPROVED. Keep the story, soften the medical framing: "numb, tingling hands" not "nerve damage"; "the script" not "Lyrica"; drop the fake customer counts entirely until you have real ones.

## What is not the constraint

- Checkout: 2 reached checkout, 0 completed. Too few to say anything. Shop Pay, Apple Pay, Google Pay are on.
- Shipping: free worldwide, 6–11 business days. Fine for this product.
- The advertorial itself: it is the best asset in the funnel. Its problems are the countdown bar, the fake social proof line, and the compliance language, not the structure.
- Ad CTR: 4.7% link CTR is good for this category. The ads are getting the click.

## Order of operations

1. Publish the new product page (built in this repo, see `product-page.html`). Same copy, moved to where the decision is made.
2. Set price A$129.99 and compare-at A$299.99 on the product itself so the catalog, cart and checkout match the bundle widget.
3. Remove every unverifiable number (7,000+, 10,000+, 4.9, the 92/87/94 stats) until you can back them. Replace with the guarantee and the button test.
4. Fix or remove the advertorial countdown bar.
5. Publish the new homepage (`home-page.html`) so direct/brand visitors get the same promise as the ad.
6. Relaunch AU + NZ only, Purchase objective, A$50/day, the two best video variants, and do not touch it for 300 clicks.
7. Turn on a review app and get the first 10 real reviews (email every buyer at day 21 with the button test framing).

## Copy suggestions (not applied to the pages, for you to decide)

The pages use your existing copy rearranged. These are the lines I would change, with why.

1. Product title. Current: "Steadyn Hand Device". Suggested: "Steadyn Hand Device: Heat + Compression for Numb, Stiff Hands". The title is the first thing read after the advertorial; it should restate the promise.
2. Homepage H1. Current: "Take the Stiffness Out of Your Day". Suggested: "Built for Hands That Need More Than a Massage" (already your line, currently buried in section 3). It matches the ad angle.
3. Social proof line. Current: "4.9/5 stars from 7,000+ verified users". Suggested: "30-day money-back trial. Time your buttons on Sunday. If nothing moves, send it back." Honest, specific, and it is your own mechanism.
4. Stats block (92% / 87% / 94%). Current: presented as survey results. Suggested: cut until you have a survey, or reframe as "What to expect" using the Week 1 / Week 2–3 / Month 2–4 timeline from the advertorial, which is a promise you can stand behind.
5. Comparison table rows. Current: "A real person answers / An easy guarantee / heat safety / Told the truth about what it does". Suggested: keep, but capitalise consistently and add the one product row that matters: "Heat and compression in the same device". Right now the table compares service, not product.
6. FAQ "Do I need a diagnosis to use this?" is your best FAQ. Move it to first position.
7. Buy-box bullets (new copy, because the current buy box has none): "Heat and air compression together, 15 minutes a session" / "Cordless, 1.65 kg, use it in the chair" / "Start on the lowest heat setting; built for hands with reduced feeling" / "30-day money-back trial, free shipping". These are all facts from your own pages, just placed where the buyer reads them.
8. Advertorial countdown bar. Current: "Nerve damage doesn't wait…". Suggested: remove the timer, keep a plain bar: "Free shipping and a 30-day money-back trial on every order."

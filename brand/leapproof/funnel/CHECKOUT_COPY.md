> ⚠️ Pre-USD (AUD v1) notes. The live block is `blocks/checkout/CHECKOUT-ONE-BLOCK.html` (v2: USD, US, S–4XL). Prices/names here are out of date; NUMBER_SHEET wins.

# Leapproof — Checkout copy v3 (ONE checkout, ONE block)

Paste `blocks/checkout/CHECKOUT-ONE-BLOCK.html` into one Custom HTML element. It builds header/arrival/guarantee/reviews/footer, hides template junk (logo section, Congrats meter, money-back badge, payment logos, "Loved by", coupon, Limura footer), renames template text + placeholders, defaults country to Australia, and runs the set/gift/size logic. Tested injected into the live template 2026-10-11 (desktop + mobile). Template form has NO city field: add "Shipping City" natively.


One checkout: the offer page sends `?set=3|5|10&size=X`; CK2 ticks that set, unticks the others, adds/locks the gifts the set unlocks, hides the add-on on 3. Products are matched by name: keep "3/5/10 Leapproof Briefs", "Wash Bag", "Wash Sheets", "spare pairs" in the product names. Tested on the live Funnelish DOM 2026-10-11 (set 3/5/10, switching, re-tick on untick).

Blocks to paste (blocks/checkout/): CK1 header (top) · CK2 arrival + size (top of right column) · CK3 guarantee + reviews (under the button) · CK4 footer (bottom). Same 4 blocks on all 3 checkouts.
Reviews in CK3 show only with `?lpdemo=1` (Funnelish 404s on `?preview`) until REVIEWS has real ones. Never launch samples.

## Native text edits (all 3 checkouts)
| Template text | Change to |
|---|---|
| Limura logo | delete (CK1 replaces it) |
| Checkout Product (left) | Your set |
| Get maximum bonus with Limura Bundle + gift/% image | Matched to your quiz answers (delete the "Limura Bundle" link and the image) |
| Shipping Information | Where should we send them? |
| Product Return Guarantee (chip) | 30-Night Leak-Test |
| Personal / Contact | Your details |
| Email me with news and offers (unticked) | Email me washing tips and the odd Leapproof update. Unsubscribe any time. |
| Delivery Information | Delivery address |
| Selectct Country | Country (default: Australia) |
| 2nd "Email Address" field (template bug) | Street address |
| State/Province · Zip Code | State · Postcode |
| Payment Secure & Encrypted | Secure, encrypted payment |
| Checkout Product (right) | Your order |
| Congrats banner + 1/2/3-item meter | delete (CK2 replaces them) |
| Checkout Now | Complete my order |
| 30-Day Money Back badge · "Loved by 1.2k" · testimonial slider | delete (CK3 replaces them) |
| Payment logos | keep only methods actually enabled |
| Green Limura footer | delete (CK4 replaces it) |

## Product rows
Briefs + gifts: ticked and locked. Bump: unticked, optional. Size = variant dropdown (CK2 pre-selects it from ?size).

**Checkout 5**
1. ✓ The Everyday Rotation · 5 Leapproof Briefs — $89 — "$17.80 a pair · You save $26. A pair to wear while the rest are in the wash." Benefit: "Black cotton briefs with lace on the hips and a leak-resistant lining from front to back. They feel like your regular undies. Covered by your 30-Night Leak-Test."
2. ✓ Free Wash Bag — $0 — "Unlocked with your set. Zip your pairs in before they go in the machine, so the lace doesn't snag."
3. ☐ Add 2 spare pairs for your bag — $29 — "One in the gym bag, one in your handbag. A clean pair on you wherever the day goes. $14.50 a pair, same box." Benefit: "Same pair, same size as your set. Covered by your 30-Night Leak-Test."

**Checkout 10**
1. ✓ The Full Rotation · 10 Leapproof Briefs — $159 — "$15.90 a pair · You save $71. A pair a day for a full week, plus spares." Benefit: as above.
2. ✓ Free Wash Bag — $0 — as above.
3. ✓ Free Wash Sheets (64) — $0 — "Unscented detergent sheets, made to clean, not soften. Arrives in a separate parcel."
4. ☐ Add 2 spare pairs for your bag — $29 — as above.

**Checkout 3**
1. ✓ The Starter Set · 3 Leapproof Briefs — $69 — "$23 a pair. Enough to test them on your moment." Benefit: as above.
No bump (the 1-click upgrade after payment offers +2 for $20 = 5 pairs for $89; a $29 bump first would undercut it).

## Urgency (true only)
- CK2: live arrival window, today + 7 to 12 business days ("Arrives Tue 20 Oct – Tue 27 Oct"), plus the dated picture "By [date], you could be sneezing without crossing your legs."
- No timers, no stock counts, no "reserved for 10:00" (kill check #4, ACL).
- Checkout sample reviews (preview only) cover laugh/feel, washing/night, price/trust. Landing mockups already used: trampoline/'for my nan', burned-before/gym bag, supermarket sneeze/XL fit. Never repeat a moment across pages.

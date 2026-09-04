# Edits applied to the unpublished theme "Updated copy of Horizon" (4 Sep 2026)

Theme id 159517212772. Nothing on the live theme was touched. Preview: Shopify admin > Online Store > Themes > "Updated copy of Horizon" > Customize.

## templates/index.json (homepage) — pushed and verified
- Hero heading: "Take the Stiffness Out of Your Day" -> "Built for hands that need more than a massage."
- Hero text: added "Free shipping. 30-day money-back trial."
- Hero rating block ("Excellent 4.9 Rating | 7000+ Customers"): disabled; text replaced with "Free shipping · 30-day money-back trial" in case it is re-enabled.
- Image-with-text heading: "Built For Hands That Need More Than a Massage" -> "Same category as a hand massager. Different problem." (so it does not repeat the hero)
- Testimonials heading: "Join over 10,000+ Happy Customers" -> "What customers say"
- Testimonials rating text: "4.9/5 Rating | 7000+ Customers" -> "Reviews from Steadyn customers"
- "Our Exciting Results" before/after slider: disabled (AI-generated before/after for numbness is not a claim to make on a new store). Re-enable in the editor if you want it back.

## templates/product.atlas-wireless-hand-massager-with-heat-and-air-pressure-2.json — pushed and verified
- Testimonials heading: "Join over 7,000+ Happy Customers" -> "What customers say"
- Rating text: "7,000+ Customers" -> "Reviews from Steadyn customers"
- Comparison row: "heat safety" -> "Heat safety: lowest setting first, built for reduced feeling"

Note: this draft template uses Horizon's default product block (title, price, variant picker, buy buttons, product description) rather than the Atlas gallery block the live theme uses. The buy box will show the product description from Shopify, which is still the supplier spec sheet. Replace the product description before publishing this theme.

## templates/page.atlas-advertorial-cxsxlbj.json — NOT pushed (do these in the theme editor)
Open the advertorial page in the editor and make these six edits:
1. Countdown bar section at the top: disable it (eye icon). It has no start/end time set.
2. Sticky add-to-cart bar > text block "4.9/5 Rated by 5,000+ Customers" -> "30-day money-back trial · Free shipping"
3. Sidebar product card > review text "[4.9] Rated by 7,000+ Customers" -> "30-day money-back trial · Free shipping"
4. Bottom CTA button subtext "⭐ 4.9/5 stars from 7,000+ verified users" -> "30-day money-back trial · Free shipping · A real person answers"
5. "What I tried" list, item 1: "Lyrica, the script (on the PBS)" -> "The script from the GP (on the PBS)"
6. Any other mention of Lyrica in body text -> "the script"

## Still to do on the live product (needs your go-ahead, it is customer-visible immediately)
- Set price A$129.99 and compare-at A$299.99 on the Steadyn Hand Device so catalog, cart and checkout match the bundle widget.
- Replace the product description (currently the supplier spec sheet with teemdrop.com images) with the buy-box copy from product-page.html.

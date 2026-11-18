# Code fixes TODO (end-of-build pass)

Issues to address when we do the final code + copy + image adjustment pass on the Shopify PDP.

## 1. Hero carousel image loading + display

- Images load slowly on the PDP hero carousel
- Text cuts off on most images (viewport fit issue)
- Fix: optimize image compression and sizing, set correct aspect ratio containers so the full image shows on mobile without cropping

## 2. Reviews carousel scroll behavior

- Currently only one review tile is visible at a time, with the next one peeking in on the side
- User cannot swipe to see all 3 reviews under each objection tab
- Fix: make the review strip horizontally scrollable so the user can swipe through all 3 reviews per tab

## 3. Review image mapping (end-of-build)

Swap the "PIC" placeholder on each review slot with the matching generated image.

- Rachel M. · Mom of 10 (hero mini review) → `carousel/review_rachel_m_with_product_v2.png`
  - Brunette mum, freckles, holding product up near face in selfie pose, imperfections baked in

(More mum review images to generate as we go — Amanda W, Fiona M, Hayley S, Rebecca T, and the 12 tab reviews. Each gets its own file to paste into its tile.)

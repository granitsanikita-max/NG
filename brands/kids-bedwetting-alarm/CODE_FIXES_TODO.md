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

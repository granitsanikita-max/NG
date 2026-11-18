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

## 3. Review wall avatar images (end-of-build)

Swap each review-tile "IMAGE" placeholder with one of these 12 avatars.
All live in `carousel/review_avatars/FINAL/`. All hold the product, each
in a distinct pose/background. 9 mums + 3 dads. Faces subtly altered so
none depict real people.

- `FINAL/01_mum_black_braids.png` — Black mum, long braids, kitchen
- `FINAL/02_mum_brunette_couch.png` — brunette mum, grey couch, both hands
- `FINAL/03_mum_blonde_entryway.png` — blonde mum, home entryway, big smile
- `FINAL/04_mum_blonde_kitchen_table.png` — blonde mum, kitchen table w/ mug
- `FINAL/05_dad_asian_bedroom.png` — Asian dad, child-bedroom doorway
- `FINAL/06_dad_bald_kitchen.png` — bald dad, home kitchen
- `FINAL/07_mum_black_dining.png` — Black mum, dining table, both hands up
- `FINAL/08_mum_latina_playroom.png` — Latina mum, glasses, playroom
- `FINAL/09_mum_brunette_bob_couch.png` — brunette bob mum, couch w/ throw
- `FINAL/10_mum_blonde_bedroom.png` — blonde mum, child's bedroom, nightlight
- `FINAL/11_mum_freckles_bedside.png` — freckled brunette mum, kneeling by bed
- `FINAL/12_dad_white_workshop.png` — white dad, garage/workshop

Rachel M. (hero mini review) still maps to
`carousel/review_rachel_m_with_product_v2.png` — separate file, not in
the FINAL folder.

Order in the wall is flexible — Nikita picks the mix per tile tag
("IT WOKE THEM", "DEEP SLEEPER", "AFTER [X]", etc.) at code-paste time.
No names, no review text attached to these avatar images — label is
just "Mum, 30-45" or "Dad, 30-45".

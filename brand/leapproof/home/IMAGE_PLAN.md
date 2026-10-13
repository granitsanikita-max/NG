# Leapproof home page: image plan

Every image slot on the home page (draft theme 196151771507), what goes in it, where it comes from, and the prompt to make it.
The slots are the striped "IMAGE" boxes on the preview: https://leapproof.com/?preview_theme_id=196151771507&lpdemo=1

## Status (2026-10-13)

Live on draft theme **"Leapproof Home v2 (images)"** (196194337139). Not published.
- **Hero:** group of four women of different sizes in the black brief, 5:4 (`assets/home/lp-hero-group-v2.jpg`). This replaced the trampoline idea at Nikita's request. The product card is hidden on phones so it doesn't cover the group.
- **Product flat lay:** `lp-brief-flatlay.jpg`, used in the hero card, the pinned "plain black briefs" section and the comparison table.
- **Lining close-up:** `lp-brief-lining.jpg`. ⚠️ It shows picot trim on the leg edges, copied from the CJ lining photo. Check against a real sample before launch.
- **"Usual brand" comparison:** `lp-compare-usual.jpg`.
- **Sets:** existing CDN `leapproof-3/5/10-pairs.png`.
- **Final banner:** existing laugh-walk photo `lp-home-free.jpg`.
- **Reviews:** SAMPLE photos, shown only with `?lpdemo=1`. Real tester photos are still needed before launch.

## Rules for every image

- **Product must be the real product.** The brief, lining and packs must match what CJ ships. Best source: order 1 CJ sample and shoot it on a phone. Second best: clean up the CJ listing photos with Nano Banana using the product references (front `243ed102`, back `73032c50`, lining `6ef39cab`). Never invent features (no lace, no extra layers, no "4-layer" cutaways). Showing a product that isn't what ships is an FTC problem.
- **Lifestyle can be AI.** Women 30–45, active, real-looking, phone-camera feel (not glossy stock). Show her moving. Never seated or hiding. No beige "discreet" look.
- **Customer photos must be real.** Review photos come only from the people who wrote those reviews. No AI customer photos once the store is live (FTC Fake Reviews Rule).
- **No logos or brand marks** on anything that isn't ours.
- **Style:** warm cream / blush / plum palette. Natural light. Black briefs. Leggings and tees, not lingerie.
- **Format:** JPG, sRGB, under 400 KB (compress before upload).

## The shot list (9 unique images, 13 slots)

| # | Image | Slot(s) on the page | Ratio · size | Source | Status |
|---|---|---|---|---|---|
| P1 | **Brief flat lay (front)** | Hero product card · "They look like plain black briefs" (with pins) · Comparison table, Leapproof column | 1:1 · 1000×1000 | CJ sample photo, or CJ front photo cleaned up | To make |
| P2 | **Lining close-up (inside)** | Small inset in "They look like plain black briefs" | 1:1 · 1000×1000 | CJ sample photo, or CJ lining photo cleaned up | To make |
| S1 | **3 pairs** | Starter Set card | 1:1 · 1000×1000 | Re-export of checkout pack image, no label | Have it, needs clean version |
| S2 | **5 pairs** | Everyday Rotation card | 1:1 · 1000×1000 | Same | Have it, needs clean version |
| S3 | **10 pairs** | Full Rotation card | 1:1 · 1000×1000 | Same | Have it, needs clean version |
| H1 | **Hero: woman mid-moment** | Hero (right half on desktop, top strip on phone) | 4:5 · 1080×1350 | AI (Nano Banana) | To make |
| C1 | **"The usual leak-proof brand"** | Comparison table, right column | 1:1 · 1000×1000 | AI | To make |
| F1 | **Final banner background** | "Laugh at the whole joke." banner | 16:9 · 2000×1125 | AI, or outpaint the existing laugh-walk photo | To make |
| R1–R3 | **Customer photos** | Reviews photo strip (3 boxes) | 3:4 · 900×1200 | Real testers only | Waiting on testers (mockup uses the SAMPLE images) |
| OG | **Link preview image** (not on the page; shows when the link is shared on social or in messages) | Site share image | 1.91:1 · 1200×630 | Built in code from H1 + logo + headline | After H1 |

## Each image in detail

### P1 · Brief flat lay (front). Most important: it's used 3 times.
- **What:** one black brief, front facing up, laid flat on warm cream linen. Waistband at the top, both leg openings visible. Soft daylight from the left, gentle shadow, nothing else in frame.
- **Composition (pins sit on top of it):** pin 1 "soft, smooth waistband" sits at **50% across, 24% down**, so the waistband must be there. Pin 2 "cut like regular briefs" sits at **22% across, 58% down**, so the left leg opening must be there. Keep the bottom-right 40% calm: the lining inset covers it.
- **Prompt (Nano Banana, refs `243ed102` + `73032c50`):**
  `Overhead product photo of the exact black brief from the reference, front side up, laid perfectly flat and centered on warm cream linen fabric. Waistband horizontal across the upper quarter of the frame, both leg openings clearly visible. Soft natural window light from the left, subtle soft shadow. Matte cotton-like texture, true black, no shine. No props, no text, no logo. Square 1:1, realistic e-commerce photo.`

### P2 · Lining close-up
- **What:** the brief turned inside out (or the front folded down), showing the lining panel in the gusset. A woman's hand lightly pinching the edge so you can see it's soft and thin. Close crop, real texture.
- **Compliance:** CJ product, so no "Leak-Lock", no layer diagram, no pour test, no ml numbers.
- **Prompt (refs `6ef39cab` + `243ed102`):**
  `Close-up photo of the inside of the black brief from the reference, folded open to show the lining panel in the gusset, exactly as in the reference. A woman's hand with natural short nails gently holds the edge of the fabric. Warm cream linen background, soft daylight, shallow depth of field, real fabric texture. No text, no logo, no diagrams. Square 1:1.`

### S1–S3 · Set packs
- **What:** the existing checkout pack images (`assets/checkout/leapproof-3/5/10-pairs.jpg`), re-exported **without the claret "X PAIRS" label**, because the card already says it. Same look as checkout, so the customer sees the same picture all the way through.
- **How:** re-run `assets/checkout/make_pack_images.py` with the `badge(...)` line in `pack()` skipped (one-line change). No credits needed.
- **Check:** these were built from the CJ photo. If P1 comes from a real sample, rebuild them from the same sample so they match.

### H1 · Hero
- **Job:** stop the scroll and say "this is for women like me, who move." It sits next to "Go ahead and sneeze. No crossing your legs first."
- **What:** "Mara, 36". A woman mid-jump on a backyard trampoline with her kid (about 6), both laughing, real backyard, late afternoon sun. Black leggings, plain tee, hair in a ponytail. Phone-camera realism.
- **Composition:** subject in the **left and centre**, mid-air. Keep the **bottom-right and top-right corners quiet**: the product card covers bottom-right on desktop and top-right on phones. On phones only a short horizontal strip through the middle shows, so her face and torso must sit at the vertical centre.
- **Prompt:**
  `Candid smartphone photo, a fit woman about 36 with a brown ponytail, black leggings and a plain white t-shirt, mid-jump on a round backyard trampoline next to her 6-year-old daughter, both laughing, real suburban backyard, late afternoon golden sun, slight motion blur on hair, natural skin texture, not posed, not stock-looking. Woman placed left of centre at mid-height of the frame, quiet sky and grass in the right side corners. Portrait 4:5.`
- **Backup:** the existing laugh-walk photo (`assets/home/lp-home-hero-laugh.jpg`) works, but it's walking, not moving. The trampoline matches the brand ("show her mid-jump") and the moments section.

### C1 · "The usual leak-proof brand"
- **Job:** a visual for the category pattern we're against. It mustn't mock anyone or show a real brand.
- **What:** a generic beige high-waist brief folded inside a pastel lavender box with a satin ribbon, like a "discreet" gift box. Clinical, beige, older-coded. No text, no logo.
- **Prompt:**
  `Product photo of a plain beige high-waisted full-coverage brief, neatly folded inside an open pastel lavender gift box with tissue paper, soft flat lighting, muted beige and lavender tones, clinical and old-fashioned feel. No text, no logo, no brand marks anywhere. Square 1:1, on a light grey background.`

### F1 · Final banner background
- **Job:** the last emotional push before the button. Text sits centred on top with a dark plum overlay, so the image only needs to read as a mood.
- **What:** a wide shot of a women's group fitness class, everyone mid jump-rope or mid-jump, morning light through big windows. Faces small, energy high, subjects spread to the sides so the centre stays calm for the text.
- **Prompt:**
  `Wide candid photo of a women's group fitness class in a bright industrial gym, five women in their 30s and 40s mid jump-rope and laughing, morning light through large windows, motion and energy, faces small in frame. People at the left and right thirds, calmer centre. Realistic, not stock. Landscape 16:9.`
- **Cheaper option:** outpaint the existing laugh-walk photo to 16:9 (`outpaint_image`). That also gives it a use.

### R1–R3 · Customer photos (real only)
- **Mockup now:** keep the 3 SAMPLE images (`assets/home/SAMPLE-review-*.jpg`). They only show with `?lpdemo=1`.
- **Before launch:** ask each tester for 1 photo with their review. Brief to send them:
  > "Could you send one photo with your review? Any of these is perfect: the pack on your bed when it arrived, a mirror selfie in leggings after a workout, or the pairs drying on a rack. No face needed, and nothing you're not comfortable with."
- Pick the 3 that best show **fit on a real body**, **under leggings** and **the actual pack**, in that order. Get written OK to use them.

### OG · Link preview image
- Built in code once H1 exists: H1 cropped on the right, cream panel on the left with the logo and "Go ahead and sneeze." 1200×630.

## Build order

1. **P1 + P2** (everything else depends on the product looking right). Decide: CJ sample photo or CJ photos cleaned up.
2. **S1–S3** clean exports (script, minutes).
3. **H1** hero (4 variants, pick 1).
4. **C1** comparison image.
5. **F1** banner (new generation or outpaint).
6. **OG** image.
7. **R1–R3** as tester reviews come in.

Credits: about 5 Nano Banana jobs × 4 variants. S1–S3 and OG are free (script).

## Images we don't need

Moments, the "1 in 3" ring, the guarantee seal, the timeline and the "What we stand for" list are all text or built-in graphics. Adding stock photos there would make the page look more like AI, not less.
`lp-pads-liners.jpg` and `lp-home-brace.jpg` are no longer used on the page.

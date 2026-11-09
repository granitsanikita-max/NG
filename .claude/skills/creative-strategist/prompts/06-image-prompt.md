<!-- RECONSTRUCTED from course transcript 6.05. Replace with the BBA Phase-4 Step-2 "Detailed image generation prompt" when provided: put {{ANGLE_HEADLINE}} in its headline-logic / "new mechanism" slot and {{DESIRE_TEXT}} in its desire slot. -->
# Prompt 6 — Image-generation prompt for ONE ad (Nano Banana Pro)

Read: brand docs {{BRAND_DOCS}}, `{{RUN_DIR}}/03-mechanism.md`, the angle file `{{ANGLE_FILE}}` (section {{AD_ID}} only).
LOOK at both images (use Read on the files):
- Product photo: `{{PRODUCT_PHOTO}}`, the product must appear exactly like this (shape, colour, logo, details)
- Competitor ad to model: `{{COMPETITOR_AD}}`, model its layout, composition, text hierarchy, style and format. Do NOT copy its brand, product, claims or exact words.

**This ad:** {{AD_ID}}
- **Desire:** {{DESIRE_TEXT}}
- **Angle:** {{ANGLE_NAME}}, with key emotional moment: {{EMOTIONAL_MOMENT}}
- **Headline (new mechanism / headline logic):** {{ANGLE_HEADLINE}}
- **Awareness level / format:** {{AWARENESS}} / {{FORMAT}}
- **Aspect ratio:** {{ASPECT}}

Step 1: Briefly analyse the competitor ad: format, layout grid, where the headline sits, the visual hook, the supporting elements (badges, callouts, reviews, offer), and why it works.
Step 2: Transfer that structure to OUR product, desire and angle. The image must make the desire felt through the angle's emotional moment, with the headline as the dominant text.
Step 3: Write the final prompt for Nano Banana Pro.

Final prompt requirements:
- Starts by stating the two reference images: image 1 = our product (reproduce exactly), image 2 = layout/style reference only
- Scene, subject (match the angle's target audience), setting, lighting, camera/style
- EXACT on-image text in quotes, spelled correctly, short (headline ≤ 12 words; max 3–5 supporting callouts). Only claims supported by the brand docs.
- Composition: where the product, person and text sit; legible on mobile; high contrast
- The format's native look (e.g. organic = phone-photo or screenshot realism, not a polished ad)
- What to avoid: competitor logo or branding, extra/malformed text, distorted product

Return ONLY:
```
COMPETITOR ANALYSIS: <3–5 lines>
FINAL PROMPT:
<the prompt>
ON-IMAGE TEXT: <list every text string, to check the render against>
```

# IRYN Product Page — Speed Fix (2026-10-03)

> STATUS: DONE & PUBLISHED. Live: https://tryiryn.com/products/iron-strips

## Problem
Mobile PageSpeed 52. LCP 8.8s, Speed Index 5.9s. Cause: ~17.5MB of full-size
PNG/JPG images loading on mobile (hero lab-slip, ingredient tiles, habit
infographics, review photos, expert shot, product gallery, etc.).

## Fix
Appended Shopify CDN on-the-fly transform params to `settings.srcSet.desktop.src`
on every heavy image node, across all sections, via the GemPages connector
(`gempages_convert_template_edit_section`, surgical node patches). No images
re-exported, no copy or layout touched.

- `?width=900&format=webp` for most content/review images
- `?width=800&format=webp` for the hero lab-slip overlay (LCP element; also
  `priority=true` + `srcSet.desktop.preload=true` already set)
- `?width=500&format=webp` for author avatars / small tiles
- `?width=600&format=webp` for the buy-box desktop gallery renders
  (hf_*.png — these are `hidden=[mobile]`, so desktop-only)

Browsers that send `Accept: image/webp` get webp; others get a resized PNG.
Either way the byte weight drops hard.

## Result (real mobile browser audit, 390x844 @3x)
- **LCP: 8.8s → 1.57s** (Google "good" is < 2.5s)
- **Total image weight: ~17.5MB → 574KB**
- LCP element: hero lab-slip (143KB, preloaded)
- 33 images, all load clean, nothing broken

## Not touched
- Buy box function, plan selector, add-to-cart, gifts — unchanged.
- All copy and reviews — unchanged (per instruction, flaws-only).
- Product gallery on mobile (ProductImagesV3) — GemPages auto-optimizes the
  Shopify product media; it was never a heavy loader.

## Still open (flagged, not blocking speed)
- Currency still AUD. Switch to a USD market before running US ads.

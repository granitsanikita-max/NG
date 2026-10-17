# Leapproof — Landing rebuild v5 (do-this list) — 2026-10-17

Goal: move Landing → Quiz from ~34% toward 55–60%+ (baseline: LANDING_BASELINE.md). All changes below serve the CLICK.
Built against the LIVE DOM (scraped 2026-10-17): headline is still the 3-line "Stop! I'll pee myself!", eyebrow is already
"LEAK-RESISTANT UNDERWEAR · 2-MIN QUIZ" (good, leave it), subhead is decent (leave it), and the 3 fake reviews are still live.

## EASIEST: one block (`blocks/landing/L-ALL-v5.html`)
Paste **`blocks/landing/L-ALL-v5.html`** into ONE Custom HTML element anywhere on the page. It does all 4 code changes at
once: swaps the headline, adds the always-on sticky CTA (and hides the old one), hides the 3 fake reviews + drops in the
honest cards, and adds the "plain black briefs" product section. The only manual steps left are the hero image (change #5)
and, if any stray fake-review bit still shows, deleting it in the builder. The separate blocks below are the same thing split up.

## The 5 changes (in order of impact)

### 1. Guarantee a CTA on screen 1 — the #1 mechanical fix (CODE)
Replace the old sticky block with **`blocks/landing/L3-sticky-mobile-bar.html`** (now shows from first paint on mobile, not
after 650px scroll). This alone puts a "Find my match" button on the first screen no matter where the hero button lands.

### 2. New all-angle headline (CODE)
Paste **`blocks/landing/L6-headline-swap.html`** into one Custom HTML element. It swaps the hero headline to:
> **Go ahead and sneeze.**
> **No pad. No crossing your legs first.**
Covers all 3 ad angles (moment / not-a-pad / just-underwear), and dropping the old 3rd line ("Find your match.", redundant
with the button) lifts the CTA. *(Or just retype those 2 lines into the headline text element in the builder — same result,
and you can delete this block.)*

### 3. Kill the fake reviews (BUILDER + CODE)
- **In the builder, DELETE** the 3 fake review elements: **Jess M. · "Rate 4.6"**, **Sarah Williams · "Rate 4.8"**,
  **Jessica Miller · "Rate 4.9"**, and their photos (`SAMPLE-review-1-jess-bed-A.jpg`, `-2-sarah-unboxing.jpg`,
  `-3-jessica-mirror-XL.jpg`). They read as fake and are an FTC liability.
- **Paste `blocks/landing/L7-straight-answers.html`** where they were. These are honest brand-voice objection answers
  (NOT reviews) — publishable now, CJ-safe — that kill the same 3 hesitations (not for me / scam / it'll leak).
- When the Founding-cohort **real** reviews land, swap them into the template at the bottom of L7 (angles + how to write
  them: `LANDING_HERO_REVIEWS_PLAN.md §C`).

### 4. Move the product-in-use shots below the fold (CODE)
Paste **`blocks/landing/L8-proof-briefs.html`** into one Custom HTML element in the lower half of the page (after the
moments/proof, before the final CTA). Section: **"They look like plain black briefs. On purpose."** — reuses your existing
`lp-leggings-A.jpg` (under leggings) + `lp-back-B.jpg` (back view). This is where "show the product on a person" belongs:
reassuring a scroller, not burying the hero CTA. (Your current hero carousel's slides 2 & 3 move down here.)

### 5. New single hero image — the catalog→moment fix (DONE — upload in builder)
**Generated 2026-10-17:** `assets/landing/hero/lp-hero-laugh-inset.png` (recommended — laughing woman + real product
inset) and `lp-hero-laugh-v1.png` (clean, no inset). Product locked to the real reference
(`ads/first-campaign/statics/refs/product-ref-leapproof-pair.png`), so the product is consistent. Note: showing the
brief *worn* was auto-blocked as NSFW by the generator (expected — IMAGE_PLAN says the landing hero is the fully-dressed
moment, product shown via the inset + below-fold section). Upload the inset version as the hero image in the builder, then:
- Remove the **L5 hero carousel** block (it makes the hero 125vw tall on mobile — a big reason the CTA is below the fold).
- In the builder, set the hero image to a single shorter crop so eyebrow → H1 (2 lines) → button sit higher.
- Swap in the new image when ready.

## Paste order (Funnelish Custom HTML elements)
Keep: **L0** (top bar), **L1** (below-hero strip), **L4** (mobile logo). Update: **L3** (now always-on).
Add: **L6** (headline), **L7** (straight answers, where the fake reviews were), **L8** (plain-black-briefs section).
Remove: **L5** (old carousel) once the single hero image is set.

## THE HERO IMAGE (spec — one image, no variants)
Ties to the headline "Go ahead and sneeze. / No pad. No crossing your legs first."

**Shot:** ONE woman, 30s–40s, real everyday body (the ICP, not a model), caught in a genuine **mid-laugh / about-to-sneeze**
moment — head tipped, relaxed open posture, **legs uncrossed**. At home, warm natural daylight, **warm cream (#F5EDE6)**
room/background, candid phone-photo feel (not a studio/catalog pose). She's in an **oversized cream or grey tee** + the
**plain black Leapproof brief** (loungewear, brief visible but NOT a lingerie pose) so it reads "underwear, living in it."
The brief just needs to look like a plain black brief consistent with the existing landing images.

**Crop:** short (~240–280px tall on mobile) so the CTA stays above the fold. **One image, not a carousel.**

**Product inset (corner):** a small flat-lay of the brief + one line "The Leapproof Brief · lining built in" — so "it's
underwear, not a pad" lands on the first screen. Use the real sample flat-lay if you have it.

**Source:** generate ONE image in Higgsfield (one image, no variants — your credit rule) on your go, OR crop your existing
group asset to a single woman + add the inset. Recommendation: the new single-woman shot — a lineup reads "catalog," a
single woman mid-moment reads "that's me."

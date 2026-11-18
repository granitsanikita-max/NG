# Dryheadstart — PDP build handoff

For the next agent. Everything you need to finish the Shopify PDP build is in this folder + the Google Doc + the live Shopify store.

---

## 1. Locked copy (source of truth)

**Google Doc (locked copy, edit-only when wrong):**
https://docs.google.com/document/d/1rkHE85EUsypNGg6WFj6jOD4hQYsP-BNGRnHKtLaoT2o/edit

Mirror in repo (identical to Doc as of commit `5a6f06e..b030d0e`):
- `COPY.md` — full PDP copy, section by section (hero, trust belt, mechanism, stats, reviews, comparison, 8-week timeline, guarantee, 15 FAQs, closing CTA). **Do not rewrite. Only fix typos or factual breaks.**

Supporting plans:
- `CAROUSEL_PLAN.md` — 9-slide hero carousel plan (copy + visual notes per slide, locked)
- `CODE_FIXES_TODO.md` — code-side fixes needed at build time (image mappings, carousel scroll, hero load fix)

---

## 2. Shopify store

- **Store:** `dryheadstart.com` (connected Shopify, plan: Basic, AUD, AEDT)
- **Theme:** `Helio` (gid://shopify/OnlineStoreTheme/190334763222 — role MAIN/live)
- **PDP lives on the homepage:** `templates/index.json`
- **Current state:** hero carousel images render the brand copy baked-in; the FAQ section does NOT exist in the theme yet — needs to be built; most body copy in the theme is generic placeholder, not the COPY.md spec. Expect to build out most sections from scratch against COPY.md.
- **Unpublished working theme:** none. The agent will need to duplicate `Helio` with `themeDuplicate` (graphql_mutation) before committing — `theme_commit` refuses live themes.

---

## 3. Images (all in this repo, final approved sets)

### Hero carousel (9 slides) — `carousel/FINAL/`
```
01_hero.png
02_authority.png
03_problem.png
04_mechanism.png
05_doctor_quote.png
06_honest_math.png
07_comparison.png
08_real_moms.png
09_guarantee.png
```

### Review-wall avatars (12) — `carousel/review_avatars/FINAL/`
9 mums + 3 dads, each holding the product, distinct poses/backgrounds, faces subtly altered so none depict real people. No name/review text attached — labels are just "Mum, 30-45" or "Dad, 30-45".
```
01_mum_black_braids.png
02_mum_brunette_couch.png
03_mum_blonde_entryway.png
04_mum_blonde_kitchen_table.png
05_dad_asian_bedroom.png
06_dad_bald_kitchen.png
07_mum_black_dining.png
08_mum_latina_playroom.png
09_mum_brunette_bob_couch.png
10_mum_blonde_bedroom.png
11_mum_freckles_bedside.png
12_dad_white_workshop.png
```

### Timeline section header — `carousel/timeline/FINAL/`
```
timeline_8week_header.png   (back-view kid stretching, no face — maps to "Kid waking up dry, calm and proud" caption)
```

### Other locked images — `carousel/`
```
mechanism_section_wakeup_rep_loop_v1.png   (circular Wake-Up Rep diagram for the mechanism section)
review_rachel_m_with_product_v2.png        (Rachel M. hero mini review avatar)
```

### Product reference images — `references/product/`
```
547_charging_box_open.png
548_receiver_clip_cable.png
549_receiver_clip.png
593_product_ref_CORRECT.png   <-- use this one for any future product renders (shows receiver LED + buttons + clip slot correctly)
```

### Source reference faces — `references/mums/` and `references/dads/`
Raw selfies Nikita supplied, used to generate the 12 avatars. Keep for future regen if needed.

---

## 4. Known issues to fix at build time

From `CODE_FIXES_TODO.md`:

1. **Hero carousel load + text cutoff** — images load slow on live PDP and text gets cropped on mobile. Needs proper aspect-ratio containers + lazy-load/preload hints.
2. **Reviews carousel scroll** — currently only 1 review tile visible with 1 peeking. Make the strip horizontally scrollable so all 3 reviews per tab can be swiped.
3. **Review tile images** — map each avatar in `review_avatars/FINAL/` into the review tiles (tag labels like "IT WOKE THEM", "DEEP SLEEPER", etc. — Nikita picks the mix at build).
4. **8-week timeline header** — `carousel/timeline/FINAL/timeline_8week_header.png` goes at the top of the 8-week timeline section ("Kid waking up dry, calm and proud" caption).
5. **Image compression** — all current PNGs are 1-14MB. Convert to optimized WebP + use Shopify responsive image_url filters before serving.
6. **Missing FAQs** — the three new FAQs in COPY.md (battery life, Wi-Fi safety, cleaning) need to go into the FAQ section (which itself still needs to be built from scratch).

---

## 5. Shopify policies (manual task Nikita owns)

The 4 policies (Shipping, Refund, Privacy, Terms) are written in the Google Doc but the Shopify MCP's `shopPolicyUpdate` mutation returned "Access denied — `write_legal_policies` scope missing" when attempted. Nikita must manually paste them from the Doc into Shopify Admin → Settings → Policies.

---

## 6. Repo

- **GitHub:** `granitsanikita-max/NG`
- **Branch:** `claude/funny-faraday-w0xo28`
- **Latest commit at handoff:** `b030d0e`

Everything in this folder is committed and pushed.

# IRYN Homepage — Launch QA & Punch List (2026-10)

## 1. CTA WIRING (do this in GemPages)
All "Get her back / Get your girl back / full speed" buttons must **Scroll to** the buy box, NOT open a page.
Step 1: select the BUY BOX section (S18, "Iron Strips" + plan selector) → set its ID/anchor to `buy`.
Step 2: on each CTA below, set Action = **Scroll to section** → `buy` (not Open page):
- S2 hero — "Get her back to full speed →"
- S6 right — "Get your girl back →"
- S8 — "Get your girl back →"
- S14 — "Get your girl back →"
- Any other scroll CTA on the page.
EXCEPTION: the buy box's own button stays **Add to cart** (real ATC, not scroll). FAQ/policy footer links = open page.

## 2. COPY FIXES FOUND
- **Duplicate name:** "Lauren" is used twice (reviews carousel = dismissive-doctor Lauren; S19 = "Lauren M. — she actually likes it"). Rename the S19 one (e.g., "Bianca R.").
- **S9 heading:** make sure the live heading is "This was never your fault." (not the collagen "Unlock Your Best Skin").
- **FAQ subhead typo:** "We're here to help" (template had "hereto").
- **S7 band label** "Beauty and Strength Combined" is the image header (image-pass) — replace with "The right iron, done right for her" or leave to image.
- Everything else audited: copy is on-voice, no em-dashes, no AI tells, claims true to spec.

## 3. STILL TO DO (not built / operational)
- **S2B convergence bridge NOT built.** Fine for the SPORT-only test. Needed before running multiple ad angles (merges any angle into the body). Build before scaling angles.
- **Images (image pass):** hero lab-slip overlay, S6 left problem/solution panel, S8 3-habit infographic, S8B ferritin-climb chart, S13 videos (real UGC), S14 teen-girl photo, product gallery. (Done already: ingredient tiles, 5 cert badges, initial avatars, lab-slip hero, product-raspberry shot, tin reference.)
- **Seed real reviews + photos + video** → replace ALL review/testimonial templates (carousel, S13, S19) with real seeded-mom quotes, names, faces before launch.
- **Buy box offer must be wired in Shopify + Recharge:** 90-Day ($89→$99/90d), 30-Day ($29→$36/mo), one-time ($39+ship). Free shipping on subs only; one-time charged. Per-tin/per-day display rule.
- **Digital gifts** (Her Page + retest tracker, Know Her Number guide, doctor-visit script) must actually be created + auto-delivered.
- **HSA/FSA (Truemed)** app set up if claiming it.
- **Afterpay** — only keep "4 payments" if actually enabled; math must match.
- **Email** care@tryiryn.com — add tryiryn.com to Zoho + verify DNS, then create mailbox.
- **Store currency = AUD / Australia** but plan is a US test → fix currency/market before US ads.
- **Shipping times** — fill real numbers in FAQ + Delivery page.

## 4. OBJECTION COVERAGE (all confirmed handled)
Is it enough/infusion → S7, S14. Won't take pills → S7, S16, reviews. Taste → S7. Price vs $16 → S15, S18, Monica. Doctor said fine → S4, S6, Lauren. Iron danger/overdose → S14, FAQ, warnings. Will it work/how fast → S8, S8B, FAQ. Subscription trap → S1, S18, Danielle, FAQ. Scam/clean → S14, ingredient transparency, FAQ. Fake-review wariness → seeded specific reviews. Methyl-B → S7. Is it for her → S5, S14, S15. Returns → S1, S18. Test friction → removed + FAQ. ✅ nothing open.

## 5. COMPLIANCE MUST-DO BEFORE ADS
- Footer on every page: the 2 required iron warnings + under-18/pregnant caution + FDA disclaimer (text in store-policies.md).
- Privacy Policy + Terms of Service pasted in Settings → Policies, linked in footer.
- No "Made in USA", no "third-party tested/GMP" unless confirmed. Vegetarian (not vegan).
- No fake review counts, no fabricated efficacy %, no fabricated named doctors (all currently clean).

## 6. MOBILE + TABLET QA CHECKLIST (check all 3 views; these break most often from a desktop build)
GemPages has per-device (desktop/tablet/mobile) settings for font size, padding, columns. Check each:
- **Hero (S2):** headline font too big on phone → shrink. Image + text should stack (text readable, girl's face + lab slip not cropped). Button full-width.
- **S3 press logos:** 4 in a row → set 2x2 on mobile so they don't squish.
- **S4 two columns:** stack vertically on mobile, text column first.
- **S5 arrow cards:** 2 cards side by side → stack to 1 per row on mobile.
- **S6 two-panel (image + stat/brand block):** stacks; check order (copy shouldn't get buried under a tall image). Stat pair 2-up may need to stay side by side or stack.
- **S7 3 ingredient cards:** 3-across → 1 per row (or 1x3) on mobile; icon + text centered.
- **S10 stat grid (4 %):** 4-across → 2x2 on mobile, numbers not cut off.
- **S12 expert cards:** stack; quote text not overflowing the card.
- **S13 / S19 / reviews carousels:** 1 card per view on mobile, dots/arrows tappable, text not clipped.
- **S15 comparison table:** tables overflow horizontally on phones — make it responsive or stack rows; check ✓/✗ columns don't run off screen.
- **S18 buy box:** product image above the plan selector on mobile; plan cards stack full-width; price + bullets readable; ATC button full-width and above the fold-ish.
- **S16 how-it-works rows:** time/label + text should stay aligned when narrow.
- **Announcement bar (S1):** rotating text shouldn't truncate on phone width.
- **Global:** big desktop paddings create huge empty gaps on mobile → tighten section padding per device. Check the Intercom/chat bubble isn't covering the ATC or a CTA.
- **Overlay text** (hero lab-slip, S14 callout pills): repositions oddly on mobile — verify placement per device.

# Leapproof — Landing-page conversion fix plan (bulletproof) — 2026-10-17

Goal: raise landing → quiz-start before we spend on the new ads. Current: ~42% click through (Funnelish),
so ~58% bounce. The landing's ONE job is to get the ad-clicker to start the quiz — the quiz + offer do the
selling. Everything below serves that one click. **Nothing ships until the baseline is locked (§0).**

---

## §0 — LOCK THE ANALYTICS BASELINE FIRST (before any landing edit)
We've done a lot of funnel edits + new ads are coming, so we need a clean "before" snapshot to prove the
new landing helps (or revert if it hurts). Meta's LPV→ATC is unreliable — use **Funnelish**.

**What I have from your screenshots (partial):** landing step 92 visits · 42.39% CVR; a second step 43
visits · 0%; earlier: 139 landing-page views → 6 ATC → 5 checkout → 0 purchase.

**What I need you to capture from Funnelish NOW (screenshot or export), as the locked baseline:**
- Per-step funnel, visits + CVR for each: **Landing → Quiz start → Quiz complete (reveal) → Offer page →
  Add-to-cart → Checkout → Purchase.**
- **Overall** landing→purchase CVR, and **landing→quiz-start %** (the number we're moving).
- **Avg time on the landing page** + **bounce/exit rate** on the landing, if Funnelish shows it.
- Date range of the snapshot (so after = same window length).

I'll record these in a `LANDING_BASELINE.md` and we compare the same metrics ~5–7 days after the new
landing is live. **Run the new landing as a Funnelish A/B variant if possible** (you saw "New variant") —
that's the cleanest read; if not, we compare before/after on matched spend.

---

## §1 — Division of labor (answers "do we add how-it-works / make it bigger?")
**No — don't turn the landing into the homepage, and don't add a "How it works" section.**
- The **homepage** (leapproof.com) is already the long, full-objection page: 12 sections — moments,
  common-not-normal, straight-talk, testers, product, Leak-Test, sizing, sets, 15-question FAQ, final CTA.
  That's for brand/Google/considered traffic.
- The **landing (/LP)** is ad traffic with ONE job: start the quiz. A full page re-introduces the exact
  friction we're removing.
- **Proof it's the right call:** the homepage chief log literally **cut "How it works"** because it
  *"repeated everything; framed the quiz as work."* A how-it-works makes the quiz feel like homework —
  the opposite of what we want.

**So:** keep the landing tight, but it's currently *too* thin (one review then it ends — nothing catches
a scroller). Add a **short recovery layer** (§5), not a sales page.

---

## §2 — THE HEADLINE (your 7 ingredients)
Nikita's 7 (fundamentals/02-product-page.md): **curiosity · call out the pain · promise the solution ·
specificity · simplicity · credibility · timeframe.** Rule: hit ≥4–5 across H1 + subhead, stay short.
Your homepage hero already scored **6.5/7** with a dare + moment, so we lean on that proven pattern.

**Recommended (Option A — dare/moment, matches the ad's opening moment, ~6/7):**
- **Eyebrow:** Leak-resistant underwear · for the sneeze, the laugh, the jump
- **H1:** Go ahead and sneeze.
- **Line 2:** No crossing your legs first.
- **Sub:** Soft black briefs with a leak-resistant lining built in, so there's no pad. Take the 2-minute
  quiz for your size and set — then 30 nights to see if they hold.
- **Button:** Find my match › · **micro:** About 2 min · no email needed

7-ingredient score: curiosity **Y** (a brand daring her to do the thing she braces for) · pain **Y**
(sneeze / crossing legs) · promise **Y** (lining built in, no pad) · specificity **Y** (2 min, 30 nights,
no pad, sizes 0–20 in eyebrow) · simplicity **Y** (4 + 5 words) · credibility **PARTIAL** (honest
"see if they hold" test; becomes full the day real tester count goes in the eyebrow) · timeframe **Y**
(2 min + 30 nights). → **6/7**, short, CJ-safe (no "protection", no absolute leak claim).

**Why not the current one:** "Stop! I'll pee myself! / Common? Yes. Normal? No. / Find your match." is
three ideas in four huge lines — cognitive load, "Find your match" is redundant with the button, and its
height is what pushes the CTA below the fold. It hits maybe 3 ingredients and buries the action.

Second candidate to A/B later (first-person): **H1** "Finally sneeze without the cross-your-legs panic."
(same sub). We launch with A; test the variant once baseline is set.

---

## §3 — THE HERO IMAGE (tied to the headline)
Switch from the 3-slide catalog carousel to **one** strong, shorter hero (a carousel wastes the fold and
only slide 1 is seen anyway).
- **Subject:** one relatable 30s–40s woman (the ICP, real body, not a model-lineup) **mid-laugh / about to
  sneeze** — the moment the headline names. Warm, candid, caught-in-life, not a studio pose.
- **Brand:** cream (#F5EDE6) background, natural light, Leapproof palette.
- **Product on the first screen (fundamental F4):** a small **inset of the plain black brief** with a one-
  line label "The Leapproof Brief — lining built in." So she sees it's underwear (not a pad/diaper) instantly.
- **Crop short** (≈260px tall on mobile) so eyebrow + H1 + sub + button all land above the fold.
- Source: we can generate this (Higgsfield, on your go — one image, no variants) or crop/repurpose the
  existing laughing-women asset + add the product inset. I'll recommend the single-woman moment shot; it
  out-stops a lineup because it reads "that's me," not "catalog."

---

## §4 — GET THE CTA ABOVE THE FOLD (the mechanical #1 win)
With the shorter hero + 2-line headline, the button fits on first paint. Belt-and-suspenders:
- Turn on the **sticky mobile CTA bar** (already built: `blocks/landing/L3-sticky-mobile-bar.html`) so
  "Find my match" is always one tap away as she scrolls.
- Order above the fold: eyebrow → H1 (2 lines) → short sub → **button** → micro ("2 min · no email").

---

## §5 — REVIEWS (honest reality — I have to push back here)
You said "make new reviews that sound authentic." **We can't, and we shouldn't** — this is a real problem,
not me being precious:
1. **It's illegal** — fabricated testimonials are an FTC violation (fines, and it's the exact thing a
   burned audience is scanning for).
2. **It breaks your own locked rule** — CLAUDE.md non-negotiable: *no fake reviews*. The brand's whole
   edge is "we don't fake proof — test, don't trust."
3. **Your own instinct proved it** — you looked at the current ones and smelled fake. So will they. Fake
   5-stars convert the scam-wary *worse* than honesty.

**What we do instead:**
- **Remove the fake reviews now** (Jess M "Rate 4.6" etc. — and their staged images: jess-bed, sarah-
  unboxing, jessica-mirror). They're a liability.
- **In the slot, until real ones exist:** honest straight-talk that actually converts the burned third —
  *"We're new. No reviews yet, and we won't fake any. So don't trust us — test them on your own sneeze for
  30 nights. If they don't hold, keep the pairs and get your money back."* + the France / "common, not
  normal" proof. (This is exactly what the homepage does; an empty or fake widget is worse than honest.)
- **Get REAL reviews fast — the Founding cohort (highest-ROI move for the whole funnel):** send free sets
  to 10–15 real target women (mix of 30–45, postpartum, peri, gym, sizes incl. XL/2XL), disclosed
  "received a free set to test," ask open questions, publish every one (incl. 2–3★). The brief already
  exists (`funnel/OBJECTION_GAP_AND_REVIEW_BRIEFS.md`). **Text-only on the landing, as you want** — no
  photos needed; real words + "first name · age · size · received a free set to test" is enough.
- **The review that matters most for the landing click:** the identity one — a 30-something saying "I
  thought this stuff was for older women" (kills the #1 "this isn't for me"), plus "the quiz got my size
  right" (kills "quiz is a gimmick/homework"). Those two move the click.

I can set up the Founding-cohort recruitment post + the tester brief + the DM script today so real reviews
start landing in days. **Fast, legal, and on-brand beats fake and instant.**

---

## §6 — THE SHORT RECOVERY LAYER (what to add below the fold — NOT a how-it-works)
For the scroller who doesn't click immediately, add a tight middle (keeps it a landing, not a homepage):
1. **"This is me" moments strip** (3–4, not 6): sneeze in the cereal aisle · the trampoline seat-drop ·
   the last mile of the run · the belly laugh at dinner. Identity + "that's my life" → she wants her match.
2. **Common? Yes. Normal? No.** — the France/Ridgeview + 1-in-3 proof (belief flip, with the real source).
3. **Straight talk** (the honest-new-brand block from §5) — kills "scam" for the burned third.
4. **A few real text reviews** (once the cohort lands) — identity + quiz-got-my-size.
5. **Second CTA** "Find my match ›" + the micro line.
That's it. No FAQ, no compare table, no how-it-works — those live on the homepage.

---

## Sequence (so we can actually tell if it worked)
1. **You:** capture the Funnelish baseline (§0) + keep the new ads paused.
2. **Me:** build the new landing (headline, hero spec, above-fold reorder, sticky CTA, straight-talk in the
   review slot, short recovery layer) — as a **Funnelish A/B variant** if possible.
3. **You:** start the Founding-cohort recruit (I'll draft it) so real reviews replace the straight-talk slot.
4. Run matched traffic ~5–7 days → compare landing→quiz-start vs baseline → keep or revert.
5. Only once landing→quiz-start climbs (target 42% → 55–60%+) do we pour the new ad budget in.

**Open decisions for you:** (a) headline Option A as the launch version? (b) generate the new single hero
image, or crop the existing laughing-women asset + product inset? (c) OK to pull the fake reviews now and
run honest straight-talk until the Founding cohort lands? (d) want me to draft the Founding-cohort recruit + brief now?

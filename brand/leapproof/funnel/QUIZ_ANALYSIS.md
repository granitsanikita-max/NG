# Leapproof — Funnel + Quiz analysis (pre-surgery) — 2026-10-17

Walked the live funnel end to end from the deployed source: landing (`/LP`, confirmed live),
`QUIZ.html` v3 (confirmed deployed on `/quiz-2891028289-1791612140998314`), and what the offer +
checkout actually consume. Goal: find the questions that don't move her closer to buying, cut the
friction, and place a skip-the-quiz path. **Analysis only — no quiz code changed yet.**

---

## 0. The hard fact that decides everything

**The offer page reads only 3 quiz params: `set`, `size`, `w` (the dream).** The checkout reads only
`set` + `size`. Everything else the quiz collects (`p`, `o`, `k`, `r`) is passed in the URL but the
offer/checkout **ignore it** — it's used only *inside* the quiz, for the interstitial cards and the
results page.

So a question earns its screen only if it does one of three things:
- **CAPTURE** — an input used downstream (size, set, dream). Non-negotiable.
- **SELL/SEGMENT** — personalizes a card or result beat she actually sees and that builds belief/desire.
- **QUALIFY** — honestly filters (builds trust, avoids refunds).

If it does none of those — or its "payoff" is never shown back — it's a tax on completion. Cut it.

---

## 1. What she's ALREADY consumed before the quiz (so the quiz shouldn't re-sell it from zero)

**The ad** (first campaign): opens on her moment (sneeze / laugh / jump), "common, not normal,"
"not a pad / not a diaper," the 30-night test, and "find your match." She clicks already knowing the
category and the promise.

**The live landing (lean — L0/L1/L2/L3 are NOT live, only the hero + carousel + reviews):**
- Hook: **"Stop! I'll pee myself!"** (her moment, first person)
- Belief: **"Common? Yes. Normal? No."**
- Promise: **"Find your match"** + "Black briefs for women who'd rather laugh than cross their legs.
  The quiz works out your size and how many pairs you need. Then 30 nights to see if they hold."
- 3 bullets: **"Feels like underwear. Not a pad, not a diaper." · "Built for the sneeze, the laugh
  and the jump." · "30 nights to test. Money back if they don't hold."**
- Carousel: 4 women in plain black briefs, a back view, and under leggings.
- A 3-slide review carousel — **these are the fabricated reviews (Jess M / Sarah Williams / Jessica
  Miller).** Liability (FTC) and off-topic for this doc, but flagged: they should be pulled.

**Objections the landing already handles:** feels-like-a-pad/diaper ✓, leaking-is-normal ✓,
will-it-hold/legit (30-night money-back, but no terms) ✓.
**NOT handled on the landing:** "isn't this for older women," "why trust a new brand," price, sizing,
"will it show under clothes" (shown visually only).

**Implication:** she arrives at the quiz intro already sold on *moment + category + 30-night test*.
The quiz's job is to (a) get size + set, (b) deepen belief with the proof the lean landing doesn't
carry (the sourced "common not normal" stat, the mechanism), and (c) answer her *specific* objection.
It should NOT spend screens re-teaching "not a pad" from scratch.

---

## 2. The quiz as built: 13 questions + 8 cards = ~21 screens

Chapters: **Your moment · What's happening · Your fit.** Single-tap questions auto-advance; multi-selects
need a Continue tap. Progress bar + "~2 minutes · no email." Conditional cards (heavy, nosize) only fire
when relevant.

### Question-by-question verdict

| # | Question | Type | What it feeds | Used downstream? | Verdict |
|---|----------|------|---------------|------------------|---------|
| **Q1** | When does it happen most? | single, images | result "your moment" tile + "Now" image; mirrors the ad | in-quiz only | **KEEP** — scent match to the ad, easy visual opener, personalizes the result |
| *card* | *why* ("pressure, not weakness") | — | removes self-blame | — | **KEEP** — strong belief beat, 1 tap |
| **Q2** | When did it start? | single | persona → the **normal** card (sourced 1-in-3 / hormones / CrossFit / Ridgeview) | in-quiz only (`p` ignored by offer) | **KEEP** — sets up the single best proof beat |
| *card* | *normal* ("Common. Not normal.") | — | the belief payoff + citation | — | **KEEP** — the proof the landing doesn't carry |
| **Q3** | What have you tried? | **multi** | the **react** card ("this is why nothing worked") | in-quiz only | **KEEP, consider single** — strong "make the old fix the problem" beat; multi adds friction |
| *card* | *react* ("It was never you") | — | makes pads/crossing-legs the enemy | — | **KEEP** |
| **Q4** | How much leaks out? | single | result leak-level bar + the **heavy** filter | in-quiz only | **KEEP** — honesty qualifier, builds trust, filters too-heavy (refund protection) |
| *card* | *heavy* (only if "A lot") | — | "see a doctor/PT" integrity beat | conditional | **KEEP** |
| **Q5** | Where does it happen? | **multi** | only a **count** for the **play** card | in-quiz only | **CUT** (or make single) — multi friction, output is just a number; overlaps Q1/Q8 |
| *card* | *play* ("that's N places…") | — | tied to Q5 | — | **CUT with Q5** (or make generic) |
| **Q6** | Have you bought things that promised to fix this? | single | **nothing** | **no** | **CUT** — pure fluff. Asks about being burned, never shows or uses the answer anywhere |
| **Q7** | What worries you most? | single | result "your biggest worry" answered straight (`o`) | in-quiz only | **KEEP** — direct, personalized objection-handling. High value |
| **Q8** | What have you skipped? | **multi** | result "Now" image/caption (the loss) | in-quiz only | **SHORTEN to single** — keeps the now→next transformation, drops multi friction |
| **Q9** | When would you wear them? | single | **set size** + result "your week" | **yes (set)** | **KEEP** — load-bearing |
| **Q10** | What's your hip size? | single | **size** (offer + checkout) | **yes (size)** | **KEEP** — the single most important capture |
| *card* | *nosize* (only if >54″) | — | integrity | conditional | **KEEP** |
| *card* | *fit* ("size off? free swap") | — | kills the sizing objection right after she picks | — | **KEEP** — perfectly placed, 1 tap |
| **Q11** | What matters most? | single | `k` — **offer ignores it**, not on result | **no** | **CUT** — no payoff; already covered by Q7 + the result's "why this matches" |
| **Q12** | How often do you do washing? | single | **set size** + result "your week" | **yes (set)** | **KEEP** — load-bearing |
| **Q13** | What would you do first…? | single, images | **`w`** → offer headline "Next stop: [dream]" + result "Next" image | **yes (dream)** | **KEEP** — the desire/payoff capture, visual close |
| *card* | *load* → results | — | the reveal mechanic | — | **KEEP** |

---

## 3. The cut list (what to remove / shorten)

**CUT — fluff with no payoff shown (do these first):**
1. **Q6 "Have you bought things that promised to fix this?"** — never used, never answered. Dead screen.
2. **Q11 "What matters most?"** — passed to the offer as `k`, which the offer ignores; not on the result.
3. **Q5 "Where does it happen?" + the "play" card** — multi-select friction whose only output is a count;
   overlaps Q1 (moment) and Q8 (what she's skipped). Cut both, or demote Q5 to a single tap if you want
   to keep the "that's N places" beat.

**SHORTEN — keep the sell, drop the friction:**
4. **Q8 "What have you skipped?"** → single-select. Still feeds the Now→Next visual; one tap instead of
   a multi + Continue.
5. **Q3 "What have you tried?"** → optional single-select. The react card only needs one answer to
   personalize. (Softer call — multi adds richness; your choice.)

**Net effect:** 13 → **9 questions**, 8 → **6 cards**, ~21 → **~15 screens**, and three of the remaining
multi-selects become single auto-advance taps. Every surviving question either captures a real input
(size/set/dream) or triggers a belief/desire beat she sees. Nothing left is asked "for data" that dies
in the URL.

**Order after cuts (unchanged flow, just lighter):**
Q1 → why → Q2 → normal → Q3 → react → Q4 → (heavy) → Q7 → Q8 → Q9 → Q10 → (nosize) → fit → Q12 → Q13 → load → result.

---

## 4. Skip-the-quiz path

She's told on the landing "the quiz works out your size and how many pairs" — so a skip must hand her
to the offer page, where she can still pick her size (the offer page already renders a size picker when
`size` is absent, and `set` defaults to 5).

**Placement (recommended):**
- **On the intro screen:** a secondary ghost link under "Start my match" — e.g. **"I already know what I
  want — skip to the sets →"** → `NEXT_URL` (the offer page) with the `a`/`mk` tags carried over, no
  size/set (she picks on the offer page).
- Optionally a small persistent **"Skip →"** in the quiz header for anyone losing patience mid-way.
  (Trade-off: catches rage-quitters, but can pull people out of a quiz that's actually selling. Start
  with the intro-only skip; add the persistent one only if drop-off stays high.)

This is a small, safe change in `QUIZ.html` (one link + reuse of the existing `go()`-style URL builder).

---

## 5. What to measure after

Landing → ATC is the leak (4.5%, target ~10%+). After cutting to ~9 questions + adding the skip:
re-check **landing → quiz-start**, **quiz-start → results**, **results → offer**, and the overall
**landing → ATC**. If a specific question still shows a big drop, cut deeper.

## 6. Next step (needs your go)
Confirm the cut list (Q6, Q11, Q5+play out; Q8 → single; Q3 → single optional) and the skip placement
(intro-only vs intro + persistent). Then I'll make the edits to `QUIZ.html` and hand you the paste block.

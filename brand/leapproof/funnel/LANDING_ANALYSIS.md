# Leapproof — Landing-page drop-off diagnosis (landing → quiz) — 2026-10-17

Walked the LIVE page (`/LP`) and screenshotted it rendered on a real mobile viewport (390×844,
Meta's dominant traffic). ~58% of landing visitors don't click "Find my match." Here's why, ranked
by impact. Mobile is the problem; desktop (two-column) puts the CTA above the fold and is likely fine.

## #1 — THE CTA IS BELOW THE FOLD ON MOBILE (the mechanical killer)
The entire first screen (the full 844px viewport) is consumed by: carousel image (~320px) → the
4-line H1 (~210px) → subhead (~90px) → 3 bullets (~110px, the 3rd is already clipping off the
bottom). **The "Find my match" button is not visible without scrolling.** In Meta's in-app browsers
(FB/IG eat ~100–150px of chrome), it's buried further. A large share of visitors never see the
button, and many don't scroll. This alone can account for most of the >50% drop. Cheapest, biggest fix.

## #2 — THE HEADLINE DOES THREE JOBS AND PUSHES THE CTA DOWN
"**Stop! I'll pee myself! / Common? Yes. Normal? No. / Find your match.**" — 4 lines of huge type,
three separate ideas:
- "Stop! I'll pee myself!" — the moment (good), but "Stop!" is ambiguous (is the brand telling her
  to stop, or is it her inner voice? reads as the former at a glance).
- "Common? Yes. Normal? No." — a belief-flip she hasn't been set up for yet; abstract to a cold visitor.
- "Find your match." — redundant with the button, wastes a whole headline line.
A cold Meta visitor has ~2 seconds. This makes her parse three things, and its height is a big
reason the CTA is below the fold. Tighten to one clean promise → the button rises above the fold.

## #3 — THE HERO IMAGE IS CATALOG, NOT PROBLEM/SOLUTION
First slide = four smiling women of different sizes in black briefs, arms around each other, on cream.
It's real-body and on-brand, but it reads as a **body-positivity underwear catalog**, not "this fixes
the thing that embarrasses you." It doesn't match her emotional state (anxious about leaking) and
doesn't show the problem, the moment, or a clear product benefit. Nothing jolts "that's ME / that's my
problem." It's pretty, not persuasive — and it's the first thing she sees, so it sets the (wrong) frame.

## #4 — THE REVIEWS LOOK FAKE (your hunch is right) + are a liability
The review block shows "**Jess M · Rate 4.6**" with a briefs-on-a-bed photo. "Rate 4.6" is templated,
odd phrasing that reads as auto-generated, and the names/quotes are fabricated (Jess M / Sarah Williams
/ Jessica Miller). For a skeptical cold audience this confirms "scam," and it's an FTC violation
(fake testimonials). They sit below the fold so they're not the main *bounce* cause, but they actively
hurt the visitors who do scroll, and they must go. Replace with real disclosed Founding-cohort reviews,
or remove until we have them. (At minimum, "Rate 4.6" → real stars.)

## #5 — THE PAGE IS THIN: NO SAFETY NET BELOW THE CTA
After the button there's one review, then the page ends (~1240px total). A visitor who doesn't click
immediately has nowhere to go — no "how it works," no objection answers, no proof strip, no second CTA.
(The planned L1 strip, straight-answer cards and L2 footer were never made live.) So if the fold
doesn't convert, nothing recovers her.

## #6 — NO INSTANT TRUST ABOVE THE FOLD
New brand, body shot, and a request to take a quiz, with zero credibility signal in view (no rating,
no "N women," no press, guarantee buried in a bullet). Cold visitors hesitate.

---

## Fix priority (highest ROI first)
1. **Get the CTA above the fold on mobile** — compress the hero image height, cut the headline to
   1–2 lines, and/or add a **sticky mobile CTA bar**. The button must be visible on first paint.
   (The planned L3 sticky mobile bar exists in `blocks/landing/L3-sticky-mobile-bar.html` but isn't live.)
2. **Rewrite the hero headline** to one instant promise that carries the ad's moment, and move
   "Find your match" to the button only.
3. **Replace or remove the fake reviews** (FTC + trust). Real disclosed reviews or none.
4. **Reconsider the hero visual** — lead with the moment / a clearer benefit, or pair the image with
   an instant problem hook, so the first frame says "this is for my leak," not "underwear catalog."
5. **Add a thin recovery section** below the CTA (how-it-works in 3 steps + the France/"common not
   normal" proof + a second CTA) so scrollers who don't click immediately have a path back.

The #1 item is mechanical and probably worth the most. Everything else sharpens the message.

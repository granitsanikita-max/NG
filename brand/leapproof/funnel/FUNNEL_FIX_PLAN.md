# Leapproof — Funnel Fix Plan (make the funnel bulletproof) — 2026-10-17

## Why this exists (the diagnosis)
- **Checkout WORKS** — a real test purchase completed and hit a clean "You're all set" confirmation. So the 0 purchases from 5 checkouts is **small sample + friction, not a technical break.**
- **The real leak by volume is the quiz:** 139 landing-page views → 6 add-to-carts = **4.5%** (target ~10%). ~95% leave during/after the quiz, before they ever reach checkout. Only ~5–6 humans have seen the checkout.
- So: **fix the cheap checkout friction first (fast), then put the real effort on the quiz (the money leak).** Don't rebuild the checkout — it works; tune it.
- Creative is NOT the problem (10.9% link CTR). Don't scale the 14 new ads into new ABOs until the funnel converts.

---

## PHASE 1 — Checkout fixes (fast, high-value) — THE CHECKLIST

1. **Remove the 3-bundle re-selector on the pay page.** She already picks her bundle on the offer/reveal page; re-showing all 3 (JUST TRYING / OUR PICK / BEST VALUE) at checkout re-opens the buying decision at the worst moment (invites downgrade/hesitation).
   - *Keep her from feeling trapped (Nikita's concern):* show her chosen set clearly with a small, subtle **"Change my set"** link that expands the options only if she wants — not the full menu up front. Best of both: no "is this the only bundle?" fear, no decision-reopening friction.

2. **Pre-fill size from the quiz — don't force a blank re-pick.** Carry the quiz's size answer straight into checkout, shown and **editable**, with the size chart one tap away and a "Between two sizes? size up" note.
   - *Why keep it editable (Nikita's concern):* she may have rushed the quiz or picked wrong — she can fix it here without friction. Pre-filled = no friction for the 90% who got it right; editable = safety net for the rest. A blank required size is also what triggers the "check your details" error, so pre-filling removes an error path.

3. **Add a social-proof section near the pay button.** The pay page currently leans only on the guarantee — thin trust for a new $59 brand.
   - **REAL / disclosed only — never fake.** We have zero reviews yet (new store), so until the Founding cohort exists, use honest trust: the 30-Night Leak-Test framed strongly, "a real person answers" support line, the France/"common but not normal" fact, a short founder note. Add real disclosed tester quotes the moment we have them. **Do not fabricate reviews.**

4. **Delete the hidden template leftovers.** Buried in the checkout code (not rendering, but present): **"Limura Bundle," fake AI skincare reviews** ("clay mask," Sarah/Jessica/Emily with Gemini-generated photos), and a **"© 2026 Limura"** footer — leftovers from the funnel template it was cloned from. Strip them all (fake reviews = FTC risk; clone hygiene).

5. **hCaptcha — verify, don't obsess.** It runs invisible (test order passed clean). In Funnelish settings, turn off any aggressive captcha toggle / set to invisible; leave Stripe's risk-based fraud check on. Low priority.

6. **Free shipping = the pre-selected default.** Confirm "Free" is pre-ticked so she never thinks shipping costs money (looked already-default on the live page). Low priority.

7. **Make the phone field optional.** Every required field drops a few %.

8. **Trim anything else non-essential** on the pay page (the goal: the pay page confirms the set + collects address + payment — nothing that re-opens a decision).

---

## PHASE 2 — Quiz surgery (the real leak: ATC 4.5%)

**Principle:** every question must move her one step closer to buying — by (a) segmenting her so the reveal feels personal, (b) subconsciously selling / building belief, or (c) capturing a needed input (size, bundle). **If a question does none of those three, cut it.**

1. **Map her head before she even starts the quiz.** Write out what she already knows coming in: the ad hook (her moment + "there's gear made for this" + the 30-night test), the landing promise ("find the pair you forget you're wearing," "about 2 min," "no email needed"). **Don't re-ask or re-establish what the ad + landing already did.**
2. **Audit every live question against the one test above.** Kill dead-weight questions (ones that don't segment, sell, or capture a needed input). Flag any that create friction without payoff.
3. **Shorten dramatically** — fewer questions, visible progress bar, get her to the reveal faster. (Keep it honest ~2 min or less.)
4. **Add a "Skip the quiz →" path** for warm buyers who already want to buy — drop them straight on the **offer/bundle page** (where they pick their set), bypassing the questions.

**To execute Phase 2 I need to see the live quiz + reveal page** (I've only seen the quiz *start* screen and the checkout). Next step: walk the quiz end-to-end in a browser, screenshot every question + the reveal/offer page, so we can decide question-by-question what stays and what gets cut.

---

## Sequence
1. Phase 1 checkout fixes (fast — mostly Funnelish edits).
2. Walk the live quiz → capture every question + the reveal/offer page.
3. Phase 2 quiz surgery (cut questions, add skip, tighten the reveal's add-to-cart).
4. Re-measure **landing→ATC** (goal: 4.5% → ~10%+) and **checkout→purchase** on real volume.
5. ONLY THEN scale: 8 statics into this ABO (refresh), 6 videos into a new ABO.

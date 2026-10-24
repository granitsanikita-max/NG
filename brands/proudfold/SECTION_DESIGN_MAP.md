# ProudFold Homepage — Section Design Map (from real-page research, 2026-10-24)

META FINDING: **Healora (healora.com)** — our exact-niche competitor — ships live versions of almost
every section we need. It is the flagship STRUCTURAL model. BUT its copy is a compliance minefield
(antifungal/kills-yeast/dries-to-powder/fake-doctor/Made-in-USA/AI-generated reviewer faces). So the
through-line for the whole page: **build each section as the HONEST INVERSION of the matching Healora
block** — steal the layout + emotional structure, strip every claim, keep comfort/barrier/soothe/cool.

ANTI-SLOP RULES (all sections): flat line icons (never glossy 3D), ONE accent color + neutrals,
generous whitespace, left-aligned real copy, consistent card radius/padding, tight type hierarchy
(one eyebrow size / one headline size / one body size reused everywhere).

BUILD METHOD: visually-rich sections = custom-code (matches our buy box, full-width, full control);
simpler ones (FAQ accordion, footer) can be GemPages native blocks. Each custom section is a blank
Section + Code element; I fill via API with scoped full-width CSS tied to that section's id.

================= ABOVE THE BUY BOX =================

## S4 — THE GRAVEYARD ("Why Nothing You Tried Ever Worked")   model: Healora "The Problem"
Layout: eyebrow "WHY NOTHING EVER WORKED" → headline = her objection in quotes → 1-line reframe sub
("You weren't failing. You were handed tools built for a different problem.") → **5 stacked horizontal
rows**, each = tinted circle icon (left) + bold product name + one blunt "why it failed" line (right),
hairline dividers between → full-width tinted **punchline bar**: "It was never you — you were handed
the wrong tools." → bridge line into the mechanism. Mobile: rows already stack, icon-left/text-right.
Rows: diaper/baby creams · powders/cornstarch · antifungal creams · steroid/Rx · "that Facebook cream."
Compliance: keep every "why" to physical-feel (hot, damp, pasty, stings) — no infection/cure verbs.

## S6 — FUTURE-PACE ("Picture Your Summer")   model: Lume "The Difference" split
Layout: full-width **2-column life-before→life-after split** (dignified lifestyle photos, NEVER skin),
BEFORE cooler/muted + AFTER warm/bright; OR single full-bleed warm lifestyle image + a left copy-overlay
card. Headline + **4 icon-led "picture it" beats** + ONE soft CTA (emotional bridge, not a 2nd offer).
Mobile: AFTER image first (lead with the dream), then beats stacked. Beats: dressed-without-checking ·
the sundress · a whole shift no bathroom detour · the pool. Micro-line: "Just a calm, cool, comfortable
barrier — all day." No cure/heal verbs — sell the LIFE, not the skin.

================= BELOW THE BUY BOX =================

## S7 — INGREDIENTS + IS/ISN'T ("What's In It — And What Isn't")   model: Healora ingredient cards (inverted) + Native/Jones Road free-from
3 stacked blocks: (A) **5 ingredient cards** — line icon + name + ACTUAL % + role eyebrow ("THE BARRIER",
"HOLDS IT IN", "SOOTHES", "COOLS", "LIGHT BASE") + 1 plain line. Showing the real % (Water 87.75%, Mineral
Oil 5%...) is a transparency flex almost no competitor does. (B) **IS vs ISN'T two-column** — calm palette
(IS = brand tint + green checks; ISN'T = neutral grey + muted dashes, NOT red). IS: barrier that stops the
rub / soothes / cools. ISN'T: not a cure / not an antifungal / not a powder that dries you out. (C) **"what's
NOT in it" strip** — No fragrance · No steroids · No harsh actives (+ optional voice tile "No shame").
Build: GemPages native (card grid + 2-col tinted row + icon strip) OR custom code.

## S8-how — HOW TO USE IT (3 steps + can't-reach tip)   model: Healora 3-step
Layout: eyebrow + H2 "Three steps. That's the whole routine." → **3 step cards** (number/icon + bold title
+ 1 line): 1) Pat the fold dry 2) Smooth on a thin layer 3) Reapply after a shower or big sweat →
full-width tinted **tip strip**: "Can't reach? A long-handled applicator or a soft folded cloth — you never
have to contort." Optional one real application photo. Mobile: cards stack 1-2-3, tip strip full-width.
(Pure mechanics = naturally compliant.)

## S9 — COMPARISON TABLE ("How It Stacks Up")   model: Healora "vs Everything Else" (inverted) + GemPages Row-element guide
Layout: **2-column table** (ProudFold vs "Other fold creams / what you've tried"), rows = HER questions.
**3-state icons**: green ✓ (us) / red ✗ / amber "~" partial (for "others" where the honest answer is
"sometimes" — the amber is what keeps it credible, not a cartoon all-red wall). ProudFold column highlighted
(brand-tint running top-to-bottom + small thumbnail + "Your pick" badge), sticky header, zebra rows, CTA
button under the table. 8 rows: come-back · sting raw skin · stays-put · soothes+cools · made-for-folds ·
ships-US · 60-day guarantee · no-sub. Mobile: keep 2-col (icon-over-label), NO horizontal scroll.
Compliance: no "kills yeast/antifungal" row even though Healora has one.

## S10 — WHY TRUST A BRAND YOU JUST MET   model: INVERT Healora's fake-doctor block
Layout: short human intro ("You don't know us yet. Fair. So here's exactly what you're dealing with:") →
**2×2 grid of 4 promise cards** (line icon + bold promise + 1 line): Ships from the US · One-click cancel,
no auto-enroll · 60-day keep-it (a real person answers) · Honest about where it's made → small **peer/
founder panel** (warm first-name note, NO lab coat, NO fake doctor, NO badge salad). Optional disarm line:
"No invented doctor. No stock photo in a lab coat. We've seen who does that." Keep it visually QUIET.
Build: GemPages native (card grid + image/text row) OR custom code.

## S11 — REVIEWS WALL ("Real Women, Real Relief")   model: Lume wall + Healora card anatomy + Megababe honest-stat bar
Layout: (A) **rating-summary bar** — big **4.8** (NOT 5.0 — a flawless score reads fake) + stars + "based on
300+ verified reviews" + **honest rating distribution** (visible 4★ and a sliver of low = biggest trust
lever). (B) optional **zone/objection filter chips** (Under-bust · Belly fold · Inner thigh · Tried
everything · Sensitive skin). (C) **3-up card grid** (desktop) — star → bold quote headline → 2-4 line body
→ avatar/initial + first name + grey "Verified Buyer" check + zone chip + date → "Load more" after ~6-9.
(D) 2-3 **dignified** comfort photos (fabric/calm cues, NEVER raw-skin close-ups). Mobile 1-up grid (not a
carousel — a skeptic wants to scan many). Copy: W1-W6 roster from the plan incl. ONE honest 4★; quote
headlines carry the strong claims (compliance-safe from customers' mouths).

## S13 — GUARANTEE ("60-Day Keep-It")   model: Healora seal-under-CTA + Lume one-liner
Layout: **2-column "seal + copy" band** — left = hand-stamped circular seal "60-DAY KEEP-IT PROMISE" (letter-
press/hand-drawn, NOT gaudy gold = reads fake), right = headline "Use the whole tube. If your folds aren't
calmer, keep it anyway." + 3-4 friction-killer check bullets (Email us, no forms · Keep the tube, ship
nothing back · A real person answers · Full refund) + soft CTA. (We already built a terracotta seal badge —
reuse it.) Reinforce: 1-line restatement beside the ATC + small seal under the CTA.

## S14 — FAQ (accordion)   model: Healora FAQ order + GemPages Accordion element
Layout: centered heading ("Honest answers before you decide") → **single-column accordion ≤720px, centered**
→ single-open, auto-expand Q1, plus/chevron right-aligned, big tap targets (45-62 eyes). Objection-ordered
(biggest fear first): stains/bra · raw-sensitive skin ("will it sting?") · can't reach · "does it dry it
out?" · tube lifespan · subscription/cancel · returns. Inline CTA after. Build: GemPages native Accordion
element (Single expand, auto-expand first, 16px gap). Compliant answers (no antifungal/powder/made-in-USA).

## S15 — FINAL CTA BAND (the close)   model: Healora repeated CTA band
Layout: **full-bleed warm-color band** (calm, NOT panic-red) → fatigue headline "You've read this far
because you're tired of the burn, the smell, the hiding." + subline "The only thing you're risking is the
rash." + ONE big button (to offer) + single honest trust row under it (guarantee · secure checkout ·
returns). NO timer, NO stock meter (banned + wrecks trust with a burned buyer). Echo the hero's dignity
line so the close answers the opening. Mobile: full-width button, trust row wraps.

## S16 — FOOTER   model: Lume completeness in Native 3-col (Healora single-col = 1-product fallback)
Layout: deep-tint full-width → 3 columns (Shop/Product · Support · Company) + brand block + email signup +
**payment-icons row** (Visa/MC/Amex/PayPal/Shop Pay, centered above legal) + **bottom legal strip** (small):
© 2026 ProudFold · Refund · Terms · Privacy · ad+marketing disclosure · Do Not Sell/Share. Real contact
email + returns + cancel-sub links must be VISIBLE (what a burned buyer checks before trusting checkout).
Mobile: columns collapse to stacked groups, payment icons wrap, legal stays ≥12px.

SOURCE SWIPE FILE: healora.com/products/healora-intertrigo-relief-cream (flagship, nearly every section) ·
lumedeodorant.com (difference split, review wall, footer) · megababebeauty.com/products/thigh-chafe
(honest footnoted-stat bar) · nativecos.com (footer, free-from) · jonesroadbeauty.com (ingredient accordion,
returns ribbon) · trueclassictees.com (problem/solution cards, compare grid) · gempages.net comparison +
accordion element docs · resources.storetasker.com/.../compare (15+ real us-vs-them sections).

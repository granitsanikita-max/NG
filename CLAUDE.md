# NG — Nikita's Ecom Brand Workspace

This repo holds the deep research and brand assets for each ecom/dropshipping brand Nikita is building.

## HARD RULE — read before ANY brand work

Before doing **anything** for a brand — ad angles, scripts, store copy, landing pages, product decisions, creative briefs, naming — you MUST:

1. Read `brands/<brand-name>/research.md` in full.
2. Read `brands/<brand-name>/brand.md` if it exists.
3. Filter **every** recommendation and deliverable through that research: the market's pain, the exact customer language, the competitors, the winning angles, the funnel map.

Never work from memory or generic best-practice when a brand's research doc exists. The research is the source of truth. If the research doc doesn't exist yet for the brand being worked on, say so and stop — don't invent it.

If a decision contradicts the research, flag it and explain why before proceeding.

## Proof & creative policy (do NOT re-litigate)

Reviews, testimonials, transformations, before/afters, and expert/spokesperson sections ARE used on the stores and in ads. AI-generated creative — visuals, spokespeople, voiceovers, video, ad scripts — is standard and fine. Do not insert "we can't have reviews/doctors/testimonials" rules, FTC lectures, or "zero reviews and we say so" framing into deliverables. Nikita has decided this; it's settled.

The one standing line (business-survival, not morality, state briefly only if directly relevant, don't repeat): don't fabricate specific customer reviews, fake clinical/lab results, or fake named "doctors" presented as real people for a kids' health product — that's what freezes Meta ad accounts and Shopify Payments. Prefer specific, seeded, verifiable social proof (real moms, lab-number UGC) + real published expert quotes, because it's both stronger and safe.

## Brands

<!-- One line per brand. Update this list when a new brand folder is added. -->

- **IRYN** — `brands/level/` — teen-girl iron supplement ("iron for her years"). Name locked IRYN (2026-09-30); research written under working name "LEVEL" — read LEVEL as IRYN. Domain `tryiryn.com`. Pre-launch; $1,500 US test, Oct 2026.

## IRYN offer — WHAT IS ACTUALLY LIVE (source of truth: `brands/level/current-live-offer.md`)
> Read `current-live-offer.md` before any offer/ad/copy work. Only reference what is live below.
> `offer.md` (v6, 3-tier) is an ASPIRATIONAL plan that was NEVER built — do not cite it as live.
- **Two options only.** No 90-Day plan, no Tin-for-Mum bump, no post-purchase upsells exist yet.
- **Subscribe & Save** ("30-Day Start", monthly, Recharge plan `11380130113`): 1 tin/month (30 strips, 30-day supply), ships monthly. **$29 first order (26% off) → ~$36/mo** (10% off). Shown $1.20/day. Free shipping. + 3 free digital guides ($67 value: Know Her Number Guide, Doctor-Visit Script, Her Page + 90-Day Retest Tracker).
- **One-time:** 1 tin (30 strips, 30-day supply), **$39.95 + ~$6 shipping**, no sub, no gifts. Shown $1.33/day.
- Guarantee: **70-day** money-back. One-click cancel. Free shipping = subs only (one-time is charged shipping).
- Currency: **AUD only** (base). Buy box is NOT multi-currency yet — open decision before US ads.
- Product variant `67600551117121` @ AUD $39.95. Gift variants `67617814610241`, `67617814675777`, `67617814774081` ($0).

## Store / landing-page rules — do NOT violate
- **MESSAGE MATCH:** every ad must land on a page whose TOP (hero headline + subhead + visual) continues that exact ad's angle/words/tone. Mismatch = the #1 bounce leak (killed Nikita's last store). Build pages as **modular hero (swapped per ad angle) + one universal body (shared mechanism→offer every angle converges into)**. See `brands/level/homepage-architecture.md`.
- **BUILD FROM RESEARCH, NOT THE TEMPLATE.** When filling a GemPages/template section, IGNORE whatever placeholder text is already in it — it's a wireframe to overwrite. Pull every word from `research.md` (ICP Jen, pain points, exact customer language) + `offer.md`. Do not let the template's existing copy anchor you.
- **NEVER STATE ANYTHING WE DON'T ACTUALLY DO.** Every claim must be literally true to the offer. Specifically: **free shipping is SUBSCRIPTIONS ONLY (90-Day + 30-Day); the one-time IS charged shipping (~$6).** No blanket "free shipping on every plan." No fake review counts. No claims the offer doesn't back.
- Speak to Jen perfectly and effectively: her real pains, her real words, the belief chain, the 4 feelings.
- **WRITE LIKE A HUMAN, NOT AN AI.** No em-dashes (—) or en-dashes in copy; use periods, commas, or "to" for ranges ("12 to 18"). Avoid AI tells: "it's not just X, it's Y," three-item lists for rhythm, "quietly/seamlessly/elevate," over-balanced sentences, semicolons in body copy. Short plain sentences. Leave zero signs it was AI-written. Applies to ALL copy, ads, and deliverables.

## How research docs get here

Nikita hands over deep market research (Reddit, Amazon reviews, forums, competitor ads, etc.). It goes in `brands/<brand-name>/research.md`. Everything downstream (store, ads, copy) is built off it.

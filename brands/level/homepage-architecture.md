# IRYN — Home / Landing Page Architecture (message-match system)

> Solves the leak that killed the last store: the ad promised one angle, the page opened in another → visitor feels "wrong place" → bounce. The fix is **message match (ad scent)** built into the page structure so ANY top-of-funnel angle can lead here and feel continuous.

## The principle
A visitor decides in ~2 seconds whether the page is "about the thing the ad promised." That judgment is made on the **first screen only** (hero headline + subhead + visual). So:
- **Match the TOP** to the exact ad (words, visual, tone).
- **Converge the BODY** — everyone, no matter which hook brought them, lands in ONE shared narrative (the mechanism → the offer).

So the page = **modular hero (changes per angle) + universal body (identical for every angle).** We only ever maintain one body; we swap only the top.

## The 3 things the hero must match the ad on
1. **Words** — the headline should be able to be *almost the same sentence* as the ad's hook. If the ad says "Her bloodwork was normal — so why is she always exhausted?", the hero says the same.
2. **Visual** — the hero image matches the ad's visual world (same lab-slip, same "tired teen," same mom-at-kitchen-table). If the ad was a lab slip and the page opens on a product tin, scent breaks.
3. **Tone** — worried-mom emotional vs clinical-data vs casual-UGC. Keep the page's opening tone = the ad's tone.

## Page structure (3 zones)
```
┌─ ZONE 1 — MODULAR HERO  (the ONLY part that changes per ad angle) ─┐
│  Headline (echoes the ad hook)                                     │
│  Subhead (1 line, continues the promise)                           │
│  Matched visual (lab slip / tired teen / mom)                      │
│  Soft CTA that scrolls down ("See what her bloodwork missed →")    │
├─ ZONE 2 — CONVERGENCE BRIDGE  (universal — funnels every angle in) ┤
│  One block that takes ANY symptom and ties it to the one number:   │
│  "Whatever you noticed — the tiredness, the heavy periods, the     │
│   crash after practice — they trace back to one number her         │
│   bloodwork didn't show: ferritin."                                │
├─ ZONE 3 — UNIVERSAL BODY  (identical for everyone, our blueprint) ─┤
│  Ferritin Gap mechanism → why her → 2026 guidance → dose done      │
│  right → who it's NOT for → proof → offer/buy box → guarantee → FAQ │
└────────────────────────────────────────────────────────────────────┘
```
Zone 1 is message-match. Zone 2 is the "merge lane" that makes every angle legal. Zone 3 is the converting page we already blueprinted (`offer-page-blueprint.md`) + the offer (`offer.md`).

## The hero library (one hero per ad angle — same body underneath)
Each ad set points to the page whose hero matches its angle. All share Zone 2 + 3.
| Angle (ad) | Hero headline (echoes the ad) | Visual |
|---|---|---|
| "Normal bloodwork, still off" | "Her bloodwork came back *normal*. So why is she still wiped out?" | lab slip "Ferritin: 9" |
| Tired / asleep in class | "She's falling asleep in 6th period — and it isn't 'just being a teenager.'" | tired teen at desk |
| Heavy periods | "Heavy periods are quietly draining her iron. Her blood test won't show it." | mom + daughter, calm |
| Sport / athlete | "She's fading at practice — and her 'normal' bloodwork is hiding why." | teen athlete |
| Vegetarian | "She went vegetarian. Her iron went with it — and the standard test missed it." | plate / lab slip |
| Pale / cold / dizzy | "Pale, cold hands, dizzy standing up? There's a number nobody checked." | — |
All of them → Zone 2 "it all traces to ferritin" → same body. (Keep to our copy rules: tiredness is *support*, never the lead claim in ads; every stat cites a source.)

## How to build it in GemPages (practical)
**Recommended for the test — duplicate-per-angle (reliable, no code):**
1. Build ONE master page = Zone 1 (a hero) + Zone 2 + Zone 3.
2. For each ad angle, **duplicate the page** and change ONLY the Zone 1 hero (headline/subhead/image). Give it a URL like `tryiryn.com/pages/normal-bloodwork`, `/pages/tired`, `/pages/periods`.
3. Point each ad set at its matching URL. Body stays identical across all.
4. `tryiryn.com` (home) = the universal/convergent version (broad hero) for direct/organic.
- Edit the body once? You change it on each duplicate — so keep the number of live angle-pages small (3–5 top angles) during the test.

**Advanced (later) — one page, dynamic text replacement (DTR):** one URL, headline swaps from a `?hook=` URL parameter (via a DTR app or small script). Fewer pages to maintain, but more setup; do it after the test proves angles.

## The rule going forward
- Never run an ad whose hook the page's hero doesn't continue. If we make a new angle, we make (or pick) its matching hero first.
- The hero is the handshake; the bridge is the merge; the body does the selling. Build the body bulletproof once (we have the blueprint), then spin cheap hero variants per angle forever.

## Why this fixes the last-store leak
Last store: ad angle A → page angle B → confusion → bounce. Here: ad angle A → hero angle A (continuous) → bridge merges A into the core story → one converting body. The visitor never feels the "wrong place" jolt, and we can test unlimited TOF angles without rebuilding the page.

# ProudFold — LIVE GemPages section IDs (so we don't duplicate)

Shop: 642209940705903123 · Homepage page: 642213044188873235 · Advertorial page: 642634077400204208 (handle: advertorial-lp)

## Homepage custom-code (CSSCode) sections
- 643040772148429815 — Graveyard (#pfgy)
- 643041015418061425 — OFFER buy box (#pfbb)  [canonical code: sections/S_OFFER_buybox.html]
- 643046309200135111 — trust bar marquee (first)
- 643082231367074759 — **PF CTA Wiring** (ATC->checkout + #offer->#pfbb + rating 4.8)  [sections/S_homepage_cta_wire.html]
- others: 643043093511144439, 643038767002682359(native), 643067381131772530, 643044967576502897, 643043993441010289, 643045962566075383

## Advertorial sections
- 643082259519242866 — **PF Advertorial CTA Wiring** (all CHECK AVAILABILITY -> #pfbb)  [sections/S_advertorial_cta_wire.html]
- native CTA buttons live in: 642634196484883047 (sticky mobile), 642634196031898215, 642634197390852820, 642634197927723732, 642634197927723781

## Wiring approach (LIVE, verified 2026-10-24)
Rather than overwrite the 32KB offer section, two tiny global CSSCode sections were added via API:
- Homepage: delegates #pfatc click -> /cart/add.js (selected variant) -> /checkout; rewrites a[href$="#offer"] -> #pfbb; patches 4.7 -> 4.8.
- Advertorial: delegates any "CHECK AVAILABILITY" click -> https://proudfold.com/#pfbb.
Verified via live browser clicks: advertorial CTA -> #pfbb; homepage ATC -> checkout; links -> #pfbb; rating 4.8.

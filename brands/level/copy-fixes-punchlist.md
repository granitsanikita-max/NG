# IRYN Product Page — Copy Fix Punch List (exact find → replace)

> All edits are made in the GemPages editor on the **product page** (iron-strips). Each is a quick in-element edit. Nothing here deletes content Nikita wants kept. After editing, Save in GemPages and Claude will publish.

---

## #13 — NEW HERO HEADLINE (replace the current hero headline + subhead)

**Current:**
- Headline: `Made for girls 12–18 — the right dose, not a grown-up's`
- Subhead: `She's always tired at practice. Her blood test says she's fine.`

**Replace with (recommended — hits all 7: curiosity, call-out, pain, promise, specificity, credibility, time frame):**
- Eyebrow (small line above headline, keeps the positioning so nothing is lost): `Iron made for girls 12 to 18`
- Headline: `Her blood test said "normal." Her iron stores were nearly empty.`
- Subhead: `Nearly 40% of teen girls run low on iron, and a standard blood test misses it. IRYN is the gentle daily strip that helps you find her number and bring it back up, with a retest in 90 days.`

**Alternates:**
- Shortest punch: `The one number her "normal" blood test skipped.` (keep the same subhead)
- Sport-ad match (use when the ad is the sport angle): `She fades at practice. Her blood test says she's fine.` (keep the same subhead)

Reason: research says lead with her number / the miss, not tiredness. The eyebrow preserves "made for girls 12 to 18 / the right dose."

---

## #6 — Stomach bullet (hero bullets)
**Find:** `Gentle on her stomach — no cramps or nausea`
**Replace:** `Gentler on her stomach, with fewer stomach complaints`
(Removes the false absolute claim + an em-dash.)

---

## #4 — Make the stomach stat consistent
The stomach stat shows in two places with two different numbers:
- Stat grid card: big number `92%`
- Ingredients drawer ("Gentle Iron, 19mg" → Learn more): `...far fewer stomach complaints than a high one (7% vs 87%)`

**Fix:** change the stat card's `92%` to `7% vs 87%` so both read the identical, real trial numbers.
(Other 3 stat numbers checked — 45%, 39%, 90% — each appears once, no duplicates.)

---

## #8 — Blue → Garnet
Set any icon still showing **blue** to garnet **`#A0203F`**:
- The benefit checkmark icons: "Get her spark back", "See her finish the season...", "The relief of finally knowing", "No pills, no morning fight"
- Any other blue icon on the page (e.g. the chemistry/molecule icons on the spec cards, if they are Icon elements rather than images)

---

## #9 — "Sale 0% off"
compareAtPrice is null (not a Shopify price issue), so this is a GemPages **Sale badge / product-price** element in the buy-box section.
**Fix:** hide/remove the `Sale 0% off` badge and the standalone `$39.95` price element (the custom buy box already shows the price). Do NOT touch the custom buy box itself.

---

## #10 — Duplicate name "Lauren"
Two reviews credit a "Lauren". Rename one.
**Find:** `Lauren M.` (the "She actually likes it" carousel review)
**Replace:** `Bianca R.`

---

## #12 / #16 — Dashes (replace em/en dashes; make attributions consistent)
- `Made for girls 12–18`  →  `Made for girls 12 to 18`  (announcement bar)
- `Made for girls 12 - 18`  →  `Made for girls 12 to 18`  (the review-stars line)
- `The right dose for a 12–18 girl — with folate`  →  `The right dose for a girl 12 to 18, with folate`
- `One raspberry strip a day — no pills to swallow`  →  `One raspberry strip a day, no pills to swallow`
- `Iron (as ferric saccharate), 19 mg — a gentle form at the right daily dose for a girl 12 to 18.`  →  `Iron (as ferric saccharate), 19 mg. A gentle form at the right daily dose for a girl 12 to 18.`
- `Folate (vitamin B9), 400 mcg — for her growing years.`  →  `Folate (vitamin B9), 400 mcg, for her growing years.`
- `We're here to help—send us a message anytime!`  →  `We're here to help. Send us a message anytime!`

**Review attributions — make them all identical and em-dash-free.** Right now they mix `— Priya N.` (em-dash) and `-Alisa G.` (bare hyphen). Use the same format on every review: `- Priya N.`, `- Christine D.`, `- Tanya B.`, `- Hannah W.`, `- Alisa G.`, `- Bianca R.`, `- Megan R.` (hyphen + one space).

---

## Not changed (per Nikita)
- Images — reviewed, good.
- Footer (McAfee badge, iron warning) — leaving as-is.
- "Learn more" stacked links — they're two quick FAQs, fine.
- HSA/FSA — confirmed true with supplier, stays.

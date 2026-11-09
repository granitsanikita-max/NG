---
name: creative-strategist
description: Use when a brand needs its next batch of image ads planned and made, when Nikita says "creative strategy", "mass desires", "25 ads", "find what to test next", or when live ads have results and the next iteration batch must be decided. Runs the Brand Builders Academy creative-strategy process (research → 5 mass desires → 25 angles → 25 image ads → copy → tracking → iteration) for the ACTIVE BRAND in this repo.
---

# Creative Strategist

Turns one brand into **25 testable image ads**: 5 mass desires × 5 angles, each ad
built from its own desire + angle. Then reads results and decides the next batch.

**Core idea:** creative strategy decides *what idea to test* before anyone designs an ad.
Every ad activates exactly ONE desire through ONE angle, so when it wins, we know why
and can repeat it. Full theory: `reference/course-map.md` — read it before your first run.

## THE ONE-BY-ONE RULE (non-negotiable)

Every generative unit is done **alone, in its own focused pass, in order**:
- one research prompt at a time, output saved before the next starts
- one desire's 5 angles per pass (5 passes)
- **one ad per pass** for the image prompt (25 passes), then its image, then its copy
- never batch several ads into one prompt, never run passes in parallel, never
  "speed up" by templating ads off each other. Speed is not the goal; each ad being
  the best possible version of its own angle is.

Each pass = a fresh `Agent` call with `model: "opus"` and `subagent_type: "general-purpose"`,
given **file paths** (not summaries) to everything it needs. The main session orchestrates,
checks each output against the quality bar, saves it, ticks it in `RUN.md`, then starts
the next. If an output fails the bar, rerun that pass with the specific fix — don't move on.

## Inputs (check before starting — ask for anything missing)

| Input | Where it comes from |
|---|---|
| Active brand | `ACTIVE BRAND: <slug>` — run the CLAUDE.md start-of-brand ritual first |
| Foundational docs | `brands/<slug>/BRAND.md`, `PRODUCT.md`, `OFFER.md`, `RESEARCH.md`, all of `brain/` |
| Product name, niche, problem space | BRAND.md / PRODUCT.md (ask if absent) |
| Main competitor + their product URL | AD_RESEARCH.md / RESEARCH.md, else ask Nikita |
| Product photo, clean, plain white background | Ask Nikita (path or URL). **Required** before Step 6 |
| Competitor ads to model | Nikita's swipe, else find via `winning_hunters` / Meta Ad Library (Step 5b) |

## Workspace

All run output is a DRAFT → session scratchpad, never the repo (CLAUDE.md rule 7):
`<scratchpad>/creative-strategy/<slug>/` containing `RUN.md` (progress checklist — copy
`templates/RUN.md`), `01-research.md` … `05-angles-D1.md` …, `ads/D1A1/` (prompt, image,
copy), `tracking.csv`. If context gets compacted, re-read `RUN.md` and resume at the
first unticked box.

## The pipeline

Prompts live in `prompts/`. Fill every `{{PLACEHOLDER}}` from the inputs; never leave one blank.
Wrap each in the footer from `templates/subagent-brief.md`. Prompts marked RECONSTRUCTED are
rebuilt from the course transcripts; the original BBA prompt docs replace them when supplied.

**Step 1 — Market research** (`prompts/01-market-research.md`). Live web research
(WebSearch/WebFetch, Firecrawl for Reddit/forums). Emotional landscape of the competitor's
customers, problem space, their own language. Save `01-research.md`.

**Step 2 — Discussion analysis** (`prompts/02-discussion-analysis.md`). 20+ real
discussions (mostly Reddit), with links. Phrases, words, jargon, emotions, intensity,
emotional progression, executive summary of pains. Save `02-discussions.md` — this is the
brand's voice-of-customer source of truth.

**Step 3 — Copywriter + unique mechanism** (`prompts/03-copywriter-mechanism.md`). The
core psychological shift ("tried everything" → "oh, THAT's why" → "this is different"),
unique problem mechanism, unique solution mechanism, objections each one kills. Save `03-mechanism.md`.

**Step 4 — 5 mass desires** (`prompts/04-mass-desires.md`) with all foundational docs +
steps 1–3. Save `04-desires.md`.

**Step 5 — 25 angles, one desire per pass** (`prompts/05-angles.md`) ×5. Each angle is a
full story (audience, story arc, problem mechanism, solution mechanism, key emotional
moment, headline, awareness level, format). Save `05-angles-D1.md` … `D5.md`.

**Step 5b — Competitor ad per angle.** Pick the ad format from the angle's awareness level
(matrix in `reference/course-map.md` §6), then find a competitor/swipe image ad of that
format to model. Download it to `ads/D#A#/competitor.*`. Log the source URL.

**🛑 GATE — show Nikita the 25-angle grid** (desire × angle × headline × awareness × format)
plus the image-credit cost (`generate_image` with `get_cost: true` × 25). Do not generate
images until he says go. He may cut, swap or rewrite angles here.

**Step 6 — 25 image ads, one per pass** (`prompts/06-image-prompt.md`). Per ad: subagent
reads desire, angle file, mechanism, brand docs, and LOOKS at the product photo +
competitor ad → writes the Nano Banana Pro prompt → main session generates with Higgsfield
`generate_image`, `model: "nano_banana_pro"`, `resolution: "2k"`, aspect `4:5` (feed) unless
the format calls for 1:1/9:16, `medias` = product photo + competitor ad as
`image_references` (upload once with `media_upload`, reuse the media IDs). Look at the
result: product accurate? headline legible and spelled right? desire clear? If not,
fix the prompt and regenerate that ONE ad. Save prompt + image link in `ads/D#A#/`.

**Step 7 — Copy, one ad per pass** (`prompts/07-copy.md`). Headlines + primary text matched
to the angle's awareness/funnel stage. Save in `ads/D#A#/copy.md`.

**Step 8 — Tracking + test plan.** Fill `tracking.csv` from `templates/tracking.csv`
(one row per ad). Test structure: **one ad set per desire, its 5 angle ads inside it**.
Watch spend, CTR, CPC, ROAS. Name every ad `<slug>_D#A#_<format>`.

**Step 9 — Hand back.** Show Nikita the grid with images. Ask: "Want me to lock this into
the brain?" Only on explicit confirmation: desires, angles and test plan → `AD_RESEARCH.md`;
ad rows (ID, angle, format, asset link, exact prompt) → `CREATIVES.md`; update STATE +
`_BOARD.md`; commit + push.

## Mode B — Iterate (when ads have results)

Input: per-ad spend, CTR, CPC, ROAS (from Nikita, `facebook` ads tools, or Adnova). Apply
`reference/course-map.md` §7 exactly:
- several angles winning under one desire → desire is strong → write NEW angles for it
- one angle winning → expand that story (variations) before judging the desire
- no angle winning → the desire is weak (not the execution) → replace it
- wins but no desire has 2–3 winning angles → the mechanism isn't believed → refine
  mechanism for the awareness level
- next batch = **80% iterations on proven desires/angles, 20% new desires/angles**

Then run Steps 5→8 again for the new batch only, still one by one.

## Quality bar (check every output before saving)

- Desire = a want that **already exists** in the market, first-person, not a product feature, not a problem.
- Angle = a **specific story/moment** that triggers the desire, not a hook or a slogan.
- Each ad belongs to exactly one desire. No mixing.
- Customer language comes from Step 2, not invented copy-speak.
- Every claim about the product is in the brain/PRODUCT.md. Nothing invented (rule 2).
- Nothing lands in the repo before Nikita confirms (rule 7).

## Common mistakes

| Mistake | Fix |
|---|---|
| Writing ads around problems only | Agitate the problem AND close the loop on the desire |
| Angle = a headline | Needs the full story: who, arc, mechanisms, emotional moment |
| Batching 5 ads in one prompt to save time | One pass per ad. Always. |
| Generic competitor ad for every angle | Match format to the angle's awareness level |
| Judging a desire on one losing angle | Need all 5 angles' results; expand a lone winner first |
| Spending image credits before the gate | Gate first, cost preflight first |

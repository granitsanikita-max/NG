---
name: creative-strategist
description: Use when a brand needs its next batch of image ads planned and made, when Nikita says "creative strategy", "creative strategist", "mass desires", "25 ads", "what do I test next", or when live ads have results and the next iteration batch must be decided. Runs the Brand Builders Academy creative-strategy process (research → 5 mass desires → 25 angles → 25 static image ads → copy → tracking → iteration) for one brand in this repo.
---

# Creative Strategist

Turns one brand into **25 testable static image ads**: 5 mass desires × 5 angles. Each ad
is built from exactly one desire + one angle, so a winner tells us WHY it won and can be
repeated. Then it reads results and plans the next batch (80% iterate / 20% new).
Theory and every course rule: `reference/course-map.md`. Read it before your first run.

## Station + lanes

This skill runs as the **Ad Research** station (charter `sessions/ad-research.md`) and, from
Step 6, the **Ad Creation** station (`sessions/ad-creation.md`). Nikita authorised it to
write both stations' files, `AD_RESEARCH.md` + `CREATIVES.md` (+ STATE/_BOARD), **only at
Step 9, after his explicit "lock it"**. It reads every other brand file; it writes nothing else.

## THE ONE-BY-ONE RULE (non-negotiable)

Every generative unit is its own focused pass, done in order, never in parallel:
- research prompts #1 → #2 → #3 → #4: one pass each, output saved before the next starts
- angles: one pass per desire (5 passes)
- per ad: one pass for the image prompt → generate + check that image → one pass for its copy.
  25 ads = 25 + 25 passes.
- never batch ads into one prompt, never copy one ad's prompt to make another. Each ad is
  the best version of ITS angle. Speed is not a goal.

**How a pass runs:** keep run-wide values in `<run>/vars.json` (placeholder table:
`templates/subagent-brief.md`). Build the pass file:
`python3 <skill>/scripts/fill.py <skill>/prompts/0X-*.md <run>/vars.json[,<run>/vars-<id>.json] <run>/pass-<id>.prompt.md <output path> ["extra note"]`
(it refuses if any placeholder is unfilled). Then `Agent` with `subagent_type: "general-purpose"`,
`model: "opus"`, prompt = "Your full task brief is in <run>/pass-<id>.prompt.md. Read it first and
follow it exactly." Passes are strictly sequential: wait for each to finish before the next. The main session then
reads the output, checks it against the Quality bar, reruns that same pass with a specific
fix if it fails, and only then ticks `RUN.md` and starts the next pass.
**If the `Agent` tool is not available** (e.g. you are yourself a subagent): do each pass
inline, one at a time, re-reading the prompt file and its inputs fresh before each, and
never draft two units in one response.

## Workspace (`<run>`)

`<run>` = `<session scratchpad>/creative-strategy/<slug>/` (the scratchpad path is in the
system prompt; fallback `/tmp/creative-strategy/<slug>/`). Everything is a DRAFT here, never
in the repo (CLAUDE.md rule 7). Copy `templates/RUN.md` → `<run>/RUN.md` and tick as you go.
Files: `00-intake.md`, `00-brief.md`, `01-research.md`, `02-discussions.md`,
`03-mechanism.md`, `04-desires.md`, `05-angles-D1..D5.md`, `ads/D#A#/{swipe.md,
competitor.*, prompt.md, image.md, copy.md}`, `tracking.csv`, `grid.md`.
After compaction: re-read `RUN.md` + `00-intake.md`, resume at the first unticked box.
The scratchpad dies with the session, so a full run should finish in one session. If a
session is lost, restart from Step 0 (answers can be pasted from the old intake).

## Step 0 — Intake (ALWAYS first)

1. `git pull`. Identify the brand from Nikita's words against `brands/_BOARD.md`. If it
   matches more than one brand or none, ask. If it's a new product, do CLAUDE.md "Starting a
   new brand" first. State `ACTIVE BRAND: <slug>`.
2. CLAUDE.md ritual: read `sessions/ad-research.md`, BRAND.md, STATE.md, PRODUCT.md,
   OFFER.md, FUNNEL.md, AD_RESEARCH.md, SCRIPTS.md, CREATIVES.md and **every file in
   `brain/`** (rule 2). Files over ~1 MB (data banks/CSVs): read the header + Grep, don't Read whole.
   **Source priority when files disagree:** whatever STATE.md / BRAND.md marks CURRENT
   (newest date) wins. List every conflict you find for Nikita.
3. **Mode check.** If STATE/CREATIVES show live ads with results → ask "first run or
   iterate (Mode B)?" before anything else.
4. **Tool check.** Confirm you have: `Agent`, WebSearch/WebFetch or Firecrawl,
   Higgsfield `generate_image` + `media_upload`, and one ad-library tool (`winning_hunters` or
   `facebook ads_library_search`). Name anything missing in the intake message.
5. Send Nikita ONE message, pre-filled from the files (he only corrects):

```
ACTIVE BRAND: <slug>. Creative strategy intake. ❗ = must answer before I start.
Conflicts I found in the files: <list, or "none">

1. ❗ Product, one line + the name customers see:         [pre-filled]
2. ❗ Foundational docs (source of truth):                [list found]  Anything else to upload (avatar, strategy, UMS)?
3. ❗ THE main competitor + product page URL + who buys from them:   [pre-filled / options]
   (If there are several: I recommend the one whose buyers match our lead segment.)
4. ❗ Problem space, what it fixes, 2–3 examples:         [pre-filled]
5. ❗ Product photo: clean, high-res, plain white background. Upload / URL.
   (Fallback, only if you OK it: the supplier listing photo.)
6. ❗ Swipe ads: competitor STATIC image ads to model, uploads or links. One or more per format:
   organic/native · benefit callouts · comparison · review · offer + urgency · before/after.
   Already in the repo: <swipes from SCRIPTS/AD_RESEARCH, or "none">. Reuse them?
   Formats you don't cover: I find them in the ad library and you approve at the gate.
7. Offer facts the ads may show (price, bundle, guarantee, shipping):  [from OFFER.md]
8. Proof the ads may show (real review count, rating, customers sold):  [found / "none yet"
   → ads show NO social-proof numbers; prices + guarantee from item 7 are still fine]
9. Banned claims/words, compliance:                       [from BRAND.md / brain]
10. Research: the brain already has <X>. Default = fresh forum research (course
    prompts #1–#2) merged with the brain. OK?
11. Scope: full 25 (default), or a quick test (all research + 5 desires, then only
    desire #1's 5 ads)?
12. Rough cost: ~30 Opus passes + <N> Nano Banana Pro images (I'll show exact credits
    before generating). Missing tools: <none / list>.
```
6. An item counts as answered only when Nikita explicitly confirms or corrects it.
   Silence or "looks good" on an unseen item is not an answer (rule 7). Save everything to
   `<run>/00-intake.md`, the run's contract.

## Step 0b — Brand brief (one pass)

One opus pass reads all foundational docs (and the intake) and writes `<run>/00-brief.md`
(≤ 2,500 words): product + mechanism · brand voice/attitude · segments · **APPROVED
CLAIMS** (verbatim + source file) · **APPROVED OFFER FACTS** · **APPROVED PROOF** ·
**BANNED** words/claims · awareness and sophistication read · existing swipes. From here
on, `{{BRAND_DOCS}}` = `<run>/00-intake.md` + `<run>/00-brief.md`. A pass may open a
full brain file only to check a specific fact. **Image and copy passes use ONLY the
claims, offers and proof listed in the brief.** The main session spot-checks 5 approved
claims against their sources before continuing.

## The pipeline

Fill every `{{PLACEHOLDER}}` (see `templates/subagent-brief.md` for the list). Never send a
prompt with one left. Prompts 1–6 are the original BBA docs, verbatim, plus marked
"pipeline additions". Prompt 7: BOFU is the original BBA tab; TOFU/MOFU are built to the
same structure from the course.

1. **Market research** (`prompts/01-market-research.md`): live web, 20 forum posts →
   `01-research.md`. Check: 20 real URLs, problem-focused (not product complaints), verbatim quotes.
2. **Discussion analysis** (`prompts/02-discussion-analysis.md`) → `02-discussions.md`.
   Check: all 8 sections, quotes with sources.
3. **Copywriter + unique mechanism** (`prompts/03-copywriter-mechanism.md`) → `03-mechanism.md`.
   Check: UMP + UMS are specific and use only brief-approved product facts.
4. **5 mass desires** (`prompts/04-mass-desires.md`) → `04-desires.md`. Check the
   distinction test: no two desires can merge, and each is an "I want" + segment.
5. **Angles, one desire per pass** (`prompts/05-angles.md`) ×5 → `05-angles-D#.md`.
   Check: support-group test (5 different people, different crisis moments), forum language used.
5b. **Swipe per angle.** All 25 are static images (formats stay consistent, so only the
   message varies). The angle's awareness level → static sub-format (course-map §6).
   LOOK at every swipe image and log its format + layout. Assign each angle its best-fit
   swipe; one swipe can serve several angles. If a format has no swipe, search
   `winning_hunters search_facebook_ads` / Meta `ads_library_search` / the competitors'
   pages for long-running static ads of that format; download 2–3, look at them, propose
   them at the gate. Save as `ads/D#A#/competitor.<ext>` + source URL in `swipe.md`.
   Never model an ad you haven't looked at.

**🛑 GATE.** Show Nikita the grid (`templates/desire-angle-grid.md` filled: desire ×
angle × headline × awareness × format × swipe thumbnail/link) + exact credits
(`generate_image` with `get_cost: true`, × number of ads). No images until he says go. He
may cut, swap or rewrite angles or swipes here.

6. **Image, one ad per pass** (`prompts/06-image-prompt.md`). Get each reference into
   Higgsfield ONCE and log the ids in `<run>/media.json`: anything with a public URL →
   `media_import_url` (small, preferred); local-only files → `media_upload` (one file per
   call, since its signed URLs are huge) → `curl -X PUT` → `media_confirm`. Pass → `prompt.md`.
   Then `generate_image` with `model: "nano_banana_pro"`, `resolution: "2k"`,
   `aspect_ratio: "1:1"`, `medias: [{product, image_references}, {swipe, image_references}]`,
   `prompt` = FINAL PROMPT. Wait (`jobs_wait`), then LOOK at the result: product matches
   the photo? Every ON-IMAGE TEXT string spelled right? ≤ 3 focal points? Desire readable in
   2 seconds? Nothing outside the brief? Competitor branding gone? Fail → fix the prompt and
   regenerate THAT ad (max 3 tries, then flag it). Log the job id + URL in `image.md`.
7. **Copy, one ad per pass** (`prompts/07-copy.md`): the ad's funnel stage picks the
   section → `copy.md`. Check: character limits, brief-only claims, one desire.
8. **Tracking** → `tracking.csv` (`templates/tracking.csv` = BBA Ad Tracking Master columns)
   + `grid.md`. ICP = a named person with age, situation and goal; Problems = numbered
   mechanism beliefs; Key Objections = in their own voice. Structure: **one ad set per
   desire, its 5 angle ads inside**. Ad name `<slug>_D#A#_<format>`; folder `<slug>/D#/`.
9. **Hand back.** Show Nikita all images + grid + copy. Ask "Want me to lock this into the
   brain?" Only on an explicit yes: desires, angles, swipes, test plan → `AD_RESEARCH.md`;
   one row per ad (ID, desire/angle, format, image URL, exact final prompt, headline,
   primary text) → `CREATIVES.md`; STATE + `_BOARD.md`; commit + push.

## Mode B — Iterate (ads have results)

Get per-ad spend, CTR, CPC, ROAS (Nikita, `facebook` ads tools, or Adnova) into the
grid. Then (course-map §8):
- 2+ angles winning under one desire → strong desire → new angles (new stories) for it
- 1 angle winning → expand that story (variations) before judging the desire
- 0 angles winning → the desire is weak, not the execution → replace it (new Step 4 pass for 1 desire)
- wins scattered, no desire with 2–3 winners → the mechanism isn't believed → refine
  the mechanism for the awareness level (rerun Step 3 with the results attached)
- next batch = **80% iterations, 20% new**. Run Steps 5→9 for that batch, one by one.

## Quality bar (every output)

- Desire = a want that ALREADY exists, "I want …", not a feature, not a problem.
- Angle = a specific person's story + crisis moment, not a hook or a slogan.
- One ad = one desire. No mixing.
- Language comes from `02-discussions.md`, not copy-speak.
- Every claim, number, offer and proof point is in `00-brief.md`. Nothing invented (rule 2).
- Nothing in the repo before Nikita's explicit confirm (rule 7).

## Common mistakes

| Mistake | Fix |
|---|---|
| Starting research before the ❗ answers | Intake first, always |
| Each pass reading the whole 1 MB brain | Brief once; passes read the brief |
| Ads about the problem only | Agitate, then close the loop on the desire |
| Angle = headline | Full story: who, arc, mechanisms, emotional moment |
| Batching 5 ads in one prompt | One pass per ad |
| Same swipe layout for every awareness level | Format follows awareness |
| Invented "10,000+ happy customers" badge | Proof only from the brief |
| Killing a desire after one losing angle | Judge on all 5; expand a lone winner first |
| Generating before the gate | Gate + exact credits first |

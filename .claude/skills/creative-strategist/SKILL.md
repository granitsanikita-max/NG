---
name: creative-strategist
description: Use when a product or brand needs a creative strategy, when Nikita says "creative strategy", "creative strategist", "mass desires", "angles", "25 angles", "what do I test next", or when live ads have results and the next desires/angles must be decided. Runs the Brand Builders Academy creative-strategy process, one pass at a time: research → 5 mass desires → 5 angles each = 25 angles in a spreadsheet. Then it asks whether to also swipe the 25 static image ads.
---

# Creative Strategist

**The outcome, every run: 5 mass desires × 5 angles = 25 angles, delivered as a spreadsheet**
(the BBA testing grid + full angle detail). Each future ad is built from exactly one desire +
one angle, so a winner tells you WHY it won and can be repeated.
After the spreadsheet, it **asks** whether to also swipe the 25 static image ads (optional
Part 2). Ad copy is NOT part of this skill; Nikita writes it.
With live results, Mode B decides the next desires/angles (80% iterate / 20% new).
Theory and every course rule: `reference/course-map.md`. Read it at the start of every run.

## THE ONE-BY-ONE RULE (non-negotiable)

Every unit is its own focused pass, run strictly in order. A pass starts only after the
previous pass's output is saved and checked. Nothing runs in parallel. Nothing is batched.
- 0b brief → #1 research → #2 discussions → #3 mechanism → #4 desires (5 passes)
- angles: one pass per desire, D1 → D5 (5 passes; each pass reads the angles already written)
- spreadsheet (script, not a pass), then the Part 2 question
- Part 2 only: per ad, image-prompt pass → image → check, then the next ad (25 passes)
- core run ≈ **10 passes**; with Part 2, + 25 passes + 25–50 images. Never copy one ad's prompt to make another.

**Pass mechanics (Agent tool available):** values live in `<run>/vars.json` (run-wide) and
`<run>/vars-<id>.json` (per pass: `<id>` = `D#` for an angle pass, `D#A#` for an ad pass; the
passes before that need no per-pass file). Placeholder table: `templates/subagent-brief.md`.
Build the pass:
`python3 <skill>/scripts/fill.py <skill>/prompts/<file> <run>/vars.json[,<run>/vars-<id>.json] <run>/pass-<id>.prompt.md <output path> ["extra note"]`
It appends the footer and refuses if a placeholder is unfilled. Then call `Agent`
(`subagent_type: "general-purpose"`, `model: "opus"`) with: "Your full task brief is in
<run>/pass-<id>.prompt.md. Read it first and follow it exactly." Wait for it. Read the output,
check it against the step's check + the Quality bar, rerun the same pass with the specific
fix if it fails, then tick `RUN.md`.

**Inline mode (no Agent tool, e.g. claude.ai):** you run each pass yourself, on whatever
model you are. Before each pass, re-read its prompt file, the Footer and every input file
fresh. One pass per response: do it, save the output, show the footer's 3-line summary,
then **end your turn** with "Next: <pass>. Reply `go`, or `autopilot` to run the rest
without stopping." Autopilot still stops at 🛑 THE QUESTION, 🛑 Gate 1, the Lock, any FLAGGED ad, and
anything that needs an upload from the user. It is still one pass per response.

## Environment: detect at Step 0

**Repo mode:** `git rev-parse --show-toplevel` works and that folder has `brands/_BOARD.md`
and `CLAUDE.md`. Work from the repo root, obey its CLAUDE.md (rule numbers below refer to it).
Sections marked **[repo]** apply only here.

**Upload mode** (skill uploaded to claude.ai / Claude desktop): anything else. Overrides:
- **The user** may not be Nikita. Address whoever is talking. The CLAUDE.md rules don't
  exist here, but their spirit holds: no invented facts, nothing final until the user confirms.
- **Brand files** = the user's uploads (intake item 2). Read each in full and confirm in one
  line what you read. No git, STATE, board or charters. Skip every **[repo]** step.
- **`<run>`** = `/mnt/user-data/outputs/creative-strategy/<brand>/` if writable, else
  `./creative-strategy/<brand>/`. **No filesystem at all** → keep each output as a clearly
  headed chat message, and at the Lock step give everything as one downloadable document.
- **Intake changes:** first line "Creative strategy intake: <brand>" (no ACTIVE BRAND).
  Item 6 asks for swipe uploads, since there's no ad-library search. Item 12 says "~10 passes in
  this chat (+25 if you want images; they run in your Nano Banana Pro unless an image connector exists)."
- **Images without a connector (Part 2):** Step 8 outputs the FINAL PROMPT + which reference images to
  attach, in order. The user renders it in Nano Banana Pro and uploads the result, and you
  run the checks. Because each render is a round trip, the user may choose at Gate 1:
  (a) one ad at a time (prompt → user renders → check), or (b) all 25 prompt passes
  first (still one per response), then renders and checks ad by ad. The max-3-tries rule
  still applies per ad. Gate 1's cost line = "25 renders + remakes in your Nano Banana Pro".
- **fill.py without code execution:** by hand. Drop the leading `<!-- … -->` comment, replace
  every `{{UPPERCASE}}`, then append the extra note and the Footer from
  `templates/subagent-brief.md`. Check that no `{{UPPERCASE}}` is left.
- **Spreadsheet:** run `scripts/make_sheet.py` if code execution exists; otherwise build the
  same two tables (Testing Grid + Angles) as a downloadable CSV/markdown by copying the angle
  files exactly. **Mode B** starts by asking the user to upload the spreadsheet + LOCKED doc.

## [repo] Station + lanes

Runs as the **Ad Research** station (`sessions/ad-research.md`); in Part 2 also as **Ad
Creation** (`sessions/ad-creation.md`). It reads every brand file. It writes only at the lock
step: `AD_RESEARCH.md` (+ STATE, _BOARD), plus `CREATIVES.md` only if Part 2 ran (that file
belongs to Ad Creation, so ask Nikita once to OK it), and only what he locks.

## Workspace `<run>`

[repo] `<session scratchpad>/creative-strategy/<slug>/` (path in the system prompt; fallback
`/tmp/creative-strategy/<slug>/`). Drafts only, never the repo (rule 7).
Files, in creation order: `RUN.md` (from `templates/RUN.md`) · `00-intake.md` ·
`product.<ext>` · `00-brief.md` · `vars.json` · `01-research.md` · `02-discussions.md` ·
`03-mechanism.md` · `04-desires.md` · `desires.json` · `05-angles-D1..D5.md` ·
**`creative-strategy-<brand>.xlsx` + `.csv`** (the outcome) · Part 2 only: `swipes/` +
`swipes/CATALOG.md` · `plan-grid.md` · `media.json` · per ad `ads/D#A#/{competitor.<ext>,
swipe.md, prompt.md, image.png, image.md}` · always: `pass-*.prompt.md` + `vars-*.json` (fill.py).
After compaction: re-read `RUN.md`, `00-intake.md`, this file and `reference/course-map.md`,
then resume at the first unticked box. A full run takes hours. If the session is lost, start
a new one, re-run Step 0 (paste the old `00-intake.md`), then do only what's missing.

## Step 0: Intake (ALWAYS first)

1. Detect the environment. **[repo]** `git pull`, match the user's words to `brands/_BOARD.md`
   (ask if 0 or 2+ match; new product → CLAUDE.md "Starting a new brand"), state
   `ACTIVE BRAND: <slug>`, read both charters, every brand `.md` file and every file in
   `brain/` (rule 2; files over ~1 MB: header + Grep only). Where files disagree, whatever
   STATE/BRAND marks CURRENT (newest date) wins; list the conflicts. **Upload:** read every uploaded doc.
2. **Mode check.** Ask "first run, or iterate (Mode B)?" if: live ads with results exist,
   [repo] AD_RESEARCH.md already holds a locked creative strategy, or [upload] the user
   mentions a previous run or LOCKED file.
3. **Tool check:** opus `Agent` · web search/fetch (or Firecrawl) · Higgsfield `generate_image`
   + `media_import_url` · an ad-library tool (`winning_hunters` / `facebook ads_library_search`).
   Name what's missing, and what that changes.
4. Send ONE message, pre-filled from the docs, so the user only corrects:

```
ACTIVE BRAND: <slug>. Creative strategy intake. ❗ = must answer before I start.
Conflicts I found in the files: <list, or "none"; only if there are 2+ docs>

1. ❗ Product, one line · the name customers see · niche:      [pre-filled]
2. ❗ Foundational docs (source of truth):                 [list found]  Anything else (avatar, strategy, UMS)?
3. ❗ THE main competitor + product page URL + who buys from them:   [pre-filled / options]
   (If there are several, I recommend the one whose buyers match our lead segment. A competitor
   with a different mechanism is fine; we model its customers and ad formats, never its mechanism.)
4. ❗ Problem space, what it fixes, 2–3 examples:          [pre-filled]
5. ❗ Product photo: clean, high-res, plain white background (upload / URL).
   (Fallback only if you OK it: the supplier listing photo.)
6. ❗ Swipe ads: competitor STATIC image ads to model (uploads / links), ideally 1+ per format:
   native/organic (no text) · benefit callouts · comparison · review · offer + urgency · before/after.
   [repo] Already in the repo: <list / none>. Reuse? Formats you don't cover: I search and you approve at Gate 1.
7. (Only if you'll want images) Where the ads send traffic: product page · advertorial · listicle · quiz?
8. Offer facts the ads may show (price, bundle, guarantee, shipping):  [from OFFER]
9. Proof the ads may show (real review count, rating, customers): [found / "none yet" → no
   social-proof numbers on ads; prices + guarantee from 8 are still fine]
10. Banned claims/words · claims waiting on proof (e.g. a sample) · health/medical limits:  [from docs]
11. Research: <what the docs already contain>. Default = fresh forum research (prompts #1–#2)
    merged with it. OK?
12. Scope: full 25 angles (default) · or quick test = all research + 5 desires + desire 1's 5 angles.
    Cost: ~10 Opus passes for the 25 angles. Images are optional afterwards (+25 passes +
    25 Nano Banana Pro images; exact credits shown first). Missing tools: <none / list>.
Reply with your corrections and answers. I start only when every ❗ is answered.
```
5. An item counts as answered only when the user confirms or corrects it explicitly (rule 7).
   "go" or "looks good" covers only the items the user can see answered. If ❗ items are
   still open, ask for just those. Save to `<run>/00-intake.md`, the run's contract. Save the
   product photo as `<run>/product.<ext>`.

## Step 0b: Brand brief (1 pass, `prompts/00b-brand-brief.md`)

One pass reads every foundational doc and writes `00-brief.md` (≤ 3,500 words): product +
mechanism · voice · segments · **APPROVED CLAIMS** (verbatim + source) · **APPROVED OFFER
FACTS** · **APPROVED PROOF** · **BANNED** · **GATED** (claims waiting on proof) · awareness ·
customer voice · creative history · conflicts. Then spot-check 5 approved claims against
their sources (inline mode: re-open the source docs; don't check from memory). Write
`<run>/vars.json`: RUN_DIR, BRAND_DOCS (= `00-intake.md, 00-brief.md` with full paths),
PRODUCT, PRODUCT_SHORT, NICHE, COMPETITOR, COMPETITOR_URL, COMPETITOR_DEMOGRAPHIC,
PROBLEM_SPACE_EXAMPLES, PRODUCT_PHOTO.
**From here on, every claim, offer, number and proof point comes from `00-brief.md`.**

## The pipeline

Prompts 01–06 are the original BBA prompt docs. Each file marks its few placeholder swaps
and "pipeline additions". Every check below is done by the orchestrator (you) before ticking.

1. **Market research** (`01-market-research.md`) → `01-research.md`. Check: 20 posts with
   URLs, about the problem (not product complaints), verbatim, FULL vs EXCERPT marked.
2. **Discussion analysis** (`02-discussion-analysis.md`) → `02-discussions.md`. Check: all
   8 sections, quotes tagged [FULL]/[EXCERPT]/[BANK], source table. It may correct #1; log it in RUN.md.
3. **Copywriter + unique mechanism** (`03-copywriter-mechanism.md`) → `03-mechanism.md`.
   Check: the UMP and UMS are specific, and the UMS uses only brief-approved facts.
4. **5 mass desires** (`04-mass-desires.md`; extra note: "also open the customer-avatar /
   foundational doc(s) listed in 00-intake") → `04-desires.md`. Check: "I want …" + segment,
   passes the distinction test.
5. **Angles, one desire per pass** (`05-angles.md`, D1 → D5) → `05-angles-D#.md`.
   `vars-D#.json` = DESIRE_NUMBER, DESIRE_TEXT (the full desire block from 04), and
   PREVIOUS_ANGLE_FILES (earlier `05-angles-D*.md`, or "none"). Check: the depth bar, the
   support-group test, forum language, ⚠GATED tags on headlines.
   *Quick-test scope:* run D1 only, then continue with D1's 5 ads.
6. **The spreadsheet: the main outcome.** Write `<run>/desires.json` from `04-desires.md`
   (`[{"n":1,"desire":"I want …","segment":"…"}, …]`), then run
   `python3 <skill>/scripts/make_sheet.py <run> "<brand>"` → `creative-strategy-<brand>.xlsx`
   (tab **Testing Grid** = BBA Mass Desire output spread: desire → 5 angles → SPEND · CTR · CPC ·
   ROAS; tab **Angles** = every angle in full: audience, story arc, both mechanisms, emotional
   moment, headlines, awareness, funnel, static format, objections) + the same as `.csv`. It copies the
   files exactly. Fix anything it reports under CHECK (rerun that angle pass), then rerun it.
   Show the user the 5 desires + 25 angle names and deliver the spreadsheet file.

**🛑 THE QUESTION (always ask, then stop):**
```
Your 25 angles are done (spreadsheet attached). Next:
A) I swipe the 25 static image ads now: I match a competitor swipe to each angle, show you the
   plan + cost, then make them one by one in Nano Banana Pro
B) You'll make the images yourself: I'll lock the strategy now
C) Later: I'll lock the strategy now; just say "swipe the images" when you're ready
```
**B or C** → go to **Lock**. **A** → Part 2.

## Part 2 (optional): swipe the 25 static image ads

7. **Swipe per angle** (not a generative pass; work through the angles in order). Medium =
   static images for all ads (formats stay consistent, so only the message varies). Each
   angle's **Static Format** (from its angle file) decides the swipe. In order:
   (a) the best-fit swipe of that format from the user's set (one swipe can serve several angles);
   (b) none → search `winning_hunters search_facebook_ads` / Meta `ads_library_search` for
   long-running static ads of that format, download 2–3 and propose them at Gate 1;
   (c) no tool or nothing found → the closest swipe the user gave, with the substitution logged.
   LOOK at every swipe before using it. Log each in `swipes/CATALOG.md` (advertiser · run
   dates · format · NATIVE or DESIGNED · layout). Per ad: copy the chosen swipe to
   `ads/D#A#/competitor.<ext>` and write `ads/D#A#/swipe.md` (which swipe, source URL, why).
   We model the swipe's layout and format, never its product, claims or mechanism.

**🛑 GATE 1: before any image.** Show `plan-grid.md` (`templates/plan-grid.md`: one row per
ad: desire · angle · headline · awareness · format · swipe) + cost (exact credits via
`generate_image` with `get_cost: true` × ads × ~1.5 for remakes; upload mode without a
connector: number of renders). The user may cut, swap or rewrite rows. No images until they say go.

8. **Images, one ad at a time, D1A1 → D5A5** (`06-image-prompt.md`). `vars-D#A#.json` = the
   desire fields + AD_ID, ANGLE_FILE, ANGLE_NAME, EMOTIONAL_MOMENT, COMPETITOR_AD, and
   ANGLE_HEADLINE = the most specific and emotionally sharp of the 3 options with no
   ⚠GATED/BANNED claim. Pass → `prompt.md`.
   **Generate (with a Higgsfield connector):** each reference goes into Higgsfield once
   (`media.json`): public URL → `media_import_url`; local file → `media_upload` (one file per
   call) → `curl -X PUT` → `media_confirm`. `generate_image` with `model: "nano_banana_pro"`,
   `resolution: "2k"`, `aspect_ratio: "1:1"`, `prompt` = FINAL PROMPT, `medias` = **exactly the
   references named in the prompt's first line, in that order** (DESIGNED: product, swipe;
   NATIVE with product not shown: swipe only). `jobs_wait` → download to
   `ads/D#A#/image.png` → look at it.
   **Check:** product matches the photo · every ON-IMAGE TEXT string exact · ≤ 3 focal points ·
   desire readable in 2 seconds · nothing outside the brief · no competitor branding ·
   NATIVE: reads as a real phone photo with no text · the job ran on the model you asked for.
   **Fail →** write down the reason, then fix it: a small fix → edit `prompt.md` yourself; a
   wrong concept → rerun the pass with the reason as the extra note. Regenerate THAT ad, max
   3 tries, then mark it FLAGGED (autopilot stops). Log every try in `image.md`.
   Finish one ad (prompt → image → check) before starting the next.
9. Rerun `make_sheet.py`: the spreadsheet picks up each ad's image link + swipe source. Show
   all images (FLAGGED marked) and deliver the updated spreadsheet.

## Lock (after the question, or after Part 2)

Ask "Want me to lock this in?" Lock only what the user confirms, in this order:
1. Mechanism: UMP + UMS (03).
2. Language bank: the top 20 verbatim phrases with sources (02).
3. The 5 desires (04).
4. All 25 angles in full (05).
5. The spreadsheet.
6. Part 2 only: the swipes, and per ad the image URL + file name + exact final prompt.
- **[repo]** Items 1–5 → `AD_RESEARCH.md` ("Creative Strategy <date>"), with the spreadsheet saved
  next to it as `brands/<slug>/creative-strategy-<date>.xlsx` (ask once, since it's a new file). Item 6
  → `CREATIVES.md`, after Nikita OKs writing that file. Then STATE + `_BOARD.md`, commit, push.
  Image URLs can expire, so tell Nikita to download the finals.
- **Upload:** one document `creative-strategy-<brand>-LOCKED.md` (items 1–4, 6) + the spreadsheet.

## Mode B: Iterate (ads have results)

Start: load the locked strategy ([repo] AD_RESEARCH.md + the spreadsheet; [upload] the LOCKED
document + spreadsheet). Missing mechanism or language bank → rerun 0b → #3 first. Get per-ad
spend, CTR, CPC and ROAS (from the user, or ads tools if connected) into the spreadsheet's
Testing Grid. Read it per desire (course-map §8):
- **2+ angles win under one desire** → strong desire → Prompt 05 with the extra note "5 NEW
  angles for this desire; don't reuse these: <winning + existing angles>".
- **1 angle wins** → expand that story first → Prompt 05 with the extra note "5 VARIATIONS of
  angle <X>: same desire, crisis point and mechanism; change the person, setting and opening moment."
- **0 angles win** → the desire is weak (not the execution) → Prompt 04 with the extra note
  "these desires exist: <list>. Output exactly 1 new desire that passes the distinction test
  against all of them." Then Prompt 05 for it.
- **Wins scattered, no desire with 2–3 winners** → the mechanism isn't believed → rerun
  Prompt 03 with the results attached.
- Next batch = 25 angles: **20 iterations** (on proven desires/angles) + **5 new**. Then the
  spreadsheet (Step 6), the question, and Part 2 if wanted, one ad at a time.

## Quality bar (every output)

- Desire = a want that ALREADY exists, "I want …", not a feature, not a problem.
- Angle = a specific person's story + crisis moment at Prompt 05's depth bar, not a hook or a slogan.
- One ad = one desire. No mixing.
- Language comes from `02-discussions.md`, not copy-speak. No forum usernames anywhere.
- Every claim, number, offer and proof point is in `00-brief.md`. GATED claims stay out until
  proven. Health-adjacent products: no medical or cure claims, and before/afters only where the
  platform allows them. Nothing invented.
- Nothing final before the user's explicit confirm.
- When a later pass corrects an earlier file, the later file wins (the Footer says so); log it in `RUN.md`.

## Common mistakes

| Mistake | Fix |
|---|---|
| Starting research before the ❗ answers | Intake first, always |
| Each pass reading the whole brain | Brief once; passes read the brief |
| Angles about the problem only | Each angle must land on its desire |
| Angle = headline | Full story at the depth bar |
| Batching angles or ads | One pass each, finish one before the next |
| Skipping the question after the spreadsheet | Always ask A / B / C |
| Native swipe + badges and a headline on the image | Native = no text; the angle goes in your primary text |
| Mirroring a swipe that breaks the brand rules | The brief beats the swipe |
| Copying the course's dog-leash story | It's a depth benchmark only |
| Invented "10,000+ happy customers" badge | Proof only from the brief |
| Killing a desire after one losing angle | Judge on all 5; expand a lone winner first |
| Generating images before Gate 1 | Gate + cost first |
| Writing ad copy | Not this skill's job; Nikita writes copy |

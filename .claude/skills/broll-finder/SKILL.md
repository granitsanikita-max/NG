---
name: broll-finder
description: >-
  Finds REAL b-roll clips for Nikita's ads instead of generating them with AI (which burns credits and
  looks worse). Give it a storyboard / shot list (pasted, or from a Whole Ad Structures teardown) and,
  for product shots, the supplier/product URL. It classifies each scene, searches free commercially-safe
  stock libraries (Pexels + Pixabay) for generic scenes, pulls real product footage from the supplier
  listing for product scenes, judges every clip against a strict quality bar (authentic/tactile/
  cinematic — never generic corporate stock), and returns 3–5 vetted candidates per scene with previews
  + download links for Nikita to pick. Use whenever Nikita needs b-roll, stock clips, or footage for an
  ad — "find b-roll for this ad", "get me clips for these scenes", "find footage for my storyboard",
  "I need real b-roll not AI". It sources and vets clips; it does NOT generate video with AI.
---

# B-Roll Finder

Nikita's ads are 100% AI right now — AI avatar talking heads + AI b-roll — and the AI b-roll burns
credits and looks fake. This skill replaces the b-roll half with **real, vetted clips**: he gives a
storyboard, it returns download-ready clips that hit a real quality bar.

**It sources and vets — it never AI-generates.** The whole point is to stop paying for AI b-roll.

## The quality bar is the whole game

Read `references/quality-bar.md` before selecting anything and apply it hard. "Shit b-roll" comes from
returning the first generic corporate-stock clip. The bar (calibrated to Nikita's reference ad): real,
tactile, natural-light, appetizing inserts + one cinematic money shot; reject anything that reads as
staged stock. Better to hand back 2 great clips for a scene than 5 with 3 duds.

## Step 1 — Get the storyboard + product URL

Accept the storyboard either way:
- **Pasted scene list** — scene # + description (+ optional shot type / desired length).
- **From a teardown** — a row in the *Whole Ad Structures* DB / a skeleton Nikita points to: use its
  beats as the scene list.

If a scene involves the actual product, also get the **supplier/product URL** (his AliExpress / Amazon
/ competitor listing) so product footage can come from there. Ask for it once if product scenes exist
and it wasn't given.

## Step 2 — Classify every scene into a lane

For each scene decide which lane it's in — this is what makes the skill useful, not just a stock search:

- **STOCK lane** — generic, non-product scenes (tired feet, a mom in a kitchen, pouring coffee, city
  street, hands typing, nature, close-up of dates). These can be found on Pexels/Pixabay.
- **PRODUCT lane** — the actual product in frame (unboxing, the label, product in-hand, the device
  working). Stock will NEVER have his product → pull from the supplier listing footage.
- **SHOOT/AI lane** — a hero/product shot that neither stock nor the supplier has (e.g. a bespoke
  cinematic money shot of HIS branded bar). Flag these explicitly so Nikita knows the FEW clips he
  actually needs to shoot or (only here) AI-generate — instead of AI-ing everything.

State the lane split up front so he sees how much is coverable for free.

## Step 3 — STOCK lane: search, then vet against the bar

For each stock scene, run the bundled searcher (it reads `PEXELS_API_KEY` + `PIXABAY_API_KEY` from env):

```bash
python3 "${SKILL_DIR}/scripts/broll_search.py" --query "<vivid query: subject + emotion + shot type>" \
    --orientation portrait --min-dur 2 --max-dur 15 --per-source 6
```

- Write **2–3 query variants** per scene (literal for action/product beats, conceptual for emotional
  beats) and merge results — don't rely on one phrasing.
- The script filters hard specs only (≥720 short side, duration window, portrait-first). **You** then
  **read each candidate's `preview_image`** (Read the URL) and judge it against `quality-bar.md`. Drop
  everything that reads as generic/corporate/watermarked/cheap.
- Keep the **3–5 best per scene**. If nothing clears the bar, say so for that scene rather than padding
  with duds (and suggest a better query or that it's a SHOOT/AI scene).

## Step 4 — PRODUCT lane: pull supplier footage

For product scenes, get the real product footage from the listing:
- Use the **watch** skill / a browser pull on the supplier or competitor product URL to grab the
  listing's video(s), or the product's own gallery clips.
- If the listing has no usable video, ask Nikita for the supplier's clips (most AliExpress sellers send
  raw footage on request) — don't fake it with stock of a *different* product.

## Step 5 — Present candidates, then download picks

Present per scene, scannable:
`Scene 3 — "hands squeezing a date": [Pexels ▸ preview] 1080×1920 · 6s · authentic macro, natural light — ✅ hits the bar`
Give the preview link + a one-line why-it-matches + the quality read. Let Nikita pick (candidates-to-
pick is his chosen mode). Then download the picks, named by scene:

```bash
python3 "${SKILL_DIR}/scripts/broll_search.py" --out-dir <dir>/scene_03 --download "<url1>" "<url2>"
```

Deliver the downloaded files (SendUserFile) or hand him the folder, and a one-line summary: scenes
covered by stock / by supplier / still needing a shoot.

## Setup (one-time)
- Free API keys: **Pexels** (pexels.com/api) and **Pixabay** (pixabay.com/api/docs) — 2-min signup
  each. Set `PEXELS_API_KEY` and `PIXABAY_API_KEY` as env vars (the repo SessionStart hook can inject
  them the same way it does the Groq key). Pexels is the quality workhorse; Pixabay adds breadth.
- Both licenses allow **commercial use with no attribution required** — safe for paid ads. (Still avoid
  clips with recognizable logos/brands/people that imply endorsement.)

## Guardrails
- **Never AI-generate b-roll here** — this skill exists to replace that. Only *flag* the rare SHOOT/AI
  scene.
- **Quality bar is non-negotiable** — reject generic corporate stock even if it "technically matches."
- **Vertical 9:16** for ad b-roll (portrait, or cleanly croppable). No watermarks, no burned-in captions.
- **Product footage must be HIS product** — never substitute stock of a similar-but-different product.
- **Free only** (per Nikita) — Pexels + Pixabay + supplier footage. Don't route to paid libraries
  unless he later adds one.
- If a key is missing, the script says so — tell Nikita to add it rather than silently returning half.

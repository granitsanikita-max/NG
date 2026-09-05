---
name: swipe-pipeline
description: >-
  One-command, hands-off swipe-file automation for Nikita: it asks a couple of intake questions
  (ad concept + niche + how many), then runs the WHOLE chain by itself — hunts the longest-running
  winning ads (by concept and niche) across Winning Hunter + the Facebook Ad Library, confirms the
  stores are real 7–8-figure operators, tears down the top ones (transcript + frames + copyable
  skeleton), and files each as a fully-tagged row in the "Whole Ad Structures" Notion database — with
  no manual approve step in between. Use when Nikita wants the entire find→teardown→file flow run
  automatically: "run the swipe pipeline", "run the whole thing", "auto-swipe [concept] ads in
  [niche]", "find and tear down the best [concept] ads", "build my swipe file for [niche]",
  "fill my structures for [concept]". This is the automated superset of ad-finder + ad-teardown.
---

# Swipe Pipeline (find → teardown → file, automatic)

This is the hands-off orchestrator. Nikita triggers it once and it does everything ad-finder and
ad-teardown do, chained, without stopping for a manual approval. He ends up with new, fully-tagged,
copyable ad structures in Notion and never touches the middle.

It **reuses the other two skills' logic** — it doesn't reinvent it. When a step says "run the
ad-finder hunt" or "run the ad-teardown flow," follow that skill's own steps (they're installed
alongside this one, including ad-teardown's `fb_ad_pull.py` browser fallback and frame/transcript
machinery).

## Step 1 — Intake (ask, then run)

Sharpen the run before spending calls/credits. Unless Nikita already gave these in his message, ask
with **one `AskUserQuestion`** (batch them — don't ask one at a time):

1. **Concept** — Storytelling / Personal Story · Long-form VSL · UGC Testimonial · Listicle ("X reasons")
   · Street Interview · Founder Story · Demo/Unboxing · Myth-Buster · **Any format**.
2. **Niche** — niche / product / keyword (neuropathy, pet odor, eczema…), or "any."
3. **How many to fully tear down** — default **3** (each teardown = a video download + Whisper +
   dozens of frame reads, so this is the expensive part — keep it small). If Nikita asks for more than
   **6**, confirm once before running, since it's real time and credits.

Echo one confirmation line and go — do NOT wait for further approval after intake, that's the point:
`Running full swipe pipeline: hunting [concept] ads in [niche], tearing down the top 3, filing to Whole Ad Structures. Sit back.`

## Step 2 — Hunt (ad-finder logic, concept + niche)

Follow the **ad-finder** skill: load `winning_hunters` + `facebook` tools, apply the **Concept → hunt
recipe** (its Step 1b table) plus the niche, `sort_by=longestrunning`. Confirm each candidate store is a
real **7–8-figure operator** with `get_store_details` (drop the small ones), and **verify each ad
actually matches the chosen concept** (scan the copy/creative) — drop mismatches. Rank by run length →
store revenue tier → number of variants. Over-collect a pool (~10–15), then take the **top N** (the
count from intake) for teardown.

For each of the top N, get its WinningHunter single-ad link (`app.winninghunter.com/ad/<productid>?platform=meta`)
— the link rule from ad-finder (never a bare `facebook.com/ads/library/?id=…`, it won't isolate one ad).

## Step 3 — Log the picks (audit trail, auto-approved)

Append the top N to the **Ad Finds — To Review** DB (`collection://32981cf7-fc4d-4e06-a849-5f6173a312a6`,
fetch schema first) exactly as ad-finder does, but set **`Status = Approved`** immediately (the pipeline
is the approval). Start each row's **Notes** with `Concept: [concept] ·`. Dedup first: skip any Link or
Store already present. This gives a record and prevents re-tearing the same ad on the next run.

## Step 4 — Teardown each (ad-teardown logic)

For each of the N picks, run the **ad-teardown** flow (its Steps 1–5): pull the ad (WH `scan_ad`, or the
`fb_ad_pull.py` browser fallback for a raw FB link), get the transcript, read frames dense through the
hook, derive the beat-by-beat structure, and build the **copyable skeleton** (beats + CORE RULES +
STEAL THIS) per `references/skeleton-format.md`. Deliver each teardown in chat as it finishes so Nikita
can watch progress.

## Step 5 — File each into "Whole Ad Structures" (the swipe DB)

For every torn-down ad, create a **row in the Whole Ad Structures database**
(`collection://0366d32b-a1c5-44a2-8807-85649fc6c374`, fetch schema first) with the **full skeleton in
the row body** as a ```javascript code block, and fields filled:

- **Structure** (title): "[Store] — [Structure Name]".
- **Video Format** (relation → *Video Ad concepts* `collection://1137cb0c-33e8-469f-a792-4bb34761f823`):
  set it to the chosen **concept's** genre row (query that DB for the matching Name → use its page URL).
- **Niche**, **Length** (from real video duration: Short <60s / Mid 1–3 min / Long-form VSL 3 min+),
  **Awareness**, **Funnel**.
- **Strength** (derive, don't guess): **🔥 Elite** = ran ~12 mo+ or 8-fig store running it for months;
  **Strong** = proven (weeks–months, real 7–8-fig store); **Testing** = early/short/unconfirmed.
- **Source Store**, **Run Length**, **Source Link** (the WH single-ad link), **Date Added** (today).

Then flip that ad's **Ad Finds** row to **`Status = Filed`**. Do **not** add anything to Video Ad
concepts — you only *link* to it via the relation.

## Step 6 — Clean up + report

`rm -rf` each ad's working dir (downloaded video/frames) as you finish it (per ad-teardown Step 5).
Then one summary: a table of what got filed — Structure · Concept · Niche · Length · Strength · run
length — with a link to the Whole Ad Structures DB. One line: "Filed N new [concept] structures for
[niche]. Filter the DB by Concept/Niche/Strength to use them."

## Guardrails
- **The whole point is no manual step** — after intake, run start-to-finish. Only pause to confirm if
  the requested teardown count is > 6 (cost), or if a genuinely ambiguous choice appears.
- **Cost awareness** — teardown is the expensive part; default 3, never silently tear down 15.
- **Concept must actually match** — a long-running ad that isn't the requested concept doesn't belong;
  drop it rather than mislabel it.
- **Never invent** run length, revenue, or a skeleton beat — if the video won't pull, say so for that
  ad and move on; don't fabricate a teardown from copy alone.
- **Dedup across both DBs** — skip ads already in Ad Finds and structures already in Whole Ad Structures.
- **Never approve/scale spend or touch live ad accounts** — this skill only researches and files.

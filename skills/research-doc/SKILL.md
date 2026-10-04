---
name: research-doc
description: >-
  Runs Nikita's "Step 1 — Deep Market Research" by opening his LIVE Notion page (Product Launch
  Playbook → Step 1) and executing it line by line, in order, missing nothing — the Notion page is the
  ONLY source of rules, sections, standards, tools, and output format; this skill has no research rules
  of its own, it only makes sure every word on the page gets done. Builds a line-by-line ledger of the
  page, works it top to bottom, audits 100% coverage, then delivers exactly what the page says (currently
  4 Google Docs in one Drive folder). Use when Nikita says "do the research doc", "run deep research on
  [product]", "research this product", "do step 1", "fill out the research doc", or pastes a product to
  build a brand around. Front of his product→store→ads pipeline.
---

# research-doc — execute the Notion page, every word, in order

**This skill has NO rules of its own about research.** Every rule, section, standard, tool, threshold,
output format, and "done" condition lives on Nikita's Notion page **"Step 1 — Deep Market Research."**
This file only tells you HOW to read that page and make sure nothing on it is missed.

- If this file and the page ever disagree → **the page wins. Always.**
- If you catch yourself doing something because "that's how research is done" and the page doesn't say
  it → stop. Do what the page says.
- Never summarize, paraphrase, or "remember" the page. Read it fresh every run and work from its exact words.
- Effort: maximum. Slow and complete beats fast and partial. Nikita's instruction: *don't miss a single word.*

---

## STEP 1 — Fetch the live page (every run, before anything else)

1. Load Notion: ToolSearch `select:mcp__Notion__notion-fetch,mcp__Notion__notion-search`.
2. Fetch by ID: `mcp__Notion__notion-fetch` with `id: "3d3d5312-3cd6-817e-bba0-d79d8b50c076"`
   (URL: https://app.notion.com/p/3d3d53123cd6817ebba0d79d8b50c076 · parent: "Product Launch Playbook (Step-by-Step)").
3. ID fails (page moved/duplicated)? `mcp__Notion__notion-search` for `"Step 1 Deep Market Research"` →
   take the page whose parent is "Product Launch Playbook (Step-by-Step)" → fetch it.
4. **Check the fetch is complete.** If the result shows `truncated`, `unknown_block_count`, or
   `unknown_block_ids`, fetch those blocks too. Toggles, callouts, and nested bullets are part of the page —
   read them all.
5. **Open everything the page links to that a section depends on** (e.g. the Consciousness map and
   Sophistication map images, any linked Notion page). View images with Read after downloading; fetch
   Notion links with notion-fetch. If a link is dead, note it in the hand-off.
6. **Notion unreachable? STOP.** Tell Nikita Notion is down and that you won't run Step 1 from memory.
   Do not fall back to a remembered or cached version — the page is the only authority.

## STEP 2 — Build the line-by-line ledger (your contract)

1. Save the fetched page content **verbatim** to `<scratchpad>/step1-page.md`.
2. Build `<scratchpad>/step1-ledger.md`: one row per instruction on the page —
   **every heading, paragraph, bullet, sub-bullet, sub-sub-bullet, callout line, table row, and to-do box**,
   top to bottom, in page order. When one paragraph holds several instructions (e.g. "do X. Make sure Y."),
   split it into one row per instruction.
   Row format: `| L### | verbatim text | kind | section | output doc | status | where it's satisfied |`
   - **kind** = `DO` (a task to produce) · `STANDARD` (applies to every section, e.g. sourcing rules) ·
     `TOOL` (a skill/tool/source the page says to use) · `OUTPUT` (format / delivery) · `GATE` (a done-check).
   - **output doc** = whatever the page's own output instructions assign that section to.
   - **status** starts as `todo`.
3. **Prove the ledger is complete:** count the page's non-empty lines (`grep -c . step1-page.md`) and make
   sure every one is represented by at least one ledger row. Any line not in the ledger = rebuild it.
4. **Show Nikita the contract before researching:** one line per section, in page order, + the output
   docs the page asks for + anything the page says to ASK him first (e.g. the page's economics inputs).
   Ask those questions in one batched message, then continue (don't stall waiting if the page says to
   proceed without them).

## STEP 3 — Execute the page in order

- Work the ledger **top to bottom, in page order.** Right before you work a section, **re-read its exact
  ledger rows** (not your memory of them).
- **STANDARD rows apply to every section.** Re-check them each time you finish a section.
- **TOOL rows:** run every skill/tool the page names — in its tools list AND inline inside any section —
  using whatever is on the page that day (Nikita adds new ones). If one isn't available, do what the page
  says for that case and log the substitute.
- **Fanning out to sub-agents** (only in the way the page describes): give each agent (a) the **verbatim
  page text** for its sections, (b) the **verbatim STANDARD rows**, (c) its output doc. Never hand an agent
  a paraphrase. When an agent returns, check its output against those exact rows before accepting it.
- After each section: mark its rows `done` with the exact place it's satisfied (doc + section header).
  A row you genuinely can't satisfy → `blocked` + the reason (never silently `done`).

## STEP 4 — Coverage audit (before delivering — non-negotiable)

1. **Re-fetch the page.** If Nikita edited it mid-run, diff against `step1-page.md`, add new rows to the
   ledger, and do them.
2. Walk the ledger row by row against the finished output. For each row: is it actually present, as
   thorough as the page asks, and meeting every STANDARD row? If not → go back and do it.
3. Mechanical check: `grep -c '| todo |' step1-ledger.md` must be **0**. Every row is `done` (with a
   location) or `blocked` (with a reason).
4. Run the page's own final gate / verification section exactly as written.

## STEP 5 — Deliver exactly what the page asks

Follow the page's output instructions (doc split, folder, format, order, extra files, what to offer).
Tool mechanics for the usual deliverables (these are HOW-to-call notes, not rules):
- **Drive folder:** `mcp__Google_Drive__create_file` with `title` + `contentMimeType: "application/vnd.google-apps.folder"` → keep its `id` + `viewUrl`.
- **Google Doc inside it:** `mcp__Google_Drive__create_file` with `parentId: <folder id>`,
  `contentMimeType: "text/html"`, `textContent: <full HTML>` → auto-converts to a native Google Doc.
  Use `<h1>` per section, `<h2>` per sub-part, real `<table>`s, `<a href>` for every source URL.
- **Markdown copies:** write each to the scratchpad and send with `SendUserFile`.
- **Notion write-back** (only if the page says to offer it and Nikita says yes): `mcp__Notion__notion-create-pages`
  under the product page; read `notion://docs/enhanced-markdown-spec` first.

**Hand-off message (short):** the doc links · ledger coverage (`N/N rows done`, list any `blocked` + why) ·
which of the page's tools actually ran (and substitutes) · corrections from verification · anything the
page's gate couldn't confirm. Never claim "verified" unless the page's gate passed.

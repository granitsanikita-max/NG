| ID | verbatim text | kind | section | output doc | status | where satisfied |
|---|---|---|---|---|---|---|
| L001 | Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d3d53123cd6817ebba0d79d8b50c076 as of 2026-10-28T08:21:11.659Z: | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L002 | {"title":"Step 1 — Deep Market Research"} | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L003 | {"type":"emoji","emoji":"1️⃣"} | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L004 | Learn everything about the customer — better than they know themselves. | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L005 | Every other step is built on what you find here. | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L006 | Do this first, every time. | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L007 | ⬅️ You start with: a product to sell. | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L008 | ✅ You're done when: all 4 research docs are filled in — every section on this page done, in order, from real data — AND §20 Verify has passed (self-approved). | GATE | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L009 | Not before. | DO | PREAMBLE | ALL | done | All 4 docs (process) — page run top to bottom; §20 D |
| L010 | Output = 4 Google Docs, not one. | OUTPUT | OUTPUT-SPEC | ALL | done | 4 docs delivered as 4 Notion pages (Nikita override: Notion instead of Google Docs) |
| L011 | One Google Drive folder per product: "[Product] — Step 1 Research (date)". | OUTPUT | OUTPUT-SPEC | ALL | done | One Notion folder page "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L012 | Work this page top to bottom, in order — but write each section into the doc it belongs to (below), so nothing gets buried. | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L013 | Every doc opens with the Drive folder link, then Top 5 takeaways — written after §20 B–C's corrections and before §20 D, each one = a specific finding + its number or quote + the decision it forces (e.g. | OUTPUT | OUTPUT-SPEC | ALL | done | Folder link + Top 5 (written after §20 B–C, before D) at the top of each doc |
| L014 | "71% of snippets are solution-aware → lead with the mechanism"); never a section summary. | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L015 | Every doc ends with its own Sources list (every URL used in that doc). | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L016 | 📊 Doc 1 — Market & Competition (is there money + where's the opening?): Pre-0 Economics & KPIs · Audit first · 0 · 0B · 1 · 2 · 5 · 7 · 8 | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L017 | 👤 Doc 2 — The Customer (who she is + what she says): 2C data bank summary · 3 · 3A · 10 · 10B · 14 · 18 | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L018 | 🧠 Doc 3 — Persuasion (what she must believe + how we get her there): 6 · 9 · 9B · 11 · 12 · 13 · 13B · 16 · 17 · 18B | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L019 | 🎯 Doc 4 — Brand, Offer & Funnel (what we build + what we say): 2B Compliance · 4 · 4B · 15 · Funnel Map · 20 Verify report | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L020 | Plus: the full §2C customer data bank as a Google Sheet in the same folder. | OUTPUT | OUTPUT-SPEC | ALL | done | §2C Data Bank = Notion database in the folder (override of Google Sheet); CSV in repo |
| L021 | Top of each doc, in this order: Drive folder link → Top 5 takeaways → then Doc 2: the §2C summary · Doc 4: the shaded 2B SAY / DON'T SAY table. | OUTPUT | OUTPUT-SPEC | ALL | done | Top: folder link → Top 5 → Doc 2 §2C summary · Doc 4 §2B table |
| L022 | Format: phone-friendly — a big bold header for every section, smaller headers for sub-parts, short blocks over wide tables. | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L023 | Then offer (don't force) to write the 4 docs back into Notion as 4 sub-pages under one product page. | OUTPUT | OUTPUT-SPEC | ALL | done | Docs written into Notion directly (Nikita asked for Notion) |
| L024 | How to deliver (Drive): (1) create the folder FIRST (create_file, contentMimeType: application/vnd.google-apps.folder) and keep its link for the top of each doc · (2) write all 4 docs locally as .md as you go — Drive files can't be edited after upload · (3) only after §20, convert each .md to HTML (pandoc, or Python markdown with the tables extension) and upload that HTML once (parentId = folder, contentMimeType: text/html → Google Doc) and the §2C CSV (text/csv → Google Sheet) · (4) save each doc as a .md file too (contentMimeType: text/markdown + disableConversionToGoogleType: true) and send them with your final message, with all the links. | OUTPUT | OUTPUT-SPEC | ALL | done | 🔁 Notion instead of Drive per Nikita; .md written locally as we went; .md copies committed to repo |
| L025 | These deliverables override anything else — including older instructions inside the research-doc skill file. | OUTPUT | OUTPUT-SPEC | ALL | done | Delivery — Notion folder "Deep Research Run 2 — Men's Compression Tank" (Nikita override) |
| L026 | NON-NEGOTIABLE — read before every run. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L027 | 1 · Go in order. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L028 | Every run, every time. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L029 | Start at the top of this page and work down, section by section, line by line: Pre-0 → Audit first → 0 → 0B → 1 → 2 → 2B → 2C → 3 → 3A → 4 → 4B → 5 → 6 → 7 → 8 → 9 → 9B → 10 → 10B → 11 → 12 → 13 → 13B → 14 → 15 → 16 → 17 → 18 → 18B → Funnel Map → 20 (Verify always runs LAST, over everything). | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L030 | There is no §19. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L031 | Never skip ahead, never skip a section, never skip a line inside a section. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L032 | (Collecting research in parallel per "Run it as a workflow" is allowed — the WRITING stays in order.) ("Do this first" on §1 means: before every customer / strategy section below it.) | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L033 | 2 · Run EVERY skill and tool on this page — all of them, every run. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L034 | Not "if needed," not "just the main ones." Every skill in 🧰 Skills to use AND every tool named inside a section (Google Trends, Winning Hunter tools, jq, the Notion connector…) is mandatory. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L035 | The "Where each skill is required" table below says where each one runs. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L036 | A skill is down or needs a key? | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L037 | Use the closest substitute and say which — never silently skip. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L038 | Fallbacks — anything named "if X fails / is blocked / isn't installed," or limited to a region — run only when that condition is true. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L039 | 3 · Prove it at the end. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L040 | The §20 hand-off lists EVERY skill / tool on this page with ✅ ran · 🔁 substitute (which one) · ➖ not needed (why — fallbacks only) · ❌ couldn't (why). | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L041 | A skill missing from that list = the run is NOT done. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L042 | 4 · Draft → lock. §2, §4, and §4B are DRAFTS when you first reach them (the word "LOCK" inside §4B means this lock). | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L043 | You LOCK them at the end of §11, once the 1★ reviews and objections are mined. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L044 | The §9 One Belief is a draft too — rewrite it at the end of §13, once the mechanism is set. | STANDARD | NONNEG | ALL | done | Process — written in page order; all tools run (Doc 4 §20 A); LOCK after §11; One Belief rewritten after §13 |
| L045 | ## The one rule | STANDARD | ONERULE | ALL | done | All docs — every claim sourced; adversarial fact-check (Doc 4 §20 B) |
| L046 | Every answer must come from a real source — Reddit, Amazon reviews, forums, TikTok, competitor pages. | STANDARD | ONERULE | ALL | done | All docs — every claim sourced; adversarial fact-check (Doc 4 §20 B) |
| L047 | No guessing. | STANDARD | ONERULE | ALL | done | All docs — every claim sourced; adversarial fact-check (Doc 4 §20 B) |
| L048 | Not sure? | STANDARD | ONERULE | ALL | done | All docs — every claim sourced; adversarial fact-check (Doc 4 §20 B) |
| L049 | Check it with agent-reach before you trust it. | STANDARD | ONERULE | ALL | done | All docs — every claim sourced; adversarial fact-check (Doc 4 §20 B) |
| L050 | ## 📏 Standards for every section | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L051 | - Every line on this page is a requirement (rule 1 at the top) — every heading, bullet, sub-bullet, and instruction gets done; nothing dropped or merged. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L052 | - Painkiller in an uncontested market. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L053 | The wedge must be BOTH a specific, painful, unsolved PROBLEM for a large, desperate group AND white space no major competitor already runs in the target region (§2). | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L054 | Miss either half and it's weak. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L055 | - Sourced or it doesn't ship. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L056 | Behind every pain, objection, competitor, belief, and mechanism: a verbatim quote + the source URL. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L057 | Never invent a quote, stat, competitor, or run length. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L058 | Can't verify it? | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L059 | Say so — don't pad. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L060 | - Source tags: every quote, number, and claim carries a tag pointing to its source — [S1], [S2]… — matching the numbered Sources list at the end of that doc (URL · platform · date). | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L061 | Also mark how solid it is: VERBATIM (page opened, wording confirmed) · SNIPPET (search-result text — confirm before live creative) · DATA (a tool's estimate, e.g. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L062 | Winning Hunter revenue) · INFERENCE (your reasoning, no source — keep these rare and always labelled). | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L063 | - Count it, don't guess. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L064 | Every pain, desire, objection, failed solution, trigger, misconception, and belief comes from the §2C customer data bank and is ranked by how many real snippets mention it (e.g. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L065 | "31 of 142"). | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L066 | No count = no ranking. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L067 | List every distinct one — exhaustive first, then ranked: pains · desires · needs · objections · failed solutions · triggers · misconceptions · beliefs she holds · emotional states → capture EVERY distinct item the data shows, each with its count, highest-first; never a tidy one or two. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L068 | A list that comes back with only 1–2 items means you under-collected — go back to the bank. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L069 | (Exception: the §9B chain keeps persuasion order — show each belief's count next to it.) | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L070 | - Minimums are targets, not quotas. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L071 | Fewer real ones exist? | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L072 | Give the real number + why — never pad with invented or weak items. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L073 | - Search snippets: Reddit / Amazon / Facebook often block full-page fetch. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L074 | Search-result snippets are real text — quote them, but flag them so the exact wording gets confirmed at the URL before it goes into live creative. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L075 | - Tight, and every section ends in a decision: the answer + the evidence + a "So What → do this" line. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L076 | No essays. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L077 | - List sections give the FULL set, not one example — real customers have a dozen pains, objections, failed solutions. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L078 | List them all (with quotes), tightly. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L079 | - Be decisive. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L080 | Commit to the market / wedge yourself, with evidence — lead with the pick + why, runner-up in one line. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L081 | Never hand back a "which one?" menu. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L082 | If Nikita hands you a market, pressure-test it honestly. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L083 | If no uncontested big painkiller market exists, say so plainly instead of forcing a weak wedge. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L084 | - Run it as a workflow: decide the uncontested painkiller MARKET first (§1–§2 draft). | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L085 | Then fan out one deep agent per area to COLLECT research in parallel (competitors + offers + white-space sweep · customer data bank / voice / beliefs / worldview / failed solutions · authority + science + compliance + mechanism · features / triggers / history). | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L086 | Every agent researches the CHOSEN market, not the generic product, gets the exact text of the sections it collects for (never a summary), and returns findings with quotes + URLs. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L087 | Then YOU write every section in page order from what they return — no section skipped, none written out of order — then run §20 last. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L088 | - "She" = the ICP, whatever the buyer's real gender. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L089 | Never assume female — follow the data. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L090 | - Report corrections honestly. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L091 | If verification kills an earlier conclusion, say it was wrong and what replaced it — never quietly drop it. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L092 | - Research + write only. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L093 | Never touch live ad accounts or spend. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L094 | Never place an order or enter payment details on any site. | STANDARD | STANDARDS | ALL | done | All docs — every section sourced [S#]/URL + solidity tag, counted from the §2C bank, ends in So What |
| L095 | ## 🧰 Skills to use here (run these — don't do it by hand) | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L096 | - research-doc — runs this whole doc for you, start to finish, from real sources. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L097 | Start here. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L098 | - If you ARE research-doc reading this page, you're already running it — mark it ✅ in §20. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L099 | - product-pulse — what real people say about the exact product (X + Reddit). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L100 | - agent-reach — web / Reddit / forum / TikTok research + fact-checking. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L101 | - First run agent-reach doctor --json. | TOOL | SKILLS | ALL | done | agent-reach CLI not installed → Firecrawl, logged 🔁 (Doc 4 §20 A) |
| L102 | CLI not installed? | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L103 | Use the Firecrawl MCP (firecrawl_search + firecrawl_scrape) for the same jobs and log it as 🔁 in §20. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L104 | - Firecrawl — scrapes competitor sites. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L105 | - = the Firecrawl MCP tools: firecrawl_search (find pages / snippets) + firecrawl_scrape (read a page; formats: ["query"] to pull specific facts). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L106 | - playwright-skill — walks competitor stores and pulls their offer, pages, and upsells. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L107 | - Run it headless (headless: true; npm run setup once). | TOOL | SKILLS | ALL | done | headless; wrapper absent (no npm setup) → Playwright library run directly (Doc 4 §20 A) |
| L108 | If Playwright fails, use browser-use and say so. | TOOL | SKILLS | ALL | done | browser-use MCP failed to connect; Playwright worked — said so (Doc 4 §20 A) |
| L109 | - Amazon trick: paste 5★ reviews into ChatGPT → why people love it (your angles). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L110 | Paste 1–2★ → their complaints (your objection list). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L111 | - How you (the AI) run this trick: collect the reviews yourself and do the sorting yourself. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L112 | Amazon review pages often need a login, so: firecrawl_scrape each top listing's /dp/ page (its top reviews + the "Customers say" summary) across 5–10 listings, and get 1–2★ wording via firecrawl_search (site:amazon.com "[product]" "one star", + Walmart / Trustpilot), tagged SNIPPET. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L113 | There's no ChatGPT step for you, and never pass reviews through a separate chat that strips the sources. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L114 | Keep the URL + star rating + date for every review you use, so every quote stays traceable and countable. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L115 | Log it in §20 as "Amazon trick ✅" (🔁 + why only if the /dp/ pages were walled too). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L116 | - Forum tactics: sort threads by replies / views to find the most-engaged ones; steal high-view thread titles as ready-made hooks / email subject lines. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L117 | - How: firecrawl_scrape [old.reddit.com/r/[sub]/search?q=[term]&restrict_sr=1&sort=comments](http://old.reddit.com/r/%5Bsub%5D/search?q=%5Bterm%5D&restrict_sr=1&sort=comments) (and forum lists sorted by replies) to find the most-engaged threads. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L118 | Blocked? firecrawl_search site:reddit.com/r/[sub] [term] (+ product-pulse), rank threads by the comment count shown, tag SNIPPET. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L119 | List the high-view titles in §14 as "Thread-title hooks". | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L120 | - SimilarWeb — competitor traffic + audience demographics. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L121 | - No SimilarWeb connector: firecrawl_scrape [similarweb.com/website/[domain]](http://similarweb.com/website/%5Bdomain%5D) — gives age + gender split (visits only as a range). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L122 | Exact monthly visits + history: Winning Hunter get_store_details (no demographics). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L123 | If SimilarWeb is blocked, mark §3 demographics INFERENCE. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L124 | - Audit first: before researching, study your current page (or the control you're modeling) and note what's weak. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L125 | - Winning Hunter — search_facebook_ads (sort_by: longestrunning = proven) · get_store_details (traffic, revenue, time in business, installed apps) · get_store_top_ads · find_similar_shops + brief_competitor (expand the competitor list) · search_exploding_topics (§0B fallback only) · search_tiktok_products / get_tiktok_product · search_tiktok_ads · search_google_ads. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L126 | Big ad-search results often save to a file — read them with jq, not the whole file. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L127 | - Facebook Ad Library — catches advertisers Winning Hunter misses and proves which region / language an angle is or isn't run in. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L128 | Browse [facebook.com/ads/library](http://facebook.com/ads/library) with playwright-skill / browser-use (set the country + "All ads"). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L129 | A facebook connector / Ad Library API only returns normal product ads for EU / UK — use it for EU / UK only. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L130 | Library won't render headless? | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L131 | Prove region / language with Winning Hunter search_facebook_ads (keyword + countries: [target] + languages), once for the target region and once for others, and log 🔁. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L132 | - TikTok + Google / Amazon / Etsy — the rest of the competitor + white-space sweep: TikTok ads via Winning Hunter search_tiktok_ads (pass countries) · Google ads via search_google_ads (pass country / domain) · Amazon / Etsy via firecrawl_scrape. | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L133 | - A tool here isn't available? | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L134 | See rule 2 at the top (substitute, name it, never silently skip). | TOOL | SKILLS | ALL | done | Doc 4 §20 A tools table |
| L135 | Where each skill is REQUIRED (every run): | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L136 | / Skill / tool / Must run in / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L137 | / --- / --- / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L138 | / research-doc / The whole page — it runs this page top to bottom / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L139 | / Audit first / Right after Pre-0 (your current page — or, for a new product, the highest-traffic competitor page a quick search turns up; §1 re-checks it). Output in Doc 1, right after Pre-0: the URL audited + what's weak / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L140 | / product-pulse / §2C · §10 · §14 · §20 / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L141 | / agent-reach / §2C · §5 · §10 · §10B · §12 · §18 · §18B · §20 (research + fact-check) / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L142 | / Firecrawl (MCP: firecrawl_search · firecrawl_scrape) / §0B · §1 · §2C · §5 · §10B · §13 · §13B · §15 · §18B (+ every agent-reach job if its CLI isn't installed) / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L143 | / playwright-skill / Audit first · §0B (Google Trends) · §1 (funnels + Ad Library) · §2 (Ad Library region check) · §15 (every product page, offer, cart, checkout) — browser-use if it fails / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L144 | / Amazon trick / §2C · §10 · §10B · §11 / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L145 | / Forum tactics / §2C · §5 · §14 · §18 / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L146 | / SimilarWeb / §1 (traffic) · §3 (demographics) / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L147 | / Winning Hunter / §0B · §1 · §15 (get_store_details apps → upsell apps) / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L148 | / Facebook Ad Library / §0B · §1 · §2 / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L149 | / TikTok + Google / Amazon / Etsy / §0B · §1 · §2 · §15 / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L150 | / Google Trends / §0B / | TOOL | SKILLMAP | ALL | blocked | Google Trends ❌ (429) → Exploding Topics 🔁 (Doc 4 §20 A) |
| L151 | / Notion connector / Funnel Map (open the Funnel Selection Board) · §15 (open the Offer Build reference) / | TOOL | SKILLMAP | ALL | done | Doc 4 §20 A tools table (each tool ran in its required sections) |
| L152 | / Google Drive / Delivery: the folder, the 4 Docs, the §2C Sheet / | TOOL | SKILLMAP | ALL | done | 🔁 Google Drive → Notion folder per Nikita (Doc 4 §20 A) |
| L153 | ## Fill these out, in order | DO | ORDER | ALL | done | All docs in page order |
| L154 | Pre-0 · Economics & KPIs (ask Nikita FIRST, before any research) — Get: target country / region + language (every "target region" check below uses this — never guess it) · your current product page / store URL (if any) · supplier product link (real price + full spec / feature list — §17 needs it) · landed cost per unit (product + shipping + fulfilment) · planned selling price + offer shape (single / BOGO / bundle) · processing % (default 3%). ⚠️ Use the REAL supplier price — never the fake AliExpress "welcome deal" first-order teaser. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L155 | Then show a KPI table (real math, show the formulas) for each offer variant — metrics as rows, offer variants as columns (max 4), formulas under the table: | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L156 | - Nikita = the person running this. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L157 | Wait for his answers. | DO | Pre-0 | Doc1 | done | Nikita approved the run-2 plan (groups, research picks lead, reuse run-1 rows, new Notion folder) before research |
| L158 | Can't ask in this run? | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L159 | Use what the request already gives. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L160 | Missing costs are fine (see below) — a missing target region is NOT: stop and ask. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L161 | - Contribution margin $ = Price − landed − processing − other (the most you can pay per order and break even). | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L162 | - Spelled out: CM $ = Price − (landed per unit × units in the order) − (processing % × Price) − other per-order costs (packaging etc.; 0 if none). | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L163 | - Contribution margin % = CM $ ÷ Price. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L164 | - Break-even ROAS = 1 ÷ CM% (= Price ÷ CM $). | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L165 | Break-even CPA = CM $. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L166 | - Target ROAS / CPA at ~20% and ~30% net — the "scale" line and the "kill" line. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L167 | - Formulas: Target CPA at n% net = CM $ − (n × Price). | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L168 | Target ROAS = Price ÷ Target CPA. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L169 | "Price" = the full order value of that offer variant (a bundle = the whole order). | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L170 | If CM% ≤ n, that target is impossible — say so. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L171 | - Scale line = the ~30% net CPA (at or under it → scale). | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L172 | Kill line = the ~20% net CPA (consistently above it → fix or kill). | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L173 | Show break-even next to both. | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L174 | - No costs yet? | DO | Pre-0 | Doc1 | done | Doc 1 · Pre-0 Economics & KPIs |
| L175 | Flag it, keep going, and add a reminder just above Doc 1's Sources list to send COGS to finish the table. | OUTPUT | Pre-0 | Doc1 | done | Costs known; reminder for CJ combined-parcel quote + CJ URL above Doc 1 Sources |
| L176 | 0 · Product & core problem — One line: what it is, the ONE problem it solves, who for. | DO | 0 | Doc1 | done | Doc 1 · §0 |
| L177 | Everything hangs off this. | DO | 0 | Doc1 | done | Doc 1 · §0 |
| L178 | Make sure the market that you are going to sell to is really needing a solution to there problem not just a want this will make the market actually passionate since they have a real big problem that they are needing help for. not just bringing it to a market that might want it. | DO | 0 | Doc1 | done | Doc 1 · §0 |
| L179 | - Mass desire test (Schwartz): you can't create desire — only channel one that already exists. | DO | 0 | Doc1 | done | Doc 1 · §0 |
| L180 | Score the desire behind this problem 1–5 on urgency (how badly she wants it fixed now) · staying power (does it keep nagging her, or fade?) · scope (how many people feel it). | DO | 0 | Doc1 | done | Doc 1 · §0 |
| L181 | Give real evidence for each score. | DO | 0 | Doc1 | done | Doc 1 · §0 |
| L182 | Low scores = a weak market — say so. | DO | 0 | Doc1 | done | Doc 1 · §0 |
| L183 | 0B · Demand & Seasonality (real numbers, not vibes) — Prove there's money here, and WHEN. | DO | 0B | Doc1 | done | Doc 1 · §0B |
| L184 | - Search trend: Google Trends for the problem + the product (5 years, target country) via playwright-skill / browser-use (Firecrawl gets blocked) — rising / flat / dying + the peak months. | TOOL | 0B | Doc1 | blocked | Google Trends HTTP 429 ×2 (Playwright, normal loads) — no 5-yr curve; manual 2-min check given (Doc 1 §0B) |
| L185 | Blocked? | DO | 0B | Doc1 | done | Doc 1 · §0B |
| L186 | Use Winning Hunter search_exploding_topics (volume + monthly history + growth), label it "not country-filtered", and log it in §20. | TOOL | 0B | Doc1 | done | Doc 1 · §0B |
| L187 | - Marketplace demand: Amazon — top listings' review counts + "bought in past month" badges (firecrawl_scrape the Amazon search-results page with formats: ["query"]). | TOOL | 0B | Doc1 | done | Doc 1 · §0B |
| L188 | TikTok Shop — units / sales via Winning Hunter (search_tiktok_products with country: [target] → get_tiktok_product slices "metrics" + "history"; target country not covered? say so). | TOOL | 0B | Doc1 | done | Doc 1 · §0B |
| L189 | - Ad demand: how many advertisers are running this product / problem right now (Winning Hunter search_facebook_ads: 3–5 keywords — product, problem, 2 synonyms — with countries: [target]; page with the scroll cursor until no new advertisers appear, max 5 pages per keyword; de-dupe advertisers with jq; report the count + the queries used — plus the Facebook Ad Library) and how long the longest have run. | TOOL | 0B | Doc1 | done | Doc 1 · §0B |
| L190 | - Verdict: growing / stable / declining · peak months · launch-timing call. | DO | 0B | Doc1 | done | Doc 1 · §0B |
| L191 | Every number gets its source + date. | DO | 0B | Doc1 | done | Doc 1 · §0B |
| L192 | 1 · Competitor scan (do this first) — Reverse-engineer what's already working; never copy it. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L193 | Confirm real demand exists (winning ads / scaled stores are out there). | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L194 | - Long-list first: before picking, list EVERY advertiser / store selling this found across all sources (name · URL · # active ads · longest-running ad · region). | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L195 | Expand it with Winning Hunter find_similar_shops (each competitor's domain) + brief_competitor. | TOOL | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L196 | Aim for 10+, or give the real number and why. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L197 | The 3 direct picks below = the 3 with the most proven spend (longest-running + most active ads). | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L198 | - Pick 3 direct competitors (same/similar product, same market, actively running paid ads). | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L199 | For each, capture: | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L200 | - Shop signals: monthly traffic · how long in business · # active ads · longest-running ad (= proven) · most-duplicated ad (= their real winner) · other pages running ads to the same domain (= whitelisting / creator angle). | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L201 | - Most-duplicated: Winning Hunter search_facebook_ads with keyword: [domain], searchkeyword: "landingurl", min_duplicates: 2, sort_by: longestrunning — the creative with the most duplicates = their winner. | TOOL | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L202 | - Traffic: get_store_details covers Shopify stores only — not Shopify / not found → the SimilarWeb range, labelled. | TOOL | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L203 | - Ads: the pain (or desire) they lead with · their mechanism · the avatar · the creative format (UGC / native / static / animation) · the hooks/ideas that repeat across ads. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L204 | - Log at least their top 10 ads (get_store_top_ads with their domain — platform meta, then tiktok / google — + search_facebook_ads sort_by: longestrunning). | TOOL | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L205 | One row each: ad URL · start date · days running · format · what it leads with (plain claim / bigger claim / mechanism / upgraded mechanism / identity) · hook (first line). | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L206 | Keep it as one ad-log file — §8's counts and the TAKEN map come from it. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L207 | - Funnel: where the click goes (PDP / advertorial / listicle / quiz) and the one job that page does. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L208 | - Offer: price · guarantee · bonus · bundle · upsell — and where it's weak / missing (that's your opening). | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L209 | - Then 3 indirect competitors — take the dominant pain/desire/avatar you found and search the PAIN, not the product (magnesium → search "inflammation") to find bigger brands selling to that same pain. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L210 | Steal what's working there; it's less saturated in your category. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L211 | - Map competitors thoroughly — Winning Hunter (longest-running ads + store details + top ads) + Facebook Ad Library + TikTok + Google / Amazon / Etsy. | TOOL | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L212 | Re-check Audit first: if the highest-traffic competitor isn't the page you audited, audit it too and update Doc 1. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L213 | Then write a TAKEN map covering the whole long-list, one line per incumbent: owned angle + region + active / abandoned. | DO | 1 | Doc1 | done | Doc 1 · §1 (1A–1E) |
| L214 | 2 · Your gap (Purple Ocean) — The one angle nobody else is hitting, built on Section 1 (change the angle on demand that's already proven — don't invent a market no one buys). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L215 | Find your edge from three gaps, in this order: | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L216 | - 1. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L217 | Creative-format gap — a format competitors are barely using (native when all are polished; UGC / animation when all are static). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L218 | Take a proven message, express it in a fresher format. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L219 | - 2. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L220 | Mechanism gap — a faster / easier / better "how" (e.g. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L221 | "clears it in 30 minutes"). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L222 | Speed or ease becomes the differentiator. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L223 | - 3. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L224 | Avatar gap — a buyer no one targets (mouth spray → cigar smokers, not students). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L225 | Rebuild the creative + page around that avatar. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L226 | Pick the first gap you can genuinely win. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L227 | - A format or mechanism gap is HOW you attack — the wedge you commit must still name the MARKET (who + their painful problem) that passes the gate below. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L228 | - Check all three first: one line per gap with the §1 evidence for or against it (which competitor ads prove it's open or closed) — then pick. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L229 | - The Purple Ocean Gate — the gap must pass ALL of this before you commit: | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L230 | - PAINKILLER — a specific, desperate, under-served PROBLEM (not a "nicer [product] for [broad audience]" want). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L231 | The market must genuinely NEED a fix (§0). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L232 | - UNCONTESTED — no major competitor already runs this market / angle in the target region. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L233 | An angle the biggest competitor already runs = automatic FAIL (red ocean). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L234 | A proven-but-abandoned angle, or one only run in another region / language = de-risked white space — take it. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L235 | - A MARKET, not an ANGLE — a market = a large group bound by one massive painful problem they'll pay to solve (a whole brand + 20 ads). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L236 | An angle = one entry scenario (one ad). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L237 | If you wrote a single occasion, zoom out to the market behind it. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L238 | - 3 automatic fails: (1) vitamin ("a nicer [product]") · (2) red ocean (your biggest competitor's own angle) · (3) angle-as-market (a single scenario). | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L239 | - Before you commit the draft, answer in writing: "Which competitor is already running this exact angle, and where?" If one runs it in your target region, it's NOT purple — find the gap they miss. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L240 | - Commit — lead with your pick + the evidence; note the runner-up in one line. | DO | 2 | Doc1 | done | Doc 1 · §2 (LOCKED in Doc 3 §11; §20 correction) |
| L241 | 2B · Compliance & Claims — SAY / DON'T SAY (do this before writing any copy — and re-check the §2 draft angle against it) — Identify the product's ACTUAL category and pull the rules that apply to IT (don't paste supplement rules onto a mobility aid). | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L242 | Output a two-column ✅ SAFE TO SAY / ❌ NEVER SAY table. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L243 | - Ad-platform policy (Meta especially): | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L244 | - Personal Attributes rule — the #1 silent killer. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L245 | Never imply you know the viewer's personal attributes — health condition, disability, age, religion, race / ethnicity, sexual orientation, gender identity, financial status, criminal record. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L246 | "Do you have [condition]?" / "Your [condition]…" = instant reject; the word "other" ("meet other [X] parents") also triggers it. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L247 | Reframe to third person / self-identifying: "Some people who…", "For anyone who…". | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L248 | Naming a condition is allowed if it doesn't imply the viewer has it ("New bunion relief now available" ✅ vs "Your bunion pain…" ❌). | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L249 | Keep deep condition education on the LANDING PAGE — Meta reviews landing pages too, so the same rules apply there. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L250 | - No unsubstantiated health / condition / cure claims — no "cures / treats / heals / prevents / reduces [condition]". | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L251 | Sell feeling / comfort / routine / function + outcome. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L252 | - Watch before/after, idealized-body, and medical-device implications. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L253 | - Category-specific — look up the real rules: supplements (health-claim substantiation, no disease claims) · kids / baby (CPSIA / ASTM F963, choking warning, no SIDS / "safe for crib") · beauty (cosmetic-vs-drug line) · mobility / daily-living aids (usually Class I / freely advertisable — the risk is copy language, not the product class) · sensory / "calming" (treat as health claims needing substantiation). | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L254 | - Legal / claims substantiation (FTC / FDA-style): structure/function + comfort claims OK-ish; disease-treatment / efficacy claims not. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L255 | Flag shaky science and product/mechanism mismatches honestly — never claim a mechanism the product doesn't own. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L256 | Testimonials ≠ substantiation for a health claim. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L257 | - Add a one-line "why your last ads probably got rejected" if relevant, and for restricted audiences a short "how to reach them WITHOUT naming the condition" note. | DO | 2B | Doc4 | done | Doc 4 · §2B |
| L258 | 2C · Customer data bank (build it BEFORE §3 — every customer section from §3 to §18 is pulled from it) — Collect what real people actually say about this problem, this product, and the alternatives they've tried. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L259 | - How much: at least 100 snippets, aim for 150+, from at least 4 source types: Reddit · Amazon 1–2★ AND 4–5★ reviews · TikTok / YouTube comments · forums / Trustpilot / Facebook groups · X (via product-pulse). | TOOL | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L260 | Use the forum tactics + Amazon trick above to collect it. | TOOL | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L261 | TikTok / YouTube comments: playwright-skill on the video URL, scroll to load the comments, save the text — won't load? say so and use the other source types. | TOOL | 2C | Doc2 | blocked | YouTube comments loaded for 5 videos then 429; TikTok comments login-walled (not bypassed); said so; 8 source types used (Doc 2 §2C) |
| L262 | Can't reach 100? | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L263 | Report the real number and why — never pad. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L264 | - Every snippet: the verbatim quote · URL · platform · date · star rating (if it's a review) · tags: pain · desire · need · objection · failed solution · trigger · misconception · belief · emotional state · awareness stage · burned / skeptical · authority they trust · buyer group (who's posting) · great phrase. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L265 | - Keep it as a file from the first snippet: one local CSV, one row per snippet (quote · URL · platform · date · stars · one column per tag). | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L266 | Every parallel agent writes the same columns. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L267 | Merge + remove duplicates (same URL + quote) before counting. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L268 | Every count on this page is a script / jq tally of that file — never an estimate. | TOOL | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L269 | Paste the tally into Doc 2 as the summary below (top 10 per tag) — the full counts stay reproducible from the CSV. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L270 | This same file is uploaded as the §2C Sheet. | OUTPUT | 2C | Doc2 | done | The same CSV = the §2C Data Bank Notion database |
| L271 | - Count: tally every tag. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L272 | Every customer list from §3 to §18 (pains, desires, needs, objections, failed solutions, triggers, misconceptions, beliefs, emotional states, authorities, sub-avatars) is ranked by these counts. | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L273 | - Save it: the full bank becomes the Google Sheet in the product's Drive folder (one row per snippet — uploaded at delivery, after §20). | OUTPUT | 2C | Doc2 | done | Full bank → Notion database in the folder (override of Google Sheet), uploaded after §20 |
| L274 | Doc 2 opens with the summary: snippets per source type + the top 10 of each tag — one line per tag (Pain: item (n) · item (n) · …), no quotes there (the quotes live in their sections). | DO | 2C | Doc2 | done | Doc 2 · §2C summary + §2C Data Bank (Notion database) |
| L275 | 3 · Ideal customer (ICP) — Exactly who she is: demographics + mindset + situation. | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L276 | One real person, not "everyone." | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L277 | - Worldview (write as one of them): capture her religious · political · social · economic attitudes + prejudices / stereotypes (what she rolls her eyes at, who she thinks "gets it"). | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L278 | Mirror these so the copy reads like a familiar voice, not an outsider. | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L279 | Sum her core view of life, love & family in 1–3 sentences. | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L280 | - Required fields: age range · life stage · household · income band · job type · country / urban-rural · a typical day when the problem hits. | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L281 | Next to each field: the §2C snippet count or SimilarWeb figure behind it. | TOOL | 3 | Doc2 | done | Doc 2 · §3 |
| L282 | Any field with no data = INFERENCE. | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L283 | Every worldview line quotes at least one §2C snippet or is marked INFERENCE. | DO | 3 | Doc2 | done | Doc 2 · §3 |
| L284 | 3A · Sub-avatars (the scale targets) — §3 is who you launch to. | DO | 3A | Doc2 | done | Doc 2 · §3A (G2, G1, G5, G4 at full depth) |
| L285 | Now list the 3–5 OTHER real buyer groups the §2C data bank shows (different ages, jobs, situations, gift-buyers…) — the ones you'll target once the store gets its first buyers and you start scaling. | DO | 3A | Doc2 | done | Doc 2 · §3A (G2, G1, G5, G4 at full depth) |
| L286 | For each: who they are · their #1 pain in their own words (quoted + sourced) · how big the group looks (how many §2C snippets come from them) · where they gather (subreddits, groups, interests) · the angle that would open them. | DO | 3A | Doc2 | done | Doc 2 · §3A (G2, G1, G5, G4 at full depth) |
| L287 | Rank them. | DO | 3A | Doc2 | done | Doc 2 · §3A (G2, G1, G5, G4 at full depth) |
| L288 | Every sub-avatar must come from real data — no invented personas. | DO | 3A | Doc2 | done | Doc 2 · §3A (G2, G1, G5, G4 at full depth) |
| L289 | 4 · Contrast — Do the opposite of the market. | DO | 4 | Doc4 | done | Doc 4 · §4 (LOCKED) |
| L290 | Stand out like black letters on white paper. | DO | 4 | Doc4 | done | Doc 4 · §4 (LOCKED) |
| L291 | Name the exact contrast. | DO | 4 | Doc4 | done | Doc 4 · §4 (LOCKED) |
| L292 | - How: take the 5 things nearly all §1 competitors do the same way (visual style · tone · claim type · offer shape · page format). | DO | 4 | Doc4 | done | Doc 4 · §4 (LOCKED) |
| L293 | For each: the evidence + your exact opposite. §4 = execution contrast; §4B = identity — don't repeat §4B here. | DO | 4 | Doc4 | done | Doc 4 · §4 (LOCKED) |
| L294 | 4B · Brand Positioning System (how to actually stand out — run this for every product) — A different ad angle is not enough in a saturated market. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L295 | When you can't outspend the incumbents, you win by owning a whole-brand IDENTITY they structurally can't copy. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L296 | Don't sell the product's benefit — build a brand people JOIN. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L297 | Model: Liquid Death — a zero-differentiation commodity (canned water) that beat billion-dollar giants on identity + attitude alone, not on product. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L298 | Research and LOCK these for the product before you build anything: | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L299 | - The Enemy — what/who is the brand against? | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L300 | Usually the dishonest / lazy / corrupt way the whole category currently operates (fake experts, hidden fees, overclaiming, the thing that quietly screws the customer). | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L301 | A brand with an enemy is a brand people rally to. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L302 | Find the enemy inside the category's own 1★ reviews and repeated complaint patterns. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L303 | - What we stand FOR — the belief / truth we'll tell that the category won't (even when it costs us a sale). | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L304 | This is the identity the customer adopts by buying from us. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L305 | - The Attitude — the personality + tone NO incumbent occupies (if they're all warm / soft / polished → be blunt / funny / raw; if all clinical → be human). | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L306 | Attitude is the moat: a big corporate operation can't authentically switch into it. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L307 | - The Uncopyable Test — ask: "if the #1 competitor tried to adopt this positioning tomorrow, would it INDICT them or make them look insane?" If yes → real moat. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L308 | If they could just bolt it on (a discount, a feature, a nicer photo) → it's not positioning, keep digging. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L309 | - Whole-store thread — the position must live on EVERY surface, not one ad: the name, the About-page manifesto, the product-page proof, the offer / guarantee, which reviews you show, the voice. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L310 | If it only lives in the ad, it's an angle, not a brand. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L311 | - Weakness-as-weapon — being small / new / broke is an ASSET here: underdog vs. rich incumbents = David vs. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L312 | Goliath, and people root for David. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L313 | Name how the brand's limitation becomes its story. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L314 | - Guardrails: (1) you must actually BE what you claim — a hypocritical position detonates harder than none; (2) attack the category PATTERN, never name-and-shame a specific competitor (defamation risk). | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L315 | - Output (lock one line): "We are the [attitude] brand that stands FOR [truth] and AGAINST [enemy] — the [category] for people who [identity]." Everything downstream (§13B story, §14 voice, the offer, the store) executes this one line. | DO | 4B | Doc4 | done | Doc 4 · §4B (LOCKED in Doc 3 §11; §20 refined) |
| L316 | 5 · Awareness level — Where is she: Unaware → Problem → Solution → Product → Most aware? | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L317 | Each level is spoken to differently. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L318 | Then pick the funnel that moves her to buy. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L319 | - Here, name the funnel type her stage needs; the final pick is made once, in the Funnel Map. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L320 | - Measure it, don't guess (two ways): (1) Discourse-volume proxy — search "[problem] + Reddit" (and forums). | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L321 | Pages and pages of threads = she clearly knows the problem (at least problem-aware); barely any threads = low awareness (unaware/problem-aware) → you'll have to build the problem before you sell. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L322 | How burned / skeptical she is gets measured in §8, not here. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L323 | (2) Real-data split — sort the §2C snippets by stage and count them: "what is this / why does this happen" = problem-aware · "does [solution type] work? / what actually helps?" = solution-aware · "[brand] review / is [brand] legit?" = product-aware · "best deal / discount code for [brand]" = most aware. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L324 | Report the counts as a % split across the 5 stages, so you enter where the MAJORITY actually sits (most-aware is almost always the smallest slice). | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L325 | Unaware people don't post — that slice can only be estimated, so label it INFERENCE. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L326 | - Low awareness? | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L327 | Bridge a symptom → the problem. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L328 | When the market doesn't know the problem exists, don't sell the problem cold. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L329 | Find a symptom she already notices and already wants gone (or one that becomes urgent once she learns what it means), then walk her: symptom → hidden problem → your product. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L330 | Hunt symptoms in the research (Google AI-overview for "signs of [problem]", then "[symptom]" + Reddit) and pick the ones that (a) she'd act on anyway, or (b) turn scary once tied to the real cause. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L331 | - No AI-overview tool: firecrawl_search "signs of [problem]" → read the top medical / expert pages (e.g. | TOOL | 5 | Doc1 | done | Doc 1 · §5 |
| L332 | Mayo Clinic, Cleveland Clinic, NHS), then search each symptom + Reddit. | DO | 5 | Doc1 | done | Doc 1 · §5 |
| L333 | 6 · Consciousness level — Her emotional state: where she sits on the [Map](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6869b8ab-b480-4897-854f-6525d7b26cc9_3573x3195.jpeg) ladder right now (Shame · Guilt · Apathy · Grief · Fear · Desire · Anger · Pride) and where the copy moves her (Courage → Neutrality → Willingness → Acceptance). | DO | 6 | Doc3 | done | Doc 3 · §6 |
| L334 | Use the emotion names only — ignore the numbers on the map (they aren't real science and never go in copy). | DO | 6 | Doc3 | done | Doc 3 · §6 |
| L335 | Back her current state with real quotes + the §2C emotional-state tag counts (e.g. | DO | 6 | Doc3 | done | Doc 3 · §6 |
| L336 | Fear 38 · Shame 21 · Apathy 9). | DO | 6 | Doc3 | done | Doc 3 · §6 |
| L337 | (Awareness = how much she knows. | DO | 6 | Doc3 | done | Doc 3 · §6 |
| L338 | Consciousness = how she feels about it.) | DO | 6 | Doc3 | done | Doc 3 · §6 |
| L339 | 7 · Funnel level — Top, middle, or bottom — where this traffic sits. | DO | 7 | Doc1 | done | Doc 1 · §7 |
| L340 | - "This traffic" = the cold traffic your launch ads will reach (the §3 ICP at her §5 stage). | DO | 7 | Doc1 | done | Doc 1 · §7 |
| L341 | State the level and what it means for the ad's job and the first page (pre-sell vs. straight to the product page). | DO | 7 | Doc1 | done | Doc 1 · §7 |
| L342 | 8 · Sophistication stage — How tired the MARKET is ([map](https://swipefile.com/wp-content/uploads/2020/07/stages-of-market-sophistication.png)). | OUTPUT | 8 | Doc1 | done | Doc 1 · §8 |
| L343 | Skepticism rises with every level (more time + more buying experiences = more burned). | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L344 | Match your marketing to the level: | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L345 | - Level 1 — Birth of the market: just make the claim. | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L346 | - Level 2: make the claim BIGGER than the competition's. | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L347 | - Level 3: introduce a mechanism — a logical reason WHY your claim is achievable (Section 13). | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L348 | - Level 4: create a BETTER mechanism, or an upgraded version of the previous one. | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L349 | - Level 5: skepticism is at the max — she no longer believes in ANY mechanism. | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L350 | New advanced strategies must be activated: sell identification (who she is + what the brand stands for, §4B), not another mechanism. | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L351 | - Prove the level, don't pick it by feel: classify every §1 competitor ad you captured by what it leads with (plain claim · bigger claim · mechanism · upgraded mechanism · identity) and count them (e.g. | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L352 | "14 of 22 lead with a mechanism"). | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L353 | Add the §2C count of burned snippets ("tried everything" · "scam" · "nothing works"). | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L354 | State the level + the evidence. | DO | 8 | Doc1 | done | Doc 1 · §8 |
| L355 | 9 · Beliefs: now → needed — What she believes now vs. what she must believe to buy. | DO | 9 | Doc3 | done | Doc 3 · §9 (rewritten in §13 Step 7) |
| L356 | Map how to change it. | DO | 9 | Doc3 | done | Doc 3 · §9 (rewritten in §13 Step 7) |
| L357 | Pull from real reviews/forums/Reddit. | DO | 9 | Doc3 | done | Doc 3 · §9 (rewritten in §13 Step 7) |
| L358 | - The One Belief (Evaldo Albuquerque): sum the whole sale in one line before you write §9B — "This new opportunity — [name the opportunity] — is the key to [her #1 desire by §2C count], and it's only attainable through [your mechanism — working name now]." Every belief in §9B leads to this one. | DO | 9 | Doc3 | done | Doc 3 · §9 (rewritten in §13 Step 7) |
| L359 | It's a DRAFT here: rewrite it at the end of §13 with the final mechanism. | DO | 9 | Doc3 | done | Doc 3 · §9 (rewritten in §13 Step 7) |
| L360 | 9B · The Belief Chain (North Star) — the ≤6 beliefs she MUST hold before she'll buy, written as "I believe that…" statements, in order. | DO | 9B | Doc3 | done | Doc 3 · §9B |
| L361 | This is the destination you lead her to before you mention the offer — every line of copy walks her one step closer. | DO | 9B | Doc3 | done | Doc 3 · §9B |
| L362 | Marketing = changing what she believes now into these. | DO | 9B | Doc3 | done | Doc 3 · §9B |
| L363 | Build it from the research (believe now → the gap → the belief that unlocks the buy). | DO | 9B | Doc3 | done | Doc 3 · §9B |
| L364 | - Each belief: what she believes now (quote + §2C count) → the belief she needs → the proof that moves her (§11 / §13 proof list — fill from §11 / §13 when written; §13's last bullet re-checks §9B). | DO | 9B | Doc3 | done | Doc 3 · §9B |
| L365 | 10 · Everything about the ICP — Pains · objections · needs · core desires / dream outcome · misconceptions · mindset (psychographics) · key experiences & moments · and what she's already tried and failed (failed solutions). | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L366 | All from real reviews / forums / Reddit / Amazon — no assumptions. | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L367 | - Pulled from the §2C data bank — list every distinct one, then rank — every pain, desire, objection, need, and misconception in the data gets listed (all of them, not a top handful), each showing how many snippets mention it, highest first, with its 1–2 best quotes + sources. §10B (failed solutions) and §11 (objections) go deeper and refer back to these items by name — never re-paste the same quote. | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L368 | - Past victories + failures: where she's WON before (what worked, even briefly — shows what she already believes works + gives you aspirational proof) AND where she's FAILED (the let-downs that made her cynical). | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L369 | - Product failures → refer to §10B items by name. | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L370 | Only add here the failures that weren't a product (a diet, a doctor visit, a habit change). | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L371 | - Goals — near + far: her short-term wins (what she wants this week/month) AND her long-term dream outcome. | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L372 | Hit both — the near-term win earns the click, the long-term dream sells the identity. | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L373 | - The 4 forces (Jobs-to-be-Done — she only switches when Push + Pull beat Anxiety + Habit): Push — the pain pushing her away from what she does now · Pull — the dream pulling her toward something new · Anxiety — her fears about the NEW thing (will it work, is it a scam, will it fit, is it a hassle) · Habit — what keeps her stuck with the old way (comfort, sunk cost, "it's fine for now"). | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L374 | Anxiety + habit are why people DON'T buy — each one gets answered in §11. | DO | 10 | Doc2 | done | Doc 2 · §10 |
| L375 | 10A · Desire Ladder (surface → core) — run on ALL desires, every time — Ranking desires by raw §2C count tells you the desire she says most, not the one that actually drives the buy — so ladder every one. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L376 | For each surface desire from the §10 list (all of them, not a top handful), ask "why does she want that?" → answer in her words → ask again → 3–5 times, until you hit a core human driver (status · belonging/connection · security · freedom/autonomy · control/certainty · identity/self-image · significance · love · self-worth · time — plus any the data shows). | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L377 | Stop a ladder when the next "why" just repeats the last answer — that's the root. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L378 | - Ladder them ALL, extract every core — run the ladder on every surface desire you can get from §2C and pull out every distinct core desire that surfaces. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L379 | Don't force them down to one or two; multiple real core drivers is the point — capture all of them. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L380 | - Then rank the cores — once every desire is laddered, tally how many surface desires + §2C snippets roll up into each core driver and rank the cores highest-first. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L381 | This ranked core list is what actually drives her — stronger than the surface ranking. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L382 | - Anchor every rung in data — each "why" = a §2C snippet (quote + count) or marked INFERENCE. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L383 | Never invent a deeper motive the data doesn't show. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L384 | - Output: (1) the full map — surface desire (n) → why → why → CORE DRIVER for every desire; (2) the ranked core-desire list, each core with its rolled-up count + the surface desires feeding it. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L385 | - Wire it in — the surface desire = what the hook/ad says (she recognizes it); the top cores = what §4B identity, §9 One Belief and §13B story resonate on (why she buys). | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L386 | Repoint the §9 One Belief at the #1 core desire, not the top surface one. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L387 | - Mirror of §13: §13 ladders the problem to its root cause ("why is this happening?"); this ladders the desire to its root ("why does she want this?"). | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L388 | A launch needs both. | DO | 10A | Doc2 | done | Doc 2 · §10A |
| L389 | 10B · Existing Solutions Teardown — tear apart every alternative she already uses: | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L390 | - What she uses now — all of it (competitors, DIY, home remedies, doing nothing). | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L391 | - What she LIKES about it — keep this in your offer too. | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L392 | - What she DISLIKES about it — this is your differentiation. | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L393 | - Horror stories — the worst experiences people had with those solutions (grab the real quotes — they go straight into copy). | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L394 | - Do they even believe these solutions work? — if YES, you've got more convincing to do; if NO, capture exactly why they gave up. | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L395 | - Source: Amazon 1★ + 5★, forums, Reddit. | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L396 | - Rank the alternatives by §2C failed-solution count; at least 1 sourced horror-story quote + 1 like / dislike quote for each. | DO | 10B | Doc2 | done | Doc 2 · §10B |
| L397 | 11 · Objections → answers (2 columns) — Every worry you don't answer, she answers for herself, then leaves. | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L398 | For each: say the worry in her own words → kill it with proof (guarantee, a number/study, a testimonial from someone like her, a demo, or an honest trade-off). | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L399 | Run this checklist so none slip through: price · "will it work" · "for someone like me" · trust/scam · ease of use · upkeep/cost · time to results · returns/guarantee · looks. | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L400 | Power move: raise the product's most obvious flaw first, then flip it — it reads as honesty. | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L401 | (Amazon 1–2★ mining fills this fast.) | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L402 | - Rank + reality-check: list objections highest §2C count first. | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L403 | Tag every proof HAVE NOW · CAN CREATE before launch (a demo to film, a guarantee, a spec photo) · DON'T HAVE (e.g. reviews for a new store). | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L404 | An objection whose only answer is DON'T HAVE is flagged OPEN, not answered. | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L405 | The count + proof tag go inside the answer cell, so it stays 2 columns. | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L406 | - Now LOCK §2, §4, and §4B: go back and update them with what §10–§11 found (the enemy and the real gap live in the 1★ reviews and objections). | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L407 | Write what changed from the draft — and if the MARKET itself changed (not just the angle), redo §0–§11 for the new market (re-run the §2 gate) and say so. | DO | 11 | Doc3 | done | Doc 3 · §11 (+ LOCK note) |
| L408 | 12 · Authority figure — Who SHE actually trusts in this niche (don't assume a doctor). | DO | 12 | Doc3 | done | Doc 3 · §12 |
| L409 | Borrow that trust in your store + copy. | DO | 12 | Doc3 | done | Doc 3 · §12 |
| L410 | - List the top 3–5 by §2C count. | DO | 12 | Doc3 | done | Doc 3 · §12 |
| L411 | For each: name · type (doctor / creator / community figure / fellow sufferer) · reach · a quote showing she trusts them + URL · how the store can borrow that trust without implying they endorse you. | DO | 12 | Doc3 | done | Doc 3 · §12 |
| L412 | 13 · Unique mechanism (UMP → UMS) — The logical reason this product works when everything she tried didn't. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L413 | It becomes the spine of the ad + advertorial later. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L414 | This step is RESEARCH: find, document and prove the mechanism in full — don't write final copy here. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L415 | The more crowded the market (§8), the more this matters, and in a crowded market the clearest mechanism wins, not the cleverest. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L416 | - What a mechanism IS: an explanation that answers 4 questions, in order: | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L417 | - Why does her problem exist (the hidden root cause)? | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L418 | - Why did everything she tried fail? | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L419 | - What actually needs to happen instead? | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L420 | - How does this product make that happen? | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L421 | - What it is NOT: a feature, an ingredient list, a benefit, an outcome, a product name, a slogan, or science words on their own. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L422 | Ingredients, specs and design are evidence for the mechanism, never the mechanism itself — research them fully anyway, they're the proof. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L423 | - 🐱 UMP vs UMS (research both fully — you can't define either until the research surfaces them): | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L424 | - UMP = mechanism of the PROBLEM — the hidden root cause behind her symptom. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L425 | A strong UMP takes the blame off her: it wasn't that she didn't try hard enough, it's that everything she tried treated the symptom, not the cause. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L426 | - UMS = mechanism of the SOLUTION — what this product does that gets around that exact cause. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L427 | It must feel inevitable after the UMP: if the UMP says "X is broken," the UMS acts on X. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L428 | Research exactly how this product does that — the spec / ingredient / dose / process / design that lets us claim it, and what separates it from the category + cheaper lookalikes. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L429 | - Step 1 — Gather the raw material. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L430 | - Start with what's already here: §10B (existing solutions) + the §2C failed-solution / misconception / belief tags. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L431 | - Then go get more. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L432 | The research so far was collected for other sections and is almost never enough for the mechanism. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L433 | Run dedicated research for this step — her side (reviews, Reddit, forums, comments, competitors' 1★ reviews: why fixes failed + what she thinks causes it), the science side (studies, medical / expert sources, how the underlying problem actually works), the competitor side (their mechanism claims, so we know what's taken) and the product side (spec / ingredient data). | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L434 | Keep going until every link in Step 2 is backed by real sources; if something truly can't be found, say so and log it as a gap. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L435 | - Capture everything — don't filter yet: everything she tried that didn't work (+ her own explanation why) · everything that worked only temporarily (+ why it came back) · everything she blames herself for · what she currently believes causes it (right and wrong) · what experts / sources say the real cause is (with link). | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L436 | Quote the source for every point. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L437 | - Step 2 — Map the problem as a 4-link chain (every link fully documented, with sources): | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L438 | - Trigger — what starts it. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L439 | - Hidden process — what happens that she can't see. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L440 | This is the core of the UMP; research it deepest. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L441 | - Visible symptom — what she actually notices. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L442 | - Why the failed solutions missed it — show, solution by solution, that they act on the symptom and never on the hidden process. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L443 | - Step 3 — Map the solution. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L444 | For the product, document: exactly which link of the chain it acts on and how · every spec / ingredient / dose / process / design detail that supports that (with proof for each) · what the product does NOT do, so we never claim it. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L445 | - Step 4 — Draft at least 3 UMP → UMS candidate pairs. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L446 | Every pair must come from THIS market's research. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L447 | There's no fixed sentence pattern to follow — for each pair, find the framing that fits what the research actually shows, and explore different ways of explaining the cause and the fix until each one reads clearly and naturally to her. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L448 | Study how the strongest competitors and adjacent markets explain their mechanisms for inspiration on structure, but never copy their wording or their mechanism. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L449 | - Step 5 — Run every candidate pair through these checks. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L450 | Record the result; don't delete a candidate for failing — note why. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L451 | - 90% familiar, 10% new: write down what part she already believes, and the ONE new piece the mechanism adds. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L452 | All new = she won't believe it. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L453 | Nothing new = not a mechanism yet — keep researching. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L454 | - Clarity test: could an 11-year-old repeat it back after hearing it once? | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L455 | If it needs a long explanation, note the simplest plain-English version you can write, in her words, at a 5th–8th grade level. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L456 | - Plain-words test for any term we might use: say just the term with no explanation — could a stranger guess what it means? | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L457 | Record which terms pass and which don't. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L458 | AI-generated terms usually fail; check every one. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L459 | - Honesty check (§2B): does the product actually own this mechanism, and is every claim sayable? | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L460 | If the product and the mechanism don't match, flag the gap plainly. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L461 | - Step 6 — Score and pick a lead. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L462 | For each pair score: proof available now (Y/N) · already used by a §1 competitor (check the TAKEN map — quote the ad if yes) · sayable under §2B (Y/N) · passes the clarity test (Y/N) · 90/10 split (the familiar part / the new part) · how strongly the research supports it (# sourced quotes + studies) · fit with the §8 sophistication stage: Stage 2–3 → a clear mechanism alone can win · Stage 4 → it must be an upgraded mechanism that explains why the mechanisms already in the market fall short · Stage 5 → the mechanism carries the identity rather than leading. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L463 | Pick a lead pair and show every score. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L464 | Keep all 3 pairs and all research in the doc — runners-up become angles and backups. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L465 | - Step 7 — Finish. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L466 | - Core metaphor: one simple picture that makes the lead mechanism instantly graspable — research what she already compares it to in her own words. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L467 | - Proof list: match every mechanism claim to proof — a study (with link), a demo you can film, a spec / material fact, or a real customer result (quoted + sourced). | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L468 | No proof yet → go research it; still can't find it → flag it as a gap. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L469 | Never drop it silently. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L470 | - One-sentence summary of each: "UMP: …" and "UMS: …" in her words, at a 5th–8th grade level. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L471 | - Now rewrite the §9 One Belief with this lead mechanism, and re-check §9B against it. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L472 | Write what changed. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L473 | - Lifespan: the lead mechanism becomes the brand's mechanism — lock it after the first ad test confirms it. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L474 | Ads, angles and sub-avatars can each open from a different link in the chain, but they all lead to the same UMS. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L475 | Only revisit the core mechanism if: tests show it doesn't land · the market saturates on it (raise it a level rather than replacing it) · it's a new product with a different root cause · compliance forces it. | DO | 13 | Doc3 | done | Doc 3 · §13 (Steps 1–7) |
| L476 | 13B · Discovery Story — the origin story of the mechanism/product: the struggle before it, how it was "discovered," the turning point. | DO | 13B | Doc3 | done | Doc 3 · §13B |
| L477 | This is the spine of the advertorial. | DO | 13B | Doc3 | done | Doc 3 · §13B |
| L478 | Even for a sourced product, build it from real, verifiable history — the true history of the product, its ingredients / materials / design, or the mechanism (who first found or used it, when, how, what happened to it). | DO | 13B | Doc3 | done | Doc 3 · §13B |
| L479 | Every fact gets a source (§20 B fact-checks it); never invent a founder, an expert, or an event. | DO | 13B | Doc3 | done | Doc 3 · §13B |
| L480 | Then pull real emotional beats from customer stories in the research. | DO | 13B | Doc3 | done | Doc 3 · §13B |
| L481 | Collect the §18B history candidates before writing this section (the features / triggers / history agent gathers them) and name the one you build from — don't run a separate history search. | DO | 13B | Doc3 | done | Doc 3 · §13B |
| L482 | 14 · Voice — Exactly how she talks. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L483 | Save a swipe of her real phrases to drop into hooks and copy. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L484 | 5th–8th grade reading level, never higher. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L485 | - Emotional Journey: map the arc — Awareness → Frustration → Desperation / seeking a fix → Relief / commitment — and know where your traffic enters it. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L486 | - Swipe size: at least 50 short, vivid phrases (her metaphors, exaggerations, her own labels — e.g. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L487 | "walking on marbles"), not full pain sentences. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L488 | Mark ★ the ones that appear in 3+ snippets. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L489 | - Quote buckets: as you scrape, sort real quotes into pain/frustration · mindset · deep fears · motivation & urgency · emotional response to struggle. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L490 | These drop into hooks and body copy verbatim. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L491 | - "As you scrape" = sort the §2C quotes; use quotes not already shown in §10. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L492 | - Words to USE vs. words to AVOID: USE = her exact words from the §2C data bank (the swipe) — these go into hooks, headlines, and body copy. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L493 | AVOID = words she never uses: clinical / technical terms, marketer-speak, and the hype words the category's ads overuse. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L494 | List each avoid-word with the plain word she'd say instead (e.g. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L495 | "hallux valgus" → "bunion"). | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L496 | An avoid-word may appear ONLY on the product page or FAQ when it's needed for accuracy or education (e.g. naming the condition) — never in ads, hooks, or headlines. | DO | 14 | Doc2 | done | Doc 2 · §14 |
| L497 | 15 · Competitor Offers + Price Ladder — Go through EVERY competitor named earlier on this page that sells online (the whole §1 long-list incl. direct + indirect, plus any others found in §0B and §10B — skip DIY / doing nothing) — not a sample. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L498 | To keep it fast: for Shopify stores, first firecrawl_scrape [domain]/products/[handle].js (every variant, tier price, compare-at price in one call); then ONE playwright-skill script loops the whole URL list (product page → add to cart → cart → checkout, stop) and saves each step's text + screenshot to files. | TOOL | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L499 | A store the script can't get through → write "cart not walked — why" in its block. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L500 | From those files (and the .js data), capture everything they sell with. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L501 | Go as far as the checkout page and stop at the payment step — never enter payment details, never place an order, never use real personal data. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L502 | - One-time purchase: the single-unit price · the compare-at / "was" price. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L503 | - Bundles + tiers: every quantity tier (1 / 2 / 3-pack…) + price per unit · BOGO · subscription price + terms. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L504 | - Free gifts + bonuses: what's thrown in, at which tier, and the "value" they claim. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L505 | - Upsells + cross-sells: order bumps · cart add-ons · shipping protection · warranties — each with its price. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L506 | Post-purchase one-click upsells only show after paying — so infer them from the store's installed apps (Winning Hunter get_store_details, e.g. | TOOL | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L507 | Zipify OCU / ReConvert / Rebuy) and label INFERENCE. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L508 | - Guarantee + returns: length · conditions · who pays return shipping · where returns go. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L509 | - Shipping: free-shipping threshold · stated delivery times. | OUTPUT | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L510 | - Discount mechanics: pop-up offers (what they give for email / SMS) · countdowns · coupon codes · the "reason for the discount." | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L511 | - Where it's weak / missing — the gap you can beat. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L512 | - Output: one short block per competitor (bold name, one line per item above, the page URL as the source for every number) + a 4-column summary table: competitor · price · best offer · gap. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L513 | Under it, 3 lines: Table stakes (what at least half of them do — you must match it) · Best-in-class (the strongest offer + who runs it) · Nobody offers (the open slots → Offer inputs). | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L514 | - Price ladder: the same (or closest) product's REAL price at every level — AliExpress / CJ (not the welcome-deal teaser) → Amazon → TikTok Shop → each competitor above. | TOOL | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L515 | Shows the price floor, the price ceiling, and how much brand + offer you need to justify your price. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L516 | - Offer inputs for Step 2: the problems your offer stack must solve (top of §10 + §11) · the guarantee gap · the natural bundles (e.g. both feet, day + night) · the price point to test (then re-run the Pre-0 KPI table at this price in Doc 1). | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L517 | Open and match the input list of the offer reference; Step 2 builds the offer (); this section hands it the raw material. | DO | 15 | Doc4 | done | Doc 4 · §15 (A–E + Pre-0 re-run) |
| L518 | 16 · Psychological solution — Not just the logical fix (the product) — the emotional fix underneath (Hormozi). | DO | 16 | Doc3 | done | Doc 3 · §16 |
| L519 | 17 · Features → benefits — Every feature → its benefit → the desire it hits → the struggle it removes → the objection it raises → how you handle it. | DO | 17 | Doc3 | done | Doc 3 · §17 |
| L520 | Gives you endless things to talk about. | DO | 17 | Doc3 | done | Doc 3 · §17 |
| L521 | Mark every weak claim or product / mechanism mismatch. | DO | 17 | Doc3 | done | Doc 3 · §17 |
| L522 | 18 · Trigger events — What makes her start looking for a fix. | DO | 18 | Doc2 | done | Doc 2 · §18 |
| L523 | Use these in your ad hooks later. | DO | 18 | Doc2 | done | Doc 2 · §18 |
| L524 | - At least 8, ranked by §2C trigger count. | DO | 18 | Doc2 | done | Doc 2 · §18 |
| L525 | Each = a concrete moment (what just happened + where + who was there — e.g. | DO | 18 | Doc2 | done | Doc 2 · §18 |
| L526 | "couldn't keep up on the walk with the grandkids") + a quote + URL. | DO | 18 | Doc2 | done | Doc 2 · §18 |
| L527 | Vague states ("pain getting worse") don't count. | DO | 18 | Doc2 | done | Doc 2 · §18 |
| L528 | 18B · Curiosity & Corruption Angles (hook fuel) — mine the market's history: | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L529 | - Lost / forgotten / suppressed solution — did someone try to fix this before in a unique way (especially pre-1960)? | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L530 | A discovery that got buried, "ancient wisdom," "what's old is new again." What happened to it? | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L531 | (e.g. the WW2 foot-fungus cure.) | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L532 | - Corruption / "Fall from Eden" — did this pain used to not exist, or be smaller? | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L533 | What outside force made it worse (an industry, a person, a policy)? | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L534 | Is there a group/era/tribe that doesn't have this problem — and why? → your common-enemy origin story. | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L535 | - At least 2 candidates per type, each with a URL — none real? write "none found" + the searches you ran; never invent one. | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L536 | Run this history search once: §13B picks one candidate from here by name instead of re-researching it. | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L537 | - Source: Google ("history of [problem]", "popular [category] of the 1900s", "where [problem] doesn't exist"), forums, old articles. | DO | 18B | Doc3 | done | Doc 3 · §18B |
| L538 | The Funnel Map (do this before building any page) | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L539 | Fill out the exact full funnel structure you're going to build for THIS product. | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L540 | First pick the funnel from the — match it to her awareness level (§5) and what the product needs; for a single-hero product the default is the Discovery Stack (Advertorial → Offer Page). | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L541 | Say which funnel and why. | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L542 | Each page continues the conversation — it never repeats what the last touchpoint already said. | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L543 | Ad (does x) → Pre-sell page (Does X, gives the mechanism + proof) → Product page (sells THIS product + offer) → Cart (raise order value) → After purchase (kill regret, upsell, get repeat buys) | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L544 | - Fill in every stage for THIS product — replace every "x": what the ad does · which mechanism + which proof the pre-sell page uses · the offer inputs the product page will sell (§15 → the full offer is built in Step 2) · how the cart raises order value · what happens after purchase. | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L545 | If the chosen funnel has no pre-sell page, write "none — why". | DO | FunnelMap | Doc4 | done | Doc 4 · Funnel Map |
| L546 | 20 · Verify — Run agent-reach + product-pulse to fact-check the whole doc. | TOOL | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L547 | Nothing ships unverified. | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L548 | - A) Run every skill / tool this page names — in "Skills to use" AND inline in any section (including anything added later). | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L549 | Tool down or needs a key? | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L550 | Use the closest substitute and say so — never silently skip. | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L551 | In the hand-off (the §20 Verify report in Doc 4 AND your final message), list EVERY skill / tool on this page with ✅ ran · 🔁 substitute (which one) · ➖ not needed (why — fallbacks only) · ❌ couldn't (why). | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L552 | - B) Adversarial fact-check — skeptics told to REFUTE, not confirm: the wedge, "the market is real", "uncontested in [region]", the authority, the mechanism / science, the economics, AND every historical / heritage / medical / statistical fact that could go into ad copy (a made-up "history" fact in a live ad is a credibility + compliance problem). | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L553 | Each → CONFIRMED (with URL) or CORRECTED (right fact + URL). | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L554 | Fix the docs and report every correction. | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L555 | - C) Completeness check — re-open THIS page and check every heading, bullet, and sub-bullet against the 4 docs: present? thorough (full lists, not one example)? sourced or flagged as inference? | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L556 | Name which source types were mined (Reddit · Amazon 1–2★ + 4–5★ · forums · TikTok / TikTok Shop · Facebook Ad Library · competitor pages) and fill any gap. | TOOL | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L557 | - D) Self-approval — every box true, or (after a real attempt) the reason it can't be, written in the hand-off: | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L558 | - [ ] Every line on this page is covered in the 4 docs, thorough, and sourced (or flagged inference). | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L559 | - [ ] Every skill / tool this page names was run, substituted (named), or marked ➖ (fallbacks only) — and all of them are listed in the hand-off. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L560 | - [ ] The §2C data bank has 100+ snippets from 4+ source types (or the real number + why), and every customer list (§3–§18) is ranked by a real tally of that file. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L561 | - [ ] Every historical / medical / stat claim that could enter ad copy is verified with a URL (or removed). | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L562 | - [ ] The wedge passes the Purple Ocean Gate (§2): painkiller + uncontested + a real MARKET. | GATE | 20 | Doc4 | blocked | Box NOT ticked: G3 is painkiller + market but contested (InShape, Selure, Alphacore) — stated plainly in Doc 4 §20 D + hand-off |
| L563 | - [ ] The §2B compliance table matches the product's actual category. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L564 | - [ ] Economics use the REAL price (no fake welcome-deal teaser). | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L565 | - [ ] Product / mechanism gaps are flagged honestly. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L566 | - [ ] The Funnel Map is filled — every stage, for THIS product. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L567 | - [ ] §2, §4, §4B were LOCKED after §11 and the §9 One Belief rewritten after §13 — what changed is written down. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L568 | - [ ] The target region came from Pre-0 (not guessed), and Audit first is done. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L569 | - [ ] Each of the 4 docs has the folder link + Top 5 takeaways at the top and its own Sources list at the end; the §2C CSV is final and ready to upload as the Sheet. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L570 | - [ ] Corrections from verification are reported, not hidden. | GATE | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L571 | - Only then upload (How to deliver, steps 3–4), open every link to confirm it works, say "verified & self-approved" and deliver. | GATE | 20 | Doc4 | done | Uploaded to Notion after §20, links opened, "verified & self-approved (one box unticked)" stated |
| L572 | Can't tick a box? | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L573 | Say so plainly in the hand-off. | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L574 | ➡️ Feeds: Step 2 (offer/store/funnel), Step 3 (ad angles), Step 4 (scripts). | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L575 | AFTER You have gotten ai to do this research you need to now sit down analyse everything and highlight and add notes to certain things and just really get to know ur consumer better than they know themselves . | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L576 | CLAUDE MAKE SURE YOU TELL NIKITA THIS AFTER RUNNING THE FULL SKILL. | DO | 20 | Doc4 | done | Doc 4 · §20 Verify report |
| L577 | Changelog | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L578 | 2026-10-18 — Customer-research depth upgrade — stop desires / pains / beliefs coming back surface-level, and ladder desires to their root. | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L579 | Global "Count it, don't guess" rule — every customer list (pains · desires · needs · objections · failed solutions · triggers · misconceptions · beliefs she holds · emotional states) must now list EVERY distinct item + count, ranked — never a tidy top 1–2. | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L580 | Only 1–2 = under-collected. | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L581 | §10 (Everything about the ICP) — the "pulled from §2C" bullet now reads list every distinct one, then rank (all of them, not a top handful). | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L582 | §10A · Desire Ladder (NEW) — ladder every surface desire ("why does she want that?" ×3–5) down to a core human driver, extract every distinct core desire, then rank the cores by rolled-up count; repoint the §9 One Belief at the #1 core. | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L583 | Mirrors §13, which already ladders the problem to its root. | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L584 | Left unchanged on purpose: the §9B belief chain stays ≤6 — that's the persuasion sequence, not the full belief inventory. | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L585 | Heads-up: this fixes the method only. | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |
| L586 | Research already run under the old version (e.g. | DO | CHANGELOG | ALL | done | Note only — refers to another product (Women's Cardholder); this run uses the upgraded method |
| L587 | Women's Cardholder — Step 1) has surface-level desires and should be re-run to get the laddered cores. | DO | CHANGELOG | ALL | done | Note only — not applicable to this product |
| L588 | --- | DO | CHANGELOG | ALL | done | Method applied: exhaustive ranked lists (Doc 2 §10, Doc 3 §11) + §10A ladder on all 13 desires (Doc 2) |

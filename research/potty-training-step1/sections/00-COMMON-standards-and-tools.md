*Learn everything about the customer — better than they know themselves. Every other step is built on what you find here. Do this first, every time.*
**⬅️ You start with:** a product to sell.
**✅ You're done when:** all 4 research docs are filled in — every section on this page done, in order, from real data — AND §20 Verify has passed (self-approved). Not before.
<callout icon="📂" color="blue_bg">
	**Output = 4 Google Docs, not one.** One Google Drive folder per product: "\[Product\] — Step 1 Research (date)". Work this page top to bottom, in order — but write each section into the doc it belongs to (below), so nothing gets buried. Every doc opens with the Drive folder link, then **Top 5 takeaways** — written after §20 B–C's corrections and before §20 D, each one = a specific finding + its number or quote + the decision it forces (e.g. "71% of snippets are solution-aware → lead with the mechanism"); never a section summary. Every doc ends with its own **Sources** list (every URL used in that doc).
	**📊 Doc 1 — Market & Competition** (is there money + where's the opening?): Pre-0 Economics & KPIs · Audit first · 0 · 0B · 1 · 2 · 5 · 7 · 8
	**👤 Doc 2 — The Customer** (who she is + what she says): 2C data bank summary · 3 · 3A · 10 · 10B · 14 · 18
	**🧠 Doc 3 — Persuasion** (what she must believe + how we get her there): 6 · 9 · 9B · 11 · 12 · 13 · 13B · 16 · 17 · 18B
	**🎯 Doc 4 — Brand, Offer & Funnel** (what we build + what we say): 2B Compliance · 4 · 4B · 15 · Funnel Map · 20 Verify report
	**Plus:** the full §2C customer data bank as a Google Sheet in the same folder.
	**Top of each doc, in this order:** Drive folder link → Top 5 takeaways → then Doc 2: the §2C summary · Doc 4: the shaded 2B SAY / DON'T SAY table.
	**Format:** phone-friendly — a big bold header for every section, smaller headers for sub-parts, short blocks over wide tables. Then *offer* (don't force) to write the 4 docs back into Notion as 4 sub-pages under one product page.
	**How to deliver (Drive):** (1) create the folder FIRST (`create_file`, `contentMimeType: application/vnd.google-apps.folder`) and keep its link for the top of each doc · (2) write all 4 docs locally as .md as you go — Drive files can't be edited after upload · (3) only after §20, convert each .md to HTML (`pandoc`, or Python `markdown` with the tables extension) and upload that HTML once (`parentId` = folder, `contentMimeType: text/html` → Google Doc) and the §2C CSV (`text/csv` → Google Sheet) · (4) save each doc as a .md file too (`contentMimeType: text/markdown` + `disableConversionToGoogleType: true`) and send them with your final message, with all the links.
	**These deliverables override anything else** — including older instructions inside the `research-doc` skill file.
</callout>
<callout icon="⚠️" color="red_bg">
	**NON-NEGOTIABLE — read before every run.**
	**1 · Go in order. Every run, every time.** Start at the top of this page and work down, section by section, line by line: Pre-0 → Audit first → 0 → 0B → 1 → 2 → 2B → 2C → 3 → 3A → 4 → 4B → 5 → 6 → 7 → 8 → 9 → 9B → 10 → 10B → 11 → 12 → 13 → 13B → 14 → 15 → 16 → 17 → 18 → 18B → Funnel Map → 20 (Verify always runs LAST, over everything). There is no §19. Never skip ahead, never skip a section, never skip a line inside a section. (Collecting research in parallel per "Run it as a workflow" is allowed — the WRITING stays in order.) ("Do this first" on §1 means: before every customer / strategy section below it.)
	**2 · Run EVERY skill and tool on this page — all of them, every run.** Not "if needed," not "just the main ones." Every skill in 🧰 Skills to use AND every tool named inside a section (Google Trends, Winning Hunter tools, `jq`, the Notion connector…) is mandatory. The "Where each skill is required" table below says where each one runs. A skill is down or needs a key? Use the closest substitute and say which — never silently skip. Fallbacks — anything named "if X fails / is blocked / isn't installed," or limited to a region — run only when that condition is true.
	**3 · Prove it at the end.** The §20 hand-off lists EVERY skill / tool on this page with ✅ ran · 🔁 substitute (which one) · ➖ not needed (why — fallbacks only) · ❌ couldn't (why). A skill missing from that list = the run is NOT done.
	**4 · Draft → lock.** §2, §4, and §4B are DRAFTS when you first reach them (the word "LOCK" inside §4B means this lock). You LOCK them at the end of §11, once the 1★ reviews and objections are mined. The §9 One Belief is a draft too — rewrite it at the end of §13, once the mechanism is set.
</callout>
## The one rule
Every answer must come from a real source — Reddit, Amazon reviews, forums, TikTok, competitor pages. No guessing. Not sure? Check it with `agent-reach` before you trust it.
## 📏 Standards for every section
- **Every line on this page is a requirement** (rule 1 at the top) — every heading, bullet, sub-bullet, and instruction gets done; nothing dropped or merged.
- **Painkiller in an uncontested market.** The wedge must be BOTH a specific, painful, unsolved PROBLEM for a large, desperate group AND white space no major competitor already runs in the target region (§2). Miss either half and it's weak.
- **Sourced or it doesn't ship.** Behind every pain, objection, competitor, belief, and mechanism: a **verbatim quote + the source URL**. Never invent a quote, stat, competitor, or run length. Can't verify it? Say so — don't pad.
- **Source tags:** every quote, number, and claim carries a tag pointing to its source — `[S1]`, `[S2]`… — matching the numbered Sources list at the end of that doc (URL · platform · date). Also mark how solid it is: **VERBATIM** (page opened, wording confirmed) · **SNIPPET** (search-result text — confirm before live creative) · **DATA** (a tool's estimate, e.g. Winning Hunter revenue) · **INFERENCE** (your reasoning, no source — keep these rare and always labelled).
- **Count it, don't guess.** Every pain, desire, objection, failed solution, trigger, misconception, and belief comes from the §2C customer data bank and is **ranked by how many real snippets mention it** (e.g. "31 of 142"). No count = no ranking. (Exception: the §9B chain keeps persuasion order — show each belief's count next to it.)
- **Minimums are targets, not quotas.** Fewer real ones exist? Give the real number + why — never pad with invented or weak items.
- **Search snippets:** Reddit / Amazon / Facebook often block full-page fetch. Search-result snippets are real text — quote them, but flag them so the exact wording gets confirmed at the URL before it goes into live creative.
- **Tight, and every section ends in a decision:** the answer + the evidence + a **"So What → do this"** line. No essays.
- **List sections give the FULL set, not one example** — real customers have a dozen pains, objections, failed solutions. List them all (with quotes), tightly.
- **Be decisive.** Commit to the market / wedge yourself, with evidence — lead with the pick + why, runner-up in one line. Never hand back a "which one?" menu. If Nikita hands you a market, pressure-test it honestly. If no uncontested big painkiller market exists, say so plainly instead of forcing a weak wedge.
- **Run it as a workflow:** decide the uncontested painkiller MARKET first (§1–§2 draft). Then fan out one deep agent per area to COLLECT research in parallel (competitors + offers + white-space sweep · customer data bank / voice / beliefs / worldview / failed solutions · authority + science + compliance + mechanism · features / triggers / history). Every agent researches the CHOSEN market, not the generic product, gets the exact text of the sections it collects for (never a summary), and returns findings with quotes + URLs. Then YOU write every section in page order from what they return — no section skipped, none written out of order — then run §20 last.
- **"She" = the ICP,** whatever the buyer's real gender. Never assume female — follow the data.
- **Report corrections honestly.** If verification kills an earlier conclusion, say it was wrong and what replaced it — never quietly drop it.
- **Research + write only.** Never touch live ad accounts or spend. Never place an order or enter payment details on any site.
## 🧰 Skills to use here (run these — don't do it by hand)
- **`research-doc`** — runs this whole doc for you, start to finish, from real sources. **Start here.**
	- If you ARE `research-doc` reading this page, you're already running it — mark it ✅ in §20.
- **`product-pulse`** — what real people say about the exact product (X + Reddit).
- **`agent-reach`** — web / Reddit / forum / TikTok research + fact-checking.
	- First run `agent-reach doctor --json`. CLI not installed? Use the Firecrawl MCP (`firecrawl_search` + `firecrawl_scrape`) for the same jobs and log it as 🔁 in §20.
- **`Firecrawl`** — scrapes competitor sites.
	- = the Firecrawl MCP tools: `firecrawl_search` (find pages / snippets) + `firecrawl_scrape` (read a page; `formats: ["query"]` to pull specific facts).
- **`playwright-skill`** — walks competitor stores and pulls their offer, pages, and upsells.
	- Run it headless (`headless: true`; `npm run setup` once). If Playwright fails, use `browser-use` and say so.
- **Amazon trick:** paste 5★ reviews into ChatGPT → why people love it (your angles). Paste 1–2★ → their complaints (your objection list).
	- **How you (the AI) run this trick:** collect the reviews yourself and do the sorting yourself. Amazon review pages often need a login, so: `firecrawl_scrape` each top listing's /dp/ page (its top reviews + the "Customers say" summary) across 5–10 listings, and get 1–2★ wording via `firecrawl_search` (`site:amazon.com "[product]" "one star"`, + Walmart / Trustpilot), tagged SNIPPET. There's no ChatGPT step for you, and never pass reviews through a separate chat that strips the sources. Keep the **URL + star rating + date** for every review you use, so every quote stays traceable and countable. Log it in §20 as "Amazon trick ✅" (🔁 + why only if the /dp/ pages were walled too).
- **Forum tactics:** sort threads by **replies / views** to find the most-engaged ones; steal high-view thread titles as ready-made hooks / email subject lines.
	- How: `firecrawl_scrape` [old.reddit.com/r/\[sub\]/search?q=\[term\]&restrict_sr=1&sort=comments](http://old.reddit.com/r/[sub]/search?q=[term]&restrict_sr=1&sort=comments) (and forum lists sorted by replies) to find the most-engaged threads. Blocked? `firecrawl_search` `site:reddit.com/r/[sub] [term]` (+ `product-pulse`), rank threads by the comment count shown, tag SNIPPET. List the high-view titles in §14 as "Thread-title hooks".
- **SimilarWeb** — competitor traffic + audience demographics.
	- No SimilarWeb connector: `firecrawl_scrape` [similarweb.com/website/\[domain\]](http://similarweb.com/website/[domain]) — gives age + gender split (visits only as a range). Exact monthly visits + history: Winning Hunter `get_store_details` (no demographics). If SimilarWeb is blocked, mark §3 demographics INFERENCE.
- **Audit first:** before researching, study your current page (or the control you're modeling) and note what's weak.
- **Winning Hunter** — `search_facebook_ads` (`sort_by: longestrunning` = proven) · `get_store_details` (traffic, revenue, time in business, installed apps) · `get_store_top_ads` · `find_similar_shops` + `brief_competitor` (expand the competitor list) · `search_exploding_topics` (§0B fallback only) · `search_tiktok_products` / `get_tiktok_product` · `search_tiktok_ads` · `search_google_ads`. Big ad-search results often save to a file — read them with `jq`, not the whole file.
- **Facebook Ad Library** — catches advertisers Winning Hunter misses and proves which region / language an angle is or isn't run in. Browse [facebook.com/ads/library](http://facebook.com/ads/library) with `playwright-skill` / `browser-use` (set the country + "All ads"). A `facebook` connector / Ad Library API only returns normal product ads for EU / UK — use it for EU / UK only. Library won't render headless? Prove region / language with Winning Hunter `search_facebook_ads` (`keyword` + `countries: [target]` + `languages`), once for the target region and once for others, and log 🔁.
- **TikTok + Google / Amazon / Etsy** — the rest of the competitor + white-space sweep: TikTok ads via Winning Hunter `search_tiktok_ads` (pass `countries`) · Google ads via `search_google_ads` (pass `country` / `domain`) · Amazon / Etsy via `firecrawl_scrape`.
- **A tool here isn't available?** See rule 2 at the top (substitute, name it, never silently skip).
**Where each skill is REQUIRED (every run):**
<table header-row="true">
<tr>
<td>Skill / tool</td>
<td>Must run in</td>
</tr>
<tr>
<td>`research-doc`</td>
<td>The whole page — it runs this page top to bottom</td>
</tr>
<tr>
<td>Audit first</td>
<td>Right after Pre-0 (your current page — or, for a new product, the highest-traffic competitor page a quick search turns up; §1 re-checks it). Output in Doc 1, right after Pre-0: the URL audited + what's weak</td>
</tr>
<tr>
<td>`product-pulse`</td>
<td>§2C · §10 · §14 · §20</td>
</tr>
<tr>
<td>`agent-reach`</td>
<td>§2C · §5 · §10 · §10B · §12 · §18 · §18B · §20 (research + fact-check)</td>
</tr>
<tr>
<td>`Firecrawl` (MCP: `firecrawl_search` · `firecrawl_scrape`)</td>
<td>§0B · §1 · §2C · §5 · §10B · §13 · §13B · §15 · §18B (+ every `agent-reach` job if its CLI isn't installed)</td>
</tr>
<tr>
<td>`playwright-skill`</td>
<td>Audit first · §0B (Google Trends) · §1 (funnels + Ad Library) · §2 (Ad Library region check) · §15 (every product page, offer, cart, checkout) — `browser-use` if it fails</td>
</tr>
<tr>
<td>Amazon trick</td>
<td>§2C · §10 · §10B · §11</td>
</tr>
<tr>
<td>Forum tactics</td>
<td>§2C · §5 · §14 · §18</td>
</tr>
<tr>
<td>SimilarWeb</td>
<td>§1 (traffic) · §3 (demographics)</td>
</tr>
<tr>
<td>Winning Hunter</td>
<td>§0B · §1 · §15 (`get_store_details` apps → upsell apps)</td>
</tr>
<tr>
<td>Facebook Ad Library</td>
<td>§0B · §1 · §2</td>
</tr>
<tr>
<td>TikTok + Google / Amazon / Etsy</td>
<td>§0B · §1 · §2 · §15</td>
</tr>
<tr>
<td>Google Trends</td>
<td>§0B</td>
</tr>
<tr>
<td>Notion connector</td>
<td>Funnel Map (open the Funnel Selection Board) · §15 (open the Offer Build reference)</td>
</tr>
<tr>
<td>Google Drive</td>
<td>Delivery: the folder, the 4 Docs, the §2C Sheet</td>
</tr>
</table>
## Fill these out, in order
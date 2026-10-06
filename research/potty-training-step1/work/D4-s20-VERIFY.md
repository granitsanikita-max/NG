# §20 · Verify report — "Big kids still learning" (reusable training underwear, US)

*Run 2026-10-06, last, over all 4 docs. A = every skill / tool on the page · B = adversarial fact-check + every correction · C = completeness (ledger 299 rows) · D = self-approval. Key: ✅ ran · 🔁 substitute (which) · ➖ not needed (why — fallbacks only) · ❌ couldn't (why).*

**Verdict up front:** the research is **verified & self-approved for Step 2 planning**, with five things still open that block *live creative and spend*, not the research: (1) no OEM quote → economics PROVISIONAL, (2) no pour test → every ml number OPEN, (3) Reddit / forum wording is SNIPPET → confirm at the URL before it goes in an ad, (4) the Drive folder / Sheet upload happens at delivery, (5) CARER must be re-checked monthly. Details in D.

---

## A · Every skill / tool the page names

### Skills
- **`research-doc`** — ✅ The page was run end to end, in order, by the orchestrating session (this is that run). Writer sub-agents logged themselves 🔁/➖ because they wrote sections, not the whole doc; the run as a whole is ✅.
- **`product-pulse`** — ✅ §2C wave 1 (X + Reddit sweep, ~30 Firecrawl queries; X gave 8 usable posts) · ✅ (partial) upstream school-age pass (X = 0 usable; Reddit folded into §2C) · §10 built from those bank rows · 🔁 §14 (bank rows instead of a fresh pulse) · ✅ **§20 re-find pass** (8 searches, below in B). Step 8 "publish to Notion Comments-from-X" ➖ every time: outputs go to the §2C bank and these docs, and the Notion plugin needed authorisation in this session.
- **`agent-reach`** — 🔁 **Firecrawl MCP** everywhere (§2C · §5 · §10 · §10B · §12 · §18 · §18B · §20). `agent-reach doctor --json` → `command not found` (CLI not installed), exactly the case the page names. Its YouTube route was used directly: `yt-dlp --write-comments` ✅ (27 VERBATIM rows).
- **`Firecrawl`** (`firecrawl_search` + `firecrawl_scrape`, incl. `formats:["query"]` / `directQuote`) — ✅ §0B · §1 · §2C · §5 · §10B · §13 · §13B · §15 · §18B · §20. Hit HTTP 429 several times; waited and continued. Firecrawl research tools ✅ for paper discovery (§12/§13).
- **`playwright-skill`** — ✅ via the **globally installed Playwright 1.56.1** (headless Chromium, proxy CA trusted, TLS on). The skill folder ships only SKILL.md — no `package.json` / `run.js` — so `npm run setup` could not run. Jobs: Audit first (UpAiry PDP + advertorial + daycare page) · §0B Google Trends (wave 1 + upstream) · §1 / §2 Facebook Ad Library · §15 PDP → cart → checkout walks on every DTC competitor, **stopped before payment, no data entered**. ❌ inside it: YouTube / TikTok comments (login + bot walls), AliExpress item pages, Goodnites.com (403).
- **`browser-use`** (Playwright fallback) — ➖ Playwright worked. (The browser-use MCP also failed to connect this session.)

### Named tactics and tools
- **Amazon trick** — ✅ (partial sign-in wall). /dp/ pages scraped for top reviews + "Customers say" across 5 toddler listings and the big-kid listings (MooMoo 9T, "8-10Years"); 1–2★ wording via Trustpilot (UpAiry, 26 rows at 1–2★) and Walmart. URL + stars + date kept on every row. Amazon itself gave only **2 rows at 1–2★** (deeper reviews need sign-in) — real number, stated.
- **Forum tactics** — 🔁 the page's own fallback. Firecrawl refuses reddit.com and Reddit returns 403, so `old.reddit … sort=comments` could not be scraped; `firecrawl_search site:reddit.com/r/[sub]` + product-pulse were used, threads ranked by the result set (comment counts not visible). Thread-title hooks are in Doc 2 §14 and §18.
- **SimilarWeb** — 🔁 no connector → `firecrawl_scrape similarweb.com/website/[domain]` ✅ (upairy.com demographics F 77% / M 23%). brightkidco.com / superundies.com returned "No Data" → those fields INFERENCE. Exact traffic from WH `get_store_details`.
- **Audit first** — ✅ Doc 1, right after Pre-0: UpAiry PDP + persona advertorial + `/pages/daycare-mandate` (no store of our own).
- **Winning Hunter** — `search_facebook_ads` ✅ (longestrunning, most-duplicated `min_duplicates: 2`, landingurl, pagename, adtext, countries) · `get_store_details` ✅ (UpAiry, Kid Confident, BrightKidCo, Saphire, Bloomwise, Super Undies, CARER, Lucky & Me, WunderUndies, + 4 §15 stores) · `get_store_top_ads` ✅ · `find_similar_shops` ✅ (low value: name matches only) · `brief_competitor` ✅ (low value) · `search_exploding_topics` ➖ (§0B fallback only — Google Trends rendered) · `search_tiktok_products` / `get_tiktok_product` ✅ · `search_tiktok_ads` ✅ · `search_google_ads` ✅ (UpAiry 56 US ads; CARER 89).
- **`jq`** (+ Python) — ✅ big WH result files read with `jq`; 75 ad files → 1,316 unique ad IDs / 908 copy rows; `tally.py` / `cuts.py` for every §2C count; KPI tables re-computed in §20B (all match to the cent).
- **Facebook Ad Library** — ✅ wave 1 (Playwright headless, US "potty training underwear" ~950, US "daycare potty" ~210, GB ~460) + 🔁 WH `search_facebook_ads countries:[US]` for CA / AU ("No ads match" headless) and for every §20B region check (the Library didn't render headless that pass).
- **TikTok + Google / Amazon / Etsy** — TikTok ✅ (WH ads + TikTok Shop) · Google ✅ (`search_google_ads`) · Amazon ✅ (`firecrawl_scrape`) · Etsy 🔁 (same-day marketplace-map scrape; no big-kid absorbent daytime listing found; not re-scraped).
- **Google Trends** — ✅ §0B via Playwright (US 5 years ×6 queries wave 1; 5 segment captures upstream; GB / AU / CA). Segment terms ≈0–7 vs 100.
- **Notion connector** — ✅ Funnel Selection Board (Funnel Map [B48]) and Offer Build reference (§15 [O71]) opened with `notion-fetch`.
- **Google Drive** — ⏳ **at delivery.** Folder, 4 Docs (HTML) and the §2C Sheet are uploaded after this self-approval by the parent session (How to deliver, steps 1, 3, 4). Not run yet — not skipped.
- **Supplier prices** — AliExpress ✅ (search-card prices; "New shoppers" teasers rejected) · CJ Dropshipping ❌ (human-verification wall; HTTP 429) · Alibaba OEM ❌ → 🔁 search snippets (CAPTCHA) — **no real OEM quote exists**.
- **Other substitutes used and named** — Europe PMC REST 🔁 for PubMed (reCAPTCHA) · WebSearch / WebFetch 🔁 when Firecrawl was rate-limited · `pdftotext` ✅ (K-C history PDF, Seim 1989, Rittig 2010, Breinbjerg 2021) · Shopify `products.json` / `.js` via `curl` 🔁 for ~30 stores (same data as Firecrawl, one call each).

---

## B · Adversarial fact-check (skeptics told to REFUTE)

Two skeptics ran in parallel (work/20B-skeptic-market.md, work/20B-skeptic-facts.md), plus the 601-row re-tally (work/REFRESH-LOG.md, work/UPSTREAM-CHANGES.md) and this §20 product-pulse pass. Every fix is in the docs with an inline *(§20B: …)*, *(Refresh 601: …)* or *(§20C: …)* note — nothing was dropped quietly.

### What survived (CONFIRMED)
- **The wedge passes the Purple Ocean Gate, narrowed.** PAINKILLER PASS · UNCONTESTED PASS only for the bundle (size-matched, pour-tested number + training identity + creed + School-Day Kit) · MARKET PASS (≈1.4–2.0M US kids 5–9) [V1][V5].
- **"Accidents at school" on US Meta = 9 ads, all supplements, 0 underwear** [W5]. TikTok "training underwear" US ads = 0 [W6]. TikTok Shop "big kid training underwear" US = 0 [U29].
- **7–10% of 5–13-year-olds have daytime wetting** [M64]; Boston Children's "up to 10 percent of 5-year-olds" [B1].
- **Expected bladder capacity 30 × (age + 1) ml, ages 4–12** — stronger source added (Rittig 2010, ICCS reappraisal) [V27]. It is a 50th-percentile *maximum* voided volume.
- **Brazelton was the TV spokesman for size-6 Pampers** (all four Tampa Bay lines re-confirmed by directQuote) [P1]; K-C's "I'm a big kid now" was trademarked [V22].
- **KPI arithmetic** — every CM $, CM %, break-even ROAS and 20% / 30% target in all tables re-computed in Python: matches to the cent. Real price ladder used (no AliExpress teaser).
- **§20 product-pulse re-find (8 searches):** the two headline school-age quotes were re-found word for word — "My son is 7. He is in second grade. He regularly comes home from school with wet pants or underwear." [V14] and "I have a son in year one who wets himself at school most days and never tells anyone" [V15] (still SNIPPET: search text, not the opened page). New threads back the School-Day Kit and the "toddler trainers don't hold" findings: spare clothes "inside a 'wet bag'" in the backpack [V16]; "Potty training pants aren't designed to absorb all the pee, just small accidents" [V17]; bigger-kid parents fall back on Prevail liners and Ninjamas [V18]; "sending 7-yr-old to school in pull-ups" [V19]. X: noise only (adult/ABDL accounts), same as waves 1–2. **Nothing found that refutes a §2C finding.**

### Every correction (old → new)

**Market / wedge / competitors (market skeptic)**
1. "Nobody in US paid social states a ml figure (0 of 908 ads)" → **CORRECTED.** CARER (carerspk.com) runs 27 kids' ads on US Meta: "hidden 100ml leak protection… dry at school", started 2025-12-03, seen 2026-10-05; one flat 100 ml for 10 sizes [V1]. TIICHOO prints 30–40 ml, Carer Amazon 50–80 ml [V3][V4]. The 908 was a toddler-category corpus.
2. "Nobody active in US paid social" runs the big-kid angle → **"Nobody with a brand voice; one weak live contestant (CARER)"** [V1][V2].
3. "First to state a number" → **dropped entirely.** Claim only "tested per size, printed per size". Super Undies prints 325–620 ml on *night* Brain Trainers [V9].
4. "Nobody frames school" → framing **taken** (CARER "dry at school", TIICHOO "school settings"); a packaged School-Day **Kit** is still offered by nobody found [V10].
5. "Every absorbent seller refuses worn returns" → CARER "First Pair Guarantee… keep the first pair" (first pair only) [V1]. Open slot: a guarantee tied to the printed number, every pair, 100 days.
6. BrightKidCo sensory line "last seen 08-31" → **09-05**; "0 live" is moderate confidence (WH indexes 13 of up to 107 ads); it already ran **"Not a 3-day miracle"** (GB, Apr 2026), so that phrase is not ownable [V8].
7. Saphire / Bloomwise "prove spend on daytime wetting" → **CORRECTED to "prove reach"**: Saphire sells mainly mood gummies (bedwetting e-book created 2026-09-07); Bloomwise's school-accident story is constipation / soiling, in UK wording [V6][V7].
8. Market size 1.3–1.85M → **≈1.4–2.0M** (ACS 2024: 20,081,975 children aged 5–9 × 7–10%; INFERENCE, internal only) [V5][V29].
9. Duty "~35% if" → **certain for China-made goods, ≈27.5%** (HTS 7.4–7.6% + Section 301 7.5% + 12.5%; IEEPA struck down) → landed ≈$5.70; **6 for $84 (scale CPA $15.08) beats the $119 kit ($13.23) → budget on the 6-pack lines** until the broker's HTS ruling [V12][V13].
10. Subscription: "no subscription" → **owner input restored**: one transparent, unticked **Grow-With-Me Plan** (5 pairs / 4 or 6 months, $55), skip / cancel online, ROSCA + California ARL compliant [V11]. §20C also fixed the leftover "No subscriptions" answer in Doc 3 §11.
11. MooMoo 2T-9Y "900+ bought/mo" → **300+/mo** today (Amazon re-scrape).
12. New watch item: Conni Kids Tackers (AU, 150 ml printed on every size, "school") — no US listing found.

**History / medical / stats / compliance (facts skeptic)**
13. "In January 1999 … size 6" → **1998–99** (commercial running by Dec 1998) [V21]; "27 years later" → "nearly 30 years".
14. Brazelton "launched" the size 6 / "America's best-known child-led pediatrician" → **spokesman**, "one of America's best-known pediatricians" [P9].
15. "Kimberly-Clark launched Pull-Ups nationally in 1989" → **"began a national rollout in 1989… one-third of the country over three years"** [V22].
16. **The 92% misquote:** "92% trained by 18 months (1957)" → **92% had STARTED, ~60% finished — and the data are from 1947**, read through Seim 1989 (secondary; keep off ads) [V23].
17. "Vietnam: average training age 9 months" → **misleading**: all children *used the potty* by 9 months; training *completed* at 24 months (98%). Two separate papers, now cited separately [V32].
18. "Pediatric urologists now prescribe [bladder drill]" → **"bladder programmes use again today"** (concordance ≠ prescription; health-claim drift).
19. "Pull-ups delay / cause late training" → **only an association** ("no secure conclusions… literature is inadequate") — never stated as fact [V30].
20. "Daycare makes kids train later" → **daycare is not the villain**: Schum 2001 found daycare and maternal employment not significant [V31]. Mechanism framed as caregiver *inconsistency*.
21. ERIC "Right to Go" survey → **"Voices for change"** (Young Champions 12–19, UK; 47.73% / 24.18% / 36.65%) — **never in US ads** [V24].
22. "(age + 2) × 30 ml (Koff)" → attribution corrected; use **30 × (age + 1)** (≈240 ml at 7) [V27].
23. "1999 Tampa Bay: 90% out of diapers by 2½, 22% now" → **REMOVED** (garbled, unnamed study; conflicts with the 1962 mean of 28.5 months) [V28].
24. "P&G helped fund Brazelton's foundation" + quoted Pampers ad line → **REMOVED** (no primary source; defamation-grade).
25. "95% / 80% / 50% of parents used disposables" → **REMOVED** (newsletter snippet). Azrin "3.9 h / 74%" → **REMOVED**. NHS "83% by 18 months" and "Infant Care: never too early" → stay **REMOVED**.
26. "PFAS-free is a forbidden phrase" → **not banned; high-risk** under 16 CFR 260.9 — say "no intentionally added PFAS" + a TOF test (CA ≤100 ppm, ≤50 ppm from 2027-01-01; NY ban since 2025) [V26][V33].
27. Meta personal attributes include "family status" → **not on the current list** (age, disability, health confirmed) [V25].
28. "Nobody printed the one number" (story) → **"the big-kid sizes on the shelf still don't print…"** (Super Undies, Peejamas, Snazzipants state ml/oz).
29. "your kid failing" / "Your big kid needs…" / "If your kid needs a full bladder held" → **third person** ("the kid", "Big kids need", "If a kid needs") — Meta reviews landing pages too.
30. The "2–4×" toddler-trainer comparator rests on **one UK Instagram SNIPPET** [P49] → in ads, **film our own pour of a bought US toddler trainer**.

**Earlier-run corrections (kept on the record)**
31. **The carried-in daycare / working-parent hypothesis was KILLED at §2** and confirmed at the §11 lock: UpAiry already runs it in the US (persona ads + `/pages/daycare-mandate`) [M5].
32. **"Only Thirsties has side snaps" — wrong:** BIG ELEPHANT sells side-button trainers (4.4★, 237) [P40]; side snaps are not a unique feature.
33. **"Size-ceiling" enemy — false for reusables** (MooMoo to 9Y on Amazon) → enemy replaced by "the toddler-ized, overpromising industry" (Doc 4 §4B).
34. **"BrightKidCo owns the ND sensory slot"** → partly held: its autism / sensory edition ran Jul–Sep 2026 and is now 0 live, toddler-framed (see #6).
35. **CARER is a live competitor** (see #1–#5) — added to §1, §2, §4, §4B, §15.
36. Upstream re-tally 514 → 601 rows changed conclusions: Fear is the lead emotion (24 of 79 locked; Guilt 0); school start is the #1 trigger (10 of 79); routine / reminder (7) and spare-clothes kit (4) outrank absorbency (2) as locked needs; constipation is the locked #1 belief (6); Miralax / medical ties Pull-Ups as the locked #1 failed solution (4 each) (work/REFRESH-LOG.md).

### Could not verify (stated, not hidden)
BrightKidCo "0 live" (partial WH index; Ad Library not re-rendered) · CARER's kids-only revenue (WH revenue is store-wide) · Kid Confident's 636 ads (page 1 only) · Goodnites / Pull-Ups Meta activity (WH CPG coverage thin) · HTS classification of a TPU-laminated kids' brief (needs a broker) · subscription opt-in / retention (INFERENCE targets) · Hodges Goodreads and creator subscriber counts (keep out of ads) · NYT 1999 full text (paywall; SNIPPET).

---

## C · Completeness (ledger, row by row)

**Ledger: 291 of 299 rows done · 8 blocked · 0 todo** (`step1-ledger.md`, each row with its doc + section).

**Blocked — all eight are the Drive delivery, which by the page runs only after §20:**
- L010 / L185 — the §2C Google Sheet: the CSV is final (work/2C-databank.csv, 601 rows, 22 columns), upload pending.
- L011 / L296 — "Drive folder link at the top of each doc": Top 5 takeaways ✅ (build/takeaways-Doc1–4.md), Sources lists ✅; the folder link can only be inserted once the folder exists.
- L013 / L298 — How to deliver steps 1, 3, 4 (folder, HTML + CSV upload, .md copies, open every link).
- L124 / L125 — Google Drive tool row.

**Standards checked across all 4 docs:**
- Every section file ends in **"So What → do this"** — §20C added the two that were missing (Doc 3 §11, Doc 4 §4B).
- **Source tags** resolve: build reports **0 unresolved citations** in all 4 docs. §20C fixes: [O73] pointed at an internal research file → replaced with the original public URLs (Amazon /dp/ pages, Target, The Bump, Green Mountain Diapers, Hanna Andersson); [O72] given a public Ad Library pointer; [V10]–[V13] given proper list lines; the Sources builder now ignores log / skeptic files and prefers the definition that carries a URL.
- **Counts come from the bank** (work/2C-tally.md, tallies-3-11-601.md); minimums met or the real number + why given (X 8 rows; Amazon 1–2★ 2 rows; locked-cut objections 0).
- **No invented quotes** — quote-integrity script run by Writer B; two headline quotes re-found in this pass.
- **She = the ICP** — Doc 2 §3 derives "mom" from the data (mom 17 vs dad 5 self-references), not by assumption.
- **Audit first** ✅ (Doc 1). **§2C CSV** ✅ Sheet-ready. **§9 One Belief rewritten after §13** ✅ (Doc 3, with "What changed"). **§2 / §4 / §4B LOCKED** after §11 with "What changed" ✅. **Funnel Map** — all 5 stages filled for this product ✅. **Pre-0 cost reminder** above Doc 1's Sources ✅ (§20C: added).
- **Doc 1 completeness fix (§20C):** the LOCKED §0B and §1 files say "adds to, does not replace" the wave-1 files, but the build left the wave-1 files out — so Doc 1 was missing the category demand numbers, the 22-advertiser long-list, the three direct-competitor profiles (shop signals, top ads, funnel, offer), the Ad Library check and the TAKEN map. Both wave-1 files are now in Doc 1, ahead of their LOCKED revisions, with a note that the LOCKED revision wins where they differ.

**Source types mined (§2C bank, 601 rows):** Reddit **293** · forums **112** (What to Expect, BabyCenter, Mumsnet, Facebook groups) · Amazon **78** (20 at 5★, 6 at 4★, **2 at 1★**, 50 "Customers say" excerpts without stars) · Trustpilot **44** (24 at 1★) · YouTube comments **27** · TikTok comments **14** · Walmart **13** · retailer reviews **10** · X **8** · Instagram **2**. All 1–2★: 30 rows; 4–5★: 45 rows. Plus outside the bank: **Facebook Ad Library** + WH Meta corpus (1,316 ad IDs), **TikTok / TikTok Shop** (WH), **competitor pages** (Audit + 30+ PDP / cart / checkout walks in §15).

**Gaps, honestly:** Amazon 1–2★ wording is thin (sign-in wall) — Trustpilot / Walmart carry it · 457 of 601 rows (all Reddit, most forums) are SNIPPET · TikTok comments are excerpt-only · X is noise for this category · only 79 rows are the locked school-age segment, and they hold **0** tagged objections, so the objection ranking leans on whole-bank (mostly toddler) reviews.

---

## D · Self-approval

- ✅ **Every line on this page is covered in the 4 docs, thorough, and sourced (or flagged inference).** 291 / 299 ledger rows done; the 8 open rows are the Drive delivery, which the page runs after §20.
- ✅ **Every skill / tool was run, substituted (named), or marked ➖ (fallbacks only) — and all are listed** (A). Google Drive is ⏳ at delivery, not skipped.
- ✅ **§2C has 100+ snippets from 4+ source types** — 601 rows, 10 source types — **and every customer list (§3–§18) is ranked by a real tally** of that file (whole bank, segment 225, locked 79).
- ✅ **Every historical / medical / stat claim that could enter ad copy is verified with a URL, or removed** (B, items 13–30). One caveat: the toddler-trainer comparator (60–90 ml) is a UK Instagram SNIPPET — replace it with our own filmed pour before it goes in an ad.
- ✅ **The wedge passes the Purple Ocean Gate** — PASS, narrowed: it rests on the size-matched, pour-tested number + training identity + creed + School-Day Kit. Fail condition: if our size-8 pour can't clearly beat CARER's flat 100 ml, it becomes a me-too.
- ✅ **The §2B table matches the product's category** — US children's apparel ≤12 (CPSIA / CPC eFile, FTC substantiation + textile + ROSCA, state PFAS, Meta personal attributes); not a medical device or supplement.
- ✅ **Economics use the REAL price** (1 for $19 · 6 for $84 · 10 for $119 · 15 for $159; teaser prices rejected) — but **costs are PROVISIONAL**: no OEM / COGS quote exists, so every CM, ROAS and CPA line is an estimate until Nikita sends quotes.
- ✅ **Product / mechanism gaps are flagged honestly** — no pour test yet → **the ml number is OPEN**; sizes 7–12 need an OEM run + CPC; reviews don't exist at launch; side snaps are a v1 mismatch.
- ✅ **The Funnel Map is filled** — Ad → creator-story advertorial → proof PDP → cart → post-purchase, every stage for this product.
- ✅ **§2, §4, §4B were LOCKED after §11 and the §9 One Belief rewritten after §13** — "What changed" written in each.
- ✅ **Target region came from Pre-0** — Nikita delegated it ("top 5 English or whatever you think is best"); US was chosen with evidence and confirmed at the lock. **Audit first is done.**
- ⏳ **Each doc has the folder link + Top 5 at the top and its own Sources list; the §2C CSV is final.** Top 5 ✅, Sources ✅, CSV ✅ — the folder link goes in at delivery, when the folder is created.
- ✅ **Corrections from verification are reported, not hidden** (B: 36 items).

**Remaining open items (plain):**
1. **COGS / OEM quote missing → Pre-0 economics PROVISIONAL.** Get 2–3 OEM quotes (sizes 4–12, TPU core), a broker HTS ruling and a 3PL quote, then re-run the KPI table.
2. **Pour test not done → every ml number OPEN.** No ml claim in any ad or page until the per-size pour-test protocol (Doc 4 §2B) is on file.
3. **Reddit / forum wording is SNIPPET (457 of 601 rows)** → open the URL and confirm the exact words before any quote goes into live creative.
4. **Drive delivery** — create the folder, insert its link at the top of each doc, upload the 4 Docs + the §2C Sheet, open every link.
5. **Re-check CARER, BrightKidCo, Kid Confident monthly**; get a US-trainer pour number to replace the UK comparator.

**verified & self-approved** — for the research; live creative and spend wait on items 1–3.

## Sources
- [V14] https://www.reddit.com/r/pottytraining/comments/1gansad/my_7_year_old_wets_his_pants_regularly/ · Reddit · product-pulse §20 re-find via firecrawl_search, 2026-10-06 · SNIPPET (= §2C row C:N265)
- [V15] https://www.mumsnet.com/talk/primary/1170802-Any-advice-on-wetting-at-school-age-6 · Mumsnet · product-pulse §20 re-find, 2026-10-06 · SNIPPET (= §2C row C:N339)
- [V16] https://www.reddit.com/r/kindergarten/comments/1mmvmyx/prepping_kiddo_who_struggles_with_potty_accidents/ · Reddit r/kindergarten · 2026-10-06 · SNIPPET ("extra clothes in his backpack, which are inside a 'wet bag'")
- [V17] https://www.reddit.com/r/UKParenting/comments/1l6cfq5/potty_training_pants_that_dont_leak/ · Reddit r/UKParenting · 2026-10-06 · SNIPPET
- [V18] https://www.facebook.com/groups/dddsupportgroup/posts/8455052114519079/ · Facebook group · 2026-10-06 · SNIPPET ("What reusable training pants are available for bigger kids?")
- [V19] https://www.reddit.com/r/Mommit/comments/1ndsyhy/benefits_vs_hazards_of_sending_7yrold_to_school/ · Reddit r/Mommit · 2026-10-06 · SNIPPET
- [V21] https://www.baltimoresun.com/1998/12/13/training-issues-are-looming-large-diapers-manufacturers-are-producing-bigger-disposables-for-children-who-have-outgrown-conventional-sizes-but-are-not-yet-using-the-potty/ · Baltimore Sun 1998-12-13 · SNIPPET
- [V22] https://www.kimberly-clark.com/-/media/kimberly/pdf/innovation/ProductEvol_DisposableTrainingPants_umbracoFile.pdf · Kimberly-Clark · pdftotext 2026-10-06 · VERBATIM
- [V23] https://cdn-uat.mdedge.com/files/s3fs-public/jfp-archived-issues/1989-volume_28-29/JFP_1989-12_v29_i6_toilet-training-in-first-children.pdf · Seim 1989, J Fam Pract · VERBATIM
- [V24] https://eric.org.uk/news/desperate-to-go-young-people-struggling-to-access-toilets-at-school/ · ERIC (UK) · VERBATIM
- [V25] https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/ · Meta · firecrawl_scrape 2026-10-06 · VERBATIM
- [V26] https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-260/section-260.9 · 16 CFR 260.9 · VERBATIM
- [V27] https://www.ics.org/folder/committees/children-public-documents/d/14-age-related-nocturnal-urine-volume-and-maximum-voided-volume-in-healthy-children-reappraisal-of-international-childrens-continence-society-definitions/download · Rittig 2010 (ICCS) · VERBATIM
- [V28] https://pmc.ncbi.nlm.nih.gov/articles/PMC3307553/ · Kiddoo, CMAJ 2012 · VERBATIM
- [V29] https://datacenter.aecf.org/data/tables/101-child-population-by-age-group · KIDS COUNT · SNIPPET
- [V30] https://europepmc.org/article/MED/34099398 · Breinbjerg 2021 systematic review · VERBATIM abstract
- [V31] https://europepmc.org/article/MED/11888377 · Schum 2001 · VERBATIM abstract
- [V32] https://europepmc.org/article/MED/23182948 · https://europepmc.org/article/MED/23759503 · Duong 2013 (two papers) · VERBATIM abstracts
- [V33] https://www.morganlewis.com/pubs/2024/11/new-york-and-california-bans-on-pfas-in-textiles-and-apparel-begin-january-1-2025 · Morgan Lewis · SNIPPET
- Re-used tags: [V1]–[V13] (work/D1-s2-LOCKED.md, D1-s1-LOCKED.md, D1-Pre0-LOCKED.md, D4-s15-FINAL.md) · [W5][W6][U29][M5][M64][B1][P1][P9][P40][P49].

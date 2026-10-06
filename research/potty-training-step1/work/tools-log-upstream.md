# Tools log — upstream revision after the §11 lock (2026-10-06)
Legend: ✅ ran · 🔁 substitute (which one) · ➖ not needed (why — fallbacks only) · ❌ couldn't (why)

| Skill / tool | Status | Where / what happened |
|---|---|---|
| `agent-reach` | 🔁 Firecrawl | `agent-reach` → `command not found` (CLI not installed). Every web / Reddit / forum job was run with the Firecrawl MCP, per the page's rule. |
| Firecrawl `firecrawl_search` | ✅ | §2C: ~20 queries (Reddit r/kindergarten, r/Parenting, r/ADHDparenting, r/Autism_Parenting, r/Mommit…; What to Expect, BabyCenter, Mumsnet, ADDitude / Facebook groups; X). Pre-0: Alibaba listings, CPSIA lab cost, CPSC eFiling, ShipBob pricing. §1: sensory-underwear brands, Super Undies. Hit HTTP 429 three times; waited and continued. |
| Firecrawl `firecrawl_scrape` | ✅ | Amazon search pages ("training underwear big kids size 8 10", "kids incontinence underwear boys washable") and /dp/ pages (MooMoo 9T B0CZ34MF49, "Dinosaur 8-10Years" B0H1HL64KX) with `maxAge:0`; AliExpress search (US locale); Eurofins CPC guide (`directQuote`). Alibaba search page ❌ (CAPTCHA). |
| `product-pulse` (Skill `anthropic-skills:product-pulse`) | ✅ (partial) | Loaded and run on "big-kid training underwear, school-age daytime accidents". **X:** 2 queries returned only profiles, sports and news → **0 usable posts** (same as wave 1). **Reddit:** the productive channel (folded into the §2C searches). Fewer than the skill's 25–45 searches were run because the brief's target was ≥50 school-age snippets, reached at 60. Step 8 (save report + publish to Notion "Comments from X") **➖ not done**: this pass's outputs are the §2C files, and the Notion plugin needs authorisation in this session. |
| Amazon trick | ✅ (partial wall) | /dp/ pages for the big-kid listings (MooMoo 9T, "8-10Years") scraped for "Customers say" + star splits. Full reviews are behind sign-in; visible excerpts were almost all about toddlers, so only **1** school-age Amazon row entered the bank. Star splits and aspect counts were used as DATA in §0B / §1. |
| Forum tactics | 🔁 Firecrawl search | Reddit and forums block page fetches, so threads were found with `firecrawl_search site:…` (the page's fallback). Comment counts weren't visible, so threads aren't ranked by replies. |
| YouTube comments (yt-dlp, agent-reach's video route) | ✅ | `yt-dlp --write-comments` on 4 school-age daytime-wetting videos: 2 returned comments (172 and 18), 1 hit the bot wall ("Sign in to confirm you're not a bot"). 4 new VERBATIM rows (f1V_VhGKgwE). |
| `playwright-skill` | ✅ | Google Trends (§0B): global Playwright 1.56.1, headless Chromium through the session proxy, **proxy CA trusted via the pre-configured NSS store — no TLS bypass flags** (the wave-1 script's `--ignore-certificate-errors-spki-list` flag was dropped). 5 captures of `widgetdata/multiline` JSON (2 comparisons + 3 solo terms). |
| Google Trends | ✅ | Via Playwright (above). |
| Winning Hunter `search_exploding_topics` | ➖ | §0B fallback only; Google Trends worked. |
| Winning Hunter `get_store_details` | ✅ | trysaphire.com, hellobloomkids.com, superundies.com, brightkidco.com. |
| Winning Hunter `search_facebook_ads` | ✅ | landingurl brightkidco.com (13 ads), superundies.com (4), trysaphire.com US longestrunning (103; result saved to file, read with `jq`), smartknitkids.com (0); pagename "goodnites" US (2, last seen 2024). Note: the `last_seen_from/to` filter did not narrow the Saphire pull (rows with April last-seen came back), so "ads still seen 2026-10-06" is read per row. |
| Winning Hunter `search_tiktok_products` | ✅ | US, 30d: "training underwear big kids" (no 5–9 listing), "incontinence underwear kids" (adult pads only). |
| `jq` / script tally | ✅ (python + jq) | `build_bank.py` (de-dupe, schema validation; first 514 rows byte-identical), `tally.py` (+ locked-segment cut), `cuts.py` re-run to `cuts-output-601.txt`, `addsrc.py` for cited rows. |
| WebSearch / WebFetch | ➖ | Not needed; Firecrawl recovered from its 429s. |
| `browser-use` | ➖ | Fallback only; Playwright worked. |
| Facebook Ad Library (browser) | ➖ | Not re-run in this pass: region proof for the new advertisers came from Winning Hunter `countries` fields. The §1 / §2 Ad Library checks from wave 1 stand. Re-check BrightKidCo / Kid Confident / Super Undies monthly. |
| SimilarWeb | ➖ | Not re-run; superundies.com "Health - Other" carried from [W2]. Traffic from Winning Hunter `get_store_details`. |
| Alibaba / 1688 OEM quotes | ❌ → 🔁 search snippets | Alibaba search returned "CAPTCHA Verification"; 1688 not attempted (Chinese-language login wall). Listing prices / MOQs were taken from Alibaba search-result snippets (SNIPPET) and flagged PROVISIONAL. **No real OEM quote exists yet** — Nikita must request them. |
| AliExpress | ✅ | US-locale search; every absorbent kids item was a $0.99 "New shoppers" teaser → rejected per Pre-0. |
| `research-doc` | ➖ | This was a targeted upstream revision inside the run, not a full doc run. |
| Notion connector · Google Drive | ➖ | Not required for §0–§2C; they belong to Funnel Map / §15 / delivery. |

## Blockers, in one place
- **No real OEM quote** (Alibaba CAPTCHA, no supplier contact). Pre-0 remains PROVISIONAL at $4.60 landed.
- Reddit, forum and most new rows are **SNIPPET** (75 of 79 locked-cut rows). Confirm wording at the URL before live creative.
- X gives no usable school-age content.
- Winning Hunter's coverage of big CPG brands (Goodnites, Pull-Ups) is thin, so "0 Meta ads" for them is low confidence.
- Segment search volume is ≈0, so Trends can't prove or disprove a school-start peak for the segment itself; the conversation-month tally is INFERENCE (post dates are estimates).

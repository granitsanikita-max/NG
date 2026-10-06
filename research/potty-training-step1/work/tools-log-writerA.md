# Tools log — Writer A (§3 → §11 + LOCK), 2026-10-06

**Key:** ✅ ran · 🔁 substitute · ➖ not needed · ❌ couldn't

| Tool / skill | Status | Where / what |
|---|---|---|
| `research-doc` | 🔁 | I am a writer sub-agent working the page sections directly, not the skill runner. The page text was followed line by line from sections/08-3.md through 20-11.md |
| **§2C data bank + python tallies** | ✅ | work/3-11-src/cuts.py (cuts #1–#19), quotes.py, addsrc.py; quote-integrity check. Output: work/tallies-3-11.md |
| **SimilarWeb** (§3 demographics) | 🔁 | Firecrawl scrape of similarweb.com. upairy.com ✅ (demographics, re-confirmed M39). brightkidco.com and superundies.com returned "No Data to Display" for demographics (<20K visits) → those fields marked INFERENCE [W1][W2] |
| **Firecrawl** `firecrawl_search` | ✅ | §5 discourse proxy (Reddit school-age accidents, 25 threads) [W8]; symptom → cause medical pages (Boston Children's [W9], NIDDK [W10]; a Mayo bed-wetting result was seen but not used, so W11 is unassigned); older-kid sensory underwear sweep [W12] |
| **Firecrawl** `firecrawl_scrape` | ✅ | SimilarWeb ×3 |
| `agent-reach` | 🔁 | Not required in §3–§11 except §10 / §10B. Firecrawl search was used for the same job (CLI not installed in wave 1, per tools-log-2C) |
| `product-pulse` (§10) | ➖ | Ran in wave 1 §2C (X + Reddit rows N-series in the bank). §10 is built from that bank. Nothing new needed for the counts |
| **Amazon trick** (§10, §10B, §11) | ✅ (reused) | 1★ / 5★ rows from the wave-1 Amazon / Trustpilot / Walmart mining (77 star-rated rows, 30 at 1–2★) were sorted into likes, dislikes, horror stories and objections. No new scrape: the /dp/ walls were documented in wave 1 |
| **Forum tactics** (§10, thread titles) | ✅ | Thread-title list for school-age accidents in §5 [W8]. The full §14 hook list is not in scope for this writer |
| **Winning Hunter** `search_facebook_ads` | ✅ | "big kid training underwear" US [W3]; "sensory underwear kids" US [W4]; "accidents at school" adtext US [W5]; landingurl brightkidco.com [W7]. **New finding:** school-age bedwetting supplement brands (Saphire, Bloomwise) are scaling on US Meta |
| **Winning Hunter** `search_tiktok_ads` | ✅ | "training underwear" US = 0 [W6] |
| **Playwright / browser** | 🔁 | Not re-run. §4 visual contrast used the wave-1 Playwright PDP screenshots (work/15-captures/*-1-pdp.png), viewed directly |
| **Facebook Ad Library** | ➖ | Region proof was done in wave 1 (§1/§2). Winning Hunter `search_facebook_ads` with `countries: US` was used for the new big-kid / school-age checks (🔁 method per page rule) |
| Google Trends | ➖ | §0B-only tool. A school-age term check is listed as a §0B revision in LOCK-decision.md |
| Notion / Google Drive | ➖ | Delivery steps, not in this writer's scope |

**Couldn't / gaps:**
- ❌ No pour-tested sample exists, so the capacity number is OPEN (§11 #1).
- ❌ SimilarWeb demographics exist for UpAiry only.

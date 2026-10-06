# Tools log — Market agent (Pre-0, Audit, §0, §0B, §1, §2 DRAFT, §2B) — 2026-10-06

Legend: ✅ ran · 🔁 substitute (which one) · ➖ not needed (why) · ❌ couldn't (why)

| Skill / tool | Status | Where | Notes |
|---|---|---|---|
| `research-doc` | ➖ | — | The parent session orchestrates the page. This sub-agent wrote its assigned sections only. |
| `product-pulse` | ➖ | — | Required at §2C / §10 / §14 / §20, not in these sections. |
| `agent-reach` | ❌ → 🔁 Firecrawl | §2 (Reddit fact-check) | `agent-reach doctor --json` → `agent-reach: command not found` (CLI not installed). Used `firecrawl_search` (site:reddit.com) for the same job. Results are tagged SNIPPET. |
| Firecrawl `firecrawl_search` | ✅ | Pre-0, §0, §2, §2B | AliExpress / CJ discovery; de minimis; CDC births; NCES; Reddit working-parent threads; CPSC, FTC (reviews rule, health guidance, textile labelling, ROSCA), Meta policy, PFAS. |
| Firecrawl `firecrawl_scrape` (`formats:["query"]`) | ✅ | Pre-0, Audit, §0B, §1, §2 | AliExpress search ×2 ✅. AliExpress item pages ×2 → empty shell ❌. CJ search → "Human verification" ❌. Amazon search ×3 ✅. SimilarWeb ×2 ✅. UpAiry PDP query (tiers not in DOM; got them from the HTML config instead). |
| `playwright-skill` (headless) | ✅ | Audit, §0B, §1, §2 | The skill folder only had SKILL.md (no `run.js`), so scripts ran on the globally installed Playwright with Chromium from `/opt/pw-browsers`. Proxy TLS was fixed by trusting only the session proxy CA (SPKI pin of `/root/.ccr/agent-proxy-ca.crt`). **Jobs:** UpAiry PDP + `/pages/training-underwear` + `/pages/daycare-mandate` (text + screenshots); Google Trends ×6 queries; Facebook Ad Library ×6 queries; AliExpress item pages ×3 (bot-blocked ❌). |
| `browser-use` | ➖ | — | Playwright worked. |
| Audit first | ✅ | Audit | UpAiry PDP + persona advertorial (+ daycare-mandate page found in passing). |
| Google Trends | ✅ (via Playwright) | §0B | US ×3 query sets, GB, AU, CA. Not blocked, so no fallback. |
| WH `search_exploding_topics` | ➖ | — | Fallback only. Google Trends rendered. |
| Amazon (marketplace demand) | ✅ | §0B, §2 | "potty training underwear", "reusable training pants toddler", "reusable bedwetting underwear kids": review counts + "bought in past month". |
| Amazon trick (5★ / 1★ sorting) | ➖ | — | Required at §2C / §10 / §10B / §11. |
| Forum tactics | ➖ | — | Required at §2C / §5 / §14 / §18. |
| SimilarWeb | ✅ (via `firecrawl_scrape`) | §1 | upairy.com (US 95.38%, F 77% / M 23%, 45+ = 38.9%); kidconfident.co (<20K, VN artifact). |
| WH `search_facebook_ads` | ✅ | §0B, §1, §2 | US-filtered keyword pulls k1–k5 (lastseen, adtext, landingurl, max_active_ads stepping); most-duplicated (`min_duplicates: 2`, `landingurl`, longestrunning) for upairy / kidconfident / brightkidco; longestrunning for brightkidco / tinytotsundies; pain search (adtext "potty training", 100–660 page ads). Pagination with `scroll` until no new advertisers (k1 2 pages, k2 3, k3 2). Merged with the same-day 45-search corpus. |
| `jq` (+ Python) | ✅ | §0B, §1 | De-duplicated 75 result files → 1,316 unique ad IDs / 908 unique copy rows; advertiser counts; ad-log extraction. |
| WH `get_store_details` | ✅ | Audit, §1 | upairy.com, kidconfident.co, brightkidco.com. |
| WH `get_store_top_ads` | ✅ | §1 | Meta: upairy, kidconfident, brightkidco (0 ads), tinytotsundies (0 on own page; 74 on "Rejuna"). TikTok: upairy (empty). Google covered by `search_google_ads`. |
| WH `find_similar_shops` | ✅ (low value) | §1 | kidconfident.co returned 19 name-matched, irrelevant stores (same failure file A saw on upairy.com). |
| WH `brief_competitor` | ✅ | §1 | upairy.com: only its own persona ads + look-alike domains. |
| WH `search_tiktok_products` | ✅ | §0B | keyword "potty training underwear" and "training pants", country US. |
| WH `get_tiktok_product` | ✅ | §0B | BIG ELEPHANT 1729569671740888020 (metrics + history); PeekabooCo 1732439062662713947 (metrics). |
| WH `search_tiktok_ads` | ✅ | §0B, §1, §2 | "potty training", countries US → 5 ads, 0 reusable DTC. |
| WH `search_google_ads` | ✅ | §0B, §1 | domain upairy.com, country US → 18 rows (56 ads on account). **Corrects file A** ("Google unverifiable"). |
| Facebook Ad Library | ✅ (+ 🔁 cross-check) | §0B, §1, §2 | Playwright headless, Active ads. US "potty training underwear" (~950), US "daycare potty" (~210), GB "potty training pants" (~460) rendered. CA / AU returned "No ads match" and some US loads 403'd first → region cross-checked with WH `search_facebook_ads countries:US` 🔁 (low confidence on CA / AU). |
| TikTok + Google / Amazon / Etsy sweep | ✅ / 🔁 | §0B, §1, §2 | TikTok ✅, Google ✅, Amazon ✅. Etsy 🔁: relied on file B's same-day Etsy scrape (not re-scraped). |
| AliExpress (supplier prices) | ✅ partial | Pre-0 | Search-card list prices captured; teaser (`m03_new_user`) prices rejected. Item pages blocked ❌. |
| CJdropshipping | ❌ | Pre-0 | Bot verification wall (Firecrawl); `site:cjdropshipping.com` search found no listing. |
| Notion connector | ➖ | — | Funnel Map / §15 only. |
| Google Drive | ➖ | — | Delivery is done by the parent session after §20. |

**Corrections to prior files logged:**
1. File A said "country=US returned 0 rows". It works now (§0B).
2. File A said "Google unverifiable". UpAiry runs 56 US Google ads (§0B / §1).
3. POSITIONING.md's daycare / working-parent wedge is **already run by UpAiry** in the US (§2). Killed.

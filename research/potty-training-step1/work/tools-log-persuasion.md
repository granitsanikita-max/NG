# Tools log — persuasion collector (§12 · §13 · §13B · §16 · §17 · §18B), 2026-10-06

| Skill / tool | Status | Why / what it did |
|---|---|---|
| `agent-reach` (skill loaded) | 🔁 Firecrawl MCP + WebSearch/WebFetch | `agent-reach` CLI not installed (`agent-reach: command not found`), so `doctor --json` could not run. Its web, Reddit and fact-check jobs (§12, §18B) ran on `firecrawl_search` / `firecrawl_scrape`, as the page's fallback rule says. |
| Firecrawl `firecrawl_search` | ✅ | ~25 searches: authorities and follower counts, the 92% claim, Brazelton/Pampers, Reddit daycare threads, absorbency, side-snap listings, bladder capacity. Repeated 429 rate limits; retried after waiting. |
| Firecrawl `firecrawl_scrape` | ✅ | Seim 1989 PDF, TIME 1999, Tampa Bay Times 1999, roastmypost export, BJU abstract, Amazon BIG ELEPHANT dp page, AliExpress category pages. NYT and PubMed blocked (NYT "not supported"; PubMed reCAPTCHA). |
| Firecrawl research tools (`research_search_papers`, `inspect_paper`) | ✅ | Paper discovery (Breinbjerg, Kaerts, Blum, Schum). `research_read_paper` returned empty passages, so abstracts were pulled from the Europe PMC REST API instead. |
| Europe PMC REST API (curl) | 🔁 substitute for PubMed | PubMed pages are behind reCAPTCHA; Europe PMC returned verbatim abstracts for about 25 PMIDs. |
| WebSearch / WebFetch | 🔁 supplement | Used when Firecrawl was rate-limited: NCES, AAP healthychildren, Good Inside, BLF FAQ, Oh Crap consultant, PMC1702395, Kiddoo CMAJ, Kimberly-Clark PDF, NHS GHC PDF. WebSearch summaries are tagged SNIPPET only. |
| `pdftotext` | ✅ | Extracted the Breinbjerg 2021 full text, the K-C history PDF and the NHS GHC guide. |
| `product-pulse` | ➖ | Not required for §12/§13/§13B/§16/§17/§18B per the "Where each skill is REQUIRED" table (that table puts it in §2C/§10/§14/§20). |
| `playwright-skill` / `browser-use` | ➖ | Not required for these sections (needed for Audit / §0B / §1 / §2 / §15). |
| Winning Hunter | ➖ | Not required here. The TAKEN check used the existing A-paid-ads-map.md (WH-derived, 2026-10-06). |
| Amazon trick | ➖ | Not required for these sections (§2C/§10/§10B/§11). One Amazon /dp/ page (B0D6MXSLMY) and the MooMoo listing were read for §17 features. |
| Forum tactics | ➖ | Not required for these sections (§2C/§5/§14/§18). Reddit was reached only through `site:reddit.com` searches (SNIPPETS). |
| Instagram follower counts | ✅ (SNIPPET) | From search-result snippets of instagram.com profile pages plus HypeAuditor/CreatorDB. Instagram pages were not opened directly. |

## Failed / blocked
- ❌ nytimes.com: blocked for both Firecrawl and WebFetch. The NYT 1999 lines are SNIPPET only; TIME and Tampa Bay Times give the same facts VERBATIM.
- ❌ pubmed.ncbi.nlm.nih.gov: reCAPTCHA. 🔁 Europe PMC.
- ❌ Brazelton 1962 PDF (crearamor.wordpress.com): scanned, so no text. 🔁 Kiddoo 2012 CMAJ secondary citation.
- ❌ thirsties.com and pull-ups.com: HTTP 445/403. 🔁 search snippets.
- ❌ AliExpress side-snap training *underwear* product page: not found (the search returned adult trousers). Logged as a sourcing gap.

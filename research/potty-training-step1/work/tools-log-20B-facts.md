# Tools log · §20 B fact-check (2026-10-06)

| Tool / skill | Status | What it did / why |
|---|---|---|
| `agent-reach` | 🔁 substitute | `agent-reach` is not installed (`command not found`). Firecrawl MCP (`firecrawl_search` + `firecrawl_scrape`) did the same fact-check jobs, per the page rule. |
| Firecrawl `firecrawl_scrape` | ✅ | Tampa Bay Times 1999 (directQuote: all four Brazelton lines re-confirmed). ERIC survey page (×2: stats, sample, survey name). Meta Transparency personal-attributes page. Instagram P49 failed with "site not supported" (logged ❌ below). |
| Firecrawl `firecrawl_search` | ✅ | Pampers size-6 1998 dating (Baltimore Sun, Sun-Sentinel, NYT snippet). Azrin book sales (NYT obituary). Bambino Mio 60–90 ml. Census 5–9 cohort (KIDS COUNT). AB 1817 TOF thresholds. OEKO-TEX label rules. 16 CFR 260.9. Victor Mills. Brazelton/P&G foundation (no primary hit). Hodges. |
| Europe PMC REST API (`curl`) | ✅ | Abstracts for PMIDs 31060913, 12913750, 34099398, 41099785, 11888377, 15238916, 887331, 16795291, 10930924, 23495098, 22207492, 23182948, 23759503, 11875176, 14662573, 26695997, 15154222, 27329866, 25772695, 24508614, 13872676, 913900/913901, 2592922, 41249012, 15173531, 17020216. |
| `curl` + `pdftotext` | ✅ | Maternik 2016 (ics.org). Rittig 2010 ICCS reappraisal (ics.org). Kimberly-Clark training-pants PDF. Seim 1989 J Fam Pract PDF. |
| WebFetch | ✅ | Wake Forest bladder page. Boston Children's daytime wetting. TIME 1999. Conversable Economist. CDC NCHS births. HealthyChildren (AAP). Kiddoo CMAJ (PMC). NCES Fast Facts. NIDDK. CPSC CPC page. Tampa Bay (chrome only, so Firecrawl was used instead). Meta business help (title only, so Firecrawl was used instead). |
| WebSearch | ✅ | ICCS expected-bladder-capacity formula. This led to the ics.org Rittig PDF. |
| `product-pulse` | ➖ | Not needed for this sub-task. It mines voice-of-customer, not historical/medical facts, and is run in the §20 main pass. |
| `playwright-skill` / `browser-use` | ➖ | Not needed. Every page needed rendered via Firecrawl or WebFetch. browser-use MCP was also down (connect timeout). |
| Instagram P49 (Bambino Mio 60–90 ml) | ❌ | Firecrawl doesn't support instagram.com. It stays SNIPPET, and the copy fix is to film our own comparator pour. |
| NYT 1999 article (P70) | ❌ (full text) | Paywalled. The snippet matches the quoted line, so it stays CONFIRMED (SNIPPET). |

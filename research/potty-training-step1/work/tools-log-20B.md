## §20B market skeptic — tools log (2026-10-06)
| Tool / skill | Status | Where / what |
|---|---|---|
| Winning Hunter `search_facebook_ads` | ✅ | "accidents at school" adtext US (9); brightkidco.com landingurl (13) + pagename (latest 09-05); "absorbent underwear kids" US (295, page 1 = UpAiry); "incontinence underwear for kids" US → found CARER; carerspk.com landingurl US (395, mostly adult); `kids-washable-incontinence-underwear` landingurl (27 kids ads); kidconfident.co last 30d (636, page 1). Big results saved to files and read with `jq` |
| Winning Hunter `get_store_details` | ✅ | trysaphire.com, hellobloomkids.com (numbers re-confirmed), carerspk.com (new) |
| Winning Hunter `search_tiktok_ads` | ✅ | "training underwear" US = 0; "incontinence underwear" US = 0 |
| Winning Hunter `search_tiktok_products` | ✅ | "big kid training underwear" US = 0; "kids incontinence underwear" US = 0 |
| Winning Hunter `search_google_ads` | ✅ (partly ➖) | keyword "incontinence underwear kids" US = index noise; domain carerspk.com = 89 ads (active since 2023) |
| Firecrawl `firecrawl_scrape` | ✅ | Walmart TIICHOO ×2, Amazon "kids absorbent underwear ml school age", CARER kids PDP, Super Undies Brain Trainer specs + FAQ (large results read with `jq`) |
| Firecrawl `firecrawl_search` | ✅ | Super Undies ml specs; Census ACS 5–9 population |
| WebSearch | ✅ | big-kid ml underwear brands (found TIICHOO, Conni); Conni US availability; school accident kits; China tariff stack Oct 2026; HTS 6107.11 / 6108.21; ROSCA / CA ARL subscription rules; Census |
| WebFetch | ✅ | Boston Children's daytime wetting; kidney.org product page; makemine tariff page; PubMed (blocked → Europe PMC via curl ✅) |
| `agent-reach` | 🔁 | CLI not installed (`which agent-reach` → none); Firecrawl + WebSearch used for the same jobs |
| `product-pulse` | ➖ | Not needed for a market fact-check (voice-of-customer is covered by the §2C bank and the facts skeptic) |
| Facebook Ad Library (direct) | 🔁 | Not rendered headless in this run; region proven with WH `search_facebook_ads` `countries: US` |
| `playwright-skill` | ➖ | Not needed: Firecrawl reached every PDP / listing checked |
| Census API (curl) | ❌ | Empty response; substituted the data.census.gov DP05 snippet via Firecrawl search |
| Python / `jq` | ✅ | KPI re-computation (all tables match); subscription LTV math; ad-file parsing |

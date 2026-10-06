# Pre-0 · Economics & KPIs (PROVISIONAL)

> **⚠️ PROVISIONAL. Every cost here is an estimate.** Nikita gave no supplier, landed cost or price (work/pre0-inputs.md). Supplier prices below come from real AliExpress listings (list price, never the welcome-deal teaser). Shipping and duty are estimates. Re-run this table when real COGS arrive, and again at §15's recommended price.

## Inputs
| Input | Value | Status |
|---|---|---|
| Target region / language | **US first**, English. UK, CA and AU checked as expansion markets (§0B, §2). | From Nikita (delegated) |
| Current store / page | None. Audit target = UpAiry (see Audit first). | From Nikita |
| Supplier link | None. Provisional = AliExpress listings below. | **PROVISIONAL** |
| Landed cost / unit | **$4.18–$4.68 per pair** depending on pack size (build-up below). | **PROVISIONAL** |
| Selling price / offer | 4-, 6- and 8-pack bundles, plus a 5-pack that matches the leader's price, all taken from the competitor ladder. | **PROVISIONAL** |
| Processing % | 3% (default) | Default |

### Supplier evidence (real listings, 2026-10-06, US locale)
The prices are list prices. Every listing marked `m03_new_user` (AliExpress's first-order welcome teaser) was **rejected as a price**; its crossed-out "original" price is used instead.

| # | Listing | Price used | Teaser seen (ignored) | Sold / rating | Tag |
|---|---|---|---|---|---|
| L1 | "8pcs/4pcs Washable Baby Potty Training Pants Reusable Toilet Trainer Panty…" (item 2255799937806851) | **$19.42 per pack.** Assumed to be the 8-pc SKU, so **$2.43/pair**. | $8.42 (new-user) | 400 sold, 4.4★ | DATA [M6][M7] |
| L2 | "4PCS Baby Waterproof Diapers Pee Shorts Underwears Reusable Soft Ecological Cotton Toddler Potty Training Pants" (item 3256805378033065) | **$9.18 per 4, so $2.30/pair** | $1.19 (new-user) | 2,000+ sold, 4.6★ | DATA [M10] |
| L3 | Side-button / snap variant: "Baby Training Pants Buttons Diaper Baby Underwear… Washable" (item 1005006995126534) | **$2.39** (bundle-deal price, not tagged new-user) | — | 3,000+ sold, 4.9★ | DATA [M6] |
| L4 | "3Pcs Baby Diaper Training Pants for Girls Boys Washable…" (item 1005009054913134) | $4.33 per 3, so $1.44/pair. This is a Bundle-Deals price, so it is treated as a promo floor and not used. | — | 3,000+ sold, 4.9★ | DATA [M6] |

- AliExpress item pages returned a bot-check ("punish") page in headless Playwright and an empty shell in Firecrawl. Pack-SKU splits therefore could not be confirmed, so the L1 assumption (that $19.42 buys 8 pieces) is **flagged** [M7].
- CJdropshipping search returned a "Human verification" wall [M11], so no CJ price was captured ❌.
- The side-snap variant L3 is toddler-sized (a "diaper"-style button pant). No sourceable listing yet combines side-open, underwear look and sizes 4–9 (consistent with [M47] D §4).

### Landed-cost build-up (per pair, PROVISIONAL)
| Component | Value | Basis |
|---|---|---|
| Product (FOB, conservative) | $2.43 | L1 list price ÷ 8 [M7] |
| Import duty + brokerage | $0.85 (≈35% of goods) | **INFERENCE.** US de minimis duty-free entry ended 2025-08-29 for all countries, and for China/HK in May 2025 [M12]. The rate is an estimate covering MFN apparel duty plus China-specific add-ons. **Confirm with a customs broker.** |
| CN→US shipping | $4.00 per order + $0.40 per pair | **INFERENCE.** Typical AliExpress/agent standard line, 7–12 days. UpAiry promises "4–8 days" to the US [M1]. |
| Packaging + insert card | $0.75 per order ("other") | INFERENCE |

## KPI table (metrics as rows, offer variants as columns; PROVISIONAL)
Price ladder source: competitors' single-pair list prices are $19.50–$22 (Kid Confident $19.50–$19.99 [M25][M41], UpAiry $21 with $29.99 compare-at [M3]). What they actually charge is set by bundle tiers. UpAiry's live Kaching config: **1 pair $21 · "BUY 2, GET 3 FREE" 5 pairs $35 · "BUY 4, GET 6 FREE" 10 pairs $68** (DATA, page config [M4]). Variants V1–V3 are anchored to a $21 list price; V4 copies the leader.

| Metric | V1 · 4-pack $49 | V2 · 6-pack $59 (hero) | V3 · 8-pack $69 | V4 · 5-pack $35 (match UpAiry) |
|---|---|---|---|---|
| Price (order value) | $49.00 | $59.00 | $69.00 | $35.00 |
| Effective $/pair | $12.25 | $9.83 | $8.63 | $7.00 |
| Landed / unit | $4.68 | $4.35 | $4.18 | $4.48 |
| Landed × units | $18.72 | $26.08 | $33.44 | $22.40 |
| Processing (3%) | $1.47 | $1.77 | $2.07 | $1.05 |
| Other (packaging) | $0.75 | $0.75 | $0.75 | $0.75 |
| **Contribution margin $** (= break-even CPA) | **$28.06** | **$30.40** | **$32.74** | **$10.80** |
| Contribution margin % | 57.3% | 51.5% | 47.4% | 30.9% |
| **Break-even ROAS** | **1.75** | **1.94** | **2.11** | **3.24** |
| Target CPA @20% net (**KILL line**) | $18.26 | $18.60 | $18.94 | $3.80 |
| Target ROAS @20% net | 2.68 | 3.17 | 3.64 | 9.21 |
| Target CPA @30% net (**SCALE line**) | $13.36 | $12.70 | $12.04 | $0.30 |
| Target ROAS @30% net | 3.67 | 4.65 | 5.73 | 116.7 (impractical) |

**Formulas**
- CM $ = Price − (landed per unit × units) − (3% × Price) − other.
- CM % = CM $ ÷ Price.
- Break-even ROAS = Price ÷ CM $. Break-even CPA = CM $.
- Target CPA at n% net = CM $ − (n × Price). Target ROAS = Price ÷ Target CPA.
- Scale line = the 30%-net CPA: at or under it, scale. Kill line = the 20%-net CPA: consistently above it, fix or kill.
- All values are computed per variant; landed per unit = $2.43 + $0.85 + $0.40 + ($4.00 ÷ units).

**Reading it**
- **V2 (6-pack $59) is the provisional hero.**
  - Scale at CPA ≤ $12.70 (ROAS ≥ 4.65).
  - Kill if CPA stays above $18.60 (ROAS < 3.17).
  - Break-even is a $30.40 CPA (ROAS 1.94).
- **V4 (copying UpAiry's $35 for 5) is uneconomic for a newcomer.**
  - CM is only $10.80, and the 30%-net target is effectively impossible (CPA $0.30).
  - The 20%-net target needs a CPA of $3.80.
  - UpAiry can run $7/pair only because of scale, supplier terms and LTV from cross-sells (bed mat $29.99, alarm $39.99, inserts $32.99 [M24]) — INFERENCE. **Don't price-match the leader.**
- **Sensitivity (spec risk):** the goods cost may be $4.00/pair instead of $2.43, for example for the bigger sizes or a better spec that §2 may require. In that case:
  - V2's CM falls to $17.68 (30.0%), and its 30%-net target becomes impossible (−$0.02).
  - V1 holds a 40% CM.
  - Bigger-size or better-spec SKUs therefore need either ≥$12/pair effective pricing or smaller packs.

## Benchmark check (is this CPA realistic?)
- UpAiry's WH AOV is $18.48 (DATA [M24]). Taken literally, that looks low next to its own $35/$68 tiers, so treat it as unreliable.
- Kid Confident's WH AOV is $19.75 (DATA [M25]).
- Neither figure verifies CPA. No live account data exists, so **a CPA ≤ $18.60 on cold Meta traffic is unproven.** It is a test hypothesis, not a forecast.

## So What → do this
1. Test **V2 (6-pack $59)** as the hero and **V1 (4-pack $49)** as the entry tier, with a $21/pair list anchor.
2. Kill or fix any ad set whose CPA holds above **$18.60**. Scale anything at or below **$12.70**.
3. Do **not** match UpAiry's $35/5.
4. Before any spend, order 2–3 samples of L1/L2/L3 at list price and run a pour test (ml held before leaking).
5. Get a customs-broker duty quote and replace the 35% estimate.

> **⏰ COGS REMINDER (Nikita):** send the real supplier link, unit price per pack size, shipping per order and duty quote. This table must be re-run with them, and again at §15's chosen price, before any ad spend.

## Sources
- [M1] UpAiry PDP: https://www.upairy.com/products/potty-training-underwear. Playwright headless, 2026-10-06 (VERBATIM).
- [M3] UpAiry product JSON: https://www.upairy.com/products/potty-training-underwear.js. 2026-10-06 (DATA).
- [M4] UpAiry PDP HTML, Kaching `dealBars` config: same URL, fetched 2026-10-06 (DATA. Tiers read from page config; they did not render in headless).
- [M6] AliExpress search "baby potty training pants": https://www.aliexpress.com/w/wholesale-baby-potty-training-pants.html. Firecrawl query, US, 2026-10-06 (DATA).
- [M7] AliExpress item 2255799937806851: https://www.aliexpress.us/item/2255799937806851.html. Item page blocked; price from search card, 2026-10-06 (DATA).
- [M10] AliExpress search "toddler training underwear snap": https://www.aliexpress.com/w/wholesale-toddler-training-underwear-snap.html. 2026-10-06 (DATA).
- [M11] CJdropshipping search: https://cjdropshipping.com/search/potty+training+pants.html. Blocked by human verification, 2026-10-06.
- [M12] US de minimis ended: https://www.vatcalc.com/global/global-2023-vat-gst-changes/ and https://www.marketresearchfuture.com/reports/dropshipping-market-20308. Search snippets, 2026-10-06 (SNIPPET).
- [M24] Winning Hunter `get_store_details` upairy.com, 2026-10-06 (DATA).
- [M25] Winning Hunter `get_store_details` kidconfident.co, 2026-10-06 (DATA).
- [M41] Kid Confident Big Kid Sizes product JSON: https://kidconfident.co/products/potty-training-underwear-big-kid-sizes.js. 2026-10-06 (DATA).
- [M47] Prior research: /home/user/NG/docs/potty-training-research/D-skeptic.md (2026-10-06).

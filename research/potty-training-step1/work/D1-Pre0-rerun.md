# Pre-0 · Economics & KPIs: re-run at §15's recommended test price

*Doc 1. Re-run 2026-10-06 after §15 (Competitor Offers + Price Ladder). Same formulas as Pre-0. US, USD, processing 3% (default).*

> ⚠️ **PROVISIONAL COSTS.** No supplier has been chosen and no landed cost has been received from Nikita (`work/pre0-inputs.md`). Every cost below is a placeholder built from real listing prices plus labelled assumptions. Re-run this table when the real COGS / landed quote arrives.

## Cost inputs (PROVISIONAL)

| Input | Value | Basis |
|---|---|---|
| Product cost per pair | **$2.27** | AliExpress "3 Pieces/lot Baby Training Pants 6 Layers" at **$6.82 per 3** (900+ sold, no "New shoppers" / welcome-deal tag) [O69]. Welcome-deal teaser prices ($1.09 "New shoppers save $X") were excluded per Pre-0. |
| Inbound freight + QC per pair | **$0.60** | INFERENCE (placeholder for consolidated sea/air freight to a US 3PL). Not quoted. |
| **Landed per pair** | **$2.87** | $2.27 + $0.60, PROVISIONAL |
| Other per order: outbound US shipping + pick/pack + mailer | **$7.00** | INFERENCE (placeholder). Competitors charge $5.99 shipping on small orders (Kid Confident [O6]), so this is in range but not quoted. |
| Kit extras (wet bag + caregiver card + chart) on the 10- and 15-pair kits | **+$2.50** → other = **$9.50** | INFERENCE (placeholder). Not sourced. |
| Processing | **3% of price** | Pre-0 default |

CJ Dropshipping could not be priced: it was blocked by human verification [O70].

## Offer variants (from §15 "Price point to test")

- Single pair $19 (anchor)
- 5 pairs $49
- **10-pair Home + Daycare Kit $79 = recommended test price / target AOV, pre-selected**
- 15 pairs $99

## KPI table

| Metric | Single $19 | 5-pair $49 | **10-pair Kit $79 (test)** | 15-pair $99 |
|---|---|---|---|---|
| Units in order | 1 | 5 | 10 | 15 |
| Landed (units × $2.87) | $2.87 | $14.35 | $28.70 | $43.05 |
| Processing (3%) | $0.57 | $1.47 | $2.37 | $2.97 |
| Other per order | $7.00 | $7.00 | $9.50 | $9.50 |
| **Contribution margin $** | **$8.56** | **$26.18** | **$38.43** | **$43.48** |
| **Contribution margin %** | 45.1% | 53.4% | 48.6% | 43.9% |
| **Break-even ROAS** | 2.22 | 1.87 | **2.06** | 2.28 |
| **Break-even CPA** | $8.56 | $26.18 | **$38.43** | $43.48 |
| **Kill line: target CPA at ~20% net** | $4.76 | $16.38 | **$22.63** | $23.68 |
| Target ROAS at ~20% net | 3.99 | 2.99 | **3.49** | 4.18 |
| **Scale line: target CPA at ~30% net** | $2.86 | $11.48 | **$14.73** | $13.78 |
| Target ROAS at ~30% net | 6.64 | 4.27 | **5.36** | 7.18 |

**Formulas** (as in Pre-0):

- **CM $** = Price − (landed per unit × units) − (3% × Price) − other per-order costs
  - e.g. $79 − $28.70 − $2.37 − $9.50 = **$38.43**
- **CM %** = CM $ ÷ Price → $38.43 ÷ $79 = 48.6%
- **Break-even ROAS** = Price ÷ CM $ (= 1 ÷ CM%) → $79 ÷ $38.43 = 2.06
- **Break-even CPA** = CM $
- **Target CPA at n% net** = CM $ − (n × Price)
  - 20%: $38.43 − $15.80 = $22.63
  - 30%: $38.43 − $23.70 = $14.73
- **Target ROAS** = Price ÷ Target CPA
  - $79 ÷ $22.63 = 3.49
  - $79 ÷ $14.73 = 5.36
- **Scale line** = the ~30% net CPA: at or under it, scale. **Kill line** = the ~20% net CPA: consistently above it, fix or kill.
- CM% is above 30% in every variant, so no target is impossible.

**So what → do this:**

1. Test the **$79 10-pair kit** as the pre-selected middle tier. It needs a first-order **CPA ≤ $22.63 (ROAS ≥ 3.49)** to clear 20% net, and ≤ $14.73 (ROAS ≥ 5.36) to scale. Break-even is $38.43 / ROAS 2.06.
2. The single pair at $19 cannot carry paid traffic (break-even CPA $8.56). Keep it only as the anchor.
3. **Shipping and pack-out ($7–9.50) is the biggest cost after product.** Getting a real 3PL quote matters more than squeezing the unit price.

**Sanity check against the market (INFERENCE):**

- At UpAiry's own prices with the same provisional costs, the margins are thin:
  - 5 pairs for $35: CM = $35 − $14.35 − $1.05 − $7.00 = $12.60 (36%), break-even ROAS 2.78.
  - 10 pairs for $68: CM = $68 − $28.70 − $2.04 − $9.50 = $27.76 (40.8%), break-even ROAS 2.45.
- Pricing **above** UpAiry is needed for margin, and §15 justifies the premium with the kit, an honest guarantee and absorbency proof.

**📌 Reminder (send COGS):**

- Nikita, please send the real supplier link, unit price at MOQ, inbound freight per unit and the US 3PL pick/pack + postage quote.
- This table is PROVISIONAL until then.
- Every value marked INFERENCE above ($0.60 freight, $7.00 per order, $2.50 kit extras) must be replaced.

**Sources:**
- [O6] https://kidconfident.co/products/potty-training-underwear
- [O69] https://www.aliexpress.com/w/wholesale-toddler-potty-training-pants.html
- [O70] https://cjdropshipping.com/search/potty+training+pants.html (blocked)

The full O-list is in `work/D4-s15.md`.

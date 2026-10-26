# ECONOMICS — ProudFold
> Owned by: Economics & analytics planning.
> Front gate reads: brain/, PRODUCT.md. Back scoreboard reads: STORE.md, CREATIVES.md, live numbers.
> Rule: numbers are dated; append new reads, never overwrite history.

## Front gate (before we build) — set 2026-10-26, grounded in brain/01-market-competition-pricing.md
> Currency note: product/store sells in **USD**; the Meta ad account (`990807943351623`, "PROUDFOLD") bills in **AUD**. Break-even below is USD. Convert ad spend AUD→USD before judging ROAS (≈0.65 AUD/USD as a placeholder — confirm live rate).

- **Landed cost:** $6.70/tube single · $3.25/tube in a 5-pack · ~$9.75 for a 3-pack. Processing 2.9% + $0.30.
- **Sell price:** $29.95 single · $49.95 "Comfort Duo" 2-pack · $64.95 3-pack. (Brain is internally mixed on the 3-pack: Doc 1 models a $49.95 3-pack; the offer ladder in RESEARCH names $64.95 for the 3-pack. The one live order was a $64.95 3-pack. **Open: lock the 3-pack price + COGS.**)
- **Gross margin:** $29.95 single → **CM $22.08 / 73.7%**. $49.95 3-pack → CM ~$38.45 / 77% (before shipping; ~$33.95 / 68% if free-ship ~$4.50). 
- **AOV target:** ~$50 (2-pack is the intended hero of the ladder).
- **Break-even ROAS / CPA (the number ads must beat):**
  - Single $29.95 → **BE ROAS 1.36 · BE CPA $22.08**
  - 3-pack $49.95 → BE ROAS ~1.30 (1.47 with shipping) · BE CPA $38.45
  - **Use BE ROAS ≈ 1.4 and BE CPA ≈ $22 (single) as the working targets.**
- **Verdict:** **GO.** Margins are fat (73.7% CM); the constraint is CAC + ad-ban risk + reorder LTV, not margin. Money is in reorder LTV (~$60–120 over 2–3 refills), not first-order profit.

---

## Back scoreboard (once live)

### 2026-10-26 — First read: "WARM UP C1 Statiocs" (static test). Pulled by economics station.
**Source:** Meta Ads MCP (account 990807943351623, campaign 120251126990710504, date range = maximum) + Shopify analytics (proudfold.com). **All ad figures AUD. All store/revenue figures USD.**

**Verdict: TOO EARLY to scale or kill on sales — but the money is leaking at checkout, not at the ad.** Campaign is optimized for **Add to Cart** (not purchase), and total volume is tiny (A$97.96 / 817 impressions / 6 ATC). Do NOT make purchase/ROAS calls yet. The usable signals are creative (cost-per-ATC, CTR) and the store-side checkout drop-off.

**Campaign totals (all-time, AUD):**
| Metric | Value |
|---|---|
| Spend | **A$97.96** (≈ US$64 @ ~0.65 — approx) |
| Impressions / Reach / Freq | 817 / 624 / 1.31 |
| CPM | A$119.90 |
| Clicks (all) / CTR (all) | 73 / **8.94%** |
| Link clicks / link CTR | 52 / ~6.4% |
| CPC (all) / cost per link click | A$1.34 / A$1.88 |
| Landing page views / cost per LPV | 45 / A$2.18 |
| **Adds to cart / cost per ATC** | **6 / A$16.33 blended** |
| Purchases / ROAS | **0 / n/a** (campaign optimizes for ATC, so no purchase signal expected) |

**Funnel (campaign):** 817 impr → 52 link clicks (6.4%) → 45 LPV (87% load) → 6 ATC (13% of LPV) → **0 purchase**.
Read: **top-of-funnel is strong** (8.94% CTR, A$2.18/LPV). Chain breaks at **cart → purchase**.

**Per-static read (9 ads, ranked by what matters):**
| Ad | Spend AUD | Impr | CTR | CPM | LPV | ATC | Cost/ATC | Call |
|---|---|---|---|---|---|---|---|---|
| **AD7** | 11.86 | 134 | 6.72% | 88.51 | 7 | **4** | **A$2.97** | ⭐ early winner — best full-funnel |
| **AD9** | 13.02 | 126 | 7.14% | 103.33 | 2 | **2** | A$6.51 | watch — 2nd ATC driver |
| AD5 | 11.64 | 127 | **14.17%** | 91.65 | 15 | 0 | — | best hook/click (A$0.65 CPC) but 0 ATC — great scroll-stopper, weak at driving cart |
| AD3 | **30.93** | 173 | 9.25% | **178.79** | 6 | 0 | — | 🩸 early loser — ate 32% of budget, worst CPM, 0 ATC |
| AD6 | 20.48 | 149 | 7.38% | 137.45 | 7 | 0 | — | 🩸 ate 21% of budget, 0 ATC |
| AD1/AD8/AD2/AD4 | <$6 each | — | — | — | — | 0 | — | too little data, ignore |

**Biggest spend finding:** **AD3 + AD6 ate A$51.41 (52% of budget) for 0 ATC**, while **AD7 + AD9 drove all 6 ATC on A$24.88 (25%).** Budget is spread across statics regardless of result — reallocate toward AD7.

**Store-side reconciliation (Shopify, USD):**
- Real external orders in period: **0.** (`FROM sales` = 0 orders / $0.)
- Only "order" = **#1001, $64.95, "Sergey Granitsa," PAID** on 2026-10-25 → **self/family test order** (Nikita's surname), not a customer sale. Excluded from the scoreboard.
- Store funnel Oct 24–26 (when carts began): ~154 sessions → 10 sessions w/ cart adds → **11 sessions reached checkout → 1 completed (the test).** Real completed checkouts by customers = **0.**
- Meta's 6 ATC ≈ consistent with Shopify's 10 cart-add sessions (Meta counts ad-attributed only).

**CPA vs break-even:** No purchases → no real CPA yet. Blended cost/ATC A$16.33 (≈US$10.6) sits under BE CPA (US$22), and AD7's A$2.97 ATC is cheap — meaning **the ad economics are not the problem.**

**Winners to scale:** AD7 (lean budget here first). · **Losers to trim:** AD3, AD6 (pause/cut — burning budget at high CPM, 0 ATC).

**Decision:** **HOLD the test, do NOT scale or kill on sales data (too little volume + ATC-optimized).** The gating issue is **checkout conversion: 11 reached checkout, 0 real purchases.** That points at the store/offer/checkout, not the ads — and the store is known to be half-built (copywriting logs: GemSleep template leftovers, broken offer block, fake timer, 30-day vs 60-day guarantee, green buttons). **Next $ should fix the store before more ad spend, then re-test; if scaling later, switch the campaign objective from ATC to Purchase once the pixel has enough conversions.**

**Open / confirm later:** lock 3-pack price+COGS · confirm live AUD→USD rate · pull a Purchase-optimized read once the store is fixed and volume is 3–5× higher.

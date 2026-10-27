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

#### 2026-10-26 — Creative diagnosis (why AD3/AD6 bled, why AD5 clicks-no-carts)
Pulled the creatives. **All 9 statics are variations of ONE advertorial concept** — same first-person body ("It was never the rash. For twenty years I thought something was wrong with me… skin rubbing skin"), **same destination** (link not exposed per-ad via API; set at post level, shared — Shopify confirms the destination loads + reaches checkout, so no per-ad broken link). They differ only in image + hook headline:
- AD3 "It Was Never Your Body. It's Friction." (reframe) · AD6 reframe · **AD7 (winner) "It Was Never the Rash — It's the Rub" (mechanism reframe)** · AD5 "After 20 Years, I Finally Figured Out Why My Fold Rash Kept Coming Back" (curiosity/story).
- **Clicker-quality signal:** AD5+AD3+AD6 sent **28 LPV → 0 ATC**; AD7+AD9 sent **9 LPV → 6 ATC**. Mechanism-naming hooks pulled buyers; curiosity/identity hooks pulled tourists (AD5 = 14.17% CTR, A$0.65 CPC, 0 ATC = classic curiosity-gap: inflates CTR, deflates intent).
- **Honesty caveat:** at 130–170 impr / A$12–30 per ad, per-ad CPM & ATC are mostly NOISE. AD3's A$179 CPM is not a verdict. Don't file AD3/AD6 as "bad creative" — they're unproven. Banked conclusions are the two MACRO ones only: (1) checkout is the leak, (2) mechanism-hooks > curiosity-hooks.
- **Lesson for next batch:** test genuinely different ANGLES (different body/promise), not re-skins of one concept; lead hooks with the product mechanism/benefit; save curiosity-gap hooks for top-funnel view objectives, not cart. Nothing reads cleanly until the store converts.

#### 2026-10-26 — CORRECTION / data-quality (Nikita's steer): Shopify store funnel is POLLUTED
Nikita was browsing his own store + adding to cart during this window, so the Shopify store-side funnel (270 sessions, cart-adds, "11 reached checkout / 0 completed") is contaminated by owner traffic — NOT clean customer behaviour. **RETRACTED: the earlier "checkout is the leak / 0 of 11 completed" conclusion is not established** (that drop-off was likely Nikita's own testing). The 1 completed checkout ($64.95, "Sergey Granitsa") is a confirmed self/family test.
- **SOURCE OF TRUTH for this brand = Meta ad-ATTRIBUTED data only** (people who came from the ads). Pixel purchase attribution won't count Nikita's own direct visits.
- **Clean (Facebook-attributed) picture is thin:** 45 LPV → 6 ATC (13%) → 0 purchases. **6 carts → 0 sales is NOT enough data to diagnose checkout/CVR** (expect ~1 sale at 6 carts even when perfect). We do NOT have a measurable conversion problem yet — we have almost no data.
- **Implication:** can't optimise a CVR we can't measure. No checkout app / no cart app / no funnel rebuild — all premature. Real path: (1) spend enough for a real Facebook-attributed read, (2) THEN diagnose the actual drop-off. Nikita to exclude his own IP in Shopify admin so store analytics clean up for later cross-checks.
- **STORE CORRECTION:** earlier "half-built store" claim was from STALE copywriting build logs — I never viewed the live store. Nikita confirmed + showed screenshots: **store + checkout are FULLY BUILT and on-brand** (Shop Pay/PayPal/G Pay express, cards, trust line, ProudFold palette). Store is NOT the problem. (Checkout urgency/scarcity = NOT an option on Shopify Basic [needs Plus] and would violate ProudFold's anti-scam positioning — do not add.)

#### 2026-10-26 — Audience & placement breakdown (Meta-attributed) — THE REAL LEAK IS DELIVERY, not store/checkout
- **PLACEMENT (biggest lever):** **Facebook Feed A$34.98 → ALL 6 ATC (CTR 11.6%).** FB Reels A$34.59 → **0 ATC** (CPM A$157). IG feed+reels+stories ~A$22.9 → 0. FB Stories A$3.69 (CPM A$369). Audience Network + rest ~A$1.6 → 0. **~63% of budget (~A$62) went to non-Feed placements for 0 ATC.** Statics die in Reels/Stories/video placements (Advantage+ Placements spraying stills into video-first slots). → run statics on **FB Feed (+ maybe IG Feed) only**.
- **DEMOGRAPHICS:** **ALL 6 ATC = women; 0 from men.** Men got ~A$25 (25% of budget, incl. ~A$17 on 18–34 males) → 0 ATC = waste. Spend skewed **too OLD**: 65+ women ate **A$49 (50% of budget)**, CPM A$164, for 2 ATC (lots of clicks, low add-rate = curiosity/reading). Avatar = women **45–62**. Efficient buyer segments: 25–34F (A$0.84→2 ATC, 18.75% CTR) + 55–64F (A$16→2 ATC); core 45–54F under-served (A$5). → tighten to **women 45–64, exclude men, cap/down-weight 65+**.
- **Real vs curiosity ATC:** mixed but directionally real — all from women; core/younger women converted clicks→ATC efficiently (intent); 65+ = curiosity. Can pull `omni_initiated_checkout` (ad-attributed) to measure intent depth if needed.
- **Not chasing** period-over-period trend / industry benchmark (Ads MCP steering) — meaningless at 3 days / A$98.
- **ACTION (pending Nikita approval):** ad-set edits — (1) placement → Facebook Feed only; (2) audience → women 45–64, exclude men. Editing a live ad set pauses + re-enters learning; re-activate in same step. Settings fix, NOT a store rebuild.

#### 2026-10-26 — DIRECTION SET (Nikita's call) — supersedes the tightening proposal above
- **Audience tightening = DROPPED (Nikita, correctly).** Brand-new pixel (launched ~1 day ago, ~A$98 spent) is deep in LEARNING; the spread to men/65+/all placements is exploration, not a settings error. Tightening now raises CPM + starves learning. → **KEEP BROAD.** (Only structural bit = statics in Reels/Stories; video covers those placements — don't micro-manage.)
- **No funnel to 'fix':** store + checkout fully built & on-brand; no proven conversion problem (data too thin + was polluted). 'Fix funnel first' = waiting on a non-problem → skip.
- **DIRECTION = build creative VOLUME + DIVERSITY:** new ANGLES + VIDEO, not re-skins of the one advertorial. Both the pixel's data engine and the #1 lever. Pipeline: ad-scripting (TOF Google Doc V1–V10 video / S1–S11 image ready) → storyboarding → creation.
- **Learning-phase economics:** ATC-optimized ad set needs ~50 ATC/wk to EXIT learning ≈ **~A$800/wk at ~A$16/ATC**. Below that the pixel never stabilises → permanent erratic delivery (= the spread observed). Either budget to exit learning or expect noise. Don't split a small budget across many ads in one ABO set (Meta starves most — AD4 got 5 impr). Few concepts, enough budget each.
- **Open:** Nikita to give daily budget → economics to set exact per-concept test spend + hard kill/scale thresholds.

#### 2026-10-27 — LEAK LOCALIZED: checkout completion (not ad/audience). Meta-attributed, lifetime A$176.37
Full funnel (Meta): 1,648 impr → 107 link clicks → **93 LPV → 21 ATC (23%, A$8.40/ea) → 8 checkouts initiated (38%, A$22/ea) → 0 PURCHASE (0%).** ⚠️ Reality check: it's **A$8.40/ATC blended, not "A$2"**; 21 ATC is solid-not-crazy. Cheap ATCs that don't buy = cost, not win.
- **LEAK = IC→Purchase (0/8).** 8 real people reached the checkout page and none finished → leak is **checkout/offer**, NOT ad/creative/audience/curiosity.
- **Audience RULED OUT as cause:** country = **100% US** (all impr/ATC/IC). Not cheap-geo junk. Quality events from **FB Feed** (16/21 ATC, 6/8 IC, A$62); Audience Network A$5/0 ATC = not a junk-placement problem. Curiosity ruled out — 38% of ATC initiated checkout = real intent.
- **#1 SUSPECT = US shipping config.** Store country = Australia, sells USD, targets US. If US shipping rates aren't set / show broken/shock rate at the shipping step → buyers start checkout, hit shipping, bail = exactly this pattern. #2 = price/trust cold-feet at payment (new brand, no reviews). → **NEXT: read-only pull of Shopify shipping zones/rates + payment methods (config, not polluted behavioral data) to confirm.** Pending Nikita go.
- Daily: Oct25 A$29/0 ATC · Oct26 A$71/6 ATC/2 IC/0 purch · Oct27(today, derived) ~A$76/~15 ATC/~6 IC/0 purch. Cost/ATC falling as pixel learns; purchases still 0 every day.
- Caveat: 8 IC is still a smallish sample, but it's the clearest signal yet + agrees with Shopify's 0 real orders.

#### 2026-10-27 — Full live funnel audit (scraped proudfold.com) — PAGE IS NOT THE LEAK
Walked the whole live funnel. **Prior "half-built store" + "no reviews" guesses were WRONG — now actually inspected.** The page is strong: **312 reviews / 4.8★** w/ breakdown + named testimonials, **60-day keep-it guarantee** (×6), dedicated trust block (US-ship / no-sub / honest sourcing / secure checkout), clear mechanism, ingredient %s, 12-Q objection-killing FAQ, all payment methods, compliance held. **Landing page / offer / trust are NOT the conversion leak.**
- **REAL LEAK #1 (primary, ~structural):** campaign is **optimized for ADD-TO-CART**. Meta then finds the cheapest *adders*, not buyers → textbook "flood of cheap ATCs, 0 purchases." A$8/ATC isn't a bargain, it's Meta efficiently finding non-buyers. This is the main cause.
- **REAL LEAK #2 (offer friction):** PDP "Add to Cart" defaults to the **$64.95 3-pack** (most-popular pre-selected). $65 first order to an unknown brand, cold = steep first ask; $29.95 single is not the default.
- **#3 caveat:** 8 IC still thin — first sale could be near; don't rebuild.
- **FIX SEQUENCE (corrected):** you do NOT need a prior purchase to run a Purchase-optimised campaign — Meta allows Purchase optimisation on a 0-purchase pixel; it just delivers conservatively / "learning limited" until sales come in, but it hunts BUYERS from day one. So: (1) **launch a NEW ad set/campaign optimised for PURCHASE now** (can't flip the event on the existing live ATC ad set — must create new); stop running ATC (it trains the pixel on non-buyers). Only if Purchase won't spend at budget, bridge with **Initiate Checkout**, never ATC. (2) lower first-purchase barrier to land first sales faster — default/lead the **$29.95 single** + small (10–15%) first-order code. (3) keep volume growing; goal now = first sales + clean data, not peak efficiency. *(Supersedes the earlier "seed ATC then switch" note — that overstated the need to seed.)*
- Note: all store-side execution (offer default, discount code) = store-build/offer stations; optimisation-event switch = ads/Nikita. Economics owns the diagnosis + the seed-then-switch logic.

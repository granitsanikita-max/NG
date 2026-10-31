# PDP AUDIT — Unhidden (men's compression slimming tank)

> "Chief" QA pass of the product page against Nikita's fundamentals.
> Audited: 2026-10-31 · Branch `claude/funny-faraday-w0xo28`
> Sources: Notion "② Product Page (PDP)" (read in full) + "Reference — Funnel & Store Page Fundamentals"; repo `COPY.md`, `BRAND.md`, `brain/DOC2_CUSTOMER.md`, `brain/DOC3_PERSUASION.md`; visuals in `assets/`; built-state from this session's screenshots.
> **Live page NOT pulled:** the Unhidden PDP runs on a native Shopify theme ("Blocky"), not GemPages (the 4 connected GemPages shops are other brands). All live-only checks (button wiring, first-accordion-open, sticky bar, actual rendered order) are flagged **[VERIFY LIVE]**.

---

## ⚠️ HEADLINE: 4 existential compliance landmines (fix before a single ad runs)

BRAND.md: *"COMPLIANCE (EXISTENTIAL — a competitor page was already Meta-disabled)."* The page currently violates the brand's own rail in four places. Any one can get the page/ad account killed.

1. **Fabricated reviews & rating.** The page shows **"581 real men's reviews"** and **"Rated 4.8."** 581 is the number of *research snippet rows* in `DOC2_CUSTOMER.md` — **not customers**. The brand was created **2026-10-30** and has **zero real buyers**. COPY.md rail: *"No review counts/stars until real."* → The 581/4.8, the 8 named reviews (Keith/Mark/Reggie/…), and the mini-review strip are all **invented**.
2. **Fabricated statistics.** The "Numbers That Matter" block asserts **93% / 89% / 91%** "from 581 real men's reviews." Made-up stats presented as measured results = the highest-risk claim type.
3. **Sample-gated claims already depicted.** BRAND.md: *"⚠️ SAMPLE-PENDING — do NOT claim or depict until a physical sample is tested: long-cut 'stays below the belt', invisible-under-white/no-lines, strong compression, exact fabric %."* The page currently depicts **all of them**: `05_invisible.png` (invisible under white shirt), `ums/tab3_cutlong.png` (stays below belt), the before/afters + `13_four_way_stretch.png` (strong compression), "holds the gut flat all day under a dress shirt" (mini-review).
4. **Fake scarcity.** "Founding Run — first 500 kits · 83% SOLD." A brand-new store with no sales can't have sold 415 kits. PDP doc + Nikita's rule: *"No fake timers or fake stock. Urgency only when true."*

These are not "nice to have" fixes — they are the difference between launching and getting disabled. Everything below is secondary to these.

---

## 1. COPY CONSISTENCY

| Item | Found | Issue |
|---|---|---|
| Price | "$49.00" in ADD TO CART | No strikethrough/original, no $ or % savings, no per-day/per-unit (fails Fundamental 6). Offer is a "Kit" in COPY but page sells a flat $49 tank — **offer not reconciled**. |
| Sizes | Nav pill "S TO 5XL" + size chart S–5XL | **CONTRADICTION:** `DOC2_CUSTOMER.md` line 110 says *"ours stops at 3XL"*. BRAND.md says S–5XL. If the real CJ SKU stops at 3XL, "S–5XL" is a false availability claim and will drive wrong-size returns. **[VERIFY SKU]** |
| Colours | Colours slide "TWO STYLES. THREE COLOURS" (black/white/grey) | **CONTRADICTION:** BRAND.md says **5 colours (black/grey/navy/beige/white)**. Review photos also show a **blue-zone** style (Brian, Vince) not named on the colours slide. The variant story (how many styles, how many colours) is inconsistent across page, BRAND.md, and the review images. **Pick one truth and make every surface match.** |
| Review count | "581 real men's reviews" / "4.8" | Fabricated (see landmine 1). Also 581 appears as both "reviews" and is really research rows — pick a real number (0 at launch) or remove. |
| Guarantee | "60 days" / "60-Day No-Hassle Guarantee" | Consistent at 60 days across badge + block. ✅ (just ensure the ad + cart also say 60.) |
| Shipping | "Free shipping · Discreet plain packaging · Tracked worldwide delivery" | No delivery **timeframe** and no honest "ships from overseas" (see §7). "Tracked worldwide" hints at overseas but never states the 4–9 day CJPacket window. |
| Swap offer | "Wrong size? We swap it free — both ways." | Good and consistent with the sizing risk-reversal in DOC3. ✅ Keep. |
| Mechanism name | "Hold-It-Flat" (COPY) | **[VERIFY LIVE]** that the page uses the locked "hold it flat / holds a soft chest and belly flat" language and never "slims/shrinks/tightens skin." |

**Action:** lock a single source-of-truth spec block (price, sizes, colours/styles, guarantee, shipping window, review count) and make every section match it.

---

## 2. FUNDAMENTALS COVERAGE (vs Notion "② Product Page")

| # | Fundamental | On page? | Execution | Fix |
|---|---|---|---|---|
| F1 | Above the fold carries benefit + proof + price + buy path | **Yes** | Hero gallery + "Look Solid The Second It's On" + buy box + proof line all above fold | Strong structurally — but the proof line is fabricated (landmine 1). |
| F2 | Gallery sells on its own, claim burned on each image | **Yes (strong)** | 11+ story-stack slides, captions on images, infographic not angles | Best part of the page. Keep. |
| F3 | Trust before claim (rating at/above title) | **Weak** | Rating present but **fake**; [VERIFY LIVE] it sits above title on mobile | Replace with a *true* trust signal at launch (e.g. founder guarantee / "first run" framing) until real reviews exist. |
| F4 | Benefit beats name (name never alone) | **Yes** | Headlines are benefit-led ("Look solid the second it's on", "Walk in like you've got nothing to hide") | Strong. |
| F5 | Buy box effortless — numbered steps, tiles, sizing rule at selector | **Weak / [VERIFY LIVE]** | Not seeing numbered "1. Select… 2. Select…" steps or size/colour **tiles with descriptors**; size chart is a separate section not a rule at the selector | Add numbered steps, option tiles, and a one-line sizing rule *at the picker* ("Between sizes? Size up — swap free"). |
| F6 | Spell out the money, never make them do math | **Missing** | Only "$49" flat | Add was/now, $ + % saving, and a per-item price if the Kit is multi-unit. Reconcile with OFFER. |
| F7 | Biggest fear-reducer under button as a full sentence + 1 proof line | **Weak** | "Wrong size? We swap it free" + secure-checkout line; guarantee is lower | Put the biggest fear-reducer (the keep-it/refund guarantee) as a full sentence directly under ADD TO CART, plus one proof line. |
| F8 | Proof believable, visible, cast; faces match buyer | **Yes on form, fails on truth** | 8-review wall, faces match ICP (40–60 bigger men) ✅; but fabricated, and not every review is cast to a distinct objection | Faces/casting are right. Truth is the problem (landmine 1). |
| F9 | Only true claims; every number identical | **FAIL** | Fabricated reviews, stats, scarcity; sample-gated claims depicted | The core failure. See landmines. |
| F10 | Every section one job, belief order | **Yes** | Promise → proof → mechanism → comparison → guarantee → reviews → FAQ roughly follows blueprint | Good. Confirm order live. |
| F11 | Specific & visceral, fluid sentences | **Yes** | Copy is concrete and in-voice (stop-slop) | Strong. |
| F12 | Features + benefits + outcomes all present | **Yes** | Built-to-last (features) + benefits + "walk in" outcome | Good. |
| F13 | Visual hierarchy / one dominant CTA | **[VERIFY LIVE]** | — | Confirm one dominant CTA per screen. |
| F14 | Long is fine if every section earns scroll | **Yes** | Page is long and mostly earns it | Cut the video section (being removed) rather than ship a weak one. |

**Zone/Blueprint gaps (present elsewhere in the doc, missing or weak here):**
- **Offer / bundle ladder (Zone 5):** no quantity ladder, no bundle cards, no per-unit — OFFER.md is still an empty template. **Offer must be finalised before this page can convert.**
- **Delivery date (Zone 5/6):** no estimate shown (see §7).
- **Sticky buy bar (Zone 16):** not present (you asked how to add it). **Missing.**
- **Email capture for non-buyers (Zone 16):** likely missing — add after reviews.
- **Founder line / mission (Zone 15):** "The scale isn't the finish line — your shirt is" is the locked positioning but there's no signed founder note on the page. Add one short signed line.
- **First FAQ accordion open by default (Zone 14):** [VERIFY LIVE].
- **Full star distribution (Zone 13):** a perfect 4.8 with no distribution reads fake — moot until reviews are real.

---

## 3. VISUALS

Inventory: `carousel/01–15`, `reviews/01–08`, `ums/tab1–4`.

- **No two identical files reused** across sections. ✅
- **Format over-repetition (flag):** three different split-screen torso comparisons now exist — `02_before_after.png` (carousel), the Numbers-section before/after (new model), and `15_comparison.png` (generic-vs-Unhidden). Different people, same visual *beat*. Risk of "seen it already" fatigue. Keep the carousel before/after + the comparison; make sure the Numbers section leads with the **stats**, not a third near-identical before/after.
- **Model continuity:** the bearded model appears in `01_hero` and `02_before_after` (intentional brand model) — fine.
- **Placeholders still live [VERIFY LIVE]:** the **3 embedded mini-reviews under the hero buttons** were planned but **not yet made** (still cream "Intertrigo" tube placeholders in the last screenshots). The **video section** is being cut. Confirm no cream-tube placeholder survives anywhere.
- **Sample-gated depictions (compliance, not quality):** `05_invisible`, `ums/tab3_cutlong`, before/afters and `13_four_way_stretch` depict claims that must be sample-verified first (landmine 3).
- **Colour accuracy:** review images show a **blue-zone** variant that the colours slide doesn't name — align the visuals with the final colour/style list.

---

## 4. REVIEWS (human + compliance)

The 8 reviews **read genuinely human** — varied voice, specific, no obvious AI tells, and the faces match the ICP (older bigger men). Casting is decent (big-guy/4XL, sizing, invisible-under-shirt, returns).

Compliance / authenticity flags:
- **All fabricated** (landmine 1–2). Invented names + AI faces asserting results the product hasn't been sample-proven to deliver.
- **Sample-gated claims inside reviews:** "holds the gut flat all day, even under a dress shirt" (Dave R. mini), "didn't roll up over my stomach" (Reggie), the "under a white work shirt, no one notices" angle (Phil) — these assert long-cut/invisible/all-day hold that BRAND.md says must not be claimed pre-sample.
- **Weight-loss mention:** Mark D. "dropped a good amount of weight a couple years back" — the rail allows at most *one* inclusive nod to weight loss and bans weight-loss *claims*; as a customer backstory it's borderline-OK but watch it doesn't read as a weight-loss promise.

**Verdict:** voice is good; the problem is they're invented and lean on unproven claims. At minimum, soften any review that asserts a sample-gated capability until the sample is tested.

---

## 5. BUTTONS / CTAs  **[VERIFY LIVE — page not pullable]**

From the screenshots: only **2** real CTAs (top buy box + bottom) + a "Scroll to… Button 1–4" group you were wiring.

Must verify / fix on the live theme:
- [ ] Every ADD TO CART actually adds to cart / opens cart (not a dead anchor).
- [ ] The "See It In Action" / "See Result" hero buttons jump to the correct **deep** gallery slides (recommended: Result → before/after, In Action → four-way-stretch or "Built For Every Build").
- [ ] The "Scroll to… Button 1–4" anchors resolve to real section IDs.
- [ ] Add the missing CTAs: **sticky bar** (always-visible) + inline CTAs after Before/After, after Comparison, after Reviews, after Guarantee (per the CTA-ladder plan).
- [ ] FAQ accordions, size-chart link, and the mini-review carousel arrows all function.

---

## 6. (reserved — see ranked punch-list in §9)

---

## 7. PRODUCT-DETAIL COMPLETENESS

A buyer can't commit without these. Current state:

| Detail | On page? | Note / fix |
|---|---|---|
| **Shipping time** | **Missing** | Only "tracked worldwide." Real spec (BRAND.md): ships China, **1–3 day processing + 4–9 day CJPacket**. State an honest delivery window ("Arrives ~7–12 days, tracked") near the button. **Do NOT fake US stock** (competitor North Alpine's fake "ships from Ohio" is in the research as a trust-killer). |
| **"Ships from overseas" honesty** | **Missing** | Compliance expects honest origin. Frame positively ("ships direct from our maker, tracked the whole way") but don't hide it. |
| **Fabric / material composition** | **Missing** | PRODUCT.md is an empty template; exact **fibre %** is sample-gated (BRAND.md). You CAN describe it generically ("seamless knit, 4-way stretch, breathable") — which the page does — but the real composition must be confirmed from the CJ spec before any % is printed. Pull the CJ spec for SKU **CJYD323488814NM**; 180g weight is the only hard spec we have. |
| **Care / wash instructions** | **Missing** | None on page. Add simple care copy (machine wash cold, hang dry) — also supports the "holds shape wash after wash" claim, which is itself sample-gated. |
| **Sizing specifics** | **Weak/wrong** | Size chart is **weight-based** (S 50–69kg…). DOC3 §11 says the fix for the #2 objection is a **measured chart (height + chest + waist), not weight bands**, plus body-length-per-size in cm. The current weight chart actively *weakens* the sizing answer. Rebuild once the sample is measured. |
| **What's in the box / "the Kit"** | **Missing** | COPY references "the Kit" but the page never lists what a Kit contains. Define it (tank + size-swap card + ? ) or sell a single tank — and make price/offer match. |

---

## 8. OBJECTIONS COVERAGE (from `DOC2`/`DOC3`, ranked by snippet count)

| # | Objection (count) | Answered on page? | Where / strength | Fix |
|---|---|---|---|---|
| 1 | **Not strong enough / "just a tight tee"** (73, +36 scam = #1 cluster) | **Weak + risky** | Comparison section + four-way-stretch + before/afters *assert* strong compression, but it's **sample-gated** and fabricated. DOC3: this answer **fails if the CJ sample is light compression → don't launch on this SKU until tested.** | Get the sample. Film a real with/without + stretch-the-panel demo. Until then this #1 objection is unproven. |
| 2 | **Sizing wrong** (70) | **Weak** | Size chart (weight-based) + "swap free" | Replace weight chart with height+chest+waist measured chart + fit rule at the selector. Swap-free is good — keep it loud. |
| 3 | **Hard to put on** (40) | **Contradiction** | FAQ put-on line | DOC3 power-move: *"Step into it, don't pull it over your head."* Earlier this session the FAQ was flipped to **"pull it over your head"** — which **contradicts** the research AND the put-on-video concept. **[VERIFY LIVE]** and set it to step-in. Add the 20-sec put-on demo. |
| 4 | **Scam / ad lied** (36) | **Partial** | "We claim less" tone, swap offer, plain packaging | DOC3/Nikita: prove it by *what you DON'T claim* and real demos — never by saying "we're honest." The fabricated 581/4.8/stats do the **opposite** and actively trigger this objection. Remove them. |
| 5 | **Price** (33) | **Weak** | Flat $49 | Add savings math + per-item value; "swap free both ways" already lowers risk. |
| 6 | **Too tight / can't breathe** (26) | **Missing** | — | Add honest fit guidance ("snug not painful — can't breathe? size up, swap free"). Comfort is sample-gated (worn 8h). |
| 7 | **Refund / return hassle** (23) | **Yes** | 60-day guarantee + swap-both-ways | Strong — state money-back (not store credit) and who pays return postage in plain words. ✅ |
| 8 | **Durability** (20) | **Missing** | "holds shape wash after wash" (sample-gated claim) | Needs sample proof; add care copy. |
| 9 | **Rolls up / too short** (17 + 13 = 30; 36 long-torso needs) | **Risky** | UMS "cut long stays below the belt" | **Single biggest product risk** (DOC3). CJ body length unknown → **OPEN until the sample is measured.** Don't depict/claim long-cut until confirmed; print body-length-per-size when you can. |
| 10 | **Slow shipping (China)** (14) | **Missing** | — | State honest tracked delivery window (see §7). |

**Unhandled on the page today:** #6 too-tight/breathe, #8 durability, #10 shipping time — all **missing**. #1, #2, #3, #9 are present but **weak, contradicted, or sample-gated**.

---

## 9. RANKED FIX PUNCH-LIST (most → least conversion/risk impact)

**TIER 0 — Existential (do before any traffic):**
1. **Remove/replace fabricated social proof** — the "581 reviews", "4.8", and 93/89/91 stats. At launch, reframe as founder/first-run honesty ("We're new. Here's the deal and a 60-day no-risk promise") until real reviews exist.
2. **Get the physical sample and test it.** It gates the entire product-truth layer: real compression (#1), long-cut/rolls-up (#9), invisible-under-white, breathability, durability, fabric %. DOC3 is explicit: *if the sample is light compression or too short, do not launch on this SKU.*
3. **Pull every sample-gated claim/depiction** until the sample passes (invisible-under-white `05`, cut-long `tab3`, strong-compression demos, "holds all day").
4. **Kill fake scarcity** ("83% sold / first 500") unless you genuinely cap and track it.
5. **Resolve the S–5XL vs 3XL contradiction** and the 3-vs-5 colours/styles contradiction — one true spec everywhere.

**TIER 1 — Must-fix for conversion:**
6. **Finalise the offer** (OFFER.md is empty): price ladder / Kit contents / savings math, then make the buy box show $ + % savings and per-item price (F6).
7. **Fix sizing:** measured chart (height+chest+waist), fit rule at the selector, keep "swap free" loud (objection #2).
8. **Fix the put-on instruction** to "step in, don't pull over head" + add the demo (objection #3, and it contradicts itself right now).
9. **Add shipping/delivery honesty** — tracked window, origin framed honestly (§7, objection #10).
10. **Add the sticky buy bar + the 4 inline CTAs** (after before/after, comparison, reviews, guarantee).
11. **Number the buy-box steps, show option tiles with descriptors** (F5).

**TIER 2 — Strengthen:**
12. Make the 3 hero mini-review images (replace cream-tube placeholders).
13. Add care/wash copy and "what's in the box."
14. Add a signed founder line (Zone 15) + email capture for non-buyers (Zone 16).
15. Add honest fit guidance for too-tight/breathe (objection #6).
16. Reduce before/after format repetition (lead the Numbers section with stats, not a third split-torso).
17. Put the biggest fear-reducer as a full sentence directly under ADD TO CART (F7).

**TIER 3 — Verify on live theme:** button wiring, first-FAQ-open, one-dominant-CTA hierarchy, mechanism language never says "slim/shrink/tighten skin," review distribution.

---

### Bottom line
The **craft** is strong — gallery story-stack, benefit-led copy, comparison, guarantee, human-sounding reviews, ICP-matched faces. The page **fails on truth**: it leans on fabricated proof and depicts claims the product hasn't been sample-verified to deliver, which is the exact thing that got a competitor disabled. **Sample first, then swap invented proof for real.** Everything in Tier 1–3 is straightforward once Tier 0 is handled.

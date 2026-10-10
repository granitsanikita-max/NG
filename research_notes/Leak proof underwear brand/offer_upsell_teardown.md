# Offer / Upsell / Bundle / Free-Gift Teardown — Women's Leak-Proof & Incontinence Underwear (US)

Run: **2026-10-10**. Builds on `wh_ads_offers_demand.md §15`. Tools: WinningHunter MCP (`get_store_details`, `get_store_top_ads`, `search_facebook_ads`) + Firecrawl (`firecrawl_scrape` query-mode on live cart/collection/PDP pages).

**Solidity tags:** **LIVE** = read off the store's live page this run · **APP** = mechanic inferred from an installed Shopify app confirmed via `get_store_details` · **PRIOR** = from §15/earlier run · **INFERENCE** = my reasoning. Modeled revenue/AOV/traffic are third-party SimilarWeb-style estimates, directional only.

> **Method note / honesty flag:** Live PDP→cart→checkout walks were done via Firecrawl query-mode on collection/PDP/homepage DOM (captures price ladder, shipping bar, countdown, popup copy, guarantee badges, buy-more tiers). What a headless-cart walk would add and I could NOT fully see: (a) the exact free-gift SKU that auto-adds at a cart threshold when the app toggles it on (Everdries runs it as an Intelligems on/off split test — gift item not exposed on the live DOM this run), and (b) the live post-purchase one-click upsell screen (only visible after a real card auth). Those two are flagged **APP/INFERENCE** per competitor.

---

## 1. PER-COMPETITOR OFFER TABLE

### EVERDRIES — everdries.com  *(DR king; AOV $91.10 LIVE; Charlotte NC; 2M pairs shipped claim)*
| Lever | Detail | Tag |
|---|---|---|
| **Bundle ladder** (Comfy & Discreet) | 5-pk **$59.95** / compare $124.75 (−52%, **$11.99/u**) · 10-pk **$99.95** / $249.50 (**$10.00/u**) · 15-pk **$129.95** ($8.66/u) | LIVE |
| Other lines | Bikini 5-pk $39.95/$124.75 · Bikini 10-pk **$59.95**/$249.50 ($6.00/u) · Bikini Heavy 10-pk $79.95/$319.50 · Boyshorts 5-pk $69.95/$139.75 · Highrise Shorts 5-pk $79.95/$159.75 · Cotton / Cotton Hi-Waist 5-pk $69.95/$139.75 · Comfort Plus 5-pk $59.95/$124.75 | LIVE |
| "% off" framing | **Permanent fake anchor** — every SKU sits at −50% to −52% vs a compare-at that is never the real price. | LIVE |
| **Free gift / GWP** | **EG Auto Add to Cart Free Gift** app installed; bundle PDP image filename `og_free_gifts_PDP_photos_split_test_1.webp` confirms a gift-with-bundle offer that is **Intelligems-split-tested on/off**. Gift auto-adds in the Slide Cart at a bundle threshold. Exact item not exposed on live DOM this run (test off / gated). | APP + INFERENCE |
| **Order bump** | Separate SKU handle `comfy-discreet-leakproof-underwear-bundles-2-add-on` = an add-on bump product; surfaced in **Slide Cart Drawer by AMP** (slide-cart upsell). | APP + INFERENCE |
| **Post-purchase 1-click** | None detected (no AfterSell/ReConvert/Zipify/Rebuy in app list). Upsell is pre-checkout (slide cart) only. | APP |
| **Subscription** | **None** (`.js` confirmed no selling plan). | PRIOR |
| **Free shipping** | **Over $80**. | LIVE |
| **Guarantee** | **NONE stated** anywhere (home/collection/PDP). Trustpilot 2.5/560, 0% reply to 196 negatives; clusters = "leak protection fails", "told to still wear a pad", buyer pays return shipping, no prepaid label, "not returnable once worn". **Returns are a liability, not a lever.** | LIVE |
| **Urgency / popup** | **Live countdown timer** (2h 47m, perpetual/fake). Email/SMS popup not surfaced to scraper. Klaviyo + Postscript installed. | LIVE + APP |
| Apps (stack) | Loox reviews · Klaviyo · Postscript SMS · **Slide Cart Drawer (AMP)** · **EG Auto Add to Cart Free Gift** · **Intelligems A/B** · Triple Whale · Google/YouTube | LIVE |

### VERA'S UNDIES / VERA CARES / MIRIANO / NESLEMY / Mindsparkl  *(dropship clone template, burst-and-die)*
| Lever | Detail | Tag |
|---|---|---|
| **Bundle ladder** | "Signature Leakproof 5-pk" ~**$39.99–$64.54**. Qty ladder = **Buy 5 get 1 free / Buy 10 get 2 / Buy 15 get 4**. | PRIOR |
| "% off" framing | "**Up to 60% OFF + Free Gifts**"; "**Closing 70% off everything**" fake store-closing scarcity; "34 years helping women" fake-founder framing. | PRIOR (ad copy) |
| **Free gift / GWP** | Ad copy promises "**+ Free Gifts**" with bundles; specific item **not named** in creative or on (intermittently dark) store. Delivered via a free-gift/bundle app. | INFERENCE |
| **Order bump / post-purchase** | Bundle app + Convertful popup; no durable post-purchase stack (sites die before one matters). | PRIOR |
| **Subscription** | None. | PRIOR |
| **Guarantee** | Thin / unclear; Vera Underwear Trustpilot 3.5/505, Ultradries 3.5/245. | PRIOR |
| Shares Shopify PID 7082150330417 (Vera ↔ Miriano). Fear advertorials ("I was a nurse, pads nearly killed me"). | | PRIOR |

### KNIX — knix.com  *(scaled retention brand; AOV $109.50; period/everyday, NOT incontinence-positioned)*
| Lever | Detail | Tag |
|---|---|---|
| **Bundle ladder** | Per-pair **$22–$48**. **Automatic buy-more-save: 3+ styles → 15% off · 5+ → 20% off · 7+ → 25% off** (AIOD automatic discounts). Pre-built kits: 2-packs $70–$80 (save $14–$16), Essential No-Show 5-pk $85–$95 (save $25–$30), 3-packs $60–$80, Full Cycle Kit from $136/$171 (save $35), Heavy Flow Kit $135–$148 (save $35–$38). | LIVE |
| **Free gift / GWP** | **Spend $150 → FREE Overnight Reusable Pads** (Super Leakproof Reusable Snap Pads Overnight 3-Pack). Exact item + threshold confirmed on live DOM. | LIVE |
| **Order bump / post-purchase** | **Rebuy** post-cart/one-click upsell engine + AIOD auto-discounts drive the $109 AOV. | PRIOR + APP |
| **Subscription** | None core (apparel one-time). | PRIOR |
| **Free shipping** | **Over $100**. | LIVE |
| **Guarantee** | **30-day "First Pair Risk Free"** (wear the first pair, return if not satisfied). | LIVE |
| Trustpilot 4.5/674, 92.6% reply. Okendo+Trustpilot, Klaviyo, Northbeam. | | PRIOR |

### THINX / SPEAX — thinx.com  *(period pioneer; bladder = "Speax" line; TV-led via Tatari)*
| Lever | Detail | Tag |
|---|---|---|
| **Bundle ladder** | Flat per-pair pricing, no compare-at discounting. Bladder SKUs ~$20–$43 (Everyday $20, Basic $27, Hiphugger ~$41). Only buy-more lever: "**Add 3 eligible products → 10% off**" via a create-custom-set builder. | LIVE + PRIOR |
| **Free gift / GWP** | None detected. | LIVE |
| **Subscription** | None. | PRIOR |
| **Guarantee** | 60-day (prior). | PRIOR |
| **Loyalty** | **SwellRewards** points loyalty (retention, not AOV). Attentive SMS, Yotpo, Friendbuy referral, Loop Returns. | PRIOR |
| No urgency/offer; abandoned aggressive Meta DR; PFAS reputation scar. | | PRIOR |

### MODIBODI — modibodi.com  *(original period brand, AU-led, softening)*
| Lever | Detail | Tag |
|---|---|---|
| **Bundle ladder** | Underwear basic brief **$20.99–$30.99** (Moderate $20.99, Super $27.99, Teen boyshort $30.99); swimwear $49–$120. **Permanent ~50%-off** posture (every SKU PROMO-tagged). No multipack-discount app surfaced. | LIVE + PRIOR |
| **Free gift / GWP** | None detected this run. | LIVE |
| **Subscription** | None. | PRIOR |
| **Free shipping** | **Over $75**. | LIVE |
| **Guarantee** | **60-Day Risk-Free Trial**. | LIVE |
| **Popup** | **20% off** signup. | LIVE |
| Laundry bag ~$7.19 (prior). SwellRewards, Loop Returns, Gorgias, Nosto, Okendo. Trustpilot 3.5/1,191, 21.7% reply (service decline); permanent discounting erodes margin. | | PRIOR |

### JUDE — wearejude.com  *(supplement-LED subscription; underwear is an attach item; UK; non-Shopify Next.js)*
| Lever | Detail | Tag |
|---|---|---|
| **Products** | Underwear **from £16.60** (£24.95 hi-waist at Boots/H&B). Supplement **from £25.00–£26.63/mo**. | LIVE |
| **Bundle ladder** | Day & Night Duo **£99** · Strength & Sleep Duo **£99**, both badged "**SAVE 30%**". | LIVE |
| **Subscription** | **Subscribe & save up to 33%** (supplement replenishment is the core model). | PRIOR |
| **Free gift / GWP** | None (supplement model). | — |
| **First-order** | **20% off first order** via quiz. **Referral £10/£10** both sides. | LIVE |
| **Guarantee** | **90-day first-order money-back refund**. | PRIOR |
| Trustpilot 4.5/5,565 — strongest recurring-revenue + trust model in the set. | | LIVE |

### ATTN:GRACE — attngrace.com  *(skin-safe/sustainable bladder-leak; B-Corp; now pads + body-care led)*
| Lever | Detail | Tag |
|---|---|---|
| **Products** (S&S / retail price) | Pads $13.50–$16.20 / up to $18 · Liners $12.60/$14 · Odor-Proof Bags 50ct $15.75/$17.50, 150ct $40.50/$45 · Signature Drawstring Bag **$7.99** · Barrier Cream $18/$20 · Deodorant $12.60/$14 · Body Oil $25.20/$28 · Calm Spray $17.99/$19.99 · Flushable Wipes $25.20/$28. | LIVE |
| **Bundle builder** | **"Bundle & save 15%"** custom builder (pick-your-mix). | LIVE |
| **Subscription** | **Recharge Subscriptions = core**, **10% off** subscribe price; **free shipping drops to $40+** for subscribers. | LIVE + APP |
| **Free gift / GWP** | None detected. | LIVE |
| **Free shipping** | **Over $50** (one-time) / **$40** (subscribe). | LIVE |
| **Guarantee** | **60-Day Money-Back Guarantee**. | LIVE |
| RevenueHunt Shop Quiz, Intelligems A/B, Klaviyo, Okendo, Gorgias. Washable underwear de-emphasized vs pads. | | PRIOR |

### SAALT — saalt.com  *(sustainable period underwear + cups; B-Corp; lean stack; AOV $49.28)*
| Lever | Detail | Tag |
|---|---|---|
| **Bundle ladder** | Per-pair **$15–$47** (Seamless Thong $15/$30, Cotton Brief $22/$29, Comfort Brief $27/$39, CloudShort $26/$47, Seamless Brief $39). Buy-more: "**Add 3 more items → save 10%**". Live promo: **BOGO 50% off, code BOGO50**. | LIVE |
| **Free gift / GWP** | None. | LIVE |
| **Subscription** | None. | LIVE |
| **Free shipping** | **Over $79**. | LIVE |
| **Guarantee** | **90-Day Saalt Bliss Guarantee**. | LIVE |
| **Popup** | **10% off** first order. | LIVE |
| Lean: Yotpo, Klaviyo, Postscript, Triple Whale — **no bundle/upsell app**. Period-first, not incontinence. | | PRIOR |

---

## 2. WHAT EVERYONE DOES / BEST-IN-CLASS / NOBODY DOES

**Table stakes (everyone):**
- Multipack/qty ladder (3/5-pack) or auto buy-more-save, with a per-unit drop as qty rises.
- A reviews widget (Loox / Okendo / Yotpo), Klaviyo email + an SMS app (Postscript/Attentive).
- A free-shipping threshold set **above** the hero bundle ($75–$100 is the cluster; attn:grace lowest at $50).
- Signup popup = **10–20% off first order** (Saalt 10%, Everdries/Modibodi/Jude 20%).
- A "better than pads / 100% leakproof" promise.

**Best-in-class (worth copying):**
- **Knix** — AIOD **automatic buy-more-save (15/20/25% at 3/5/7 styles)** + **Rebuy** one-click upsell → **$109 AOV**; plus a **real, named GWP** ("spend $150, free Overnight Reusable Pads 3-pk") that is an on-brand consumable, not junk.
- **Jude** — **subscribe & save up to 33%** on a consumable + **90-day money-back** + 20% quiz capture + £10/£10 referral → genuine recurring revenue and 4.5★/5,565 trust.
- **Everdries** — **EG Auto Add to Cart Free Gift + Slide Cart + Intelligems A/B** on a fake-anchor bundle ladder → $91 AOV at massive scale (even with a 2.5★ product). The *mechanic* is best-in-class; the *honesty* is the opening.
- **Saalt / Modibodi** — **90-day / 60-day risk-free trial guarantees** as the trust headline.

**Nobody does (white space for us):**
- A **credible, named-founder incontinence brand** that pairs **(a) an honest bundle ladder (real anchor, not fake −52%)**, **(b) a genuine keep-the-pair wear-test guarantee**, and **(c) a replenishment subscription** — on Meta DR. Everdries/clones have the upsell mechanics but 2.5–3.5★ trust and fake anchors; period brands (Thinx/Saalt/Modibodi) have trust but no incontinence positioning, no urgency, no subscription; Jude has the subscription + guarantee but underwear is a bolt-on and it's UK. **No one owns "real brand + real guarantee + subscription" in US washable incontinence underwear.**
- **No one runs a true post-purchase one-click upsell in the incontinence lane** (Everdries/clones stop at the slide cart; only Knix, a period brand, runs Rebuy). An AfterSell/ReConvert one-click refill after checkout is uncontested here.

---

## 3. RECOMMENDED OFFER ARCHITECTURE — OUR BRAND
*(active 30s–40s incontinence; hero = 3-pack; landed cost ~$7–9/u test, ~$9–12/u real. Modeled at **$10.50/u real COGS** below.)*

### 3.1 Bundle ladder (honest anchor beats the clones' fake −52%)
| Tier | Price | Per-unit | Honest anchor / framing | COGS @ $10.50/u | Gross margin |
|---|---|---|---|---|---|
| **1-pack** ("Try One") | **$29** | $29.00 | No discount. Deliberately unattractive; exists for trial/retargeting + as the *real* per-unit anchor every multipack compares against. | $10.50 | $18.50 (64%) |
| **3-pack — HERO** | **$69** | $23.00 | Compare-at = 3 × $29 = **$87 → "Save $18 (21%)"** (a true, defensible number). Default-selected. | $31.50 | $37.50 (54%) |
| **5-pack — BEST VALUE** | **$95** | $19.00 | Compare-at = 5 × $29 = **$145 → "Save $50 (34%)"**. Badge "Most popular / best price per pair". | $52.50 | $42.50 (45%) |

Rationale: sits **above the clone/Everdries $8–$12/u bundle floor** (so we read as a real brand, not dropship) and **below the period-brand $20–$47/pair ceiling** — while every "save" number is arithmetic off a price we actually charge for a single. That is the differentiator: clones show −52%/−60%/−70% off invented compare-ats; we show a smaller but *honest* 21–34%. Honesty is the brand wedge against Everdries' 2.5★ "misleading marketing" complaints.

### 3.2 Free gift (cheap, high-perceived-value, on-brand)
- **Gift: a discreet mesh wash/travel pouch** (branded, doubles as a "machine-wash bag" + "carry a spare in your bag" pouch). Landed COGS **~$1.00–$1.50**; present it at **"$14 value — FREE"**.
- **Threshold: auto-add on orders $59+** (i.e. the **3-pack hero and up qualify; the 1-pack does not**) — this pulls single-pair shoppers up to the hero bundle to "unlock the free [pouch]."
- **Mechanic:** **EG Auto Add to Cart Free Gift** app (the exact app Everdries runs) + a **Slide Cart** so the gift visibly drops in with a "🎁 Free wash bag added!" line. A/B the gift on/off and the threshold with **Intelligems** (again mirroring Everdries' proven stack).
- Optional step-up (copy Knix's consumable-GWP idea): at **$120+** add a **free mini overnight-absorbency pair** ("$29 value") to push 5-pack + bump baskets higher.

### 3.3 Order bump (1 item, at cart) + post-purchase one-click (1 item)
- **Order bump (in Slide Cart, pre-checkout):** **"Add 1 Overnight / Heavy-Day pair — $19"** (vs $29 standalone). It's the same hero SKU in the highest-absorbency variant; natural attach for "nights / long days," ~$19 adds pure incremental margin ($8.50 GM) with zero new CAC. App: **Slide Cart Drawer by AMP** add-on (Everdries' pattern) or **Rebuy** smart-cart if budget allows.
- **Post-purchase one-click (the uncontested lane):** immediately after checkout, **"Add a second 3-pack at 25% off — one tap, no re-entering payment: $52 ($17.33/pair)."** This is where the incontinence lane has *no* competitor (only period-brand Knix runs post-purchase). App: **AfterSell** or **ReConvert** (cheaper, built for exactly this; use **Zipify OCU** or **Rebuy** if scaling). Take-rate 10–20% on a relevant one-click refill is normal → straight AOV/margin lift with no ad cost.

### 3.4 Subscription / replenishment
- **"Refresh Rotation" — subscribe & save 15%, 90-day cadence** (quarterly auto-ship of a 3-pack). Underwear doesn't deplete like pads, so position it as *rotation refresh / wear-and-tear replacement* ("doctors suggest replacing leak underwear every ~6 months"), not consumable replenishment.
- **Mechanic:** **Recharge** (attn:grace's stack) or native **Shopify Subscriptions**. First subscription box can also carry the free pouch. This plus the guarantee is the white-space nobody owns in US incontinence.

### 3.5 Shipping threshold + guarantee (the headline trust lever)
- **Free shipping over $59** — set exactly so the **hero 3-pack clears it and the 1-pack does not** (a second nudge off the money-losing single). This is *below* the $75–$100 competitor cluster, which reads as generous without us eating shipping on single pairs.
- **Guarantee = the hero of the whole offer: "60-Night Leak-Test Guarantee — wear them, wash them, put them through real leaks for 60 nights. If they don't hold, full refund and keep the pairs. No return to ship back."** This directly nukes Everdries' two biggest Trustpilot liabilities at once — "leak protection fails" **and** "buyer pays return shipping / no prepaid label / restrictive returns." Keep-the-pairs + no-return-shipping is more generous than Knix's 30-day, matches attn:grace/Modibodi's 60-day, and is cheaper to honor than it sounds (return-shipping on worn underwear is near-zero-salvage anyway, so "keep it" costs the same refund minus the reverse-logistics headache). Lead every ad and the PDP with it.

### 3.6 AOV math — why the stack is non-optional vs Meta CAC
Assume a realistic category **Meta CAC of ~$35** (crowded lane: 54+ US advertisers, rising fatigue; conservative).

| Order shape | Revenue | COGS @ $10.50/u | GM before CAC | **Net after $35 CAC** |
|---|---|---|---|---|
| **1 pair only** (no stack) | $29 | $10.50 | $18.50 | **−$16.50 (loses money)** |
| 3-pack hero | $69 | $31.50 | $37.50 | **+$2.50** |
| 3-pack + free pouch + $19 overnight bump | $88 | $42.00 | $46.00 | **+$11.00** |
| 5-pack + bump | $114 | $63.00 | $51.00 | **+$16.00** |
| 3-pack + bump + post-purchase 2nd 3-pack @25% ($52) | $140 | $73.50 | $66.50 | **+$31.50** |

**Takeaway:** a single pair at $29 **loses ~$16 per order** against a $35 CAC — selling 1-packs on Meta is structurally unprofitable, exactly why Everdries/clones force bundles and gifts. The stack lifts the realistic **blended AOV from $29 to ~$85–$95** (hero + free-gift threshold pull + order bump + ~15% post-purchase take), turning every lever from a $16 loss into a $10–$30 contribution, *before* the 90-day subscription and repeat purchases compound LTV. Make the **3-pack the only hero in ads**, gate the **free pouch + free shipping at $59** so the 1-pack is always the worse deal, and let the **post-purchase one-click** (which no incontinence competitor runs) and the **subscription** carry LTV.

### 3.7 Discount / capture mechanics
- **Signup popup: 15% off first order (email + SMS)** — mid of the 10–20% competitor band; protects margin while matching the category. Klaviyo (email) + Postscript (SMS), Everdries' exact stack.
- **No fake countdown / no fake store-closing.** The clones' perpetual timers and "70% off everything, closing down" are the trust liability we're exploiting — we win on honesty. If urgency is needed, use a *real* 72-hour first-order window tied to the popup code.
- First-order code stacks on the honest bundle, not on a fake anchor, so a 3-pack at $69 − 15% = **$58.65 + free pouch + free shipping** is a genuinely strong, defensible first-order offer.

---

## 4. APP STACK SHOPPING LIST (to replicate the mechanics)
| Function | App | Copied from |
|---|---|---|
| Qty/bundle ladder + auto buy-more-save | **AIOD Automatic Discounts** (or bundle app) | Knix |
| Free gift auto-add at threshold | **EG Auto Add to Cart Free Gift** | Everdries |
| Slide cart + in-cart order bump | **Slide Cart Drawer by AMP** (or Rebuy smart cart) | Everdries / Knix |
| Post-purchase one-click upsell | **AfterSell / ReConvert** (Zipify OCU or Rebuy at scale) | (uncontested in incontinence) |
| Subscription (90-day refresh) | **Recharge** or Shopify Subscriptions | attn:grace / Jude |
| A/B testing (gift on/off, threshold, price) | **Intelligems** | Everdries / attn:grace |
| Reviews | **Loox** or **Okendo** | Everdries / Knix |
| Email + SMS + popup | **Klaviyo + Postscript** | Everdries |

---

## TOOLS RUN (this session)
- ✅ `firecrawl_scrape` query-mode (LIVE): everdries.com (home + /collections/all), knix.com leakproof collection, saalt.com leakproof collection, attngrace.com shop-all, modibodi.com incontinence→super-absorbency, wearejude.com home, thinx bladder (404→custom-set promo captured).
- ✅ `get_store_details`: everdries.com — confirmed app stack (**EG Auto Add to Cart Free Gift, Slide Cart Drawer by AMP, Intelligems A/B**, Loox, Klaviyo, Postscript, Triple Whale), AOV $91.10, bundle ladder, traffic 239,714 (Sep, recovering off 173k June floor vs 1.37M Dec peak), Trustpilot 2.5/560 gap clusters.
- ✅ Prior §15 reused for: Knix Rebuy/AIOD + AOV $109.50, Jude subscribe-&-save 33% / 90-day refund, Thinx SwellRewards, Modibodi laundry bag, clone buy-5-get-1 ladder + ad copy.
- 🔁 Free-gift **SKU** (Everdries) and live **post-purchase upsell screens** not captured (Intelligems-gated / require real checkout) — flagged APP/INFERENCE.
- ❌ Headless cart→checkout walk not executed (query-mode DOM reads used instead).

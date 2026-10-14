# Leapproof: first campaign plan (Step 3 output → brief for Step 4)

> **Creative superseded 2026-10-13.** §1 (the 15-ad batch) is replaced by `first-campaign/FIRST_CAMPAIGN_CREATIVE_PLAN.md` (Google Doc: "Leapproof · First Campaign: Formats, Angles & Hooks"). The new plan is all top of funnel. It covers:
> - Avatar: the Pad-and-Liner Mom, problem-aware.
> - Angles A1/A2/A3, all landing on the live hero.
> - Video (top of funnel): V1 liner + VO, V2 AI talking liner (3D animation), V3 Pixar-style AI story of the moment. Chosen as the top COLD formats, modelled on UltraDries (the brand still acquiring customers), not Everdries' spend (mostly warm). A-vs-B comparison and silent on-body are proven but warm → moved to retargeting; see `first-campaign/FIRST_CAMPAIGN_SUMMARY.html` §6 for their reference ads. `research/format_scoreboard.json` holds the normalised ranks.
> - Statics: S1 long-form liner photo, S4 text cards.
> - Per ad: a Miro visual hook, hooks, and 3 proven references per format.
>
> §0 (tracking blockers), §2–3 (ATC warm-up → purchase ABO, budgets, break-even) and §4 still apply.

Built only from what's proven in `AD_RESEARCH.md`, with no 70/20/10 swings. Every concept below names the live winner it copies.
Numbers come from `funnel/NUMBER_SHEET.md` (USD sets $45 / $59 / $99) and your Step 5 benchmarks:
- CPM ~$28–30
- link CTR 2–3%
- add-to-cart ~10%
- cart→buy 25%
- learning phase 3–4 days
- don't judge before ~2× product price

## 0. Before a cent is spent (these block launch)

1. **Remap AddToCart in Funnelish.**
   - By default, Funnelish's Meta Pixel app fires **Lead + AddToCart when someone opts in** (an email is entered), not when she picks a set.
   - An ATC campaign on the default setting would optimise for email submits.
   - Fix: Funnel → **Apps → Meta Pixel → customise events** → AddToCart = the product page's set button click (or the checkout page visit).
   - Keep Lead on the quiz opt-in. InitiateCheckout (payment entry) and Purchase stay on their defaults.
2. **Pixel + Conversions API.**
   - Paste the Pixel ID and a CAPI access token into the same app.
   - Use one pixel across Funnelish and Shopify.
   - Check in Events Manager → Test Events (with ad blockers off) and run one Stripe **test-mode** purchase so Purchase lands with its value.
3. **Health & wellness check.**
   - Meta restricts data from domains it classes as health-related.
   - At the "mid" level it **blocks AddToCart/Purchase optimisation entirely**.
   - Open Events Manager → your dataset and look for a restriction notice on the domain.
   - If there is one, stop and tell me: the campaign gets re-planned.
   - To stay clear of it:
     - no "incontinence" or medical words in Funnelish product names, page URLs or event data;
     - quiz answers stay in the opaque code (FUNNEL_PLAN §7).
4. **Domain (recommended).**
   - Ads currently go to `leapproof.myfunnelish.com` (a shared domain).
   - Connect a subdomain such as `go.leapproof.com` in Funnelish and verify `leapproof.com` in Business Manager.
5. **Exclusions (Step 5, Rule 0):**
   - purchasers (180 days, from the Purchase event);
   - you and your team;
   - Audience Network off.
6. **Samples in hand** for the 2 filmed video concepts (V1, V2). Everything else can be built now from the product-accurate images we already have.

## 1. The creative batch: 15 ads = 9 video + 6 static

**Why 60/40:**
- Everdries' live library is ~91% video, and ~65% of the top-30-by-impressions creatives across both winners are video.
- Statics still take UltraDries' #1 and #2 slots and Everdries' #1 image.
- We go 60/40 for launch because statics can be made now; videos need the product on bodies.

Every ad links to the landing page with its `?a=` angle code (FUNNEL_PLAN §6). Copy gets written in Step 4 from these directions. Hook lines here are directions, not final copy.

First-person lines (V1-h3, V2-h2, V2-h3) only go out in the mouth of a real person who actually did it: a tester or creator, disclosed. Otherwise use the hands-only / brand-voice version of the same hook.

### Video: 3 concepts × 3 hooks = 9

| ID | Concept (format × angle) | Copies these live winners | Hook directions (all pass the "you" rule) | `a=` | Awareness / stage | Needs |
|---|---|---|---|---|---|---|
| **V1** | **Pad vs Leapproof side-by-side** (A-vs-B UGC × replace pads) | Carol 1629603918494594 (275d, **#1 on page**), Everdries 1577194033627020 (275d), 1920176635259424 (250d), 811197242009709 (230d), "mom vs me" 4313776562168091 (243d). ~260–420 live variants. | h1 hands only: a pad and a liner vs the brief on the bed, finger pointing: "Pad vs Leapproof. What's the difference?" · h2 on body: "Here's a pad under leggings… and here's Leapproof." · h3: "What I used to wear to the gym vs what I wear now." | `m` | problem→solution / TOF | samples; h2–h3 need 1 woman 30–45 |
| **V2** | **"Just launched" reveal** (voiceover over b-roll × new/launch) | 1812439156098880 (231d, 7 dupes, video #3), 2394499821001286 (263d, "just got dropped off at my front door"), 1367572708560789 (130d, "So I just did something a little crazy"). "new design" ~420 live. | h1: "Leak-proof underwear that looks like plain black briefs just launched 🤯" · h2: "These just landed on my doorstep." · h3: "So I just did something a little crazy… I bought 10 pairs of underwear." | `m` | solution / TOF | samples, hands + on-body cuts, VO |
| **V3** | **"Why are we still using pads?"** (problem-object open × pads are the wrong tool) | 1206351388295667 (275d, 6 dupes, video #14), 1887889898483490 (275d), AI talking pad 1700150534480418 (208d) and 1400650075258672 (#4 on its page). "pads" ~190 live. | h1 POV: a pad stuck in underwear + 🤢, "It's 2026. Why are we still sticking pads in our underwear?" · h2 AI talking pad: "I'm a pad. I bunch, I shift, and I go in the bin every day." · h3: "The sneeze hits mid-squat. The pad slides. Again." | `n` | problem / TOF | no samples for the hook; product b-roll from our images or footage |

### Static: 3 concepts × 2 = 6

| ID | Concept | Copies these live winners | Variants | `a=` | Needs |
|---|---|---|---|---|---|
| **S1** | **Long-form native story**: ugly phone photo plus a long caption (your Notion "Native MSL" structure) | UltraDries **#1 and #2 images by impressions** (1271768424869385, 3241631309352492, 209d), Everdries postpartum 883503151225665 (245d) | v1: a pad on a gym floor / in a gym bag + "Every woman who leaks at the gym gets told the same thing: wear a pad. Here's what nobody tells her…" · v2 postpartum: a pad box in the change bag + the "it's just normal after kids" story | `n` / `p` | **brand voice** (no fake persona) or a real tester's story |
| **S2** | **Native on-body photo** + plain caption | 3899002186909593 (231d), 955109570520004 (221d), Carol 1646147329768369 (152d) | v1: back view (lp-back-B) · v2: under leggings (lp-leggings-A). Caption: "They look like plain black briefs. That's the point." | `m` | existing images |
| **S3** | **Product collage + offer** | **Everdries #1 image by impressions**, 1259007659608370 (275d, 2 dupes) | v1: 5-panel collage (flat lay, lining, pack, stack, on body) + "10 pairs · $99 · $9.90 a pair · free Wash Bag + Wash Sheets · 30-Night Leak-Test" · v2: "5 pairs · $59 · free Wash Bag · 30-Night Leak-Test" (the 5-pair set gets the Wash Bag only) | `m` | existing images. **No sale, no timer.** |

### Held back (proven, but each needs something we don't have yet)

- **F5 "Don't buy X tomorrow" / "Don't get the 3-pack" offer video.** #1 Everdries video by impressions (2033165163976432, 323d), and 3917176148585428 (162d). Goes to **retargeting** once there are ~1,000 landing visitors: "Don't get the 3-pack. The 10 is $9.90 a pair and comes with both free gifts." Honest offer only.
- **Skeptic UGC testimonial** ("I thought they were too thin to hold anything…"). The ~210 "I was skeptical" variants and 886997533759184 (334d, oldest live ad). Needs real Founding 30 testers, disclosed.
- **Expert explainer.** UltraDries runs 6 of its top-30 videos this way. Needs a real, named pelvic PT.
- **Tips listicle static**, "Leaking at the gym: 5 things that help". Carol 887125520881386, #1 on page, 249d. Next batch, once a PT checks the tips.

## 2. Phase 1: AddToCart warm-up (Days 1–3)

**My call: take your option 2.** Run a normal ABO, optimised for AddToCart, not a one-off warm-up campaign. It costs the same, but the ad sets you build are the ones you keep.

| Setting | Value |
|---|---|
| Campaign | `LP \| WARMUP \| ATC \| ABO \| US`. Objective: Sales. Conversion event: **AddToCart (remapped)**. 7-day click / 1-day view. |
| Ad sets (2 × $15/day = **$30/day**, 3 days = **$90**) | `VIDEO \| m+n \| US W28-50 broad`: V1-h1, V2-h1, V3-h1. `STATIC \| m+n \| US W28-50 broad`: S1-v1, S2-v1, S3-v1. |
| Audience | US, women, 28–50, English, no interests. Advantage+ audience **off** for these 3 days so the age fence holds. |
| Placements | Advantage+ placements, minus Audience Network |
| Ad names | `concept \| angle \| format \| audience`, e.g. `V1-padvs \| m \| ugc-compare \| W28-50 \| h1` |
| URL | `…/LP?a=m&utm_source=meta&utm_campaign={{campaign.name}}&utm_content={{ad.name}}` |
| If samples aren't in yet | Run it with S1–S3 + V3 (no samples needed). Add V1/V2 in Phase 2. |

**What to expect, straight:**
- At your benchmarks, $30/day buys ~20–30 link clicks a day.
- At ~10% add-to-cart that's **~2–3 ATCs a day, ~6–10 over the three days**.
- Meta needs ~50 a week per ad set to leave learning, so this won't pick winners on ATC count.
- What it does do:
  - seasons the pixel;
  - proves every event fires;
  - shows which hooks stop the scroll.
- **Kill nothing on ATC count.**

**Read on Day 3 (per ad):**
- link CTR against your 2–3% benchmark: well under 2% is a hook problem;
- CPC;
- landing → quiz start;
- quiz completion;
- ATC rate against ~10%.

Write these down as the baseline.

## 3. Phase 2: Purchase test, ABO (Day 4 onwards)

**Structure:**
- New campaign: `LP | TEST | PURCH | ABO | US`. Conversion event: **Purchase**.
- **One ad set per concept** (V1, V2, V3, S1, S2, S3), each with its 3 or 2 hook variants.
- Same audience and exclusions as Phase 1.

**Budget:**
- Each concept needs ~$120 (≈2× the $59 hero set) before it can be judged. At **$30/ad set/day** that's 4 days.
- Full test: 6 × $30 = **$180/day**.
- Lean: start V1, V2, S1, S3 (the strongest evidence) at **$120/day**, and swap V3 and S2 in as you cut.

**Break-even ROAS ≈ 1.6** (worked out from NUMBER_SHEET §1b):

| Set | Gross profit | Less Stripe | Break-even ROAS |
|---|---|---|---|
| 3 pairs ($45) | $33 | ≈ $31 | 1.43 |
| 5 pairs ($59) | $41 | ≈ $38 | 1.55 |
| 10 pairs ($99) | $63 | ≈ $60 | 1.66 |

This is before Leak-Test refunds and Fit Promise reships. Recompute after the first 50 orders. Stop-loss: refunds over 10% of the first 50 orders → pause.

**Rhythm (your Step 5 rules):**
- Don't touch anything for 3–4 days.
- Then kill / fix / scale with the Kill or Scale tool:
  - **Fix:** find the first leak. Low CTR → hook; good CTR, low ATC → page/quiz; ATC but no buy → checkout.
  - **Kill:** a concept that can't clear ~1.6 ROAS by ~3× price (~$180 spent).
  - **Scale:** about 20% budget steps.
- Winners go back to Step 4 for more hooks on the same body.

## 4. Order of work from here

1. You: the blockers in §0 (pixel remap, CAPI, restriction check, test purchase). Get samples.
2. Me (Step 4): write the 15 ads from these skeletons, with a compliance check on every line.
3. Make the statics now (existing images); film or generate V1–V3 once samples land.
4. Launch Phase 1 → Day 4 Phase 2 → first kill/keep read on Day 7–8.

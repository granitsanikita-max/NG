# Leapproof: what's working in this niche (Step 3 research)

Pulled 2026-10-13 from the live US Meta Ad Library, plus WinningHunter for store revenue.
Every row below is backed by live ads. The ad IDs open in the Ad Library: `facebook.com/ads/library/?id=<ID>`.
The full evidence (286 proven ads with hooks, format, angle and link) is in `research/proven_ads.csv`.

## How "winning" was decided (no guessing)

- **Proven** means the ad is still active today and has run for **90+ days**. Advertisers kill losers fast.
- **Scaling** is shown three ways:
  1. **Impression rank.** The Ad Library can sort a brand's live ads by impressions, so a rank of #1 means that's where the spend goes.
  2. **Live count.** How many of the brand's live ads use the same hook or angle, counted across their whole library, not a sample.
  3. **Meta duplicates.** The same creative running in several ad sets.
- **Only brands making real money count:**

| Brand | Revenue (30d, WinningHunter) | Live US ads | Used as |
|---|---|---|---|
| **Everdries** (+ "Carol Henderson" persona page) | $1.6–2.8M | ~1,200 (≈740 video, ≈72 single-image, rest dynamic/catalog) | main model |
| **UltraDries** (4 persona pages: Life Beyond Leaks, Susan's Bladder Tips, Bladder Freedom Stories, Living Leak-Free) | $280–520K | ~200 | second model |
| Origin (pelvic PT), Mireva (pelvic trainer), local pelvic clinics | n/a | 90–372-day ads | only to check which hooks land on **30–45 women** |

- **Thrown out:**
  - Vera ($11–22K, traffic dying).
  - Ancienflow ($9–18K, collapsing).
  - LadyDry (0 live ads).
  - Knix (catalog ads only).
  - Thinx, Speax and Modibodi (nothing live in the US).
  - Everly ($0.9–1.6M bladder supplement): fake-doctor personas, so it's not a model.
- **Coverage:**
  - 193 proven ads from Everdries + UltraDries.
  - Hooks, format and angle pulled from 156 ads. That includes 45 of the 48 proven ads in each page's top 10 by impressions; the 3 not pulled are copies of concepts already covered.
  - Live counts run across both brands' full libraries.

## The 10-second version

1. **Video carries the spend.** Of Everdries' live video + image ads, about 91% are video, and about 65% of the top-30-by-impressions creatives across both brands are video.
2. **Statics still win slots.** UltraDries' #1 and #2 ads by impressions are statics, and so is Everdries' #1 image.
3. **The #1 angle across both brands is "pads/diapers are the wrong tool."**
4. **Everdries' biggest bet is "new / upgraded design".** About 420 live videos.
5. **Their #1 format is the A-vs-B side-by-side.** Old vs new, diapers vs Everdries, "what my mom uses vs what I use".
6. **Their headline is a customer quote:** `"Everdries changed my life"`. It's on ~400 live videos and 69 of 153 proven ads.
7. **Visual hooks that win:**
   - the product on a body (hands snapping the waistband);
   - a gross problem object (a used pad on the floor, a diaper bulge with a red arrow);
   - a side-by-side split.
8. **Offer framing they scale:**
   - 5-pack price vs "usually $X a pair" (~260 live);
   - "Perfect Fit Guarantee: new size free, no return" (~250 live);
   - "free gifts".
9. **Both winners sell to women 60+.** The hooks proven on **30–45 women** (sneeze, workout, postpartum, "not normal") come from pelvic clinics, Origin and Mireva, plus two Everdries statics.
10. **Much of what they run we can't legally copy:**
    - fake nurses and persona pages;
    - "100% leak-proof", "27× its weight";
    - UTI claims;
    - a "Black Friday sale" running since January.

    We copy the **format and hook structure** and swap out the claims (see §5).

---

## 1. Formats that win (ranked by evidence)

### Video

| # | Format | What it is | Evidence | Can we run it now? |
|---|---|---|---|---|
| F1 | **A-vs-B side-by-side** | Two pairs on a bed or hangers with a finger pointing between them. Or "here's what I look like in X / and in Y" on-body. | "original" ~260 live, "new design" ~420 live. Carol 1629603918494594 (275d, 6 dupes, **#1 on that page**). Everdries 1577194033627020 (275d), 1920176635259424 (250d, "diapers vs Everdries"), 811197242009709 (230d). | Yes, as **pad/liner vs Leapproof**. Needs the product on a body. |
| F2 | **Voiceover over b-roll, "news" hook** | "X have been redesigned for 2026 🤯" over fast on-body cuts. | Their most common format (24 of 76 unique Everdries creatives). 1812439156098880 (231d, 7 dupes, video #3), 903330442312047 (207d). | Yes, as "just launched". We are new, so it's true. |
| F3 | **Silent on-body try-on** | No voice, no text. A hand pulls up the waistband or stretches it under shorts or leggings. The caption does the selling. | 2012952326325019 (230d, 7 dupes), 1753945612644056 (246d, 3 dupes), 4033313263646750 (275d). | Yes. Cheapest to make. |
| F4 | **UGC talking head** | Excited woman to camera, holding the pack. | 886997533759184 (**334d, oldest live ad**, 7 dupes, video #2). | Only with real testers (Founding 30, disclosed). |
| F5 | **Promo announcement, reverse-psychology hook** | "Do NOT buy X tomorrow…" | 2033165163976432 (**#1 video by impressions**, 323d). 913473541362974 (275d). 2288431304917292 (275d). | Yes, but honest offer only, no fake sale. Best as **retargeting** (FUNNEL_PLAN §6 OFFER route). |
| F6 | **Expert explainer** | "Clinician" selfie in an office, talking to camera. | UltraDries runs it on 6 of its top-30 videos. 1212849274166991 (226d), 1575888883702412 (226d). | **No.** Every one is a persona or actor. Only with a real named pelvic PT. |
| F7 | **AI skit / talking object** | Animated pad villain ("I'm a bulky pad…", "I'm your disposable pad… I need to be honest with you"), Pixar-style woman. | 1700150534480418 (208d, 2 dupes), 1047546990938022 (Susan #3, 133d), 1400650075258672 (#4 on Bladder Freedom Stories, 104d). | Yes. No people needed. |

**Video length:**
- Everdries: median ~72s, most between 52s and 89s.
- UltraDries: median ~3:18, most between 3 and 4 minutes. These are long expert or talking-pad videos.

Longer is clearly not a problem in this niche.

### Static

| # | Format | What it is | Evidence | Can we run it now? |
|---|---|---|---|---|
| S1 | **Long-form native story** | Ugly phone photo of a problem object (used pad, pad on a bathroom floor) plus a long first-person caption. Your Notion "Native MSL / Confession" structure. | UltraDries **#1 and #2 images by impressions** (1271768424869385, 3241631309352492, 209d). Everdries postpartum 883503151225665 (245d). "What my mom uses vs what I use" 4313776562168091 (243d). | Yes, in **brand voice** or from a real tester's story. Never a fake persona. |
| S2 | **Native at-home on-body photo** | Looks like her own photo, no text, review-style caption. | 3899002186909593 (231d), 955109570520004 (221d), Carol 1646147329768369 (152d). | Yes. Our back-view and under-leggings images fit. |
| S3 | **Product collage + offer caption** | 5-panel product photos (pairs, liner close-up, stack in hands). | **Everdries #1 image by impressions**, 1259007659608370 (275d, 2 dupes). | Yes, with the real bundle math. Drop the fake "Black Friday". |
| S4 | **Before/after mirror selfie** | "The left photo was taken on a Tuesday morning." | Carol 1414715850705994 (250d). | Later. Needs a real customer. |
| S5 | **Value tips listicle graphic** | "Incontinence Tips: Exercise Edition", 5 numbered tips. | Carol 887125520881386 (**#1 on that page**, 249d). | Yes. Gym version for our athlete angle. |

---

## 2. Angles that win (ranked)

Live = number of Everdries' live US video ads (~740) using that wording, found by keyword search inside their page.

| # | Angle | Evidence | Leapproof (CJ column) version |
|---|---|---|---|
| A1 | **Pads/diapers are the wrong tool** | 21 of 22 UltraDries creatives. Everdries "pads" ~190 live, "diapers" ~75 live. 20 of the 52 top-30-by-impressions creatives. | Pads and liners bunch, feel like a diaper and go in the bin every day (FUNNEL_PLAN §2 enemy line). No UTI or "bacteria" claims. |
| A2 | **New / upgraded / just launched** | "new design" ~420 live, "original" ~260 live. Their current wave, "redesigned with cotton" (~220 live, launched Sept), is too new to count as proven. | "Just launched." True for us. We **can't** use cotton: our fabric is viscose. |
| A3 | **Feels like normal underwear / thin / invisible** | "thin" ~270, "comfortable" ~230, "high waist" ~240, "invisible" ~110. | "They look like plain black briefs. That's the point." Under-leggings visuals. |
| A4 | **Skeptic → believer** | "I was skeptical" ~210, "almost threw them away… so thin" ~78. 2062973080914066 (186d). | Only from real testers (objection O23, "looks too thin to work"). |
| A5 | **Offer: bundle + fit guarantee + gifts** | "50% off" ~300, "5-pack" ~260, "fit guarantee" ~250, "$69.95" ~140. "WARNING! Don't get a 5-pack… (get more)" 3917176148585428 (162d). | Fit Promise, free Wash Bag/Sheets, $9.90/pair on 10, 30-Night Leak-Test. **No fake "50% off".** |
| A6 | **Age identity** | "over 60" ~330 live. | Theirs, not ours. Our segment callouts are moment / postpartum / athlete, in the third person. |
| A7 | **Trigger moments** | Everdries "sneeze" ~100, "laugh" ~110 live. Origin "Leak when you sneeze?" (372d). Clinics: "Sneezing shouldn't require crossing your legs" (112d), "…jump on the trampoline with your kids" (103d). | Our default angle `m`. Strongest proof for 30–45. |
| A8 | **Postpartum / moms** | Origin (316d, several). Mireva "Moms are finally feeling in control again" (321d). Everdries "Target bathroom 3 weeks after giving birth" static (245d). | Angle `p`. |
| A9 | **Active / fitness** | Carol "Tips: Exercise Edition" (#1 on page). Clinics "Do you pee when you work out?" (112d). Origin "Missing your workout crew because of bladder leaks?" (137d). | Angle `t`. |
| A10 | **Night-time leaks** | "night" ~81–100 live, 1736682901089240 (178d). | **Skip.** Only if the CJ brief covers the back (FUNNEL_PLAN O20). |

---

## 3. Hooks that win (exact wording from live winners)

### Visual hooks (first 3 seconds)

What the 52 top-30-by-impressions creatives open on:

- **Product on a body, hand pulling the waistband** (15 of 52).
- **Problem object in close-up** (12 of 52):
  - a used, stained pad;
  - a pad on a bathroom floor;
  - a diaper bulge with a red arrow;
  - a toilet POV with a pad and 🤢.
- **Side-by-side split:** two pairs on hangers or a bed with a finger pointing (10 of 52).
- Excited woman to camera, waving a mailer.
- "Clinician" in an office, selfie angle. Persona: can't copy.
- AI talking pad / Pixar-style animated woman.

### Text and spoken hooks, grouped

**Comparison**
- "I loved my original Everdries, but their new design is 10 times better." (275d ×3, Carol #1)
- "Old versus new Everdries, what's the difference?" (Carol video #10)
- "Here's what I look like in diapers… and here's what I look like in Everdries." (250d, 230d)
- "What my mom uses for incontinence vs what I use for incontinence." (static, 243d)

**News**
- "Everdries have been redesigned for 2026 🤯" (231d, 7 dupes)
- "Everdries new boyshort design just got dropped off at my front door!" (263d)
- "So I just did something a little crazy…" (180d, 130d)
- "Who knew leakproof underwear could look THIS good!" (232d)

**Contrarian / problem**
- "It's 2025! Why are you still using pads? 🤢 / Pads weren't designed to be an incontinence solution" (275d, 6 dupes)
- "I'm a bulky pad. I contain your bladder leaks, but I bunch up, shift out of place…" (AI, 208d)
- "This is what happens to your pad every single night." (169d)

**Reverse psychology / offer**
- "Do NOT buy Everdries tomorrow or the day after that." (#1 video, 323d)
- "If you bought Everdries yesterday, you made a huge mistake…" (275d)
- "WARNING! Don't get a 5-pack from Everdries. I made this mistake." (162d)
- "I'm sick and tired of constantly buying new Everdries!" (124d)

**Static caption openers**
- "I need to warn every woman who uses disposable pads…" (#1 and #2 UltraDries images)
- "I just found out something about the pads I've been wearing every day for 6 years…" (202d)
- "Don't waste your money on organic reusables until you read this." (179d)
- "Sorry in advance if this is too personal but I just had to share this!" (275d)
- "When I first got my Everdries I almost threw them away!! They were so thin…" (~78 live)
- "OK I know I shouldn't be posting this at my age but…" (123d)
- "The left photo was taken on a Tuesday morning." (250d)
- "I called my mom crying from a Target bathroom three weeks after giving birth." (245d)

**Hooks proven on 30–45 women (clinics / Origin / Mireva)**
- "Leak when you sneeze?" (Origin, 372d)
- "Sneezing shouldn't require crossing your legs." (112d)
- "Did you know it's not normal to pee your pants?" (163d)
- "Do you pee when you work out?" (112d)
- "Because saying 'leaking after pregnancy is normal' should make us all a little nervous 😬" (139d)
- "Moms are finally feeling in control again and THIS is why." (321d)
- "Still waiting to 'bounce back'?" (137d)
- "Missing your workout crew because of bladder leaks?" (137d)
- "…the leaking when you laugh, sneeze, lift a box, or jump on the trampoline with your kids." (103d)

⚠️ Several of these break our Meta "you" rule as written ("Do you…", "Leak when you…"). Keep the moment, change the person:
- "For anyone who's crossed her legs before a sneeze."
- "Sneezing shouldn't require crossing your legs." Passes as is.

### Headlines

- `"Everdries changed my life"`: a customer-quote headline. ~400 live, 69 of 153 proven.
- "NEW Leakproof Boyshorts!!"
- "Finally! Stylish Protection That Actually Works"

Our equivalent is a **real** tester quote, once one exists. Until then, a plain product line.

---

## 4. Offer, CTA, landing

- **CTA button:** "Shop Now" on 100% of proven ads from both winners.
- **Everdries:**
  - Ads go to product-specific pages, plus one "nighttime listicle".
  - Offer: 5-pack $59.95–69.95 vs "usually $24.95–27.95 a pair".
  - "3 free gifts".
  - Perfect Fit Guarantee.
  - The "50% off" anchor is fake (it never ends).
- **UltraDries:**
  - Every ad goes to one "reasons-why" advertorial (`/reasons-why-v3-us`).
  - Cost-of-pads math ("$12,000+").
  - Money-back guarantee.
- **What that means for us:** our offer already has the pieces they scale.
  - Fit Promise = their Perfect Fit Guarantee.
  - Free Wash Bag/Sheets = their "free gifts".
  - Per-pair price = their per-pair anchor.
  - 30-Night Leak-Test = UltraDries' money-back guarantee.

  Our landing → quiz replaces their advertorial or product page. That swap is the one part that's ours.

## 5. What we can't copy, and the swap

| Their element | Why not | Our swap |
|---|---|---|
| Persona pages posing as customers (Carol Henderson, Life Beyond Leaks, Susan's Bladder Tips) | Fake reviews (FTC 2024 rule) | Post from the Leapproof page. Testimonials only from real testers, disclosed ("Received a free set to test"). |
| Nurse / gynecologist actors | Fake doctors | Only with a real, named pelvic PT (unlock later). |
| "100% leak-proof", "does not leak", "27× its weight", "20% more absorbent", water-pour test | Absolute claims; CJ column (no pour demo, no absorbency numbers) | "Made for light leaks" (only if our own sample test passes). |
| UTI / rash / "pads breed bacteria" | Health claims | Pads bunch, shift, feel like a diaper, go in the bin, cost money every month. |
| Black Friday / "50% off" running for months | Fake urgency | Real bundle math, gifts and guarantee. |
| "Women 60+" callouts | Not our customer | Moment / postpartum / athlete, said in the third person. |
| "Do you leak when you sneeze?" | Meta personal-attributes ("you") rule | Action or third person: "For anyone who's crossed her legs before a sneeze." |
| "Built for pee, not blood" / attacking period undies | CJ column | Pads and liners only. |
| "Redesigned with cotton" | Our fabric is viscose, not cotton | "Feels like plain underwear." |

## 6. The one honest risk

Both money-makers sell to 60+. Our formats and hooks are proven, but the evidence that these hooks land on 30–45 women comes from clinics, Origin and Mireva (90–372 days), plus two Everdries statics (postpartum, "mom vs me").

That's real proof, but thinner than the 60+ proof. If the 30–45 version stalls after a fair test, the fully proven fallback is the same concepts cast at 50–60+. That's a brand decision for you, not something to switch quietly.

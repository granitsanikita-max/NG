# §1 · Competitor scan — LOCKED-market revision (2026-10-06, after the §11 lock)

**Adds to, does not replace:** work/D1-s1.md. Its long-list, the 3 direct-competitor profiles (UpAiry, Kid Confident, BrightKidCo) and the 40-row ad log still stand for the toddler category. This revision re-scans for the **locked market** ("Big kids still learning", 5–9, daytime) and updates the long-list, BrightKidCo's status, the indirect competitors and the TAKEN map.

**Answer up front:**
- **Nobody sells big-kid daytime training underwear with a brand voice in US paid social right now** — *(§20B: corrected — add)* but **CARER (carerspk.com) runs a no-brand-voice kids' version on US Meta**: "hidden 100ml leak protection… dry at school", ages 4–16, 27 ads indexed since Nov 2025, still seen 2026-10-05 [V1]. BrightKidCo, the only one that tried an autism / sensory version, has 0 live ads (underwear last seen 2026-08-31; last ad of any kind 2026-09-05). Super Undies, the big-kid specialist, has run no ads since 2025 and is a night / special-needs catalogue.
- **The same parent IS being sold to at scale, by supplement brands:** Saphire (≈$0.9–1.6M/30d est.) and Bloomwise (≈$0.75–1.35M/30d est.) run first-person "my 7-year-old…" stories on Meta. They are this market's **indirect competitors** and its proof of reach.
- Big sizes on marketplaces (MooMoo 9T, "8-10Years" trainers, Carer, TIICHOO) have no brand, no stated capacity and visible leakage complaints.

Method (all 2026-10-06): Winning Hunter `get_store_details` (trysaphire.com, hellobloomkids.com, superundies.com, brightkidco.com) and `search_facebook_ads` (`searchkeyword: landingurl` for each domain, `pagename` "goodnites", countries US where set); `search_tiktok_products` (US); Amazon search scrapes; Firecrawl search for sensory-underwear brands. SimilarWeb superundies.com from [W2].

## 1 · Long-list additions for the locked market
| # | Brand | URL | Active Meta ads (WH) | Longest / last-seen ad | Region | Status |
|---|---|---|---|---|---|---|
| 23 | **Saphire** (indirect: kids' mood / focus gummies + bedwetting page + "From Wet Sheets to Sleepovers" e-book) | trysaphire.com | **103** ads to the domain in the US index; persona pages "Sarah Mitchell" **419** active, "Dr. James Harper" 178, "Try Saphire" 98 [U26]. Wave-1 snapshot: 684 + 226 + 149 [W3][W4] | Ads since 2026-02-13; "Sarah Mitchell" ads still seen 2026-10-06 [U26] | US 65.6% (also TH, GB, MX, ES) [U20] | **Live, scaling**: 188,362 visits Aug 2026 (×12 since Dec 2025); 30d revenue est. $870K–$1.6M; AOV $39.08 [U20] |
| 24 | **Bloomwise / Hello Bloom Kids** (indirect: kids' "meltable" supplements) | hellobloomkids.com | **420** active on page; "He had accidents at school at six years old" [W5] | — | US 90.8% [U21] | **Live, fastest-growing**: 828 → 139,388 visits (Jan → Aug 2026); 30d est. $748K–$1.35M; AOV $58.12; Recharge subscriptions [U21] |
| 25 | **Super Undies** (direct, big-kid specialist: bedwetting "Brain Trainers", special-needs 3-in-1 at **$34.99**, sizes "3 to 12 year olds") | superundies.com | **0.** 4 ads ever indexed; last seen **2025-11-25** (NZ); last US ad **2025-01-28** [U25] | 2024-05-30 → 2025-01-28 (US, bedwetting) | US 100% [U22] | **Inactive in paid**; 13,098 visits (Aug 2026); 30d est. $85K–$145K; **AOV $90.81**; store since 2019; "We're the big kid diaper experts!"; SimilarWeb "Health - Other" [W2][U22] |
| 26 | **MooMoo Baby 2T-9Y / 9T** (direct, marketplace) | amazon.com/dp/B0CZ34MF49 · /dp/B0C36FXQRL | 0 Meta | — | US (Amazon) | **Live**: 10-pack 9T $29.74 (**$2.97/pair**), 3,290 ratings, 9% 1★; leakage 116 of 180 mentions negative [U10]; 2T-9Y 900+ bought/mo in wave 1 [M17] |
| 27 | **BIG ELEPHANT** (big sizes to 9–10Y on Amazon; TikTok Shop listings are toddler) | amazon.com · TikTok Shop | 0 Meta | — | US | **Live**: TikTok Shop 10-pack 722 units / $24.1K (30d), "NOT Diapers… Limited Absorbency… Daytime Use Only" [U29] |
| 28 | **"Dinosaur 8-10Years" trainer** (no-name marketplace) | amazon.com/dp/B0H1HL64KX | 0 | — | US | Live: $18.99, 330 ratings, **16% 1★**; leakage 30 of 43 mentions negative [U11] |
| 29 | **Carer / TIICHOO / FUVVRVAL / EZ Moms** (big-kid absorbent "incontinence" boxers and trainers, ages 4–18) | amazon.com · carerspk.com | 0 *(§20B: corrected — CARER runs **27 kids' ads on US Meta** ("hidden 100ml leak protection… at school", live 2026-10-05) [V1]; TIICHOO / FUVVRVAL / EZ Moms 0)* | — | US | Live: Carer size 10 4-pack $39.99; TIICHOO 5-pack $31.99 (100+/mo); FUVVRVAL $29.99 (100+/mo); EZ Moms 5T-6T 100+/mo [U8][U9] |
| 30 | **Goodnites** (Kimberly-Clark; night, disposable; Autism Society partner per the lock) | goodnites.com | **0 indexed in the last 2 years.** 2 US ads indexed, last seen **2024-02-14**; one says it "holds the equivalent of 2 water bottles… 16 oz. in total" [U27] | 2023-06-30 → 2024-02-14 | US | Live on shelf (10K+/mo on Amazon [M17]); **WH coverage of big CPG brands is weak, so "0 ads" is low confidence** |
| 31 | **Sensory non-absorbent underwear:** Lucky & Me, SmartKnitKIDS, WunderUndies | luckyandme.com · amazon.com/dp/B09BN3YPSS · wunderundies.com | SmartKnitKIDS: **0** ads to its domain [U28]; others not indexed by name | — | US | Live, organic / SEO. Seamless, tagless, organic cotton; Lucky & Me packs $32–$40 [U33]. **No absorbency** (INFERENCE from listings). Recommended by ND parents: "We ended up getting Lucky & Me brand underwear and we haven't had any problems since!" [U34] (SNIPPET) |

**BrightKidCo status — updated** (replaces row 3 of work/D1-s1.md):
- **0 live.** 13 ads ever indexed to brightkidco.com [U24].
- The **autism / sensory underwear** ad ("Autistic kid still in Pull-Ups?… Over 10,000 autism families made the switch to big kid underwear") ran **2026-07-20 → last seen 2026-08-31** (US / GB) [U24]. *(§20B: corrected — a later sensory ad "Still in Pull-Ups?… 100 days risk-free" ran 2026-08-28 → **last seen 2026-09-05** (US/GB), so the sensory line's last sighting is 09-05, not 08-31. Note: WH indexes only 13 ads to the domain though the page showed up to 107 active, so "0 live" is moderate-confidence. BrightKidCo also already used "Not a 3-day miracle" in an April 2026 GB ad, so that phrase is not ownable [V8].)*
- The last ad of any kind was the **"Autism Constipation SOLVED!"** gummy (Happy Poop™), 2026-09-02 → **last seen 2026-09-05** [U24].
- The sensory PDP is still framed for toddlers: "Potty Training Underwear for Sensory-Sensitive Toddlers… Help Your Child Become Potty Trained in 4–6 Weeks" [U23].
- Store: 19,689 visits (Aug 2026), 30d est. $115K–$230K, 100% US; Trustpilot 3.0 from 2 reviews ("No exchange for wrong size") [U23].
- **Read:** a toddler-framed sensory handle, abandoned in paid. It could return; re-check monthly.

## 2 · Direct competitors for the locked market
The 3 with the most proven spend in the **category** are unchanged (UpAiry, Kid Confident, BrightKidCo; see work/D1-s1.md §2). In the **locked segment** there is **no direct competitor with active paid spend**:

| Candidate | Big-kid sizes? | Active paid? | Stated capacity? | Verdict |
|---|---|---|---|---|
| UpAiry | XL (55–70 lb) on PDP; creative stops at 4.5–5 [ad log] | Yes, ≈1,684 Meta ads (toddler / daycare) | No | Category leader, **not** in our segment's creative |
| Kid Confident | "Big Kid Sizes" SM/MD/LG $19.99 [M41] | Big-kid ad paused 2026-09-12 [M30] | No | Tested, stopped |
| BrightKidCo | Max L 4–6+ (lock) | **0 live** [U24] | No | Abandoned |
| Super Undies | To 12 years | **0 since 2025** [U25] | No (stuffable "Floods" liners) | Night / special-needs, clinical tone |
| MooMoo / BIG ELEPHANT | To 9–10 | Marketplace only | No ("Limited Absorbency") | No brand, leakage complaints |
| **CARER (carerspk.com) / TIICHOO** *(§20B: split out — was grouped above as "Marketplace only · No stated capacity")* | 4–16 / 4–18 | **CARER: yes, US Meta (27 kids ads, 100 ml "at school" copy, live 2026-10-05) [V1]**; TIICHOO: marketplace only | **Yes, small and flat:** CARER 100 ml all sizes (PDP) / 50–80 ml (Amazon titles); TIICHOO 30–40 ml [V1][V3][V4] | **The closest real competitor.** Incontinence-coded, adult-store brand, product codes, no creed, not size-matched, 3.9★ (48) |

## 3 · Indirect competitors for THIS market (same parent, same pain, different product)
| Indirect competitor | What they sell | Proof of scale | What's working (steal the principle) |
|---|---|---|---|
| **Saphire** | Kids' mood / focus gummies; bedwetting page; dry-nights e-book | 103 ads in the US index; persona pages up to 419 active; ~$0.9–1.6M/30d est. [U20][U26] | **First-person parent story about a named-age child** ("My 7-year-old wakes up happy…"), persona doctor page, advertorial landers (`/pages/mom-burnout-adv`, `/pages/gentle-parenting`). **Steal:** first-person, specific age, real outcome — with **real** creators only (§2B bans their personas) |
| **Bloomwise** | Kids' "meltable" supplements | 420 active on page; traffic ×168 in 7 months; ~$0.75–1.35M/30d est. [U21][W5] | **School-accident story** as the hook ("accidents at school at six years old"). **Steal:** the school-day scene as the opening frame |
| **UpAiry Tummy Gummies** (via "Kereisa Collens") | Constipation gummies | 77 active; "accidents at school, which led to him being teased" [W5] | Links accidents to constipation and teasing. **Our version:** we don't treat the cause; we handle the accident with dignity and say "talk to your pediatrician" |

**§20B caveat on reach proof:** Saphire's revenue is mainly mood / focus gummies + ADHD guides (bedwetting e-book created 2026-09-07) and Bloomwise's school-accident hook is a **constipation / soiling** story in UK English ("A&E", "£200", "health visitor") [V6][V7]. They prove this parent (school-age, often ND) is reachable on US Meta at $39–58 AOV; they do **not** prove she spends on daytime-wetting gear.

**Their weak spots (our opening):** health claims and fake personas (Saphire Trustpilot 3.0 from 74 reviews; complaints: "Difficult subscription cancellation process" 7, "Unauthorized or unexpected subscription charges" 5, "Use of fake profiles and AI-generated content in marketing" 1 [U20]); a gummy can't stop today's wet trousers at school.

## 4 · TAKEN map — updated for the locked market
| Incumbent | Owned angle | Region | Status |
|---|---|---|---|
| UpAiry (7 pages) | Feel-wet mechanism; toddler late-trainer shame (to 4.5–5); daycare / kindergarten deadline; working-parent; fake-mom advertorials; $21 "SCAM"; **Tummy Gummies on "accidents at school + teased"** | US 95%, GB, CA | **Active** (dominant, toddler) |
| Kid Confident | "7 accidents in 1 day" UGC; anti-3-day; feedback-loop listicles; big-kid sizes (1 ad) | US | **Active** (big-kid ad **paused**) |
| BrightKidCo | "Body-Signal Learning Layer™"; deadline fear; **autism / sensory toddler edition**; "30 Days Potty Trained Promise"; "Autism Constipation SOLVED!" | US / GB / CA / NZ | **Abandoned** (0 live; last seen 2026-09-05) |
| **Saphire** | **Night / bedwetting + ADHD mood** for school-age kids, via first-person persona stories and a dry-nights e-book | US 66%, GB, CA, AU | **Active, scaling** |
| **Bloomwise** | **School-age accidents / ADHD / calm** via supplements; school-accident story hook | US 91% | **Active, scaling fast** |
| **Super Undies** | "Big kid diaper experts": bedwetting Brain Trainers, special-needs 3-in-1 ($34.99), sizes to 12; "Health - Other" | US 100% | **Inactive in paid** (organic / SEO only) |
| **Goodnites / Pull-Ups / Ninjamas** | Night protection, "holds 16 oz" (Goodnites 2023), disposable convenience, "Learning Layer Feels Wet" | US retail | **Active on shelf**; Meta not indexed since 2024 (low confidence) |
| **MooMoo 2T-9Y / 9T, BIG ELEPHANT, "8-10Years", Carer, TIICHOO, FUVVRVAL, EZ Moms** | Marketplace value + de-claimed absorbency; big sizes with no brand or number | US Amazon / TikTok Shop | **Active (no paid social)** |
| **Lucky & Me / SmartKnitKIDS / WunderUndies** | Sensory comfort (seamless, tagless, soft), **no absorbency** | US | Active (organic / SEO) |
| Tiny Tots, Rudie Baby, My Carry Potty, Sculptara, Drynimo… | Toddler category angles (see work/D1-s1.md §5) | CA / AU / UK / US | Unchanged |

**White space (locked market), confirmed:**
- **Daytime + big-kid sizes + real-underwear look + a stated number per size + a brand voice** is owned by nobody active. *(§20B: still true as a bundle, but its parts are not: a flat 100 ml number + "at school" + real-underwear look + ages 4–16 is live on US Meta from CARER [V1]. What nobody has: a size-matched pour-tested number, a training (not incontinence) identity, a creed, and the School-Day Kit.)*
- Night is TAKEN (Saphire, Goodnites, Super Undies). The ND sensory *comfort* claim is held organically by Lucky & Me / SmartKnit, but **without absorbency**. The ND *training* claim was BrightKidCo's, now abandoned.
- **Caveat:** Goodnites published a capacity figure ("16 oz") in 2023 for night pants; Super Undies prints 325–620 ml per size on its night Brain Trainers [V9]. *(§20B: corrected — was "Our 'first to state a number' claim must be scoped to daytime training underwear in US paid social now (0 of 908 ads)".)* **Drop the "first to state a number" claim entirely:** CARER (100 ml, US Meta), TIICHOO (30–40 ml) and Carer Amazon (50–80 ml) already print numbers on big-kid daytime-capable underwear [V1][V3][V4]. Claim only what is ours: "tested per size, printed per size".

## So What → do this
1. **Attack the daytime big-kid gap** that nobody runs in paid: sizes to 12, real-underwear look, pour-tested ml per size.
2. **Copy the supplement brands' reach mechanics, not their tactics:** first-person, named-age stories from **real** parents and creators; school-day scenes. No personas, no health claims, no subscription traps (their Trustpilot shows the cost).
3. **Price against Carer ($10–13.75/pair) and Super Undies ($34.99), not MooMoo ($2.97).** Win the MooMoo comparison only with a *visible* ml difference on camera.
4. Re-check BrightKidCo, Kid Confident's big-kid ad and Super Undies in the Ad Library **monthly** (re-entry risk).

## Sources
- [V1]–[V7] §20B re-checks, 2026-10-06 — full lines in work/D1-s2-LOCKED.md Sources.
- [V8] Winning Hunter `search_facebook_ads` keyword "brightkidco", pagename, sort lastseen, 2026-10-06: latest last-seen 2026-09-05 (sensory "Still in Pull-Ups?" + Happy Poop); April 2026 GB ad copy "Not fully trained. Not a 3-day miracle." (DATA / VERBATIM as indexed).
- [V9] Super Undies Brain Trainer specifications: https://superundies.com/pages/brain-trainer-specifications ("Absorbs 325 ml… 400 ml… 540 ml… 620 ml without added inserts", S 3-5y → XL 10+), firecrawl_scrape 2026-10-06 (VERBATIM). Night product per https://superundies.com/pages/what-is-the-difference-between-the-nighttime-and-hero-undies.
- [U8] Amazon "kids incontinence underwear boys washable": https://www.amazon.com/s?k=kids+incontinence+underwear+boys+washable, 2026-10-06 (DATA).
- [U9] Amazon "training underwear big kids size 8 10": https://www.amazon.com/s?k=training+underwear+big+kids+size+8+10, 2026-10-06 (DATA).
- [U10] Amazon MooMoo 9T: https://www.amazon.com/dp/B0CZ34MF49, 2026-10-06 (DATA).
- [U11] Amazon "Dinosaur 8-10Years": https://www.amazon.com/dp/B0H1HL64KX, 2026-10-06 (DATA).
- [U20] Winning Hunter `get_store_details` trysaphire.com (incl. Trustpilot gap analysis), 2026-10-06 (DATA).
- [U21] Winning Hunter `get_store_details` hellobloomkids.com, 2026-10-06 (DATA).
- [U22] Winning Hunter `get_store_details` superundies.com, 2026-10-06 (DATA).
- [U23] Winning Hunter `get_store_details` brightkidco.com, 2026-10-06 (DATA).
- [U24] Winning Hunter `search_facebook_ads` keyword brightkidco.com, `searchkeyword: landingurl`, `sort_by: lastseen`: 13 ads; latest last-seen 2026-09-05, 2026-10-06 (DATA / VERBATIM copy as indexed).
- [U25] Winning Hunter `search_facebook_ads` keyword superundies.com, landingurl, lastseen: 4 ads; latest last-seen 2025-11-25, 2026-10-06 (DATA).
- [U26] Winning Hunter `search_facebook_ads` keyword trysaphire.com, landingurl, countries US, longestrunning: total 103, 2026-10-06 (DATA).
- [U27] Winning Hunter `search_facebook_ads` keyword "goodnites", `searchkeyword: pagename`, countries US: 2 ads, last seen 2024-02-14, 2026-10-06 (DATA / VERBATIM copy).
- [U28] Winning Hunter `search_facebook_ads` keyword smartknitkids.com, landingurl: 0 results, 2026-10-06 (DATA).
- [U29] Winning Hunter `search_tiktok_products` US, 30d ("training underwear big kids", "incontinence underwear kids"), 2026-10-06 (DATA).
- [U33] Lucky & Me sensory-friendly collection: https://luckyandme.com/collections/sensory-friendly-kids-clothing ; WunderUndies: https://wunderundies.com/ ; SmartKnitKIDS: https://www.amazon.com/SmartKnitKIDS-Girls-Seamless-Sensitivity-Undies/dp/B09BN3YPSS (SNIPPET, firecrawl_search 2026-10-06).
- [U34] Reddit r/Autism_Parenting "Sensory-friendly underwear": https://www.reddit.com/r/Autism_Parenting/comments/1fkc8qk/sensoryfriendly_underwear/ (SNIPPET).
- [W2] SimilarWeb superundies.com (Health - Other): https://www.similarweb.com/website/superundies.com/ (DATA, via work/D2-s3.md).
- [W3][W4][W5] Winning Hunter searches (defined in work/D2-s3A.md).
- [M17] [M30] [M41] and the ad log: work/D1-s1.md / work/D1-s0B.md / work/ad-log.csv.

# §20 B · Adversarial fact-check: history, medical, stat and science claims that could reach ad copy

*Skeptic run, 2026-10-06. The brief was to refute, not confirm. Each fact was re-opened at a primary source where one exists (Europe PMC REST abstracts, journal PDFs, CDC / NIDDK / CPSC / FTC / eCFR, K-C's own PDF, period newspapers via Firecrawl). The `agent-reach` CLI is not installed, so Firecrawl stood in for it (🔁, see work/tools-log-20B-facts.md).*

**Verdicts:**
- **CONFIRMED**: the source was opened and the wording matches.
- **CONFIRMED (SNIPPET)**: real, but only search text was seen. Confirm it before live creative.
- **CORRECTED**: the right fact and its URL are given, and the file was fixed in place.
- **REMOVE**: unverifiable. It must not enter ad copy. An inline "(§20B: unverified — do not use in ads)" note was added.

Every edit in the files carries a "(§20B: …)" note, so nothing was silently changed.

**Scope note:** the brief mentioned "autism 1 in 31" and an ADHD prevalence figure. **Neither stat appears in any of the files checked** (grep over all of work/*.md). Nothing was checked or added for them. If someone adds them later, they need the CDC ADDM 2025 report and a NSCH source, and they must stay off ads (Meta personal attributes).

---

## A · History / heritage (§13B spine, §18B hooks, Funnel Map history beat)

| # | Claim (file) | Verdict | Evidence |
|---|---|---|---|
| H1 | Brazelton was "the spokesman for the new size 6 Pampers… kids over 35 pounds". He "approached Pampers with the idea of the size 6 diaper". "it's the child's deal". "pressures with day care" (D3-s13B, D3-s18B C1, research-persuasion C1) | **CONFIRMED**. The earlier flag "re-fetch returned chrome only" is now resolved: a Firecrawl directQuote scrape returned all four lines. | https://www.tampabay.com/archive/1999/01/06/parents-cheer-for-diaper-change/ |
| H2 | **"In January 1999 … size 6"** / "In 1999 the fix was a size 6 diaper" (D3-s13B, D4-FunnelMap) | **CORRECTED → 1998–99.** The commercial was already running in Dec 1998. | Baltimore Sun 1998-12-13: https://www.baltimoresun.com/1998/12/13/training-issues-are-looming-large-diapers-manufacturers-are-producing-bigger-disposables-for-children-who-have-outgrown-conventional-sizes-but-are-not-yet-using-the-potty/ · Sun-Sentinel 1998-12-27 https://www.sun-sentinel.com/1998/12/27/diaper-trends/ (SNIPPET) |
| H3 | Brazelton "**launched**" the size 6. He was "**the most famous / America's best-known child-led pediatrician**" (D3-s13B story) | **CORRECTED.** He was the spokesman, not the launcher. The superlative can't be proven, so the copy now says "promoted on TV by one of America's best-known pediatricians". | TIME, NYT (H4, H5) |
| H4 | TIME 25 Jan 1999: "chairman of the Pampers Parenting Institute". Critics said the Pampers tie "stinks". "giving the same advice long before". Problems fell "from the national average of 8% to about 1%" (Brazelton's own claim) | **CONFIRMED** | https://time.com/archive/6734449/war-of-the-diapers/ |
| H5 | NYT 12 Jan 1999: "Dr. Brazelton advises in a television commercial for Pampers size-6 diapers, suitable for children 35 pounds and over" | **CONFIRMED (SNIPPET)**. The NYT page is blocked. | https://www.nytimes.com/1999/01/12/us/two-experts-do-battle-over-potty-training.html |
| H6 | "27 years later" (D3-s13B) | **CORRECTED → "nearly 30 years" (1998 → 2026)** | H2 |
| H7 | Tampa Bay: "1962 study … 90 percent out of diapers by 2½ … only 22 percent are trained by that age now" (research-persuasion) | **REMOVE.** It is garbled in the re-scrape ("2{"), the "22%" study is unnamed, and it conflicts with the 1962 paper's reported **mean of 28.5 months** | Kiddoo, CMAJ 2012: https://pmc.ncbi.nlm.nih.gov/articles/PMC3307553/ |
| H8 | "P&G had helped Brazelton fund his own foundation". The quoted Pampers ad line "I'm glad there's finally a bigger diaper…" (research-persuasion, P10) | **REMOVE.** No primary source was found. The foundation line is a defamation-grade claim about a real person. | search 2026-10-06 (no hit) |
| H9 | Brazelton 1962, *Pediatrics*: 1,170 children, daytime continence at a mean of 28.5 months | **CONFIRMED** (paper exists, PMID 13872676; figures via Kiddoo) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3307553/ · https://doi.org/10.1542/peds.29.1.121 |
| H10 | "**In 1989 Kimberly-Clark launched Pull-Ups nationally**" (D3-s13B) | **CORRECTED → "began a national rollout in 1989", "blanketing one-third of the country over a three-year period".** | K-C PDF: https://www.kimberly-clark.com/-/media/kimberly/pdf/innovation/ProductEvol_DisposableTrainingPants_umbracoFile.pdf |
| H11 | K-C quotes: "'big kid' underwear … convenience, practicality and performance of a diaper". "The market potential wasn't in diapers. Parents didn't want to perpetuate the diapering stage." Cloth trainers in the 1980s were "quite messy" | **CONFIRMED** (PDF text re-read) | same K-C PDF |
| H12 | Slogan "I'm a big kid now!" (was a Wikipedia SNIPPET) | **CONFIRMED, upgraded.** K-C's PDF says "I'm a big kid now." "So we trademarked the whole line". | same K-C PDF |
| H13 | "So the first big-kid product was a diaper with an underwear story" | **Kept, labelled INFERENCE/opinion.** It's our reading of K-C's words, not a quoted fact. | — |
| H14 | Pampers went on sale in Peoria, Dec 1961, at "ten cents a diaper". Disposables had ~1% of the US diaper market in 1957 and 42% in 1973 | **CONFIRMED** (secondary: Conversable Economist, citing Postrel, *Works in Progress*, 2026) | https://conversableeconomist.com/2026/05/07/history-of-the-disposable-diaper/ |
| H15 | "95% of parents used them late '90s; 80% early '80s; 50% early '70s" (P10) | **REMOVE** (newsletter SNIPPET, no original) | — |
| H16 | Victor Mills (P&G) was motivated by his grandchild's cloth diapers | **CONFIRMED (secondary)** | Conversable Economist (above); https://en.wikipedia.org/wiki/Victor_Mills |
| H17 | Sears, Maccoby & Levin 1957: "92% … started … and 60% had completed" before 18 months | **CONFIRMED as Seim 1989 reports it, with a date CORRECTION.** Seim says Sears "reported data from **1947**". Say "1940s data" or "a 1957 book", never "in 1957, 92%…". It is a secondary reading, so keep it off ads. | https://cdn-uat.mdedge.com/files/s3fs-public/jfp-archived-issues/1989-volume_28-29/JFP_1989-12_v29_i6_toilet-training-in-first-children.pdf |
| H18 | The 92% "trained by 18 months" misquote (UpAiry, Go Diaper Free, the 1999 NYT/Brody piece) | **Confirmed as a misquote.** Never repeat it. | Seim PDF (above) |
| H19 | "Sayable" line: "today half aren't trained until about 3 (35–39 months)" | **CORRECTED.** That is a 1995–96 Milwaukee sample, not "today". It now reads "in a 1990s US study". | Schum 2001, PMID 11888377 (Europe PMC) |
| H20 | Digo (deVries 1977): "night and day dryness is accomplished by 5 or 6 months" | **CONFIRMED** | https://doi.org/10.1542/peds.60.2.170 (PMID 887331) |
| H21 | Vietnam: whistle cue, "all children used the potty by the age of 9 months", "completed" at 24 months. Comparison: 98% complete at 24 months vs 5% of Swedish children *started* | **CONFIRMED.** These are **two separate papers**: the whistle is PMID 23182948, and the 98% vs 5% is PMID 23759503 (n = 47 vs 57). The file now cites them separately. | Europe PMC abstracts |
| H22 | Bakker & Wyndaele 2000: 321 respondents, 812 children. Bladder drill "progressively abandoned". "good concordance" with programmes for treating bladder dysfunction | **CONFIRMED**, but the hook "**pediatric urologists now prescribe**" is **CORRECTED**. "Prescribe" overstates "concordance" and drifts into a health claim. | PMID 10930924, https://doi.org/10.1046/j.1464-410x.2000.00737.x |
| H23 | Azrin & Foxx 1971: 9 institutionalized adults, median 4 days, incontinence "reduced immediately by about 90%" | **CONFIRMED** | https://doi.org/10.1901/jaba.1971.4-89 |
| H24 | The 1974 book "sold more than three million copies" | **CONFIRMED, upgraded** to a NYT obituary (SNIPPET) | https://www.nytimes.com/2013/04/16/health/nathan-azrin-behavioral-psychologist-dies-at-82.html |
| H25 | Azrin 1974: "average 3.9 h", "success rate closer to 74%" (Wikipedia) | **REMOVE** (unverified) | — |
| H26 | Foxx & Azrin: ready children trained in a mean of 4.5 h | **CONFIRMED** (Kiddoo) | PMC3307553 |
| H27 | Children's Bureau "Infant Care" said "Never too early" (L6) | **REMOVE** (already banned. The pamphlet text was never read) | — |
| H28 | "Who invented training pants": none claimed | **OK.** No inventor is claimed anywhere. | — |
| H29 | NHS GHC "83% out of nappies by 18 months in the 1970s–80s" | **REMOVE** (already banned. No citation in the PDF) | — |

## B · Medical / prevalence / statistical

| # | Claim (file) | Verdict | Evidence |
|---|---|---|---|
| M1 | Daytime wetting affects 7–10% of 5–13-year-olds [M64] (D1-s0, D3-s6/9/9B/16, FunnelMap) | **CONFIRMED.** Abstract: "affects approximately 7-10% of children (aged 5-13 years)". | https://pubmed.ncbi.nlm.nih.gov/31060913/ |
| M2 | Boston Children's: "Up to 10 percent of 5-year-olds are estimated to have problems with wetting accidents". Usual potty-training age is ~5, then see a pediatric urologist. Causes include small functional bladder capacity and kids being "too busy" to empty fully | **CONFIRMED** | https://www.childrenshospital.org/conditions-treatments/daytime-wetting-enuresis |
| M3 | NIDDK: daytime wetting is "commonly caused by holding urine too long, constipation…" [W10] | **CONFIRMED** | https://www.niddk.nih.gov/health-information/urologic-diseases/bladder-control-problems-bedwetting-children/symptoms-causes |
| M4 | **≈1.3–1.85M US children aged 5–9** with daytime wetting (D1-s0-LOCKED) | **CORRECTED → ≈1.4–2.0M.** The 5–9 cohort is ≈20.1M (28,156,369 children aged 5–11 in 2024 × 5/7). Internal sizing only, never in an ad. | https://datacenter.aecf.org/data/tables/101-child-population-by-age-group |
| M5 | US births in 2024: 3,622,673 [M66] | **CONFIRMED** | https://www.cdc.gov/nchs/pressroom/releases/20250423.html |
| M6 | Expected bladder capacity is 30 × (age + 1) ml for ages 4–12 (ICCS / "Koff") [B4] | **CONFIRMED**, with a stronger source added. Rittig 2010, *J Urol* (ICCS reappraisal): "the universally used formula 30 × (age + 1) ml is indeed valid … only if the first morning void is disregarded". **Caveat:** it is a 50th-percentile *maximum* voided volume, not a typical void. | https://www.ics.org/folder/committees/children-public-documents/d/14-age-related-nocturnal-urine-volume-and-maximum-voided-volume-in-healthy-children-reappraisal-of-international-childrens-continence-society-definitions/download · Maternik 2016 PDF (ics.org, quote re-read) |
| M7 | Wake Forest: (age + 2) × 30 ml. "For a 5-year-old … (5+2) 30 = 210 ml" [B5] | **CONFIRMED** (VERBATIM) | https://www.wakehealth.edu/specialty/p/pediatric-urology/how-much-should-a-bladder-hold |
| M8 | D3-s9 / D3-s9B attribute "(age + 2) × 30" to **Koff** | **CORRECTED.** The Wake Forest page gives no attribution, and the literature calls 30 × (age + 1) "Koff's formula". Copy should use 30 × (age + 1) (as D3-s9-REWRITE does) and say "a standard pediatric formula". | Rittig 2010 (above) |
| M9 | "A big kid's bladder holds **2–4×** what toddler trainers are rated for" (D3-s13, D3-s13B) | **CONFIRMED with caveats.** It is exact for ages 5–7 (180–240 ml vs 60–90 ml) and conservative at 8–9 (up to 5×). The toddler side rests on **one UK brand's Instagram SNIPPET** [P49], which can't be scraped. **In ads, replace the comparator with our own filmed pour of a bought toddler trainer.** | P49 SNIPPET: https://www.instagram.com/p/DWVIMVNAaaG/ |
| M10 | Cooper 2003 *J Urol*, 467 Iowa teachers: 80% set break times, one-third told a child to wait, 18% got information, "worse following kindergarten" | **CONFIRMED** | PMID 12913750 (Europe PMC abstract) |
| M11 | ERIC "**Right to Go**" survey of 1,132: nearly half not allowed, a quarter scared, 36.65% avoid water (D3-s18B C5) | **CORRECTED.** The survey is "**Voices for change**", run Nov 2023–Jan 2024 by ERIC's Young Champions (aged 12–19). Exact figures: 47.73% / 24.18% / 36.65%. It is UK and teen, so never use it in US ads. | https://eric.org.uk/news/desperate-to-go-young-people-struggling-to-access-toilets-at-school/ |
| M12 | Breinbjerg 2021: "no secure conclusions can be made, as the literature is inadequate" | **CONFIRMED** | PMID 34099398 |
| M13 | Bladt 2025 pilot, n = 23: 43/13, 52/13, 87/35, 78/13% | **CONFIRMED** (enrolled ages 18–36 months, analysed range 19–30) | PMID 41099785 |
| M14 | Schum 2001: 50% trained at 35 (girls) / 39 (boys) months. Daycare and maternal employment were not significant | **CONFIRMED** | PMID 11888377 |
| M15 | Blum 2004 *J Pediatr*: later initiation, stool toileting refusal and constipation predict later training | **CONFIRMED** | PMID 15238916 |
| M16 | Blum 2004 *Pediatrics*: constipation precedes stool toileting refusal (STR), n = 380 | **CONFIRMED** (title and design. The 24.4% and 93.4% figures sit past the abstract cut-off of my read; keep them off ads) | PMID 15173531 |
| M17 | Taubman 2003: STR 23% vs 26%. Duration 5.2 vs 7.6 months. Training completed at 40.0 vs 43.0 months | **CONFIRMED** | PMID 14662573 |
| M18 | Seim 1989: mean completion at 24–27 months | **CONFIRMED** | PMID 2592922 |
| M19 | Largo 1977: early potty training had "no effect on bladder control by day or at night" | **CONFIRMED** | PMID 913901 |
| M20 | Simon & Thompson 2006 (2 of 5 improved). Greer 2016 (2 of 4). Tarbox 2004 (one adult) | **CONFIRMED** | PMIDs 17020216, 26695997, 15154222 |
| M21 | Kaerts 2014 (74% equal role, 17%, 30%, 18%, 40% "no idea"). Kaerts 2012 (81.8%, 79.8%) | **CONFIRMED** | PMIDs 23495098, 22207492 |
| M22 | NCES 2019: 59% in weekly nonparental care. Of those, 62% center, 38% relative, 20% nonrelative | **CONFIRMED** | https://nces.ed.gov/fastfacts/display.asp?id=4 |
| M23 | AAP / HealthyChildren: "consistent with those of your child's other caregivers". Adapted from the 2016 guide, updated 5/25/2022 | **CONFIRMED** | https://www.healthychildren.org/English/ages-stages/toddler/toilet-training/Pages/Creating-a-Toilet-Training-Plan.aspx |
| M24 | BABITT RCT (Sweden): no difference in functional GI disorders (52.0% vs 49.6%) | **CONFIRMED** | PMID 41249012 |
| M25 | Dr. Steve Hodges is a pediatric urologist and author of *It's No Accident* | **CONFIRMED (SNIPPET)** | https://www.amazon.com/dp/076277360X |

## C · Product / material / compliance claims (D3-s17, D4-s2B-LOCKED)

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| P1 | "PFAS-free" is "**a forbidden phrasing**" (D3-s17 #16) | **CORRECTED.** It is not banned by law. Under FTC Green Guides 16 CFR 260.9, a free-of claim is allowed only at trace or background level and must be substantiated, so it is high-risk without test data. Preferred wording is "no intentionally added PFAS", backed by a declaration **and** a total-organic-fluorine (TOF) test. | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-260/section-260.9 |
| P2 | California AB 1817 bans intentionally added PFAS in textiles from Jan 2025 (D4-s2B) | **CONFIRMED, plus a missing half added.** "Regulated PFAS" also means TOF ≥100 ppm from 2025, falling to **50 ppm from 1 Jan 2027**. New York's apparel ban also started 1 Jan 2025. | https://www.morganlewis.com/pubs/2024/11/new-york-and-california-bans-on-pfas-in-textiles-and-apparel-begin-january-1-2025 · https://www.buchalter.com/blogs/navigating-new-pfas-regulations-in-california-and-new-york-critical-updates-for-the-textile-and-apparel-industries/ |
| P3 | OEKO-TEX needs a certificate number | **CONFIRMED, made more precise.** The label also needs the testing institute. | https://www.oeko-tex.com/fileadmin/user_upload/Marketing_Materialien/STANDARD_100/FAQs/FAQ_STANDARD_100_EN_ES_01.2019.pdf |
| P4 | CPSC: importers must eFile the CPC with CBP from July 8, 2026 | **CONFIRMED** | https://www.cpsc.gov/Business--Manufacturing/Testing-Certification/Childrens-Product-Certificate |
| P5 | Meta's personal-attributes list includes "family status" | **CORRECTED.** It is not on the current list. Age, disability and physical/mental health (incl. medical conditions) are confirmed. The three example ads in D4-s2B were not re-found on the current page. | https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/ |
| P6 | "100% cotton" on a TPU-lined pant is a mismatch | Logic check: **CONFIRMED** (FTC textile fiber-content rules [M60] were already sourced) | — |

## D · Compliance sweep of proposed ad / landing lines (§2B table)

| File | Line | Problem | Fix (in place) |
|---|---|---|---|
| D3-s18B L3 | "What your grandmother did that pediatric urologists now prescribe." | Overstates the source and frames treatment, a health claim | "What grandma did that bladder programmes use again today." No product tie-in. |
| D3-s13 Core Metaphor | "That isn't your kid failing." | "your kid" plus accidents implies a condition (Meta). Landing pages are reviewed too. | "That isn't the kid failing." |
| D3-s9-REWRITE | "Your big kid needs the *Big-Kid Hold*." | Same | "Big kids need the *Big-Kid Hold*." |
| D3-s11, D4-FunnelMap | "If your kid needs a full bladder held…" | Same, and it's on the landing page | "If a kid needs a full bladder held…" |
| D3-s13B / FunnelMap | "Nobody printed the one number" | A false absolute: Super Undies (150–300 ml), Peejamas ("up to 4 ounces"), Snazzipants state ml. It's an FTC substantiation risk. | "The big-kid sizes on the shelf still don't print…" |
| All | Brazelton's name in ads | A factual, sourced history of a deceased public figure is OK. No image, and no implied endorsement (already flagged). The "foundation funding" line is REMOVED (H8). | — |
| All | Prevalence stats | Third person only ("Up to 10% of 5-year-olds…"). Never "your child". | Already in §2B. Confirmed as compliant. |

---

## Corrections log (file: old → new)

**D3-s13B.md**
- "In 1989 Kimberly-Clark launched Pull-Ups nationally" → "began a national rollout of Pull-Ups … one-third of the country over a three-year period".
- Slogan [P71]: SNIPPET → VERBATIM (K-C trademark line).
- "In January 1999, America's best-known child-led pediatrician" → "By late 1998 / January 1999, … one of America's best-known pediatricians".
- [P1]: "VERBATIM, collector's scrape" → re-confirmed via Firecrawl, plus the Baltimore Sun 1998 source.
- "27 years later" → "Nearly 30 years later (1998 → 2026)".
- The "2–4×" line now carries the Rittig 2010 confirmation, the age caveat, and the note "use own pour, not P49" in ads.
- "the obvious question nobody printed an answer to" → "…the mainstream big-kid trainers don't print…".
- Story paragraph: "In 1999 … launched by the most famous child-led pediatrician in America … for the next 27 years … Nobody printed the one number" → "In 1998 … promoted on TV by one of America's best-known pediatricians … for nearly 30 years since … The big-kid sizes on the shelf still don't print the one number".
- Fact-check flags for [P1] and [P71] are marked RESOLVED.

**D3-s18B.md**
- L2: the two Duong papers are now cited separately.
- L3 hook: "…pediatric urologists now prescribe" → "…bladder programmes use again today".
- L4: book sales upgraded to the NYT obituary.
- C1: [P1] re-confirmed.
- C2: slogan upgraded, and "began rolling out in 1989" added.
- C5: ERIC "Right to Go" → "Voices for change" (Young Champions aged 12–19, Nov 2023–Jan 2024), with exact 47.73% / 24.18% / 36.65%. Marked UK/teen, not for US ads.
- C6: "data from 1947" date caveat added.

**D3-s13.md**
- UMP point 1 now has a §20B confirmation note (Rittig 2010; it's a 50th-percentile max voided volume; the "2–4×" age range; replace the P49 comparator).
- Proof-list rows for the 2–4× claim and the prevalence stats were updated to CONFIRMED with URLs.
- Core Metaphor: "your kid failing" gets a compliance note → "the kid failing".

**D3-s9.md**: "(age + 2) × 30 ml (Koff) … ~270 ml at 7" → attribution corrected. Use 30 × (age + 1) → 240 ml at 7.

**D3-s9B.md**: the (age + 2) × 30 line is marked superseded by 30 × (age + 1). P49 is noted as a UK SNIPPET.

**D3-s9-REWRITE.md**: "Your big kid needs…" → compliance note: "Big kids need…".

**D3-s11.md** and **D4-FunnelMap.md**: "If your kid needs a full bladder held" → compliance note: "If a kid needs…".

**D4-FunnelMap.md**
- "1999 the answer … size 6" → "1998–99 …".
- "the shelf still has no number" → "big-kid sizes on the shelf still print no number" (not absolute).
- A P49 comparator note was added.
- "1999 size-6 history" → "1998–99".

**D1-s0-LOCKED.md**: "≈1.3–1.85M US children aged 5–9" → "≈1.4–2.0M" (KIDS COUNT / Census base ≈20.1M). Marked internal-only.

**D3-s17.md** #16:
- "PFAS-free … is a forbidden phrasing" → not banned, but high-risk under 16 CFR 260.9.
- Added the TOF test with California's 100 ppm limit, falling to 50 ppm on 1 Jan 2027.
- OEKO-TEX now needs the cert number **and** the testing institute.

**D4-s2B-LOCKED.md**
- The PFAS row gains the AB 1817 TOF thresholds, New York's ban and 16 CFR 260.9.
- Meta: "family status" is not on the current Personal Attributes list. The example ads were not re-found. The current page's health example was added.
- CPC eFile July 8, 2026: CONFIRMED note.

**research-persuasion.md**
- The "90% by 2½ / 22% now" line → **REMOVE** note.
- "P&G helped fund his foundation" and the ad line → **REMOVE** note.
- "95% / 80% / 50% of parents" → **REMOVE** note. The 1% → 42% and Peoria 1961 lines → CONFIRMED note.
- "Sayable accurate version" (92% / "today 35–39 months") → reworded: "1940s data", "a 1990s US study".
- Azrin "3 million" → CONFIRMED (NYT). "3.9 h" and "74%" → REMOVE.
- Pull-Ups slogan → upgraded, plus the rollout wording.
- New note: never cite the 1999 NYT/Brody "92 percent" line.

## Checked and left unchanged (no external fact to refute)
These items are internal tallies or tool data, not historical or medical facts: data-bank counts (n = 601 / 79), Winning Hunter ad counts (0 of 908, Haven 236 ads), Google Trends indices, and Goodreads ratings. Also unchanged: D2-s10, D2-s14 and D4-s4B, which hold no external historical or medical claims beyond those listed above, and D3-s6, D3-s12 and D3-s16, which only re-use M1 and M2.

## Net effect on the ad story
The §13B spine **survives**, with three wording fixes:
- the date becomes 1998–99;
- "spokesman", not "launched";
- the claim becomes "the mainstream shelf doesn't print a number", not "nobody does".

The mechanism math survives on a stronger source (Rittig 2010). The one weak link is the toddler-trainer comparator (P49, one UK Instagram snippet). **Film our own pour of a bought US toddler trainer** and use that number instead.

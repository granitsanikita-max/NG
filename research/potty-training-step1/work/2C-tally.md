# §2C — Data bank tally (reproducible)
Run: 2026-10-06 (re-run after the §11 lock, upstream revision) · Source file: `work/2C-databank.csv` (one row per snippet, page column schema) · Build: `python3 work/2C-src/build_bank.py` (merges + de-dupes on URL+quote) → tally: `python3 work/2C-src/tally.py`.
Every number below is printed by the script — no estimates.

## How the bank was built
- **New rows (N001–N264, 264):** collected this run. Trustpilot UpAiry (3 pages scraped, VERBATIM) · Amazon /dp/ pages for BIG ELEPHANT, MooMoo Baby, Gerber, Hanes, Pampers Easy Ups (top reviews VERBATIM, "Customers say" aspect excerpts SNIPPET) · Walmart review page + search excerpts · YouTube comments (yt-dlp comment API, VERBATIM) · TikTok comments (search excerpts, SNIPPET) · X via product-pulse (SNIPPET) · Reddit, What to Expect, BabyCenter, Mumsnet, Facebook-group search excerpts (SNIPPET).
- **Re-used rows (S001–S252, 250 kept):** from `docs/potty-training-research/snippets.md`, re-tagged into this schema by `work/2C-src/convert_old.py`. The script maps the old #tags to the new tags, adds keyword rules on the quote text, and takes great phrases from the C-parent-voice swipe file. 2 rows were dropped because they are not customer voice: S025 (a vendor's reply) and S243 (a publisher's editorial). Capture: Reddit/search rows stay SNIPPET; What to Expect full-thread scrapes and retailer-review scrapes become VERBATIM; Mumsnet WebFetch rows become SNIPPET, because the earlier run did not check them character by character.
- **Re-verification of the re-used rows (sample):** 11 distinctive phrases were searched again with Firecrawl. 9 came back at the same URL: S070, S093, S146, S182 (full text visible on What to Expect, so it is VERBATIM), S018, S091, S066, S129, and the S221 thread. S001 and S026 did not come back in this search. That means "not re-found", not "contradicted", and both stay SNIPPET. Reddit still returns 403 for page fetches, so no Reddit row could be upgraded to VERBATIM.
- **Dates:** reviews, YouTube, TikTok and X rows carry the date shown on the page. YouTube dates are approximate because the site only shows "N years ago". Re-used Reddit rows carry `~YYYY-MM (est. from post ID)`, interpolated from base-36 post IDs, so treat them as an estimate (INFERENCE) and not as a quoted date.
- **Tagging:** one person tagged the new rows by hand. The re-used rows were tagged by rule. Tags are short, normalised labels, and a cell can hold several values separated by "; ". Labels were merged where they meant the same thing; the NORM map in build_bank.py lists every merge.

## Read these numbers with 3 caveats
1. **Search depth ≠ prevalence.** The re-used bank was built with extra queries on neurodivergent (ND) kids, late trainers and night wetting. That is why "ND / sensory parent" (117 in wave 1; 132 after the upstream wave) and "late training" (70; now 74) rank high. The upstream wave was deliberately queried on school-age daytime accidents, so the locked-segment counts are also search-depth evidence, not market share. Treat the segment counts as how much evidence exists, not as market share. The new rows were collected without a positioning lens and are dominated by general toddler parents and product reviews.
2. **UpAiry's subscription scam inflates "scam".** 1★ Trustpilot reviews are mostly about a hidden gummy subscription. That is a fact about the UpAiry checkout, not about the product category. Trustpilot shows 185 of its 557 UpAiry reviews at 1★ (page meta).
3. **Amazon:** Amazon showed 28 full reviews with stars (2 at 1–2★, 26 at 4–5★); the sign-in wall hides deeper review pages. Another 49 rows are the excerpts Amazon quotes under each "Customers say" aspect, where the star rating is not shown. Most of the 1–2★ wording therefore comes from Trustpilot, Walmart and Reddit.
   - **DATA from the Amazon aspect widgets, counted by Amazon:**
     - MooMoo: Leakage 525 mentions (140 positive / 385 negative); Absorbency 523 (293 / 230); Value 327 (183 / 144).
     - BIG ELEPHANT: Leakage 276 (88 / 188); Size 221 (50 / 171); Fit 346 (232 / 114).
     - Gerber: Fit 1,020 (694 / 326); Absorbency 297 (223 / 74).
     - Star splits: BIG ELEPHANT 14,123 ratings (76/13/5/2/4%) · MooMoo 17,722 (76/11/5/2/6%) · Gerber 6,670 (82/12/3/1/2%) · Easy Ups 1,001 (81/11/4/1/3%) · Walmart BIG ELEPHANT 839 (7% 1★).


## Upstream wave after the §11 lock (2026-10-06) — 514 → 601 rows
- **Why:** the locked market is "Big kids still learning" (US parents of 5–9-year-olds with DAYTIME accidents; work/LOCK-decision.md). Only 19 wave-1 rows carried the buyer group "school-age accidents parent", so the segment counts were thin.
- **What was added:** 87 new rows (N265–N351) in `work/2C-src/new_zsa1.py`, same columns and tagging scheme. The file name sorts after the wave-1 files, so the existing IDs N001–N264 did not shift. The first 514 rows of the CSV are byte-identical to the pre-revision file (checked with `cmp`).
  - Reddit 61 (r/kindergarten, r/Parenting, r/pottytraining, r/ADHDparenting, r/ParentingADHD, r/Autism_Parenting, r/Mommit, r/AskParents, r/AskTeachers, r/Teachers, r/specialed, r/Incontinence, r/breakingmom, r/daddit, r/Preschoolers) · Forum 21 (What to Expect 4, BabyCenter 5, Mumsnet 10, Facebook groups 2) · YouTube comments 4 (yt-dlp, VERBATIM) · Amazon 1 (MooMoo 9T "Customers say" Fit excerpt).
  - Search snippets = SNIPPET (Reddit/forums still block page fetches). YouTube comment text = VERBATIM.
- **Buyer-group rule for the new rows:** "school-age accidents parent" is used ONLY when the poster describes their own child aged about 5–9 with daytime accidents. Advice-givers are tagged "commentator" and teachers "school teacher", so the locked-segment count is not inflated. Result: 60 of the 87 new rows are in the locked segment; the other 27 are commentators / teachers / ND parents with no stated age.
- **Not usable (logged, not padded):** X returned only noise (profiles, sports, news) for school-age wetting queries → 0 rows. Amazon big-size listings (MooMoo 9T, "Dinosaur 8-10Years") showed only toddler-age "Customers say" excerpts except one; full reviews sit behind sign-in. Facebook-group results were mostly AI summaries, so only 2 quoted comments were kept. Night-only and soiling-only posts were skipped (out of scope).
- **Dates:** Reddit dates are estimated from the post ID with the same anchor table as wave 1; 2 posts older than the first anchor are marked "before 2015-08". Forum threads carry "n/d".
- **New tag values introduced:** need "spare-clothes kit for school", "school accommodation"; pain "child afraid to ask at school"; belief "child can't help it"; authority "pelvic floor PT", "continence charity (ERIC)"; buyer group "commentator", "school teacher". Everything else reuses wave-1 labels.

## Script — `work/2C-src/tally.py`
```python
# Tally every tag column of work/2C-databank.csv (multi-value cells split on "; ")
import csv, collections, os, sys
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","2C-databank.csv")
R=list(csv.DictReader(open(p,encoding="utf-8"))); N=len(R)
TAGS=["pain","desire","need","objection","failed_solution","trigger","misconception","belief","emotional_state","awareness_stage","burned_skeptical","authority_trusted","buyer_group"]
def cnt(col):
    c=collections.Counter()
    for r in R:
        for v in [x.strip() for x in r[col].split(";") if x.strip()]: c[v]+=1
    return c
print(f"TOTAL snippets (after de-dupe on url+quote): {N}")
print("\n## Snippets per source type")
for k,v in collections.Counter(r["source_type"] for r in R).most_common(): print(f"- {k}: {v}")
print("\n## Capture"); [print(f"- {k}: {v}") for k,v in collections.Counter(r["capture"] for r in R).most_common()]
rev=[r for r in R if r["stars"]]
print("\n## Star-rated reviews: ",len(rev)," | 1-2★:",sum(r['stars'] in('1','2') for r in rev)," | 3★:",sum(r['stars']=='3' for r in rev)," | 4-5★:",sum(r['stars'] in('4','5') for r in rev))
amz=[r for r in R if r["source_type"]=="Amazon"]
print("Amazon rows:",len(amz),"| with star shown:",sum(bool(r['stars']) for r in amz),"| Amazon 1-2★:",sum(r['stars'] in('1','2') for r in amz),"| Amazon 4-5★:",sum(r['stars'] in('4','5') for r in amz),"| Amazon excerpts w/o star (Customers-say aspect quotes):",sum(not r['stars'] for r in amz))
LABEL={"pain":"Pain","desire":"Desire","need":"Need","objection":"Objection","failed_solution":"Failed solution","trigger":"Trigger","misconception":"Misconception","belief":"Belief","emotional_state":"Emotional state","awareness_stage":"Awareness","burned_skeptical":"Burned/skeptical","authority_trusted":"Authority trusted","buyer_group":"Buyer group"}
print("\n## Top 10 per tag (n = snippets mentioning it, of",N,")")
for t in TAGS:
    c=cnt(t); tagged=sum(1 for r in R if r[t].strip())
    print(f"{LABEL[t]} [{tagged} tagged]: "+" · ".join(f"{k} ({v})" for k,v in c.most_common(10)))
print("\n## Awareness-stage split (§5)")
c=cnt("awareness_stage")
for k in ["unaware","problem","solution","product","most"]: print(f"- {k}: {c.get(k,0)} ({100*c.get(k,0)/N:.0f}%)")
print("\n## Emotional-state counts (§6)")
for k,v in cnt("emotional_state").most_common(): print(f"- {k}: {v}")
b=[r for r in R if r["burned_skeptical"].strip()]
print(f"\n## Burned / skeptical (§8): {len(b)} of {N} snippets ({100*len(b)/N:.0f}%)")
for k,v in cnt("burned_skeptical").most_common(): print(f"- {k}: {v}")
print("\n## Buyer-group counts (§3A) — a snippet can carry >1 group")
for k,v in cnt("buyer_group").most_common(): print(f"- {k}: {v}")
print("\n## Full counts per tag (all values)")
for t in TAGS[:8]+["authority_trusted"]:
    print(f"\n### {LABEL[t]}"); [print(f"- {k}: {v}") for k,v in cnt(t).most_common()]
print("\n## Great phrases captured:",sum(bool(r['great_phrase']) for r in R))

# ---- Added 2026-10-06 (upstream revision after the §11 lock) ----
sp=lambda v:[x.strip() for x in v.split(";") if x.strip()]
def cntR(rows,col):
    c=collections.Counter()
    for r in rows:
        for v in sp(r[col]): c[v]+=1
    return c
LOCK=[r for r in R if "school-age accidents parent" in sp(r["buyer_group"])]
SEGB={"ND / sensory parent","late-trainer parent","school-age accidents parent"}
segB=[r for r in R if SEGB & set(sp(r["buyer_group"]))]
print(f"\n## LOCKED-SEGMENT CUT — 'Big kids still learning' (buyer_group contains 'school-age accidents parent' = parent of a ~5–9-year-old with DAYTIME accidents): {len(LOCK)} of {N} rows")
print("Source types: "+" · ".join(f"{k} ({v})" for k,v in collections.Counter(r['source_type'] for r in LOCK).most_common()))
print("Capture: "+" · ".join(f"{k} ({v})" for k,v in collections.Counter(r['capture'] for r in LOCK).most_common()))
print("ND overlap (also tagged 'ND / sensory parent'):",sum("ND / sensory parent" in sp(r["buyer_group"]) for r in LOCK))
for t in TAGS:
    c=cntR(LOCK,t); tagged=sum(1 for r in LOCK if r[t].strip())
    print(f"{LABEL[t]} [{tagged} tagged]: "+" · ".join(f"{k} ({v})" for k,v in c.most_common(10)))
c=cntR(LOCK,"awareness_stage")
print("Awareness split (locked cut): "+" · ".join(f"{k}: {c.get(k,0)} ({100*c.get(k,0)/len(LOCK):.0f}%)" for k in ["unaware","problem","solution","product","most"]))
print(f"\n## Segment B (wave-1 definition: ND / sensory OR late-trainer OR school-age): {len(segB)} of {N} rows")
c=cntR(segB,"awareness_stage")
print("Awareness split (segment B): "+" · ".join(f"{k}: {c.get(k,0)} ({100*c.get(k,0)/len(segB):.0f}%)" for k in ["unaware","problem","solution","product","most"]))
fc=__import__("re").compile(r"diaper|nappies|nappy|goodnite|goodnight|size 7|non[- ]?verbal|level 3|level 2",__import__("re").I)
print("Segment B full-containment language (same regex as cuts.py #16):",sum(bool(fc.search(r['quote'])) for r in segB))
print("Locked cut full-containment language:",sum(bool(fc.search(r['quote'])) for r in LOCK))
```

## Output (verbatim)
```
TOTAL snippets (after de-dupe on url+quote): 601

## Snippets per source type
- Reddit: 293
- Forum: 112
- Amazon: 78
- Trustpilot: 44
- YouTube comments: 27
- TikTok comments: 14
- Walmart: 13
- Retailer reviews: 10
- X: 8
- Instagram comments: 2

## Capture
- SNIPPET: 457
- VERBATIM: 144

## Star-rated reviews:  77  | 1-2★: 30  | 3★: 2  | 4-5★: 45
Amazon rows: 78 | with star shown: 28 | Amazon 1-2★: 2 | Amazon 4-5★: 26 | Amazon excerpts w/o star (Customers-say aspect quotes): 50

## Top 10 per tag (n = snippets mentioning it, of 601 )
Pain [449 tagged]: late training (3.5y+ still not trained) (74) · leaks / soaked after one pee (55) · deadline pressure (daycare/school rule) (41) · daily accidents at school/daycare (38) · parent burnout (34) · judgment / shame from others (30) · withholding / poop refusal (29) · night wetting (29) · child doesn't notice wet / body signals (28) · regression (24)
Desire [202 tagged]: dry nights (43) · daycare/school-ready (39) · less mess / cleanup (29) · no-pressure process (19) · child learns from feeling wet (15) · independence (pull on/off herself) (10) · child dignity / real underwear (9) · protection out in public (4) · daycare-approved (3) · out of diapers / independence (3)
Need [284 tagged]: absorbency that holds a pee (104) · feel-wet signal (43) · bigger sizes (24) · leakproof at night (23) · daycare-friendly (19) · sensory-friendly fit (16) · routine / reminder system (14) · reliable sizing / fit (14) · honest checkout (13) · fun designs (11)
Objection [110 tagged]: won't hold pee / leaks (47) · scam / hidden subscription (16) · waste of money (15) · holds only one small accident (14) · sizing / fit uncertain (13) · price (10) · feels like a diaper (5) · skeptical of brand / reviews (5) · shipped from China (5) · quality (3)
Failed solution [204 tagged]: Pull-Ups / disposables (67) · training underwear (UpAiry) (27) · 3-day / Oh Crap method (23) · training underwear (generic) (22) · training underwear (MooMoo) (13) · training underwear (BIG ELEPHANT) (11) · rewards / stickers / bribes (8) · training underwear (other brand) (8) · tried everything (6) · Miralax / medical (6)
Trigger [114 tagged]: daycare/preschool deadline (31) · school start (K/Reception) (20) · daycare pull-up/underwear rules (11) · relative judgment (10) · soaked bed (9) · school/teacher complaint (6) · outgrew largest size (4) · new sibling (4) · 3-day weekend attempt (4) · sleepover invite (2)
Misconception [24 tagged]: late training = lazy parenting (4) · should be trained by 2/3 (4) · 3 days is enough (4) · untrained at 5 = severe delay (2) · special underwear speeds training (2) · missed the window (1) · pull-ups at 4.5 = neglect (1) · training underwear should catch everything (1) · leak proof training underwear exists (1) · pricier = leakproof (1)
Belief [117 tagged]: feeling wet teaches the child (25) · every kid own timeline (13) · pull-ups are just diapers (13) · constipation causes accidents (12) · readiness matters (10) · no shame approach (9) · pull-ups hide the wet (8) · methods don't work for ND kids (6) · ads overpromise (5) · pull-ups cause regression (3)
Emotional state [601 tagged]: Neutrality (223) · Pride (86) · Anger (86) · Fear (66) · Apathy (44) · Acceptance (26) · Desire (18) · Shame (15) · Guilt (15) · Grief (11)
Awareness [601 tagged]: problem (250) · product (176) · solution (174) · unaware (1)
Burned/skeptical [74 tagged]: waste of money (34) · scam (19) · nothing works (15) · tried everything (8) · skeptical (4)
Authority trusted [75 tagged]: other parents (22) · daycare staff (15) · creator with lived experience (7) · pediatrician (6) · occupational therapist (4) · pediatric urologist (3) · ABA therapist (2) · daycare teacher experience (2) · potty-training creator (2) · influencer review (2)
Buyer group [601 tagged]: general toddler parent (199) · ND / sensory parent (132) · school-age accidents parent (79) · late-trainer parent (64) · working parent / daycare (61) · night / bedwetting parent (47) · withholding parent (28) · commentator (21) · dad (21) · regression parent (17)

## Awareness-stage split (§5)
- unaware: 1 (0%)
- problem: 250 (42%)
- solution: 174 (29%)
- product: 176 (29%)
- most: 0 (0%)

## Emotional-state counts (§6)
- Neutrality: 223
- Pride: 86
- Anger: 86
- Fear: 66
- Apathy: 44
- Acceptance: 26
- Desire: 18
- Shame: 15
- Guilt: 15
- Grief: 11
- Willingness: 8
- Courage: 3

## Burned / skeptical (§8): 74 of 601 snippets (12%)
- waste of money: 34
- scam: 19
- nothing works: 15
- tried everything: 8
- skeptical: 4

## Buyer-group counts (§3A) — a snippet can carry >1 group
- general toddler parent: 199
- ND / sensory parent: 132
- school-age accidents parent: 79
- late-trainer parent: 64
- working parent / daycare: 61
- night / bedwetting parent: 47
- withholding parent: 28
- commentator: 21
- dad: 21
- regression parent: 17
- childcare worker: 12
- twins parent: 11
- eco / cloth parent: 9
- grandparent / gift buyer: 9
- school teacher: 4
- teen / self: 1
- single parent: 1

## Full counts per tag (all values)

### Pain
- late training (3.5y+ still not trained): 74
- leaks / soaked after one pee: 55
- deadline pressure (daycare/school rule): 41
- daily accidents at school/daycare: 38
- parent burnout: 34
- judgment / shame from others: 30
- withholding / poop refusal: 29
- night wetting: 29
- child doesn't notice wet / body signals: 28
- regression: 24
- parent guilt: 19
- size / big-kid products: 18
- leaks / soaked bed at night: 18
- constant accidents: 18
- child refuses: 17
- sensory discomfort: 17
- sizing / fit problems: 17
- laundry / mess: 15
- cost / money drain: 14
- hidden subscription / billing: 14
- child shame / embarrassment: 13
- child can't communicate need: 12
- daycare pull-up/underwear rules: 10
- fear child will be teased: 6
- poop accidents messy: 6
- limited time (working parent): 5
- daycare vs home inconsistency: 4
- slow shipping: 4
- outings / public accidents: 3
- stress of training: 3
- parent shame / embarrassment: 2
- can't access specialist help: 2
- poor quality: 2
- child refuses product: 2
- marriage strain: 2
- refund not honoured: 2
- child refuses underwear: 1
- small leaks after training: 1
- power struggle: 1
- punishment backfires: 1
- stuck at home during training: 1
- doesn't hold pee: 1
- cheap brands don't hold: 1
- hidden subscription: 1
- daily accidents at school age: 1
- no resources for older / ND kids: 1
- size / big kid output: 1
- pressure on child: 1
- no resources for older kids: 1
- child holds until pull-up on: 1
- consistency hard for busy parent: 1
- long timeline: 1
- comparison to peers: 1
- new sibling: 1
- can't access doctor: 1
- child afraid to ask at school: 1

### Desire
- dry nights: 43
- daycare/school-ready: 39
- less mess / cleanup: 29
- no-pressure process: 19
- child learns from feeling wet: 15
- independence (pull on/off herself): 10
- child dignity / real underwear: 9
- protection out in public: 4
- daycare-approved: 3
- out of diapers / independence: 3
- big-kid underwear feeling: 3
- fun designs kid wants to wear: 3
- sleepovers without shame: 2
- dry bed: 2
- backup after training: 2
- off pull-ups: 2
- real-underwear look with protection: 2
- child-led readiness: 2
- faster training: 2
- body awareness (register need to go): 2
- protection for almost-accidents: 1
- fewer outfit changes: 1
- child picks own pair: 1
- child confidence: 1
- child wants to wear them: 1
- comfort on sensitive skin: 1
- buys time to reach potty: 1
- dignity / looks like pants: 1
- daycare on board: 1
- less mess at daycare: 1
- train over a weekend: 1
- calm no-pressure process: 1
- leave the house: 1
- less stress: 1
- support during training: 1
- real underwear look: 1
- training on the go: 1
- feel wet without the mess: 1
- method that fits my child: 1
- next step after pull-ups: 1
- reusable / lasts: 1
- help for older kids: 1
- something that works: 1
- feel like a good parent: 1
- relief / patience: 1
- school-ready without pressure: 1
- consistent at daycare: 1
- daycare-ready: 1
- train before back to work: 1

### Need
- absorbency that holds a pee: 104
- feel-wet signal: 43
- bigger sizes: 24
- leakproof at night: 23
- daycare-friendly: 19
- sensory-friendly fit: 16
- routine / reminder system: 14
- reliable sizing / fit: 14
- honest checkout: 13
- fun designs: 11
- discreet: 10
- washable / reusable: 9
- resources for older / ND kids: 7
- easy pull up/down: 7
- spare-clothes kit for school: 7
- waterproof cover layer: 6
- durable / washable: 4
- layered protection: 4
- real-underwear look with protection: 3
- real-underwear feel: 3
- wetness indicator: 2
- affordable: 2
- easy poop cleanup: 2
- front absorbency (boys): 1
- soft: 1
- absorbency for dribbles: 1
- nap protection: 1
- protection out in public: 1
- breathable: 1
- returns / guarantee: 1
- school accommodation: 1

### Objection
- won't hold pee / leaks: 47
- scam / hidden subscription: 16
- waste of money: 15
- holds only one small accident: 14
- sizing / fit uncertain: 13
- price: 10
- feels like a diaper: 5
- skeptical of brand / reviews: 5
- shipped from China: 5
- quality: 3
- no better than regular underwear: 3
- not needed: 2
- guarantee not honoured: 2
- shipping time: 2
- ads overpromise: 2
- returns cost: 1
- not worth it: 1
- big brand let down: 1
- only useful late in training: 1
- may not work for my kid: 1
- may slow training: 1
- category is a scam: 1
- not worth the price: 1
- will leak out the front: 1
- poop cleanup: 1

### Failed solution
- Pull-Ups / disposables: 67
- training underwear (UpAiry): 27
- 3-day / Oh Crap method: 23
- training underwear (generic): 22
- training underwear (MooMoo): 13
- training underwear (BIG ELEPHANT): 11
- rewards / stickers / bribes: 8
- training underwear (other brand): 8
- tried everything: 6
- Miralax / medical: 6
- Goodnites: 5
- gadgets (seats, potties, books): 3
- regular underwear: 2
- training underwear (Gerber): 2
- naked method: 2
- training underwear (Hanes): 2
- potty watch: 1
- regular character underwear: 1
- diapers / nappies: 1
- punishment: 1
- cheap training underwear: 1
- diapers at night: 1
- rewards / games: 1

### Trigger
- daycare/preschool deadline: 31
- school start (K/Reception): 20
- daycare pull-up/underwear rules: 11
- relative judgment: 10
- soaked bed: 9
- school/teacher complaint: 6
- outgrew largest size: 4
- new sibling: 4
- 3-day weekend attempt: 4
- sleepover invite: 2
- back to work: 2
- accidents at preschool: 2
- school says back to nappies: 2
- seeing ads: 2
- about to start training: 2
- one painful poop: 1
- holiday break / planned start: 1
- child asks for underwear: 1
- after 3-day method: 1
- weekend training before daycare Monday: 1
- cabin fever during training: 1
- bought from social media ad: 1
- diaper size outgrown: 1
- child takes diaper off: 1
- started kindergarten: 1
- going back to work: 1
- accidents at school: 1

### Misconception
- late training = lazy parenting: 4
- should be trained by 2/3: 4
- 3 days is enough: 4
- untrained at 5 = severe delay: 2
- special underwear speeds training: 2
- missed the window: 1
- pull-ups at 4.5 = neglect: 1
- training underwear should catch everything: 1
- leak proof training underwear exists: 1
- pricier = leakproof: 1
- just potty train him: 1
- it's very easy: 1
- readiness is an excuse: 1

### Belief
- feeling wet teaches the child: 25
- every kid own timeline: 13
- pull-ups are just diapers: 13
- constipation causes accidents: 12
- readiness matters: 10
- no shame approach: 9
- pull-ups hide the wet: 8
- methods don't work for ND kids: 6
- ads overpromise: 5
- pull-ups cause regression: 3
- consistency / schedule works: 2
- pressure backfires: 2
- fake reviews everywhere: 2
- night dryness is developmental: 1
- learning not training: 1
- commit and it goes fast: 1
- pull-ups help early training: 1
- all training pants are kind of a scam: 1
- reviews from other parents: 1
- cheaper alternatives are the same: 1
- you get what you pay for: 1
- reviews + easy returns lower risk: 1
- cheaper options work just as well: 1
- 3-day method only fits stay-at-home parents: 1
- nothing works: 1
- child can't help it: 1

### Authority trusted
- other parents: 22
- daycare staff: 15
- creator with lived experience: 7
- pediatrician: 6
- occupational therapist: 4
- pediatric urologist: 3
- ABA therapist: 2
- daycare teacher experience: 2
- potty-training creator: 2
- influencer review: 2
- experienced childcare worker: 1
- nursery staff: 1
- experienced childcarer: 1
- Oh Crap method: 1
- autism consultant: 1
- OT creator: 1
- pediatrician (TikTok): 1
- author / performance coach: 1
- pelvic floor PT: 1
- continence charity (ERIC): 1

## Great phrases captured: 271

## LOCKED-SEGMENT CUT — 'Big kids still learning' (buyer_group contains 'school-age accidents parent' = parent of a ~5–9-year-old with DAYTIME accidents): 79 of 601 rows
Source types: Reddit (55) · Forum (18) · YouTube comments (4) · TikTok comments (1) · Amazon (1)
Capture: SNIPPET (75) · VERBATIM (4)
ND overlap (also tagged 'ND / sensory parent'): 16
Pain [66 tagged]: daily accidents at school/daycare (34) · constant accidents (16) · child doesn't notice wet / body signals (8) · late training (3.5y+ still not trained) (7) · deadline pressure (daycare/school rule) (7) · regression (7) · parent burnout (4) · withholding / poop refusal (3) · judgment / shame from others (3) · night wetting (2)
Desire [11 tagged]: daycare/school-ready (8) · child dignity / real underwear (2) · independence (pull on/off herself) (2)
Need [16 tagged]: routine / reminder system (7) · spare-clothes kit for school (4) · absorbency that holds a pee (2) · discreet (2) · feel-wet signal (1) · real-underwear look with protection (1) · bigger sizes (1) · fun designs (1)
Objection [0 tagged]: 
Failed solution [12 tagged]: Miralax / medical (4) · Pull-Ups / disposables (4) · tried everything (2) · training underwear (generic) (1) · diapers / nappies (1) · Goodnites (1)
Trigger [20 tagged]: school start (K/Reception) (10) · daycare/preschool deadline (4) · school/teacher complaint (4) · school says back to nappies (2) · accidents at school (1) · relative judgment (1)
Misconception [1 tagged]: pull-ups at 4.5 = neglect (1)
Belief [7 tagged]: constipation causes accidents (6) · readiness matters (1)
Emotional state [79 tagged]: Neutrality (30) · Fear (24) · Apathy (7) · Acceptance (5) · Anger (4) · Pride (4) · Grief (2) · Willingness (1) · Desire (1) · Courage (1)
Awareness [79 tagged]: problem (55) · solution (22) · product (2)
Burned/skeptical [2 tagged]: tried everything (1) · nothing works (1)
Authority trusted [10 tagged]: pediatric urologist (3) · pediatrician (3) · other parents (2) · pelvic floor PT (1) · continence charity (ERIC) (1)
Buyer group [79 tagged]: school-age accidents parent (79) · ND / sensory parent (16) · working parent / daycare (7) · withholding parent (3) · late-trainer parent (1) · dad (1)
Awareness split (locked cut): unaware: 0 (0%) · problem: 55 (70%) · solution: 22 (28%) · product: 2 (3%) · most: 0 (0%)

## Segment B (wave-1 definition: ND / sensory OR late-trainer OR school-age): 225 of 601 rows
Awareness split (segment B): unaware: 0 (0%) · problem: 150 (67%) · solution: 59 (26%) · product: 16 (7%) · most: 0 (0%)
Segment B full-containment language (same regex as cuts.py #16): 30
Locked cut full-containment language: 6
```

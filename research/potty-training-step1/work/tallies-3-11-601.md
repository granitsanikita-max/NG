# Tallies for §3–§11 — 601-row re-run (refresh after the §2C upstream wave)
Run on 2026-10-06 against `work/2C-databank.csv` (**601 rows**; the first 514 rows are byte-identical to the file the §3–§11 drafts were written on). Replaces nothing: the 514-row run stays in `work/tallies-3-11.md` for the record.

**Commands run (all from the repo root `research/potty-training-step1/`):**
1. `python3 work/3-11-src/cuts.py` — all cuts #1–#19 on 601 rows. Output is identical (`diff -q`) to the committed `work/3-11-src/cuts-output-601.txt`, so it is not repeated here; read that file for #1–#19.
2. `python3 work/2C-src/tally.py` — whole-bank tag counts, the locked-segment cut and the segment-B awareness split. Output is the "Output (verbatim)" block of `work/2C-tally.md` (re-run today; identical).
3. **New:** `python3 cuts_lock.py work/2C-databank.csv` — the same cuts as cuts.py #3–#16, run on the **locked school-age cut** (79 rows). Script and output below.
4. **New:** `python3 lookup.py work/2C-databank.csv` — every tag value side by side: bank 514 | bank 601 | segment B 161 | segment B 225 | locked 19 | locked 79. The "514/161/19" columns are computed on the first 514 rows of the same CSV, which reproduces the old run exactly (checked against `tallies-3-11.md` and the old 2C counts). Script and output below. A `*` marks a value whose bank count changed.

The two new scripts were run from a scratch directory (not added to `work/`); their full text is below, so they can be pasted into a file and re-run.

**Definitions:**
- **Segment B** = `buyer_group` contains "ND / sensory parent", "late-trainer parent" or "school-age accidents parent" → **225** rows (was 161).
- **Locked cut** = `buyer_group` contains "school-age accidents parent" (a parent describing their own ~5–9-year-old with daytime accidents) → **79** rows (was 19). This is the §11-locked customer.
- Multi-value cells are split on "; ".

**Caveats (still apply):** segment counts reflect search depth (the upstream wave was queried on school-age daytime accidents on purpose, so locked-cut counts are evidence volume, not market share). "Scam" is mostly UpAiry's checkout (#12: 15 of 19).

## Key 601-row numbers used in the §3–§11 refresh
| Metric | Bank 601 | Segment B 225 | Locked 79 |
|---|---|---|---|
| Awareness problem / solution / product | 250 (42%) / 174 (29%) / 176 (29%) | 150 (67%) / 59 (26%) / 16 (7%) | 55 (70%) / 22 (28%) / 2 (3%) |
| Burned / skeptical rows | 74 (12%) | 10 (4%) | 2 (3%) |
| Fear / Apathy / Anger / Guilt | 66 / 44 / 86 / 15 | 40 / 23 / 7 / 8 | 24 / 7 / 4 / 0 |
| Quotes naming age 5–11 / 4 / toddler | 65 / 24 / 73 | — | 26 / 2 / 3 |
| Dad (buyer group) | 21 | 3 | 1 |
| Self-ref mom / dad in quote | 17 / 5 | — | 1 / 1 |
| Keyword: work / money / god / school / shame | 36 / 32 / 2 / 57 / 25 | 9 / 1 / 1 / 42 / 10 | 2 / 0 / 1 / 29 / 4 |
| Full-containment language (#16) | — | 30 | 6 |
| Tagged objections (rows with any) | 110 | — | 0 |
| Top venue | r/pottytraining 50 | r/Autism_Parenting 37 · r/Parenting 28 · What to Expect 20 | r/Parenting 16 · r/kindergarten 13 · Mumsnet 10 |

## Script — cuts_lock.py (locked-cut version of cuts.py #3–#16)
```python
# Locked-cut (school-age accidents parent, 79 rows) version of cuts.py sections #3-#16, plus bank-wide pct helpers.
# Run: python3 cuts_lock.py /home/user/NG/research/potty-training-step1/work/2C-databank.csv
import csv,collections,re,sys
R=list(csv.DictReader(open(sys.argv[1],encoding="utf-8"))); N=len(R)
sp=lambda v:[x.strip() for x in v.split(';') if x.strip()]
L=[r for r in R if 'school-age accidents parent' in sp(r['buyer_group'])]
def cnt(rows,col): return collections.Counter(v for r in rows for v in sp(r[col]))
print("N",N,"| locked cut rows:",len(L))
print("\n# L3 source types"); print(collections.Counter(r['source_type'] for r in L).most_common())
print("\n# L4 platform top 15"); print(collections.Counter(r['platform'] for r in L).most_common(15))
age510=re.compile(r"\b(5|6|7|8|9|10|11|five|six|seven|eight|nine|ten)(\.5)?[- ]?(y/?o|yo|year|years|yr)",re.I)
age4=re.compile(r"\b(4|four)(\.5| and a half)?[- ]?(y/?o|yo|year|years|yr)",re.I)
age23=re.compile(r"\b(2|3|two|three)(\.5| and a half)?[- ]?(y/?o|yo|year|years|yr)|toddler|\b\d\d ?(mo|month)",re.I)
print("\n# L6 age named: 5-11:",sum(bool(age510.search(r['quote'])) for r in L),"| 4:",sum(bool(age4.search(r['quote'])) for r in L),"| 2-3/toddler:",sum(bool(age23.search(r['quote'])) for r in L))
print("  dad in cut:",cnt(L,'buyer_group')['dad'])
gender={'mom/mother/mum/wife/her husband':re.compile(r"\b(mom|mother|mum|mama|my husband|wife)\b",re.I),'dad/father/my wife':re.compile(r"\b(dad|father|my wife)\b",re.I)}
for k,p in gender.items(): print("  self-ref",k,sum(bool(p.search(r['quote'])) for r in L))
kw={'work/job/full-time':r"\b(work|job|full[- ]time|office|shift)\b",'money/afford/expensive/budget':r"\b(afford|expensive|budget|money|cost|pay|\$)",'school/teacher/kindergarten':r"\b(school|teacher|kindergart|pre-?k|class)",'daycare/nursery':r"\b(daycare|day care|nursery|preschool)",'grandma/MIL/family judgment':r"\b(grandma|grandmother|mother[- ]in[- ]law|MIL|in-laws|my mom said|family)\b",'therapist/OT/ABA/doctor':r"\b(OT|ABA|therapist|pediatrician|doctor|paed|BCBA)\b",'god/church/pray/bless':r"\b(god|church|pray|bless)",'husband/partner/marriage':r"\b(husband|partner|marriage|DH)\b",'tired/exhausted/burn':r"\b(tired|exhaust|burn|wits|lose my mind|losing my mind)",'laundry/wash':r"\b(laundry|wash)",'shame/embarrass/judg':r"\b(shame|embarrass|judg|neglect|lazy)"}
print("\n# L7 keyword hits (locked cut)")
for k,p in kw.items():
    rx=re.compile(p,re.I); print(f"  {k}: {sum(bool(rx.search(r['quote'])) for r in L)}")
for col in ['pain','desire','need','objection','failed_solution','trigger','misconception','belief','emotional_state','awareness_stage','burned_skeptical','authority_trusted','buyer_group']:
    print(f"\n# L8 {col}"); print(cnt(L,col).most_common(25))
b=[r for r in L if r['burned_skeptical'].strip()]
print(f"\n# L burned rows: {len(b)} of {len(L)} ({100*len(b)/len(L):.0f}%)")
c=cnt(L,'emotional_state')
print("\n# L emotion %:"," · ".join(f"{k} {v} ({100*v/len(L):.0f}%)" for k,v in c.most_common()))
fc=re.compile(r"diaper|nappies|nappy|goodnite|goodnight|size 7|non[- ]?verbal|level 3|level 2",re.I)
ac=re.compile(r"accident|underwear|undies|pants|pee(s|d)? (his|her) pants|wet",re.I)
f=[r for r in L if fc.search(r['quote'])]; a=[r for r in L if ac.search(r['quote']) and not fc.search(r['quote'])]
print("\n# L16 full-containment:",len(f),"| accidents/underwear (no diaper words):",len(a),"| neither:",len(L)-len(f)-len(a))
```

## Output — cuts_lock.py on 601 rows (verbatim)
```
N 601 | locked cut rows: 79

# L3 source types
[('Reddit', 55), ('Forum', 18), ('YouTube comments', 4), ('TikTok comments', 1), ('Amazon', 1)]

# L4 platform top 15
[('Reddit r/Parenting', 16), ('Reddit r/kindergarten', 13), ('Mumsnet', 10), ('BabyCenter Community', 5), ('Reddit r/pottytraining', 4), ('Reddit r/Preschoolers', 4), ('Reddit r/Autism_Parenting', 4), ('YouTube (What four things should you consider in a daytime wetting child?)', 4), ('Reddit r/ADHDparenting', 3), ('Reddit r/Mommit', 3), ('Reddit r/ParentingADHD', 2), ('Reddit r/toddlers', 1), ('TikTok', 1), ('Reddit r/breakingmom', 1), ('Reddit r/AskParents', 1)]

# L6 age named: 5-11: 26 | 4: 2 | 2-3/toddler: 3
  dad in cut: 1
  self-ref mom/mother/mum/wife/her husband 1
  self-ref dad/father/my wife 1

# L7 keyword hits (locked cut)
  work/job/full-time: 2
  money/afford/expensive/budget: 0
  school/teacher/kindergarten: 29
  daycare/nursery: 0
  grandma/MIL/family judgment: 0
  therapist/OT/ABA/doctor: 0
  god/church/pray/bless: 1
  husband/partner/marriage: 0
  tired/exhausted/burn: 1
  laundry/wash: 0
  shame/embarrass/judg: 4

# L8 pain
[('daily accidents at school/daycare', 34), ('constant accidents', 16), ("child doesn't notice wet / body signals", 8), ('late training (3.5y+ still not trained)', 7), ('deadline pressure (daycare/school rule)', 7), ('regression', 7), ('parent burnout', 4), ('withholding / poop refusal', 3), ('judgment / shame from others', 3), ('night wetting', 2), ('child shame / embarrassment', 2), ('fear child will be teased', 2), ('child refuses', 1), ('daily accidents at school age', 1), ('sensory discomfort', 1), ('laundry / mess', 1), ('child afraid to ask at school', 1), ('leaks / soaked after one pee', 1), ("child can't communicate need", 1), ('limited time (working parent)', 1)]

# L8 desire
[('daycare/school-ready', 8), ('child dignity / real underwear', 2), ('independence (pull on/off herself)', 2)]

# L8 need
[('routine / reminder system', 7), ('spare-clothes kit for school', 4), ('absorbency that holds a pee', 2), ('discreet', 2), ('feel-wet signal', 1), ('real-underwear look with protection', 1), ('bigger sizes', 1), ('fun designs', 1)]

# L8 objection
[]

# L8 failed_solution
[('Miralax / medical', 4), ('Pull-Ups / disposables', 4), ('tried everything', 2), ('training underwear (generic)', 1), ('diapers / nappies', 1), ('Goodnites', 1)]

# L8 trigger
[('school start (K/Reception)', 10), ('daycare/preschool deadline', 4), ('school/teacher complaint', 4), ('school says back to nappies', 2), ('accidents at school', 1), ('relative judgment', 1)]

# L8 misconception
[('pull-ups at 4.5 = neglect', 1)]

# L8 belief
[('constipation causes accidents', 6), ('readiness matters', 1)]

# L8 emotional_state
[('Neutrality', 30), ('Fear', 24), ('Apathy', 7), ('Acceptance', 5), ('Anger', 4), ('Pride', 4), ('Grief', 2), ('Willingness', 1), ('Desire', 1), ('Courage', 1)]

# L8 awareness_stage
[('problem', 55), ('solution', 22), ('product', 2)]

# L8 burned_skeptical
[('tried everything', 1), ('nothing works', 1)]

# L8 authority_trusted
[('pediatric urologist', 3), ('pediatrician', 3), ('other parents', 2), ('pelvic floor PT', 1), ('continence charity (ERIC)', 1)]

# L8 buyer_group
[('school-age accidents parent', 79), ('ND / sensory parent', 16), ('working parent / daycare', 7), ('withholding parent', 3), ('late-trainer parent', 1), ('dad', 1)]

# L burned rows: 2 of 79 (3%)

# L emotion %: Neutrality 30 (38%) · Fear 24 (30%) · Apathy 7 (9%) · Acceptance 5 (6%) · Anger 4 (5%) · Pride 4 (5%) · Grief 2 (3%) · Willingness 1 (1%) · Desire 1 (1%) · Courage 1 (1%)

# L16 full-containment: 6 | accidents/underwear (no diaper words): 59 | neither: 14
```

## Script — lookup.py (side-by-side counts, old vs new, bank / segment B / locked)
```python
# Side-by-side counts per tag value: bank514 | bank601 | segB514 | segB601 | lock514 | lock601
import csv,collections,sys
sp=lambda v:[x.strip() for x in v.split(';') if x.strip()]
R=list(csv.DictReader(open(sys.argv[1],encoding="utf-8")))
O=R[:514]
SEG={'ND / sensory parent','late-trainer parent','school-age accidents parent'}
def segs(rows): return rows,[r for r in rows if SEG&set(sp(r['buyer_group']))],[r for r in rows if 'school-age accidents parent' in sp(r['buyer_group'])]
bo,so,lo=segs(O); bn,sn,ln=segs(R)
cols=["pain","desire","need","objection","failed_solution","trigger","misconception","belief","emotional_state","awareness_stage","burned_skeptical","authority_trusted","buyer_group"]
def c(rows,col): return collections.Counter(v for r in rows for v in sp(r[col]))
print("col | value | bank514 | bank601 | segB161 | segB225 | lock19 | lock79")
for col in cols:
    C=[c(x,col) for x in (bo,bn,so,sn,lo,ln)]
    for v,_ in C[1].most_common():
        vals=[x.get(v,0) for x in C]
        flag=" *" if vals[0]!=vals[1] else ""
        print(f"{col} | {v} | "+" | ".join(map(str,vals))+flag)
```

## Output — lookup.py (verbatim; columns: bank514 | bank601 | segB161 | segB225 | lock19 | lock79)
```
col | value | bank514 | bank601 | segB161 | segB225 | lock19 | lock79
pain | late training (3.5y+ still not trained) | 70 | 74 | 70 | 74 | 3 | 7 *
pain | leaks / soaked after one pee | 54 | 55 | 2 | 3 | 0 | 1 *
pain | deadline pressure (daycare/school rule) | 41 | 41 | 19 | 19 | 7 | 7
pain | daily accidents at school/daycare | 21 | 38 | 18 | 34 | 18 | 34 *
pain | parent burnout | 31 | 34 | 9 | 12 | 1 | 4 *
pain | judgment / shame from others | 26 | 30 | 13 | 14 | 2 | 3 *
pain | withholding / poop refusal | 29 | 29 | 12 | 12 | 3 | 3
pain | night wetting | 27 | 29 | 2 | 4 | 0 | 2 *
pain | child doesn't notice wet / body signals | 22 | 28 | 15 | 20 | 3 | 8 *
pain | regression | 17 | 24 | 0 | 7 | 0 | 7 *
pain | parent guilt | 19 | 19 | 8 | 8 | 0 | 0
pain | size / big-kid products | 18 | 18 | 11 | 11 | 0 | 0
pain | leaks / soaked bed at night | 18 | 18 | 2 | 2 | 0 | 0
pain | constant accidents | 2 | 18 | 0 | 16 | 0 | 16 *
pain | child refuses | 17 | 17 | 13 | 13 | 1 | 1
pain | sensory discomfort | 15 | 17 | 14 | 16 | 0 | 1 *
pain | sizing / fit problems | 17 | 17 | 3 | 3 | 0 | 0
pain | laundry / mess | 14 | 15 | 1 | 2 | 0 | 1 *
pain | cost / money drain | 14 | 14 | 4 | 4 | 0 | 0
pain | hidden subscription / billing | 14 | 14 | 0 | 0 | 0 | 0
pain | child shame / embarrassment | 10 | 13 | 1 | 3 | 0 | 2 *
pain | child can't communicate need | 11 | 12 | 11 | 12 | 0 | 1 *
pain | daycare pull-up/underwear rules | 10 | 10 | 0 | 0 | 0 | 0
pain | fear child will be teased | 2 | 6 | 1 | 3 | 0 | 2 *
pain | poop accidents messy | 6 | 6 | 1 | 1 | 0 | 0
pain | limited time (working parent) | 4 | 5 | 0 | 1 | 0 | 1 *
pain | daycare vs home inconsistency | 4 | 4 | 1 | 1 | 0 | 0
pain | slow shipping | 4 | 4 | 1 | 1 | 0 | 0
pain | outings / public accidents | 3 | 3 | 0 | 0 | 0 | 0
pain | stress of training | 3 | 3 | 0 | 0 | 0 | 0
pain | parent shame / embarrassment | 2 | 2 | 0 | 0 | 0 | 0
pain | can't access specialist help | 2 | 2 | 2 | 2 | 0 | 0
pain | poor quality | 2 | 2 | 0 | 0 | 0 | 0
pain | child refuses product | 2 | 2 | 1 | 1 | 0 | 0
pain | marriage strain | 2 | 2 | 0 | 0 | 0 | 0
pain | refund not honoured | 2 | 2 | 0 | 0 | 0 | 0
pain | child refuses underwear | 1 | 1 | 0 | 0 | 0 | 0
pain | small leaks after training | 1 | 1 | 0 | 0 | 0 | 0
pain | power struggle | 1 | 1 | 1 | 1 | 0 | 0
pain | punishment backfires | 1 | 1 | 0 | 0 | 0 | 0
pain | stuck at home during training | 1 | 1 | 0 | 0 | 0 | 0
pain | doesn't hold pee | 1 | 1 | 0 | 0 | 0 | 0
pain | cheap brands don't hold | 1 | 1 | 0 | 0 | 0 | 0
pain | hidden subscription | 1 | 1 | 1 | 1 | 0 | 0
pain | daily accidents at school age | 1 | 1 | 1 | 1 | 1 | 1
pain | no resources for older / ND kids | 1 | 1 | 1 | 1 | 0 | 0
pain | size / big kid output | 1 | 1 | 1 | 1 | 0 | 0
pain | pressure on child | 1 | 1 | 0 | 0 | 0 | 0
pain | no resources for older kids | 1 | 1 | 1 | 1 | 0 | 0
pain | child holds until pull-up on | 1 | 1 | 1 | 1 | 0 | 0
pain | consistency hard for busy parent | 1 | 1 | 1 | 1 | 0 | 0
pain | long timeline | 1 | 1 | 1 | 1 | 0 | 0
pain | comparison to peers | 1 | 1 | 1 | 1 | 0 | 0
pain | new sibling | 1 | 1 | 0 | 0 | 0 | 0
pain | can't access doctor | 1 | 1 | 0 | 0 | 0 | 0
pain | child afraid to ask at school | 0 | 1 | 0 | 1 | 0 | 1 *
desire | dry nights | 43 | 43 | 4 | 4 | 0 | 0
desire | daycare/school-ready | 38 | 39 | 18 | 19 | 7 | 8 *
desire | less mess / cleanup | 28 | 29 | 2 | 3 | 0 | 0 *
desire | no-pressure process | 19 | 19 | 7 | 7 | 0 | 0
desire | child learns from feeling wet | 15 | 15 | 1 | 1 | 0 | 0
desire | independence (pull on/off herself) | 6 | 10 | 0 | 2 | 0 | 2 *
desire | child dignity / real underwear | 7 | 9 | 1 | 2 | 1 | 2 *
desire | protection out in public | 4 | 4 | 0 | 0 | 0 | 0
desire | daycare-approved | 3 | 3 | 0 | 0 | 0 | 0
desire | out of diapers / independence | 3 | 3 | 0 | 0 | 0 | 0
desire | big-kid underwear feeling | 3 | 3 | 0 | 0 | 0 | 0
desire | fun designs kid wants to wear | 3 | 3 | 0 | 0 | 0 | 0
desire | sleepovers without shame | 2 | 2 | 0 | 0 | 0 | 0
desire | dry bed | 2 | 2 | 0 | 0 | 0 | 0
desire | backup after training | 2 | 2 | 0 | 0 | 0 | 0
desire | off pull-ups | 2 | 2 | 0 | 0 | 0 | 0
desire | real-underwear look with protection | 2 | 2 | 0 | 0 | 0 | 0
desire | child-led readiness | 2 | 2 | 2 | 2 | 0 | 0
desire | faster training | 2 | 2 | 0 | 0 | 0 | 0
desire | body awareness (register need to go) | 2 | 2 | 0 | 0 | 0 | 0
desire | protection for almost-accidents | 1 | 1 | 0 | 0 | 0 | 0
desire | fewer outfit changes | 1 | 1 | 0 | 0 | 0 | 0
desire | child picks own pair | 1 | 1 | 0 | 0 | 0 | 0
desire | child confidence | 1 | 1 | 0 | 0 | 0 | 0
desire | child wants to wear them | 1 | 1 | 0 | 0 | 0 | 0
desire | comfort on sensitive skin | 1 | 1 | 1 | 1 | 0 | 0
desire | buys time to reach potty | 1 | 1 | 0 | 0 | 0 | 0
desire | dignity / looks like pants | 1 | 1 | 0 | 0 | 0 | 0
desire | daycare on board | 1 | 1 | 0 | 0 | 0 | 0
desire | less mess at daycare | 1 | 1 | 0 | 0 | 0 | 0
desire | train over a weekend | 1 | 1 | 0 | 0 | 0 | 0
desire | calm no-pressure process | 1 | 1 | 0 | 0 | 0 | 0
desire | leave the house | 1 | 1 | 0 | 0 | 0 | 0
desire | less stress | 1 | 1 | 0 | 0 | 0 | 0
desire | support during training | 1 | 1 | 0 | 0 | 0 | 0
desire | real underwear look | 1 | 1 | 0 | 0 | 0 | 0
desire | training on the go | 1 | 1 | 0 | 0 | 0 | 0
desire | feel wet without the mess | 1 | 1 | 0 | 0 | 0 | 0
desire | method that fits my child | 1 | 1 | 1 | 1 | 0 | 0
desire | next step after pull-ups | 1 | 1 | 0 | 0 | 0 | 0
desire | reusable / lasts | 1 | 1 | 0 | 0 | 0 | 0
desire | help for older kids | 1 | 1 | 1 | 1 | 0 | 0
desire | something that works | 1 | 1 | 1 | 1 | 0 | 0
desire | feel like a good parent | 1 | 1 | 1 | 1 | 0 | 0
desire | relief / patience | 1 | 1 | 1 | 1 | 0 | 0
desire | school-ready without pressure | 1 | 1 | 1 | 1 | 0 | 0
desire | consistent at daycare | 1 | 1 | 1 | 1 | 0 | 0
desire | daycare-ready | 1 | 1 | 0 | 0 | 0 | 0
desire | train before back to work | 1 | 1 | 0 | 0 | 0 | 0
need | absorbency that holds a pee | 101 | 104 | 8 | 11 | 1 | 2 *
need | feel-wet signal | 43 | 43 | 10 | 10 | 1 | 1
need | bigger sizes | 23 | 24 | 15 | 16 | 0 | 1 *
need | leakproof at night | 23 | 23 | 3 | 3 | 0 | 0
need | daycare-friendly | 19 | 19 | 1 | 1 | 0 | 0
need | sensory-friendly fit | 15 | 16 | 15 | 16 | 0 | 0 *
need | routine / reminder system | 7 | 14 | 6 | 11 | 2 | 7 *
need | reliable sizing / fit | 14 | 14 | 1 | 1 | 0 | 0
need | honest checkout | 13 | 13 | 1 | 1 | 0 | 0
need | fun designs | 10 | 11 | 0 | 1 | 0 | 1 *
need | discreet | 6 | 10 | 1 | 3 | 1 | 2 *
need | washable / reusable | 9 | 9 | 0 | 0 | 0 | 0
need | resources for older / ND kids | 7 | 7 | 7 | 7 | 0 | 0
need | easy pull up/down | 7 | 7 | 0 | 0 | 0 | 0
need | spare-clothes kit for school | 0 | 7 | 0 | 4 | 0 | 4 *
need | waterproof cover layer | 6 | 6 | 0 | 0 | 0 | 0
need | durable / washable | 4 | 4 | 0 | 0 | 0 | 0
need | layered protection | 4 | 4 | 0 | 0 | 0 | 0
need | real-underwear look with protection | 2 | 3 | 0 | 1 | 0 | 1 *
need | real-underwear feel | 3 | 3 | 0 | 0 | 0 | 0
need | wetness indicator | 2 | 2 | 0 | 0 | 0 | 0
need | affordable | 2 | 2 | 2 | 2 | 0 | 0
need | easy poop cleanup | 2 | 2 | 1 | 1 | 0 | 0
need | front absorbency (boys) | 1 | 1 | 0 | 0 | 0 | 0
need | soft | 1 | 1 | 0 | 0 | 0 | 0
need | absorbency for dribbles | 1 | 1 | 0 | 0 | 0 | 0
need | nap protection | 1 | 1 | 0 | 0 | 0 | 0
need | protection out in public | 1 | 1 | 0 | 0 | 0 | 0
need | breathable | 1 | 1 | 0 | 0 | 0 | 0
need | returns / guarantee | 1 | 1 | 0 | 0 | 0 | 0
need | school accommodation | 0 | 1 | 0 | 0 | 0 | 0 *
objection | won't hold pee / leaks | 47 | 47 | 2 | 2 | 0 | 0
objection | scam / hidden subscription | 16 | 16 | 1 | 1 | 0 | 0
objection | waste of money | 15 | 15 | 0 | 0 | 0 | 0
objection | holds only one small accident | 14 | 14 | 0 | 0 | 0 | 0
objection | sizing / fit uncertain | 13 | 13 | 2 | 2 | 0 | 0
objection | price | 10 | 10 | 2 | 2 | 0 | 0
objection | feels like a diaper | 5 | 5 | 0 | 0 | 0 | 0
objection | skeptical of brand / reviews | 5 | 5 | 0 | 0 | 0 | 0
objection | shipped from China | 5 | 5 | 1 | 1 | 0 | 0
objection | quality | 3 | 3 | 0 | 0 | 0 | 0
objection | no better than regular underwear | 3 | 3 | 0 | 0 | 0 | 0
objection | not needed | 2 | 2 | 0 | 0 | 0 | 0
objection | guarantee not honoured | 2 | 2 | 0 | 0 | 0 | 0
objection | shipping time | 2 | 2 | 0 | 0 | 0 | 0
objection | ads overpromise | 2 | 2 | 0 | 0 | 0 | 0
objection | returns cost | 1 | 1 | 0 | 0 | 0 | 0
objection | not worth it | 1 | 1 | 0 | 0 | 0 | 0
objection | big brand let down | 1 | 1 | 0 | 0 | 0 | 0
objection | only useful late in training | 1 | 1 | 0 | 0 | 0 | 0
objection | may not work for my kid | 1 | 1 | 1 | 1 | 0 | 0
objection | may slow training | 1 | 1 | 1 | 1 | 0 | 0
objection | category is a scam | 1 | 1 | 0 | 0 | 0 | 0
objection | not worth the price | 1 | 1 | 0 | 0 | 0 | 0
objection | will leak out the front | 1 | 1 | 1 | 1 | 0 | 0
objection | poop cleanup | 1 | 1 | 0 | 0 | 0 | 0
failed_solution | Pull-Ups / disposables | 61 | 67 | 8 | 12 | 0 | 4 *
failed_solution | training underwear (UpAiry) | 27 | 27 | 1 | 1 | 0 | 0
failed_solution | 3-day / Oh Crap method | 23 | 23 | 4 | 4 | 0 | 0
failed_solution | training underwear (generic) | 22 | 22 | 6 | 6 | 1 | 1
failed_solution | training underwear (MooMoo) | 13 | 13 | 2 | 2 | 0 | 0
failed_solution | training underwear (BIG ELEPHANT) | 11 | 11 | 1 | 1 | 0 | 0
failed_solution | rewards / stickers / bribes | 8 | 8 | 4 | 4 | 0 | 0
failed_solution | training underwear (other brand) | 8 | 8 | 0 | 0 | 0 | 0
failed_solution | tried everything | 4 | 6 | 1 | 3 | 0 | 2 *
failed_solution | Miralax / medical | 2 | 6 | 0 | 4 | 0 | 4 *
failed_solution | Goodnites | 4 | 5 | 2 | 3 | 0 | 1 *
failed_solution | gadgets (seats, potties, books) | 3 | 3 | 1 | 1 | 0 | 0
failed_solution | regular underwear | 2 | 2 | 0 | 0 | 0 | 0
failed_solution | training underwear (Gerber) | 2 | 2 | 0 | 0 | 0 | 0
failed_solution | naked method | 2 | 2 | 0 | 0 | 0 | 0
failed_solution | training underwear (Hanes) | 2 | 2 | 0 | 0 | 0 | 0
failed_solution | potty watch | 1 | 1 | 0 | 0 | 0 | 0
failed_solution | regular character underwear | 1 | 1 | 0 | 0 | 0 | 0
failed_solution | diapers / nappies | 1 | 1 | 1 | 1 | 1 | 1
failed_solution | punishment | 1 | 1 | 0 | 0 | 0 | 0
failed_solution | cheap training underwear | 1 | 1 | 0 | 0 | 0 | 0
failed_solution | diapers at night | 1 | 1 | 0 | 0 | 0 | 0
failed_solution | rewards / games | 1 | 1 | 0 | 0 | 0 | 0
trigger | daycare/preschool deadline | 31 | 31 | 10 | 10 | 4 | 4
trigger | school start (K/Reception) | 11 | 20 | 9 | 16 | 3 | 10 *
trigger | daycare pull-up/underwear rules | 11 | 11 | 0 | 0 | 0 | 0
trigger | relative judgment | 9 | 10 | 4 | 5 | 0 | 1 *
trigger | soaked bed | 9 | 9 | 2 | 2 | 0 | 0
trigger | school/teacher complaint | 3 | 6 | 3 | 5 | 2 | 4 *
trigger | outgrew largest size | 4 | 4 | 2 | 2 | 0 | 0
trigger | new sibling | 4 | 4 | 0 | 0 | 0 | 0
trigger | 3-day weekend attempt | 4 | 4 | 0 | 0 | 0 | 0
trigger | sleepover invite | 2 | 2 | 0 | 0 | 0 | 0
trigger | back to work | 2 | 2 | 2 | 2 | 0 | 0
trigger | accidents at preschool | 2 | 2 | 0 | 0 | 0 | 0
trigger | school says back to nappies | 2 | 2 | 2 | 2 | 2 | 2
trigger | seeing ads | 2 | 2 | 0 | 0 | 0 | 0
trigger | about to start training | 2 | 2 | 0 | 0 | 0 | 0
trigger | one painful poop | 1 | 1 | 0 | 0 | 0 | 0
trigger | holiday break / planned start | 1 | 1 | 0 | 0 | 0 | 0
trigger | child asks for underwear | 1 | 1 | 1 | 1 | 0 | 0
trigger | after 3-day method | 1 | 1 | 0 | 0 | 0 | 0
trigger | weekend training before daycare Monday | 1 | 1 | 0 | 0 | 0 | 0
trigger | cabin fever during training | 1 | 1 | 0 | 0 | 0 | 0
trigger | bought from social media ad | 1 | 1 | 0 | 0 | 0 | 0
trigger | diaper size outgrown | 1 | 1 | 1 | 1 | 0 | 0
trigger | child takes diaper off | 1 | 1 | 0 | 0 | 0 | 0
trigger | started kindergarten | 1 | 1 | 1 | 1 | 0 | 0
trigger | going back to work | 1 | 1 | 0 | 0 | 0 | 0
trigger | accidents at school | 0 | 1 | 0 | 1 | 0 | 1 *
misconception | late training = lazy parenting | 3 | 4 | 2 | 2 | 0 | 0 *
misconception | should be trained by 2/3 | 4 | 4 | 0 | 0 | 0 | 0
misconception | 3 days is enough | 4 | 4 | 1 | 1 | 0 | 0
misconception | untrained at 5 = severe delay | 1 | 2 | 0 | 0 | 0 | 0 *
misconception | special underwear speeds training | 2 | 2 | 0 | 0 | 0 | 0
misconception | missed the window | 1 | 1 | 1 | 1 | 0 | 0
misconception | pull-ups at 4.5 = neglect | 1 | 1 | 1 | 1 | 1 | 1
misconception | training underwear should catch everything | 1 | 1 | 0 | 0 | 0 | 0
misconception | leak proof training underwear exists | 1 | 1 | 0 | 0 | 0 | 0
misconception | pricier = leakproof | 1 | 1 | 0 | 0 | 0 | 0
misconception | just potty train him | 1 | 1 | 1 | 1 | 0 | 0
misconception | it's very easy | 1 | 1 | 0 | 0 | 0 | 0
misconception | readiness is an excuse | 1 | 1 | 0 | 0 | 0 | 0
belief | feeling wet teaches the child | 25 | 25 | 1 | 1 | 0 | 0
belief | every kid own timeline | 10 | 13 | 8 | 8 | 0 | 0 *
belief | pull-ups are just diapers | 13 | 13 | 1 | 1 | 0 | 0
belief | constipation causes accidents | 6 | 12 | 3 | 7 | 2 | 6 *
belief | readiness matters | 9 | 10 | 5 | 6 | 0 | 1 *
belief | no shame approach | 6 | 9 | 2 | 3 | 0 | 0 *
belief | pull-ups hide the wet | 8 | 8 | 1 | 1 | 0 | 0
belief | methods don't work for ND kids | 6 | 6 | 6 | 6 | 0 | 0
belief | ads overpromise | 5 | 5 | 0 | 0 | 0 | 0
belief | pull-ups cause regression | 3 | 3 | 0 | 0 | 0 | 0
belief | consistency / schedule works | 2 | 2 | 2 | 2 | 0 | 0
belief | pressure backfires | 2 | 2 | 0 | 0 | 0 | 0
belief | fake reviews everywhere | 2 | 2 | 0 | 0 | 0 | 0
belief | night dryness is developmental | 1 | 1 | 0 | 0 | 0 | 0
belief | learning not training | 1 | 1 | 0 | 0 | 0 | 0
belief | commit and it goes fast | 1 | 1 | 0 | 0 | 0 | 0
belief | pull-ups help early training | 1 | 1 | 0 | 0 | 0 | 0
belief | all training pants are kind of a scam | 1 | 1 | 0 | 0 | 0 | 0
belief | reviews from other parents | 1 | 1 | 0 | 0 | 0 | 0
belief | cheaper alternatives are the same | 1 | 1 | 0 | 0 | 0 | 0
belief | you get what you pay for | 1 | 1 | 0 | 0 | 0 | 0
belief | reviews + easy returns lower risk | 1 | 1 | 0 | 0 | 0 | 0
belief | cheaper options work just as well | 1 | 1 | 0 | 0 | 0 | 0
belief | 3-day method only fits stay-at-home parents | 1 | 1 | 0 | 0 | 0 | 0
belief | nothing works | 1 | 1 | 1 | 1 | 0 | 0
belief | child can't help it | 0 | 1 | 0 | 0 | 0 | 0 *
emotional_state | Neutrality | 190 | 223 | 88 | 107 | 13 | 30 *
emotional_state | Pride | 81 | 86 | 8 | 13 | 0 | 4 *
emotional_state | Anger | 80 | 86 | 4 | 7 | 1 | 4 *
emotional_state | Fear | 43 | 66 | 18 | 40 | 2 | 24 *
emotional_state | Apathy | 39 | 44 | 18 | 23 | 2 | 7 *
emotional_state | Acceptance | 17 | 26 | 7 | 12 | 1 | 5 *
emotional_state | Desire | 17 | 18 | 2 | 3 | 0 | 1 *
emotional_state | Shame | 15 | 15 | 3 | 3 | 0 | 0
emotional_state | Guilt | 15 | 15 | 8 | 8 | 0 | 0
emotional_state | Grief | 9 | 11 | 2 | 4 | 0 | 2 *
emotional_state | Willingness | 7 | 8 | 3 | 4 | 0 | 1 *
emotional_state | Courage | 1 | 3 | 0 | 1 | 0 | 1 *
awareness_stage | problem | 195 | 250 | 108 | 150 | 15 | 55 *
awareness_stage | product | 173 | 176 | 13 | 16 | 0 | 2 *
awareness_stage | solution | 145 | 174 | 40 | 59 | 4 | 22 *
awareness_stage | unaware | 1 | 1 | 0 | 0 | 0 | 0
burned_skeptical | waste of money | 34 | 34 | 0 | 0 | 0 | 0
burned_skeptical | scam | 19 | 19 | 1 | 1 | 0 | 0
burned_skeptical | nothing works | 14 | 15 | 4 | 5 | 0 | 1 *
burned_skeptical | tried everything | 7 | 8 | 3 | 4 | 0 | 1 *
burned_skeptical | skeptical | 3 | 4 | 0 | 0 | 0 | 0 *
authority_trusted | other parents | 22 | 22 | 4 | 4 | 2 | 2
authority_trusted | daycare staff | 15 | 15 | 1 | 1 | 0 | 0
authority_trusted | creator with lived experience | 7 | 7 | 7 | 7 | 0 | 0
authority_trusted | pediatrician | 2 | 6 | 0 | 3 | 0 | 3 *
authority_trusted | occupational therapist | 4 | 4 | 3 | 3 | 0 | 0
authority_trusted | pediatric urologist | 0 | 3 | 0 | 3 | 0 | 3 *
authority_trusted | ABA therapist | 2 | 2 | 2 | 2 | 0 | 0
authority_trusted | daycare teacher experience | 1 | 2 | 0 | 0 | 0 | 0 *
authority_trusted | potty-training creator | 2 | 2 | 1 | 1 | 0 | 0
authority_trusted | influencer review | 2 | 2 | 0 | 0 | 0 | 0
authority_trusted | experienced childcare worker | 1 | 1 | 0 | 0 | 0 | 0
authority_trusted | nursery staff | 1 | 1 | 0 | 0 | 0 | 0
authority_trusted | experienced childcarer | 1 | 1 | 0 | 0 | 0 | 0
authority_trusted | Oh Crap method | 1 | 1 | 0 | 0 | 0 | 0
authority_trusted | autism consultant | 1 | 1 | 1 | 1 | 0 | 0
authority_trusted | OT creator | 1 | 1 | 0 | 0 | 0 | 0
authority_trusted | pediatrician (TikTok) | 1 | 1 | 0 | 0 | 0 | 0
authority_trusted | author / performance coach | 1 | 1 | 0 | 0 | 0 | 0
authority_trusted | pelvic floor PT | 0 | 1 | 0 | 1 | 0 | 1 *
authority_trusted | continence charity (ERIC) | 0 | 1 | 0 | 1 | 0 | 1 *
buyer_group | general toddler parent | 199 | 199 | 0 | 0 | 0 | 0
buyer_group | ND / sensory parent | 117 | 132 | 117 | 132 | 5 | 16 *
buyer_group | school-age accidents parent | 19 | 79 | 19 | 79 | 19 | 79 *
buyer_group | late-trainer parent | 64 | 64 | 64 | 64 | 1 | 1
buyer_group | working parent / daycare | 61 | 61 | 20 | 20 | 7 | 7
buyer_group | night / bedwetting parent | 47 | 47 | 4 | 4 | 0 | 0
buyer_group | withholding parent | 28 | 28 | 11 | 11 | 3 | 3
buyer_group | commentator | 2 | 21 | 0 | 0 | 0 | 0 *
buyer_group | dad | 20 | 21 | 2 | 3 | 0 | 1 *
buyer_group | regression parent | 17 | 17 | 0 | 0 | 0 | 0
buyer_group | childcare worker | 12 | 12 | 0 | 0 | 0 | 0
buyer_group | twins parent | 11 | 11 | 2 | 2 | 0 | 0
buyer_group | eco / cloth parent | 9 | 9 | 0 | 0 | 0 | 0
buyer_group | grandparent / gift buyer | 9 | 9 | 1 | 1 | 0 | 0
buyer_group | school teacher | 0 | 4 | 0 | 0 | 0 | 0 *
buyer_group | teen / self | 1 | 1 | 0 | 0 | 0 | 0
buyer_group | single parent | 1 | 1 | 0 | 0 | 0 | 0
```

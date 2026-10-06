# Tallies for §3–§11 (writer A) — reproducible
Run on 2026-10-06 against `work/2C-databank.csv` (514 rows).

**Commands:**
- `python3 work/3-11-src/cuts.py > work/3-11-src/cuts-output.txt` — all cuts (#1–#19) below
- `python3 work/3-11-src/quotes.py <column> [K] [seg]` — dumps the top K quotes per tag value. Used to pick quotes. VERBATIM rows come first.
- `python3 work/3-11-src/addsrc.py <files>` — appends the cited data-bank rows (URL · platform · date · capture) to each section file
- A quote-integrity check (inline Python): every `"quote" [C:ID]` pair was checked as a substring of the row's text. 4 flags came back:
  - 3 were inner-quote-mark style only.
  - 1 was a mis-attribution (S229), now fixed.

**Definitions:**
- **Segment B** = rows whose `buyer_group` contains "ND / sensory parent", "late-trainer parent" or "school-age accidents parent". That's 161 rows.
- Multi-value cells are split on "; ".

**Caveats (from 2C-tally.md, still apply):**
- Segment counts partly reflect search depth: the ND / late / night queries were run harder.
- "Scam" is mostly UpAiry's checkout (#12 below confirms this: 15 of 19).

## Script — work/3-11-src/cuts.py
```python
# Cuts of work/2C-databank.csv for §3–§11 (writer A). Run: python3 work/3-11-src/cuts.py
import csv,collections,re,os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
R=list(csv.DictReader(open(os.path.join(B,"2C-databank.csv"),encoding="utf-8"))); N=len(R)
sp=lambda v:[x.strip() for x in v.split(';') if x.strip()]
SEG={'ND / sensory parent','late-trainer parent','school-age accidents parent'}
seg=[r for r in R if SEG & set(sp(r['buyer_group']))]
def cnt(rows,col): return collections.Counter(v for r in rows for v in sp(r[col]))
print("N",N,"| segment B (ND/sensory OR late-trainer OR school-age) rows:",len(seg))
print("\n# 1 buyer_group (all)"); print(cnt(R,'buyer_group').most_common())
print("\n# 2 buyer_group overlap inside segment B"); print(cnt(seg,'buyer_group').most_common())
print("\n# 3 source types segment B"); print(collections.Counter(r['source_type'] for r in seg).most_common())
print("\n# 4 platform (subreddit) segment B top 15"); print(collections.Counter(r['platform'] for r in seg).most_common(15))
print("\n# 5 platform all top 25"); print(collections.Counter(r['platform'] for r in R).most_common(25))
age510=re.compile(r"\b(5|6|7|8|9|10|11|five|six|seven|eight|nine|ten)(\.5)?[- ]?(y/?o|yo|year|years|yr)",re.I)
age4=re.compile(r"\b(4|four)(\.5| and a half)?[- ]?(y/?o|yo|year|years|yr)",re.I)
age23=re.compile(r"\b(2|3|two|three)(\.5| and a half)?[- ]?(y/?o|yo|year|years|yr)|toddler|\b\d\d ?(mo|month)",re.I)
print("\n# 6 age named in quote: 5-11:",sum(bool(age510.search(r['quote'])) for r in R),"| 4:",sum(bool(age4.search(r['quote'])) for r in R),"| 2-3/toddler/months:",sum(bool(age23.search(r['quote'])) for r in R))
gender={'mom/mother/mum/wife/her husband':re.compile(r"\b(mom|mother|mum|mama|my husband|wife)\b",re.I),'dad/father/my wife':re.compile(r"\b(dad|father|my wife)\b",re.I)}
for k,p in gender.items(): print("  self-ref",k,sum(bool(p.search(r['quote'])) for r in R))
print("  buyer_group dad:",cnt(R,'buyer_group')['dad'],"| single parent:",cnt(R,'buyer_group')['single parent'])
kw={'work/job/full-time':r"\b(work|job|full[- ]time|office|shift)\b",'money/afford/expensive/budget':r"\b(afford|expensive|budget|money|cost|pay|\$)",'school/teacher/kindergarten':r"\b(school|teacher|kindergart|pre-?k|class)",'daycare/nursery':r"\b(daycare|day care|nursery|preschool)",'grandma/MIL/family judgment':r"\b(grandma|grandmother|mother[- ]in[- ]law|MIL|in-laws|my mom said|family)\b",'therapist/OT/ABA/doctor':r"\b(OT|ABA|therapist|pediatrician|doctor|paed|BCBA)\b",'god/church/pray/bless':r"\b(god|church|pray|bless)",'husband/partner/marriage':r"\b(husband|partner|marriage|DH)\b",'tired/exhausted/burn':r"\b(tired|exhaust|burn|wits|lose my mind|losing my mind)",'laundry/wash':r"\b(laundry|wash)",'shame/embarrass/judg':r"\b(shame|embarrass|judg|neglect|lazy)"}
print("\n# 7 keyword hits (all | segment B)")
for k,p in kw.items():
    rx=re.compile(p,re.I); print(f"  {k}: {sum(bool(rx.search(r['quote'])) for r in R)} | {sum(bool(rx.search(r['quote'])) for r in seg)}")
for col in ['pain','desire','need','objection','failed_solution','trigger','misconception','belief','emotional_state','awareness_stage','burned_skeptical','authority_trusted']:
    print(f"\n# 8 {col} — segment B"); print(cnt(seg,col).most_common(20))
print("\n# 9 awareness split segment B (%)")
c=cnt(seg,'awareness_stage')
for k in ['unaware','problem','solution','product','most']: print(f"  {k}: {c.get(k,0)} ({100*c.get(k,0)/len(seg):.0f}%)")
print("\n# 10 stars by source for objection rows"); obj=[r for r in R if r['objection'].strip()]
print("  objection rows",len(obj),"| with stars 1-2:",sum(r['stars'] in('1','2') for r in obj),"| 4-5:",sum(r['stars'] in ('4','5') for r in obj))
print("  objection rows by source:",collections.Counter(r['source_type'] for r in obj).most_common())
print("\n# 11 failed_solution × capture/stars")
for fs,n in cnt(R,'failed_solution').most_common(10):
    rows=[r for r in R if fs in sp(r['failed_solution'])]
    print(f"  {fs}: {n} | 1-2★ {sum(r['stars'] in('1','2') for r in rows)} | 4-5★ {sum(r['stars'] in('4','5') for r in rows)} | Anger {sum('Anger' in r['emotional_state'] for r in rows)} | burned {sum(bool(r['burned_skeptical'].strip()) for r in rows)}")
print("\n# 12 burned/skeptical × source"); b=[r for r in R if r['burned_skeptical'].strip()]
print(" ",collections.Counter(r['source_type'] for r in b).most_common())
print("  'scam' rows mentioning upairy/subscription/gummies:",sum(1 for r in R if 'scam' in r['burned_skeptical'] and re.search(r"upairy|subscri|gumm|charg",r['quote']+r['url'],re.I)),"of",cnt(R,'burned_skeptical')['scam'])
print("\n# 13 UpAiry-related rows (url or quote mentions upairy):",sum(1 for r in R if re.search('upairy',r['quote']+r['url'],re.I)))
print("\n# 14 general toddler parent: awareness split")
g=[r for r in R if 'general toddler parent' in sp(r['buyer_group'])]; c=cnt(g,'awareness_stage'); print(" ",len(g),dict(c))
print("\n# 15 objection — segment-B-relevant cuts (all rows whose quote names age 4+ or bigger sizes)")
big=[r for r in R if age510.search(r['quote']) or age4.search(r['quote']) or 'bigger sizes' in r['need'] or 'size / big-kid products' in r['pain']]
print("  rows",len(big)); print("  needs:",cnt(big,'need').most_common(10)); print("  failed:",cnt(big,'failed_solution').most_common(10)); print("  pains:",cnt(big,'pain').most_common(12))
print("\n# 16 segment B split: 'full containment' (diapers/nappies/Goodnites/size 7/nonverbal/level 3) vs 'accidents/underwear' language")
fc=re.compile(r"diaper|nappies|nappy|goodnite|goodnight|size 7|non[- ]?verbal|level 3|level 2",re.I)
ac=re.compile(r"accident|underwear|undies|pants|pee(s|d)? (his|her) pants|wet",re.I)
f=[r for r in seg if fc.search(r['quote'])]; a=[r for r in seg if ac.search(r['quote']) and not fc.search(r['quote'])]
print("  full-containment language:",len(f),"| accidents/underwear language (no diaper words):",len(a),"| neither:",len(seg)-len(f)-len(a))
print("\n# 17 ad-log leads_with (n=40)")
al=list(csv.DictReader(open(os.path.join(B,"ad-log.csv"),encoding="utf-8")))
print(" ",collections.Counter(r['leads_with'] for r in al).most_common())
for br in ['UpAiry','Kid Confident','BrightKidCo']:
    print(" ",br,collections.Counter(r['leads_with'] for r in al if r['brand'].startswith(br)).most_common(), "| formats:",collections.Counter(r['format'] for r in al if r['brand'].startswith(br)).most_common())
lr=[r for r in al if int(r['days_running'])>=100]
print("  ads running >=100 days:",len(lr),collections.Counter(r['leads_with'] for r in lr).most_common())
print("\n# 18 per buyer group: top platforms + top pain")
for g in ['general toddler parent','working parent / daycare','night / bedwetting parent','withholding parent','dad','regression parent','childcare worker','grandparent / gift buyer','twins parent','eco / cloth parent']:
    rows=[r for r in R if g in sp(r['buyer_group'])]
    print(f"  {g} ({len(rows)}): platforms {collections.Counter(r['platform'] for r in rows).most_common(4)} | pains {cnt(rows,'pain').most_common(3)} | awareness {dict(cnt(rows,'awareness_stage'))}")
print("\n# 19 ad-log hook words (n=40 hooks)")
for w in ['toddler','diaper','pull-up|pull ups|pull-ups','day|week','daycare|preschool|school','accident',r'\bI |\bmy |\bMy ']:
    print(f"  /{w}/: {sum(bool(re.search(w,r['hook_first_line'],re.I)) for r in al)} of {len(al)}")
```

## Output (verbatim)
```
N 514 | segment B (ND/sensory OR late-trainer OR school-age) rows: 161

# 1 buyer_group (all)
[('general toddler parent', 199), ('ND / sensory parent', 117), ('late-trainer parent', 64), ('working parent / daycare', 61), ('night / bedwetting parent', 47), ('withholding parent', 28), ('dad', 20), ('school-age accidents parent', 19), ('regression parent', 17), ('childcare worker', 12), ('twins parent', 11), ('eco / cloth parent', 9), ('grandparent / gift buyer', 9), ('commentator', 2), ('teen / self', 1), ('single parent', 1)]

# 2 buyer_group overlap inside segment B
[('ND / sensory parent', 117), ('late-trainer parent', 64), ('working parent / daycare', 20), ('school-age accidents parent', 19), ('withholding parent', 11), ('night / bedwetting parent', 4), ('twins parent', 2), ('dad', 2), ('grandparent / gift buyer', 1)]

# 3 source types segment B
[('Reddit', 88), ('Forum', 46), ('YouTube comments', 13), ('TikTok comments', 6), ('Retailer reviews', 2), ('Instagram comments', 2), ('Trustpilot', 2), ('Amazon', 1), ('Walmart', 1)]

# 4 platform (subreddit) segment B top 15
[('Reddit r/Autism_Parenting', 31), ('What to Expect', 20), ('Reddit r/Parenting', 15), ('YouTube (How I Potty Trained My Son with Autism)', 11), ('Reddit r/pottytraining', 10), ('Reddit r/toddlers', 9), ('Mumsnet', 8), ('BabyCenter', 6), ('TikTok', 6), ('Reddit r/ADHDparenting', 5), ('Reddit r/Preschoolers', 4), ('Reddit r/kindergarten', 3), ('Mumsnet SEN', 3), ('Reddit r/daddit', 2), ('Goodnites.com review', 2)]

# 5 platform all top 25
[('Reddit r/pottytraining', 48), ('Trustpilot (UpAiry)', 44), ('Reddit r/toddlers', 43), ('What to Expect', 42), ('Reddit r/Autism_Parenting', 31), ('Reddit r/Parenting', 28), ('Amazon (MooMoo Baby)', 24), ('Mumsnet', 20), ('Amazon (BIG ELEPHANT)', 20), ('Amazon (Gerber)', 19), ('Reddit r/daddit', 18), ('TikTok', 14), ('BabyCenter', 13), ('Reddit r/Mommit', 11), ('YouTube (How I Potty Trained My Son with Autism)', 11), ('Reddit r/Preschoolers', 9), ('X (Twitter)', 8), ('Reddit r/workingmoms', 7), ('Amazon (Hanes)', 7), ('Walmart (BIG ELEPHANT)', 7), ('YouTube (Mistake That Turns a Regression Into an Ongoing Problem)', 7), ('Reddit r/ECEProfessionals', 6), ('Goodnites.com review', 6), ('Reddit r/ADHDparenting', 5), ('Reddit r/breakingmom', 5)]

# 6 age named in quote: 5-11: 42 | 4: 24 | 2-3/toddler/months: 71
  self-ref mom/mother/mum/wife/her husband 17
  self-ref dad/father/my wife 4
  buyer_group dad: 20 | single parent: 1

# 7 keyword hits (all | segment B)
  work/job/full-time: 33 | 7
  money/afford/expensive/budget: 32 | 1
  school/teacher/kindergarten: 24 | 16
  daycare/nursery: 22 | 2
  grandma/MIL/family judgment: 2 | 0
  therapist/OT/ABA/doctor: 5 | 3
  god/church/pray/bless: 1 | 0
  husband/partner/marriage: 5 | 1
  tired/exhausted/burn: 10 | 5
  laundry/wash: 11 | 0
  shame/embarrass/judg: 19 | 7

# 8 pain — segment B
[('late training (3.5y+ still not trained)', 70), ('deadline pressure (daycare/school rule)', 19), ('daily accidents at school/daycare', 18), ("child doesn't notice wet / body signals", 15), ('sensory discomfort', 14), ('child refuses', 13), ('judgment / shame from others', 13), ('withholding / poop refusal', 12), ("child can't communicate need", 11), ('size / big-kid products', 11), ('parent burnout', 9), ('parent guilt', 8), ('cost / money drain', 4), ('sizing / fit problems', 3), ('night wetting', 2), ('leaks / soaked bed at night', 2), ("can't access specialist help", 2), ('leaks / soaked after one pee', 2), ('child shame / embarrassment', 1), ('fear child will be teased', 1)]

# 8 desire — segment B
[('daycare/school-ready', 18), ('no-pressure process', 7), ('dry nights', 4), ('less mess / cleanup', 2), ('child-led readiness', 2), ('child dignity / real underwear', 1), ('comfort on sensitive skin', 1), ('child learns from feeling wet', 1), ('method that fits my child', 1), ('help for older kids', 1), ('something that works', 1), ('feel like a good parent', 1), ('relief / patience', 1), ('school-ready without pressure', 1), ('consistent at daycare', 1)]

# 8 need — segment B
[('bigger sizes', 15), ('sensory-friendly fit', 15), ('feel-wet signal', 10), ('absorbency that holds a pee', 8), ('resources for older / ND kids', 7), ('routine / reminder system', 6), ('leakproof at night', 3), ('affordable', 2), ('discreet', 1), ('easy poop cleanup', 1), ('honest checkout', 1), ('reliable sizing / fit', 1), ('daycare-friendly', 1)]

# 8 objection — segment B
[('sizing / fit uncertain', 2), ('price', 2), ("won't hold pee / leaks", 2), ('may not work for my kid', 1), ('may slow training', 1), ('shipped from China', 1), ('scam / hidden subscription', 1), ('will leak out the front', 1)]

# 8 failed_solution — segment B
[('Pull-Ups / disposables', 8), ('training underwear (generic)', 6), ('rewards / stickers / bribes', 4), ('3-day / Oh Crap method', 4), ('training underwear (MooMoo)', 2), ('Goodnites', 2), ('gadgets (seats, potties, books)', 1), ('diapers / nappies', 1), ('training underwear (UpAiry)', 1), ('training underwear (BIG ELEPHANT)', 1), ('tried everything', 1)]

# 8 trigger — segment B
[('daycare/preschool deadline', 10), ('school start (K/Reception)', 9), ('relative judgment', 4), ('school/teacher complaint', 3), ('outgrew largest size', 2), ('soaked bed', 2), ('back to work', 2), ('school says back to nappies', 2), ('child asks for underwear', 1), ('diaper size outgrown', 1), ('started kindergarten', 1)]

# 8 misconception — segment B
[('late training = lazy parenting', 2), ('missed the window', 1), ('3 days is enough', 1), ('pull-ups at 4.5 = neglect', 1), ('just potty train him', 1)]

# 8 belief — segment B
[('every kid own timeline', 8), ("methods don't work for ND kids", 6), ('readiness matters', 5), ('constipation causes accidents', 3), ('consistency / schedule works', 2), ('no shame approach', 2), ('feeling wet teaches the child', 1), ('pull-ups hide the wet', 1), ('pull-ups are just diapers', 1), ('nothing works', 1)]

# 8 emotional_state — segment B
[('Neutrality', 88), ('Fear', 18), ('Apathy', 18), ('Pride', 8), ('Guilt', 8), ('Acceptance', 7), ('Anger', 4), ('Shame', 3), ('Willingness', 3), ('Desire', 2), ('Grief', 2)]

# 8 awareness_stage — segment B
[('problem', 108), ('solution', 40), ('product', 13)]

# 8 burned_skeptical — segment B
[('nothing works', 4), ('tried everything', 3), ('scam', 1)]

# 8 authority_trusted — segment B
[('creator with lived experience', 7), ('other parents', 4), ('occupational therapist', 3), ('ABA therapist', 2), ('autism consultant', 1), ('potty-training creator', 1), ('daycare staff', 1)]

# 9 awareness split segment B (%)
  unaware: 0 (0%)
  problem: 108 (67%)
  solution: 40 (25%)
  product: 13 (8%)
  most: 0 (0%)

# 10 stars by source for objection rows
  objection rows 110 | with stars 1-2: 30 | 4-5: 11
  objection rows by source: [('Amazon', 35), ('Trustpilot', 35), ('Reddit', 24), ('Forum', 6), ('Walmart', 5), ('Retailer reviews', 2), ('TikTok comments', 2), ('YouTube comments', 1)]

# 11 failed_solution × capture/stars
  Pull-Ups / disposables: 61 | 1-2★ 0 | 4-5★ 6 | Anger 10 | burned 4
  training underwear (UpAiry): 27 | 1-2★ 20 | 4-5★ 0 | Anger 25 | burned 25
  3-day / Oh Crap method: 23 | 1-2★ 0 | 4-5★ 0 | Anger 4 | burned 9
  training underwear (generic): 22 | 1-2★ 0 | 4-5★ 0 | Anger 4 | burned 4
  training underwear (MooMoo): 13 | 1-2★ 0 | 4-5★ 0 | Anger 7 | burned 6
  training underwear (BIG ELEPHANT): 11 | 1-2★ 2 | 4-5★ 0 | Anger 9 | burned 3
  rewards / stickers / bribes: 8 | 1-2★ 0 | 4-5★ 0 | Anger 0 | burned 3
  training underwear (other brand): 8 | 1-2★ 0 | 4-5★ 4 | Anger 1 | burned 1
  tried everything: 4 | 1-2★ 0 | 4-5★ 0 | Anger 0 | burned 4
  Goodnites: 4 | 1-2★ 0 | 4-5★ 0 | Anger 0 | burned 0

# 12 burned/skeptical × source
  [('Trustpilot', 29), ('Reddit', 20), ('Amazon', 11), ('Forum', 5), ('YouTube comments', 3), ('Retailer reviews', 2), ('Walmart', 1)]
  'scam' rows mentioning upairy/subscription/gummies: 15 of 19

# 13 UpAiry-related rows (url or quote mentions upairy): 15

# 14 general toddler parent: awareness split
  199 {'problem': 25, 'solution': 47, 'product': 126, 'unaware': 1}

# 15 objection — segment-B-relevant cuts (all rows whose quote names age 4+ or bigger sizes)
  rows 78
  needs: [('bigger sizes', 23), ('leakproof at night', 7), ('absorbency that holds a pee', 5), ('resources for older / ND kids', 3), ('routine / reminder system', 2), ('sensory-friendly fit', 2), ('discreet', 2), ('feel-wet signal', 2), ('affordable', 2), ('reliable sizing / fit', 2)]
  failed: [('Pull-Ups / disposables', 7), ('Goodnites', 4), ('rewards / stickers / bribes', 1), ('training underwear (MooMoo)', 1), ('3-day / Oh Crap method', 1), ('training underwear (generic)', 1), ('training underwear (Hanes)', 1), ('punishment', 1), ('training underwear (UpAiry)', 1), ('training underwear (BIG ELEPHANT)', 1)]
  pains: [('late training (3.5y+ still not trained)', 33), ('size / big-kid products', 18), ('night wetting', 10), ('withholding / poop refusal', 9), ('child refuses', 9), ('daily accidents at school/daycare', 8), ('parent burnout', 6), ('leaks / soaked bed at night', 6), ('judgment / shame from others', 5), ("child doesn't notice wet / body signals", 4), ('deadline pressure (daycare/school rule)', 4), ("child can't communicate need", 3)]

# 16 segment B split: 'full containment' (diapers/nappies/Goodnites/size 7/nonverbal/level 3) vs 'accidents/underwear' language
  full-containment language: 26 | accidents/underwear language (no diaper words): 41 | neither: 94

# 17 ad-log leads_with (n=40)
  [('plain claim', 14), ('mechanism', 10), ('identity', 8), ('bigger claim', 4), ('upgraded mechanism', 4)]
  UpAiry [('plain claim', 5), ('identity', 5), ('mechanism', 2), ('bigger claim', 2), ('upgraded mechanism', 2)] | formats: [('image', 13), ('video', 3)]
  Kid Confident [('plain claim', 7), ('mechanism', 3), ('identity', 1), ('upgraded mechanism', 1)] | formats: [('video', 6), ('image', 6)]
  BrightKidCo [('mechanism', 5), ('bigger claim', 2), ('identity', 2), ('plain claim', 2), ('upgraded mechanism', 1)] | formats: [('video', 9), ('image', 3)]
  ads running >=100 days: 22 [('plain claim', 8), ('identity', 6), ('mechanism', 4), ('bigger claim', 2), ('upgraded mechanism', 2)]

# 18 per buyer group: top platforms + top pain
  general toddler parent (199): platforms [('Trustpilot (UpAiry)', 36), ('Reddit r/pottytraining', 24), ('Reddit r/toddlers', 19), ('Amazon (MooMoo Baby)', 18)] | pains [('leaks / soaked after one pee', 49), ('sizing / fit problems', 14), ('hidden subscription / billing', 13)] | awareness {'problem': 25, 'solution': 47, 'product': 126, 'unaware': 1}
  working parent / daycare (61): platforms [('BabyCenter', 8), ('Reddit r/workingmoms', 7), ('What to Expect', 7), ('Mumsnet', 6)] | pains [('deadline pressure (daycare/school rule)', 37), ('daily accidents at school/daycare', 10), ('daycare pull-up/underwear rules', 8)] | awareness {'problem': 37, 'solution': 21, 'product': 3}
  night / bedwetting parent (47): platforms [('Reddit r/daddit', 5), ('Reddit r/Parenting', 5), ('Amazon (MooMoo Baby)', 5), ('Reddit r/Mommit', 3)] | pains [('night wetting', 26), ('leaks / soaked bed at night', 18), ('child shame / embarrassment', 7)] | awareness {'product': 22, 'problem': 7, 'solution': 18}
  withholding parent (28): platforms [('Reddit r/toddlers', 7), ('Reddit r/pottytraining', 5), ('Reddit r/Autism_Parenting', 3), ('Reddit r/Parenting', 3)] | pains [('withholding / poop refusal', 28), ('late training (3.5y+ still not trained)', 7), ('parent burnout', 6)] | awareness {'solution': 7, 'problem': 21}
  dad (20): platforms [('Reddit r/daddit', 18), ('Mumsnet', 1), ('X (Twitter)', 1)] | pains [('night wetting', 5), ('parent burnout', 4), ('constant accidents', 2)] | awareness {'solution': 6, 'problem': 14}
  regression parent (17): platforms [('YouTube (Mistake That Turns a Regression Into an Ongoing Problem)', 5), ('Reddit r/pottytraining', 4), ('Reddit r/toddlers', 3), ('Reddit r/Parenting', 1)] | pains [('regression', 16), ('withholding / poop refusal', 3), ('deadline pressure (daycare/school rule)', 2)] | awareness {'problem': 13, 'solution': 4}
  childcare worker (12): platforms [('Reddit r/ECEProfessionals', 6), ('Reddit r/Teachers', 1), ('Amazon (Gerber)', 1), ('Mumsnet', 1)] | pains [('deadline pressure (daycare/school rule)', 2), ('daycare pull-up/underwear rules', 2), ('judgment / shame from others', 1)] | awareness {'problem': 4, 'product': 1, 'solution': 7}
  grandparent / gift buyer (9): platforms [('Trustpilot (UpAiry)', 4), ('Amazon (BIG ELEPHANT)', 2), ('Reddit r/toddlers', 1), ('Walmart (BIG ELEPHANT)', 1)] | pains [('leaks / soaked after one pee', 2), ('hidden subscription / billing', 1), ('deadline pressure (daycare/school rule)', 1)] | awareness {'product': 7, 'solution': 1, 'problem': 1}
  twins parent (11): platforms [('What to Expect', 7), ('Reddit r/Autism_Parenting', 1), ('Reddit r/Preschoolers', 1), ('WTE Multiples & Twins', 1)] | pains [('deadline pressure (daycare/school rule)', 4), ('late training (3.5y+ still not trained)', 2), ('parent burnout', 2)] | awareness {'problem': 7, 'solution': 3, 'product': 1}
  eco / cloth parent (9): platforms [('Reddit r/moderatelygranolamoms', 3), ('Reddit r/sustainability', 1), ('Reddit r/ZeroWaste', 1), ('Reddit r/toddlers', 1)] | pains [('night wetting', 2), ('withholding / poop refusal', 1), ('leaks / soaked after one pee', 1)] | awareness {'solution': 8, 'product': 1}

# 19 ad-log hook words (n=40 hooks)
  /toddler/: 10 of 40
  /diaper/: 4 of 40
  /pull-up|pull ups|pull-ups/: 5 of 40
  /day|week/: 19 of 40
  /daycare|preschool|school/: 6 of 40
  /accident/: 10 of 40
  /\bI |\bmy |\bMy /: 18 of 40
```

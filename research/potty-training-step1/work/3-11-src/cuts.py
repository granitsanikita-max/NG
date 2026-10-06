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

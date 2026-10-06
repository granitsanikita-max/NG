# Dump up to K quotes per tag value (VERBATIM first) for picking examples. python3 work/3-11-src/quotes.py COL [K] [seg]
import csv,sys,os,collections
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
R=list(csv.DictReader(open(os.path.join(B,"2C-databank.csv"),encoding="utf-8")))
sp=lambda v:[x.strip() for x in v.split(';') if x.strip()]
col=sys.argv[1]; K=int(sys.argv[2]) if len(sys.argv)>2 else 3
if len(sys.argv)>3: R=[r for r in R if {'ND / sensory parent','late-trainer parent','school-age accidents parent'}&set(sp(r['buyer_group']))]
c=collections.Counter(v for r in R for v in sp(r[col]))
for v,n in c.most_common():
    rows=sorted([r for r in R if v in sp(r[col])],key=lambda r:(r['capture']!='VERBATIM',-len(r['great_phrase'])))
    print(f"\n## {v} ({n})")
    for r in rows[:K]: print(f"- {r['id']} [{r['capture']}{(' '+r['stars']+'★') if r['stars'] else ''}] {r['quote'][:230]!r} | {r['platform']} | {r['url']}")

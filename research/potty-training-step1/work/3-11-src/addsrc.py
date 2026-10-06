# Append a "Data-bank rows cited" list (URL · platform · date · capture) for every [C:ID] tag in each file.
import csv,re,sys,os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
R={r['id']:r for r in csv.DictReader(open(os.path.join(B,"2C-databank.csv"),encoding="utf-8"))}
for f in sys.argv[1:]:
    s=open(f,encoding="utf-8").read()
    s=re.sub(r"\n### Data-bank rows cited \(§2C\).*\Z","",s,flags=re.S)
    ids=sorted(set(re.findall(r"\[C:([SN]\d{3})\]",s)),key=lambda x:(x[0],int(x[1:])))
    missing=[i for i in ids if i not in R]
    if missing: print(f,"MISSING",missing)
    if not ids: continue
    out="\n### Data-bank rows cited (§2C)\n"+"\n".join(f"- [C:{i}] {R[i]['url']} · {R[i]['platform']} · {R[i]['date'] or 'n/d'} · {R[i]['capture']}{(' · '+R[i]['stars']+'★') if R[i]['stars'] else ''}" for i in ids if i in R)+"\n"
    open(f,"w",encoding="utf-8").write(s.rstrip()+"\n"+out); print(f,len(ids),"rows")

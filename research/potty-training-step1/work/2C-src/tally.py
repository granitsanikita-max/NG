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

# Merge old (re-tagged) + new snippet files -> ../2C-databank.csv ; validate; de-dupe on (url, quote)
import csv, glob, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from convert_old import load
COLS="id,quote,url,platform,date,stars,source_type,capture,pain,desire,need,objection,failed_solution,trigger,misconception,belief,emotional_state,awareness_stage,burned_skeptical,authority_trusted,buyer_group,great_phrase".split(",")
EMO={"Shame","Guilt","Apathy","Grief","Fear","Desire","Anger","Pride","Courage","Neutrality","Willingness","Acceptance"}
AW={"unaware","problem","solution","product","most"}
def norm(s): return unicodedata.normalize("NFKC",s).replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"').lower()
old,skipped=load()
new=[]
here=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(os.path.join(here,"new_*.py"))):
    ns={}; exec(open(f,encoding="utf-8").read(),ns)
    for t in ns["ROWS"]:
        d=dict(zip(COLS[1:],t)); d["_src"]=os.path.basename(f); new.append(d)
for i,d in enumerate(new,1): d["id"]=f"N{i:03d}"
rows=old+new
NORM={"daycare provider":"daycare staff","other parents' reviews":"other parents","long timeline / not trained at school age":"late training (3.5y+ still not trained)","general toddler parent (UK)":"general toddler parent","general toddler parent (EU)":"general toddler parent","late-trainer / big-kid parent":"late-trainer parent","childcare worker (also parent)":"childcare worker",
"dry bed / sleep":"dry nights","holds an accident":"less mess / cleanup",
"daycare requires pull-ups":"daycare pull-up/underwear rules","daycare rules":"daycare pull-up/underwear rules","daycare puts trained kid in pull-ups":"daycare pull-up/underwear rules","daycare threatens back to pull-ups":"daycare pull-up/underwear rules","nursery won't help with pants":"daycare pull-up/underwear rules",
"school requires potty trained":"daycare/preschool deadline","preschool rule":"daycare/preschool deadline","starting daycare":"daycare/preschool deadline","daycare rules on pull-ups/underwear":"daycare pull-up/underwear rules",
"child doesn't notice wet":"child doesn't notice wet / body signals",
"size too small / tight elastic":"sizing / fit problems","size too small":"sizing / fit problems","size too small / shrinks":"sizing / fit problems","sizing / fit":"sizing / fit problems","sizing uncertainty":"sizing / fit problems","poor quality / tight elastic":"poor quality","leaks out the front":"leaks / soaked after one pee",
"runs small":"sizing / fit uncertain","sizing uncertain":"sizing / fit uncertain",
"sizing guidance / easy exchange":"reliable sizing / fit","consistent sizing":"reliable sizing / fit","snug leg fit":"reliable sizing / fit",
"skeptical of brand":"skeptical of brand / reviews","fake reviews":"skeptical of brand / reviews","reviews overstate":"skeptical of brand / reviews"}
def nz(cell): 
    vals=[NORM.get(v.strip(),v.strip()) for v in cell.split(";") if v.strip()]
    o=[]; [o.append(v) for v in vals if v not in o]; return "; ".join(o)
TAGC=["pain","desire","need","objection","failed_solution","trigger","misconception","belief","burned_skeptical","authority_trusted","buyer_group"]
for d in rows:
    for c in TAGC: d[c]=nz(d.get(c,""))
seen=set(); out=[]; dups=[]
for d in rows:
    key=(d["url"].strip(), norm(d["quote"]).strip())
    if key in seen: dups.append(d["id"]); continue
    seen.add(key)
    gp=d.get("great_phrase","")
    if gp and norm(gp) not in norm(d["quote"]): d["great_phrase"]=""
    assert d["capture"] in ("VERBATIM","SNIPPET"), d
    assert d["emotional_state"] in EMO, (d["id"],d["emotional_state"])
    assert d["awareness_stage"] in AW, (d["id"],d["awareness_stage"])
    assert d["url"].startswith("http"), d["id"]
    out.append({c:d.get(c,"") for c in COLS})
p=os.path.join(here,"..","2C-databank.csv")
with open(p,"w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=COLS); w.writeheader(); w.writerows(out)
print("old",len(old),"new",len(new),"dupes removed",len(dups),dups,"final",len(out)); print("excluded",skipped)

#!/usr/bin/env python3
"""Assemble the 4 Step-1 docs from section files in page order, with self-contained Sources."""
import re, csv, glob, os, sys, json
W='/home/user/NG/research/potty-training-step1/work'
OUT='/home/user/NG/research/potty-training-step1/build'
DOCS={
 'Doc 1 — Market & Competition':['D1-Pre0-LOCKED.md','D1-Pre0-rerun.md','D1-Audit.md','D1-s0-LOCKED.md','D1-s0B.md','D1-s0B-LOCKED.md','D1-s1.md','D1-s1-LOCKED.md','D1-s2-LOCKED.md','D1-s5.md','D1-s7.md','D1-s8.md'],
 'Doc 2 — The Customer':['D2-2C-summary.md','D2-s3.md','D2-s3A.md','D2-s10.md','D2-s10B.md','D2-s14.md','D2-s18.md'],
 'Doc 3 — Persuasion':['D3-s6.md','D3-s9.md','D3-s9-REWRITE.md','D3-s9B.md','D3-s11.md','D3-s12.md','D3-s13.md','D3-s13B.md','D3-s16.md','D3-s17.md','D3-s18B.md'],
 'Doc 4 — Brand, Offer & Funnel':['D4-s2B-LOCKED.md','D4-s4.md','D4-s4B.md','D4-s15-FINAL.md','D4-FunnelMap.md','D4-s20-VERIFY.md'],
}
ID=r'\[((?:[A-Z]{1,2}\d+[a-z]?)|(?:C:[A-Z]\d+))\]'
# registry: every "- [ID] ..." / "[ID] ..." definition line in any work file
reg={}
# §20C: skip logs / skeptic reports (they quote IDs, they don't define them); prefer a definition with a URL
SKIP=re.compile(r'(20B-|REFRESH-LOG|UPSTREAM-CHANGES|tools-log)')
def has_url(t): return 'http' in t.split(' · [')[0]
def score(t): return 2*has_url(t)+(not reVSINT.search(t.split(' · [')[0]))
reVSINT=re.compile(r'(work/|docs/|full line in)')
for f in sorted(glob.glob(f'{W}/**/*.md',recursive=True)):
    if SKIP.search(os.path.basename(f)): continue
    for line in open(f,errors='ignore'):
        m=re.match(r'\s*[-*>]?\s*\[((?:[A-Z]{1,2}\d+[a-z]?)|(?:C:[A-Z]\d+))\]\s*[:·-]?\s*(.+)',line)
        if m and len(m.group(2))>15 and not m.group(2).startswith('['):
            t=line.strip().lstrip('-*> ').strip()
            if m.group(1) not in reg or score(t)>score(reg[m.group(1)]): reg[m.group(1)]=t
for r in csv.DictReader(open(f'{W}/2C-databank.csv')):
    k='C:'+r['id']; reg.setdefault(k,f"[{k}] {r['url']} · {r['platform']} · {r.get('date') or 'n/d'} · {r.get('capture','')}")
def body(f):
    t=open(f'{W}/{f}').read()
    m=re.search(r'^#{1,4}\s*(Sources|Data-bank rows cited)\b.*$',t,re.M)
    return (t[:m.start()] if m else t).rstrip()+'\n'
report={}
for title,files in DOCS.items():
    parts=[]; missing_files=[]
    for f in files:
        if os.path.exists(f'{W}/{f}'): parts.append(body(f))
        else: missing_files.append(f)
    text='\n\n---\n\n'.join(parts)
    cited=[]; [cited.append(i) for i in re.findall(ID,text) if i not in cited]
    unresolved=[i for i in cited if i not in reg]
    src='\n'.join(f'- {reg[i]}' for i in cited if i in reg)
    slug=title.split(' — ')[0].replace(' ','')
    open(f'{OUT}/{slug}-body.md','w').write(text)
    open(f'{OUT}/{slug}-sources.md','w').write(src+'\n')
    report[title]={'files':len(parts),'missing_files':missing_files,'cited':len(cited),'unresolved':unresolved}
json.dump(report,open(f'{OUT}/build-report.json','w'),indent=1)
for k,v in report.items(): print(k,'| files',v['files'],'missing',v['missing_files'],'| cited',v['cited'],'| unresolved',len(v['unresolved']),v['unresolved'][:15])

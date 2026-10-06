# Writer B cuts of work/2C-databank.csv for §12, §14, §16, §17, §18. Run: python3 work/B-src/cutsB.py
import csv,collections,re,os,sys
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
R=list(csv.DictReader(open(os.path.join(B,"2C-databank.csv"),encoding="utf-8"))); N=len(R)
sp=lambda v:[x.strip() for x in v.split(';') if x.strip()]
SEG={'ND / sensory parent','late-trainer parent','school-age accidents parent'}
seg=[r for r in R if SEG & set(sp(r['buyer_group']))]
school=[r for r in R if 'school-age accidents parent' in sp(r['buyer_group'])]
def cnt(rows,col): return collections.Counter(v for r in rows for v in sp(r[col]))
print(f"ROWS N={N} | segment B={len(seg)} | school-age tag={len(school)} | last id={R[-1]['id']}")
print("\n## A authority_trusted: bank | segB | school")
a,b,c=cnt(R,'authority_trusted'),cnt(seg,'authority_trusted'),cnt(school,'authority_trusted')
for k,v in a.most_common(): print(f"- {k}: {v} | {b.get(k,0)} | {c.get(k,0)}")
print("  rows with any authority tag:",sum(bool(r['authority_trusted'].strip()) for r in R))
AUTH={'pediatrician/doctor':r"pediatrician|paediatrician|\bdoctor|\bdr\b|\bGP\b",'urologist':r"urolog",'continence nurse/ERIC/BBUK':r"continence|\bERIC\b|bladder (and|&) bowel|school nurse|\bnurse\b",'OT':r"\bOT\b|occupational",'ABA/BCBA':r"\bABA\b|BCBA",'teacher':r"teacher",'pelvic floor PT':r"pelvic floor",'Hodges':r"hodges",'Oh Crap/Glowacki':r"oh crap|glowacki",'3-day/Brucks':r"3[- ]day|three[- ]day|brucks"}
print("\n## B authority keyword mentions in quotes: bank | segB | school")
for k,p in AUTH.items():
    rx=re.compile(p,re.I); print(f"- {k}: {sum(bool(rx.search(r['quote'])) for r in R)} | {sum(bool(rx.search(r['quote'])) for r in seg)} | {sum(bool(rx.search(r['quote'])) for r in school)}")
print("\n## C trigger tag: bank | segB | school")
a,b,c=cnt(R,'trigger'),cnt(seg,'trigger'),cnt(school,'trigger')
for k,v in a.most_common(): print(f"- {k}: {v} | {b.get(k,0)} | {c.get(k,0)}")
MOM={'came home wet / spare clothes in backpack':r"came home (wet|in)|comes? home (from school )?with wet|spare (clothes|pants)|extra (clothes|pants)|backpack",
 'teacher message / call / note / request':r"teacher (sent|called|request|asked|message|said|told|needs)|called (at|from) (school|lunch)|school (called|said|did have)|note from",
 'started K / 1st grade / new school / year 1':r"start(ed|ing)? (kindy|kinder|kindergarten|school|first grade|1st grade|year ?1|reception)|new school|first (day|week) of school|gone into year|transitional kindergarten",
 'accident in front of class / classmates / teasing':r"classmate|in front of|whole class|tease|teased|laugh|made fun|someone might say|peers",
 'sleepover / camp / trip':r"sleepover|sleep over|camp\b|field trip|playdate",
 'outgrew sizes / nothing fits':r"outgr|too small|too tight|largest (size|pull)|size 7|5t-6t|doesn.t fit|don.t fit|fit her|fit him|bigger size",
 'relative / partner judgment':r"grandma|grandmother|mother[- ]in[- ]law|\bMIL\b|my mom|in-laws|his way|shame",
 'doctor / urologist referral':r"urolog|pediatrician|doctor|\bdr\b|x-ray|gastro",
 'scared to ask / bathroom access at school':r"scared to ask|ask to go|bathroom (schedule|pass)|allowed to (go|use)|hold it"}
print("\n## D school-moment keyword cuts in quotes: bank | segB | school-tag")
for k,p in MOM.items():
    rx=re.compile(p,re.I); print(f"- {k}: {sum(bool(rx.search(r['quote'])) for r in R)} | {sum(bool(rx.search(r['quote'])) for r in seg)} | {sum(bool(rx.search(r['quote'])) for r in school)}")
print("\n## E emotional_state: bank | segB | school")
a,b,c=cnt(R,'emotional_state'),cnt(seg,'emotional_state'),cnt(school,'emotional_state')
for k,v in a.most_common(): print(f"- {k}: {v} | {b.get(k,0)} | {c.get(k,0)}")
print("\n## F awareness school-tag:",dict(cnt(school,'awareness_stage')))
print("\n## G pains school-tag top 15:",cnt(school,'pain').most_common(15))
print("\n## H desires school-tag top 10:",cnt(school,'desire').most_common(10))
WORDS={'accident(s)':r"\baccidents?\b",'pee/peeing/peed':r"\bpee(s|d|ing)?\b",'wet/wets/wetting':r"\bwet(s|ting)?\b",'potty':r"\bpotty\b",'underwear':r"\bunderwear\b",'undies':r"\bundies\b",'pull-up(s)':r"pull[- ]?ups?\b",'diaper(s)/nappies':r"diapers?|napp(y|ies)",'training pants/underwear':r"training (pants|underwear|undies)",'leak/leaks/leaked':r"\bleak",'big kid / big boy / big girl':r"big (kid|boy|girl)",'potty trained':r"potty[- ]trained",'potty learning':r"potty learning",'toilet':r"\btoilet",'bathroom':r"\bbathroom",'incontinence':r"incontinen",'enuresis':r"enuresis",'urinate/urination/void':r"urinat|\bvoid",'bladder':r"\bbladder",'absorb/absorbent':r"absorb",'leakproof/leak proof':r"leak[- ]?proof",'interoception':r"interocep",'sensory':r"sensory",'autism/autistic/ASD':r"autis|\bASD\b",'neurodivergent/ND':r"neurodiver",'soaked/soaking':r"soak",'ml/oz/ounce':r"\bml\b|\boz\b|ounce",'scam':r"\bscam",'shame/embarrass':r"shame|embarrass",'dignity':r"dignity",'regression/regress':r"regress",'readiness/ready':r"\bready\b|readiness"}
print("\n## I word use in quotes (snippets containing): bank | segB | school")
for k,p in WORDS.items():
    rx=re.compile(p,re.I); print(f"- {k}: {sum(bool(rx.search(r['quote'])) for r in R)} | {sum(bool(rx.search(r['quote'])) for r in seg)} | {sum(bool(rx.search(r['quote'])) for r in school)}")
gp=[r['great_phrase'].strip() for r in R if r['great_phrase'].strip()]
print("\n## J great phrases:",len(gp))
alltext=" || ".join(r['quote'].lower() for r in R)
pc=collections.Counter()
for g in set(gp):
    pc[g]=sum(1 for r in R if g.lower() in r['quote'].lower())
for g,n in sorted(pc.items(),key=lambda x:-x[1]): print(f"  {n}x | {g}")
SWIPE={"come home wet (from school)":r"(come|comes|came|coming) (out |home )?(from school )?(with )?(wet|in (his|her) spare)",
"spare / extra clothes (in the backpack)":r"(spare|extra) (clothes|pants|trousers)",
"accidents at school":r"accidents? at (school|kindergarten|kindy)",
"pees his/her pants":r"pee(s|d|ing)? (in )?(his|her|their|your) pants",
"wets himself / wets his pants":r"wet(s|ting)? (his|her) (pants|self)|wetting (himself|herself)|wets? (himself|herself)",
"just diapers / just nappies":r"just (a )?(diapers?|napp(y|ies))|they.re just diaper|diapers with more steps|like a diaper|like diapers",
"waste of money":r"waste of money",
"not leakproof":r"not .{0,2}leak[- ]?proof",
"soaked / soaking":r"soak",
"every (single) day":r"every (single )?day|everyday|daily",
"own timeline / own pace":r"own (timeline|pace|time|timetable)|different timetable",
"wait-list":r"wait[- ]?list",
"wits end":r"wits'? ?end",
"losing my mind":r"losing my mind|lose my mind",
"exhausted / exhausting":r"exhaust",
"embarrassed / embarrassing":r"embarrass",
"doesn't notice / doesn't feel / doesn't care (he's wet)":r"(doesn.t|didn.t|don.t|isn.t) (notice|feel|care|seem to (notice|care)|realize|bothered)",
"too busy to stop (playing)":r"too busy|stop playing|interrupt|break what|cannot stop what",
"hold (at least) one pee":r"hold (at least )?(one|a) (pee|accident)|hold (really )?anything|hold (more|like)",
"a dribble":r"dribble",
"went (straight) through":r"(straight|right|went|goes|leaked|wet|seep) ?through",
"bigger sizes / sizes go up":r"bigger size|larger size|sizes go up|size up|largest",
"too tight / too small / doesn't fit":r"too tight|too small|doesn.t fit|cutting off|don.t fit|fit (her|him)",
"(butt) seams":r"seam",
"scam":r"\bscam",
"constipation":r"constipat",
"kicked out (of preschool)":r"kick(ed)? out|dismissed",
"back in pull-ups":r"back (in|into|to) (pull|diaper|napp)|buy pull-ups again",
"classmates / teased / laugh":r"classmate|teas(e|ed|ing)|laugh|made fun|someone might say|peers",
"lazy":r"\blazy",
"failure / bad mother / crap dad":r"failure|bad (mom|mother|parent)|crap dad|failing|something wrong",
"nothing works / tried everything":r"nothing (works|worked)|tried (everything|so)|we.ve done|you name it",
"I'm lost / at a loss":r"i.m lost|at a loss|don.t know what (else )?to do|out of ideas",
"constant accidents":r"constant(ly)? (accidents|wet)",
"I hate potty training / breaking me":r"hate potty|potty training (is|makes)|breaking (me|my)",
"real / regular underwear":r"real underwear|regular underwear|normal underwear|normal pants",
"big girl / big boy underwear":r"big (girl|boy|kid)",
"ready when he's ready / decided himself":r"ready when|when (he|she|they).s ready|decided (him|her)self|figured it out",
"shame / shamed":r"\bsham",
"talk to your pediatrician / doctor":r"pediatrician|doctor|\bdr\b",
"full accident / full release":r"full (accident|release|pee|bladder)|whole pee",
"puddle(s)":r"puddle",
"all over the couch / floor":r"all over|on the floor|off the floor",
"laundry / running out of pants":r"running out of|laundry|washing",
"feel(s) wet / feeling wet":r"feel(s|ing)? (the )?wet|feeling of being wet|feel when",
"school called / teacher sent a message":r"called (me|at|from)|school called|teacher (sent|called|messaged|asked|request)",
"first grade / kindergarten / year 1":r"first grade|1st grade|first grader|kindergart|kindy|year (one|1)\b|second grade",
"help!":r"\bhelp\b",
"sensory":r"sensory",
"meltdown":r"meltdown|melts down",
"pull-ups are a trap / marketing":r"marketing|gimmick|trap",
"hiding it / never tells anyone":r"never tells|hid(e|es|ing)|tucked|conceal",
"scared to ask":r"scared|afraid",
"desperate":r"desperate",
"accident(s) (bare word)":r"\baccidents?\b"}
print("\n## K swipe phrase families (snippets containing): bank | segB | school   (★ = 3+ bank)")
for k,p in SWIPE.items():
    rx=re.compile(p,re.I); n=sum(bool(rx.search(r['quote'])) for r in R)
    print(f"- {'★ ' if n>=3 else ''}{k}: {n} | {sum(bool(rx.search(r['quote'])) for r in seg)} | {sum(bool(rx.search(r['quote'])) for r in school)}")
al=list(csv.DictReader(open(os.path.join(B,"ad-log.csv"),encoding="utf-8")))
HYPE={'toddler':r"toddler",'week(s)/days speed':r"\bweeks?\b|\bdays?\b",'leakproof':r"leak[- ]?proof",'™ / technology / layer':r"™|technology|layer",'secret / finally / hack':r"secret|finally|hack",'game changer / miracle / magic':r"game[- ]?changer|miracle|magic",'STILL in diapers (shame)':r"still in diapers",'potty trained (outcome)':r"potty[- ]?trained|potty train"}
print("\n## L ad-log hook hype words (n=",len(al),")")
for k,p in HYPE.items(): print(f"- {k}: {sum(bool(re.search(p,r['hook_first_line'],re.I)) for r in al)}")
print("\n## M counts for §9B re-check, §15 offer inputs, §16/§17 (bank | segB | school)")
for col in ['objection','pain','need','desire','belief','failed_solution','misconception','burned_skeptical']:
    a,b,c=cnt(R,col),cnt(seg,col),cnt(school,col)
    print(f"\n### {col}")
    for k,v in a.most_common(30): print(f"- {k}: {v} | {b.get(k,0)} | {c.get(k,0)}")
print("\n## N awareness: bank",dict(cnt(R,'awareness_stage')),"| segB",dict(cnt(seg,'awareness_stage')))

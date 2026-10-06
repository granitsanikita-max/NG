# Re-tag docs/potty-training-research/snippets.md (252 rows, old #TAG schema) into the §2C page schema.
# Rule-based mapping from the old tags + keyword rules on the verbatim quote text, plus a small manual great-phrase table.
# Output: list ROWS_OLD of dicts (same columns as the databank). Run via build_bank.py.
import re, datetime

SRC = "/home/user/NG/docs/potty-training-research/snippets.md"

# Reddit post IDs are base-36 and increase over time; date estimated by interpolating between anchor IDs (approx. month).
ANCH = [("3ii3ei","2015-08"),("8z4kpj","2018-07"),("afork0","2019-01"),("gr190t","2020-05"),("ldalx9","2021-02"),
        ("pefrd2","2021-08"),("rztdng","2022-01"),("vri0px","2022-07"),("zean8x","2022-12"),("10a0000","2023-01"),
        ("13o0000","2023-05"),("17e0000","2023-10"),("18w0000","2024-01"),("1df0000","2024-06"),("1ey0000","2024-08"),
        ("1gi0000","2024-11"),("1i10000","2025-01"),("1jq0000","2025-04"),("1l40000","2025-06"),("1o20000","2025-10")]
def _m(s): y,m=s.split("-"); return int(y)*12+int(m)-1
_A=[(int(a,36),_m(d)) for a,d in ANCH]
def reddit_date(url):
    m=re.search(r"/comments/([a-z0-9]+)/",url or "")
    if not m: return ""
    v=int(m.group(1),36)
    pts=_A
    if v<=pts[0][0]: mm=pts[0][1]
    else:
        for (a1,m1),(a2,m2) in zip(pts,pts[1:]):
            if v<=a2: mm=m1+(v-a1)*(m2-m1)/(a2-a1); break
        else:
            (a1,m1),(a2,m2)=pts[-2],pts[-1]; mm=m2+(v-a2)*(m2-m1)/(a2-a1)
    mm=int(round(mm)); mm=min(mm,_m("2026-10"))
    return f"~{mm//12}-{mm%12+1:02d} (est. from post ID)"

PHRASE = {  # verbatim short phrases (from C-parent-voice swipe file), keyed by old S-number
 "S001":"not potty trained until they are 8","S013":"a difficult and low reward journey","S018":"The largest pull-ups are size 5t-6t",
 "S020":"I'm giving up already!","S021":"allowed him to realize he was wet","S026":"cannot have anything touching her crotch",
 "S027":"Elastic sucks?","S032":"She hates butt seams","S040":"I am desperate for help","S041":"If her brain can't hear her bladder",
 "S058":"it's honestly embarrassing","S066":"Shamed by daycare over potty training","S069":"every kid is on their own timeline",
 "S070":"Potty training makes me hate myself","S074":"Makes me feel like a bad mother","S079":"Potty training is breaking me.",
 "S084":"my lowest point of parenting","S086":"making me resent my toddler","S087":"I f*cking hate potty training.",
 "S091":"Help before we get kicked out of preschool","S093":"be dismissed from care","S100":"running our lives",
 "S108":"Poop is ruining my life","S115":"a developmental stage, not a skill","S119":"embarrassed that he still wears a pull-up",
 "S122":"keep denying him sleepovers","S139":"really doing all of us a disservice","S144":"No rewards, no punishments, no shame.",
 "S145":"an even bigger failure","S146":"destroyed my confidence","S148":"highly condescending","S149":"you weren't paying close enough attention",
 "S152":"it's breaking my spirit","S154":"Big waste of money","S156":"they're just diaper","S158":"the only difference between pull ups and pull on diapers is marketing",
 "S159":"money going down the drain","S165":"Potty training is hell.","S167":"Call it learning and not training.",
 "S168":"the worst part of parenting","S174":"I've done something wrong and broke my child","S178":"Nothing worked until he decided himself",
 "S179":"long past the window","S182":"pull ups are a trap","S189":"there's no excuse at 3.5 years old anymore","S190":"I'm losing my mind",
 "S191":"We just non judgmentally kept at it","S193":"it's mentally exhausting","S194":"the most difficult thing I have literally ever done as a parent",
 "S196":"on the wait-list to be on the wait-list","S197":"I cannot wait again until winter break","S198":"These methods do not work with a child with SPD.",
 "S199":"Stop reading the books.","S200":"hypersensitive to the feeling of urine","S201":"Skills take longer to work on.",
 "S203":"marketed towards neurotypical kids","S217":"it's lazy parenting","S218":"they will probabbly think I never bothered",
 "S219":"I feel like I'm the last !d!ot in the world","S221":"I'm a crap dad","S225":"ND children just have a different timetable",
 "S227":"Will the other children laugh at him?","S228":"ready when he was ready to be ready","S233":"saved my son embarrassment",
 "S235":"i can go to sleepover and no one knows","S237":"Worst leaks ever","S238":"excessive, unnecessary amounts of laundry",
 "S242":"isn't $20 a pair","S247":"can I please try to sleep in my underwear",
}
EXCLUDE = {"S025":"vendor reply, not a customer","S243":"publisher editorial, not a customer"}

def has(t,*ks): t=t.lower(); return any(k.lower() in t for k in ks)
def J(xs):
    out=[]; [out.append(x) for x in xs if x and x not in out]; return "; ".join(out)

def tag_row(sid,tags,quote,platform,url,cap):
    T=set(tags); q=quote; ql=q.lower(); plat=platform
    # source type
    if plat.startswith("Reddit"): st="Reddit"
    elif has(plat,"What to Expect","WTE","BabyCenter","Mumsnet","Facebook group"): st="Forum"
    elif has(plat,"Instagram"): st="Instagram comments"
    elif has(plat,"Walmart"): st="Walmart"
    else: st="Retailer reviews"
    capture = {"SNIPPET":"SNIPPET","FULL":"VERBATIM","REV":"VERBATIM","WF":"SNIPPET"}.get(cap.split()[0],"SNIPPET")
    # buyer group
    bg=[]
    if "#DEADLINE" in T or has(plat,"workingmoms") or has(ql,"go back to work","in the office","work full time"): bg.append("working parent / daycare")
    if "#ND" in T or "#SENSORY" in T: bg.append("ND / sensory parent")
    if "#LATE" in T: bg.append("late-trainer parent")
    if "#NIGHT" in T: bg.append("night / bedwetting parent")
    if "#WITHHOLD" in T: bg.append("withholding parent")
    if "#REGRESS" in T: bg.append("regression parent")
    if "#DAD" in T or has(plat,"daddit") or has(ql,"crap dad"): bg.append("dad")
    if "#TWINS" in T: bg.append("twins parent")
    if "#ECO" in T: bg.append("eco / cloth parent")
    if "#POSTTRAIN" in T: bg.append("school-age accidents parent")
    if has(plat,"ECEProfessionals","r/Teachers"): bg=["childcare worker"]
    if has(plat,"nottheonion"): bg=["commentator"]
    if has(ql,"i am 15 years old"): bg=["teen / self"]
    if has(ql,"nephew"): bg.append("relative")
    if not bg: bg=["general toddler parent"]
    # pain
    pn=[]
    if "#LATE" in T or "#ND" in T and has(ql,"year old","years old","yo ","until"): pn.append("long timeline / not trained at school age")
    if "#DEADLINE" in T: pn.append("deadline pressure (daycare/school rule)")
    if "#JUDGE" in T: pn.append("judgment / shame from others")
    if "#SHAME" in T and "#JUDGE" not in T: pn.append("child shame / embarrassment" if "#NIGHT" in T or has(ql,"he was","embarrassed","sleepover","friends") else "parent shame / embarrassment")
    if "#FAIL" in T: pn.append("parent guilt")
    if "#BURNOUT" in T: pn.append("parent burnout")
    if "#WITHHOLD" in T: pn.append("withholding / poop refusal")
    if "#NIGHT" in T: pn.append("leaks / soaked bed at night" if has(ql,"leak") else "night wetting")
    elif has(ql,"leak","soaked"): pn.append("leaks / soaked after one pee")
    if "#POSTTRAIN" in T: pn.append("daily accidents at school/daycare")
    if "#REGRESS" in T: pn.append("regression")
    if "#SIZE" in T: pn.append("size / big-kid products")
    if "#SENSORY" in T: pn.append("sensory discomfort")
    if has(ql,"notice","sensation","interoception","feel his bodies","feel wet","doesn't care","hear her bladder","bodily awareness"): pn.append("child doesn't notice wet / body signals")
    if has(ql,"non verbal","nonverbal","speech delay","cannot say","the language"): pn.append("child can't communicate need")
    if has(ql,"refuse","will not","won't","fits and cries","flat out"): pn.append("child refuses")
    if has(ql,"afford","expensive","money","insurance","$"): pn.append("cost / money drain")
    if has(ql,"laundry"): pn.append("laundry / mess")
    if has(ql,"wait-list","appointment","queue"): pn.append("can't access specialist help")
    if has(ql,"laughed","bullied","made fun"): pn.append("fear child will be teased")
    # desire
    ds=[]
    if "#DEADLINE" in T: ds.append("daycare/school-ready")
    if "#DIGNITY" in T or has(ql,"big kid","no one knows","independence","don't want to be in diapers"): ds.append("child dignity / real underwear")
    if "#NIGHT" in T: ds.append("dry nights")
    if has(ql,"sleepover"): ds.append("sleepovers without shame")
    if "#METHOD" in T or has(ql,"own pace","non judgmentally","no shame"): ds.append("no-pressure process")
    if has(ql,"absorb","contain"): ds.append("less mess / cleanup")
    # need
    nd=[]
    if "#SIZE" in T: nd.append("bigger sizes")
    if "#SENSORY" in T: nd.append("sensory-friendly fit")
    if "#F-TRAINPANT" in T or has(ql,"absorb"): nd.append("absorbency that holds a pee")
    if has(ql,"realize he was wet","feel wet","feel the wet","sensation of peeing","notice","still lets the kid feel wet","sensation of being"): nd.append("feel-wet signal")
    if "#DIGNITY" in T or has(ql,"discreet","no one knows","peers don't see"): nd.append("discreet")
    if "#NIGHT" in T and has(ql,"leak","absorb"): nd.append("leakproof at night")
    if "#ECO" in T: nd.append("washable / reusable")
    if has(ql,"timer","visual","picture schedule","signs for","schedule","potty watch","reminding"): nd.append("routine / reminder system")
    if "#ND" in T and has(ql,"books","methods","traditional","neurotypical","older boy"): nd.append("resources for older / ND kids")
    # objection (to a training-underwear purchase)
    ob=[]
    if has(ql,"waste of money","waste"): ob.append("waste of money")
    if "#F-TRAINPANT" in T and has(ql,"soaked","not as absorbent","leak"): ob.append("won't hold pee / leaks")
    if has(ql,"$20 a pair","affordable"): ob.append("price")
    if has(ql,"just diaper","marketing","trap"): ob.append("feels like a diaper")
    # failed solutions
    fs=[]
    if "#F-PULLUP" in T: fs.append("Goodnites" if has(ql,"goodnites","goodnights") else "Pull-Ups / disposables")
    if has(ql,"goodnites","goodnights") and "Goodnites" not in fs: fs.append("Goodnites")
    if "#F-REWARD" in T: fs.append("rewards / stickers / bribes")
    if "#F-3DAY" in T: fs.append("3-day / Oh Crap method")
    if has(ql,"naked") and "3-day / Oh Crap method" not in fs: fs.append("naked method")
    if "#F-WATCH" in T: fs.append("potty watch")
    if "#F-TRAINPANT" in T:
        fs.append("training underwear (MooMoo)" if has(ql,"moomoo") else ("training underwear (other brand)" if has(ql,"charlie banana","ooshbaby","hello bello","paw patrol") else "training underwear (generic)"))
    if "#F-GADGET" in T: fs.append("gadgets (seats, potties, books)")
    if has(ql,"miralax","suppositor"): fs.append("Miralax / medical")
    if has(ql,"tried everything","tried everything","tried allllll","nothing worked","we've tried everything") and not fs: fs.append("tried everything")
    # triggers
    tr=[]
    if "#DEADLINE" in T:
        tr.append("school start (K/Reception)" if has(ql,"kindergarten","reception","school") and not has(ql,"preschool") else "daycare/preschool deadline")
    if "#REGRESS" in T and has(ql,"brother","sibling","baby","home"): tr.append("new sibling")
    if has(ql,"mil","mother in law","my mom","my mother","relative","ikder relative"): tr.append("relative judgment")
    if has(ql,"teacher requested","school said","school did have a problem","called at lunch"): tr.append("school/teacher complaint")
    if has(ql,"sleepover"): tr.append("sleepover invite")
    if has(ql,"largest","too small","doesnt fit","do not fit","could not find diapers"): tr.append("outgrew largest size")
    if has(ql,"go back to work","in the office"): tr.append("back to work")
    if has(ql,"day 3","day three","day 8"): tr.append("3-day weekend attempt")
    if has(ql,"after one bad","poop incident"): tr.append("one painful poop")
    if has(ql,"leak") and "#NIGHT" in T: tr.append("soaked bed")
    # misconceptions
    mc=[]
    if has(ql,"should be potty trained by","trained by 2","16 month old should","18 month old should"): mc.append("should be trained by 2/3")
    if has(ql,"long past the window"): mc.append("missed the window")
    if has(ql,"lazy parenting"): mc.append("late training = lazy parenting")
    if has(ql,"sever developmental delay","severe developmental delay"): mc.append("untrained at 5 = severe delay")
    if has(ql,"100% full proof","can be done in 3 days"): mc.append("3 days is enough")
    if has(ql,"neglect"): mc.append("pull-ups at 4.5 = neglect")
    # beliefs
    bl=[]
    if has(ql,"own timeline","different timetable","when he was ready","decided himself","felt ready","just might take time","on their own timeline"): bl.append("every kid own timeline")
    if has(ql,"no shame","non judgmentally","don't make him feel any shame","nonjudgment"): bl.append("no shame approach")
    if has(ql,"learning and not training"): bl.append("learning not training")
    if has(ql,"just diaper","marketing","trap","no stake"): bl.append("pull-ups are just diapers")
    if has(ql,"do not work with a child with spd","neurotypical","traditional potty training doesn't","stop reading the books","do not apply"): bl.append("methods don't work for ND kids")
    if has(ql,"constipat"): bl.append("constipation causes accidents")
    if has(ql,"developmental stage, not a skill","perfectly normal"): bl.append("night dryness is developmental")
    if has(ql,"power struggle","so much pressure"): bl.append("pressure backfires")
    if has(ql,"consistency is key","strict schedule"): bl.append("consistency / schedule works")
    if has(ql,"outdated belief"): bl.append("every kid own timeline")
    # emotional state (Map ladder names)
    if has(ql,"i hate","hate myself","hate potty","burn in hell","so mad","f*cking","garbage","condescending","awful","neglect","resent","waste of money","total waste","aghhh","back the f off","the only difference between pull ups and pull on diapers is marketing"): em="Anger"
    elif "#SHAME" in T or has(ql,"embarrass","bad mother","disgust","shamed","only one still in nappies"): em="Shame"
    elif "#FAIL" in T or has(ql,"failure","terrible parent","crap dad","broke my child","last !d!ot"): em="Guilt"
    elif has(ql,"giving up","wits end","wit's end","at a loss","breaking","exhausting","losing my mind","throwing in the towel","lowest point","defeating","stressed","so frustrated","frustrating","fed up","hell","ruining my life","mentally","didn't really work","didn't make it","no progress","did everything","shelf potty training","running our lives","wreck us","tried everything"): em="Apathy"
    elif "#FEAR" in T or has(ql,"worried","scared","concerned","anxious","help","desperate","kicked out","dismissed","unenroll","laughed","panicked","stuck in transitional","need to be fully potty trained","won't go one night","leaking","resists","refuses","will not","feeling ..."): em="Fear"
    elif has(ql,"trauma","cruel","sad"): em="Grief"
    elif has(ql,"loved","liked","helped","saved","worth every penny","best","please make","please see"): em="Pride" if not has(ql,"please see") else "Desire"
    elif "#METHOD" in T: em="Acceptance"
    else: em="Neutrality"
    # awareness
    if has(ql,"moomoo","goodnites","goodnights","huggies","charlie banana","ooshbaby","hello bello","parents choice","dry nites","millie") or st in ("Retailer reviews","Walmart"): aw="product"
    elif any(t.startswith("#F-") for t in T) or "#METHOD" in T or has(ql,"pull-up","pull up","pullup","training pants","miralax","aba","timer","method","underwear","boxers","seam"): aw="solution"
    else: aw="problem"
    # burned / skeptical
    bs=[]
    if has(ql,"tried everything","tried everything","tried allllll","nothing worked","did everything","tried litterally everything","tried so so so many"): bs.append("tried everything")
    if has(ql,"waste of money","waste"): bs.append("waste of money")
    if has(ql,"didn't really work","utterly failed","disaster","bust","garbage","disservice","failed potty training","didn't make it","no real success","no progress"): bs.append("nothing works")
    # authority
    au=[]
    if has(ql,"pediatrician"): au.append("pediatrician")
    if has(ql," ot","occupational"): au.append("occupational therapist")
    if has(ql,"aba"): au.append("ABA therapist")
    if has(ql,"helped over 100 kiddos","very experienced"): au.append("experienced childcare worker")
    if has(ql,"medical advice","doctor"): au.append("doctor")
    gp = PHRASE.get(sid,"")
    if gp and gp.lower() not in ql: gp=""
    date = reddit_date(url) if st=="Reddit" else ""
    if not date and has(cap,"13 years ago"): date="~2013 (page label '13 years ago')"
    return dict(id=sid,quote=q,url=url,platform=plat,date=date,stars="",source_type=st,capture=capture,
        pain=J(pn),desire=J(ds),need=J(nd),objection=J(ob),failed_solution=J(fs),trigger=J(tr),misconception=J(mc),
        belief=J(bl),emotional_state=em,awareness_stage=aw,burned_skeptical=J(bs),authority_trusted=J(au),buyer_group=J(bg),great_phrase=gp)

def load():
    rows=[]; prev_url=None; skipped=[]
    for line in open(SRC,encoding="utf-8"):
        if not re.match(r"^S\d{3} \|",line): continue
        parts=[p.strip() for p in line.rstrip("\n").split(" | ")]
        sid,tags,qfield=parts[0],parts[1].split(),parts[2]
        cap=parts[-1]; url=parts[-2]; plat=" | ".join(parts[3:-2])
        if url=="same" or not url.startswith("http"): url=prev_url
        prev_url=url
        if plat in ("WTE",) : plat="What to Expect"
        quotes=[m.replace('\\"','"') for m in re.findall(r'"((?:[^"\\]|\\.)*)"',qfield)]
        quote=" / ".join(quotes) if quotes else qfield
        if sid in EXCLUDE: skipped.append((sid,EXCLUDE[sid])); continue
        rows.append(tag_row(sid,tags,quote,plat,url,cap))
    return rows,skipped

if __name__=="__main__":
    r,s=load(); print(len(r),"rows; excluded",s); print(r[0]); print(r[181])

# C — Parent Voice of Customer: Potty Training (toddlers → school-age)
Goal: find an underserved market / identity a potty-training-underwear brand could own.
Evidence file: `snippets.md` in this folder (252 numbered snippets S001–S252, each with tags, verbatim quote, platform, URL, capture type). Every quote below is cited by S-number.
Raw full-thread scrapes: `raw/` (What to Expect threads).

---

## 0. Method and how far to trust the numbers
- **Corpus:** 252 snippets from about 200 distinct URLs. Platforms: Reddit 170 (about 30 subreddits), What to Expect 39, Mumsnet 14, BabyCenter 5, retailer reviews 13 (Goodnites.com, Walmart, Sam's, Meijer, Dollar General, Pull-Ups), Instagram/Facebook 4, editorial 1.
- **Capture types:**
  - Reddit pages are blocked for Firecrawl scraping ("we do not support this site"), so all Reddit quotes are **search-result excerpts (SNIPPET)**. They are verbatim but short, and often thread titles.
  - What to Expect threads were scraped in full (FULL).
  - Mumsnet quotes are verbatim extractions WebFetch made from the full page (WF). WebFetch was asked for exact text, but I did not re-check each quote character by character.
  - BabyCenter: excerpts only.
- **Not obtained:**
  - Amazon review text. Scraping the product page returned no reviews, so retailer reviews stand in.
  - TikTok and YouTube comment threads (not indexed, and the search API was rate-limited).
  - Dr. Becky content.
  - The Goodnites.com reviews were labelled "13 years ago" on the page, so treat them as old (still a valid signal of a long-running gap).
- **Snippet counts are not prevalence.** I ran several queries per hypothesis, and more of them on neurodivergent (ND) kids because the brief asked for it. The tag counts below show where the *depth and emotion* is, not market share. For a better size signal, use these:
  - **Thread saturation:** every hypothesis query returned 10–15 distinct on-topic threads.
  - **Subreddit sizes.** These come from GummySearch pages. The snapshot date is unknown and may be stale.

| Subreddit | Members | Yearly growth |
|---|---|---|
| r/toddlers | 551k | +15.8%/yr |
| r/Autism_Parenting | 108k | **+42.5%/yr** |
| r/Preschoolers | 62k | +59.6%/yr |
| r/pottytraining | 49k | +26%/yr |
| r/ADHDparenting | 34k | **+68.3%/yr** |

### Tag counts (n = 252 snippets; one snippet can have several tags)
| Segment tag | n | Emotion tag | n | Failed-solution tag | n |
|---|---|---|---|---|---|
| ND (autism/ADHD/SPD/speech) | 92 | BURNOUT | 27 | 3-day / Oh Crap / naked | 20 |
| LATE (3.5y+ not day-trained) | 52 | JUDGE (family/school/strangers) | 24 | Pull-Ups | 18 |
| DEADLINE (daycare/preschool/school) | 38 | FAIL (guilt, "I'm a failure") | 16 | Training pants / cloth | 13 |
| NIGHT / bedwetting | 30 | SHAME / embarrassment | 14 | Rewards / stickers / bribes | 7 |
| WITHHOLD / constipation / fear | 24 | COMPARE | 5 | Gadgets (seats, potties, books) | 3 |
| POSTTRAIN (trained but daily accidents, 4–7y) | 16 | FEAR (child bullied/laughed at) | 5 | Potty watch | 1 |
| METHOD (anti-3-day vs child-led) | 16 | Any emotion tag | 77 | | |
| SIZE (product too small for older kid) | 14 | | | | |
| SENSORY (seams, fabric, wetness) | 13 | | | | |
| TWINS 10 · DAD 10 · REGRESS 7 · ECO 5 · DIGNITY 3 | | | | | |

Overlaps: ND and LATE appear together in 32 snippets, so most "late" stories in the ND world are long-timeline stories. ND or SENSORY appears in 96 snippets.

---

## 1. Ranked segments

### #1 — The "long-road" kids: neurodivergent (autistic, ADHD, sensory, speech-delayed) children still toilet-learning at 4–9 (Hypothesis (a): **CONFIRMED, strongest**)

**Size proxy**
- 92 ND-tagged snippets.
- r/Autism_Parenting has 108k members (+42.5%/yr) and r/ADHDparenting 34k (+68%/yr).
- Every ND query returned 12–15 distinct "not trained at 4/5/6" threads, for example "5 year old not potty trained", "6 year old refuses to potty train", "For kids who weren't potty trained by kindergarten" and "Diapers for 6 year old".
- There are dedicated forum boards for this: What to Expect "Autism", "ADD/ADHD", "Potty training"; Mumsnet "Special needs" and "SEN"; BabyCenter threads.

**Timeline (parent-reported):**
- "very common for autistic children to not be potty trained until they are 8" (S001)
- "pretty normal to take until 7-8" (S019)
- "only just out of nappies during the school day" at 5.5 (S226)
- "ready when he was ready to be ready, which turned out to be 9 years old" (S228)
- "took over 2 years" (S206)

**Desperation: very high.**
- "the most difficult thing I have literally ever done as a parent" (S194)
- "I'm giving up already!" (S020)
- "I am desperate for help" (S040)
- "a difficult and low reward journey" (S013)
- "on the wait-list to be on the wait-list" for occupational therapy (S196)
- Insurance "barely covers ... OT" (S205)
- Cost: "especially one with special needs is very expensive" (S231)

**What fails them, specifically**
1. **Methods built for neurotypical kids.**
   - "everything I read acts like this can be done in 3 days, over a weekend, or by keeping your child naked. These methods do not work with a child with SPD." (S198)
   - "definitely marketed towards neurotypical kids with no stomach problems" (S203)
   - "traditional potty training doesn't really work for autistic kids" (S209)
   - "Stop reading the books. They do not apply" (S199)
2. **Size ceiling.**
   - "The largest pull-ups are size 5t-6t and are starting to be..." (S018)
   - A 6-year-old in size 4T-5T training pants (S015)
   - "too big for many typical baby diapers but then still too small for adult-sized protection" (S243)
   - "I could not find diapers that fit her" (8yo autistic, S230)
   - Goodnites used as a daytime training pant "because of his weight" (S231)
   - Repeated "please make a bigger size" (S234, S232)
   - Parents hunt for brands that go "up to size 9" (S017, S021)
3. **Interoception.** The child cannot feel wet or full, so products that hide wetness (Pull-Ups) block learning, but plain underwear means floods.
   - "difficulty understanding the sensation of peeing" (S181)
   - "lowered interoception" (S039)
   - "If her brain can't hear her bladder, she needs a workaround" (S041)
   - "didn't feel his bodies signals" (S191)
   - What parents praise: absorbent *and* "allowed him to realize he was wet" (S021).
4. **Sensory intolerance of the garment itself.**
   - "cannot have anything touching her crotch, at all" (S026)
   - "all undies give her wedgies ... Elastic sucks?" (S027)
   - "hates butt seams" (S032)
   - "hypersensitive to the feeling of urine ... meltdown ... about wet socks" (S200)
   - Workarounds: "flat-locked seams" and "size up if ... red lines" (S037), boys' boxers (S030), "homemade underwear ... wide waistband" (S028), "autism friendly underpants on etsy" (S034).
   - Today sensory-friendly underwear and absorbent training underwear are **separate products**. Nobody combines them for older kids.
5. **Communication.** Speech-delayed and nonverbal kids cannot announce the need, so parents rely on timers, visuals and signs.
   - "Set a timer on repeat every 20 mins" (S005)
   - "Visual aids like picture schedules" (S007)
   - "we taught signs for potty pee and poop" (S-WTE in raw)
   - "thought he needed the language. he totally did not." (S185)
6. **School and outsiders.**
   - "Will the other children laugh at him? Will the teachers wish he wasn't there?" (S227)
   - "The school did have a problem with it and it was awful" (S229)
   - "could be lazy parenting or it could be autism" (S064)

**Parents' identity and beliefs:**
- They have given up the mainstream milestone clock, often after first blaming themselves.
- They speak in **"own timeline / different timetable / non-judgmentally / neuro-affirming"** language:
  - "ND children just have a different timetable" (S225)
  - "the toileting journey looks very different for autistic children" (S225)
  - "We just non judgmentally kept at it" (S191)
- They are researchers and system-builders (timers, visuals, ABA, OT, Miralax, signs).
- They are fiercely protective of the child's dignity and still carry a residue of judgment from outsiders.
- They form a self-identified community: dedicated subreddits and forum boards growing 40–70% a year.

**Competitive note:** Goodnites runs ADHD/autism bedwetting content and an Autism Society partnership, so the big incumbent is staking out **night** in this segment. I found no brand owning **daytime toilet-learning for ages 4–9 with sensory needs**.

---

### #2 — "Late" neurotypical trainers, 3.5–5, and the shame and judgment around them (Hypothesis (b): **CONFIRMED, as parent shame more than child shame**)

**Size proxy**
- 52 LATE snippets, of which about 20 are not ND.
- r/toddlers has 551k members.
- Titles are a genre of their own: "3 1/2 y/o STILL not potty trained", "At my wits end with almost 4 year old", "HELP-my 4.5 year old refuses", "I am a failure at potty training".

**Desperation: high, focused on the parent's self-worth.**
- "Potty training makes me hate myself, dislike my child" (S070)
- "making me resent my toddler" (S086)
- "I feel like a failure" (S080, S081, S085, S082)
- "like I've done something wrong and broke my child" (S174)
- "I feel like I'm the last !d!ot in the world" (S219)

**Judgment sources (24 JUDGE):**
- Grandparents and in-laws: "My mom keeps giving me so much slack ... he'll be made fun of at school" (S173); "should be potty trained by 2!" (S071); MIL/FIL (S072); "my 16 month old should be potty trained by now" (S075); "looks of disgust ... Makes me feel like a bad mother" (S074)
- Online strangers: "obliterated by these 'parents' ... terrible mother" (S081); "A 3 and 4 year old is long past the window" (S179)
- Lawmakers and teachers (S077, S078)
- Comparison: "Every parent we personally know under 3 years old has their kid already potty trained" (S189)

**What fails them:**
- Pull-Ups: "pull ups are a trap ... they also have no stake in becoming potty trained" (S182); "If I put pull-ups on them, they will happily go right away!" (S188)
- Rewards and gadgets: "Special toilet seat, cool undies, bribes, all of it. Nothing worked" (S178); "books, songs, cartoons, all models of potties...naked days" (S220)

**Belief split:**
- One camp says "you missed the window" (S179).
- The other camp follows the pediatrician: "doesn't recommend traditional potty training methods [over 3]. It can just cause a power struggle" (S176).

**Assessment:** This is a large and emotional group, but the identity is temporary. Most of these kids train within months, and parents want to *leave* the group, not belong to it. It works as an **acquisition moment** for #1 and #4, not as a standalone identity.

---

### #3 — Daycare / preschool / school deadline pressure (Hypothesis (d): **CONFIRMED as a trigger, not an identity**)

**Size proxy**
- 38 DEADLINE snippets.
- Rules are common: "pretty standard requirement for most preschools" (S090); "Ours does this. It's not uncommon." (S092)

**Desperation: acute and time-boxed.**
- "must be potty trained in one month or be dismissed from care" (S093)
- "Help before we get kicked out of preschool" (S091)
- "if they have too many accidents they will unenroll your child" (S094)
- "Preschool starts next month" (S088)
- Working parents: "I'm a teacher and go back to work soon. I cannot wait again until winter break" (S197); "expected to be in the office 4 days a week" (S224)
- UK: "starting Reception this Sept" (S216); "they will probabbly think I never bothered" (S218)
- Dad: "I feel like school think I'm a crap dad" (S221)

**What fails them:**
- The 3-day weekend promise: "3 day potty method…. Didn't really work. Now back to daycare" (S098)
- Pull-Ups at daycare: "pull-ups led to a huge months long regression" (S157)
- Schools that send kids home or demand nappies: "maybe it's best if hes put back in nappies" (S221 context); "teacher requested we put him back in pull ups" (S250)

**Assessment:** This is the most common *trigger* in the data. It pushes families into the shame zone, and for ND families into #1. It is a strong marketing hook ("school-ready", "accident-ready for school"), but the deadline passes, so the identity does not last.

---

### #4 — "Trained but not dry": 4–7-year-olds with daily accidents at school, plus night wetting (Hypotheses (c) and (g): **CONFIRMED; partly owned by incumbents at night**)

**Size proxy**
- 30 NIGHT and 16 POSTTRAIN snippets.
- r/kindergarten has a recurring thread type: "Kindergartener has accidents daily" (S125), "Daily pee accidents", "Potty Accidents - Starting Kindergarten in the Fall" (S128), "5.5 year old pees his pants at school everyday" (S129).

**Causes parents name:**
- Constipation: "Majority of pee accidents at this age are caused by long term constipation" (S127)
- ADHD play-absorption: "cannot stop what she is doing to go pee and pees her pants all day long" (S040); "hates interrupting his playtime" (S045)
- Night: hormonal, "a developmental stage, not a skill" (S115)

**Child-side shame (strongest here):**
- "embarrassed that he still wears a pull-up at night" (S119)
- "refused to wear a pull up after turning 7 it embarrassed him" (S121)
- "denying him sleepovers" (S122)
- "so his peers don't see his pull-up" (S123)
- Adult memory: "so much trauma and shame from my bedwetting growing up" (S114)

**The dignity pull:** Kids want real underwear even when not dry.
- "can I please try to sleep in my underwear" (S247)
- "refusing to wear pull ups for sleep" (S248)
- "They both don't want to be in diapers ... training underwear helped" (S116)
- Parents ask for "training underwear and disposable ... booster pads that she can discreetly change" (S249)

**What fails them:**
- Leaks in Pull-Ups and Goodnites: "leaking night pull-ups" (S112, S117); "leak EVERY night" (S232); "still leaks through the goodnites all over his sheets" (S239); "new design ... leaks every night" (S240)
- Sizing: "do not fit my 4 year old" (S241)
- Laundry and waste: "excessive, unnecessary amounts of laundry" (S238)
- Eco parents look for washable nighttime pull-ups (S161, S162), but this niche is small (ECO = 5).

**Assessment:** Night is a big category, but Goodnites and Pull-Ups Night own it with deep distribution. The **daytime discreet "real underwear with backup" for 4–7-year-olds at school** is less owned, and it overlaps heavily with #1 (ADHD and autism).

---

### #5 — Withholders: poop fear and constipation (Hypothesis (e): **CONFIRMED as desperate; weak fit for an underwear brand**)

**Size proxy**
- 24 WITHHOLD snippets.
- The query returned 15/15 on-topic threads.

**Desperation: extreme.**
- "Poop is ruining my life…. 2 months of stool witholding" (S108)
- "Toddler's fear of poop is running our lives" (S100)
- "it's starting to wreck us" (S109)
- "We've tried EVERYTHING" (S107)
- A 4-year-old who goes "weeks and weeks without pooping ... suppositories" (S171-thread)

**Solutions parents use:** Miralax, suppositories, timed sits, footstools, bubbles.
- "the best and easiest solution is Miralax" (S102)
- Squatty-potty success (WTE raw thread)
- The garment angle is mainly "give them a pull-up so they can poop" (S106), and kids hold "until naptime ... when he goes from underwear to a pull-up" (S195).

**Assessment:** This is a medical and behavioural problem, so underwear does not solve it. It feeds #1 (encopresis "very common amongst autistic children", S004) and #4 (constipation leads to pee accidents). Address it in content and community, not as the core market.

---

### #6 — Anti-pressure / child-led vs the "3-day" / Oh Crap culture (Hypothesis (f): **CONFIRMED as the ideological fault line, and the culture a brand can stand for**)

**Evidence:** F-3DAY 20 and METHOD 16 snippets. The backlash is loud and emotional:
- "The author of Oh Crap can go burn in hell" / "destroyed my confidence" (S146)
- "really doing all of us a disservice" (S139)
- "highly condescending" (S148)
- "convincing readers that if you try and fail, it's because you weren't paying close enough attention" (S149)
- "It feels like an even bigger failure knowing it didn't work" (S145)
- "so much pressure that she stopped" (S150)
- "Skills take longer to work on" (S201)

**The counter-creed parents articulate:**
- "No rewards, no punishments, no shame" (S144)
- "Call it learning and not training" (S167)
- "every kid is on their own timeline" (S069)
- "outdated belief that kids should be potty trained at 2" (S076)

The 3-day camp is still alive and recommended ("I second the oh crap method", WTE twins thread), so this is a real debate, not a consensus.

**Assessment:** This is not a segment by itself. It is the **belief system** that binds #1, #2 and #4. A brand that says "learning, not training; no deadlines; no shame; every body on its own timeline" lands directly on this wound.

---

### Small or not standalone (from the data)
- **Twins** (10): The pain is real ("hardest thing I've had to do with twins", S193; "can't afford the pull-ups anymore", S190), but small, and the needs match the late or ND segments.
- **Dads** (10): Mostly the same frustration ("Potty training is hell", S165; "worst part of parenting", S168). The distinct angle is a dad judged by school (S221). Not a separate need.
- **Regression after a sibling** (7): Transient. Weeks to months (S132–S136).
- **Eco / cloth** (5): Mostly complaints that training pants soak after one pee ("Big waste of money", S154). Too small to anchor a brand, but useful as a value layer (washable).

---

## 2. Recommendation: the market a brand could own
**"Long-road kids": children aged about 3.5–9 still learning to stay dry, led by neurodivergent kids (autism, ADHD, sensory, speech), and including late trainers and school-age kids with daily accidents. Their parents have rejected the 3-day, milestone-shaming culture.**

Why this group:
- **Bound by one painful problem:** "my kid is past the age the products and methods were designed for".
- **Has a self-made identity and growing communities:** ND parenting subs growing 40–70% a year; "different timetable", "non-judgmentally", "neuro-affirming".
- **Repeat-purchase need lasting years, not 3 days.**
- **Clear, unmet product specs** that incumbents do not combine:
  1. **Sizes past 5T-6T**, up to about 10–12, without looking like a diaper (S018, S015, S230–S234, S243).
  2. **Sensory-safe build:** tagless, flat or outside seams, soft wide waistband, no crotch bulk (S026–S032, S037).
  3. **Feel-wet but contain-it absorbency**, so the child can learn interoceptively without flooding the floor or classroom (S021, S183, S181, S039).
  4. **Dignity and discretion:** looks like real "big kid" underwear for school and sleepovers (S119–S123, S247–S249).
  5. **Support tools, not deadlines:** visual schedules, timer or watch cues, sign cards, school care-plan templates (S005, S007, S041, S227).
- **Incumbent gap:**
  - Pull-Ups stop at 5T-6T and are seen as "just diapers" (S156, S158).
  - Goodnites owns *night* and partners with autism groups, but leaks and sizing complaints persist (S232, S239–S241).
  - Toddler training-underwear brands are sized and styled for ages 2–4, and some parents call them a "waste of money" (S154, S164, S237).
  - Sensory-underwear brands are not absorbent.

**Kill or qualify list**
- (b) Late NT trainers: real, but a passing identity. Use as a funnel, not the core.
- (c) Night: real and big, but incumbent-owned. Enter via the daytime/night *system* for long-road kids, not head-on.
- (d) Deadline: the best trigger and messaging hook ("school-ready"), not an identity.
- (e) Withholding: desperate, but needs medical solutions. Treat as education content.
- (f) Anti-pressure: adopt it as the brand's creed.

---

## 3. Verbatim swipe file (parents' own words)
**Long-road / ND**
- "is very common for autistic children to not be potty trained until they are 8 years old." (S001)
- "I found my ASD child was ready when he was ready to be ready, which turned out to be 9 years old." (S228)
- "ND children just have a different timetable" (S225)
- "the toileting journey looks very different for autistic children" (S225)
- "If her brain can't hear her bladder, she needs a workaround." (S041)
- "I think he genuinely has difficulty understanding the sensation of peeing." (S181)
- "These methods do not work with a child with SPD." (S198)
- "Stop reading the books. They do not apply" (S199)
- "on the wait-list to be on the wait-list" (S196)
- "The largest pull-ups are size 5t-6t and are starting to be..." (S018)
- "too big for many typical baby diapers but then still too small for adult-sized protection" (S243)
- "She cannot have anything touching her crotch, at all." (S026)
- "all undies give her wedgies ... Elastic sucks?" (S027)
- "He's hypersensitive to the feeling of urine and wetness in general" (S200)
- "We just non judgmentally kept at it." (S191)
- "a difficult and low reward journey until it gets better one fine day" (S013)
- "Will the other children laugh at him? Will the teachers wish he wasn't there?" (S227)

**Shame, judgment, failure**
- "Potty training makes me hate myself, dislike my child" (S070)
- "like I've done something wrong and broke my child" (S174)
- "I feel like there's no excuse at 3.5 years old anymore." (S189)
- "I'm anxious of other people's judgement that it's lazy parenting" (S217)
- "they will probabbly think I never bothered." (S218)
- "I feel like school think I'm a crap dad" (S221)
- "looks of disgust ... Makes me feel like a bad mother." (S074)
- "33 month old nowhere near potty trained and it's honestly embarrassing" (S058)
- "Shamed by daycare over potty training" (S066)

**Methods and products**
- "Oh crap and the three day method thing destroyed my confidence" (S146)
- "if you try and fail, it's because you weren't paying close enough attention" (S149)
- "It feels like an even bigger failure knowing it didn't work" (S145)
- "Skills take longer to work on." (S201)
- "No rewards, no punishments, no shame." (S144)
- "Call it learning and not training." (S167)
- "pull ups are a trap" (S182)
- "they're just diaper" (S156)
- "the only difference ... is marketing" (S158)
- "Special toilet seat, cool undies, bribes, all of it. Nothing worked until he decided himself" (S178)
- "It will still get soaked and has to be changed after 1 pee. Big waste of money" (S154)
- "absorbes the mess well but still lets the kid feel wet that isn't $20 a pair?" (S242)

**Deadline**
- "must be potty trained in one month or be dismissed from care" (S093)
- "Help before we get kicked out of preschool" (S091)
- "I cannot wait again until winter break to try this." (S197)

**Kid dignity**
- "can I please try to sleep in my underwear" (S247)
- "embarrassed that he still wears a pull-up at night" (S119)
- "i can go to sleepover and no one knows" (S235)
- "saved my son embarrassment and helped him keep his independence" (S233)

---

## 4. Gaps and next steps
- Get **Amazon 1–2★ / 4–5★ review text** for training underwear: Gerber, MooMoo, Hanna Andersson, Pull-Ups 5T-6T, and sensory brands. This needs a scraper that supports Amazon reviews, or a manual export.
- Get **TikTok and YouTube comments** on Big Little Feelings, Oh Crap and Dr. Becky potty content, and on autism-toileting creators. Instagram reels exist (S245, S246) but the comments were not retrievable.
- **Validate size demand** by checking how many "size 7+ / older kid" training-underwear SKUs exist and their review volume.
- Search terms worth tracking: "potty training autistic 5 year old", "training underwear size 8", "sensory friendly underwear kids", "pull ups too small".

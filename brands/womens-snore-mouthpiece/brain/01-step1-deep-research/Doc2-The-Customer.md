# 👤 Doc 2 — The Customer

**Folder:** [Anti-Snoring Mouthpiece for Women — Step 1 Research (2026-11-23)](https://app.notion.com/p/421d53123cd6810dbc39fd43ab250416) · ICP: women 40–60 who snore · Markets: AU first → NZ · UK runner-up · US later · Meta only.

## Top 5 takeaways
1. **Her #1 core desire is love / connection: back in the same bed (124 rolled-up snippets), then identity, not being "the snorer" (103).** "Stop snoring" (43) is only the surface.
   - → Ads name the surface ("the snoring"); the brand sells "your side of the bed back" and "you're not the snorer any more".
2. **Her biggest moment is being SENT AWAY.** Spare room / separate rooms is the biggest sub-group (73 of 479), ahead of menopause-onset (59), apnoea worry (52) and dreading a shared room on trips (51). The data shows she's usually the one who leaves the bed, not him.
   - → Swap "He moved to the spare room. Bring him back." for her version: she's the one on the sofa.
3. **Embarrassment is the #1 pain (54), and the partner's complaint the #1 trigger (49).** Menopause onset is #2 trigger (37) and #1 belief ("it's my hormones", 41).
   - → Open ads on the moment he complains or she hears the recording, then explain the menopause link (Doc 3).
4. **What failed her most is the cheap mouthguard (95, mostly 1–2★ reviews), not tape (8).** The top objections are uncomfortable to sleep in (46), too big (38) and scam doubt (36); her top need is comfortable fit (59), then small mouth size (34).
   - → Lead the product page on fit: a true women's size, a gentle start, and a guarantee that covers an opened device. Tape stays one test cell only.
5. **She jokes about it, but it hurts.** Self-deprecating humour shows up in 53 snippets, next to frustration (111) and embarrassment (52). Phrases: "I sounded like a cartoon character", "a small truffle pig is sharing my bed. Mortifying.", "Apparently, I snore now. Thanks, perimenopause."
   - → Write in her frank, dry, wry voice (74 swipe phrases in §14), never clinical and never pitying.


---

# §2C · Customer data bank — summary

**What it is:** one local CSV, one row per snippet, every tag in its own column — `data/databank.csv`, **479 snippets** [S1]. Every count on Doc 2 is a python tally of that file (`data/tally.json`), never an estimate. The full bank becomes the §2C Sheet at delivery.

**Who is in it:** ICP only — women 40–60 who snore themselves (or someone describing HER snoring). Buyer group: icp_unknown_age 269 · icp_core 192 · partner_of_icp 18 [S1].

### Snippets per source type (6 types — the 4+ rule is met)
- reviews_other **145** (Trustpilot 78 · Walmart 67)
- forum **133** (Mumsnet 91 · Facebook groups/posts 40 · Menopause Matters 2)
- reddit **112**
- news_comments **75** (Daily Mail 45 · Telegraph 12 · WalesOnline 8 · Guardian 6 · NextTribe 4)
- x **10**
- video_comments **4**
- Solidity: VERBATIM 421 · SNIPPET 58. Country: GB 184 · unknown 154 · US 121 · CA 8 · AU 6 · NZ 3 · DE 2 · JE 1 [S1].

### What was removed or blocked (say it plainly)
- **19 rows removed as outside the ICP** before counting: 5 from a poster who is likely under 40, 4 "baby-weight" posts, 7 from one woman whose story is told at 63, 3 tape reviewers who never say they snore. **7 duplicates** (same URL + quote) removed.
- **Amazon review pages were sign-in-walled** (amazon.com and amazon.co.uk filtered review pages both redirect to sign-in — not bypassed). So **0 Amazon rows**. The 1–2★ and 4–5★ wording came from **Trustpilot + Walmart** instead (69 rows 1–2★ · 69 rows 4–5★ · 7 rows 3★). Amazon's own "Customers say" summaries are used as DATA in §10B.
- TikTok (login wall) and YouTube (captcha) were not bypassed → only 4 video comments. Facebook groups = search snippets only (login wall).

### Top 10 per tag (n of 479 — quotes live in their sections)
- **Pain:** embarrassed_snoring (54) · snoring_got_worse_menopause (42) · relationship_strain (42) · dread_sharing_room (38) · fear_sleep_apnoea (35) · partner_wakes_her (24) · tired_daytime (24) · wakes_self_up (24) · girls_trip_holiday_fear (24) · partner_moves_to_spare_room (23)
- **Desire:** stop_snoring (43) · wake_rested (25) · partner_sleeps (23) · sleep_in_same_bed (20) · share_room_without_shame (16) · avoid_cpap_or_surgery (15) · simple_fix_that_works (12) · not_be_the_snorer (3) · quiet_fix_privately (2) · feel_feminine_normal (2)
- **Need:** comfortable_fit (59) · small_mouth_size (34) · affordable (16) · no_jaw_pain (15) · works_first_night (13) · adjustable (10) · breathe_through_mouth_ok (9) · easy_to_clean (8) · discreet (4) · works_with_dentures_or_crowns (3)
- **Objection:** uncomfortable_sleep (46) · too_big_bulky (38) · scam_doubt (36) · jaw_pain_tmj (21) · price (18) · wont_stay_in (11) · fear_its_apnoea_needs_doctor (6) · looks_unattractive (6) · teeth_movement (6) · hygiene_smell (5)
- **Failed solution:** boil_bite_mouthguard (95) · apps_trackers (16) · weight_loss (14) · nasal_strips (11) · pillow_positional (11) · cpap (9) · mouth_tape (8) · side_sleeping_tennis_ball (7) · nasal_spray (6) · doctor_dismissed (5)
- **Trigger:** partner_complaint (49) · menopause_onset (37) · recording_heard (21) · weight_gain (11) · holiday_shared_room (11) · child_comment (10) · girls_trip_upcoming (9) · friend_comment (9) · new_relationship (7) · partner_moved_out_of_bed (6)
- **Misconception:** only_men_snore (9) · nothing_can_be_done (7) · denial_i_dont_snore (6) · need_dentist_custom_only (4) · tape_fixes_all_snoring (2) · snoring_is_harmless (2) · only_overweight_people_snore (2) · mouthguards_are_for_grinding (1) · side_sleeping_fixes_it (1) · its_just_allergies (1)
- **Belief:** it_is_menopause_hormones (41) · it_is_my_weight (27) · snoring_is_unladylike (14) · its_my_nose (12) · cheap_devices_dont_work (7) · i_must_have_apnoea (7) · devices_are_uncomfortable (6) · alcohol_makes_it_worse (2) · nothing_works_for_me (1) · cpap_is_unattractive (1)
- **Emotional state:** frustration (111) · relief (90) · humour_self_deprecating (53) · embarrassment (52) · resignation_apathy (37) · grief_sadness (33) · anger (32) · anxiety (32) · guilt (28) · shame (27)
- **Awareness stage:** problem_aware (220) · product_aware (107) · most_aware (76) · solution_aware (66) · unaware (10)
- **Burned / skeptical:** no (370) · yes (109)
- **Authority they trust:** partner (31) · sleep_clinic (24) · dentist (15) · gp_doctor (13) · friend (5) · brand:sleeppro (5) · ent (4) · brand:vitalsleep (2) · brand:snoreeze (2) · brand:snorelab (2)
- **Buyer group:** icp_unknown_age (269) · icp_core (192) · partner_of_icp (18)
- **Great phrase:** 377 of 479 rows carry one (free text, not a label) → the §14 swipe

**So What → do this:** treat the bank as the single source for every list below; the loudest signals are embarrassment, the menopause link, the spare room and the shared room — and the #1 product failure is a mouthguard that didn't fit her.

---

# §3 · Ideal customer (ICP)

**One real person:** a woman in her mid-40s to late 50s (INFERENCE from the 97 rows aged 40–60), married or with a long-term partner, in peri- or post-menopause, who never used to snore (or only "cute" snores) and now does — loudly. Her husband nudges, shoves or leaves; she ends up in the spare room or turning down trips with friends. She has tried strips, tape, sprays or a cheap mouthguard. She lives in the UK first (Mumsnet is her voice), then AU/NZ/US.

> SimilarWeb failed for every competitor domain this run, so there is **no audience-demographics data**. Every field below shows the §2C count behind it; anything the bank does not show is marked **INFERENCE**.

### Required fields
- **Age range:** 40–60 (set by Nikita). Bank: 101 rows carry a number age; **97 of them are 40–60** (40–49: 49 rows · 50–60: 48 rows; 4 outside: 30, 30, 38, 62) [S1]. Peak 50–59 = INFERENCE from the science (D1/D3), not the bank. Note: one person can give several rows (news articles), so these are row counts, not people.
- **Life stage:** peri- / post-menopause. **138 rows** carry a menopause/peri signal (age column or quote); belief "it's menopause hormones" 41; trigger "menopause onset" 37 [S1]. Kids mostly older (teen/adult daughters, a 17-year-old son, grandchildren in 2 rows) — thin, INFERENCE.
- **Household:** married / partnered. Husband, DH, hubby, partner, boyfriend or fiancé is named in **114 quotes** (husband/DH/hubby alone: 79) [S1]. Partner is the #1 authority (31) and #1 trigger (49).
- **Income band:** **INFERENCE** — middle income, price-aware but pays to fix it. Bank signals: price objection 18 · "affordable" need 16 · she pays extra for her own room on trips (own/extra room in 7 quotes) [S1].
- **Job type:** **INFERENCE** — only 1 quote names a job ("a stressful job"); she works or is retiring; not a lever.
- **Country / urban–rural:** GB 184 of 479 (38%) · US 121 · AU/NZ 9 [S1]. Urban vs rural: no data — **INFERENCE** (Mumsnet/Daily Mail = suburban UK).
- **A typical day when the problem hits:** the night, not the day. Somewhere between midnight and 5am he nudges, shoves, claps or shouts; she gets up and goes to the spare room; next day she's tired and he complains. Partner wakes her 24 · tired in the day 24 · wakes herself up 24 [S1]. In her words: "Dh and I are in a bedroom with two single beds. I must have been snoring and he couldn't reach over to shake me as he'd usually do. He loudly clapped, two different occasions and then shouted out my name." [S2 · VERBATIM]

### Worldview (written as one of them)
- **Religious:** **INFERENCE** — nothing in 479 snippets; only 3 rows use "bless"/"prayers" as a figure of speech. Not a lever; keep copy secular.
- **Political:** **INFERENCE** apart from one theme — she feels let down by the health system and handles it herself. US: "I am American so I can't afford health insurance and am out here raw-dogging it" [S3 · VERBATIM]. (UK version — NHS waiting lists — quoted in §10 under "a simple fix that works".)
- **Social:** to her, snoring is something old, overweight men do — not women like her. Belief "snoring is unladylike" 14 · misconception "only men snore" 9 [S1]. "We often feel like this is a un-sexy condition of older, overweight men who snore loudly. Trust me, it is not!" [S4 · VERBATIM]
- **Economic:** she'll pay for peace, but hates wasting money on gadgets that don't work (scam/waste objection 36). "It causes issues if we booking a cottage or apartment cos we need to find one with an extra room (I always pay more which is fine)." [S5 · VERBATIM]
- **Prejudices / eye-rolls:** she rolls her eyes at the husband who snores too but blames her, at fake reviews, and at "just lose weight". "My husband says I snore. Yet, I ask you why am I the only one awake?" [S6 · VERBATIM] · "How can a prospective buyer believe a review?" [S7 · 1★ · VERBATIM]
- **Who "gets it":** other women in menopause, not men and not doctors. "People are often super-blaming on the snoring partner til they start snoring themselves in menopause, when it becomes them at fault too." [S8 · SNIPPET]
- **Life, love & family (1–3 sentences):** Marriage is closeness — sharing a bed is part of being a couple, and losing it feels like the start of drifting apart. Family and friends matter: she wants to be the mum, sister and friend who comes on the trip, not the one who books a room alone. INFERENCE built on relationship strain 42 · dread sharing a room 38 [S1] and: "we started sleeping in separate rooms, which is fine. … when we go on vacation we sleep together and snoring is not a problem, but we still sleep in separate rooms most nights." [S9 · VERBATIM]

**So What → do this:** write every ad to a married UK woman in menopause who has just been "told" she snores — her husband and her friends are the audience she fears, not her health. Keep it secular, plain, a bit funny, and never preachy about weight.

---

# §3A · Sub-avatars (the scale targets)

**Framing, said plainly:** Nikita ordered **ICP-only research** for this run. So these are not other buyer groups (no men, no gift-buyers, no younger women) — they are the **real sub-groups INSIDE women 40–60 who snore** that the §2C bank shows. Size = how many of the 479 snippets fall in each group (python over the tag columns; a snippet can sit in more than one group — **288 of 479** fall in at least one). Ranked by size.

### 1 · Sent to (or left in) the spare room — 73 snippets
- **Who:** married/partnered; he moves out of the bed, or she's sent to the spare room. Tags: relationship strain, partner moves out, separate bedrooms, wants the same bed. 35 icp_core · GB 38.
- **#1 pain (relationship strain 42), her words:** "It’s a sad state of affairs when you are dumped in the middle of the night, every night. … First I’ll get a gentle nudge and be politely asked to roll over on to my side. Then, after 10 minutes, I’ll be told to “STOP SNORING” and be given a shove." [S10 · VERBATIM]
- **Where she gathers:** Mumsnet AIBU + Chat (19 snippets), r/snoring (7), Daily Mail / Telegraph comment readers (15), HerSpace Perimenopause & Menopause Support (Facebook) [S1].
- **Opening angle (our line):** *Back in your own bed* — the empty-bed morning, not the noise.

### 2 · Menopause-onset snorers (never used to snore) — 59 snippets
- **Who:** snoring started or got much worse in peri/menopause; she links it to hormones. 50 icp_core.
- **#1 pain (snoring got worse with menopause 42), her words:** "only ever snored after a drinking sesh or if I had a bad head cold and was 'wee, cute snores'. Now it's EVERY night." [S11 · VERBATIM]
- **Where she gathers:** r/Menopause (11), r/Perimenopause (5), r/WomenOver40, Facebook HerSpace group (7 snippets), Mumsnet Chat [S1].
- **Opening angle (our line):** her own title *Suddenly I snore…* — name the menopause change as the cause (not her weight, not her fault), then the jaw-forward fix. Watch: AirVex already runs "menopause snoring" in GB (see §2).

### 3 · Apnoea worriers (afraid it is something worse) — 52 snippets
- **Who:** scared it's sleep apnoea; some diagnosed, some on CPAP and hating it. 23 icp_core.
- **#1 pain (fear of sleep apnoea 35), her words:** "yes can be. get it tested, sleep apnea is a killer" [S12 · VERBATIM]
- **Where she gathers:** r/Menopause (12), r/Zepbound, r/fitbit, r/GenX, Guardian readers [S1].
- **Opening angle (our line, careful):** *Snoring — or something more? Check with your GP first. If it's simple snoring, here's the quiet option.* Never "treats apnoea" (regulatory: snoring-only claim).

### 4 · Room-sharers (girls' trips, holidays, family stays) — 51 snippets
- **Who:** dreads the shared room; books her own room or says no. Most UK (GB 37).
- **#1 pain (dread sharing a room 38), her words:** "when I stay away with friends I'm always mortified that next day they say how I've kept them awake all night and they so tired and how awful my snoring is." [S5 · VERBATIM]
- **Where she gathers:** Mumsnet Chat (20 snippets — hen party, girls' weekend, hotel-room threads), Daily Mail, WalesOnline, Facebook travel/retreat groups [S1].
- **Opening angle (our line):** *Say yes to the girls' weekend* — the next-morning comment, solved before the trip.

### 5 · Burned by a mouthguard that was too big — 46 snippets
- **Who:** already bought a mouthpiece; it was made for a man's mouth. Mostly reviews (US 36, GB 5). Tags: too big/bulky, small mouth.
- **#1 pain (too big 38 / small mouth 34), her words:** "I’m an average sized woman and this device is HUGE! There is no way I could get it in my mouth." [S13 · 1★ · VERBATIM]
- **Where she gathers:** Trustpilot pages of VitalSleep, SnoreRx, SleepMD, Sleepzee, Snoreeze; Walmart SnoreMD reviews [S1].
- **Opening angle (our line):** *It wasn't the idea that failed — it was the size.* A slimmer fit made for her mouth.

### Also in the bank (smaller — test after the top 5)
- **Weight-gain snorers — 35:** "Over the last few months I've turned into a snorer, I wake me self up with my grunts and poor DH hasn't had a good night sleep since." [S14 · VERBATIM] Mumsnet Chat + r/Menopause.
- **Tape / strip / spray switchers — 37 (28 by failed-solution tag + mentions):** "I’ve tried loads of things… making sure I lie on my side, sprays, snoring strips and I’m lying here at 2am and I’ve just ordered some awful mouth guard thing." [S15 · VERBATIM] r/Menopause (9), r/snoring.
- **New relationship — 14:** "I'm quite paranoid about having a new partner." [S16 · VERBATIM] r/snoring, Mumsnet Chat.

**So What → do this:** launch to the ICP with the **spare-room** and **menopause-onset** stories; scale next into **room-sharers** (girls' trip) and **burned-by-a-big-mouthguard** — both have their own ready-made hook. Keep apnoea worriers for later and only with a GP line.

---

# §10 · Everything about the ICP

All lists = every distinct label in the §2C bank, highest first, "n of 479" [S1]. Quotes are the bank's best unused ones for that label. §10B (failed solutions) and §11 (objections) go deeper and refer back to these items by name.

## Pains (24)
1. **Embarrassed that she snores** — 54 of 479 · "I feel guilty for keeping him awake, I feel really unattractive, quite embarrassed by it and because of this don’t like to talk about it." [S15 · VERBATIM] · "Feel very embarrassed, bad for DH and it’s putting me off going away with friends ☹️." [S17 · VERBATIM]
2. **Snoring started / got worse with menopause** — 42 of 479 · "I snore - not overweight, like a glass of wine but snore when I don't have anything to drink. I think it's meno related as only started relativley recently" [S5 · VERBATIM] · "Paul has complained that I snore only since I started the change in late 2010." [S18 · VERBATIM]
3. **Relationship strain** — 42 of 479 · "I'm mortified that Steven has to watch and listen to me snoring; it can't be appealing to see your wife, mouth open, snoring like a pig. I worry it may drive a wedge between us if it carries on and we sleep apart more often." [S18 · VERBATIM] · "Steven is very placid but my snoring causes us to snap and if I pour a glass of wine to unwind, Steven winces, aware that alcohol makes my snoring worse." [S18 · VERBATIM]
4. **Dreads sharing a room** — 38 of 479 · "We went away once with extended family and they said they could hear me through the bedroom walls." [S19 · VERBATIM] · "My snoring means I avoid going on trips away with other people because I’m so embarrassed. I can’t go away with my sister, for example, because she hates noise and wouldn’t be able to sleep." [S19 · VERBATIM]
5. **Fear it's sleep apnoea** — 35 of 479 · "I could hear myself go quiet, then I’d be gasping for breath and snoring really loudly. I knew something wasn’t right." [S19 · VERBATIM] · "By this point I was beyond exhausted. I was falling asleep in the day and I was drowsy when driving." [S19 · VERBATIM]
6. **Partner wakes her (nudge, shake, shove)** — 24 of 479 · "My partner sleeps with earplugs but if he can still hear me he shakes me awake and asks me to turn over." [S20 · VERBATIM] · "Three or four nights a week he has to wake me in an attempt to stop the racket and once a week he decamps to the sofa" [S18 · VERBATIM]
7. **Tired in the day** — 24 of 479 · "I was so exhausted I was snoring so my husband shoved my arm to make me stop snoring!!!! Now I’m wide awake and mad as shit!" [S21 · VERBATIM] · "I am miserable because I can’t sleep. It’s 6:30am and I’ve been awake since 4am" [S22 · VERBATIM]
8. **Wakes herself up** — 24 of 479 · "I snore terribly every single night. As a child I used to wake myself up with my snoring, but it’s got worse as I’ve got older." [S19 · VERBATIM] · "I’m also often realising I'm snoring before I'm fully asleep. It seems to be back of the throat snores rather than nasal." [S11 · VERBATIM]
9. **Girls' trip / holiday fear** — 24 of 479 · "Socially, I have turned down caravanning holidays with friends knowing that I would make their break a nightmare due to my loud snoring. It is hugely embarrassing." [S23 · VERBATIM] · "Historically, on girls' weekends, I have always been the number one room (or even bed) choice. Not only do I sleep on my back, arms crossed like a vampire in a coffin and still, but I am entirely silent." [S24 · VERBATIM]
10. **He moves to the spare room** — 23 of 479 · "Most mornings, I sleepily stretch my arm across the bed to reach for Paul only to discover he has decamped to the spare bedroom to escape my thunderous snoring. Again." [S18 · VERBATIM] · "After 17 years of marriage waking to an empty bed leaves me feeling fretful and insecure." [S18 · VERBATIM]
11. **Separate bedrooms** — 23 of 479 · "shall I just admit that our days of sharing a bed are over and make myself comfortable with a new mattress in the spare room?" [S15 · VERBATIM] · "I believe it definitely played a part in the breakdown of my marriage as my nasal nocturnal orchestra meant that my husband refused to sleep in the same room as me, let alone the same bed." [S23 · VERBATIM]
12. **Snoring after weight gain** — 19 of 479 · "I'm 47 years old. Not on HRT. I have started snoring for the first time in my life. I am not overweight but have gained 10 pounds over the last year despite a lot of effort. Has anyone else had this problem? Is it the weight or also the hormones?" [S25 · VERBATIM] · "my husband says I don’t snore anymore and that before starting zepbound my snoring was getting louder and louder" [S26 · VERBATIM]
13. **Shock at hearing a recording** — 16 of 479 · "It was only when James recorded my snoring on my phone that I realised just how bad I sounded. It didn’t even sound human!" [S19 · VERBATIM] · "He once recorded me snoring and even replayed it back to our friends to prove how loud I was. When I heard it I was pretty shocked. I sounded like a cartoon character." [S19 · VERBATIM]
14. **Feels unfeminine / unsexy** — 16 of 479 · "We have just celebrated our 19th wedding anniversary but even the security of a long marriage does not stop my snoring from leaving me feeling embarrassed and decidedly unsexy." [S18 · VERBATIM] · "my self-confidence has diminished, so there is a knock-on effect." [S18 · VERBATIM]
15. **Dry mouth / sore throat** — 12 of 479 · "I’d wake up with a really dry mouth. My tongue would be white from dehydration." [S27 · VERBATIM] · "Yeah…I recently started mouth taping because my mouth would fall open and I’d snore/wake up with a nasty super dry mouth and throat. every few hours." [S28 · VERBATIM]
16. **Partner jokes / teases** — 5 of 479 · "People see snoring as a bit of a joke, but it’s affected my life," [S23 · VERBATIM] · "I am, but luckily not that frequently, and not loud enough to initiate divorce proceedings according to DH 😬" [S16 · VERBATIM]
17. **Got worse with age** — 4 of 479 · "When I hit my mid-50s, my silent slumber disappeared to the dismay of my husband. I began snoring on a semi-regular basis—and snoring loudly. He can sometimes hear me snoring from the living room, several rooms away." [S29 · VERBATIM]
18. **Hospital or shared ward** — 3 of 479 · "When I travel with friends I always book my own room. I dread having to go into hospital or anything like that." [S16 · VERBATIM]
19. **Can't sleep on her back** — 2 of 479 · "I'm a 46 year old slim female and I apparently snore like a freight train. My partner is so loving and understanding but he never gets a good nights sleep (nor do l!) he says it's worse on my back but I still do on my side sometimes and I have TMJ which apparently obstructs airway." [S30 · VERBATIM]
20. **Low self-confidence** — 2 of 479 · "I was probably a little bit in denial for a while. You don’t feel very good about yourself in menopause anyway. Throw this into the equation and it really wasn’t a nice time." [S27 · VERBATIM]
21. **Partner can't sleep** — 2 of 479 · (partner's words) "She's blissfully unaware, while I'm lying there desperately trying to block it out with my pillow." [S18 · VERBATIM]
22. **Partner wears earplugs** — 1 of 479 · "I totally agree I'm a snorer & my partner doesn't snore at all.He wears ear plugs." [S19 · VERBATIM]
23. **Social isolation** — 1 of 479 · "Consequently, I have turned down all events with shared accommodation rather than really annoy and lose good friends." [S23 · VERBATIM]
24. **Fear of snoring in public (plane)** — 1 of 479 · "Ladies I need help with snoring. I snore loudly regularly but hubby usually nudges me on the plane. Travelling by myself to the west coast so I know" [S31 · SNIPPET]

## Objections (14) — §11 answers each
1. **Uncomfortable to sleep in** — 46 of 479 · "The fit is uncomfortable but not completely unwearable." [S32 · 1★ · VERBATIM]
2. **Too big / bulky** — 38 of 479 · "If you have a small mouth - these will not work for you." [S32 · 1★ · VERBATIM] · "I do have a small mouth and narrow arches. This item is much too large and thus extremely uncomfortable. so... small mouths beware." [S32 · 1★ · VERBATIM]
3. **"It's a scam / waste of money"** — 36 of 479 · "Total waste of money. Uncomfortable, stiff, and doesn't fit or work." [S33 · 1★ · VERBATIM] · "it does not work it forms to your mouth but not like it should , I still snored" [S32 · 1★ · VERBATIM]
4. **Jaw pain / TMJ** — 21 of 479 · "it didnt fit my jaw size and it made me open my mouth superwide while it was in. i was concnered if i would get a jaw cramp." [S32 · 1★ · VERBATIM] · "made my mouth hurt to bad. the fit on my teeth was so tight that it made my teeth hurt" [S32 · 1★ · VERBATIM]
5. **Price** — 18 of 479 · "these also do not work they have been a complete waste of money,also expensive at £9.99 from boots for 16 tablets." [S34 · 1★ · VERBATIM]
6. **Won't stay in** — 11 of 479 · "It moved all night back and forth and was super uncomfortable" [S32 · 1★ · VERBATIM] · "Terrible, does not stay in! A waste of money." [S33 · 1★ · VERBATIM]
7. **"It might be apnoea — I need a doctor"** — 6 of 479 · "If you find that you do snore, or are having breathing issues in the night, you really should sign up for a sleep study. These are brutal and I never want to do one again" [S35 · VERBATIM] · "I have always put off going to the doctors because they will say its because i am overweight." [S14 · VERBATIM]
8. **Looks unattractive** — 6 of 479 · "She looks like a fighter pilot about to hit some G-forces, or an elephantine robot." [S29 · VERBATIM]
9. **Teeth will move** — 6 of 479 · "The device caused my teeth to move." [S36 · 1★ · VERBATIM] · "I am noticing that my jaw shifts some changing my bite. My jaw aches some at the joint in the morning." [S37 · 5★ · VERBATIM]
10. **Hygiene / smell / mould** — 5 of 479 · "Main complaint is mold. There are too many crannies to clean it daily" [S38 · 1★ · VERBATIM] · "I ended up getting an infection in my mouth after using this product that required me to go to the doctor three times" [S39 · 1★ · VERBATIM]
11. **Already tried a mouthguard — failed** — 3 of 479 · "pillows, vapours, different positions, nose strips, mouth guards. Nothing seems to help me." [S40 · VERBATIM] · "my snoring was quite loud and irritating to someone….. CPAP didn't work (I hated the hoses) , mouth piece didn't work, and nasal strips didn't work." [S41 · SNIPPET]
12. **Can't wear with crowns / dentures** — 3 of 479 · "If you have dentures, dental implants, asthma or sleep apnea, it's suggested to not use this. This was no where on the online information!" [S32 · 2★ · VERBATIM]
13. **Gag reflex** — 3 of 479 · "I am having trouble with it at the moment it seems to be too big and I am gaging when I put it in my mouth." [S42 · 5★ · VERBATIM] · "you’re effectively sticking a piece of wire down your throat and your gag reflex kicks in." [S10 · VERBATIM]
14. **Drooling** — 1 of 479 · "it is uncomfortable, and so thick you cant shut your mouth, so you dribble. absolute con." [S43 · 1★ · UNVERIFIED: the S43 URL holds a different Sleepzee review (returns refused for "hygiene reasons"); this wording was not found at the source. Do not use in creative until re-sourced]

## Needs (10)
1. **Comfortable fit** — 59 of 479 · "I've tried a cheap one and found it to uncomfortable." [S44 · VERBATIM] · "Comfortable and after a couple if nights i got used to it." [S45 · 5★ · VERBATIM]
2. **Fits a small mouth** — 34 of 479 · "Too bloody big for my mouth followed instructions but its not comfortable and held my mouth wide money wasted that I won't get back" [S46 · 1★ · VERBATIM] · "I think in theory this a brilliant product but not suitable for a small mouths, I have tried many time but its simply to big for my mouth." [S47 · 3★ · VERBATIM]
3. **Affordable** — 16 of 479 · "It's about $10 on Amazon for a 30-day Supply and worth every penny!" [S48 · VERBATIM] · "recommended a mouth piece. For $2500 au!!!" [S30 · VERBATIM]
4. **No jaw pain** — 15 of 479 · "I got the SnoreRx Plus mouth guard and while it did stop my snoring which was great (I used an app to measure), it was too big for my mouth and I was nervous it was gonna mess up my jaw. So I returned it" [S49 · 3★ · VERBATIM]
5. **Works the first night** — 13 of 479 · "The first night I wore it, the snoring stopped and i slept more peacefully." [S50 · VERBATIM] · "SnoreGym and SnoreLab and why tf do I have to exercise my mouth?? Can’t anything just keep working?? /whineover" [S51 · VERBATIM]
6. **Adjustable** — 10 of 479 · "Easy to fit, adjustable" [S32 · 5★ · VERBATIM] · "when you first use it don’t advance your jaw and get used to it for a couple of days. Then you can advance as much or little as needed." [S15 · VERBATIM]
7. **Can still breathe through her mouth** — 9 of 479 · "It actually isnt restrictive, i can cough in it!" [S44 · VERBATIM] · "loosely on the sides and leaving a hole in the middle where my mouth could breathe if needed" [S52 · VERBATIM]
8. **Easy to clean** — 8 of 479 · "one didn’t clean up very well (after a few weeks I was grossed out)" [S53 · 5★ · VERBATIM]
9. **Discreet** — 4 of 479 · "For a quick and discreet test, first find a free snoring app for your smartphone." [S35 · VERBATIM]
10. **Works with dentures / crowns** — 3 of 479 · "Cannot be used with dentures. They did not mention this." [S54 · 1★ · VERBATIM] · "No dental work - not sure how many do t have some kind of dental work" [S55 · 2★ · VERBATIM]

## Core desires / dream outcome (11) — laddered in §10A
1. **Stop snoring** — 43 of 479 · "Better than snoring though. And I'll do anything that helps me to get a good night's sleep." [S24 · VERBATIM] · "he told me “Hey, I think you stopped snoring.”" [S56 · VERBATIM]
2. **Wake rested** — 25 of 479 · "I'd pay anything to sleep well." [S24 · VERBATIM] · "I sleep better too because I’m not waking up to drink water or because I snort myself awake." [S57 · VERBATIM]
3. **Let him sleep** — 23 of 479 · "Looking for solutions so my poor man can rest." [S58 · VERBATIM] · "my husband has stopped complaining as he is now able to get enough sleep." [S24 · VERBATIM]
4. **Sleep in the same bed again** — 20 of 479 · "We enjoy that lovely closeness of falling asleep, legs and arms entwined. It's one of many things that helps to foster a loving feeling towards one another and I don't want to lose that." [S18 · VERBATIM] · "I worry how our relationship will be affected if we have to continue sleeping separately 90 per cent of the time, just as we have done for the past two years." [S18 · VERBATIM]
5. **Share a room without shame** — 16 of 479 · "Now if someone asked me to share a room with them it wouldn’t bother me." [S23 · VERBATIM] · "What if I've been snoring for years and everyone has just been too polite to mention it? I feel retrospectively self-conscious and concerned about future trips." [S24 · VERBATIM]
6. **Avoid CPAP or surgery** — 15 of 479 · "none of the masks would fit. The air was blowing so violently, it was seeping out the sides, burning my eyes" [S27 · VERBATIM] · "I fully resisted a CPAP due to claustrophobia" [S59 · VERBATIM]
7. **A simple fix that works** — 12 of 479 · "I'd love a sleep study but the NHS just has waiting lists years long so shall try mouth tape and side sleeping first n see." [S60 · VERBATIM] · "Definitely going to get tape today as nose clear and it's definitely a mouth breathing snore issue. :) Thanks." [S61 · VERBATIM]
8. **Not be "the snorer"** — 3 of 479 · "I’m a petite woman, not the type you’d expect to snore as loud as I do." [S62 · 5★ · VERBATIM] · "I started a new relationship with a light sleeper and was afraid my snoring might be a deal breaker." [S63 · 5★ · VERBATIM]
9. **Fix it quietly / privately** — 2 of 479 · same 2 snippets as "a simple fix" (NHS waits) and "fear of snoring in public" (flying alone) above.
10. **Feel feminine / normal** — 2 of 479 · same 2 snippets as "relationship strain" #1 and "feels unfeminine" #1 above.
11. **Works the first night** — 1 of 479 · "my husband -- who gets up very early -- said he had to check to make sure I was still breathing since he didn't hear me snoring like usual." [S59 · VERBATIM]

## Misconceptions (10)
1. **Only men snore** — 9 of 479 · "My first thought was that there was no way I had sleep apnea because I don't fit the "stereotype" typically associated with this disorder." [S64 · VERBATIM] · "See, i honestly didn't realize that many women did snore." [S65 · VERBATIM]
2. **Nothing can be done** — 7 of 479 · "GP confirmed that so long as I didn't have the kind that stop breathing even for very short periods, snoring doesn't do any harm and can't necessarily be cured, apart from rolling over etc." [S66 · VERBATIM] · "I saw my GP and apparently my throat is extra narrow - so it's anatomical 😭😭😭" [S16 · VERBATIM]
3. **"I don't snore"** — 6 of 479 · "My husband says I snore…
Clearly I don’t, it’s purring 😉" [S67 · VERBATIM] · (partner) "sometimes even trying to convince me that she hasn't been snoring at all." [S18 · VERBATIM]
4. **Only a dentist's custom device works** — 4 of 479 · "I've even recommended it to my dentist as an alternative to expensive appliances" [S68 · 5★ · VERBATIM]
5. **Tape fixes all snoring** — 2 of 479 · "I just stared mouth taping about a week ago and WOW!" [S69 · VERBATIM]
6. **Snoring is harmless** — 2 of 479 · same 2 snippets as "nothing can be done" #1 (GP) and "partner jokes" #1 above.
7. **Only overweight people snore** — 2 of 479 · "After my 2nd banding in Feb my snoring volume which was sort of cute (according to my husband), has really gotten loud.. I am not heavy" [S70 · SNIPPET] · "my snoring? I'm not overweight, or have any of the well known" [S71 · SNIPPET]
8. **Mouthguards are only for grinding** — 1 of 479 · "I use a mouth guard to stop me grinding my teeth, but I still snore! Is it a different sort of mouth guard that stops you snoring?" [S44 · VERBATIM]
9. **Side sleeping fixes it** — 1 of 479 · "I snore whether I'm on side or back." [S72 · SNIPPET]
10. **It's just allergies** — 1 of 479 · "I felt like I was being nudged awake, and have allergies so from time to time I snore, but always attributed it to the allergies" [S73 · SNIPPET]

## Mindset (psychographics)
**Beliefs she holds (10)** — §9B works these:
- It's menopause hormones 41 of 479 · "I assume I've now got a crazy wrinkly throat on the inside to match the outside ... Perhaps it just flops around non-stop." [S74 · VERBATIM]
- It's my weight 27 of 479 · "my snoring disappeared completely for like 2 weeks when I started. But the snoring comes back in waves" [S75 · VERBATIM]
- Snoring is unladylike 14 of 479 · "Not to mention unladylike, monstrous, embarrassed and unattractive." [S40 · VERBATIM]
- It's my nose 12 of 479 · "I have had sinus issues since being a child and I try my best but it persists." [S16 · VERBATIM]
- Cheap devices don't work 7 of 479 · "I was silly in my hopefulness in this product." [S76 · 1★ · VERBATIM]
- I must have apnoea 7 of 479 · "Having lain awake next to me listening to my snoring one night, she was convinced that I was also suffering from sleep apnoea" [S18 · VERBATIM]
- Devices are uncomfortable 6 of 479 · "I’m glad I don’t snore too bad for my husband because none of these look very comfortable." [S77 · VERBATIM]
- Alcohol makes it worse 2 of 479 · same snippet as "relationship strain" #2 above.
- Nothing works for me 1 of 479 · "I had an operation at 12 years old to have them removed, but it didn’t make a difference." [S19 · VERBATIM]
- CPAP is unattractive 1 of 479 · same snippet as "looks unattractive" above.

**Emotional states (14):** frustration 111 · relief 90 · self-deprecating humour 53 · embarrassment 52 · resignation 37 · grief/sadness 33 · anger 32 · anxiety 32 · guilt 28 · shame 27 · fear 26 · hope 20 · shock 6 · pride 4 [S1]. (Quotes: §14 buckets; ladder: Doc 3 §6.) Read: she jokes about it in public and cries about it in private. Burned/skeptical = **109 of 479**.

**Key experiences & moments:** ranked in §18 (partner complaint 49 · menopause onset 37 · hearing a recording 21 …).

**What she's tried and failed:** ranked in §10B (boil-and-bite mouthguard 95 · apps 16 · weight loss 14 · nasal strips 11 · pillows 11 …).

## Past victories + failures
**Where she has WON (what worked, even briefly):**
- A mouthguard that fit: "I have a mouth guard and it’s been transformative. What a difference." [S15 · VERBATIM] (full stories: §10B "boil-and-bite mouthguard" likes)
- Losing weight: "I started exercising regularly and lost some weight. My snoring is back to normal." [S78 · VERBATIM]
- One pillow, better neck: "Snore less now as only use one pillow that helps align my neck." [S79 · VERBATIM]
- CPAP, when it was apnoea: "I now wear a CPAP and it's a lifesaver." [S80 · VERBATIM]
- A partner's view of a jaw device: "Basically it forces the lower jaw forward a bit. While it was kind of uncomfortable for her the first week or so, the results were instantaneous." [S81 · VERBATIM]
→ She already believes **jaw-forward works** and **weight matters** — use both as proof, not as blame.

**Where she has FAILED (not a product):**
- **Diet:** "I know shifting some more weight will help, but I still snore when thinner, just not as much." [S15 · VERBATIM]
- **Doctor visit:** "Would love any input. My Dr says menopause has not shown to create more snoring, but it seems like anecdotally it does." [S75 · VERBATIM]
- **Sleep studies that "found nothing":** "(I’ve had two sleep studies both indicating I DO NOT have sleep apnea; though I suspect I could have UARS which no one seems to ever mention is a thing)" [S82 · VERBATIM]
- **Habit change (alcohol, smoking):** "Drinking exacerbates my snoring … I’ve already given up smoking and losing weight is a constant battle. I’m not convinced dieting will solve the problem anyway." [S10 · VERBATIM]
- Product failures (mouthguards, strips, tape, sprays, CPAP, apps, pillows, surgery) → see §10B by name.

## Goals — near + far
- **Near (this week / this month):** get through tonight without being woken; survive the trip that's already booked; a fix that works from night one (need "works first night" 13 · trigger "girls' trip coming up" 9). "so I am looking for short term solutions for when I sleep over" [S83 · VERBATIM]
- **Far (the dream):** back in the same bed for good, never "the snorer" again, no CPAP (desires: same bed 20 · not the snorer 3 · avoid CPAP 15). "As a woman I was so tired of feeling embarrassed and avoiding falling asleep at friends houses because I knew no one would be able to sleep near me." [S84 · 5★ · VERBATIM]
→ The near win (tonight, the trip) earns the click; the far dream (same bed, not "the snorer") sells the identity.

## The 4 forces (she switches only when Push + Pull beat Anxiety + Habit)
- **Push (pain now):** embarrassment 54 · relationship strain 42 · menopause-worse 42 · dread sharing a room 38 · apnoea fear 35. "It seems to be getting worse as I get older and I’m panicking." [S40 · VERBATIM]
- **Pull (the dream):** stop snoring 43 · wake rested 25 · let him sleep 23 · same bed 20. "Just as I was about to give up and move to the sofa permanently, I’ve been thrown a lifeline." [S10 · VERBATIM]
- **Anxiety (fear of the NEW thing):** uncomfortable 46 · too big 38 · scam/waste 36 · jaw pain 21 · price 18 · won't stay in 11 · teeth move 6 · looks bad 6. "I was a bit skeptical has I had tried a competitors which didn’t work for me." [S85 · 5★ · VERBATIM]
- **Habit (stuck with the old way):** resignation 37 · separate bedrooms "it's fine" 23 · paying for her own room · "maybe it's just the age". "We sleep in separate rooms because of my snoring. It's not ideal but it's better than him being awake all night because of me." [S19 · VERBATIM] · "Apparently, I snore sometimes too and I`m thin. Maybe its just the age." [S15 · VERBATIM]
→ Anxiety + Habit are why she doesn't buy — §11 answers each one.

**So What → do this:** lead with the spare-room/embarrassment push and the same-bed pull; kill the three big anxieties up front (fit for a small mouth, comfort/jaw, "is this another waste of money") — they outrank price.

---

# §10A · Desire Ladder (surface → core)

Every one of the 11 surface desires from §10, laddered. Each rung = a §2C quote/count or INFERENCE. "co-tag" = how many of that desire's snippets also carry the tag (python).

## (1) The full map
1. **Stop snoring (43)** → why? so he can sleep — co-tag "let him sleep" 10 of 43: "My husband was so excited to finally get a full nights sleep instead of listening to me cutting logs all night!!!" [S86 · 5★ · VERBATIM] → why? so the marriage holds — co-tag relationship strain 5: "My husband told me first the first time in 5 years last night waste first night i didn't snore thank you Honex for saving my marriage." [S87 · 5★ · VERBATIM] → why? to be loved as she is — INFERENCE, echoed in the §14 swipe line "My husband still loves me!" → **LOVE / CONNECTION** (+ IDENTITY: "not the snorer")
2. **Wake rested (25)** → why? co-tag tired in the day 7 of 25: "I feel so much better in the morning. My brain fog is gone." [S32 · 5★ · VERBATIM] → why? to get her days back: "means I’m exhausted every day. By the end of the week I’m really irritable. A good night’s sleep fixes everything" [S19 · VERBATIM] → why? INFERENCE: to feel like herself again in midlife → **VITALITY / TIME**
3. **Let him sleep (23)** → why? guilt — co-tag guilt 6 of 23: "I try not to disturb my husband, but I can’t help it." [S19 · VERBATIM] → why? she hates being the burden: "Not a sexy look or feeling but your partner does get some sleep" [S44 · VERBATIM] → why? to be a good wife, not the problem → **SELF-WORTH** (+ LOVE)
4. **Same bed again (20)** → why? co-tag relationship strain 10, separate bedrooms 9 of 20: (partner) "felt like we were drifting apart. So that’s not an option." [S88 · VERBATIM] → why? the closeness (see §10 "same bed" quote: legs and arms entwined) → **LOVE / CONNECTION**
5. **Share a room without shame (16)** → why? co-tag dread sharing a room 14 of 16: "I avoid situations such as weekends away where I may have to share a room with others" [S16 · VERBATIM] → why? so she isn't left out: "If there wasn't a room for me by myself, I'm afraid I would agree with PPs who say 'don't go'." [S66 · VERBATIM] → why? to keep her friends (see §10 "social isolation") → **BELONGING** (+ FREEDOM to travel · SELF-WORTH: "not fair on them")
6. **Avoid CPAP or surgery (15)** → why? co-tag fear of apnoea 5 of 15: "Of course I will have to try CPAP first and the idea is not attractive" [S4 · VERBATIM] → why? she's scared for her health but wants a gentler way: "I choose discomfort and a little realignment of teeth over heart attack or stroke." [S89 · 5★ · VERBATIM] → **SECURITY (health)**
7. **A simple fix that works (12)** → why? she's tired of trying: "Is there any hope?!" [S40 · VERBATIM] → why? she wants certainty after let-downs (burned 109 of 479): "This one really works. Easy set up and immediate results" [S33 · 5★ · VERBATIM] → **CONTROL / CERTAINTY**
8. **Not be "the snorer" (3)** → why? co-tag embarrassment 3 of 3 (see §10 quote "not the type you'd expect to snore") → why? snoring is "unladylike" (belief 14): "for a female it makes you feel not feminine." [S90 · VERBATIM] → **IDENTITY / SELF-IMAGE**
9. **Fix it quietly / privately (2)** → why? she doesn't want to ask or explain: "There is no good way to say 'does anyone mind if I snore'?" [S66 · VERBATIM] → why? INFERENCE: handle it herself, on her terms (NHS waits, travelling alone) → **IDENTITY** (+ FREEDOM)
10. **Feel feminine / normal (2)** → why? "decidedly unsexy" (§10) → why? to feel attractive to him: "It is very unattractive!" [S91 · SNIPPET] → **IDENTITY / SELF-IMAGE**
11. **Works the first night (1)** → why? her husband notices by morning (§10 quote) → why? INFERENCE: quick proof after many let-downs → **CONTROL / CERTAINTY** (+ LOVE: he's the judge)

## (2) Ranked core desires
Rolled-up count = unique snippets carrying any feeding desire **or** a rung tag for that core (python over databank.csv; rung tags listed). Highest first.
1. **LOVE / CONNECTION — 124 of 479** · 4 surface desires (stop snoring · let him sleep · same bed · works first night; 73 snippets) + rung tags relationship strain, he moves out, separate bedrooms, partner wakes her.
2. **IDENTITY / SELF-IMAGE — 103** · 4 desires (not the snorer · feel feminine · fix it privately · stop snoring; 50) + embarrassment, feels unfeminine, low confidence, "unladylike".
3. **VITALITY / TIME — 59** · 1 desire (wake rested; 25) + tired in the day, wakes herself up.
3. **SELF-WORTH (not a burden) — 59** · 2 desires (let him sleep · share a room; 38) + guilt.
5. **SECURITY (health) — 48** · 1 desire (avoid CPAP/surgery; 15) + apnoea fear, "I must have apnoea", "needs a doctor".
6. **BELONGING — 44** · 1 desire (share a room; 16) + dread sharing a room, girls' trip fear, social isolation, hospital.
7. **CONTROL / CERTAINTY — 27** · 2 desires (simple fix · works first night; 13) + "cheap devices don't work", "nothing works", "nothing can be done".
8. **FREEDOM — 22** · 2 desires (share a room · fix it privately; 18) + camping, solo flight, work-trip triggers.

## Wire it in
- **Hook / ad** = the surface desire she says (stop snoring, sleep through, same bed, share the room).
- **§4B identity, §9 One Belief, §13B story** = the top cores. **Repoint the §9 One Belief at #1 LOVE / CONNECTION** (our line: *you can be back in the same bed*), with #2 IDENTITY (our line: *you're not "the snorer" — it's the change, not you*) as the second note.

**So What → do this:** sell the closeness, not the silence — every ad's payoff is *back in your own bed / he stays*, and every proof shot shows the couple, not the device.

---

# §10B · Existing Solutions Teardown

Ranked by §2C failed-solution count [S1]. Every alternative: what she likes (keep it), dislikes (our edge), a horror story, and whether she believes it works. Product items are referred to from §10 by name.

### 1 · Boil-and-bite / OTC mouthguard — 95 (68 of them are 1–2★ reviews · 16 are 4–5★ · burned 81)
- **Likes (keep):** partner-confirmed quiet, cheaper than the dentist, a smaller size. "My hubby said my snoring went from a 10 down to a 3." [S32 · 5★ · VERBATIM] · "I was so happy to see a smaller size for women! … we are back in the same room" [S92 · 5★ · VERBATIM]
- **Dislikes (our edge):** built for a man's mouth; too big, jaw pain, falls out, can't close lips (§10 objections: too big 38 · jaw pain 21 · won't stay in 11 · drooling 1). "I am a female, 5'4” and this felt like it was designed for a large man, not for a woman." [S32 · 1★ · VERBATIM]
- **Horror:** "I ordered the Sleepzee to help me stop snoring while on a European vacation with me sister. … I would find the mouthpiece in the bed or on the floor the next morning. … I am a woman so maybe the mouthpiece is for a man's mouth?" [S93 · 1★ · VERBATIM]
- **Do they believe it works?** Split. Happy women say it's the only thing that worked; unhappy women blame the **fit**, not the jaw-forward idea → the belief gap is "will it fit ME", not "does it work". Amazon UK "Customers say" (DATA, all reviewers): SnoreLessNow Somnofit-S fit 5+/7−; TOMED SomnoGuard 3 fit 2+/12−, comfort 2+/10− [S135].

### 2 · Apps / snore trackers — 16
- **Likes:** a private way to check, and a score to prove progress. "I have an Apple Watch which will tell me anything strange about my breathing. So far so good." [S94 · VERBATIM]
- **Dislikes:** it measures, it doesn't fix. "I’m also tracking my snoring with an iPhone app called SnoreLab, although knowing I snore 60 per cent of the night and my snoring is “epic”, hasn’t improved the situation." [S10 · VERBATIM]
- **Horror:** "I downloaded an App to hear it and it’s really bad. I cry every time I hear myself. It’s the most humiliating thing you could hear from yourself and has battered my confidence. I’m devastated." [S40 · VERBATIM]
- **Believe it works?** As a fix, NO — as proof, YES (use the before/after score as our demo).

### 3 · Weight loss — 14 (non-product; also §10 failures)
- **Likes:** it does help some. "I put on over 20 pounds when peri first started and my snoring was really bad. It's improved once I lost the weight again." [S95 · SNIPPET]
- **Dislikes:** slow, hard in menopause, and thin women snore too (belief "it's my weight" 27). "Although I snored when thin too, it's worse now." [S16 · SNIPPET]
- **Horror:** "I was told that if I lost some weight, the sleep apnea would subside. Months passed, and of course, I did not lose the weight." [S96 · 5★ · VERBATIM]
- **Believe it works?** Half — she believes it, but can't do it fast enough for the trip or tonight.

### 4 · Nasal strips — 11 (burned 10 of 11)
- **Likes:** "Nose strips work for me and hubby, even helped stop his sleep apnea." [S97 · VERBATIM]
- **Dislikes:** "Great in theory, but it made little difference." [S18 · VERBATIM] · Amazon UK Breathe Right "Customers say": snoring reduction 43+/45− (DATA).
- **Horror:** no stand-out horror in the bank — the worst is quiet defeat: "I have tried nasal strips but didn't work." [S71 · SNIPPET]
- **Believe it works?** NO for her kind of snore (throat/mouth, not nose). → our line (mechanism to confirm in §13): *Strips fix noses. Yours is your jaw.*

### 5 · Pillows / positional — 11
- **Likes:** "I started sleeping in a wedge pillow." [S98 · VERBATIM]
- **Dislikes / horror:** "I tried raising my pillows so I'm sleeping at an angle, again as recommended by experts. … it had little effect on me." [S18 · VERBATIM]
- **Believe it works?** A little, sometimes. Not enough.

### 6 · CPAP — 9 (+ avoid CPAP desire 15)
- **Likes:** when it's apnoea, it can change her life. "Using a CPAP mask has ABSOLUTELY changed my life." [S5 · VERBATIM]
- **Dislikes:** "I tried a CPAP machine but it was incredibly annoying and the medical supply company was horrid." [S99 · VERBATIM]
- **Horror:** "I was going on a girl's weekend trip and I just wouldn't feel comfortable wearing a face mask and being hooked up to my machine for my friends to see." [S100 · 5★ · VERBATIM] · "even with a CPAP I wake constantly throughout the night." [S101 · VERBATIM]
- **Believe it works?** Yes for apnoea — but she'll do almost anything to avoid it. Our line: snoring only; apnoea → GP (never claim to replace CPAP).

### 7 · Mouth tape — 8
- **Likes:** cheap, simple, some say it helps. "Don’t tape your whole mouth. I leave the sides of my mouth open so I can still breathe out my mouth if needed." [S102 · VERBATIM]
- **Dislikes:** Amazon UK Longevity Sleep Tape "Customers say": stickiness 146+/178−, skin irritation 53+/75− (DATA).
- **Horror:** "I tried mouth taping but it gave me anxiety." [S103 · VERBATIM]
- **Believe it works?** Many do (tape is the high-awareness fix; misconception "tape fixes all snoring" 2). When it fails she blames herself → our line (mechanism to confirm in §13): *Tape didn't work? It was never your mouth — it's your jaw.*

### 8 · Side-sleeping / tennis ball — 7
- **Likes:** "I slept on my side last night and no snoring apparently. Gonna look into body pillows today." [S104 · VERBATIM]
- **Dislikes:** "I would snore no matter what I tried to do (sleep on my stomach, right side, back, upright, ...)." [S69 · VERBATIM]
- **Horror:** "I’ve tried sewing a tennis ball into the back of my pyjamas to change my sleeping position (it fell out). … Nothing has worked." [S10 · VERBATIM]
- **Believe it works?** No — she's tried it.

### 9 · Nasal spray — 6
- **Likes:** none in the bank (0 positive spray rows).
- **Dislikes:** "She’s had me try multiple allergy nasal sprays but don’t feel they been helping" [S22 · VERBATIM]
- **Horror:** "Female, 50 years old, overweight. Tried but did not help: - Spray for the vessels. - Things that are put inside the nose and mouth (separate)." [S105 · VERBATIM]
- **Believe it works?** No.

### 10 · Doctor visit dismissed it — 5 (non-product; also §10 failures)
- **Likes:** ruling out apnoea gives relief.
- **Dislikes / horror:** "Apnoea was ruled out but there has been no let-up in my snoring, which has since defied such over-the-counter remedies as nasal breathing strips." [S18 · VERBATIM] · (partner) "She went to the sleep doc and they said everything’s fine." [S88 · VERBATIM]
- **Believe it works?** She trusts the GP for apnoea, not for snoring help.

### 11 · Throat spray / lozenges — 5
- **Likes:** "does seem to reduce my snoring by a few decibels" [S10 · VERBATIM]
- **Dislikes / horror:** "I tried some anti-snoring sprays, but they didn’t help." [S19 · VERBATIM] · (lozenges: see §10 "price" quote)
- **Believe it works?** No.

### 12 · Surgery (adenoids, tonsils, nose) — 5
- **Likes:** "I used to snore horribly until I got my tonsils and adnoids taken out, now I snore a little" [S106 · SNIPPET]
- **Dislikes:** "(surgery didn't help)" [S16 · VERBATIM]
- **Horror:** "I had many operations on my ears when I was young and had adenoids removed etc. but I just seem to be incapable of sleeping with my mouth shut." [S40 · VERBATIM]
- **Believe it works?** Mostly no; and it's a big step she wants to avoid (desire 15).

### 13 · Custom dentist device — 5 (4 of 5 rows are 4–5★)
- **Likes:** it works and fits. "I ordered a custom device from this company a number of years ago which was really effective and stopped me snoring." [S107 · 5★ · VERBATIM]
- **Dislikes:** price. "Before spending $1000 on something custom-made by a dentist, I decided to try this just to see if I could even tolerate it in my mouth." [S32 · 4★ · VERBATIM]
- **Horror:** "I have had appliances from Dentist's, they did not hold up at all and did not recommend any cleaners." [S108 · 5★ · VERBATIM]
- **Believe it works?** YES — the dentist device is her "gold standard". Our job (our line): *the same jaw-forward idea, sized for you, without the £1,000 bill* (claims per regulatory).

*(Items #14–#18 rewritten in the §20 gap-fill — full like / dislike / horror / believe-it-works for each; the earlier #14 'likes' quote came from a 38-year-old outside the ICP and was replaced.)*


**Tools used:** python over data/databank.csv (479 rows; failed_solution tag + quote text search), with a substring check against docs/doc1–4_body.md so no quote repeats one already in the docs. Pulled by product-pulse / Firecrawl collectors V1–V3 (see §2C).
Counts are "n of 479 tagged" plus "+m untagged text mentions". Source numbers are existing Doc 2 S-numbers where the URL already exists.

**Correction to report:** the current #14 "Likes" quote [S109] ("…plus intake nose strips now to stop snoring 😅") is from a **38-year-old** in r/perimenopause_under45 (bank row v1-007, age_signal "38"). She's outside the 40–60 ICP, and the quote is a current-use mention, not a like. Replace it as below.

### 14 · Nasal dilator: 4 tagged (+1 untagged mention); burned 3 of 4
- **Likes:** works only as a helper next to a mouthguard. "A mouth guard plus nasal dilators that fit inside the nose worked for me." Mumsnet Chat, GB, *I fixed snoring* (NEW SOURCE: https://www.mumsnet.com/talk/_chat/5238569-i-fixed-snoring?page=2 · date not shown · SNIPPET)
- **Dislikes:** goes on the list of things tried and dropped. "I have tried nasal sprays, sleeping sitting up, nasal strips, nose appliances, mouthpieces that were either too big for my mouth and left me in pain all day, or were completely ineffective." [S92 · Trustpilot vitalsleep.com · 5★ · 2020-01-24 · VERBATIM]
- **Horror:** "I was at the end of my rope, ready to consider paying out of pocket for surgery that has no guarantee of success. My husband and I were sleeping in separate rooms." [S92 · 5★ · 2020-01-24 · VERBATIM] (written after nose appliances failed)
- **Believe it works?** **No, not on its own.** 0 of 4 tagged rows say a dilator alone worked; 3 of 4 list it among failures. The only positive is a dilator **plus** a mouthguard. In bank-label terms she thinks of it as "its_my_nose" (12). INFERENCE: it fails because it never touches the jaw/throat.

### 15 · Cutting alcohol: 4 tagged (+7 untagged mentions = 11 of 479 mention drink/alcohol); non-product
- **Likes:** none found. 0 of 11 rows say stopping drinking stopped the snoring. The closest is the belief behind it: "Drinking exacerbates my snoring and, like many people, I'm having an extra glass or two during lockdown." [S10 · Telegraph · GB · midlife · 2020-04-16 · VERBATIM]
- **Dislikes:** she already doesn't drink, and still snores. "Me and DH have separate rooms 🫣 I'm not over weight and I haven't smoked for 10+yrs, don't drink." [S16 · Mumsnet · GB · 2024-09-22 · VERBATIM]
- **Horror:** "It is so bad I don't stay overnight with relatives any more because of the snoring." (from a woman who opens with "I don't drink") (NEW SOURCE: https://www.mumsnet.com/talk/am_i_being_unreasonable/2269234-To-be-embarrassed-by-my-snoring · date not shown · SNIPPET) · "I also avoid situations where I may need to sleep near other people. It's very frustrating 😑" [S16 · 2024-09-22 · VERBATIM]
- **Believe it works?** **Split, and mostly no.** 3 rows believe alcohol makes it worse (v1-038 "100x worse" [S103]; Telegraph [S10]; Daily Mail "Steven winces" [S18]). 5 rows say they **don't drink and still snore** (v1-080, v1-089, v1-126, v1-176, v2-125). Counter-proof that a jaw device beats the wine: "I've just had a remark from my husband that my snoring was remarkably better ( even after a few glasses of wine)." (NEW SOURCE: https://uk.trustpilot.com/reviews/662e0507403890ea182f039e · Trustpilot (Snoreeze mouthguard) · 5★ · GB · 2024-04-28 · VERBATIM)
- **So What:** never tell her to give up her glass of wine. Use "Still snore when you haven't had a drop?" (INFERENCE; hook built on 5 "don't drink" rows).

### 16 · Supplements / oils / vapours / lozenges: 3 tagged
- **Likes:** one believer. "When my snoring starts, I take 5000 ui of Vitamin D every day for a month." [S111 · r/Menopause · 2022-11-03 · VERBATIM] (her result line is already quoted in §10B). Compliance: anecdote only; never echo it as a claim.
- **Dislikes:** they taste odd and do nothing. "I've also tried nasal strips, lubricating lozenges and strange-tasting throat sprays." [S10 · Telegraph · GB · 2020-04-16 · VERBATIM] (lozenge price complaint: see §10 "price" [S34 · already used])
- **Horror:** after "pillows, vapours, different positions, nose strips, mouth guards": "It seems all the muscles in my throat go to jelly once I'm asleep and I'm just honking the night away and annoying the hell out of anyone in earshot." [S40 · Mumsnet AIBU · GB · 'as I get older' · 2022-09-22 · VERBATIM]
- **Believe it works?** **1 of 3 yes** (vitamin D), **2 of 3 no** (vapours, lozenges "complete waste of money"). Low belief, low spend.

### 17 · Chin strap: 1 tagged (+1 untagged mention by a third party)
- **Likes:** none. **Only 1 row of her own, and no like or horror quote that is specifically about the chin strap.** Say so, don't pad.
- **Dislikes:** bought alongside everything else, and none of it worked. "I've ordered mouldable mouth guards, chin straps and curved anti-snore pillows to change the position of my head and mouth during the night." [S10 · Telegraph · GB · midlife · 2020-04-16 · VERBATIM] (her next line, "Nothing has worked.", is already in §10B #8)
- **How others see it:** it's a list item people suggest to the husband. "If she doesn't have OSA, nasal strips, mouth tape, a chin strap.... sleeping in separate rooms, weight loss...." (r/GenX reply about a "post menopausal woman who now snores", 2024-02-06 · VERBATIM · comment URL https://www.reddit.com/r/GenX/comments/1ak3e65/wife_snores_need_suggestions/kp6ge3h/ = [S143] thread)
- **Believe it works?** **No** (1 of 1 tried → failed). Competitor HiZuu already uses it as a failed alternative in AU ads: "Why people try it after pillows, sprays and chin straps" (Meta 4147770232190757, 2026-11-23, VERBATIM).

### 18 · Anti-snore ring: 1 tagged
- **Why she had one:** her partner bought it, and it's a great self-deprecating line. "So far the only ring he's given me is the Good Night Anti-Snoring Ring, (£29.99) which stimulates acupressure points on your finger to keep your airways open." [S10 · Telegraph · GB · 2020-04-16 · VERBATIM]
- **Likes:** none (0 of 1).
- **Dislikes / horror:** already quoted ("mine keeps falling off and the roars continue" [S10]).
- **Believe it works?** **No** (1 of 1). Paid £29.99, the same as the GB DTC mouthpiece going rate.

### Doing nothing / work-arounds: add the missing "Believe it works?" line
- **Believe it works?** **As a truce, yes; as a fix, no.** Separate rooms are the most common work-around (separate bedrooms 23 · he wears earplugs 7 · she books her own room 7 · she sleeps on the sofa 7 [S1]). The likes in §10B (#S15) come from couples who've made peace with it. The dislikes and horror (#S16, #S10) show she still feels it's unfair on others and dreads trips (INFERENCE from the counts above; no new quote needed).

**So What → do this:** #14–#18 together are 13 tagged rows (2.7% of the bank). These are minor detours, not the main enemy. Use only two of them in copy: "don't drink and still snore" (#15) and the ring line as humour (#18). Keep the fight on boil-and-bite fit (95) and tape/strip let-downs.

---


### Doing nothing / work-arounds (not a failed-solution tag — counted from pain tags + quote search)
- **What:** separate bedrooms (23) · he wears earplugs (7 quotes) · she books her own room (7) · she sleeps on the sofa (7) [S1].
- **Likes:** "We now have separate bedrooms. Sex is better than before - we both sleep well to our own timetable and our own (age related) snoring patterns" [S15 · VERBATIM]
- **Dislikes:** "I don’t actually mind the idea of sharing a room with a friend or sister but it’s not really fair on them" [S16 · VERBATIM]
- **Horror:** "It sounds harsh, but after four years of broken sleep, my partner Russell is at his wits’ end – and so am I. I often wake up on the sofa and it’s a nightly routine we’re both desperate to change." [S10 · VERBATIM]

**So What → do this:** don't fight the mouthguard idea — she already half-believes it. Fight the **fit** (built for him) and the tape/strips let-down, and answer refund distrust inside the offer (a policy-true guarantee — never the ad's selling line); position as the step up from tape and the step down from a £1,000 dentist device.

---

# §14 · Voice

Reading level for all copy: 5th–8th grade.

## Emotional journey (where traffic enters)
1. **Awareness** — *apparently I snore*. Shock 6 · unaware 10 · trigger: told by partner 49, heard a recording 21.
2. **Frustration** — frustration 111 · embarrassment 52 · anger 32 · guilt 28 · shame 27.
3. **Desperation / seeking a fix** — anxiety 32 · fear 26 · resignation 37 · grief 33 · hope 20; awareness: problem-aware **220 of 479 (46%)** · solution-aware 66.
4. **Relief / commitment** — relief 90 · pride 4; product-aware 107 · most-aware 76 (mostly reviewers) [S1].
→ **Meta cold traffic enters at stage 2→3** (problem-aware, frustrated, not yet sure a mouthpiece is for her). INFERENCE from the awareness split.

## Swipe — her phrases (★ = the key words appear in 3+ snippets; count in brackets, python regex over the bank)
- "Suddenly I snore…" (thread title) [S136] ★ (6)
- "Peri has turned me into a snorey monster practically overnight" (thread title) [S11] (2)
- "I now snore 1000% worse" [S112] (1)
- "I have become one of them" [S113 · SNIPPET] (1)
- "Add that to my list of symptoms" [S71 · SNIPPET] (2)
- "I now am my Mother. Noooo!!!" [S114] (1)
- "a crazy wrinkly throat on the inside to match the outside" [S74] (1)
- "a “throat snorer” rather than a “nose snorer”" [S14] ★ (3)
- "I snore like a beast now" [S99] ★ (7)
- "I apparently snore like a freight train" [S30] ★ (7)
- "I snore like a foghorn" [S115 · SNIPPET] ★ (7)
- "mouth open, snoring like a pig" [S18] ★ (7)
- "like a tractor in the bedroom" [S116] ★ (3)
- "I snore like a tractor lol, if a tractor does lol" [S115 · SNIPPET] ★ (3)
- "start a chainsaw with her face" [S117] (2)
- "it sounds like a revving motorbike" [S5] ★ (7)
- "I sounded like a cartoon character" [S19] ★ (7)
- "I sound like a walrus in distress" [S10] ★ (7)
- "a small truffle pig is sharing my bed. Mortifying." [S24] ★ (5)
- "It didn’t even sound human!" [S19] (1)
- "cutting logs all night" [S86] (1)
- "I’m just honking the night away" [S40] (1)
- "then the room is shaking" [S40] (1)
- "my nasal nocturnal orchestra" [S23] (1)
- "they could hear me through the bedroom walls" [S19] ★ (6)
- "he can hear me downstairs and throughout the house" [S118 · SNIPPET] ★ (6)
- "Not a cute little dainty snore either" [S119 · SNIPPET] ★ (5)
- "IT IS NOT CUTE SNORING" [S83] ★ (5)
- "Clearly I don’t, it’s purring" [S67] (1)
- "Just been told I SNORE horrifically. Want to cry." [S120 · SNIPPET] ★ (5)
- "I cry every time I hear myself" [S40] ★ (5)
- "unladylike, monstrous, embarrassed and unattractive" [S40] ★ (3)
- "I feel really unattractive" [S15] ★ (3)
- "decidedly unsexy" [S18] ★ (3)
- "it makes you feel not feminine" [S90] ★ (3)
- "I look like a complete prat" [S24] (1)
- "DH is threatening he will disappear in the spare room" [S14] ★ (13)
- "DH is already in the spare room with no sign of coming back" [S40] ★ (13)
- "I hate waking up to find DH not there" [S121 · SNIPPET] (2)
- "dumped in the middle of the night, every night" [S10] (1)
- "Stop snoring or move out." [S10] (1)
- "my husband shoved my arm" [S21] ★ (11)
- "partner woke me by kicking me repeatedly" [S20] ★ (11)
- "move to the sofa permanently" [S10] ★ (7)
- "our days of sharing a bed are over" [S15] ★ (16)
- "Hate sharing a hotel room." [S16] ★ (16)
- "I always opt to pay for an extra room" [S16] ★ (7)
- "I actually declined a girls trip" [S122] ★ (4)
- "saved my girl's weekend (and my friendships.)" [S100] ★ (4)
- "I would make their break a nightmare" [S23] (2)
- "Hen party anxiety!" (thread title) [S66] ★ (3)
- "stressed to death about sleeping" [S5] (2)
- "everyone has just been too polite to mention it" [S24] (1)
- "There is no good way to say 'does anyone mind if I snore'?" [S66] (1)
- "I feel sometimes like people think I can control it?" [S5] (1)
- "I dread having to go into hospital" [S16] ★ (4)
- "the shame and guilt of disturbing everyone" [S40] ★ (3)
- "not loud enough to initiate divorce proceedings" [S16] ★ (8)
- "thank you Honex for saving my marriage" [S87] ★ (8)
- "he might not marry me in 8 weeks time" [S123] (2)
- "afraid my snoring might be a deal breaker" [S63] (1)
- "trying to avoid the darth vader machine" [S103] (1)
- "Too bloody big for my mouth" [S46] ★ (14)
- "maybe the mouthpiece is for a man's mouth?" [S93] ★ (3)
- "You literally cannot shut your mouth" [S39] ★ (5)
- "like someone had punched me in the front teeth" [S124] ★ (5)
- "a useless non fitting piece of plastic" [S125] (2)
- "Small price to pay for a quiet night." [S32] (1)
- "My husband still loves me!" [S53] (1)
- "not the type you’d expect to snore" [S62] (1)
- "Can’t anything just keep working??" [S51] (1)
- "My brain fog is gone." [S32] ★ (3)
- "the only thing that has ever worked" [S126] ★ (3)
- "it’s been transformative. What a difference." [S15] (1)

## Quote buckets (sorted from the bank; none of these appear in §10)
- **Pain / frustration:** "He deals with it by shaking me until I get up and move into the spare room. … he’ll just shake / nudge me then will complain the next day about how tired he is because it’s so hard to sleep next to me." [S15 · VERBATIM] · "I'm so annoyed I'm up at this hour, facing a full day and he's having a day to himself on a full night's rest." [S2 · VERBATIM] · "I snore like a tractor lol, if a tractor does lol. That is why I get to spend nights on my own. I get embarrassed by my snoring." [S115 · SNIPPET]
- **Mindset:** "All the women in my family are snorers. But. Not all snoring is sleep apnoea. There is a difference." [S15 · VERBATIM] · "I used to only snore when I was sick with a cold or flu or something, but now... I don't know what's changed, but I snore now." [S127 · VERBATIM] · "I'm in perimenopause which means I'm in my do not give a fuck era." [S128 · VERBATIM] (not for ads)
- **Deep fears:** "Our marriage isn’t really in the best place at the moment anyway and I’m worried this is going to be the thing that tips us over the edge." [S15 · VERBATIM] · "I doze off, throat closes up, and I wake up in a panic." [S3 · VERBATIM] · "once you know it's an issue, you never really sleep easy again as you're so concerned you're waking them up." [S15 · VERBATIM]
- **Motivation & urgency:** "We’re supposed to be away next weekend but I can’t face the shame and guilt of disturbing everyone. I feel heart broken and stuck." [S40 · VERBATIM] · "It was time for me to find out the cause and how to fix it." [S29 · VERBATIM] · "Thanks for giving me hope… it’s on the way! Can I ask what one you went for?" [S15 · VERBATIM]
- **Emotional response to the struggle:** "Nor has listening to a recording – I sound like a walrus in distress and if I were Russell I’d leave me, too." [S10 · VERBATIM] · "all my stuff is still in ‘his’ room because that’s an emotional hurdle we just can’t get past." [S15 · VERBATIM] · "I was so stubborn, i didn't want to admit it. Stupid, right?" [S129 · VERBATIM]

## Words to USE vs AVOID
**USE (her words — bank counts):** snore / snoring · "my husband says" / DH / hubby (husband·DH·hubby in 79 quotes vs "partner" 18) · mouth guard (25) ≈ mouthpiece (21) · spare room (13) · share a room / bed (16) · too big (14) · small mouth (9) · jaw (27) · embarrassed (19) · mortified (5) · menopause / peri (46) · girls' trip / weekend away · first night (9) · "throat snorer" [S1].

**AVOID in ads, hooks and headlines → the plain swap she'd use:**
- mandibular advancement device / MAD (bank: 1 / 4 — only from dentist-fitted users) → "mouth guard" / "mouthpiece"
- oral appliance / anti-snoring device (bank 1 / 0 · ads 7) → "mouth guard"
- obstructive sleep apnoea / OSA (bank OSA 2) → don't use in ads at all; FAQ/red-flag box only: "if you stop breathing or gasp in your sleep, see your GP"
- upper airway / airway (bank 6 · ads 5) → "throat"
- genioglossus, muscle tone, soft palate (bank 0 / 0 / 2) → "the muscles in your throat relax"
- perimenopausal, hormonal decline (bank "perimenopausal" 0 · "hormon-" 5) → "menopause", "peri", "the change"
- sleep divorce (bank 0) → "separate rooms", "the spare room"
- partner (in UK ads) → "husband" (her default; keep "partner" as a variant)
- **Category hype words she never says** (count in 340 logged competitor ads vs bank): "instantly" (ads 17 · bank 1) → "from the first night" (only if true) · "hack" (ads 11 · bank 0) → "tip" · "#1" (ads 13 · bank 1) → drop it · "stop snoring" as a promise (ads 53) → "quieter nights" / "help reduce snoring" · "cure", "eliminate" (bank 1 / 1) → never (regulatory: "an aid in the reduction of snoring" on the product page only) · "clinically proven" → only with real proof.
- An avoid-word may appear ONLY on the product page or FAQ when needed for accuracy (e.g. "mandibular advancement device (a mouth guard that holds your jaw forward)").

## Thread-title hooks (high-engagement titles, her words — forum tactics)
Ranked by replies/comments within the ICP-own list (VERBATIM titles unless marked SNIPPET):
1. "Dh woke me up to stop me snoring, he's got the whole day to himself" — Mumsnet, 260 replies [S2]
2. "My snoring… spare room forever?" — Mumsnet AIBU, 94 replies + 77 poll votes [S15]
3. "Woken up being kicked repeatedly, partner says I was snoring" — Mumsnet AIBU, 5 pages [S20]
4. "Mortified...what do guys think of a women that snores? 🥲" — r/AskMenAdvice, 66 comments [S90]
5. "My snoring is ruining my marriage!" — Mumsnet, 37 replies [S44]
6. "So embarrassed by my snoring :(" — Mumsnet, 29 replies [S5]
7. "Women who snore (or used to snore) - how do (or did) you deal with it?" — r/AskWomenOver30, 28 comments [S137]
8. "Peri has turned me into a snorey monster practically overnight." — r/Menopause, 26 comments [S11]
9. "Hopeless woman looking for a nose snoring solution ( DO NOT SAY SEPARATE BEDS)" — r/snoring, 21 comments [S83]
10. "Hen party anxiety!" — Mumsnet, ~20 replies [S66]
11. "Dry nose and snoring?? Disrupting my life :(" — r/Menopause, 18 comments [S82]
12. "Suddenly snoring" — r/Perimenopause, 13 comments [S25]
13. "Snoring is now 1000% worse" — r/Menopause, 12 comments [S112]
14. "Ladies, when did you first realize you snore?" — r/snoring, 12 comments [S138]
15. "Oh no. I'm now a snorer." — Mumsnet, 10 replies [S14]
16. "To be devastated at how bad my snoring is!" — Mumsnet AIBU [S40]
17. "Suddenly I snore…" — r/WomenOver40, 5 comments [S136]
18. "Just been told I SNORE horrifically. Want to cry." — Mumsnet [S120]
19. "Ending a relationship because of my snoring" — Mumsnet AIBU [S139]
20. "I'm now sleeping in spare room for my own sanity!!" — Facebook HerSpace group [S118]
21. "How many women now snore!? Is it happening for you? I have become one of them" — Facebook [S113]
22. "Ladies, are we gonna sit here and act like we don't snore lol" — Facebook Dull Women's Club [S140]
- Partner-side titles (him describing HER — big threads): "She snores LOUD!" r/datingoverforty, 136 comments [S141] · "How do you deal with your wife's snoring?" r/AskMen, 135 [S142] · "Wife Snores need suggestions" ("We are both 56") r/GenX, 70 [S143].
- Read: her own-snoring threads are 5–260 replies; threads about HIS snoring run 100–600 — she lives inside menopause and marriage threads, not snoring threads [S144].

**So What → do this:** write hooks in her title-voice ("Suddenly I snore…", "Spare room forever?", "Hen party anxiety!"), lean on the ★ phrases (spare room, snore like a…, sounds like…, can't shut my mouth, too big), and keep every clinical word off the ad.

---

# §18 · Trigger events

Ranked by §2C trigger count [S1]. Each = a concrete moment (what + where + who) + her words.

1. **Partner complaint — 49.** *In bed at night; after nudges and shoves her partner finally snaps.* "This routine will continue with harder and more frantic pushes, until I hear the exasperated cry: “I can’t live like this, I love you but I NEED to sleep. Stop snoring or move out.”" [S10 · VERBATIM]
2. **Menopause onset — 37.** *Peri starts; one night her husband leaves the bed and she realises she is a snorer now.* "On top of the normal fun of meno, I now snore 1000% worse. Drove my husband out last night. :( Anyone else?" [S112 · VERBATIM]
3. **Hearing a recording — 21.** *Her husband records her on his phone and plays it back to her.* "Eventually, he recorded me snoring and played it back to me. I was completely baffled and got help straight away." [S130 · VERBATIM]
4. **Weight gain — 11.** *Peri + a few extra pounds; her fiancé says it's every night now and he's getting headaches.* "I’m currently going through peri menopause and have also gained a bit of extra weight. My fiancé has said my snoring is getting much worse and I’m now snoring every night which means he’s not getting much sleep and he suffers debilitating headaches." [S123 · VERBATIM]
5. **Holiday / shared room — 11.** *A hotel room with her daughter on a mini-break; the daughter tells her (or cries).* "I snore, dd2 told me a few weeks ago when we were in a hotel room together sharing a bed. I fell asleep next to her and she burst out crying as she couldn’t sleep. I asked what was wrong, she told me and swapped with dd1" [S14 · VERBATIM] · "I was devastated to recently learn – via my 17-year-old daughter, with whom I recently went on a mini break – that I have started to snore." [S24 · VERBATIM]
6. **A child's comment — 10.** *Her son, on another floor of the house, tells her husband how loud she is.* "My son commented to my husband how loud I was snoring and was worried about it . I was upstairs and they were on another level." [S131 · VERBATIM]
7. **Girls' trip coming up — 9.** *She sees her friends have booked shared rooms for the trip.* "Yes this is what I've been doing. Happy to pay extra but just seen friends have booked shared rooms .. I didnt realise. I did say I would get own room but they gone ahead and booked shared ones? I feel sometimes like people think I can control it?" [S5 · VERBATIM]
8. **A friend's comment — 9.** *On a girls' trip, her friends tell her next morning they were worried about her breathing.* "I blamed it on menopause until I went on a girls' trip and my friends told me how worried they were about my breathing while I was sleeping." [S59 · VERBATIM]
9. **New relationship — 7.** *First sleepover with a new partner; he flees to the sofa.* "I have a new partner and in our first sleep over, I MADE HIM FLEE THE BEDROOM, this giant man was found asleep on his tiny sofa with legs dangling out" [S83 · VERBATIM]
10. **He moved out of the bed — 6.** *She wakes up and he's in the spare room — and he's not coming back.* "DH is already in the spare room with no sign of coming back. That was bad enough and has taken me months to come to terms with." [S40 · VERBATIM] · "Just woke up to find husband in spare room." [S132 · VERBATIM]
11. **Camping / caravan — 2.** *Friends invite her on a caravan break; she says no.* (quoted in §10 "girls' trip / holiday fear" #1 — she turned down caravanning holidays with friends.)
12. **Work trip, shared hotel room — 2.** "I travel often and sometimes share hotel rooms" [S110 · VERBATIM]
13. **Family visit, shared room — 1.** *Daughter and grandchildren come to stay; nobody wants the room next to hers.* "when my daughter Beth and her daughters, Freya, five, and Evie, four, come to stay, she and Paul argue over the spare room, as neither wants to share a bedroom with me." [S18 · VERBATIM]
14. **Family trip, shared house — 1.** (quoted in §10 "dreads sharing a room" #1: heard through the bedroom walls.)
15. **Turned 50 — 1.** "Any tips for a snoring female? I've just started and turned 50 recently." [S133 · SNIPPET]
16. **Retreat, shared room — 1.** "Retreat Sleep Question: Snoring 💤 😥 I snore and am worried I might disturb the person I’m sharing a room with… any tips, tricks or products" [S134 · SNIPPET]
17. **Flying alone — 1.** (quoted in §10 "fear of snoring in public".)
18. **Hospital stay — 1.** "I had a hysterectomy in 2018 and the anaesthetist came to see me because of the SA being in my notes." [S5 · VERBATIM]

**So What → do this:** build the first hooks on moments 1–3 and 5–8: the shout in the night, peri made me a snorer, the phone recording, the daughter in the hotel room, the friends' shared-room booking. Each is a 3-second scene she has lived.

---

# Sources (Doc 2)
- S1 — §2C data bank — databank.csv, 479 rows (merged V1+V2+V3; 19 out-of-ICP rows and 7 duplicates removed) · local CSV → uploaded as the §2C Sheet at delivery · 2026-11-23
- S2 — https://www.mumsnet.com/talk/_chat/5517154-dh-woke-me-up-to-stop-me-snoring-hes-got-the-whole-day-to-himself · mumsnet · 2026-04-15
- S3 — https://www.reddit.com/r/Menopause/comments/1r9own5/apnea_caused_by_peri/ · reddit · 2026-02-20
- S4 — https://www.reddit.com/r/Fibromyalgia/comments/1ve63rs/has_anyone_ran_out_of_treatment_options/p1gtr4n/ · reddit · 2026-08-03
- S5 — https://www.mumsnet.com/talk/_chat/4611921-so-embarrassed-by-my-snoring · mumsnet · 2022-08-15
- S6 — https://x.com/i/status/1453572883205218306 · x.com · 2021-10-28
- S7 — https://www.walmart.com/reviews/product/807239446 · walmart.com (Intelliguard Pro) · 9/26/2021
- S8 — https://www.mumsnet.com/talk/_chat/5517154-dh-woke-me-up-to-stop-me-snoring-hes-got-the-whole-day-to-himself?page=10 · mumsnet
- S9 — https://www.reddit.com/r/AmIOverreacting/comments/1w14911/aio_for_seriously_reconsidering_a_2month/p6j2gi6/ · reddit · 2026-08-29
- S10 — https://www.telegraph.co.uk/family/relationships/help-female-foghorn-snoring-ruining-relationship/ · telegraph.co.uk · 2020-04-16
- S11 — https://www.reddit.com/r/Menopause/comments/yjyvxi/peri_has_turned_me_into_a_snorey_monster/ · reddit · 2022-11-02
- S12 — https://www.reddit.com/r/Menopause/comments/1p8fom7/comment/nr7n2zd/ · reddit · 2025-11-28
- S13 — https://uk.trustpilot.com/reviews/66a6c2c698a0fa980fa2985d · trustpilot (sleepmd.net) · 2024-07-29
- S14 — https://www.mumsnet.com/talk/_chat/4321687-oh-no-i-m-now-a-snorer · mumsnet · 2021-08-13
- S15 — https://www.mumsnet.com/talk/am_i_being_unreasonable/5017646-my-snoring-spare-room-forever · mumsnet · 2024-02-28
- S16 — https://www.mumsnet.com/talk/_chat/5171411-do-you-snore · mumsnet · 2024-09-22
- S17 — https://www.mumsnet.com/talk/_chat/5216395-snoring-me · mumsnet · 2024-11-23
- S18 — https://www.dailymail.co.uk/femail/article-3283637/When-s-WOMEN-snoring-sparks-war-bedroom-Sleeping-wife-snores-no-laughing-matter.html · dailymail.co.uk · 2015-10-22
- S19 — https://www.dailymail.co.uk/femail/article-6655155/Female-foghorns-wives-snoring-nightmare-study-shows-women-worse-men.html · dailymail.co.uk · 2019-01-31
- S20 — https://www.mumsnet.com/talk/am_i_being_unreasonable/4834123-woken-up-being-kicked-repeatedly-partner-says-i-was-snoring · mumsnet · 2023-06-23
- S21 — https://www.reddit.com/r/Menopause/comments/105m3qf/so_angry_this_is_my_sleep_for_the_week_today_is/ · reddit · 2023-01-07
- S22 — https://www.reddit.com/r/Perimenopause/comments/1xpe3d5/dry_nose_and_snoring_highly_disruptive/ · reddit · 2026-11-06
- S23 — https://www.walesonline.co.uk/news/health/mum-says-loud-snoring-played-13264082 · walesonline.co.uk · 2017-07-04
- S24 — https://www.dailymail.co.uk/lifestyle/fitness-wellbeing/article-15250645/ALICE-SMELLIE-mortified-snoring-miracle-cure-stopped-night.html · dailymail.co.uk · 2025-11-02
- S25 — https://www.reddit.com/r/Perimenopause/comments/1j0zwwt/suddenly_snoring/ · reddit · 2025-03-01
- S26 — https://www.reddit.com/r/Zepbound/comments/1uzyw1t/fatty_liver_and_sleep_apnea/oyb3eyq/ · reddit · 2026-07-18
- S27 — https://www.theguardian.com/lifeandstyle/2026/feb/07/deafening-draining-and-potentially-deadly-are-we-facing-a-snoring-epidemic · theguardian.com · 2026-02-07
- S28 — https://www.reddit.com/r/Menopause/comments/1k243nx/comment/mnsz8md/ · reddit · 2025-04-18
- S29 — https://nexttribe.com/magazine/snoring-solutions/ · nexttribe.com · 2023-11-02
- S30 — https://www.reddit.com/r/snoring/comments/1i67byu/snoring_devices/ · reddit · 2025-01-21
- S31 — https://www.facebook.com/groups/789547842998320/posts/1131271292159305/ · facebook
- S32 — https://www.walmart.com/reviews/product/983382357 · walmart.com (SnoreMD) · 2/28/2026
- S33 — https://www.walmart.com/reviews/product/428840037 · walmart.com (SmartGuard) · 9/10/2025
- S34 — https://uk.trustpilot.com/reviews/672a123d70a8af037414cf33 · trustpilot (snoreeze.com) · 2024-11-05
- S35 — https://www.reddit.com/r/Menopause/comments/xxj2nv/if_you_are_having_trouble_sleeping_please/ · reddit · 2022-10-06
- S36 — https://uk.trustpilot.com/reviews/6accfb049919c3fceaa3ed97 · trustpilot (honexcompany.com) · 2026-10-12
- S37 — https://uk.trustpilot.com/reviews/5b83e0318c83fd0bd0047f16 · trustpilot (vitalsleep.com) · 2018-08-27
- S38 — https://uk.trustpilot.com/reviews/6a32996f14c3e614ede4452b · trustpilot (sleepzee.co) · 2026-06-17
- S39 — https://uk.trustpilot.com/reviews/6966b96e7b40195053ddd04a · trustpilot (snorerx.com) · 2026-01-13
- S40 — https://www.mumsnet.com/talk/am_i_being_unreasonable/4639231-to-be-devastated-at-how-bad-my-snoring-is · mumsnet · 2022-09-22
- S41 — https://www.facebook.com/ConvergentDental/videos/wallpaper-peeling-off-type-snoring/416446456801041/ · facebook
- S42 — https://uk.trustpilot.com/reviews/5b84a9948c83fd0bd004c5d8 · trustpilot (vitalsleep.com) · 2018-08-28
- S43 — https://uk.trustpilot.com/reviews/6966757cc72b0ec9a9c15566 · trustpilot (sleepzee.co) · 2026-01-13
- S44 — https://www.mumsnet.com/talk/general_health/5525949-my-snoring-is-ruining-my-marriage · mumsnet · 2026-05-06
- S45 — https://uk.trustpilot.com/reviews/67042971f34c79695fccaf63 · trustpilot (sleeppro.com) · 2024-10-07
- S46 — https://uk.trustpilot.com/reviews/6876a0bb042dc7e49953656b · trustpilot (snoreeze.com) · 2025-07-15
- S47 — https://uk.trustpilot.com/reviews/5ed3a37025e5d209b8f90d4c · trustpilot (snoreeze.com) · 2020-05-31
- S48 — https://www.reddit.com/r/Menopause/comments/1m9aou6/4_specificallyhas_anyone_else_experienced_ear_pain/n5ff2sj/ · reddit · 2025-07-27
- S49 — https://uk.trustpilot.com/reviews/6ab46e443e2fb5f15b033771 · trustpilot (snorerx.com) · 2026-09-24
- S50 — https://www.reddit.com/r/CPAP/comments/1x97ntn/okay_when_do_i_start_to_feel_better_haha/phl9zf5/ · reddit · 2026-10-18
- S51 — https://www.reddit.com/r/snoring/comments/1j5hqyr/comment/mgkn4i8/ · reddit · 2025-03-07
- S52 — https://www.reddit.com/r/Menopause/comments/1g081a8/im_so_tired_of_being_tired_can_menopause_cause/lr9pxtr/ · reddit · 2024-10-10
- S53 — https://uk.trustpilot.com/reviews/675322201c4603850979206a · trustpilot (vitalsleep.com) · 2024-12-06
- S54 — https://www.walmart.com/reviews/product/20161870541 · walmart.com (QuietLab Pro) · 10/23/2026
- S55 — https://www.walmart.com/reviews/product/17852366153 · walmart.com (CorBreev) · 7/2/2026
- S56 — https://www.reddit.com/r/Zepbound/comments/1uqm77n/what_was_your_oh_no_i_need_to_change_i_need/ow9upoh/ · reddit · 2026-07-08
- S57 — https://www.reddit.com/r/Menopause/comments/1k243nx/comment/mnuk3rp/ · reddit · 2025-04-19
- S58 — https://www.reddit.com/r/snoring/comments/1kkepnr/any_other_young_healthy_snorers_out_there/ms89jt6/ · reddit · 2025-05-14
- S59 — https://www.reddit.com/r/fitbit/comments/1wp2j8h/if_your_sleep_looks_like_this_i_have_some_bad/pe7rz80/ · reddit · 2026-10-06
- S60 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iuvapup/ · reddit · 2022-11-03
- S61 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iuvae4k/ · reddit · 2022-11-03
- S62 — https://uk.trustpilot.com/reviews/5e128121c8454508343bcc6f · trustpilot (vitalsleep.com) · 2020-01-06
- S63 — https://uk.trustpilot.com/reviews/5ee8eb8a7dd75307088524fe · trustpilot (vitalsleep.com) · 2020-06-16
- S64 — https://www.reddit.com/r/Perimenopause/comments/1fgz48c/diagnosed_with_sleep_apnea/ · reddit · 2024-09-14
- S65 — https://www.reddit.com/r/AskMenAdvice/comments/1pzby5t/comment/nwp3hfx/ · reddit · 2025-12-30
- S66 — https://www.mumsnet.com/talk/_chat/4552757-hen-party-anxiety · mumsnet · 2022-05-21
- S67 — https://x.com/i/status/1765102353273798939 · x.com · 2024-03-05
- S68 — https://uk.trustpilot.com/reviews/6a04990032d43928e7128d35 · trustpilot (vitalsleep.com) · 2026-05-13
- S69 — https://www.youtube.com/watch?v=g0RehE4T-T8&lc=UgxT-i3AWUJ66bO4XjJ4AaABAg · youtube · 2025 (1 year ago)
- S70 — https://www.facebook.com/groups/herspaceperimenopauseandmenopausesupport/posts/1319778550030695/ · facebook
- S71 — https://www.facebook.com/groups/herspaceperimenopauseandmenopausesupport/posts/1417559726919243/ · facebook
- S72 — https://www.facebook.com/groups/herspaceperimenopauseandmenopausesupport/posts/1176236687718216/ · facebook
- S73 — https://www.facebook.com/groups/1405682240649555/posts/1668234927727617/ · facebook
- S74 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iurano0/ · reddit · 2022-11-02
- S75 — https://www.reddit.com/r/snoring/comments/kd0qbl/estradiol_estrace_and_increased_snoring_rem_and/ · reddit · 2020-12-14
- S76 — https://uk.trustpilot.com/reviews/6af79cabe66a0b7c081fb459 · trustpilot (snorerx.com) · 2026-11-14
- S77 — https://www.youtube.com/watch?v=5sZHGqyN0u8&lc=UgzyDWTbvEmYB7YWSXp4AaABAg · youtube · 2022 (4 years ago)
- S78 — https://www.reddit.com/r/Menopause/comments/1p8fom7/comment/nrdjuxl/ · reddit · 2025-11-29
- S79 — https://discussion.theguardian.com/comment-permalink/173795607 · theguardian.com · 2026-02-07
- S80 — https://www.reddit.com/r/Menopause/comments/1k243nx/comment/mnr1ufy/ · reddit · 2025-04-18
- S81 — https://www.reddit.com/r/GenX/comments/1ak3e65/comment/kp6h0ql/ · reddit · 2024-02-06
- S82 — https://www.reddit.com/r/Menopause/comments/1xpc4ap/dry_nose_and_snoring_disrupting_my_life/ · reddit · 2026-11-06
- S83 — https://www.reddit.com/r/snoring/comments/1us3v9b/hopeless_woman_looking_for_a_nose_snoring/ · reddit · 2026-07-09
- S84 — https://uk.trustpilot.com/reviews/5ebc5c8b25e5d209b8ea2c37 · trustpilot (vitalsleep.com) · 2020-05-13
- S85 — https://uk.trustpilot.com/reviews/63ea3c1b9b64b1bdaf55d800 · trustpilot (vitalsleep.com) · 2023-02-13
- S86 — https://uk.trustpilot.com/reviews/5c801fbc97afa10a783ba898 · trustpilot (vitalsleep.com) · 2019-03-06
- S87 — https://uk.trustpilot.com/reviews/6af52af9282f0b3f27efedde · trustpilot (honexcompany.com) · 2026-11-12
- S88 — https://www.reddit.com/r/Advice/comments/sdyres/my_wife_has_started_snoring_and_its_keepingwaking/ · reddit · 2022-01-27
- S89 — https://www.walmart.com/reviews/product/902897793 · walmart.com (PureSleep) · 6/10/2026
- S90 — https://www.reddit.com/r/AskMenAdvice/comments/1pzby5t/mortifiedwhat_do_guys_think_of_a_women_that_snores/ · reddit · 2025-12-30
- S91 — https://www.menopausematters.uk/forum/index.php?topic=6627.0 · menopausematters.uk
- S92 — https://uk.trustpilot.com/reviews/5e2b23043c93ae0b24964c3b · trustpilot (vitalsleep.com) · 2020-01-24
- S93 — https://uk.trustpilot.com/reviews/6a37ec398bc8997410dfeec7 · trustpilot (sleepzee.co) · 2026-06-21
- S94 — https://www.reddit.com/r/Menopause/comments/1p8fom7/comment/nrhfobr/ · reddit · 2025-11-30
- S95 — https://www.facebook.com/groups/1405682240649555/posts/1520882925796152/ · facebook
- S96 — https://uk.trustpilot.com/reviews/5d2e95ffccd70b06a44d055e · trustpilot (vitalsleep.com) · 2019-07-17
- S97 — https://www.youtube.com/watch?v=UAhgAm4PPis&lc=UgzCZ0ZKUKgpSAa-ZDl4AaABAg · youtube · 2021 (5 years ago)
- S98 — https://www.reddit.com/r/Menopause/comments/1p8fom7/comment/nra6ska/ · reddit · 2025-11-28
- S99 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iurazfk/ · reddit · 2022-11-02
- S100 — https://uk.trustpilot.com/reviews/6a64f7288e97e3fd6c585bac · trustpilot (vitalsleep.com) · 2026-07-25
- S101 — https://www.reddit.com/r/Menopause/comments/11jnitc/who_else_acquired_sleep_apnea_in_perimenopause/ · reddit · 2023-03-06
- S102 — https://www.reddit.com/r/migraine/comments/18tfm67/migraine_and_working_out/kffhduj/ · reddit · 2023-12-29
- S103 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iurgk4u/ · reddit · 2022-11-02
- S104 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iuvasma/ · reddit · 2022-11-03
- S105 — https://www.reddit.com/r/snoring/comments/b27v1t/solutions_to_deal_with_snoring/ · reddit · 2019-03-17
- S106 — https://www.facebook.com/groups/herspaceperimenopauseandmenopausesupport/posts/1013954437279776/ · facebook
- S107 — https://uk.trustpilot.com/reviews/672c98311962722a4876353f · trustpilot (sleeppro.com) · 2024-11-07
- S108 — https://uk.trustpilot.com/reviews/5d4ad506f018690bd04a509d · trustpilot (vitalsleep.com) · 2019-08-07
- S109 — https://www.reddit.com/r/perimenopause_under45/comments/1wa84jw/what_age_did_peri_start_for_you/p8n26ou/ · reddit · 2026-09-08
- S110 — https://www.reddit.com/r/snoring/comments/1aoduv7/success_after_6_months_of_frustration/ · reddit · 2024-02-11
- S111 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iuvhs6l/ · reddit · 2022-11-03
- S112 — https://www.reddit.com/r/Menopause/comments/1k243nx/snoring_is_now_1000_worse/ · reddit · 2025-04-18
- S113 — https://www.facebook.com/mary.martin.10485546/posts/how-many-women-now-snore-is-it-happening-for-you-i-have-become-one-of-them-see-h/10229231466044501/ · facebook
- S114 — https://www.reddit.com/r/Menopause/comments/yjyvxi/comment/iuvajz3/ · reddit · 2022-11-03
- S115 — https://www.facebook.com/groups/996346809343075/posts/1034345952209827/ · facebook
- S116 — https://uk.trustpilot.com/reviews/5e1e35ccc8454503e831f859 · trustpilot (vitalsleep.com) · 2020-01-14
- S117 — https://www.reddit.com/r/Menopause/comments/1wxazov/comment/pduiiq5/ · reddit · 2026-10-04
- S118 — https://www.facebook.com/groups/herspaceperimenopauseandmenopausesupport/posts/1262353459106538/ · facebook_group
- S119 — https://www.facebook.com/carla.almeida.54540/posts/okay-who-else-snores-because-apparently-i-do-my-husband-keeps-waking-me-up-becau/10232152856946182/ · facebook
- S120 — https://www.mumsnet.com/talk/general_health/2152590-Just-been-told-I-SNORE-horrifically-Want-to-cry · mumsnet
- S121 — https://www.mumsnet.com/talk/am_i_being_unreasonable/2451945-To-divorce-DH-for-snoring?page=2 · mumsnet
- S122 — https://www.reddit.com/r/AmIOverreacting/comments/1upcwqd/aio_about_sharing_a_bed_on_a_40th_birthday_trip/owmrcto/ · reddit · 2026-07-10
- S123 — https://www.reddit.com/r/snoring/comments/v0wa40/snoring_getting_worse/ · reddit · 2022-05-30
- S124 — https://uk.trustpilot.com/reviews/6aa6551c9d613ff9383551b1 · trustpilot (sleeppro.com) · 2026-09-13
- S125 — https://uk.trustpilot.com/reviews/6a2849a1d11acd8a75ad7ca0 · trustpilot (mutesnore.com) · 2026-06-09
- S126 — https://uk.trustpilot.com/reviews/6344c0119b12f67dfedd8a39 · trustpilot (vitalsleep.com) · 2022-10-11
- S127 — https://www.reddit.com/r/WomenOver40/comments/1niizj9/comment/nejbe2t/ · reddit · 2025-09-16
- S128 — https://x.com/i/status/2093174182129635497 · x.com · 2026-08-28
- S129 — https://www.reddit.com/r/Menopause/comments/1k243nx/comment/mnsvqlp/ · reddit · 2025-04-18
- S130 — https://www.reddit.com/r/MuslimMarriage/comments/1ur1d87/how_to_gently_approach_my_husband_about_changes/owgjcf8/ · reddit · 2026-07-09
- S131 — https://www.reddit.com/r/Menopause/comments/1k243nx/comment/mnr55pm/ · reddit · 2025-04-18
- S132 — https://x.com/i/status/489526933118394368 · x.com · 2014-07-16
- S133 — https://www.facebook.com/groups/arnica/posts/10164508012386789/ · facebook
- S134 — https://www.facebook.com/groups/quiltretreats/posts/779777467834688/ · facebook
- S135 — data/amazon_trick_V2.md — Amazon UK /dp/ "Customers say" summaries (Somnofit-S, SomnoGuard 3, Longevity Sleep Tape B0CBCQ8YT6, Breathe Right Original) · scraped 2026-11-23 · DATA
- S136 — https://www.reddit.com/r/WomenOver40/comments/1niizj9/suddenly_i_snore/ · reddit · 2025-09-16
- S137 — https://www.reddit.com/r/AskWomenOver30/comments/p3hjaw/women_who_snore_or_used_to_snore_how_do_or_did/ · Reddit · 2021-08 · VERBATIM
- S138 — https://www.reddit.com/r/snoring/comments/1j5hqyr/ladies_when_did_you_first_realize_you_snore/ · reddit · 2025-03-07
- S139 — https://www.mumsnet.com/talk/am_i_being_unreasonable/3777973-Ending-a-relationship-because-of-my-snoring · mumsnet
- S140 — https://www.facebook.com/groups/dullwomenscluboriginal/posts/1148253852967111/ · facebook_group
- S141 — https://www.reddit.com/r/datingoverforty/comments/14rc6gv/she_snores_loud/ · Reddit · VERBATIM
- S142 — https://www.reddit.com/r/AskMen/comments/1owx2r8/how_do_you_deal_with_your_wifes_snoring/ · Reddit · VERBATIM
- S143 — https://www.reddit.com/r/GenX/comments/1ak3e65/wife_snores_need_suggestions/ · reddit · 2024-02-06
- S144 — data/discourse_V1.md — V1 discourse-volume note (Reddit + Mumsnet query counts) · 2026-11-23 · DATA

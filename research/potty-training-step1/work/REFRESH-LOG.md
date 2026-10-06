# REFRESH-LOG — §3–§11 numbers re-run on the 601-row bank (2026-10-06)

**What was done:** every count cited in the 17 files below was re-run against `work/2C-databank.csv` (601 rows; was 514) with `work/3-11-src/cuts.py`, `work/2C-src/tally.py` and two new read-only cuts (locked-segment cut + old/new side-by-side lookup). Commands, scripts and full output: **work/tallies-3-11-601.md**. Numbers were changed in place; wording was kept except where a conclusion moved, and each such place carries an inline *(Refresh 601: …)* note.

**Conventions used in the edited files:**
- "seg" / "segment B" = ND / sensory OR late-trainer OR school-age parent: **161 → 225**.
- "locked" / "locked cut" = buyer group "school-age accidents parent" (the §11-locked customer): **19 → 79**. Added next to the whole-bank number in §3, §3A, §5, §6, §8, §10, §10B, §11 (and in §4, §7, §9, §9B, LOCK-decision, D1-s2-LOCKED where a segment claim is made).
- Not touched: numbers that do not come from the bank (ad log, Winning Hunter / SimilarWeb / Amazon-aspect figures, Saphire / Bloomwise ad counts, prices, medical stats). The "Data-bank rows cited" footers were not regenerated: every cited row is in the first 514 rows, which are byte-identical.

## Conclusion-level changes
1. **§6 lead emotion (D3-s6.md, echoed in D4-s4.md / D3-s11.md):** Fear is now clearly first, no longer tied with Apathy — segment B Fear 40 vs Apathy 23 (was 18 / 18); locked cut **Fear 24 of 79 (30%)** vs Apathy 7. **Guilt is 0 of 79** in the locked cut, so "Guilt underneath" holds only for segment B. The decision (write Fear → Courage, not Anger) is unchanged and better supported.
2. **§3 venues (D2-s3.md):** in segment B r/Parenting (28) overtook What to Expect (20) for #2 behind r/Autism_Parenting (37). For the **locked customer the #1 venue is r/Parenting (16), then r/kindergarten (13), Mumsnet (10); r/Autism_Parenting has only 4**.
3. **§3 / §10 trusted voices (D2-s3.md, D2-s10.md):** the locked customer cites **pediatric urologist 3 · pediatrician 3 · other parents 2**, and "creator with lived experience" 0 (it stays #1 in segment B at 7).
4. **§10 pains (D2-s10.md):** segment B top 5 is now late 74 · **school accidents 34 (up from #3 to #2)** · not noticing 20 · deadline 19 · sensory 16 / constant accidents 16. The **locked cut's top pains are school accidents 34 · constant accidents 16 · not noticing 8 · late / deadline / regression 7**. Late training is no longer #1 there, and **sensory (1) and size (0) drop out**. The So-What "PDP around late, school accidents, not noticing, sensory, size" is flagged inline.
5. **§10 needs (D2-s10.md):** for the locked customer the #1 need is a **routine / reminder system (7 of 79)**, then a **spare-clothes kit for school (4)**; absorbency is 2 of 79. The bank and segment B still rank absorbency #1 (104 / 11).
6. **§10 triggers (D2-s10.md):** **school start is now #1** in segment B (16 vs daycare deadline 10) and in the locked cut (10 vs 4). Bank-wide, daycare deadline (31) is still #1.
7. **§10 beliefs (D2-s10.md):** "constipation causes accidents" doubled (6 → 12 bank; 3 → 7 segment B) and is the **top belief in the locked cut (6 of 79)**. "Own timeline" and "methods don't work for ND kids" are 0 of 79.
8. **§10B ranking (D2-s10B.md):** Miralax / medical rose 2 → 6 and now outranks Goodnites (5). In the locked cut it **ties Pull-Ups for #1 failed solution (4 each)**. Sections were not renumbered (cross-references); a note was added.
9. **§11 objections (D3-s11.md):** no objection count changed, and the **locked cut has 0 tagged objections**, so the ranking rests on whole-bank reviews. Noted as a caveat; the ranking is not changed.
10. **Unchanged conclusions (checked):** problem-aware entry (§5/§7: segment B 67%, locked 70%; product-aware 8% → 7%, locked 3%); "she's burned on methods, not products" (§8: 10 of 225 burned, locked 2 of 79); school-ready = segment #1 desire (§9: 19 of 225; also #1 in the locked cut, 8 of 79); 3-day / Oh Crap still the #3 failed solution; Pull-Ups still #1 bank-wide (67); the PAINKILLER gate still PASSes (D1-s2-LOCKED).

## Every changed number, by file (old → new)

### D2-s3.md
- Segment B 161 of 514 (31%) → 225 of 601 (37%); ND 117 → 132; school-age 19 → 79; late-trainer 64 unchanged; added locked cut 79 of 601 (13%), ND overlap 16
- Age named 5–11: 42 of 514 → 65 of 601 (locked 26 of 79); age 4: 24 unchanged (locked 2); toddler/2–3: 71 → 73 (locked 3)
- dad 20 of 514 → 21 of 601 (locked 1 of 79)
- self-ref dad/father 4 → 5 (mom 17 unchanged); locked cut mom 1 / dad 1
- segment dad 2 of 161 → 3 of 225 (locked 1 of 79)
- Life stage: 42 → 65 quotes name ages 5–11 (locked 26 of 79)
- Household: husband 5, single 1, twins 11 unchanged; added locked cut 0/0/0 of 79
- Money words 32 of 514 → 32 of 601; segment 1 of 161 → 1 of 225; locked 0 of 79
- Work words 33 of 514 → 36 of 601; segment 7 of 161 → 9 of 225; locked 2 of 79
- Venues: r/Autism_Parenting 31 of 161 → 37 of 225; WTE 20 (now #3); r/Parenting 15 → 28 (now #2); locked cut r/Parenting 16, r/kindergarten 13, Mumsnet 10, r/Autism_Parenting 4 — CONCLUSION CHANGED
- Religious words 1 of 514 → 2 of 601; segment 0 → 1; locked 1 of 79 (conclusion 'not a lens' holds)
- waste of money 34 of 514 → 34 of 601 (locked 0 of 79)
- Authorities seg B: creator 7, other parents 4, OT 3, ABA 2 unchanged; new ped urologist 3, pediatrician 3 in seg; locked cut ped urologist 3, pediatrician 3, other parents 2, PT 1, ERIC 1, creator 0 — CONCLUSION NUANCED for locked customer
- Where to find her: added locked-cut venue order (r/Parenting 16, r/kindergarten 13, Mumsnet 10, BabyCenter Community 5)
- Sources: added tallies-3-11-601.md

### D2-s3A.md
- Launch ICP 161 of 514 → 225 of 601 (segment B); locked cut 79 of 601
- Added locked-cut definition line
- #1 toddler parent 199 of 514 → 199 of 601 (locked 0)
- #2 working parent 61 of 514 → 61 of 601 (locked 7)
- #3 night 47 of 514 → 47 of 601 (locked 0)
- #4 withholding segment overlap 11 unchanged; locked 3
- #4 withholding 28 of 514 → 28 of 601 (locked 3)
- #5 grandparent 9 of 514 → 9 of 601 (locked 0)
- Dads 20 → 21; r/daddit 18 → 19; locked 1
- Childcare 12, regression 17, twins 11, eco 9 unchanged (locked 0 each); noted new groups commentator 21, school teacher 4

### D4-s4-DRAFT.md
- No bank-derived numbers changed. The file cites only ad-log counts (10 / 18 / 14 of 40 hooks — tally #17 / #19, unchanged on re-run) and external figures (0 of 908 ads, 19 complaints [M24], 1,684 persona ads).

### D4-s4.md
- Segment emotions Fear 18 → 40, Apathy 18 → 23, Anger 4 → 7; locked Fear 24, Apathy 7, Anger 4 (Courage-not-fear decision unchanged; Fear now clearly dominant)

### D4-s4B-DRAFT.md
- won't hold pee 47 of 514 → 47 of 601 (count unchanged)
- late training = lazy parenting 3 → 4; judgment / shame 26 → 30

### D4-s4B.md
- bigger-sizes need 23 → 24 (size pain 18 unchanged)

### D1-s5.md
- Seg problem-aware 108 of 161 (67%) → 150 of 225 (67%); locked 55 of 79 (70%)
- Seg product-aware 13 of 161 (8%) → 16 of 225 (7%); locked 2 of 79 (3%)
- §5 table: seg n 161 → 225: problem 108 (67%) → 150 (67%), solution 40 (25%) → 59 (26%), product 13 (8%) → 16 (7%); bank n 514 → 601: unaware 1 (0%), problem 195 (38%) → 250 (42%), solution 145 (28%) → 174 (29%), product 173 (34%) → 176 (29%); added locked column 0 / 55 (70%) / 22 (28%) / 2 (3%) / 0
- Source note for locked column
- So-what: 8% → 7% product-aware (locked 3%)
- Sources: added tallies-3-11-601.md

### D3-s6.md
- Headline 'Fear + Apathy, Guilt underneath': CONCLUSION SHARPENED — Fear now dominant (seg 40 vs Apathy 23; locked 24 vs 7); Guilt 0 in locked cut
- Seg B emotions n 161 → 225: Neutrality 88 → 107, Fear 18 → 40, Apathy 18 → 23, Pride 8 → 13, Guilt 8, Acceptance 7 → 12, Anger 4 → 7, Shame 3, Willingness 3 → 4, Desire 2 → 3, Grief 2 → 4, Courage (new) 1; added locked block Neutrality 30, Fear 24, Apathy 7, Pride 4, Guilt 0, Acceptance 5, Anger 4, Shame 0, Willingness 1, Desire 1, Grief 2, Courage 1
- Bank emotions n 514 → 601: Neutrality 190 → 223, Pride 81 → 86, Anger 80 → 86, Fear 43 → 66, Apathy 39 → 44, Acceptance 17 → 26, Desire 17 → 18, Shame 15, Guilt 15, Grief 9 → 11, Willingness 7 → 8, Courage 1 → 3
- Bank Anger 80 → 86
- Segment Anger 4 → 7 (locked 4)
- Fear 18 → 40 (locked 24)
- Apathy 18 → 23 (locked 7)
- Guilt 8 unchanged (locked 0)
- Shame 3 unchanged; judgment/shame pain seg 13 → 14 (locked Shame 0, pain 3)
- Grief 2 → 4 (locked 2)
- Pride / Acceptance 8 + 7 → 13 + 12 (locked 4 + 5)
- Sources: added tallies-3-11-601.md

### D1-s7.md
- Segment product-aware 8% → 7% (problem 67% unchanged); locked 70% / 3%

### D1-s8.md
- Burned 71 of 514 (14%) → 74 of 601 (12%)
- nothing works 14 → 15; tried everything 7 → 8; skeptical 3 → 4 (waste of money 34, scam 19 / 15 UpAiry unchanged)
- Segment burned 8 of 161 (5%) → 10 of 225 (4%): nothing works 4 → 5, tried everything 3 → 4, scam 1; added locked 2 of 79 (3%)
- methods don't work for ND kids 6 unchanged (locked 0)
- Category level: 14% → 12% burned (25 of 27 UpAiry unchanged)
- Sources: added tallies-3-11-601.md

### D3-s9.md
- every kid own timeline 10 → 13 bank (seg 8, locked 0); readiness matters 9/5 → 10/6 (locked 1)
- late = lazy 3 → 4; untrained at 5 = severe delay 1 → 2; judgment/shame pain 26 → 30
- Pull-Ups failed solution 61 → 67
- school-ready desire seg 18 of 161 → 19 of 225 (locked 8 of 79, #1); bank 38 of 514 → 39 of 601 (still #2 after dry nights 43)
- Sources: added tallies-3-11-601.md

### D3-s9B.md
- Header n 514 → 601; segment 161 → 225; locked 79 noted
- Belief 1: judgment 26 → 30; late = lazy 3 → 4 (trained by 2/3 4, parent guilt 19 unchanged)
- Belief 2: Pull-Ups 61 → 67; daily school accidents 21 → 38 (locked 34)
- Belief 4: absorbency 101 → 104; bigger sizes 23 → 24
- Belief 5: sensory-friendly fit 15 → 16; sensory discomfort 15 → 17
- Sources: added tallies-3-11-601.md

### D2-s10.md
- §10 Pains re-ranked on 601 bank counts (55 → 56 distinct): late 70 → 74 (seg 70 → 74, locked 7); leaks/soaked 54 → 55 (seg 2 → 3, locked 1); deadline 41 (seg 19, locked 7); daily school accidents 21 → 38 (seg 18 → 34, locked 34; moved #9 → #4); burnout 31 → 34 (seg 9 → 12, locked 4); judgment 26 → 30 (seg 13 → 14, locked 3); withholding 29 (seg 12, locked 3); night wetting 27 → 29 (seg 2 → 4, locked 2); doesn't notice wet 22 → 28 (seg 15 → 20, locked 8); regression 17 → 24 (seg 0 → 7, locked 7; moved #14 → #10); parent guilt 19 (seg 8, locked 0); size 18 (seg 11, locked 0); leaks bed 18 (locked 0); constant accidents 2 → 18 (seg 0 → 16, locked 16; promoted from two-mention list to #14); child refuses 17 (seg 13, locked 1); sensory discomfort 15 → 17 (seg 14 → 16, locked 1); sizing 17 (seg 3); laundry 14 → 15 (locked 1); cost 14 (seg 4); hidden sub 14; child shame 10 → 13 (seg 1 → 3, locked 2); can't communicate 11 → 12 (seg 11 → 12, locked 1); daycare rules 10; fear teased 2 → 6 (seg 3, locked 2; promoted to #24); limited time 4 → 5 (locked 1); long tail 19 → 20 items (+ child afraid to ask at school). Segment top 5: late 70 → 74 · school accidents 18 → 34 (now #2) · notice wet 15 → 20 · deadline 19 · sensory 14 → 16 / constant 16. Added locked top 5 — CONCLUSION CHANGED
- Header: bank 514 → 601; seg 161 → 225; added locked 79
- Sources: added tallies-3-11-601.md
- Objections 25 distinct and all counts unchanged; added locked cut 0
- §10 Needs (29 → 31 distinct): absorbency 101 → 104 (seg 8 → 11, locked 2); feel-wet 43 (seg 10, locked 1); bigger sizes 23 → 24 (seg 15 → 16, locked 1); sensory-friendly fit 15 → 16 (seg 15 → 16, locked 0); routine/reminder 7 → 14 (seg 6 → 11, locked 7; moved #11 → #7); fun designs 10 → 11 (locked 1); discreet 6 → 10 (seg 1 → 3, locked 2; moved #14 → #11); new spare-clothes kit for school 7 (seg 4, locked 4); real-underwear look w/ protection 2 → 3 (locked 1; moved out of two-mention list); new one-mention school accommodation. Locked #1 need = routine/reminder — CONCLUSION CHANGED for locked customer
- §10 Desires: dry nights 43 (locked 0); school-ready 38 → 39 (seg 18 → 19, locked 8 = locked #1); less mess 28 → 29; no-pressure 19 (seg 7); feel wet 15; independence 6 → 10 (seg 2, locked 2) now ranks #6 above dignity 7 → 9 (seg 2, locked 2) — order of #6/#7 swapped
- Misconception late = lazy 3 → 4 (now tied with #1/#2 at 4; numbering kept so the 'we correct #…' line stays valid)
- Misconception untrained at 5 = severe delay 1 → 2
- Misconceptions: added locked cut (pull-ups at 4.5 = neglect 1)
- §10 Mindset beliefs re-ranked: own timeline 10 → 13; constipation 6 → 12 (moved #6 → #4); readiness 9 → 10; no-shame 6 → 9; single-mention beliefs 12 → 13 (25 → 26 distinct). Segment top: own timeline 8 · constipation 3 → 7 (new #2) · ND methods 6 · readiness 5 → 6. Locked top: constipation 6, readiness 1 — CONCLUSION CHANGED for locked customer
- Trust: creator 7 in segment unchanged; locked cut creator 0, ped urologist 3, pediatrician 3, other parents 2
- Pro-therapy OT 3, ABA 2 unchanged; locked 0/0; pediatrician 3, ped urologist 3 in seg and locked
- §10 Triggers (26 → 27 distinct): deadline 31 (seg 10, locked 4); school start 11 → 20 (seg 9 → 16, locked 10); relative judgment 9 → 10 (seg 4 → 5, locked 1; now #4 above soaked bed 9); school/teacher complaint 3 → 6 (seg 3 → 5, locked 4; moved #9 → #6); outgrew 4 (seg 2); one-mention 11 → 12 (+ accidents at school). School start now #1 in seg B and locked cut — CONCLUSION CHANGED
- Miralax / medical 2 → 6 (seg 4, locked 4)
- 4 forces Push: school accidents 18 → 34 seg (locked 34); size 11 seg (locked 0); judgment 13 → 14 seg (locked 3); burnout 31 → 34 bank (locked 4). Pull: school-ready 18 → 19 seg (locked 8); dignity 7 → 9 (locked 2); less mess 28 → 29 (locked 0); no-pressure 19 (locked 0)
- Anxiety: sensory 15 → 16 (sensory-friendly fit need; sensory discomfort pain is 17). Objection counts 47/16/15/13/10/5 unchanged; locked cut 0 objections
- Habit: own timeline 10 → 13
- So-what 'PDP around top 5 pains: late, school accidents, not noticing, sensory, size' — CONCLUSION CHANGED (noted inline)

### D2-s10B.md
- Header n 514 → 601, seg 161 → 225, locked 79; note Miralax 6 now outranks Goodnites 5 (sections not renumbered); locked failed solutions listed
- #1 Pull-Ups 61 → 67 (seg 8 → 12, locked 4)
- #2 UpAiry 27 unchanged (seg 1, locked 0)
- #3 3-day 23 unchanged (seg 4, locked 0)
- #4 generic 22 unchanged (seg 6, locked 1)
- #5 MooMoo 13 unchanged (seg 2, locked 0)
- #6 BIG ELEPHANT 11 unchanged (seg 1, locked 0)
- #7 rewards 8 unchanged (seg 4, locked 0)
- #9 Goodnites 4 → 5 (seg 2 → 3, locked 1)
- #12 Miralax / medical 2 → 6 (seg 4, locked 4 = ties Pull-Ups for locked #1) — ranking note added
- Sources: added tallies-3-11-601.md

### D3-s11.md
- Added '(locked 0)' to all 25 objection rows — the 79-row locked cut has 0 tagged objections; all 25 bank objection counts unchanged
- Ranking header n 514 → 601; locked cut has 0 objections (ranking unchanged; caveat added)
- #5 bigger sizes need 23 → 24 (locked 1); sizing pain 17 (locked 0)
- #7 sensory discomfort 15 → 17 (child refuses 17; locked 1/1)
- Checklist: judgment 26 → 30; late 70 → 74 (locked 3 / 7)
- Checklist: laundry pain 14 → 15
- Checklist: fun designs 10 → 11; dignity 7 → 9 (locked 1 / 2)
- Full-containment 26 of 161 → 30 of 225 (locked 6 of 79)
- Anger 4 → 7 in segment (locked 4); Fear 40 / 24 added
- Sources: added tallies-3-11-601.md

### D1-s2-LOCKED.md
- PAINKILLER row: segment 161 of 514 → 225 of 601 (+ locked 79); late training 70 → 74; school accidents 18 → 34 (locked 34); judgment 13 → 14; size 11 unchanged. PASS unchanged

### LOCK-decision.md
- Segment 161 of 514 → 225 of 601 (problem-aware 67% unchanged); locked 79, 70%
- Pains: late 70 → 74; school accidents 18 → 34 (locked 34); judgment 13 → 14; sensory 14 → 16; size 11
- Full-containment 26 of 161 → 30 of 225 (locked 6 of 79)
- §2C revision item: 161 rows → 225; awareness 67/25/8% → 67/26/7%; full-containment 26 → 30; locked 79, 70/28/3%, 6
- school-age accidents parent 19 → 79 (action marked done)

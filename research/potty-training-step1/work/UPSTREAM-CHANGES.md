# UPSTREAM-CHANGES — numbers that changed after the re-tally (2026-10-06)

**Why this file exists:** the §11 lock sharpened the market to "Big kids still learning" (US, 5–9, daytime). Per the page's lock rule, §0–§2C were brought in line, and the §2C bank was extended from **514 → 601 rows** (+87; locked-segment rows **19 → 79**). This file lists every number that changed, old → new, with the file and line where the old number still sits, so §3–§11 can be refreshed. **The §3–§11 files were NOT edited by this pass** (they belong to the writers).

**Reproduce every "new" count:**
- `python3 work/2C-src/build_bank.py` → `work/2C-databank.csv` (601 rows; the first 514 are byte-identical to the old file).
- `python3 work/2C-src/tally.py` → `work/2C-tally.md` (adds the locked-segment cut).
- `python3 work/3-11-src/cuts.py > work/3-11-src/cuts-output-601.txt` (the old run is kept as `cuts-output.txt`).

**Two segment definitions — keep them apart:**
- **Segment B** (the wave-1 definition used in §3–§11): ND / sensory OR late-trainer OR school-age parent. **161 → 225.**
- **Locked cut** (new): school-age accidents parent only (a 5–9 child with daytime accidents). **19 → 79.** Recommended for §3–§11 headline counts from now on; Segment B stays as the broader ND / late frame.

## 1 · Bank-level numbers (whole bank)
| Metric | Old (n = 514) | New (n = 601) | Where the old number sits |
|---|---|---|---|
| Total snippets | 514 | **601** | D2-s3.md:8, 9, 24, 38, 45, 67, 81 · D2-s3A.md:3, 16, 36, 55, 75, 92 · D1-s5.md:26 · D3-s6.md:18 · D1-s8.md:34 · D3-s9.md:64 · D3-s9B.md:4 · D2-s10.md:3 · D2-s10B.md:3 · D3-s11.md:3 · tallies-3-11.md:2, 91 · LOCK-decision.md:44 · D1-s2-LOCKED.md:32 |
| Source types | Reddit 232 · Forum 91 · YouTube 23 · Amazon 77 | Reddit **293** · Forum **112** · YouTube **27** · Amazon **78** (others unchanged) | D2-2C-summary.md (rewritten) |
| Capture | 140 VERBATIM · 374 SNIPPET | **144** VERBATIM · **457** SNIPPET | D2-2C-summary.md (rewritten) |
| Pain: late training (3.5y+) | 70 | **74** | LOCK-decision.md:45 · D1-s2-LOCKED.md:32 · D2-s10.md:64 · tallies-3-11.md:127 |
| Pain: daily accidents at school/daycare | 21 | **38** | D3-s9B.md:20 |
| Pain: judgment / shame from others | 26 | **30** | D3-s9B.md:10 |
| Pain: child doesn't notice wet | 22 | **28** | 2C summary |
| Pain: regression | 17 | **24** | 2C summary |
| Pain: parent burnout | 31 | **34** | 2C summary |
| Need: absorbency that holds a pee | 101 | **104** | D3-s9B.md:38 · D2-s10.md:76 |
| Need: bigger sizes | 23 | **24** | D4-s4B.md:20 · D3-s11.md:26 · D3-s9B.md:38 |
| Need: routine / reminder system | 7 | **14** | 2C summary |
| Failed solution: Pull-Ups / disposables | 61 | **67** | D3-s9.md:26 · D3-s9B.md:20 · D2-s10B.md:10 · tallies-3-11.md:174 |
| Failed solution: Miralax / medical | 2 | **6** | 2C summary |
| Desire: daycare/school-ready | 38 | **39** | D3-s9.md:64 · D2-s10.md:99 |
| Desire: child dignity / real underwear | 7 | **9** | D2-s10.md:214 |
| Desire: less mess / cleanup | 28 | **29** | D2-s10.md:214 |
| Trigger: school start (K/Reception) | 11 | **20** | 2C summary |
| Trigger: school/teacher complaint | 3 | **6** | 2C summary |
| Belief: constipation causes accidents | 6 | **12** | 2C summary |
| Belief: every kid own timeline | 10 | **13** | 2C summary |
| Belief: no shame approach | 6 | **9** | 2C summary |
| Authority: pediatrician | 2 | **6** | 2C summary |
| Buyer group: ND / sensory parent | 117 | **132** | D2-s3.md:8 · tallies-3-11.md:94, 97 |
| Buyer group: school-age accidents parent | 19 | **79** | D2-s3.md:8 · LOCK-decision.md:135 · tallies-3-11.md:94, 97 |
| Buyer group: dad | 20 | **21** | D2-s3.md:24 |
| Awareness split | problem 195 (38%) · solution 145 (28%) · product 173 (34%) | problem **250 (42%)** · solution **174 (29%)** · product **176 (29%)** | D1-s5.md:29 (+ the rest of the §5 table) |
| Burned / skeptical | 71 of 514 (14%) | **74 of 601 (12%)** | D1-s8.md:34 |
| Emotional states | Neutrality 190 · Pride 81 · Anger 80 · Fear 43 · Apathy 39 · Acceptance 17 · Desire 17 · Shame 15 · Guilt 15 · Grief 9 · Willingness 7 · Courage 1 | Neutrality **223** · Pride **86** · Anger **86** · Fear **66** · Apathy **44** · Acceptance **26** · Desire **18** · Shame 15 · Guilt 15 · Grief **11** · Willingness **8** · Courage **3** | D3-s6.md:18–19 |
| Quotes naming a child aged 5–11 | 42 of 514 | **65 of 601** | D2-s3.md:9 |
| Quotes naming a toddler / 2–3-year-old | 71 | **73** | D2-s3.md:9 |
| Keyword hits — work words (all \| seg B) | 33 \| 7 | **36 \| 9** | D2-s3.md:45 |
| Keyword hits — money words (all \| seg B) | 32 \| 1 of 161 | 32 \| 1 **of 225** | D2-s3.md:38 |
| Keyword hits — god / church / pray (all \| seg B) | 1 \| 0 | **2 \| 1** | D2-s3.md:67 |
| Keyword hits — school / teacher / kindergarten (all \| seg B) | 24 \| 16 | **57 \| 42** | tallies-3-11.md (#7) |
| Keyword hits — shame / embarrass / judg (all \| seg B) | 19 \| 7 | **25 \| 10** | tallies-3-11.md (#7) |
| Great phrases captured | 242 | **271** | 2C-tally.md |

**Unchanged (no new rows touched them):** objections (all values, e.g. "won't hold pee / leaks" 47, scam 16, holds one small accident 14, sizing 13); "waste of money" 34 (D2-s3.md:81); general toddler parent 199; working parent / daycare 61 and its 37 / 21 / 3 awareness split (D2-s3A.md:36–40); night / bedwetting 47 (D2-s3A.md:55); withholding 28 (D2-s3A.md:75); grandparent 9 (D2-s3A.md:92); "feeling wet teaches the child" 25; "dry nights" 43; 3-day / Oh Crap 23 (D2-s10.md:193); size / big-kid products pain 18 (D4-s4B.md:20); "ads overpromise" 5.

## 2 · Segment B numbers (161 → 225)
| Metric | Old (n = 161) | New (n = 225) | Where the old number sits |
|---|---|---|---|
| Segment size | 161 of 514 (31%) | **225 of 601 (37%)** | D2-s3.md:8 · D2-s3A.md:3 · D1-s5.md:4–5, 26 · D3-s6.md:12 · D1-s8.md:45 · D3-s9.md:64 · D3-s9B.md:4 · D2-s10.md:3 · D2-s10B.md:3 · D3-s11.md:77 · tallies-3-11.md:13, 91 · LOCK-decision.md:44, 46, 134 · D1-s2-LOCKED.md:32 |
| Awareness | problem 108 (67%) · solution 40 (25%) · product 13 (8%) | problem **150 (67%)** · solution **59 (26%)** · product **16 (7%)** | D1-s5.md:4, 5, 29 · LOCK-decision.md:44, 134 · tallies-3-11.md:154, 164 |
| Pain: daily accidents at school/daycare ("school accidents") | 18 | **34** | LOCK-decision.md:45 · D1-s2-LOCKED.md:32 · D2-s10.md:64 · tallies-3-11.md:127 |
| Pain: doesn't notice wet | 15 | **20** | D2-s10.md:64 |
| Pain: sensory discomfort | 14 | **16** | LOCK-decision.md:45 · D2-s10.md:64 |
| Pain: judgment / shame | 13 | **14** | LOCK-decision.md:45 · D1-s2-LOCKED.md:32 · D3-s6.md:36 |
| Pain: size / big-kid products | 11 | 11 (unchanged) | LOCK-decision.md:45 |
| **Segment top-5 pains** | late 70 · deadline 19 · school accidents 18 · doesn't notice wet 15 · sensory 14 | late **74** · school accidents **34** · doesn't notice wet **20** · deadline 19 · sensory **16** / constant accidents **16** | D2-s10.md:64 |
| Full-containment language (#16) | 26 of 161 | **30 of 225** (locked cut: **6 of 79**) | LOCK-decision.md:46, 134 · D3-s11.md:77 |
| Burned / skeptical | 8 of 161 (5%) | **10 of 225 (4%)** | D1-s8.md:45 |
| Desire: daycare/school-ready (seg #1) | 18 | **19** | D3-s9.md:64 · D2-s10.md:99, 214 |
| Need: absorbency that holds a pee | 8 | **11** | D2-s10.md:76 |
| Need: bigger sizes | 15 | **16** | tallies-3-11.md (#8) |
| Need: routine / reminder system | 6 | **11** | tallies-3-11.md (#8) |
| Failed solution: Pull-Ups / disposables | 8 | **12** | D2-s10B.md:10 |
| Trigger: school start | 9 | **16** (now seg #1, ahead of daycare deadline 10) | tallies-3-11.md (#8) |
| Belief: constipation causes accidents | 3 | **7** | tallies-3-11.md (#8) |
| Dad in segment | 2 of 161 | **3 of 225** | D2-s3.md:26 |
| Top venues | r/Autism_Parenting 31 · What to Expect 20 · r/Parenting 15 | r/Autism_Parenting **37** · **r/Parenting 28** · What to Expect 20 · **Mumsnet 15** · **r/kindergarten 13** | D2-s3.md:58 |
| Emotional states | Neutrality 88 · Fear 18 · Apathy 18 · Pride 8 · Guilt 8 · Acceptance 7 · Anger 4 · Shame 3 · Willingness 3 · Desire 2 · Grief 2 | Neutrality **107** · Fear **40** · Apathy **23** · Pride **13** · Acceptance **12** · Guilt 8 · Anger **7** · Willingness **4** · Grief **4** · Shame 3 · Desire **3** · Courage **1** | D3-s6.md:12–16, 21 ("only 4 Anger rows" → 7), 24 ("Fear (18)" → 40), 36 |
| Rows naming age 4+ or bigger sizes (#15) | 78 | **102** | tallies-3-11.md (#15) |

## 3 · NEW numbers — the locked-segment cut (79 rows; no old equivalent beyond "19 rows")
Use these as the §3–§11 headline counts for "big kids still learning":
- Pain: **daily accidents at school 34** · constant accidents 16 · doesn't notice wet 8 · late training 7 · deadline 7 · regression 7.
- Trigger: **school start 10** · daycare/preschool deadline 4 · school/teacher complaint 4 · school says back to nappies 2.
- Need: **routine / reminder 7** · **spare-clothes kit for school 4** · absorbency 2 · discreet 2.
- Desire: daycare/school-ready 8 · dignity / real underwear 2 · independence 2. Objections: **0**.
- Awareness: **problem 55 (70%) · solution 22 (28%) · product 2 (3%)**.
- Emotion: Neutrality 30 · **Fear 24 (30%)** · Apathy 7 · Acceptance 5 · Anger 4 · Pride 4.
- Authority: **pediatric urologist 3 · pediatrician 3** · other parents 2 · pelvic floor PT 1 · ERIC 1. Belief: **constipation causes accidents 6**.
- ND overlap 16 of 79 · full-containment language 6 of 79.
- Conversation timing (INFERENCE, estimated dates): 22 of 54 dated posts in Aug–Oct.
- Suggested replacement for the "PAINKILLER" evidence line in LOCK-decision.md:45 / D1-s2-LOCKED.md:32: "Locked segment = 79 of 601 snippets (Segment B 225). Daily school accidents 34; school start trigger 10; Fear 30%; late training 74 (bank)."

## 4 · Upstream (§0–§2B) numbers that changed in the LOCKED files
| Item | Old | New | Old file:line → new file |
|---|---|---|---|
| Landed cost / pair | $2.87 (AliExpress toddler $2.27 + $0.60) | **$4.60** (OEM $4.00 + $0.60), duty excluded; $6.00 with ~35% duty | D1-Pre0-rerun.md:11, 13 → D1-Pre0-LOCKED.md |
| Hero offer | 10-pair "Home + Daycare Kit" $79 | **10 for $119** (School-Day Kit), entry **6 for $84** | D1-Pre0-rerun.md:22–25, 29 → D1-Pre0-LOCKED.md |
| CM $ / CM % (hero) | $38.43 / 48.6% | **$59.93 / 50.4%** (6 for $84: $46.88 / 55.8%) | D1-Pre0-rerun.md:35–36 |
| Break-even ROAS (hero) | 2.06 | **1.99** (6 for $84: 1.79) | D1-Pre0-rerun.md:37 |
| Kill line CPA / ROAS (hero) | $22.63 / 3.49 | **$36.13 / 3.29** | D1-Pre0-rerun.md:39–40 |
| Scale line CPA / ROAS (hero) | $14.73 / 5.36 | **$24.23 / 4.91** | D1-Pre0-rerun.md:41–42 |
| With duty (~35%) | — | hero CM $45.93 (38.6%), BE ROAS 2.59, kill $22.13, scale $10.23 | D1-Pre0-LOCKED.md (new) |
| Launch cash | not estimated | **≈ $7.5K–$23.5K** (MOQ goods $4–12K, freight, duty, lab $1.2–2.7K, 3PL, samples) | D1-Pre0-LOCKED.md (new) |
| §0 who it's for | "mostly ages 2–4, long tail to 9" | **5–9, daytime** | D1-s0.md:3 → D1-s0-LOCKED.md |
| §0 mass desire | Urgency 4 · Staying 4 · Scope 5 = **13/15** | Urgency 4 · Staying **5** · Scope **3** = **12/15** | D1-s0.md:30–33 |
| §0 deadline evidence | 38 of 252 (C file) | school accidents 34 of 79; school-start trigger 10 | D1-s0.md:9 |
| §0B segment search | not measured | ≈0–7 on a scale where "potty training underwear" = 100; Aug–Sep school-start peak **not** found in search | D1-s0B.md → D1-s0B-LOCKED.md |
| §1 BrightKidCo | "0 now (peak 107)", longest 42 d | **0 live; underwear last seen 2026-08-31; any ad last seen 2026-09-05; 13 ads ever** | D1-s1.md:21 → D1-s1-LOCKED.md |
| §1 long-list | 22 + marketplace | **31** (+ Saphire, Bloomwise, Super Undies, MooMoo 9T, BIG ELEPHANT big sizes, "8-10Years", Carer / TIICHOO / FUVVRVAL / EZ Moms, Goodnites, Lucky & Me / SmartKnit / WunderUndies) | D1-s1.md:16 → D1-s1-LOCKED.md |
| Saphire active ads | 684 + 226 + 149 (W3/W4 snapshot) | 103 ads to the domain (US index); pages Sarah Mitchell 419 · Dr. James Harper 178 · Try Saphire 98; 30d rev. est. $870K–$1.6M | LOCK-decision.md:25, 114 · D1-s2-LOCKED.md:27 (keep the W snapshot; add U20/U26) |
| Bloomwise | 420 active | 420 active; 139,388 visits (Aug 2026); 30d est. $748K–$1.35M | LOCK-decision.md:115 · D1-s2-LOCKED.md:27 (add U21) |
| Super Undies | $34.99, <20K visits, "Health - Other" | same + **0 ads since 2025** (last US ad 2025-01-28), AOV $90.81, 13,098 visits | D1-s2-LOCKED.md:36 |
| "Nobody states a ml figure" | 0 of 908 ads | still true for **current** US daytime training-underwear ads; but **Goodnites ran "16 oz" in 2023** (night). Scope the claim | D1-s2-LOCKED.md:17 |

## 5 · Refresh checklist for the §3–§11 writers
1. Replace "514" with **601** and "161" with **225** wherever counts are cited; add the **locked cut (79)** next to segment claims.
2. §3 (D2-s3.md:8, 58): venue order is now r/Autism_Parenting 37 → r/Parenting 28 → What to Expect 20 → Mumsnet 15 → r/kindergarten 13.
3. §5 (D1-s5.md:4–5, 26–29): segment awareness stays 67% problem-aware; the locked cut is **70%**.
4. §6 (D3-s6.md): Fear is now the dominant non-neutral state in the segment (40 of 225; **24 of 79** in the locked cut).
5. §8 (D1-s8.md:34, 45): burned 74 of 601 (12%); segment 10 of 225 (4%).
6. §9 / §9B / §10 / §10B: Pull-Ups 67 (seg 12); school-ready 39 (seg 19); absorbency 104 (seg 11); bigger sizes 24; daily school accidents 38 bank / 34 seg.
7. §11 (D3-s11.md:26, 77): bigger sizes 24; full containment 30 of 225 (6 of 79).
8. LOCK-decision.md:44–46, 134–135 and D1-s2-LOCKED.md:32: update the segment evidence line (§3 above).

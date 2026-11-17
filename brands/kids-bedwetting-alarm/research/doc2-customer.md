Here is the result of "fetch" for the Page with URL https://app.notion.com/p/41ad53123cd681269897cff67a4c0c0a as of 2026-11-17T02:25:20.415Z:
<page url="https://app.notion.com/p/41ad53123cd681269897cff67a4c0c0a" icon="👤">
<ancestor-path>
<parent-page url="https://app.notion.com/p/41ad53123cd681129e0eeec522e4d6f4" title="Kids' Bedwetting Alarm — Step 1 Research (2026-11-16)"/>
</ancestor-path>
<properties>
{"title":"Doc 2 — The Customer"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"👤"}</iconMetadata>
<content>
<b>Kids' wireless bedwetting alarm · moms of kids 8–12 · US/UK/CA/AU/NZ · Meta ads · Step 1 Research (2026-11-16)</b>

📂 <b>Research folder (Notion):</b> <mention url="https://app.notion.com/p/41ad53123cd681129e0eeec522e4d6f4">Kids' Bedwetting Alarm — Step 1 Research (2026-11-16)</mention> — Doc 1 Market & Competition · Doc 2 The Customer · Doc 3 Persuasion · Doc 4 Brand, Offer & Funnel · §2C Customer Data Bank

## ⭐ Top 5 takeaways (written after §20 verification)

1. <b>The avatar holds, but it's a ceiling.</b> Kids 8–12 are 50% of threads that state an age, but 7 is the single most common age, and 75% of alarm-review buyers' kids are 5–8. → Keep moms of 8–12; cast and target the child at \~7–10 so the 5–8 buyers aren't shut out.
2. <b>The social stage is the reason to start, not where the alarm is used.</b> \~25% of parent posts mention sleepovers/camp/friends, and 0 families use an alarm at the sleepover (they use pull-ups, desmopressin or a word with the host). → Hooks say "start before the date", never "wear it there".
3. <b>Her real wall is device reliability, not trust.</b> Didn't wake him (48), doesn't work (44), false alarms (37), battery (36), broke (36) vs scam/no delivery (50) once off-topic Saphire rows are removed. → Lead proof with "it actually wakes him and keeps working".
4. <b>The #1 trigger is a date landing.</b> The school camp/trip date arrives (113 · 56 first-hand), then a sleepover invitation (111 · 58), then a friend finding out (45). → Build the ad calendar and hooks around those moments.
5. <b>Her deepest desire is control after years of "wait" (score 397); his is belonging (351).</b> → Write the One Belief on control and the hooks on belonging; never lead with "dry nights" alone.

---

# 2C · Customer data bank — summary

<b>What it is.</b> One merged CSV of real customer snippets: <b>2,232 rows</b>. 65 of them are Unikor's own curated on-site reviews, kept apart because the brand picked them. That leaves <b>2,167 CORE rows</b>; the first draft's ranked lists were a script tally of those rows \[S1\]. It clears the page's bar: 100+ snippets from 4+ source types.

<b>§20 correction (V3) — the first version of this bank was wrong on several headline numbers.</b> 179 of the 201 Saphire / saffron-gummy Trustpilot rows never mention bedwetting; they are ADHD, mood and billing reviews. Keeping them inflated trust (147), subscription (81), gummies (81), anger (106) and "burned" (336). They are now excluded as well, so <b>every ranked list in this doc runs on 1,988 CLEAN rows</b> (2,167 CORE − 179) \[S2\] \[S3\]. The old figure is shown in brackets wherever it moved a lot.

## Snippets per source type (CORE)

- Reddit: <b>923</b> (50 threads with comments + the opening posts of \~300 search-hit threads; r/Parenting, Mommit, breakingmom, daddit, AskParents, ADHDparenting, Autism\_Parenting, UKParenting, AskUK, australia, bedwetting, BoyScouts, laundry, amiwrong and others)
- Amazon reviews: <b>581</b> (10 US /dp/ pages give the "Customers say" excerpts; 13 [amazon.co.uk](http://amazon.co.uk) /dp/ pages give full reviews with stars and dates). This covers 1–2★ and 4–5★.
- Trustpilot: <b>285</b> (Unikor, Saphire, Oopsie Heroes, Dryly, DryBuddy, Stay Dry at Night, Upairy, nidfashions). <b>106 remain in the ranked lists</b> after the 179 off-topic Saphire rows are removed \[S2\]
- Walmart reviews: <b>137</b> (8 alarm listings + GoodNites XL), all with stars and dates
- Forums: <b>105</b> (Mumsnet (UK), Netmums (UK), BabyCenter, What to Expect, Quora titles)
- YouTube comments: <b>52</b> · TikTok comments: <b>46</b> · Facebook groups: <b>25</b> · X: <b>6</b> · other web: <b>7</b> ([drugs.com](http://drugs.com), blogs)
- Excluded from the ranked lists: Unikor on-site reviews: <b>65</b>, all 5★ \[S1\]
- Also excluded (§20 V3): <b>179</b> Saphire / saffron-gummy Trustpilot rows whose text never mentions bedwetting. 22 gummy rows that do mention it stay in \[S2\]

## How it was collected

- <b>Forum tactics</b> ✅ (agent B, agent D). Reddit threads were ranked by comment count through ScrapeCreators, then their comments were pulled. Firecrawl can't scrape [reddit.com](http://reddit.com), so old.reddit was skipped. Thread-title hooks are in §14 \[S4\].
- <b>Amazon trick</b> ✅ (agent E). Firecrawl scraped each listing's /dp/ page for its top reviews and the "Customers say" summary. Full review lists need a login on .com, so the same ASINs were opened on .[co.uk](http://co.uk) instead (🔁). Walmart reviews came through Alexandria and Trustpilot through playwright \[S5\].
- <b>product-pulse</b> ✅ (agent B; partial). The skill ran on "kids bedwetting alarm":
  - <b>X:</b> 9 Alexandria x-com searches plus 3 Firecrawl searches. These returned \~6 usable posts, so X is close to silent on this topic.
  - <b>Reddit:</b> 2 Firecrawl searches, plus ScrapeCreators for depth (50 threads, 966 comments).
  - <b>Skipped on purpose:</b> the skill's Notion-publish step and its save-to-repo step, because this was a collect-only run.
  - <b>Agent E</b> also wrote a review-based pulse \[S6\] \[S7\].
- <b>agent-reach</b> 🔁. The CLI is not installed ("command not found"). Its jobs ran on Firecrawl + Alexandria instead. TikTok/YouTube comments also came through ScrapeCreators instead of playwright \[S4\].

## How to read the counts (honest caveats)

- <b>The tags are noisy.</b> Agents B and E tagged rows with keyword rules, which get roughly 10–25% wrong.
  - I merged label variants with a NORM dictionary.
  - I re-checked noisy labels with a confirm-regex on the quote. Example: "battery / charging" was firing on Saphire's billing "charges"; after the check it fell from 72 to 36 rows (the first draft printed 40; the tally says 36).
  - I read samples behind every published item.
  - <b>Read every (n) as a ranking, not a census</b> \[S8\].
- <b>Search bias.</b> Agents B and D searched "9/10/11 year old", "sleepover" and "camp" on purpose. That means the <b>8–12 share and the social-stage share are an UPPER BOUND</b> \[S9\].
- <b>A count is a snippet, not a person.</b> One long thread can give 20 rows.
- <b>One vote per thread changes the picture (§20 V3).</b> Per-row counts double-count long threads: one 9–11-year-old thread can add 20 rows. Where it matters (child age), this doc now shows the unique-thread count too \[S10\].
- <b>Social-stage labels are the noisiest (§20 V3).</b> In a hand-read sample, sleepover / camp / friend labels were wrong about 4–5 times in 10 (advice from scout leaders, teachers or adults, not a first-hand pain or trigger). Use the §18 first-hand counts for triggers. Estimated noise: 25–45% on social labels, 10–25% on the rest \[S3\].
- <b>AITA-style subs are low credibility (§20 V3).</b> At least 33 rows come from r/amiwrong (15), r/AmIOverreacting (11), AITAH / AmItheAsshole (6) and TrueOffMyChest (1). Some are template or troll posts; quotes from them are flagged where used \[S3\].
- <b>Evidence tags on quotes (§20 V3).</b> \[VERBATIM\] = re-opened live by the §20 verifier and the wording matched. \[SNIPPET\] = copied from the collected bank (API pull, search excerpt or a login-walled Amazon US "Customers say" excerpt) and not re-opened; confirm at the URL before it goes into live creative.
- <b>The buyer-group tag has known errors.</b> Two moms are tagged "pediatric/medical professional", for example the "social suicide" post \[S11\].

## Top 10 per tag (CLEAN bank, verified counts — quotes live in their sections)

All counts \[S2\] (first draft: \[S1\])

- <b>Pain:</b> child ashamed / embarrassed (171) · can't go to sleepovers (108) · camp / school-trip fear (100) · wets every night (77) · endless laundry (72) · fear of friends finding out / teasing (70) · parent sleep loss (68) · deep sleeper can't wake (56) · pull-ups leak / outgrown (51) · parent frustration / temper (41)
- <b>Desire:</b> dry nights (211) · reassurance / not alone (110) · child's confidence / feel normal (85) · fast results (84; \~4 in 10 sampled rows mis-tagged) · go to sleepovers / camp (69) · ditch pull-ups (21) · child wakes on own (11) · keep the secret (8) · dry before camp (4) · money back (3)
- <b>Need:</b> something that actually wakes the child (172) · reliable sensor (123) · rule out a medical cause (59) · comfortable to wear (36) · vibration / quiet mode (35) · discreet option away from home (31) · reward chart in the box (31) · guidance on what works (26) · child can use it alone (24) · parent receiver (14)
- <b>Objection:</b> scam / no delivery / no support (50) · didn't wake the child (48) · doesn't work / waste of money (44) · price (40) · false alarms from sweat / skin (37) · battery / charging (36) · broke in days–weeks (36) · child refuses / takes it off (33) · too loud, wakes siblings (29) · takes weeks (24). (179 Saphire Trustpilot rows that never mention bedwetting are excluded; with them, trust = 147 and subscription = 81, almost all ADHD-gummy billing complaints. Subscription is now 12 and drops out of the top 10.)
- <b>Failed solution (used / mentioned):</b> pull-ups / GoodNites / DryNites (381) · bedwetting alarm (232) · doctor / clinic visits (180) · desmopressin / meds (113) · waiting it out (79) · alarm didn't work, said outright (61) · mattress protectors / pads (49) · therapy / OT / pelvic floor (36) · limiting fluids (36) · constipation treatment (33). Saffron gummies / supplements: <b>21 about bedwetting</b> (81 incl. Saphire ADHD/mood reviews) — it falls from #5 to #13.
- <b>Trigger:</b> school camp / trip coming up (113) · sleepover invite (111) · friend found out / teased (45) · child crying / says ashamed (37) · doctor said wait (33) · visiting relatives / holiday (32) · child turning 8+ and still wet (25) · sibling compared / got dry first (19) · outgrew pull-up sizes (12) · child asked for help (11)
- <b>Misconception (only 8 exist):</b> child is lazy / doing it on purpose (18) · always a sign of abuse / trauma (13) · night dryness can be potty-trained (8) · limiting fluids will fix it (2) · a supplement can stop it (1) · he'll grow out of it (1) · alarm is worn at sleepovers (1) · alarm only detects, doesn't train (1)
- <b>Belief:</b> it's very common / normal (111) · deep sleep is the cause (96) · genetic / runs in the family (79) · will grow out of it (72) · linked to ADHD / autism (52) · alarms work (37) · rough first weeks, must persist (35) · hormone not developed yet (26) · alarm trains the brain (23) · not the child's fault (14)
- <b>Emotional state:</b> frustration (171) · worry (139) · embarrassment (104) · desire (82) · relief (79) · hope (78) · fear (64) · shame (62) · helplessness (59) · anger (50). \[Saphire non-bedwetting rows removed; first draft: frustration 277 · worry 147 · anger 106.\]
- <b>Awareness stage:</b> product (903) · problem (611) · solution (381) · most aware (89) · unaware (4). Review rows default to "product". In the community rows by parents: solution 189 · problem 163 · product 46 · most 28 \[S12\]
- <b>Burned / skeptical:</b> no (1,754) · yes (234) \[Saphire non-bedwetting rows removed; first draft: yes 336\]
- <b>Authority:</b> doctor / GP (121) · pediatrician (70) · other parents / reviews (47) · urologist (32) · enuresis / bladder clinic (30) · book / program (26) · studies (26) · specialist (14) · nurse / school nurse (11) · grandparents (10)
- <b>Buyer group:</b> other / commenters (870) · parent, gender unknown (748) · mom (175) · adult who wet as a child (108) · dad (33) · teen writing about self (33) · grandparent (9) · adult bedwetter (6) · medical pro (6). \[First draft on full CORE: parent unknown 813 · mom 177 · dad 34 · grandparent 22.\]
- <b>Child age (parent rows):</b> not stated (485) · 8–12 (303) · 5–7 (127) · 13+ (39) · under 5 (11). By unique thread (one vote each, §20 V3): 8–12 = 151 of 300 (50%), 5–7 = 106 (35%) \[S10\]
- <b>Country visible:</b> not visible (1,019) · US (491) · UK (372) · AU (56 + 4 AU/NZ) · NL (17) · CA (5) · NZ (2) · others (22). \[First draft on full CORE: US 632 · UK 394 · AU 67 · CA 10 · NZ 3 — 141 of the removed Saphire rows were US.\]
- <b>Great phrase:</b> free text, too varied to tally. See the §14 swipe.

<b>So What → do this:</b> Build every list below from the CLEAN bank and quote it, not memory. Treat 8–12 and "social stage" numbers as ceilings (8–12 is 50% by thread, not 63%). The hardest numbers we have are the review-side <b>reliability</b> complaints — didn't wake (48), doesn't work (44), false alarms (37), battery (36), broke (36) — because they come with stars and dates. The "burned by online scams" story was mostly Saphire noise (trust 147 → 50).

---

# 3 · Ideal customer (ICP)

<b>Locked avatar (Nikita, 2026-11-16):</b> a mom of a child aged 8–12 who still wets the bed. We sell for the kid and market to her. The angle is the social stage: sleepovers, camp, friends finding out. Below, the data pressure-tests that avatar. It stays locked; the findings change how we speak to her.

## The one person

She's a mom, \[INFERENCE\] probably in her 30s–40s (no reliable self-stated ages in the bank), with two or three kids. Her 9-to-11-year-old has "never had a dry night" or is still wet most nights. She has asked the pediatrician every year and keeps hearing "he'll grow out of it." She has bought pull-ups for years. She may already have tried a cheap alarm that "didn't wake him." She's tired, not panicked, until a sleepover invite or a school-camp form lands. Then her child's fear becomes her deadline.

## Required fields (each with the number behind it)

- <b>Age range: \[INFERENCE\] 30s–40s.</b> No reliable self-stated mom ages in the bank. <b>Correction (§20 V3):</b> the first draft used three "I 34f / 39f / 40f" posts as evidence; all three are r/amiwrong posts from three accounts that share one template and look like troll posts, so they are excluded \[S3\].
  - <b>Best proxy (SimilarWeb):</b> the biggest seller on this exact pain, [trysaphire.com](http://trysaphire.com), has an audience that is <b>74.66% female</b>. By age: 18–24 8.19% · 25–34 23.91% · 35–44 20.71% · 45–54 23.67% · 55–64 14.95% · 65+ 8.58% \[S13\]. Caveat: that site also sells ADHD/mood gummies, so it is a proxy, not our buyer.
  - SimilarWeb shows "No Data to Display" for age and gender on [unikor.shop](http://unikor.shop) \[S14\] and on [goodnites.com](http://goodnites.com) \[S15\].
  - <b>\[INFERENCE\]</b> The exact age band beyond this proxy.
- <b>Gender: mostly moms (direction, not a census).</b> Gender is visible in only 211 of 1,046 parent rows (20%); there it is 177 moms vs 34 dads (84%), but most "mom" tags come from mum-only forums we chose to search (Mumsnet, r/Mommit, r/breakingmom). <b>Explicit in the text: 24 moms vs 9 dads (73%)</b> \[S16\]. Direction: mostly moms; size: not measurable from this bank. (On the clean bank: 175 moms vs 33 dads \[S2\].) Saphire's audience is 74.66% female \[S13\].
- <b>Life stage:</b> a married mom (or, less often, a single parent) with 2–4 kids, often more than one of whom wets. "All 4 of my children wet the bed, almost every night" \[S17\]. Sibling comparison or "got dry first" shows up as a trigger in <b>19</b> snippets \[S1\].
- <b>Household:</b> mostly two parents. A minority are single, step or co-parent households: <b>46</b> snippets \[S1\]. Example: "I am a single father… I am completely exhausted trying to handle everything on my own" \[S18\]. Bedwetting often runs in the family: <b>79</b> snippets \[S1\].
- <b>Income band: \[INFERENCE\] price-conscious middle.</b> <b>40</b> snippets object on price (51 before the Saphire cleanup), and money spent on pull-ups is a pain in <b>15</b> \[S1\]. "there's no way we can afford the really fancy ones" \[S19\]. "I almost purchased the Malem today, but \$99 is pretty steep" \[S20\]. No income figure exists in the data.
- <b>Job type: NOT FOUND.</b> Jobs are almost never stated. The only signals are a student mom aiming for a Bachelor's degree and a teen athlete's practice schedule \[S21\]. <b>\[INFERENCE\]</b> Working mom with little slack at night.
- <b>Country / urban-rural:</b>
  - Of snippets with a visible country (clean bank): <b>US 491 · UK 372 · AU 60 (incl. 4 AU/NZ) · CA 5 · NZ 2</b>; 1,019 not visible, mostly Reddit. (First draft: US 632 — 141 of the removed Saphire reviews were US.)
  - Parent rows only: US 242 · UK 177 · AU 37 (incl. 4 AU/NZ) · CA 2 · NZ 1 \[S2\].
  - <b>CA and NZ have almost no parent voice in the bank. Their copy will rest on US/UK/AU voice.</b>
  - Unikor's traffic is <b>59.48% US</b> (the page does not say desktop-only) \[S14\].
  - Urban vs rural: <b>NOT FOUND</b> (no signal) → \[INFERENCE\] suburban.
- <b>A typical day when the problem hits (night first):</b>
  - "I wrote this at 3:45am after a night time wake up" \[S22\]
  - "I have to wake him up at 1:00 am every morning to avoid another load of laundry" \[S23\]
  - "Now I'm doing laundry at 3 am" \[S24\]
  - The morning: "it breaks my heart when I wake him for school and he remembers then cries with frustration and shame that he can't stop this" \[S25\]
  - The counts behind it: parent sleep loss <b>68</b> · endless laundry <b>72</b> · child ashamed <b>171</b> \[S1\].

## The child's age reality (blunt)

- <b>The single most common age is 7.</b> By unique thread/review (one vote per thread), the peak is sharper than the first draft said: 5 (20) · 6 (31) · <b>7 (52)</b> · 8 (38) · 9 (39) · 10 (34) · 11 (33) · 12 (28) \[S10\]. Per row, long 9–11 threads add many rows: 5 (21) · 6 (35) · 7 (62) · 8 (50) · 9 (60) · 10 (58) · 11 (57) · 12 (51) \[S1\] (clean bank: 7 = 59 rows vs 9 = 60; by thread 7 = 49 vs 9 = 39 \[S2\]).
- <b>8–12 is still the biggest band, even after you allow for search bias.</b> 8–12 = 305 of 487 rows (63%), but <b>151 of 300 unique threads (50%)</b>; 5–7 = 106 threads (35%) \[S10\]. 182 of the 305 rows inherit the age from the thread opener \[S16\]. <b>Correction (§20 V3):</b> the first draft led with 63%; the fair figure is 50%. Agents B and D also searched "9/10/11 year old" on purpose, so even 50% is a ceiling \[S9\].
- <b>Among actual alarm BUYERS, 5–7 leads.</b> In the review bank (agent E, no age-targeted searching), parent reviews that state an age split <b>5–7: 43 vs 8–12: 34</b> \[S1\]. Agent E's own pass found 38 vs 28 \[S26\]. So, as a share of buyers, the alarm market leans younger than our avatar. In alarm reviews with an exact age (gummies / GoodNites / DDAVP excluded), <b>5–8-year-olds are 53 of 71 (75%); 9–12 only 16 (23%)</b> \[S10\].
- <b>The social stage is real but a minority, and it rises with age.</b> These are snippets that carry a sleepover, camp or friends label:
  - 8–12 parent rows: <b>68 of 305 (22%)</b>
  - 5–7: <b>11 of 130 (8%)</b>
  - 13+: <b>11 of 40 (28%)</b> \[S1\]
  - A wider regex on the quote text gives 25% / 17% / 35% \[S1\].
  - By unique thread, 53 of 151 8–12 threads (35%) mention the social stage. But the social labels mis-tag at \~40–50%, so the <b>first-hand social share is probably \~15–25%</b> \[INFERENCE from \[S16\]\].
  - Agent D's age-only searches (no social words in the query) found social mentions in <b>13 of 57</b> distinct parent posts (23%) \[S27\].

## Where the data cuts against the avatar (said plainly)

1. <b>Most of what 8–12 moms post is laundry, sleep, "is this normal" and the doctor.</b> Only about 1 in 4–5 of their posts is about the social stage. The social stage is the most <i>emotional</i> content (it's strongest in the kids' own voice), but it is not the most <i>frequent</i>.
2. <b>Many 8–12 moms are already burned on alarms.</b> "Bedwetting alarm (used)" appears in <b>232</b> snippets and "alarm didn't work (said outright)" in <b>61</b> \[S1\]. "We have tried alarms with no luck" \[S28\].
3. <b>For the sleepover itself, families use pull-ups, desmopressin or a word with the host, not an alarm.</b> The alarm is a home training tool; the social stage is the <b>motivation and the deadline</b>, not the use case. Belief tags: tell the host / camp staff <b>11</b>, pull-ups at camp / sleepovers <b>10</b>, desmopressin for overnights <b>9</b>, decline or limit <b>5</b> \[S1\]. "My son uses it on any overnight trips and its only failed once" \[S29\]. Zero bank rows show a family using an alarm <i>at</i> a sleepover \[S30\].
4. <b>The doctor is her top authority, and often the one who said "wait."</b> Doctor/GP <b>121</b> + pediatrician <b>71</b> \[S1\].
5. <b>The alarm buyer is younger than the avatar.</b> In alarm reviews with an exact age, 75% are 5–8 and 23% are 9–12 \[S10\]. The 8–12 mom is the biggest voice in the <i>conversation</i>; the 5–8 mom is the biggest voice at the <i>cash register</i>.
6. <b>The "burned online" story was mostly noise.</b> The first draft read trust (147) + subscription (81) as proof she has been scammed. With the off-topic Saphire reviews removed it is 50 + 12. Her real alarm worries are reliability: won't wake him (48), doesn't work (44), false alarms (37), battery (36), broke (36) \[S2\].
7. <b>The angle is not empty.</b> Saphire already tells the 9–10-year-old sleepover/camp story at scale \[S31\]. That is a Doc 1 finding, but it shapes her: she may have already seen "the alarm didn't work" told <i>to</i> her by gummy ads.

## Worldview (written as one of them)

- <b>Social:</b>
  - <i>(her voice, summary \[INFERENCE\]): It's not his fault and nobody should shame him.</i> It's very common (<b>111</b>) and not the child's fault (<b>14</b>) \[S1\].
  - "if shaming helped with bladder control, no kid would ever wet the bed" \[S32\].
  - She worries about how other kids will react: "He's at the age where these things are going to be fuel for being picked on and it worries me." \[S33\]
- <b>Economic:</b>
  - <i>(her voice, summary \[INFERENCE\]): I'm tired of paying for pull-ups every month, but I won't waste money on junk.</i> "I can't justify buying them month after month much anymore" \[S34\].
  - The trust and subscription objections are smaller than the first draft said (<b>trust 50, subscription 12</b> once off-topic Saphire ADHD reviews are removed; Unikor's own Trustpilot is 1.9 from 13) \[S2\]. She is wary, not scarred; her bigger worry is wasting money on a unit that doesn't work.
- <b>Religious: \[INFERENCE\] — not visible in parent posts.</b> The one prayer line in the bank is a child's: "When i go to a sleepover i always like PRAY TO GOD that this night is different" \[S35\]. → Keep copy secular.
- <b>Political: \[INFERENCE\] — no signal in the data.</b> → Keep copy apolitical.
- <b>Prejudices / eye-rolls (what she rolls her eyes at):</b>
  - <b>Relatives who blame:</b> "acording to my mother it's my fault" \[S36\] · "she is now saying if it doesn't stop everyone will be laughing at him" \[S37\].
  - <b>The "just wait" doctor:</b> "all anybody ever says is that everything's fine… So we just need to wait and I'm like how much longer?" \[S11\].
  - <b>The "lazy" theory</b> (<b>18</b> snippets; mostly kids accusing their families of holding it): "Everyone in my family keep calling me lazy" \[S35\].
  - <b>Products that over-promise:</b> "completely wasted my money stupidly trusted their reviews" \[S38\] (the review now carries an update: "They have now got back to me to send a refund.").
- <b>Who she thinks "gets it":</b>
  - <b>Other parents who've been there</b> (other parents / reviews <b>47</b>; 64 before the Saphire cleanup).
  - <b>Adults who wet as kids</b> (<b>108</b> snippets). "I wet the bed until I was 14 and it stopped when I got my first period" \[S39\].
  - <b>A doctor who finally helps:</b> "We switched pediatricians because it didn't seem like our old one was addressing this problem" \[S40\].

<b>Her core view of life, love & family (1–3 sentences, in her voice — \[INFERENCE\] summary built on the quotes that follow):</b> My kid is healthy, kind and normal. He just can't wake up yet, and I will not let a body thing he can't control take away the sleepovers and trips every other kid gets. I'm done being told to wait; I want something that actually works, and I want him to never feel like the odd one out. Anchors: "I want him to go do things, but he just can't control it." \[S23\] · "the peace from finally having something parenting related that actually works" \[S41\]

## §20 verdict on the avatar (V3, said plainly)

Source for this block: \[S3\].

- <b>"Moms" holds directionally.</b> Where gender is visible, 73–90% of parents are moms, and Saphire's audience is 74.66% female (confirmed live). But gender is visible in only 1 in 5 parent rows, mostly because we searched mum forums. Don't quote "84%" as a market fact.
- <b>"8–12" holds for the conversation, not the cash register.</b> In community threads 8–12 is the biggest band at \~50% of age-stated threads (not 63%). Among people who bought and reviewed an alarm, 75% of stated ages are 5–8 and only 23% are 9–12. Age 7 is the single most common age by thread (52 vs 39 for age 9). The first draft stated the 7-peak but understated how young the buyer is.
- <b>The social stage is real and rises with age, but it is a minority motive.</b> \~22% of 8–12 parent rows, \~35% of 8–12 threads, and probably 15–25% first-hand once mis-tags are allowed for. It is the strongest emotion, not the most common reason.
- <b>The trust / subscription "burned online" story is mostly Saphire noise</b> (147 + 81 → 50 + 12). Her real alarm anxieties are "won't wake him" (48), "doesn't work" (44), false alarms (37), battery (36) and broke (36).
- <b>Decision (Nikita's lock stands):</b> keep the locked avatar, moms of 8–12. The social stage is the <b>creative world and the motivation</b> (a dated deadline), not the use case. <b>Cast and target \~7–10</b> so the 5–8 buyer core isn't shut out. <b>Lead objection handling with "it actually wakes him and keeps working,"</b> not with "we're not a scam." Re-test the age split from Meta breakdowns after the first spend.

## What this means for the ads (keep the avatar, adjust the aim)

- <b>Keep 8–12 + the social stage as the creative world.</b> It's the most emotional slice. In the 8–12 rows it is \~3× more frequent than in the 5–7 rows (22% vs 8%).
- <b>Make the dated event the hook, and the alarm the home plan before it.</b> "Camp is in 8 weeks — start tonight." Never imply he wears it at the sleepover.
- <b>Open on a burned mom, not a naïve one.</b> "If the last alarm didn't wake him…" Back it with the parent-receiver story. This is objection #2 by count (48) and the main failure parents describe in communities.
- <b>Cast and target \~7–10, not 10–12.</b> 7 is the single most common age by thread, and 75% of alarm reviewers with a stated age have a 5–8-year-old. A 7–10 cast keeps the sleepover story believable without shutting out the biggest buyer group.
- <b>Say "pediatricians recommend alarms first,"</b> not "your doctor is wrong." She trusts her doctor.

<b>So What → do this:</b> Launch to the locked avatar (mom of an 8–12-year-old), but cast and target the child at \~7–10. Write every hook around a dated social moment as the <i>reason to start now</i>, and lead the proof with "it actually wakes him and keeps working" (receiver in her room, sensor that doesn't false-alarm, battery that lasts the night) — not with anti-scam lines. Demographic fields are proxies: Saphire's audience is 75% female and 25–54 heavy, but it is mostly ADHD/mood gummy buyers. Re-check age and gender in Meta's breakdowns after the first spend.

---

# 3A · Sub-avatars (the scale targets)

Ranked by how many §2C snippets come from each group. Counts \[S1\].

## 1. Moms of 5–7-year-olds (the younger, "laundry" mom)

- <b>Size:</b> <b>130</b> parent snippets from <b>98</b> threads/URLs (127 rows on the clean bank; 106 threads by the V3 thread key). Among actual alarm buyers in reviews she <i>leads</i> (43 vs 34 for 8–12), and by exact age 5–8-year-olds are 75% of alarm reviewers \[S10\]. <b>She is the cash-register buyer;</b> a \~7–10 cast in the main ad set already speaks to her older half.
- <b>#1 pain in her words:</b> night changes and laundry. "sometimes he is wet already and I have to change him and his whole bedding (he sleeps in a full size bed) in the middle of the night" \[S42\]
- <b>Where she gathers:</b> r/Parenting, r/Mommit, r/UKParenting, r/pottytraining, Amazon/Walmart alarm reviews.
- <b>Angle that opens her:</b> "Start now, before the sleepover years." Same product, an earlier deadline. <b>Caution: this is Unikor's lane</b> ("Mom, why can't I stop?" with a 7-year-old) \[S43\].

## 2. Parents of kids with ADHD / autism

- <b>Size:</b> <b>68</b> parent snippets from <b>45</b> threads/URLs (44 rows / 34 threads name ADHD or autism in the quote itself; the rest inherit it from r/ADHDparenting). <b>Correction (§20 V3):</b> the first draft said 84 / 62; 16 of those were Saphire ADHD-gummy reviews with no bedwetting content \[S3\]. ADHD/autism is also a belief in <b>52</b> snippets.
- <b>Anxiety is her extra layer.</b> Anxiety / stress shows up in <b>80</b> rows (38 parents): stress-triggered relapse, and the fear that an alarm will frighten an anxious child \[S3\].
- <b>#1 pain:</b> "VERY deep sleeper" plus a doctor who shrugs. "His Dr. does not seem concerned, she said that it is normal for kids with adhd to not develop the hormone at the same age neurotypical kids do" \[S44\]
- <b>Where they gather:</b> r/ADHDparenting, r/ParentingADHD, r/Autism\_Parenting, IEP/special-needs Facebook groups \[S45\].
- <b>Angle:</b> the deep sleeper whose "brain is so busy." "His doctor told me his brain is so busy during the day with the adhd…" \[S45\]. Use a vibration mode, keep it calm, and never call it a buzzer.
- <b>Warning:</b> these families report alarms failing more often. "bedwetting alarms don't work because he has severe anxiety" \[S46\]. Saphire and VigorNatura already target this group \[S31\].

## 3. Parents of teens 13+ (and the teens themselves)

- <b>Size:</b> <b>40</b> parent snippets (33 threads) + <b>33</b> teen self-voice snippets (14 threads). This group has the sharpest social pain (28–35% social).
- <b>#1 pain:</b> "I don't want him wetting the bed until he's 17 years old." \[S47\]. The teen's version: "I just want it to stop so I can be a normal teen and not the outcast of the house who pisses the bed." \[S48\]
- <b>Where they gather:</b> r/Incontinence, r/bedwetting, r/AdultBedwetting, r/Parenting; teens in YouTube comment sections \[S49\].
- <b>Angle:</b> "before high school / before the 8th-grade trip." Privacy and the teen's own control. Market to the parent only (Meta minors rules — see Doc 4 compliance).

## 4. Dads, including single and divorced fathers

- <b>Size:</b> <b>34</b> snippets from <b>20</b> threads (33 on the clean bank). Only 9 dads say so explicitly in the text \[S16\]. Small, but owned by no one: only 4 "dad voice" ad copies were found \[S31\].
- <b>#1 pain:</b> sleep and being alone with it. "I haven't had a full night's rest in years" \[S22\] · "I am completely exhausted trying to handle everything on my own" \[S18\]
- <b>Where they gather:</b> r/daddit ("Bedwetting - at my wits end.", 103 comments), r/Parenting \[S9\].
- <b>Angle:</b> "Dad who wet the bed too: break the cycle without shame." Practical, kit-and-steps tone.

## 5. Step-parents, co-parents, foster/kinship carers

- <b>Size:</b> <b>46</b> snippets from <b>40</b> URLs. The regex catches some aunts and older siblings too, so this group is <b>noisy</b>.
- <b>#1 pain:</b> cost and two houses. "My step son is 12 years old and has been peeing the bed consistently since I've known him ... Washing and drying bedding is just not sustainable financially." \[S50\] · "Considering adoptive placement for a teen with a bedwetting issue." \[S51\]
- <b>Where they gather:</b> r/stepparents (not searched — gap), r/Fosterparents, r/Parenting.
- <b>Angle:</b> "Same routine in both homes." The kit is small and travels between houses. For foster care, trauma-informed copy, doctor first.

<b>Too thin to target:</b> grandparents. There were 22 snippets, but 13 were Saphire gummy reviews with no bedwetting content and are now excluded, leaving <b>9</b> \[S2\]; in posts they show up as the <i>trigger</i> ("everyone will be laughing at him"), not the buyer.

<b>So What → do this:</b> The \~7–10 cast in the launch set already reaches the older half of the 5–8 buyer core. Scale order after launch: <b>(1) moms of 5–7</b> (biggest buyer group, but Unikor's lane: a separate "start before the sleepover years" ad set) → <b>(2) ADHD/autism parents</b> (vibration + calm, ADHD-interest targeting) → <b>(3) parents of teens</b> (privacy, "before high school") → <b>(4) dads</b> (open voice) → <b>(5) step / co-parent</b> (two-home kit).

---

# 10 · Everything about the ICP

Every list below is every distinct item in the bank, ranked by CLEAN verified count (CORE minus the 179 off-topic Saphire rows); parent-row counts are shown as "parents n." All counts \[S2\]. Where a count moved, the first-draft figure is in brackets. §10B (failed solutions) and §11 (objections, Doc 3) go deeper and refer back to these by name.

## Pains (21 distinct)

1. <b>Child ashamed / embarrassed (171; parents 71).</b> "He told me a few days ago that even though I have never "shamed him" ever, that he feels very ashamed. Sad mom here who is out of ideas." \[S52\]
2. <b>Can't go to sleepovers (108; parents 53).</b> "He threw the card in the trash… He said because he is scared he will pee the bed, and that broke my heart." \[S23\]
3. <b>Camp / school-trip fear (100; parents 42).</b> "12 yo turns to me and just says "mom I wet the bed" and I realized that if he's still wetting at night he can't go. It would be social suicide." \[S11\]
4. <b>Wets every night / several times a night (77; parents 49).</b> "My 9 yo son has wet nights every single night. He has never had a dry night." \[S53\]
5. <b>Endless laundry (72; parents 47).</b> "All 4 of my children wet the bed, almost every night. I am exhausted of washing laundry all day." \[S17\]
6. <b>Fear of friends finding out / teasing (70; parents 36).</b> "we (and him) are scared that if his friends find out he wears pull-ups to bed.. they are going to make fun of him." \[S54\]
7. <b>Parent sleep loss / night wakings (68; parents 34).</b> "I haven't had a full night's rest in years" \[S22\]
8. <b>Deep sleeper, can't wake (56; parents 36).</b> "he sleeps like the dead, and at home I have to physically pull him up and out of bed and walk him to the toilet while he's deliriously asleep." \[S55\]
9. <b>Pull-ups leak / outgrown (51; parents 23).</b> "They are soaked each morning, like so full and heavy its like a brick." \[S25\] · "pull-ups are no longer available for her size" \[S56\]
10. <b>Parent frustration / temper (41; parents 22).</b> "I just yelled at two of my kids for wetting the bed. I feel so bad" \[S57\]
11. <b>Hiding wet sheets / pull-ups (37; parents 19).</b> "When I moved his bed, I found a stash of urine soaked nighttime pull-ups!" \[S58\] (r/AmIOverreacting is an AITA-style sub — low credibility, §20 V3)
12. <b>Years of struggle / no end in sight (36; parents 29) \[37\].</b> "My son is twelve and wets the bed constantly. I thought it would start to slow down by now, but there doesn't seem to be an end in sight." \[S59\]
13. <b>Child's self-esteem / feels limited (33; parents 9).</b> "I struggle watching the kid feel limited in what he can do" \[S60\]
14. <b>Child punished / shamed by family (29; parents 11).</b> "acording to my mother it's my fault as I've left him in pull ups" \[S36\]
15. <b>Smell (21; parents 16).</b> "there was still a strong urine smell in his room and I couldn't figure out why" \[S58\]
16. <b>Money wasted on pull-ups / products (15; parents 9).</b> "Washing and drying bedding is just not sustainable financially." \[S50\]
17. <b>Child cried / scared by the alarm (13; parents 11).</b> "First 3 weeks, the alarm would scare my son to death, almost like night terrors." \[S61\]
18. <b>Never had a dry night (8; parents 8).</b> "My son is 12 and has never had a dry night. His pediatrician isn't worried." \[S45\]
19. <b>Doctor said wait (8; parents 8).</b> "our pediatrician has repeatedly assured us that she's not concerned, he'll grow out of it eventually-- etc etc." \[S62\]
20. <b>Relapse after being dry (6; parents 4).</b> "was dry the last 2.5 years after using Oopsie Hero alarm to night train. After a recent illness has wet the bed 95% of the time for the last couple months." \[S17\]
21. <b>Sibling comparison (2; parents 2).</b> "DS10 is feeling very jealous and ashamed to be outpaced by his little brother." \[S63\]

## Objections (25 distinct — §11 in Doc 3 answers each)

Ranked on the CLEAN bank. <b>Correction (§20 V3):</b> the first draft ranked trust (147) and subscription (81) as #1 and #2; 102 and 75 of those rows were Saphire ADHD / mood / billing reviews that never mention bedwetting. Trust is still #1, but only just (50 vs 48), and subscription falls to #17 \[S2\] \[S3\].

1. <b>Scam / no delivery / no support (50 after removing 102 Saphire reviews unrelated to bedwetting; 147 raw; parents 25).</b> 38 rows are about alarm sellers. "I never received the unit" \[S64\]
2. <b>Didn't wake the child; the parent woke instead (48; parents 27).</b> "He never woke up so we had to wake him" \[S65\]
3. <b>Doesn't work / waste of money (44; parents 23) \[60\].</b> "Faulty item doesn't work at all - completely wasted my money stupidly trusted their reviews." \[S38\] (update on the review: "They have now got back to me to send a refund." — so it is weaker "no support" evidence than it looked)
4. <b>Price / too expensive (40; parents 17) \[51\].</b> "This was expensive but only worked correctly for two weeks" \[S66\]
5. <b>False alarms from sweat / skin (37; parents 22).</b> "As soon as this touched my sons skin it would go off." \[S67\]
6. <b>Battery / charging (36; parents 14).</b> "We learned we needed to charge it every day so it would last through the night." \[S68\]
7. <b>Broke in days to weeks (36; parents 11) \[38\].</b> "Only lasts about a month. Bought 2 and both broke" \[S67\]
8. <b>Child refuses / takes it off (33; parents 18) \[44\].</b> "he hates it and is becoming less and less cooperative using it." \[S63\]
9. <b>Too loud, wakes siblings / the whole house (29; parents 15).</b> "But is very loud. No way to turn it down if the child shares a room" \[S69\]
10. <b>Takes weeks / brutal first weeks (24; parents 21) \[27\].</b> "Therapee needs commitment the first 2 weeks were like having a new born baby again" \[S70\]
11. <b>Sensor missed the wee or went off too late (21; parents 14) \[23\].</b> "the alarm would sound between 3 and 8 minutes AFTER the bedwetting occurred" \[S71\]
12. <b>Clip hard to attach / falls off (20; parents 8).</b> "It also came undone at night" \[S72\]
13. <b>Confusing instructions (16; parents 9) \[18\].</b> "instructions were clearly poorly translated to English, connection is subpar." \[S68\]
14. <b>Receiver range / connection drops (14; parents 10).</b> "the alarm has only sounded 3 of those times. We've tried pairing it every night before bed" \[S73\]
15. <b>Ruins sleep / school next day (12; parents 5).</b> "I worry school work could drop a little if she is up in the middle of the night most nights?" \[S74\]
16. <b>Child too young / body not ready (12; parents 3).</b> "this is perfectly developmentally normal even if annoying." \[S75\] (Weak fit, §20 V3: this is a commenter's reassurance, not a buyer's objection.)
17. <b>Subscription trap (12 bedwetting-relevant; 81 raw, 75 Saphire; parents 7).</b> "Made from China & unauthorized auto-subscription" \[S76\]
18. <b>Hard to turn off at 2 a.m. (10; parents 4).</b> "the beeping wouldn't stop whether the cable was in or not. Hard to focus when half asleep." \[S77\]
19. <b>Not loud enough (7; parents 5).</b> "This product is not loud enough to wake up my child...." \[S78\]
20. <b>Alarm = punishment / scares an anxious child (6; parents 5).</b> "Please don't do this. My parents used this on me and it gave me such anxiety I couldn't sleep properly for years." \[S79\] Thread title: "Bed wetting alarms - is this punishment?" (105 comments) \[S80\]
21. <b>Away-from-home discretion (5; parents 5).</b> "Do I use this alarm at sleepovers and with my roommate in college" \[S81\]
22. <b>Medication worries (3; parents 3).</b> "He said we could try medication for a sleepover… Don't really want to medicate him ." \[S82\]
23. <b>Gummies aren't a bedwetting product (1; parents 1) \[2\].</b> "not one of them helps with kids bed wetting" \[S83\]
24. <b>Is it worth it, or should we just wait? (1 tagged; the "wait" belief has 72).</b> "should have listened to my pediatrician and waited for him to outgrow it." \[S84\]
25. <b>Relapse after the alarm (1).</b> "He was dry for 2 or 3 weeks. But then he ..." \[S85\]

## Needs (13 distinct)

1. <b>Something that actually wakes the child (172; parents 94).</b> "the alarm is obnoxious, loud enough to wake our deep sleeper." \[S86\]
2. <b>A reliable sensor that catches the first drops and doesn't false-alarm (123; parents 62).</b> "we have been through a few bedwetting alarms on Amazon, but unfortunately they all seem to be not that sensitive? It seems like when he goes, he empties out almost entirely before the alarm starts." \[S87\]
3. <b>Rule out a medical cause first (59; parents 22).</b> "our family has a wonderful doctor who is aware of everything and helping rule out medical causes." \[S17\]
4. <b>Comfortable to wear (36; parents 24).</b> "the transmitter/sensor has no cables, is easy to use and comfortable for her to wear" \[S88\]
5. <b>Vibration / quiet mode for shared rooms (35; parents 24).</b> "Alarm is very loud and scared my 8 yo son! Now he just uses it on vibrate." \[S89\]
6. <b>A discreet option for away from home (31; parents 15).</b> "She wears a pull up at home, but it would be too obvious at a friend's house." \[S90\]
7. <b>A reward chart in the box (31; parents 22).</b> "When he put the 7th dry morning sticker in a row on his chart he said, "Mom, I'm cured!"" \[S91\]
8. <b>Guidance on what actually works (26; parents 18).</b> "what are some aids that I can use to help him wake up at night. He is a VERY deep sleeper." \[S44\]
9. <b>Something the child can run on his own (24; parents 18).</b> "very straightforward and easy for a child to do by themselves" \[S73\]
10. <b>A parent receiver, so she hears it from her room (14; parents 10).</b> "Sure woke me up down the hall EVERY NIGHT, which is also the point." \[S92\]
11. <b>A seller who answers and honours the guarantee (4; parents 4).</b> "they offer a 60 day money back which is why I have brought this product… contacted them on 6 occasions… no response" \[S38\]
12. <b>Wireless / easy setup (3; parents 3).</b> "It is wireless so it's easy to use" \[S86\]
13. <b>Works with a pull-up over the underwear (1).</b> "We wanted extra protection just in case and put a pull-up over her underwear" \[S93\]

## Core desires / dream outcome (14 distinct — §10A ladders each)

1. <b>Dry nights (211; parents 121).</b> "However this week we are currently on 6 CONSECUTIVE DRY NIGHTS! We haven't had one dry night before let alone 6 in a row." \[S94\]
2. <b>Reassurance / not alone (110; parents 47).</b> "Are we the only ones out there going through this?" \[S59\]
3. <b>Child's confidence / feeling normal (85; parents 48) \[87\].</b> "It affects her confidence and she feels like she has this embarrassing secret" \[S95\]
4. <b>Fast results (84; parents 47) \[93; \~4 in 10 sampled rows are mis-tagged — e.g. "after 3 weeks the sensor stopped working"\].</b> "Worked in just three nights for my 11 year old daughter! Worth every penny." \[S96\]
5. <b>Go to sleepovers / camp like other kids (69; parents 38).</b> "My 9 year old was desperate to be dry at night and have sleepovers and thanks to the Chummie alarm, he now can." \[S97\]
6. <b>Ditch pull-ups (21; parents 15).</b> "My 7.5 year old has wanted to get out of pull-ups for 2 years." \[S97\] (The first draft quoted an r/amiwrong template post here; replaced, §20 V3.)
7. <b>Child wakes on his own to pee (11; parents 9).</b> "All my problems are solved now he wakes up on his own and goes potty. A thrilling moment as a parent." \[S98\]
8. <b>Keep the secret (8; parents 7).</b> "He is always worried someone is going to find out." \[S99\]
9. <b>Dry before camp, a deadline (4; parents 4).</b> "He wants to do a summer camp in July… and I'd love to be able to help him before then if possible." \[S100\]
10. <b>Money back (3; parents 3).</b> "just get a refund, then all correspondence stopped cold." \[S38\]
11. <b>A full night of sleep for the family (3; parents 1).</b> "Not sure what was more satisfying— the sleep I got after or the peace from finally having something parenting related that actually works." \[S41\]
12. <b>A normal childhood / normal teen (2).</b> "I just want it to stop so I can be a normal teen" \[S48\]
13. <b>Be a good parent (2; parents 2).</b> "I feel like a bad mom that he stinks and his room stinks" \[S46\]
14. <b>Stop the laundry (1; parents 1).</b> "I'm so ready to stop doing laundry practically everyday!" \[S20\]

<b>Dream outcome, in one line from the data:</b> dry every morning, a proud kid who says "Mom, I'm cured!", and a yes to the sleepover, without another year of waiting. "He is so happy because he can now have friends come for sleepovers." \[S101\]

## Misconceptions (8 tagged + 3 held as "beliefs" that the science contradicts — rebuttals in Doc 3 §13)

1. <b>Child is lazy / doing it on purpose (18; parents 5).</b> "I half wonder if they're being lazy - have no incentive to get up and go to the toilet!" (a UK dad) \[S102\]
2. <b>It's always a sign of abuse / trauma (13; parents 0).</b> These are commenters, not her, quoting a Scouts brochure: "Reports nightmares or bedwetting" \[S103\]
3. <b>Night dryness can be potty-trained / he needs to feel wet (8; parents 6).</b> "All my parent friends… told me wife and I that he needed to feel pee in order for his body to wake up." \[S22\]
4. <b>Limiting fluids will fix it (2; parents 2).</b> "She said to just limit his drinking before bedtime, and to also wake him up once" \[S104\]. Limiting fluids also shows up as something tried (36).
5. <b>A supplement can stop it (1).</b> "the vitamin D and saffron supports the brain-bladder connection" \[S105\]
6. <b>He'll grow out of it (1 tagged; held as a belief in 72).</b> "I called a doctor and he said that he should grow out of it by 17." \[S47\]
7. <b>The alarm is worn at sleepovers (1)</b> and 8. <b>the alarm only detects, it doesn't train (1).</b> Both come from the same 11-year-old's questions: "if I use an alarm to detect wetness then isn't that already too late?" \[S81\]
8. <b>(Belief) "Deep sleeper, so nothing will work" (deep sleep is the cause: 96).</b> "I'm such a deep sleeper that I literally sleep through them, so they never really helped." \[S106\]
9. <b>(Belief) "Pull-ups are fine, leave it" (8).</b> Agent B classed this as the opposite camp to "pull-ups enable it" \[S9\].
10. <b>(Belief) "It's the parent's fault" (3).</b> Mostly relatives blaming the mom; see pain #14.

## Mindset / psychographics

<b>Beliefs she holds (22 distinct):</b>

- it's very common / normal (111; parents 44)
- deep sleep is the cause (96; 63)
- genetic / runs in the family (79; 22)
- will grow out of it (72; 32) — incl. the sub-belief <b>"it stops at puberty"</b> (26 rows; 11 parents, §20 V3 sweep), often a doctor script ("grow out of it by 17")
- linked to ADHD / autism (52; 34)
- alarms work / are the proven fix (37; 30)
- rough first weeks, must persist (35; 19)
- hormone not developed yet (26; 14)
- alarm trains the brain (23; 17)
- not the child's fault (14; 7)
- small bladder (11; 5)
- away from home: tell the host / camp staff (11; 7)
- away from home: pull-ups at camp / sleepovers (10; 9)
- desmopressin for overnights (9; 7)
- pull-ups are fine, don't shame (8; 6)
- away from home: decline / limit / stay up all night (5; 4)
- it's the parent's fault (3)
- kids are dry away from home (3)
- kids today are kinder (2)
- I must be the only one (1)
- a cheap alarm is enough (1)
- the child isn't bothered (1)

Best quote: "Enuresis runs in the family. I wet the bed later than I should have but I stopped. He will too." \[S107\]

<b>Emotional states (17 distinct; parents n):</b> frustration (171; 91) · worry (139; 83) · embarrassment (104; 34) · desire (82; 39) · relief (79; 56) · hope (78; 43) · fear (64; 23) · shame (62; 23) · helplessness (59; 36) · anger (50; 28) · pride (38; 24) · grief (34; 15) · exhaustion (32; 27) · guilt (20; 12) · apathy (12; 10) · skepticism (1) · love (1). <b>Correction (§20 V3):</b> the first draft had frustration 277 and anger 106 (#3); most of that anger was Saphire billing reviews. Anger drops to #10.

- <b>Anxiety / stress (not a tag; §20 V3 regex sweep): 80 rows, 38 parents.</b> Two shapes: stress-triggered relapse, and the fear that an alarm will frighten an anxious child \[S3\].
- <b>The frame she lives in:</b> worried, tired, not alarmed. "Currently we are very apathetic about the issue, believing it will resolve over time, so we just use bedtime pull-ups and normalise it" \[S74\]
- <b>Awareness:</b> most parents are already <b>solution-aware</b> (community parent rows: solution 189 · problem 163 · product 46 · most 28) \[S12\].
- <b>Burned:</b> 234 of 1,988 clean snippets are burned or skeptical (first draft: 336 of 2,167, inflated by Saphire billing reviews) \[S2\].

## Key experiences & moments

- <b>The 3 a.m. sheet change:</b> "a sheet, a mattress protector, a sheet, a mattress protector and the pee STILL gets through every single layer and onto the mattress" \[S108\]
- <b>The binned invite:</b> "He threw the card in the trash" \[S23\]
- <b>The trip conversation at dinner:</b> "mom I wet the bed" \[S11\]
- <b>Finding the stash under the bed:</b> "I found a stash of urine soaked nighttime pull-ups!" \[S58\]
- <b>The relative who sees the Goodnites:</b> "she asked me to hide her goodnites somewhere else so nobody would see them" \[S109\] ⚠ <b>Low credibility (§20 V3):</b> r/amiwrong template post (the same "I 3xf and my husband 3xm" opener on three accounts; a top comment calls it a troll post). Do not use in creative.
- <b>The camp cabin:</b> "a very 'visible' nighttime accident that was discovered by the entire cabin right as he was waking up" \[S110\]
- <b>Alarm night one:</b> "Well, holy crap this is hard… so I abandoned ship and put him back in diapers." \[S53\]
- <b>The win:</b> "I can see how proud he is to wake up every day and tell me he's dry" \[S94\]

## Failed solutions

Ranked in §10B, by name: pull-ups · alarms · doctor visits · desmopressin · gummies · waiting · bed pads · therapy/OT · limiting fluids · constipation treatment · lifting/waking · pee before bed · sleep study/tonsils · punishment · reward charts · chiropractor.

## Past victories + failures

<b>Where she's WON (even briefly) — what she already believes works:</b>

- <b>Alarms that clicked — in reviews.</b> 339 "works" reviews against 116 "failed" (71% of reviews that state an outcome; star-based, ≥4★ = works). <b>In parent communities it's closer to a coin flip</b> (\~28 works vs \~35 fails, hand-read regex hits; "slept through it" is the main failure) \[S111\]. Median <b>3 weeks</b> to dry \[S7\]. "In a week he was wetting less. By the time of the trip he was dry the whole time. Cost around £70 but a miracle." \[S25\]
- <b>Desmopressin for a night:</b> "it was like a miracle drug. My child woke up nearly every morning dry." Then: "We thought the problem was solved. Nope." \[S40\]
- <b>Motivation alone (brief):</b> "When she was motivated after years of struggling with it—she stopped no problem. In 6 months she was dry" (then relapsed) \[S112\]
- <b>Pull-ups as peace:</b> "I prefer a happy kiddo than one who feels bad about themselves" \[S113\]

<b>Where she FAILED (non-product let-downs only; product failures are in §10B):</b>

- <b>Doctor visits that ended in "wait"</b> (doctor visits 180; doctor said wait 33 as a trigger). "Then from 9 on it's been an exclamation of concern and no offer of advice or help." \[S56\]
- <b>Limiting fluids (36):</b> "We tried limiting liquids before bedtime, but nothing seems to work." \[S18\]
- <b>Lifting / waking at night (30):</b> "I have to wake him up at 1:00 am every morning to avoid another load of laundry." \[S23\]
- <b>Therapy / OT / pelvic floor (36):</b> "I tried OT. Didn't help." \[S45\]
- <b>Constipation clean-outs (33):</b> "Her doctor kept insisting that it was constipation and to do frequent "flush outs"" \[S114\]
- <b>Punishment / chores (19):</b> "I have made her start stripping her own bed at home" \[S115\]

## Goals — near + far

- <b>Near (this week or month), the click:</b>
  - Fewer wet sheets and one full night's sleep (sleep loss 68, laundry 72).
  - A first dry night or a streak (desires: dry nights 211, fast results 84).
  - "Survive" the next sleepover or camp. "I'd love to be able to help him before then if possible." \[S100\]
- <b>Far (the identity sale):</b>
  - A confident kid who does sleepovers, camps and trips without a plan to hide (confidence 85, sleepovers/camp 69).
  - A mom who "finally" fixed it instead of waiting. "Wish I had done it sooner." \[S116\]

## The 4 forces (she switches only when Push + Pull beat Anxiety + Habit)

- <b>Push (away from now):</b>
  - Laundry (72), sleep loss (68), the child's shame (171), the binned invite or trip (108 + 100).
  - "how much longer?" \[S11\]
- <b>Pull (toward new):</b>
  - Dry nights (211), a fast win (84), a proud kid (85), a yes to sleepovers (69).
  - "He's been dry ever since… it's meant he can do things like Beavers camps without feeling awkwardness or embarrassment. Was worth every penny." \[S117\]
- <b>Anxiety (about the new thing) → answer in §11:</b>
  - <b>#1: Will it actually wake him, and will it work at all (didn't wake 48, doesn't work 44)?</b>
  - <b>#2: Will it keep working — no false alarms, no breaking, no daily charging (37 / 36 / 36)?</b>
  - Is it a scam, will it arrive, will they refund (trust 50, subscription 12 once off-topic Saphire ADHD reviews are removed; first draft 147 + 81)?
  - Will it scare him or wake his brother (punishment 6, too loud 29)?
  - Will I survive the first weeks (24)?
- <b>Habit (what keeps her stuck):</b>
  - Pull-ups work as containment (381 mentions).
  - The doctor said wait (wait belief 72).
  - "It's common" (111).
  - Sunk cost of an alarm that already failed (61).
  - "we are very apathetic about the issue" \[S74\]

<b>So What → do this:</b>

- Every ad needs one Push from the top 6 pains and one Pull from the top 5 desires.
- Every landing page must kill the top anxieties on screen, <b>in this order</b>: (1) "it actually wakes him" — the "slept through it" story answered by the parent receiver; (2) "it keeps working" — a sensor that doesn't false-alarm, a battery that lasts the night, a unit that doesn't break (only claims a sample has proved); (3) an honest "first 1–3 weeks are hard"; then (4) a real support promise and a one-time payment as reassurance, not the lead.
- Pull-ups and "wait" are the habits to break. Frame both as "a patch, not a fix."

---

# 10A · Desire Ladder (surface → core)

Each rung is a §2C quote (with its count) or is marked \[INFERENCE\]. Counts \[S2\].

## Full map — her surface desires

1. <b>Dry nights (211)</b> → why? "Now I'm doing laundry at 3 am" (laundry 72) \[S24\] → why? her own sleep and sanity: "my sleep is ruined" (sleep loss 68) \[S52\] → why? years of "wait" with nothing that works: "the peace from finally having something parenting related that actually works" \[S41\] → <b>CORE: CONTROL / CERTAINTY</b> (secondary: time).
2. <b>Reassurance / not alone (110)</b> → why? "Are we the only ones out there going through this?" \[S59\] → why? to know her child is healthy and it's not her fault: "it's such a taboo subject" \[S74\] → <b>CORE: SECURITY / PEACE OF MIND</b> (secondary: belonging, for the mom herself).
3. <b>Fast results (84)</b> → why? "So we just need to wait and I'm like how much longer?" \[S11\] → why? the clock is running toward camp and high school (years of struggle 37) → <b>CORE: TIME</b> (secondary: control).
4. <b>Child's confidence / feel normal (85)</b> → why? "It's getting harder to keep his confidence up as he gets older." \[S118\] → why? so he isn't limited: "I struggle watching the kid feel limited" \[S60\] → why? so it doesn't mark him for years: "I literally got teased all the way to the end of high school" (a dad, recalling) \[S119\] → <b>CORE: LOVE / PROTECTING HIS SELF-WORTH</b>.
5. <b>Go to sleepovers / camp (69)</b> → why? "particularly because a friend of his was going" \[S110\] → why? not to be left out: "I feel really sad at the thought of DS missing out on the trip" \[S120\] → <b>CORE: BELONGING (the child's)</b>.
6. <b>Ditch pull-ups (21)</b> → why? not be the baby: "I know it makes him feel like a baby sometimes" \[S121\] → why? the sibling who got there first: "I'm worried seeing his younger brother be able to stop wearing pull-ups before him ... may make him resentful or jealous" \[S122\] (replaces an r/amiwrong template post, §20 V3) → <b>CORE: STATUS / GROWING-UP IDENTITY (the child's)</b>.
7. <b>Child wakes on his own (11)</b> → why? "All my problems are solved now he wakes up on his own" \[S98\] → why? the kid runs his own night \[INFERENCE\] → <b>CORE: AUTONOMY (the child's)</b>.
8. <b>Keep the secret (8)</b> → why? "He is always worried someone is going to find out." \[S99\] → why? "he HATED having to ask an adult for help, hated it much more than the being wet itself" \[S123\] → <b>CORE: STATUS + AUTONOMY (the child's)</b>.
9. <b>Dry before camp (4)</b> → why? "I'd love to be able to help him before then" \[S100\] → why? belonging, the same as #5 → <b>CORE: BELONGING</b>.
10. <b>Money back (3)</b> → why? "completely wasted my money stupidly trusted their reviews" \[S38\] (this reviewer later got a refund offer) → <b>CORE: SECURITY (money / not being fooled)</b>.
11. <b>Full night of sleep (3)</b> → why? the same rung as #1 ("the sleep I got after") → <b>CORE: TIME</b>.
12. <b>Normal childhood / normal teen (2)</b> → why? "not the outcast of the house who pisses the bed" \[S48\] → <b>CORE: IDENTITY / BELONGING (the child's)</b>.
13. <b>Be a good parent (2)</b> → why? "I feel like a bad mom that he stinks" \[S46\] → <b>CORE: IDENTITY / SELF-IMAGE (the mom's)</b>. Guilt is an emotional state in 20 snippets.
14. <b>Stop the laundry (1)</b> → why? "I'm so ready to stop doing laundry practically everyday!" \[S20\] → <b>CORE: TIME</b>.

## The child's own ladder (kids and teens in their own words)

- <b>"PRAY TO GOD that this night is different"</b> at sleepovers \[S35\] → why? "I thought they wouldn't be my friend no more" \[S49\] → <b>BELONGING</b>.
- <b>"it's my biggest secret"</b> \[S49\] → why? "I'm so scared of being outted" \[S124\] → <b>STATUS / SELF-IMAGE</b>.
- <b>"OI GET UP"</b> (recording his own alarm voice) → why? "this was very much his own initiative" \[S125\] → <b>AUTONOMY</b>.

## Ranked core-desire list (rolled up)

- <b>How the score works:</b> each core's score = the snippets of the surface desires that ladder to it (primary core only) + the pain snippets that sit on its rungs. One pain is counted once.
- <b>The mapping is my judgement, so the scores are \[INFERENCE\]; the inputs are bank counts.</b>

1. <b>CONTROL / CERTAINTY ("something that actually works, not more waiting") — 397.</b>
   - Desires: dry nights 211.
   - Pains: wets every night 77 · deep sleeper 56 · years of struggle 37 · doctor said wait 8 · never had a dry night 8.
2. <b>BELONGING (the child's) — 351.</b>
   - Desires: sleepovers/camp 69 · dry before camp 4.
   - Pains: can't go to sleepovers 108 · camp fear 100 · friends finding out 70.
3. <b>LOVE / PROTECTING HIS SELF-WORTH — 318</b> (first draft 320).
   - Desire: confidence 85.
   - Pains: child ashamed 171 · self-esteem 33 · shamed by family 29.
4. <b>TIME (her sleep, her mornings) — 269</b> (first draft 278).
   - Desires: fast results 84 · full night's sleep 3 · stop laundry 1.
   - Pains: laundry 72 · sleep loss 68 · frustration/temper 41.
5. <b>STATUS / GROWING-UP IDENTITY (the child's) — 140.</b>
   - Desires: ditch pull-ups 21 · keep the secret 8.
   - Pains: pull-ups leak/outgrown 51 · hiding 37 · smell 21 · sibling 2.
6. <b>SECURITY / PEACE OF MIND — 134.</b>
   - Desires: reassurance 110 · money back 3.
   - Pains: money wasted 15 · relapse 6.
7. <b>AUTONOMY (the child's) — 11.</b> Desire: wakes on own 11. The child-voice rungs add to it.
8. <b>IDENTITY (the mom's: "good mom") — 4</b> desire snippets, plus 20 guilt emotional states.

## Wire it in

- <b>Surface (what the hook says):</b> dry nights, laundry, the binned sleepover invite, camp in X weeks.
- <b>Top cores (what she buys):</b> #1 <b>control/certainty</b> for the mom, #2 <b>belonging</b> for the child. They are close (397 vs 351), and the social-stage angle lives in #2.
- <b>§9 One Belief (Doc 3) should point at #1:</b> "finally something that works instead of waiting." The <b>child's belonging</b> carries the emotion and the deadline. §4B identity and the §13B story should run on both: <i>the mom who stopped waiting so her kid could say yes.</i>
- <b>Mirror of §13:</b> §13 ladders the problem down to its cause. This ladders the desire down to control plus belonging. A launch needs both.

<b>So What → do this:</b> Write the One Belief on <b>control</b> ("the method pediatricians recommend first, so you can stop waiting"). Write the hooks on <b>belonging</b> ("the sleepover he binned the invite for"). Never lead with "dry nights" alone: it's the most-said desire but not the deepest.

---

# 10B · Existing Solutions Teardown

Ranked by §2C failed-solution count on the CLEAN bank. That count is "used or mentioned"; where the bank can tell, explicit failures are shown separately. Counts \[S2\]. <b>Correction (§20 V3):</b> saffron gummies were #5 (81) in the first draft; only 21 of those rows are about bedwetting, so they move to #12. About 3–4 in 10 sampled failed-solution rows are suggestions ("is he willing to wear…?") rather than things the family used \[S3\]. Brand-level counts (rows naming the brand, with star splits) \[S1\].

## Ranking

1. Pull-ups / GoodNites / DryNites: <b>381</b>
2. Bedwetting alarms (all brands): <b>232</b> used; <b>61</b> said outright it failed
3. Doctor / clinic visits: <b>180</b>
4. Desmopressin (DDAVP) / meds: <b>113</b> \[120\]
5. Waiting it out: <b>79</b> \[80\]
6. Mattress protectors / bed pads / guards: <b>49</b>
7. Therapy / OT / pelvic floor: <b>36</b>
8. Limiting fluids: <b>36</b>
9. Constipation treatment: <b>33</b>
10. Lifting / waking at night: <b>30</b>
11. Pee right before bed: <b>22</b>
12. Saffron gummies / supplements: <b>21</b> about bedwetting \[81 incl. Saphire ADHD/mood reviews\]
13. Sleep study / tonsils / airway: <b>20</b>
14. Punishment / shaming: <b>19</b>
15. Reward / sticker charts alone: <b>12</b>
16. "Tried everything" (unspecified): <b>10</b> \[11\]
17. More water by day / bladder training: <b>4</b>
18. Chiropractor: <b>3</b>

## 1. Pull-ups / GoodNites / DryNites (381; 206 parent rows)

- <b>Uses now:</b> the default for most families, and the usual plan for camp and sleepovers too (pull-ups at camp/sleepovers belief: 10).
- <b>Likes:</b> a dry bed and a calm kid. GoodNites Girls XL has <b>4.6★ on 9,186 ratings</b> (1★ 370) \[S126\]. "I prefer a happy kiddo than one who feels bad about themselves" \[S113\]
- <b>Dislikes (51 leak/outgrown + 15 cost):</b>
  - "Barely went half the night and they leaked" \[S113\]
  - "the biggest kid's pull-ups are now far too small - super uncomfortable and not containing all the liquid" \[S70\]
- <b>Horror story:</b> the hidden-evidence cluster (hiding 37). "When I moved his bed, I found a stash of urine soaked nighttime pull-ups!" \[S58\] The relative finding the pack: "she asked me to hide her goodnites somewhere else so nobody would see them" \[S109\] ⚠ <b>Low credibility (§20 V3):</b> r/amiwrong template post (the same "I 3xf and my husband 3xm" opener on three accounts; a top comment calls it a troll post). Do not use in creative.
- <b>Does she believe it works?</b> <b>Yes, as containment; no, as a fix.</b> Some parents think pull-ups delay it ("needed to feel pee", 8).
- <b>Why it fails her:</b> it hides the problem and doesn't end it. It gets visible at exactly the sleepover age, and big kids outgrow the sizes.

## 2. Bedwetting alarms, the category (232 used; 61 explicit fails)

- <b>Category verdict:</b> 339 works · 116 failed · 23 mixed in reviews that state an outcome (71% works; star-based, ≥4★ = works). <b>In parent communities (Reddit / forums, where the avatar talks) it is closer to a coin flip:</b> \~28 works vs \~35 fails on hand-read regex hits \[S111\]. Median <b>3 weeks</b> to dry (n=120) \[S7\].
- <b>What Amazon's own review summaries say:</b> loudness is the only big aspect that is net negative (305+ / 363−). Clip accessibility is 32+ / 159− on DryEasy \[S7\].
- <b>Likes (agent E tally; keep these in our offer):</b> dry nights 121 · fast results 81 · works for deep sleepers 51 · child pride 47 · vibration mode 33 · chart + stickers 30 · child does it alone 23 · parent hears it 22 · sleepover/camp freedom 9 \[S126\].
- <b>Dislikes (our differentiation; alarm review rows, verified):</b> doesn't work 43 · trust/support 38 · battery 36 · broke 36 · false alarms 34 · price 29 · too loud 27 · clip 20 · missed the wee / too late 18 · didn't wake child 17 · bad instructions 16 · range/pairing 12 · hard to switch off 10 \[S1\].
- <b>Horror story:</b> "He was literally laying in a puddle of urine… THE FIRST TIME I USED IT!!!" \[S127\]. And the adult who remembers: "it was so loud and announced the whole house I failed again" \[S128\]
- <b>Does she believe it works?</b> <b>In reviews, yes (339 works vs 116 failed, star-based). In parent communities it's closer to a coin flip (\~28 works vs \~35 fails, hand-read regex hits) — "slept through it" is the main failure.</b> <b>Correction (§20 V3):</b> the first draft said "Mostly YES" from reviews alone. Burned buyers mostly blame <i>the unit</i>; community parents also doubt it will wake <i>their</i> deep sleeper. → We must prove <b>it wakes him</b> and <b>our unit's reliability</b>. Every claim about our unit is UNVERIFIED (no sample yet).

<b>Each alarm brand (ranked by rows that name it):</b>

- <b>Chummie (191 rows; 4–5★ 55 / 1–2★ 12).</b>
  - Uses: Amazon/Walmart buyers, wired.
  - Likes: "My 9 year old was desperate to be dry at night and have sleepovers and thanks to the Chummie alarm, he now can." \[S97\]
  - Dislikes / horror: "This was expensive but only worked correctly for two weeks and stopped working at all." \[S66\]
  - Caveat: the 2016–18 Walmart 5★ cluster reads promotional \[S126\]. 19–20% 1★ on Amazon \[S7\].
  - Why it fails her: wired to the body, pricey (\$79.99–\$99.99), uneven quality.
- <b>DryEasy (185 rows, mostly Amazon excerpts).</b>
  - Likes: "Sure woke me up down the hall EVERY NIGHT, which is also the point." \[S92\]
  - Dislikes: "But is very loud. No way to turn it down if the child shares a room" \[S69\]; the clip is the most-hated part (159 negative mentions) \[S126\].
  - Horror: NOT FOUND as a single story (the clip/loudness complaints are the worst it gets).
  - Why it fails her: the fiddly clip, and a siren she can't turn down.
- <b>Generic Amazon/Walmart clip-ons, our price tier (113 rows; 4–5★ 42 / 1–2★ 27).</b> Listings sit at 2.8★, 3.1★, 2.9★, 1.9★ and 1.0★ \[S7\].
  - Likes: "this helped our son sleep through the night woth no accidents. he is a very deep sleeper" \[S129\]
  - Dislikes: "We learned we needed to charge it every day so it would last through the night." \[S68\]
  - Horror: "As soon as this touched my sons skin it would go off… My son just took the arm bad off." \[S67\]
  - <b>Why it fails her: this is the tier our CJ unit comes from.</b> False alarms, daily charging and dead sensors are the reasons.
- <b>DRI Sleeper Eclipse (95 rows).</b>
  - Likes: "It is wireless so it's easy to use and the alarm is obnoxious, loud enough to wake our deep sleeper." \[S86\]
  - Dislikes / horror: "This only worked once. After the first two or three nights whenever it was worn, the alarm would constantly go off." \[S130\]
  - Why it fails her: \$149–\$190 for "an expensive, tiny piece of plastic" \[S131\]
- <b>TheraPee (66 rows; \$299 / \$199–\$399 plans).</b>
  - Likes: "I hesitated to buy this because it is expensive, but it works! He is so happy because he can now have friends come for sleepovers." \[S101\]
  - Dislikes: price; "It took about 12 weeks for him to be fully "cured,"" \[S132\]
  - Horror: NOT FOUND (0 one- or two-star rows in the bank).
  - Why it fails her: priced out of reach for most.
- <b>Wet-Stop3 (64 rows).</b>
  - Likes: "His brain just wouldn't tell him to get up. This has been a life saver!" \[S133\]
  - Dislikes / horror: "Kept going off even when dry. So defeated the purpose. Waste of money." \[S134\]
  - Why it fails her: a wired, clunky, hard-to-silence old design.
- <b>Oopsie Heroes (48 rows; 4–5★ 32 / 1–2★ 10).</b>
  - Likes: the app and the kid's motivation. "OI GET UP" \[S135\]. Several 5★ Trustpilot reviews praise the app's design in marketing-like language ("Such a beautifully designed app") \[S136\], so treat them carefully.
  - Dislikes / horror: "the alarm would sound between 3 and 8 minutes AFTER the bedwetting occurred" \[S71\]
  - Why it fails her: lag and a sensor that misses the wee.
- <b>Unikor NightGuard, the main competitor (13 Trustpilot reviews; TrustScore 1.9; 12×1★, 1×2★).</b> The bank holds 20 rows because two collectors overlapped.
  - Likes: <b>none found independently.</b> On-site it shows 4.7 on 1,735 reviews with <b>zero 1–2★</b>. Import source: "copy" 139 · CSV import 56 · written on-site <b>5</b>, of the 200 newest \[S126\]. That makes it brand-curated (kept out of the ranked lists).
  - Dislikes: "I never received the unit" \[S64\]
  - Horror: "they offer a 60 day money back which is why I have brought this product… contacted them on 6 occasions to return and had absolutely no response" \[S38\]. (A separate 1★, "stupidly trusted their reviews", now carries the update "They have now got back to me to send a refund.") · "Broken sensor after 4 days" \[S137\]
  - Why it fails her: trust. She sees the ads but can't verify the store.
- <b>Rodger (10 rows).</b>
  - Likes: "very straightforward and easy for a child to do by themselves… It took our 8 year old no more than 2 weeks to have fully dry nights" \[S73\]
  - Dislikes / horror: "about 10 accident in the last month and the alarm has only sounded 3 of those times. We've tried pairing it every night" \[S73\]
  - Why it fails her: \$179.99, and it needs special underwear.
- <b>Dryly (7 rows; NL, out of region).</b>
  - Likes: design and kid pride.
  - Dislikes: "NIghtmare to get going, I gave up" (EUR 250) \[S126\]
  - Why it fails her: price and setup.
- <b>Malem (4 rows).</b>
  - Likes: "We bought the malem alarm… 6 weeks before going on a 4 night school trip… By the time of the trip he was dry the whole time. Cost around £70 but a miracle." \[S25\]
  - Dislikes: "I almost purchased the Malem today, but \$99 is pretty steep." \[S20\]
  - Horror: <b>NOT FOUND</b> in the bank. Amazon Malem Ultimate PRO has 28% 1★ (3.3★ on 53) \[S7\].
  - Why it fails her: clinical and pricey.
- <b>DryBuddy (2 rows).</b> The Trustpilot page is mostly a clothes-dryer brand, so it is <b>not usable</b> as alarm evidence \[S126\]. One 1★ ("Awful cheap product…") is about the dryer, not the alarm \[S138\]. Likes / dislikes / horror for the alarm: <b>NOT FOUND</b>.

## 3. Doctor / clinic visits (180; 120 parent rows name a doctor)

- <b>Uses now:</b> an annual checkup question, a pediatric urologist, an NHS bladder clinic (UK).
- <b>Likes:</b> the doctor who recommends an alarm (10). "The pediatrician told us to wait it out. He suggested trying pee monitors, and we tried other brands and failed. Finally tried this and within one month, completely dry!" \[S73\]
- <b>Dislikes (doctor said wait: 33 as a trigger):</b> "Then from 9 on it's been an exclamation of concern and no offer of advice or help." \[S56\]
- <b>Horror:</b> "Ask for a urology referral and was told it wasn't necessary." \[S45\]
- <b>Believes it works?</b> She trusts the doctor (the #1 authority, 121 + 71) but has given up on getting <i>action</i>.
- <b>Why it fails her:</b> "wait" isn't a plan.

## 4. Desmopressin / DDAVP (113)

- <b>Uses now:</b> for overnights (belief: 9). "My son uses it on any overnight trips and its only failed once" \[S29\]
- <b>Likes:</b> it works the same night. "it was like a miracle drug" \[S40\]
- <b>Dislikes:</b> it stops working when you stop it. "If we were up at the cottage and forgot to spray, he would wet the bed." \[S139\]
- <b>Horror:</b> "He didn't pee for hours after he woke up and then threw up the day after he took it. We only tried it once!" \[S140\]
- <b>Believes it works?</b> <b>Yes, as a one-night patch.</b> That makes it the direct competitor for the sleepover/camp <i>night</i>.
- <b>Why it fails her:</b> it's a pill every night forever, and "We thought the problem was solved. Nope." \[S40\]

## 5. Waiting it out (79; the "will grow out of it" belief: 72)

- <b>Uses now:</b> the default after the doctor visit.
- <b>Likes:</b> no cost, no fight. "Enuresis runs in the family… He will too." \[S107\]
- <b>Dislikes:</b> "So we just need to wait and I'm like how much longer?" \[S11\]
- <b>Horror:</b> "When I was younger dr's Simply said I would outgrow it… I was allowed to stop wearing diapers when I entered high school at almost 15." \[S35\]
- <b>Believes it works?</b> Yes, eventually, which is why it's the habit to beat.
- <b>Why it fails her:</b> the clock runs into the sleepover years.

## 6. Mattress protectors / bed pads / bed guards (49)

- <b>Related alternative (§20 V3 sweep): washable / reusable pads and pants — 24 rows (11 parents)</b> (washable incontinence pads, "nighttime undies", period pants) \[S3\].
- <b>Likes:</b> damage control. "I called it the bedding lasagna method." \[S141\]
- <b>Dislikes:</b> "the pee STILL gets through every single layer and onto the mattress" \[S108\]
- <b>Horror:</b> "He's now sleeping on the floor because he peed through the protector pad onto the mattress." \[S53\]
- <b>Believes it works?</b> Only as damage control.
- <b>Why it fails her:</b> it's more laundry, not less.

## 7. Therapy / OT / pelvic floor (36)

- <b>Likes:</b> NOT FOUND in the bank.
- <b>Dislikes / horror:</b> "I tried OT. Didn't help." \[S45\] · "We've taken him to urologist after urologist, psychiatrists, physiotherapists, Chiropractors, GPs, even holistic healers." \[S142\]
- <b>Why it fails her:</b> slow, costly, aimed at a different problem.

## 8. Limiting fluids (36)

- <b>Likes:</b> easy and free. "She said to just limit his drinking before bedtime… It worked" (for one sleepover) \[S104\]
- <b>Dislikes:</b> "We tried limiting liquids before bedtime, but nothing seems to work." \[S18\]
- <b>Horror:</b> "this year his practices go until later so not drinking water before bed is not an option" (a serious athlete) \[S81\]
- <b>Why it fails her:</b> it doesn't teach waking.

## 9. Constipation treatment (33)

- <b>Dislikes / horror:</b> "Her doctor kept insisting that it was constipation and to do frequent "flush outs"" \[S114\]
- <b>Likes:</b> NOT FOUND in the bank. The science side (Doc 3) notes it helps some kids.
- <b>Why it fails her:</b> it fixes a different cause, if any.

## 10. Lifting / waking the child at night (30)

- <b>Likes:</b> some dry mornings. "We wake him up before we go to bed around 10:30 and sometimes that is enough" \[S44\]
- <b>Dislikes:</b> "I have to physically pull him up and out of bed and walk him to the toilet while he's deliriously asleep." \[S55\]
- <b>Horror:</b> "Now I read that our approach is bad because we do not allow his brain to learn to wake up" \[S42\]
- <b>Why it fails her:</b> the mom becomes the alarm, for years.

## 11. Pee right before bed (22)

- "he goes pee before bed each night… then suddenly he's peeing at night every couple days for no known reason" \[S143\]
- <b>Why it fails her:</b> it's routine, not training.

## 12. Saffron gummies, Saphire and clones (21 bedwetting-related; 201 Saphire rows, 179 of them about ADHD/mood/billing; Trustpilot 2.8 on 227 — live-confirmed)

- <b>Uses now:</b> bought from the 9-year-old-sleepover ads.
- <b>Likes (89 at 4–5★ across all 201 Saphire rows — most of those praise ADHD / mood effects, not dry nights):</b> "These gummies have helped my son stay dry at night after being a bedwetter for 12 years." \[S105\] Kids also like the taste (17) \[S126\].
- <b>Dislikes (raw gummy rows: subscription 75, trust 106 — almost all from ADHD / mood buyers, not bedwetting parents):</b> "Made from China & unauthorized auto-subscription" \[S76\]
- <b>Horror:</b> "IMPERSONATING DOCTORS VIA AI" \[S144\] · "the advert I watched marketed them as if they were designed to stop night time bed wetting" \[S145\] · "They contain St. John's Wort" \[S146\]
- <b>Believes it works?</b> <b>Split.</b> Trust is wrecked by billing problems.
- <b>Why it fails her:</b> it's not a bedwetting treatment ("not one of them helps with kids bed wetting" \[S83\]), and the subscription trap.

## 13. Sleep study / tonsils / airway (20)

- "Sleep apnea. Please get them in for sleep studies." (commenter advice) \[S147\] · "We've tried DDAVP, alarms, checked out constipation, and did a sleep study." \[S59\]
- <b>Why it fails her:</b> it rules things out rather than fixing them.

## 14. Punishment / shaming / chores (19)

- <b>Horror:</b> "My parents and school teachers would spank me for having accidents" (an adult, looking back) \[S148\]
- <b>Why it fails her:</b> she knows it backfires ("if shaming helped…").

## 15. Reward / sticker charts (12 used alone; 30 liked when bundled with an alarm)

- <b>Likes:</b> "When he put the 7th dry morning sticker in a row on his chart he said, "Mom, I'm cured!"" \[S91\]
- <b>Dislikes (alone):</b> "loads of encouragement and promises of reward. Nothing worked." \[S70\]
- <b>Why it fails her:</b> a chart can't wake a sleeping child. Keep it in the box, never sell it alone.

## 16. Chiropractor / alternative (3)

- "My SIL is a McTimoney chiropractor and has helped children with long term bed wetting problems" \[S25\] · "we tried bedwetting alarms, chiro, therapy…. I'm at a loss what to do." \[S112\]
- <b>Why it fails her:</b> no mechanism, no result.

## Doing nothing

Covered under #1 and #6: pull-ups plus waiting is the "nothing" plan. "Do we just keep pull ups?" \[S112\]

## Do they believe these work? (summary)

- <b>Alarms: in reviews yes (71%); in parent communities a coin flip (\~28 vs \~35).</b> Reviewers blame bad units; community parents fear "he'll sleep through it." → <b>Prove it wakes him and keeps working</b>: a receiver heard through walls, a filmed sweat test, an overnight battery run. None exist yet (OPEN).
- <b>Pull-ups, desmopressin, waiting:</b> she believes they <i>contain</i> the problem, not that they <i>fix</i> it. → Contrast "a patch" with "a fix."
- <b>Gummies:</b> mostly NO among the 21 bedwetting-relevant rows. → "No subscription, a real support email" is a supporting differentiator, not the lead.

<b>So What → do this:</b> Lead with <b>"it actually wakes him and keeps working,"</b> not with anti-scam lines and not with "alarms don't work." That means:

- First: a receiver in her room so <i>someone</i> wakes on night one, and a sensor that fires on the first drops. Then: no false alarms from sweat, a clip that stays on, a charge that lasts all night. <b>Only once a sample proves each one.</b>
- Second (reassurance, not the hook): one-time payment, a guarantee whose terms match the ad, and email that gets answered.
- Use pull-ups and desmopressin as the "patch vs fix" contrast. Use "the pediatrician said wait" as the status quo she's done with.

---

# 14 · Voice

## Reading level

Her own writing scores a median <b>Flesch-Kincaid grade 6.2</b> (parents, n=879; interquartile range 4.6–8.4). Community posts score 6.4 and reviews 5.9 \[S149\]. → <b>Write at grade 5–6.</b> Short sentences, kid words, no clinical terms in ads.

## Emotional journey (and where our traffic enters)

1. <b>Awareness / normalising ("it's common, he'll grow out of it").</b>
   - "Currently we are very apathetic about the issue, believing it will resolve over time, so we just use bedtime pull-ups and normalise it" \[S74\]
   - Thread title: "Are we normalizing bedwetting...?" (123 comments) \[S150\]
2. <b>Frustration (laundry, sleep, temper).</b>
   - "I cannot stand wasting money and washing all his bedclothes twice a week anymore and am desperate for advice" \[S19\]
   - "I just yelled at two of my kids for wetting the bed. I feel so bad" \[S57\]
3. <b>Desperation / seeking a fix (everything failed, an event is coming).</b>
   - "my ds is 11 next week and he wets the bed 2-3 times every night, we have tried both medications and the alarm to no avail" \[S25\]
   - "It's super discouraging, especially as we approach summer camp registration season." \[S59\]
4. <b>Relief / commitment.</b>
   - "By the time of the trip he was dry the whole time. Cost around £70 but a miracle." \[S25\]
   - "Wish I had done it sooner." \[S116\]

<b>Where our traffic enters:</b> at <b>frustration → desperation</b>, usually lit by a dated social event. Parent emotional states (clean bank): frustration 91 · worry 83 · helplessness 36 · exhaustion 27, against relief 56 \[S2\]. Parents are mostly <b>solution-aware</b> (189 of 427 community parent rows) \[S12\]. → The ad's job: name her frustration, name the event, then show why <i>this</i> alarm works where the last one didn't.

## Swipe — her real phrases

★ = appears in 3+ snippets. (n) = CLEAN snippets containing it \[S151\]; counts that moved after the §20 V3 cleanup \[S152\].

<b>Her labels and phrases (★, 3+ snippets):</b>

1. ★ "every night" (110)
2. ★ "sleepover" (116)
3. ★ "camp" (112)
4. ★ "pull-up / pull up" (138 / 130)
5. ★ "Goodnites" (62)
6. ★ "deep sleeper" (59)
7. ★ "heavy sleeper" (27)
8. ★ "sound sleeper" (3)
9. ★ "dry night(s)" (66)
10. ★ "embarrassed" (95)
11. ★ "middle of the night" (44)
12. ★ "laundry" (46)
13. ★ "grow out of it" (30) / "outgrow" (28)
14. ★ "tried everything" (26)
15. ★ "worth every penny" (21)
16. ★ "ashamed" (20)
17. ★ "every single night" (19)
18. ★ "nappies / nappy" (UK/AU: 18 / 15)
19. ★ "a miracle" (16)
20. ★ "sleep over" (16)
21. ★ "find out / found out" (14 / 12)
22. ★ "false alarm" (15)
23. ★ "waste of money" (12)
24. ★ "in a row" (12)
25. ★ "residential" (UK: 13)
26. ★ "wet sheets" (12)
27. ★ "proud of" (11) / "so proud" (6)
28. ★ "nothing worked" (10)
29. ★ "humiliated" (10)
30. ★ "game changer" (8)
31. ★ "lazy" (9)
32. ★ "whole house" (7)
33. ★ "it's normal" (7)
34. ★ "exhausted" (7)
35. ★ "desperate" (5)
36. ★ "mortified" (6)
37. ★ "school trip" (6) / "field trip" (5)
38. ★ "to no avail" (5)
39. ★ "not his fault" (5)
40. ★ "obnoxious" (alarm, 4)
41. ★ "made fun of" (4)
42. ★ "at a loss" (3)
43. ★ "strip the bed" (3)
44. ★ "puppy pad(s)" (3)
45. ★ "down the hall" (3)
46. "consecutive" (2 — below the ★ bar after the cleanup)
47. ★ "fed up" (3)
48. ★ "normal teen" (3)
49. ★ "lifesaver" (3)
50. ★ "feel awful" (3)

<b>Vivid one-offs (1–2 snippets; strong hook material):</b><br />51. "at my wits end" (2)<br />52. "drowning in pee laundry" (2)<br />53. "sleeps like the dead" (2)<br />54. "social suicide" (2)<br />55. "how much longer?" (2)<br />56. "holy crap this is hard" (2)<br />57. "abandoned ship" (2)<br />58. "like having a new born baby again" (2)<br />59. "the outcast of the house" (2)<br />60. "family secret" (2)<br />61. "OI GET UP" (2)<br />62. "a miracle drug" (2)<br />63. "an end in sight" (2)<br />64. "like a brick" (1)<br />65. "loud enough to wake the dead" (1)<br />66. "announced the whole house I failed again" (1)<br />67. "PRAY TO GOD that this night is different" (1)<br />68. "my biggest secret" (1)<br />69. "Mom, I'm cured!" (1)<br />70. "a very grumpy wet kid" (1)<br />71. "deliriously asleep" (1)<br />72. "bedding lasagna" (1)<br />73. "the sneaky dreams" (1)<br />74. "end of my rope" (1)<br />75. "out of ideas" (1)<br />76. "night terrors" (alarm, 1)<br />77. "it's such a taboo subject" (1)

## Quote buckets (new quotes, not used in §10)

- <b>Pain / frustration:</b>
  - "So far no luck just a very grumpy wet kid . I'm drowning in laundry" \[S28\]
  - "I'm literally drowning in pee laundry." \[S33\]
  - "I have to change him and his whole bedding (he sleeps in a full size bed) in the middle of the night." \[S42\]
- <b>Mindset:</b>
  - "I had no idea that it was all hormonal and fully out of his control." \[S22\]
  - "We're ALWAYS encouraging and never make him feel as if it's his fault." \[S59\]
- <b>Deep fears:</b>
  - "I feel really sad at the thought of DS missing out on the trip but equally don't want him to have to potentially face a mortifying experience." \[S120\]
  - "He's at the age where these things are going to be fuel for being picked on and it worries me." \[S33\]
- <b>Motivation & urgency:</b>
  - "The reality is now hitting him about going on the trip- it's a PGL type thing- and he's now worried about potentially being wet during the night." \[S120\]
  - "He's long set his sights on this trip with the hopes that his bedwetting would stop well ahead of time." \[S153\]
- <b>Emotional response to the struggle:</b>
  - "I'm so sad for him… I just feel awful for him." \[S11\]
  - "I would HATE for her to miss out on the fun of sleepovers because of her problem" \[S154\]
  - A "failing as a parent" line was searched for and is <b>NOT FOUND</b> verbatim in the bank, so none is used. The closest is "I feel like a bad mom" (see §10).

## Words to USE vs words to AVOID

<b>USE (her words):</b> wet the bed · wets the bed · accidents · dry nights · a dry night · pull-ups / Goodnites (US) · DryNites / night pants / nappies (UK/AU) · deep sleeper / heavy sleeper · sleepover · camp / school trip / residential (UK) · laundry / wet sheets / strip the bed · middle of the night · "he can't help it" / "not his fault" · "grow out of it" (to argue against) · "worth every penny" · "game changer" · "it worked" · "proud" · "his secret" · "find out".

<b>AVOID in ads, hooks and headlines (the plain word she'd say instead).</b> Product page or FAQ only, where accuracy needs it:

- "enuresis / nocturnal enuresis" → <b>bedwetting / wetting the bed</b>
- "void / micturition / urinate" → <b>pee</b> (US) / <b>wee</b> (UK/AU)
- "conditioning therapy / enuresis alarm" → <b>bedwetting alarm / alarm training</b>
- "moisture sensor / transmitter" → <b>the little clip / sensor</b>
- "receiver unit" → <b>the parent alarm that sits by your bed</b>
- "ADH / vasopressin / nocturnal polyuria" → <b>the night-time pee hormone</b>
- "desmopressin" → <b>the bedwetting pill or spray (DDAVP)</b> — name it only in comparisons
- "incontinence" → <b>accidents / wetting</b>
- "diaper" (for an 8–12-year-old) → <b>pull-up / night pants</b>. Kids hate "diaper": "the kid that wears a diaper" \[S30\]
- "bedwetter" as a label for the child → <b>"kids who wet the bed."</b> She uses "bedwetter" (80 snippets), but the child is mortified by labels.
- Hype words the category's ads overuse \[S31\] \[S43\]:
  - "NeuroWake technology" / "brain retraining" → <b>teaches his body to wake up</b>
  - "97% of families see results" / "98% Success Rate" → <b>most kids are dry in about 3 weeks</b>, and only with a source
  - "cure" → <b>dry nights</b> (AAP warns against "cures")
  - "Clinically Proven" / "Award Winning" → <b>the method pediatricians recommend first</b>
  - "breakthrough" / "miracle" → let customers say "miracle"; we don't
  - "buzzer" / "punishment" → <b>gentle alarm / vibration mode</b>

## Thread-title hooks (Forum tactics: most-engaged titles, comment counts)

Ranked by comments \[S9\]:

1. "Daughters (8.5 and 6) still wet the bed at night" — 373 \[S155\]
2. "Bedwetting: please help an exhausted mom create a better system" — 252 \[S17\]
3. "AITA for putting my autiatic son in goodnites despite my husband telling me not to?" — 232 \[S156\]
4. "Was I wrong for not hiding my daughters goodnites better?" — 207 (⚠ r/amiwrong template post) \[S109\]
5. "AITAH for buying my daughters goodnites at the store?" — 174 \[S157\]
6. "Am I wrong for insisting my daughter wear a pull up every night even though she usually doesn't need it?" — 166 (⚠ r/amiwrong template post) \[S158\]
7. "11m still wetting the bed and I have to keep denying him sleepovers and he's upset" — 149 \[S55\]
8. "AIO about my kid's bedwetting?" — 136 \[S58\]
9. "I lied to my best friends mom about wetting the bed" — 135 \[S159\]
10. "Are we normalizing bedwetting...?" — 123 \[S150\]
11. "My almost 12 yo still wets the bed and my heart breaks for him." — 109 \[S11\]
12. "Bed wetting alarms - is this punishment?" — 105 \[S80\]
13. "Bedwetting - at my wits end." — 103 \[S22\]
14. "6yo still wetting the bed, going back to pull-ups" — 97 \[S160\]
15. "Parents!!! Bed wetting alarms real experiences please!" (AU) — 96 \[S161\]
16. "Bedwetting (scouts)" — 93 \[S162\]
17. "Was I wrong for celebrating my older daughter getting over her bedwetting and (unintentionally) making her sister feel bad?" — 91 (⚠ r/amiwrong template post) \[S163\]
18. "My 7-year old daughter won't go one night without wetting the bed…" — 88 \[S115\]
19. "Just looking for support: Bedwetting son" — 87 \[S164\]
20. "5 year old betwetting" (UK) — 83 \[S42\]
21. "7yo Bedwetter needs to know he isn't alone." — 81 \[S165\]
22. "Bedwetting at five?" — 79 \[S166\]
23. "Teenager still bedwetting and I'm loosing my mind about it" — 73 \[S143\]
24. "My almost 13 year old still wets the bed and it makes me so sad for them" — 70 \[S40\]
25. "So Proud of my Son! (Beating Bedwetting)" — 68 \[S167\]

<b>Also high-engagement, but outside the parent avatar (agent D):</b> "My 11 year old sister has randomly started wetting the bed." (434c) · "9 yr old niece purposefully wetting bed" (331c) · "Is it normal for a 10 year old to still wet the bed ?" (100c) · "Rough situation, son wet the bed at summer camp…" (64c) \[S27\].

<b>Forum titles (SNIPPET — confirm the wording at the URL before using in creative):</b> "7yo wet the bed at a sleepover." (Mumsnet) · "Bedwetting and school residential y6" (Mumsnet) · "Would you let your child go on a sleepover wearing a pull up" (Mumsnet) · "Finally happened - Son teased by close friends for bedwetting" (BabyCenter) · "My daughter is going to a sleepover, she's 12 and wets the bed…" (Quora) · "An alarm that actually works for bed wetting" (Mumsnet) \[S9\]. Also: "How to help a teenager wearing pull-ups to a sleepover?" \[S168\]

<b>Credibility note (§20 V3):</b> #4, #6 and #17 are the three r/amiwrong template posts (same opener on three accounts; flagged as likely troll posts). #3, #5 and #8 come from AITA-style subs, which are low credibility. Use the <i>shape</i> of these titles, never their content. <b>\[INFERENCE\]</b> Bedwetting-kid creative may attract this crowd in ad comments, so plan comment moderation.

<b>Pattern:</b> the most-engaged titles are <b>confessional or permission-seeking</b> ("Am I wrong…", "AITA…", "at my wits end", "my heart breaks"). They aren't product questions. → Hook format (our draft lines, not quotes): <i>Am I wrong for saying no to his sleepover?</i> / <i>My 11-year-old binned the invite.</i>

<b>So What → do this:</b> Write hooks at grade 5–6 in her words: "every night", "deep sleeper", "sleepover", "camp", "pull-ups", "tried everything". Borrow the confessional "Am I wrong…" title shape. Keep clinical and hype words (enuresis, NeuroWake, 97%, cure) off ads entirely.

---

# 18 · Trigger events

Ranked by §2C trigger count (CORE, verified). The second number is <b>first-hand</b> rows only (a parent, or a teen about themselves); the CORE count also includes commenters' memories. Counts \[S1\]. The social triggers are inflated by targeted searches, so treat them as a ranking. <b>§20 V3 check:</b> in a hand-read sample \~5 in 10 camp / sleepover / friend rows were advice (scout leaders, teachers, adults), not a trigger, so the <b>first-hand number is the one to trust</b>. On first-hand rows and by unique thread, <b>sleepover leads camp</b> (58 vs 56; 79 vs 54 threads); #1 and #2 below are effectively tied \[S3\].

1. <b>The school camp or trip date lands (113 · first-hand 56).</b>
   - <i>What happened:</i> a trip letter, camp sign-up or registration season.
   - <i>Where:</i> at home, at dinner.
   - <i>Who:</i> the child (11–12), a sibling, mom.
   - "Last night him and his brother were talking and my youngest (9 yo) asked 12 yo if he's excited about going on the 8th grade trip to Washington DC… 12 yo turns to me and just says "mom I wet the bed"" \[S11\]
   - UK: "The reality is now hitting him about going on the trip- it's a PGL type thing" \[S120\]
2. <b>A sleepover invitation arrives (111 · 58).</b>
   - <i>What:</i> a party card or a best friend's ask.
   - <i>Where:</i> the school bag, the trash can.
   - <i>Who:</i> the child, mom.
   - "he was invited to a sleepover a couple nights ago. He threw the card in the trash and I only found it and asked him why he didn't want to go. He said because he is scared he will pee the bed" \[S23\]
3. <b>A friend or classmate finds out or comments (45 · 27).</b>
   - <i>What:</i> a smell remark, or Goodnites seen.
   - <i>Where:</i> the child's bedroom, the bathroom cabinet during a holiday visit.
   - <i>Who:</i> friends, a cousin.
   - "his friends have started to comment on how smelly his room is" \[S169\]
   - The niece who found the Goodnites in the bathroom cabinet \[S109\] ⚠ <b>Low credibility (§20 V3):</b> r/amiwrong template post (the same "I 3xf and my husband 3xm" opener on three accounts; a top comment calls it a troll post). Do not use in creative.
4. <b>The child cries or says "I'm ashamed" (37 · 19).</b>
   - <i>What:</i> the child says it out loud.
   - <i>Where:</i> the morning after, or a quiet talk.
   - <i>Who:</i> the child and mom.
   - "He told me a few days ago that even though I have never "shamed him" ever, that he feels very ashamed." \[S52\]
   - "she started waking up wet again… She was so sad and cried about it a bunch." \[S40\]
5. <b>The annual checkup says "wait" again (33 · 19).</b>
   - <i>Where:</i> the pediatrician's office.
   - <i>Who:</i> mom, child, doctor.
   - "We asked her pediatrician every year at her annual checkup and until she turned 9, the answer was always "oh it's still normal at this age". Then from 9 on it's been an exclamation of concern and no offer of advice or help." \[S56\]
6. <b>A family trip or stay away (32 · 17).</b>
   - <i>What:</i> Thanksgiving at a sister's, the in-laws, a holiday.
   - <i>Who:</i> the extended family.
   - "we will be traveling to my sisters house about 4 hours away and will be spending 4 nights there so I am a little stressed out over that as well." \[S170\]
   - "We recently traveled to my in-laws house where my son wet the bed." \[S171\]
7. <b>A birthday hits and he's still wet: 9, 10, "almost 12" (25 · 23).</b>
   - <i>Where:</i> at home.
   - <i>Who:</i> mom, looking at the calendar.
   - "He's 12 in a couple of weeks. I just feel awful for him." \[S11\]
8. <b>A sibling gets dry first, or gets compared (19 · 12).</b>
   - <i>Where:</i> the bedroom or dinner table.
   - <i>Who:</i> a younger brother or sister.
   - "his 6 yo brother has basically beat bedwetting, and DS10 is feeling very jealous and ashamed to be outpaced by his little brother." \[S63\]
9. <b>Pull-ups run out of sizes or start leaking (12 · 5).</b>
   - <i>Where:</i> the store aisle, the morning sheets.
   - <i>Who:</i> mom.
   - "At this point, pull-ups are no longer available for her size." \[S56\]
10. <b>The child asks for help or an alarm himself (11 · 11).</b>
    - <i>Where:</i> in front of the TV.
    - <i>Who:</i> the child (almost 9).
    - "he decided he wanted an alarm after watching a mythbusters episode" \[S135\]
11. <b>The doctor finally suggests an alarm (10 · 7).</b>
    - <i>Where:</i> the clinic.
    - "The pediatrician told us to wait it out. He suggested trying pee monitors" \[S73\]
12. <b>The 3 a.m. breaking point (9 · 8).</b>
    - <i>Where:</i> the laundry room at night.
    - <i>Who:</i> mom, alone.
    - "Went to check on him . He wet through the goidnite soaked the bed . ... Now I'm doing laundry at 3 am ." \[S24\]
13. <b>Wet in front of others at camp or a sleepover (7 · 2).</b>
    - <i>Where:</i> a camp cabin.
    - <i>Who:</i> half a dozen boys and his friend.
    - "he had a very 'visible' nighttime accident that was discovered by the entire cabin right as he was waking up. Including his friend" \[S110\]
14. <b>The host or another parent gets involved (5 · 4).</b>
    - "Maybe if this is the case his friends parent can pick up or you can drp off some pull ups before hand." \[S172\]
15. <b>Relapse after an illness (4 · 2).</b>
    - "After a recent illness has wet the bed 95% of the time for the last couple months." \[S173\]
16. <b>Mom finds the hidden evidence (2 · 2).</b>
    - <i>Where:</i> under the bed.
    - "When I moved his bed, I found a stash of urine soaked nighttime pull-ups!" \[S58\]
17. <b>A grandparent's comment (2 · 2).</b>
    - <i>Who:</i> great-grandma.
    - "she is now saying if it doesn't stop everyone will be laughing at him." \[S37\]

<b>Deadline calendar (from the posts):</b>

- US: summer sleepaway camp, registration Feb–Apr; 8th-grade trips.
- UK: the Year 6 residential / PGL; posts run Jan–Apr.
- AU/NZ: school camp (Year 5/6).
- Guidance already uses this deadline: "To help your child stop bedwetting before camp, it is best to start using a bedwetting alarm at least two months before." \[S174\]

<b>So What → do this:</b>

- Build the first hook set on triggers <b>#1, #2 and #3</b>: the trip letter, the binned invite, the friend who noticed. Each opens with what just happened, where and who.
- Run the pediatrician "wait" (#5) and the sibling (#8) as second-wave hooks.
- Time spend to the calendar: US camp registration Feb–Apr, UK residentials Jan–Apr, AU/NZ school camps. Lead with "start 8 weeks before," never "dry by Friday."

---

# Corrections from §20 verification (V3)

The first draft of this doc was adversarially checked against the bank and live pages on 2026-11-16 \[S3\]. Every change it forced is listed here, so nothing was quietly dropped. Backup of the pre-correction draft: docs/doc2.preV3.bak.

1. Data bank: 179 Saphire / saffron-gummy Trustpilot rows that never mention bedwetting removed from every ranked list; lists now run on 1,988 CLEAN rows (were 2,167 CORE). Re-tally script: tallies/doc2\_tally\_[v3clean.py](http://v3clean.py); swipe re-count: tallies/swipe\_count\_[v3clean.py](http://v3clean.py).
2. Objection 'scam / no delivery / no support': 147 → 50 (102 off-topic Saphire rows). Still #1, but only just ahead of 'didn't wake the child' (48).
3. Objection 'subscription trap': 81 → 12; falls from #2 to #17.
4. Objections 'doesn't work' 60 → 44 · 'price' 51 → 40 · 'child refuses' 44 → 33 · 'broke' 38 → 36 · 'takes weeks' 27 → 24 · 'sensor missed' 23 → 21 · 'confusing instructions' 18 → 16 · 'gummies not a bedwetting product' 2 → 1; objection list re-ranked.
5. Objection 'battery / charging': 40 → 36 (parents 16 → 14). The first draft's text disagreed with its own tally; the caveat line now says 72 → 36.
6. Failed solution 'saffron gummies': 81 → 21 bedwetting-related; moved from #5 to #12 in §10B (section moved and renumbered). Desmopressin 120 → 113 · waiting 80 → 79 · 'tried everything' 11 → 10.
7. §10B gummy heading: now '21 bedwetting-related; 201 Saphire rows, 179 of them about ADHD/mood/billing; Trustpilot 2.8 on 227 — live-confirmed'. Gummy likes/dislikes counts flagged as mostly non-bedwetting.
8. Emotions: frustration 277 → 171 · worry 147 → 139 · anger 106 → 50 (from #3 to #10) · relief 89 → 79 · hope 83 → 78 (§2C and §10 mindset; §14 parent figures updated too).
9. Burned / skeptical 'yes': 336 → 234.
10. Desires: fast results 93 → 84 (≈4 in 10 sampled rows mis-tagged); child's confidence 87 → 85 (now #3, fast results #4). Downstream §10 goals, 4 forces and §10A ladder updated; §10A core scores LOVE 320 → 318, TIME 278 → 269 (order unchanged).
11. Needs: comfortable to wear 37 → 36 · parent receiver 15 → 14. Pains: 'years of struggle' 37 → 36 (now #12, after 'hiding').
12. Authority: other parents / reviews 64 → 47 · pediatrician 71 → 70 · book 27 → 26. Awareness: product 1,073 → 903 · most aware 98 → 89.
13. Buyer group, child-age and country lines in §2C recomputed on the CLEAN bank (e.g. US 632 → 491, grandparents 22 → 9); §3 country and §3A grandparent lines updated.
14. Child age by unique thread added: 8–12 = 151 of 300 threads (50%), not 63% by row; 5–7 = 106 threads (35%); age 7 = 52 threads vs 39 for age 9 (the 7 peak is sharper). 182 of the 305 8–12 rows inherit their age from the thread opener.
15. Alarm reviews: 5–8-year-olds are 53 of 71 exact-age alarm reviews (75%); 9–12 only 16 (23%). Added to §3, §3A and the avatar verdict.
16. Mom share: '177 moms vs 34 dads (84%)' re-worded. Gender is visible in only 211 of 1,046 parent rows (20%), mostly via mum forums we chose. Explicit in the text: 24 moms vs 9 dads (73%). Direction holds; size isn't measurable.
17. Mom age '30s to late 40s' from three posts: WRONG evidence. All three are r/amiwrong template / likely troll posts → dropped; age is now \[INFERENCE\] 30s–40s from the SimilarWeb proxy only. 'The one person' re-worded to match.
18. r/amiwrong 'hide her goodnites' quote (§10 key moments, §10B pull-ups, §18 trigger 3) flagged low credibility. The r/amiwrong 'sleep without her pull ups' quote was replaced in §10 desires (Walmart Chummie review) and §10A ladder (r/ADHDparenting). Thread-title hooks #4/#6/#17 flagged, AITA-style subs noted as low credibility.
19. ADHD / autism sub-avatar: 84 snippets / 62 threads → 68 / 45 (44 rows / 34 threads name it in the quote itself; 16 Saphire ADHD-gummy reviews removed).
20. 'Alarms work' framing: '339 works vs 116 failed (71%)' is star-based review data. In parent communities it is ≈ a coin flip (\~28 works vs \~35 fails); 'slept through it' is the main failure. §10B 'Does she believe it works? Mostly YES' was wrong and is replaced; §10 past victories and the §10B summary updated.
21. Date fixes: Unikor Trustpilot 'stupidly trusted' 2026-11-16 → 2026-10-02 · 'correspondence stopped cold' → 2026-10-16 · '60 day money back… 6 occasions' → 2026-09-13. Oopsie Heroes '3 and 8 minutes AFTER' 2026-02-03 → 2026-03-02 (the 'AU' label was dropped: not shown live). Walmart Chummie Elite 'only worked correctly for two weeks' 2025-12-31 → date unconfirmed (the live page shows 2026-08-18).
22. Link fix: 'this was very much his own initiative' now cites comment pe17ear (2026-10-05), not ooi3mrp (2026-05-29).
23. Unikor 'stupidly trusted their reviews' review now carries a live update ('They have now got back to me to send a refund.'). This is noted everywhere it is used as 'no support' or 'doesn't work' evidence.
24. Evidence tags: 54 source marks (≈30 distinct quotes/pages) re-opened live by V3 are now \[VERBATIM\] (Unikor/Oopsie Trustpilot, Walmart Chummie Elite, Amazon UK B0DNJTYTBN, Mumsnet 1902206 and 4647394, Netmums 'school work', RCH, SimilarWeb, and the six Reddit threads V3 pulled). The 24 Amazon US /portal/ cites (behind a sign-in wall) and every other unopened cite (260 marks) are now \[SNIPPET\]. The Walmart Chummie Premium 'desperate to be dry… sleepovers' review could not be found live (the URL redirects), so it stays SNIPPET.
25. Social-stage caveat added: sleepover / camp / friend labels mis-tag \~4–5 in 10. The first-hand social share is probably 15–25%. §18 now says first-hand counts are the ones to trust, and that sleepover leads camp on first-hand rows and threads (58 vs 56; 79 vs 54).
26. Objection 16 'child too young' flagged as a weak fit (a commenter's reassurance, not a buyer objection).
27. Swipe counts moved after cleanup: find out 15 → 14 · waste of money 14 → 12 · in a row 14 → 12 · proud of 12 → 11 · game changer 9 → 8 · desperate 6 → 5 · consecutive 3 → 2 (loses its ★).
28. Under-covered themes added from V3's sweep: anxiety / stress (80 rows, 38 parents) in §3A ADHD and §10 mindset · 'it stops at puberty' (26 rows) under 'will grow out of it' · washable pads / pants (24 rows) in §10B pads.
29. Avatar verdict added to §3 (V3): keep the locked avatar, moms of 8–12. The social stage is the creative world and the motivation. Cast and target \~7–10 so the 5–8 buyers aren't shut out. Lead objection handling with 'it actually wakes him and keeps working', not anti-scam. The §3, §3A, §10 and §10B 'So What' lines were rewritten to match.
30. Not changed (V3 confirmed OK): 2,232 / 2,167 row counts and source mix · pain and trigger row counts · beliefs (incl. ADHD belief 52) · social-stage row shares (22% / 8% / 28%) · SimilarWeb figures · sub-avatar sizes for 5–7, teens, step-parents. Three duplicate row pairs (S0101/S0984, S0278/S1126, S0539/S0995) remain in the bank; their effect is ≤3 on any count.

---

# Sources (Doc 2)

- \[S1\] file:databank.csv · §2C data bank tally (tallies/doc2\_[tally.py](http://tally.py)) \[DATA\] · 2026-11-16
- \[S2\] file:tallies/doc2\_tally\_v3clean.py · §2C re-tally after §20 V3 cleanup (tallies/doc2\_tally\_[v3clean.py](http://v3clean.py)) \[DATA\] · 2026-11-16
- \[S3\] file:verify/V3-customer.md · §20 V3 customer verification \[DATA\] · 2026-11-16
- \[S4\] file:collect/B-toollog.md · agent B tool log · 2026-11-16
- \[S5\] file:collect/E-toollog.md · agent E tool log · 2026-11-16
- \[S6\] file:collect/B-product-pulse.md · agent B product-pulse · 2026-11-16
- \[S7\] file:collect/E-product-pulse.md · agent E review pulse · 2026-11-16
- \[S8\] file:tallies/doc2\_tally.py · NORM + CONFIRM rules · 2026-11-16
- \[S9\] file:collect/B-notes.md · agent B query-bias note · 2026-11-16
- \[S10\] file:verify/v3\_age.py · §20 V3 unique-thread age tally (verify/v3\_age.txt) \[DATA\] · 2026-11-16
- \[S11\] [https://www.reddit.com/r/breakingmom/comments/1fxhhjy/](https://www.reddit.com/r/breakingmom/comments/1fxhhjy/) · Reddit r/breakingmom \[VERBATIM\] · 2024-10-06
- \[S12\] file:collect/B-tally.txt · agent B parent split · 2026-11-16
- \[S13\] [https://www.similarweb.com/website/trysaphire.com/](https://www.similarweb.com/website/trysaphire.com/) · SimilarWeb \[VERBATIM\] · 2026-11-16
- \[S14\] [https://www.similarweb.com/website/unikor.shop/](https://www.similarweb.com/website/unikor.shop/) · SimilarWeb \[VERBATIM\] · 2026-11-16
- \[S15\] [https://www.similarweb.com/website/goodnites.com/](https://www.similarweb.com/website/goodnites.com/) · SimilarWeb \[SNIPPET\] · 2026-11-16
- \[S16\] file:verify/v3\_tally.py · §20 V3 independent tally (verify/v3\_tally.txt) \[DATA\] · 2026-11-16
- \[S17\] [https://www.reddit.com/r/laundry/comments/1wkc3ft/](https://www.reddit.com/r/laundry/comments/1wkc3ft/) · Reddit r/laundry \[SNIPPET\] · 2026-09-19
- \[S18\] [https://www.reddit.com/r/bedwetting/comments/1w78fua/](https://www.reddit.com/r/bedwetting/comments/1w78fua/) · Reddit r/bedwetting \[SNIPPET\] · 2026-09-04
- \[S19\] [https://www.reddit.com/r/Parenting/comments/1ehjfxm/](https://www.reddit.com/r/Parenting/comments/1ehjfxm/) · Reddit r/Parenting \[SNIPPET\] · 2024-08-01
- \[S20\] [https://www.reddit.com/r/AskParents/comments/59pcsr/bedwetting\_alarm\_experience/](https://www.reddit.com/r/AskParents/comments/59pcsr/bedwetting_alarm_experience/) · Reddit r/AskParents \[SNIPPET\] · 2016-10-27
- \[S21\] file:collect/D-avatar.md · agent D household signals · 2026-11-16
- \[S22\] [https://www.reddit.com/r/daddit/comments/1jh5b9z/](https://www.reddit.com/r/daddit/comments/1jh5b9z/) · Reddit r/daddit \[VERBATIM\] · 2025-03-22
- \[S23\] [https://www.reddit.com/r/Parenting/comments/2hny4d/](https://www.reddit.com/r/Parenting/comments/2hny4d/) · Reddit r/Parenting \[VERBATIM\] · 2014-09-28
- \[S24\] [https://www.reddit.com/r/AskParents/comments/1heylf2/comment/m2gyjp7/](https://www.reddit.com/r/AskParents/comments/1heylf2/comment/m2gyjp7/) · Reddit r/AskParents \[SNIPPET\] · 2024-12-17
- \[S25\] [https://www.mumsnet.com/talk/childrens\_health/1902206-Bedwetting-12-year-old](https://www.mumsnet.com/talk/childrens_health/1902206-Bedwetting-12-year-old) · Mumsnet (UK) \[VERBATIM\] · 2013-11-08
- \[S26\] file:collect/E-objections.md · agent E age note · 2026-11-16
- \[S27\] file:collect/D-triggers.md · agent D unbiased check · 2026-11-16
- \[S28\] [https://www.reddit.com/r/AskParents/comments/1imod6b/](https://www.reddit.com/r/AskParents/comments/1imod6b/) · Reddit r/AskParents \[SNIPPET\] · 2025-02-11
- \[S29\] [https://www.reddit.com/r/BoyScouts/comments/14l6war/comment/jpvhl2v/](https://www.reddit.com/r/BoyScouts/comments/14l6war/comment/jpvhl2v/) · Reddit r/BoyScouts \[SNIPPET\] · 2023-06-28
- \[S30\] file:collect/D-spec.md · agent D sleepover-discretion check · 2026-11-16
- \[S31\] file:collect/A-taken-map.md · Winning Hunter ad log (agent A) \[DATA\] · 2026-11-16
- \[S32\] [https://www.reddit.com/r/Mommit/comments/1w223p8/comment/p6pi4cq/](https://www.reddit.com/r/Mommit/comments/1w223p8/comment/p6pi4cq/) · Reddit r/Mommit \[SNIPPET\] · 2026-08-30
- \[S33\] [https://www.reddit.com/r/Parenting/comments/15ifxdr/11m\_still\_wetting\_the\_bed\_and\_i\_have\_to\_keep/](https://www.reddit.com/r/Parenting/comments/15ifxdr/11m_still_wetting_the_bed_and_i_have_to_keep/) · Reddit r/Parenting \[VERBATIM\] · 2023-08-04
- \[S34\] [https://www.reddit.com/r/Mommit/comments/1w223p8/comment/p6sfx8r/](https://www.reddit.com/r/Mommit/comments/1w223p8/comment/p6sfx8r/) · Reddit r/Mommit \[SNIPPET\] · 2026-08-30
- \[S35\] [https://www.youtube.com/watch?v=fym\_v7iQFDw](https://www.youtube.com/watch?v=fym_v7iQFDw) · YouTube comments \[SNIPPET\] · 2019 (approx., relative date)
- \[S36\] [https://www.reddit.com/r/bedwetting/comments/1p7zpa5/](https://www.reddit.com/r/bedwetting/comments/1p7zpa5/) · Reddit r/bedwetting \[SNIPPET\] · 2025-11-27

> ⚠️ <b>S37–S174 were rebuilt on 2026-11-17.</b> A container reset wiped the local file mid-upload. Each source below was recovered by matching the quote next to its \[S#\] against the §2C data bank CSV (and live searches for thread titles). Quote matches are exact, but a few auto-matches may point at a duplicate post — confirm the URL before using a quote in live ads. 5 marks were local tally/ad-log files (lost); 1 thread URL could not be recovered.

- \[S37\] [https://www.reddit.com/r/Autism\_Parenting/comments/1xumqte/i\_dont\_want\_to\_do\_this\_anymore/](https://www.reddit.com/r/Autism_Parenting/comments/1xumqte/i_dont_want_to_do_this_anymore/) · reddit r/Autism\_Parenting · 2026-11-12
- \[S38\] [https://www.trustpilot.com/reviews/6abf8ff56d73504fed66e0ea](https://www.trustpilot.com/reviews/6abf8ff56d73504fed66e0ea) · Trustpilot — [unikor.shop](http://unikor.shop) (NightGuard alarm) (reviewer country GB) · 2026-10-02
- \[S39\] [https://www.reddit.com/r/Incontinence/comments/1eyqr2h/](https://www.reddit.com/r/Incontinence/comments/1eyqr2h/) · reddit r/Incontinence \[OP post\] · 2024-08-22
- \[S40\] [https://www.reddit.com/r/breakingmom/comments/1lhu89g/](https://www.reddit.com/r/breakingmom/comments/1lhu89g/) · reddit r/breakingmom \[OP post\] · 2025-06-22
- \[S41\] [https://www.reddit.com/r/ADHDparenting/comments/1w4cdr4/comment/p7bz5ey/](https://www.reddit.com/r/ADHDparenting/comments/1w4cdr4/comment/p7bz5ey/) · reddit r/ADHDparenting · 2026-09-02
- \[S42\] [https://www.reddit.com/r/UKParenting/comments/1uk32yr/](https://www.reddit.com/r/UKParenting/comments/1uk32yr/) · reddit r/UKParenting (UK) \[OP post\] · 2026-06-30
- \[S43\] local research file — Winning Hunter ad log + taken map (agent A) \[DATA\] · 2026-11-16 (local file — lost in a container reset)
- \[S44\] [https://www.reddit.com/r/ADHDparenting/comments/1w4cdr4/bedwetting\_alarms\_are\_they\_really\_helpful/](https://www.reddit.com/r/ADHDparenting/comments/1w4cdr4/bedwetting_alarms_are_they_really_helpful/) · reddit r/ADHDparenting · 2026-09-01
- \[S45\] [https://www.facebook.com/groups/iepeduc/posts/1531528145700702/](https://www.facebook.com/groups/iepeduc/posts/1531528145700702/) · Facebook group comments · 2026-10-22
- \[S46\] [https://www.reddit.com/r/Autism\_Parenting/comments/1svfpt4/teenager\_still\_bedwetting\_and\_im\_loosing\_my\_mind/](https://www.reddit.com/r/Autism_Parenting/comments/1svfpt4/teenager_still_bedwetting_and_im_loosing_my_mind/) · reddit r/Autism\_Parenting · 2026-04-25
- \[S47\] [https://www.reddit.com/r/Incontinence/comments/1enudtt/](https://www.reddit.com/r/Incontinence/comments/1enudtt/) · reddit r/Incontinence \[OP post\] · 2024-08-09
- \[S48\] [https://www.reddit.com/r/bedwetting/comments/1raffwn/](https://www.reddit.com/r/bedwetting/comments/1raffwn/) · reddit r/bedwetting \[OP post\] · 2026-02-21
- \[S49\] [https://www.youtube.com/watch?v=nWdUeCVpMfo](https://www.youtube.com/watch?v=nWdUeCVpMfo) · YouTube comments · \~2018 (relative date)
- \[S50\] [https://www.reddit.com/r/pottytraining/comments/1c81rhs/12\_year\_old\_wetting\_the\_bed/](https://www.reddit.com/r/pottytraining/comments/1c81rhs/12_year_old_wetting_the_bed/) · reddit r/pottytraining · 2024-04-19
- \[S51\] [https://www.reddit.com/r/Fosterparents/comments/143mz8x/whats\_it\_like\_dealing\_with\_a\_bedwetting\_issue/](https://www.reddit.com/r/Fosterparents/comments/143mz8x/whats_it_like_dealing_with_a_bedwetting_issue/) · reddit r/Fosterparents · 2023-06-07
- \[S52\] [https://www.reddit.com/r/bedwetting/comments/1w9gkx5/seeking\_advice\_for\_11\_year\_old\_boy/](https://www.reddit.com/r/bedwetting/comments/1w9gkx5/seeking_advice_for_11_year_old_boy/) · reddit r/bedwetting · 2026-09-07
- \[S53\] [https://www.reddit.com/r/bedwetting/comments/1uw7onw/](https://www.reddit.com/r/bedwetting/comments/1uw7onw/) · reddit r/bedwetting \[OP post\] · 2026-07-14
- \[S54\] [https://www.reddit.com/r/Parenting/comments/1bdcyxb/](https://www.reddit.com/r/Parenting/comments/1bdcyxb/) · reddit r/Parenting \[OP post\] · 2024-03-13
- \[S55\] [https://www.reddit.com/r/Parenting/comments/15ifxdr/](https://www.reddit.com/r/Parenting/comments/15ifxdr/) · reddit r/Parenting \[OP post\] · 2023-08-04
- \[S56\] [https://www.reddit.com/r/Parenting/comments/1dyihv4/](https://www.reddit.com/r/Parenting/comments/1dyihv4/) · reddit r/Parenting \[OP post\] · 2024-07-08
- \[S57\] [https://www.youtube.com/watch?v=GSL\_BCrBx48](https://www.youtube.com/watch?v=GSL_BCrBx48) · YouTube comments · \~2025 (relative date)
- \[S58\] [https://www.reddit.com/r/AmIOverreacting/comments/1q6p8a1/](https://www.reddit.com/r/AmIOverreacting/comments/1q6p8a1/) · reddit r/AmIOverreacting \[OP post\] · 2026-01-07
- \[S59\] [https://www.reddit.com/r/AskParents/comments/1ba2okz/](https://www.reddit.com/r/AskParents/comments/1ba2okz/) · reddit r/AskParents \[OP post\] · 2024-03-08
- \[S60\] [https://www.reddit.com/r/Parenting/comments/rcjw8v/11\_year\_old\_still\_wets\_the\_bed\_every\_night/](https://www.reddit.com/r/Parenting/comments/rcjw8v/11_year_old_still_wets_the_bed_every_night/) · reddit r/Parenting · 2021-12-09
- \[S61\] [https://www.amazon.com/portal/customer-reviews/srp/-/RJZ35LTNL22X8](https://www.amazon.com/portal/customer-reviews/srp/-/RJZ35LTNL22X8) · Amazon US — "Customers say" excerpt (reliability) — DryEasy (wired clip) \[B00J4HFSWA\] · review date unknown
- \[S62\] [https://www.reddit.com/r/Mommit/comments/1w223p8/are\_we\_normalizing\_bedwetting/](https://www.reddit.com/r/Mommit/comments/1w223p8/are_we_normalizing_bedwetting/) · reddit r/Mommit · 2026-08-30
- \[S63\] [https://www.reddit.com/r/AskParents/comments/l9u8ez/how\_to\_help\_selfesteem\_of\_10\_yo\_bedwetter/](https://www.reddit.com/r/AskParents/comments/l9u8ez/how_to_help_selfesteem_of_10_yo_bedwetter/) · reddit r/AskParents · 2021-02-01
- \[S64\] [https://www.trustpilot.com/reviews/6ae9327c5dec8745be32c58e](https://www.trustpilot.com/reviews/6ae9327c5dec8745be32c58e) · Trustpilot — [unikor.shop](http://unikor.shop) (NightGuard alarm) (reviewer country US) · 2026-11-02
- \[S65\] [https://www.mumsnet.com/talk/potty\_training/3487720-Are-bedwetting-alarms-the-only-way-for-a-healthy-kid-with-primary-nighttime-eneuresis](https://www.mumsnet.com/talk/potty_training/3487720-Are-bedwetting-alarms-the-only-way-for-a-healthy-kid-with-primary-nighttime-eneuresis) · Mumsnet (UK) SNIPPET · date unknown
- \[S66\] [https://www.walmart.com/reviews/product/39233076](https://www.walmart.com/reviews/product/39233076) · Walmart US review — Chummie Elite Bedwetting Alarm, Green · 12/31/2025
- \[S67\] [https://www.amazon.co.uk/dp/B0DNJTYTBN](https://www.amazon.co.uk/dp/B0DNJTYTBN) · Amazon UK /dp/ top review (reviewer in the United States) — Yiisin wrist-strap bedwetting alarm · 7 November 2025
- \[S68\] [https://www.amazon.co.uk/dp/B0GVKMNPB6](https://www.amazon.co.uk/dp/B0GVKMNPB6) · Amazon UK /dp/ top review (reviewer in the United States) — generic wireless wearable alarm BJ03 \[B0GVKMNPB6\] · 28 October 2026
- \[S69\] [https://www.amazon.com/portal/customer-reviews/srp/-/R1Z03Q5Y2YHVR4](https://www.amazon.com/portal/customer-reviews/srp/-/R1Z03Q5Y2YHVR4) · Amazon US — "Customers say" excerpt (loudness) — DryEasy (wired clip) \[B00J4HFSWA\] · review date unknown
- \[S70\] [https://www.amazon.co.uk/dp/B00OX1XEGO](https://www.amazon.co.uk/dp/B00OX1XEGO) · Amazon UK /dp/ top review (reviewer in the United Arab Emirates) — TheraPee (pad + online program, \$299) \[B00OX1XEGO\] · 24 January 2023
- \[S71\] [https://www.trustpilot.com/reviews/69a577028bd5372558b00888](https://www.trustpilot.com/reviews/69a577028bd5372558b00888) · Trustpilot — [oopsieheroes.com](http://oopsieheroes.com) (Oopsie Heroes alarm) (reviewer country AU) · 2026-02-03
- \[S72\] [https://www.amazon.com/portal/customer-reviews/srp/-/RQ75RAFK8UR0Y](https://www.amazon.com/portal/customer-reviews/srp/-/RQ75RAFK8UR0Y) · Amazon US — "Customers say" excerpt (durability) — Shield Max (wired) \[B01LYX8PWW\] · review date unknown
- \[S73\] [https://www.amazon.co.uk/dp/B089B5CZ96](https://www.amazon.co.uk/dp/B089B5CZ96) · Amazon UK /dp/ top review (reviewer in the United States) — Rodger Wireless Bedwetting Alarm Kit · 7 May 2022
- \[S74\] [https://www.netmums.com/coffeehouse/being-mum-794/children-4-11-years-60/1947534-10-year-old-bedwetting-how-much-support.html](https://www.netmums.com/coffeehouse/being-mum-794/children-4-11-years-60/1947534-10-year-old-bedwetting-how-much-support.html) · Netmums (UK) · 2021-06-02
- \[S75\] [https://www.reddit.com/r/Parenting/comments/1v3ut5j/comment/oz6e3ds/](https://www.reddit.com/r/Parenting/comments/1v3ut5j/comment/oz6e3ds/) · reddit r/Parenting · 2026-07-22
- \[S76\] [https://www.trustpilot.com/reviews/6af7d8595f281b48c542b22e](https://www.trustpilot.com/reviews/6af7d8595f281b48c542b22e) · Trustpilot — [trysaphire.com](http://trysaphire.com) (Saphire saffron gummies) (reviewer country US) · 2026-11-13
- \[S77\] [https://www.walmart.com/reviews/product/54263553](https://www.walmart.com/reviews/product/54263553) · Walmart US review — Smart Bedwetting Alarm for Deep Sleepers & Children with Int · 3/5/2026
- \[S78\] [https://www.amazon.com/portal/customer-reviews/srp/-/R2QF5VV77VVLIW](https://www.amazon.com/portal/customer-reviews/srp/-/R2QF5VV77VVLIW) · Amazon US — "Customers say" excerpt (loudness) — Chummie Premium (wired) \[B00A8GF6BO\] · review date unknown
- \[S79\] [https://www.reddit.com/r/australia/comments/1tqox05/comment/ooi30gk/](https://www.reddit.com/r/australia/comments/1tqox05/comment/ooi30gk/) · reddit r/australia (AU) · 2026-05-29
- \[S80\] [https://www.reddit.com/r/ScienceBasedParenting/comments/13tscqu/bed\_wetting\_alarms\_is\_this\_punishment/](https://www.reddit.com/r/ScienceBasedParenting/comments/13tscqu/bed_wetting_alarms_is_this_punishment/) · Reddit r/ScienceBasedParenting (thread title) · —
- \[S81\] [https://www.reddit.com/r/bedwetting/comments/1w9gkx5/](https://www.reddit.com/r/bedwetting/comments/1w9gkx5/) · reddit r/bedwetting \[OP post\] · 2026-09-07
- \[S82\] [https://www.reddit.com/r/AskParents/comments/1heylf2/comment/m27bc5f/](https://www.reddit.com/r/AskParents/comments/1heylf2/comment/m27bc5f/) · reddit r/AskParents · 2024-12-15
- \[S83\] [https://www.trustpilot.com/review/trysaphire.com?stars=1&stars=2](https://www.trustpilot.com/review/trysaphire.com?stars=1&stars=2) · Trustpilot (Saphire) (non-US buyer) · 2026 (date not parsed)
- \[S84\] [https://www.amazon.com/portal/customer-reviews/srp/-/R3N14Q74PD4PZF](https://www.amazon.com/portal/customer-reviews/srp/-/R3N14Q74PD4PZF) · Amazon US "Customers say" excerpt — Wet-Stop3 \[SNIPPET\] · review date unknown
- \[S85\] [https://www.reddit.com/r/Parenting/comments/8hsrlo/does\_anyone\_have\_suggestions\_to\_cure\_bed\_wetting/](https://www.reddit.com/r/Parenting/comments/8hsrlo/does_anyone_have_suggestions_to_cure_bed_wetting/) · reddit r/Parenting SNIPPET · date unknown
- \[S86\] [https://www.amazon.com/portal/customer-reviews/srp/-/R1XA4YPHXMUNY4](https://www.amazon.com/portal/customer-reviews/srp/-/R1XA4YPHXMUNY4) · Amazon US — "Customers say" excerpt (ease of use) — DRI Sleeper Eclipse Wireless \[B004Y5B9AW\] · review date unknown
- \[S87\] [https://www.reddit.com/r/Parenting/comments/1s1moc1/bedwetting\_alarm\_for\_7\_year\_old\_recommendations/](https://www.reddit.com/r/Parenting/comments/1s1moc1/bedwetting_alarm_for_7_year_old_recommendations/) · reddit r/Parenting · 2026-03-23
- \[S88\] [https://www.amazon.co.uk/portal/customer-reviews/srp/-/R2RA6VFS8ODTBI](https://www.amazon.co.uk/portal/customer-reviews/srp/-/R2RA6VFS8ODTBI) · Amazon UK — "Customers say" excerpt (wireless) — DryEasy Pro Wireless (clip + receiver) \[B0CTMP4616\] · review date unknown
- \[S89\] [https://www.amazon.com/portal/customer-reviews/srp/-/R2GNK5D1O7JDX9](https://www.amazon.com/portal/customer-reviews/srp/-/R2GNK5D1O7JDX9) · Amazon US — "Customers say" excerpt (loudness) — Wet-Stop3 (wired clip) \[B006B8U8BG\] · review date unknown
- \[S90\] [https://www.reddit.com/r/Parenting/comments/mepy9s/](https://www.reddit.com/r/Parenting/comments/mepy9s/) · reddit r/Parenting \[OP post\] · 2021-03-27
- \[S91\] [https://www.amazon.com/portal/customer-reviews/srp/-/R1J71XVE2MA2N3](https://www.amazon.com/portal/customer-reviews/srp/-/R1J71XVE2MA2N3) · Amazon US — "Customers say" excerpt (wake-up time) — DryEasy (wired clip) \[B00J4HFSWA\] · review date unknown
- \[S92\] [https://www.amazon.com/portal/customer-reviews/srp/-/R3BJ6QQSFVVXTY](https://www.amazon.com/portal/customer-reviews/srp/-/R3BJ6QQSFVVXTY) · Amazon US — "Customers say" excerpt (wake-up time) — DryEasy (wired clip) \[B00J4HFSWA\] · review date unknown
- \[S93\] [https://www.reddit.com/r/bedwetting/comments/1l3ap5r/my\_kiddo\_finally\_got\_through\_it\_a\_post\_about/](https://www.reddit.com/r/bedwetting/comments/1l3ap5r/my_kiddo_finally_got_through_it_a_post_about/) · reddit r/bedwetting · 2025-06-04
- \[S94\] [https://www.mumsnet.com/talk/childrens\_health/4647394-9-year-old-bedwetting](https://www.mumsnet.com/talk/childrens_health/4647394-9-year-old-bedwetting) · Mumsnet (UK) · 2022-10-03
- \[S95\] [https://www.reddit.com/r/Parenting/comments/1xrfwc5/still\_dealing\_with\_bed\_wetting\_with\_my\_9\_yo/](https://www.reddit.com/r/Parenting/comments/1xrfwc5/still_dealing_with_bed_wetting_with_my_9_yo/) · reddit r/Parenting · 2026-11-09
- \[S96\] [https://www.amazon.com/portal/customer-reviews/srp/-/RFX6Z107HERE5](https://www.amazon.com/portal/customer-reviews/srp/-/RFX6Z107HERE5) · Amazon US — "Customers say" excerpt (value for money) — TheraPee (pad + online program, \$299) \[B00OX1XEGO\] · review date unknown
- \[S97\] [https://www.walmart.com/reviews/product/47711017](https://www.walmart.com/reviews/product/47711017) · Walmart US review — Chummie Premium Bedwetting Alarm, Green · 9/24/2017
- \[S98\] [https://www.amazon.com/portal/customer-reviews/srp/-/R2ZCVSISQ1P3KJ](https://www.amazon.com/portal/customer-reviews/srp/-/R2ZCVSISQ1P3KJ) · Amazon US — "Customers say" excerpt (reliability) — Shield Max (wired) \[B01LYX8PWW\] · review date unknown
- \[S99\] [https://www.reddit.com/r/Parenting/comments/1949od5/](https://www.reddit.com/r/Parenting/comments/1949od5/) · reddit r/Parenting \[OP post\] · 2024-01-11
- \[S100\] [https://www.reddit.com/r/Parenting/comments/1cg1o36/bedwetting\_alarms/](https://www.reddit.com/r/Parenting/comments/1cg1o36/bedwetting_alarms/) · reddit r/Parenting · 2024-04-29
- \[S101\] [https://www.amazon.com/portal/customer-reviews/srp/-/RAYQC1RHEV9VT](https://www.amazon.com/portal/customer-reviews/srp/-/RAYQC1RHEV9VT) · Amazon US — "Customers say" excerpt (effectiveness) — TheraPee (pad + online program, \$299) \[B00OX1XEGO\] · review date unknown
- \[S102\] [https://www.reddit.com/r/AskUK/comments/tbyyr0/](https://www.reddit.com/r/AskUK/comments/tbyyr0/) · reddit r/AskUK (UK) \[OP post\] · 2022-03-11
- \[S103\] [https://www.reddit.com/r/BSA/comments/1e0esji/comment/lcmx3hx/](https://www.reddit.com/r/BSA/comments/1e0esji/comment/lcmx3hx/) · Reddit r/BSA \[SNIPPET\] · 2024-07-11
- \[S104\] [https://www.reddit.com/r/Parenting/comments/1cg1o36/comment/l1t2a79/](https://www.reddit.com/r/Parenting/comments/1cg1o36/comment/l1t2a79/) · reddit r/Parenting · 2024-04-29
- \[S105\] [https://www.trustpilot.com/reviews/6acaf3d1451074744f28b1a3](https://www.trustpilot.com/reviews/6acaf3d1451074744f28b1a3) · Trustpilot — [trysaphire.com](http://trysaphire.com) (Saphire saffron gummies) (reviewer country US) · 2026-07-11
- \[S106\] [https://www.reddit.com/r/AdultBedwetting/comments/1v7kuu9/](https://www.reddit.com/r/AdultBedwetting/comments/1v7kuu9/) · reddit r/AdultBedwetting \[OP post\] · 2026-07-27
- \[S107\] [https://www.reddit.com/r/Parenting/comments/f0bs7p/](https://www.reddit.com/r/Parenting/comments/f0bs7p/) · reddit r/Parenting \[OP post\] · 2020-02-07
- \[S108\] [https://www.reddit.com/r/bedwetting/comments/1w3bpyb/](https://www.reddit.com/r/bedwetting/comments/1w3bpyb/) · reddit r/bedwetting \[OP post\] · 2026-08-31
- \[S109\] [https://www.reddit.com/r/amiwrong/comments/1hpf97o/](https://www.reddit.com/r/amiwrong/comments/1hpf97o/) · reddit r/amiwrong \[OP post\] · 2024-12-30
- \[S110\] [https://www.reddit.com/r/Parenting/comments/14g3e7o/](https://www.reddit.com/r/Parenting/comments/14g3e7o/) · reddit r/Parenting \[OP post\] · 2023-06-22
- \[S111\] local research file — §20 V3 alarm-outcome re-tally (verify script) \[DATA\] · 2026-11-16 (local file — lost in a container reset)
- \[S112\] [https://www.reddit.com/r/ADHDparenting/comments/1g4xmy0/](https://www.reddit.com/r/ADHDparenting/comments/1g4xmy0/) · reddit r/ADHDparenting \[OP post\] · 2024-10-16
- \[S113\] [https://www.walmart.com/reviews/product/5161423881](https://www.walmart.com/reviews/product/5161423881) · Walmart US review — Goodnites Girls Nighttime Bedwetting Underwear · 6/7/2026
- \[S114\] [https://www.reddit.com/r/bedwetting/comments/1l3ap5r/](https://www.reddit.com/r/bedwetting/comments/1l3ap5r/) · reddit r/bedwetting \[OP post\] · 2025-06-04
- \[S115\] [https://www.reddit.com/r/breakingmom/comments/sa4dwk/](https://www.reddit.com/r/breakingmom/comments/sa4dwk/) · reddit r/breakingmom \[OP post\] · 2022-01-22
- \[S116\] [https://www.reddit.com/r/Parenting/comments/1xrfwc5/comment/19sctuzg2jz8i/](https://www.reddit.com/r/Parenting/comments/1xrfwc5/comment/19sctuzg2jz8i/) · reddit r/Parenting · 2026-11-09
- \[S117\] [https://www.reddit.com/r/UKParenting/comments/1n3fsrt/comment/nbebu1v/](https://www.reddit.com/r/UKParenting/comments/1n3fsrt/comment/nbebu1v/) · reddit r/UKParenting (UK) · 2025-08-29
- \[S118\] [https://www.reddit.com/r/AskParents/comments/1heylf2/comment/m28c6lx/](https://www.reddit.com/r/AskParents/comments/1heylf2/comment/m28c6lx/) · reddit r/AskParents · 2024-12-15
- \[S119\] [https://www.reddit.com/r/Parenting/comments/zgruoc/am\_i\_in\_the\_wrong/](https://www.reddit.com/r/Parenting/comments/zgruoc/am_i_in_the_wrong/) · reddit r/Parenting (AU/NZ) · 2022-12-09
- \[S120\] [https://www.mumsnet.com/talk/primary/5324807-year-6-school-residential-11-year-old-still-bed-wetting-at-night-advice-please](https://www.mumsnet.com/talk/primary/5324807-year-6-school-residential-11-year-old-still-bed-wetting-at-night-advice-please) · Mumsnet (UK) · 2025-04-29
- \[S121\] [https://www.reddit.com/r/Parenting/comments/at8lhx/need\_advice\_son\_is\_nearly\_10\_and\_still\_constantly/](https://www.reddit.com/r/Parenting/comments/at8lhx/need_advice_son_is_nearly_10_and_still_constantly/) · reddit r/Parenting · 2019-02-21
- \[S122\] [https://www.reddit.com/r/ADHDparenting/comments/1mmz8q4/older\_adhd\_son\_bedwetting/](https://www.reddit.com/r/ADHDparenting/comments/1mmz8q4/older_adhd_son_bedwetting/) · reddit r/ADHDparenting · 2025-08-11
- \[S123\] [https://www.mumsnet.com/talk/primary/1387764-Bed-wetting-school-residential-trip-need-help](https://www.mumsnet.com/talk/primary/1387764-Bed-wetting-school-residential-trip-need-help) · Mumsnet (UK) · 2012-01-20
- \[S124\] [https://www.reddit.com/r/bedwetting/comments/1r4tbar/](https://www.reddit.com/r/bedwetting/comments/1r4tbar/) · reddit r/bedwetting \[OP post\] · 2026-02-14
- \[S125\] [https://www.reddit.com/r/australia/comments/1tqox05/comment/pe17ear/](https://www.reddit.com/r/australia/comments/1tqox05/comment/pe17ear/) · reddit r/australia (AU) · 2026-10-05
- \[S126\] [https://www.trustpilot.com/reviews/69dca287cf73f6b1b7c4a3cf](https://www.trustpilot.com/reviews/69dca287cf73f6b1b7c4a3cf) · Trustpilot — [dryly.com](http://dryly.com) (Dryly alarm) (reviewer country DK) · 2026-04-08
- \[S127\] [https://www.walmart.com/reviews/product/181427859](https://www.walmart.com/reviews/product/181427859) · Walmart US review — Wet-Detective Incontinence Alert System (pad alarm) · 12/17/2021
- \[S128\] [https://www.reddit.com/r/newcastle/comments/1tqoxvn/comment/oojanz3/](https://www.reddit.com/r/newcastle/comments/1tqoxvn/comment/oojanz3/) · reddit r/newcastle (AU) · 2026-05-29
- \[S129\] [https://www.walmart.com/reviews/product/488464399](https://www.walmart.com/reviews/product/488464399) · Walmart US review — Zest Bedwetting Alarm (Enuresis Alarm) with 8 Tones · 8/12/2022
- \[S130\] [https://www.amazon.com/portal/customer-reviews/srp/-/R38B3THBIY2OR7](https://www.amazon.com/portal/customer-reviews/srp/-/R38B3THBIY2OR7) · Amazon US — "Customers say" excerpt (reliability) — DRI Sleeper Eclipse Wireless \[B004Y5B9AW\] · review date unknown
- \[S131\] [https://www.amazon.com/portal/customer-reviews/srp/-/R3BULHQGOPNQLU](https://www.amazon.com/portal/customer-reviews/srp/-/R3BULHQGOPNQLU) · Amazon US — "Customers say" excerpt (value for money) — DRI Sleeper Eclipse Wireless \[B004Y5B9AW\] · review date unknown
- \[S132\] [https://www.amazon.com/portal/customer-reviews/srp/-/R3N1FL36URKYRJ](https://www.amazon.com/portal/customer-reviews/srp/-/R3N1FL36URKYRJ) · Amazon US — "Customers say" excerpt (effectiveness) — TheraPee (pad + online program, \$299) \[B00OX1XEGO\] · review date unknown
- \[S133\] [https://www.amazon.com/portal/customer-reviews/srp/-/R1FQFL3BJRO440](https://www.amazon.com/portal/customer-reviews/srp/-/R1FQFL3BJRO440) · Amazon US — "Customers say" excerpt (effectiveness) — Wet-Stop3 (wired clip) \[B006B8U8BG\] · review date unknown
- \[S134\] [https://www.amazon.com/portal/customer-reviews/srp/-/R1YJUOCTXYS865](https://www.amazon.com/portal/customer-reviews/srp/-/R1YJUOCTXYS865) · Amazon US — "Customers say" excerpt (value for money) — Wet-Stop3 (wired clip) \[B006B8U8BG\] · review date unknown
- \[S135\] [https://www.reddit.com/r/australia/comments/1tqox05/comment/ooi3mrp/](https://www.reddit.com/r/australia/comments/1tqox05/comment/ooi3mrp/) · reddit r/australia (AU) · 2026-05-29
- \[S136\] [https://www.trustpilot.com/reviews/6a84326ca896604e12188f3a](https://www.trustpilot.com/reviews/6a84326ca896604e12188f3a) · Trustpilot — [oopsieheroes.com](http://oopsieheroes.com) (Oopsie Heroes alarm) (reviewer country TR) · 2026-08-14
- \[S137\] [https://www.trustpilot.com/reviews/6af8da4d86ad98cdeeaa2087](https://www.trustpilot.com/reviews/6af8da4d86ad98cdeeaa2087) · Trustpilot — [unikor.shop](http://unikor.shop) (NightGuard alarm) (reviewer country US) · 2026-11-12
- \[S138\] [https://www.trustpilot.com/reviews/69d0f0b9ad153e40f3234fd3](https://www.trustpilot.com/reviews/69d0f0b9ad153e40f3234fd3) · Trustpilot — [drybuddy.com](http://drybuddy.com) (GB) · 2026-04-01
- \[S139\] [https://www.drugs.com/comments/desmopressin/for-nocturnal-enuresis.html](https://www.drugs.com/comments/desmopressin/for-nocturnal-enuresis.html) · [drugs.com](http://drugs.com) desmopressin reviews (Firecrawl query-extracted text) — Desmopressin (DDAVP) · January 18, 2020
- \[S140\] [https://www.mumsnet.com/talk/am\_i\_being\_unreasonable/5496503-bedwetting-school-residential-help](https://www.mumsnet.com/talk/am_i_being_unreasonable/5496503-bedwetting-school-residential-help) · Mumsnet (UK) · 2026-02-26
- \[S141\] [https://www.reddit.com/r/laundry/comments/1wkc3ft/comment/papmh0k/](https://www.reddit.com/r/laundry/comments/1wkc3ft/comment/papmh0k/) · reddit r/laundry · 2026-09-19
- \[S142\] [https://www.reddit.com/r/AdultBedwetting/comments/1b0e4ml/](https://www.reddit.com/r/AdultBedwetting/comments/1b0e4ml/) · reddit r/AdultBedwetting (non-US spelling) \[OP post\] · 2024-02-26
- \[S143\] [https://www.reddit.com/r/Autism\_Parenting/comments/1svfpt4/](https://www.reddit.com/r/Autism_Parenting/comments/1svfpt4/) · reddit r/Autism\_Parenting \[OP post\] · 2026-04-25
- \[S144\] [https://www.trustpilot.com/reviews/69bc04c2892f1abe2c3c35ea](https://www.trustpilot.com/reviews/69bc04c2892f1abe2c3c35ea) · Trustpilot — [trysaphire.com](http://trysaphire.com) (US) · 2026-03-16
- \[S145\] [https://www.trustpilot.com/reviews/6aaf8e026582d4e9bffb5e3f](https://www.trustpilot.com/reviews/6aaf8e026582d4e9bffb5e3f) · Trustpilot — [trysaphire.com](http://trysaphire.com) (Saphire saffron gummies) (reviewer country GB) · 2026-09-18
- \[S146\] [https://www.trustpilot.com/reviews/6aea7b1abb5deae0215e98d1](https://www.trustpilot.com/reviews/6aea7b1abb5deae0215e98d1) · Trustpilot — [trysaphire.com](http://trysaphire.com) (Saphire saffron gummies) (reviewer country US) · 2026-11-03
- \[S147\] [https://www.reddit.com/r/laundry/comments/1wkc3ft/comment/papym1q/](https://www.reddit.com/r/laundry/comments/1wkc3ft/comment/papym1q/) · reddit r/laundry · 2026-09-19
- \[S148\] [https://www.reddit.com/r/AdultBedwetting/comments/ehst6e/comment/fclmft8/](https://www.reddit.com/r/AdultBedwetting/comments/ehst6e/comment/fclmft8/) · reddit r/AdultBedwetting · 2019-12-31
- \[S149\] local research file — Flesch-Kincaid reading-level tally of the §2C bank \[DATA\] · 2026-11-16 (local file — lost in a container reset)
- \[S150\] [https://www.reddit.com/r/Mommit/comments/1w223p8/are\_we\_normalizing\_bedwetting/](https://www.reddit.com/r/Mommit/comments/1w223p8/are_we_normalizing_bedwetting/) · Reddit r/Mommit (thread title) · —
- \[S151\] local research file — voice-phrase tally of the §2C bank \[DATA\] · 2026-11-16 (local file — lost in a container reset)
- \[S152\] local research file — §20 V3 clean-bank re-tally \[DATA\] · 2026-11-16 (local file — lost in a container reset)
- \[S153\] [https://www.reddit.com/r/Parenting/comments/t1a81t/](https://www.reddit.com/r/Parenting/comments/t1a81t/) · reddit r/Parenting \[OP post\] · 2022-02-25
- \[S154\] [https://www.reddit.com/r/breakingmom/comments/13wvznh/](https://www.reddit.com/r/breakingmom/comments/13wvznh/) · reddit r/breakingmom \[OP post\] · 2023-05-31
- \[S155\] [https://www.reddit.com/r/Parenting/comments/1v3ut5j/daughters\_85\_and\_6\_still\_wet\_the\_bed\_at\_night/](https://www.reddit.com/r/Parenting/comments/1v3ut5j/daughters_85_and_6_still_wet_the_bed_at_night/) · Reddit r/Parenting (thread title) · —
- \[S156\] [https://www.reddit.com/r/AmItheAsshole/comments/q6hav4/aita\_for\_putting\_my\_autiatic\_son\_in\_goodnites/](https://www.reddit.com/r/AmItheAsshole/comments/q6hav4/aita_for_putting_my_autiatic_son_in_goodnites/) · Reddit r/AmItheAsshole (thread title) · —
- \[S157\] [https://www.reddit.com/r/AITAH/comments/127w2g0/aitah\_for\_buying\_my\_daughters\_goodnites\_at\_the/](https://www.reddit.com/r/AITAH/comments/127w2g0/aitah_for_buying_my_daughters_goodnites_at_the/) · Reddit r/AITAH (thread title) · —
- \[S158\] [https://www.reddit.com/r/amiwrong/comments/1gkgfl6/am\_i\_wrong\_for\_insisting\_my\_daughter\_wear\_a\_pull/](https://www.reddit.com/r/amiwrong/comments/1gkgfl6/am_i_wrong_for_insisting_my_daughter_wear_a_pull/) · Reddit r/amiwrong (thread title; template post) · —
- \[S159\] [https://www.reddit.com/r/confession/comments/1k8hne0/i\_lied\_to\_my\_best\_friends\_mom\_about\_wetting\_the/](https://www.reddit.com/r/confession/comments/1k8hne0/i_lied_to_my_best_friends_mom_about_wetting_the/) · Reddit r/confession (thread title) · —
- \[S160\] [https://www.reddit.com/r/Parenting/comments/1unqdje/6yo\_still\_wetting\_the\_bed\_going\_back\_to\_pullups/](https://www.reddit.com/r/Parenting/comments/1unqdje/6yo_still_wetting_the_bed_going_back_to_pullups/) · Reddit r/Parenting (thread title) · —
- \[S161\] [https://www.reddit.com/r/newcastle/comments/1tqoxvn/parents\_bed\_wetting\_alarms\_real\_experiences\_please/](https://www.reddit.com/r/newcastle/comments/1tqoxvn/parents_bed_wetting_alarms_real_experiences_please/) · Reddit r/newcastle (AU, thread title) · —
- \[S162\] thread title "Bedwetting (scouts)" — Reddit, collected by agent B; exact URL not recovered after the container reset · 2026-11-16
- \[S163\] [https://www.reddit.com/r/amiwrong/comments/1g3xwsj/was\_i\_wrong\_for\_celebrating\_my\_older\_daughter/](https://www.reddit.com/r/amiwrong/comments/1g3xwsj/was_i_wrong_for_celebrating_my_older_daughter/) · Reddit r/amiwrong (thread title; template post) · —
- \[S164\] [https://www.reddit.com/r/Parenting/comments/13cr6i7/just\_looking\_for\_support\_bedwetting\_son/](https://www.reddit.com/r/Parenting/comments/13cr6i7/just_looking_for_support_bedwetting_son/) · Reddit r/Parenting (thread title) · —
- \[S165\] [https://www.reddit.com/r/Mommit/comments/1wpgm55/7yo\_bedwetter\_needs\_to\_know\_he\_isnt\_alone/](https://www.reddit.com/r/Mommit/comments/1wpgm55/7yo_bedwetter_needs_to_know_he_isnt_alone/) · Reddit r/Mommit (thread title) · —
- \[S166\] [https://www.reddit.com/r/Parenting/comments/1xtl2vx/bedwetting\_at\_five/](https://www.reddit.com/r/Parenting/comments/1xtl2vx/bedwetting_at_five/) · Reddit r/Parenting (thread title) · —
- \[S167\] [https://www.reddit.com/r/Parenting/comments/ekfo0w/so\_proud\_of\_my\_son\_beating\_bedwetting/](https://www.reddit.com/r/Parenting/comments/ekfo0w/so_proud_of_my_son_beating_bedwetting/) · Reddit r/Parenting (thread title) · —
- \[S168\] [https://www.facebook.com/groups/1855706591377001/posts/4597484970532469/](https://www.facebook.com/groups/1855706591377001/posts/4597484970532469/) · Facebook group SNIPPET · date unknown
- \[S169\] [https://www.reddit.com/r/ADHDparenting/comments/1pbs6jy/bed\_wetting\_help/](https://www.reddit.com/r/ADHDparenting/comments/1pbs6jy/bed_wetting_help/) · reddit r/ADHDparenting · 2025-12-01
- \[S170\] [https://www.reddit.com/r/bedwetting/comments/1ov9r71/](https://www.reddit.com/r/bedwetting/comments/1ov9r71/) · reddit r/bedwetting \[OP post\] · 2025-11-12
- \[S171\] [https://www.reddit.com/r/JUSTNOMIL/comments/vi8ggk/son\_wet\_the\_bed\_mil\_went\_into\_a\_rage/](https://www.reddit.com/r/JUSTNOMIL/comments/vi8ggk/son_wet_the_bed_mil_went_into_a_rage/) · reddit r/JUSTNOMIL · 2022-06-22
- \[S172\] [https://www.reddit.com/r/Parenting/comments/1bdcyxb/comment/kum3v85/](https://www.reddit.com/r/Parenting/comments/1bdcyxb/comment/kum3v85/) · reddit r/Parenting · 2024-03-13
- \[S173\] [https://www.reddit.com/r/laundry/comments/1wkc3ft/](https://www.reddit.com/r/laundry/comments/1wkc3ft/) · reddit r/laundry \[OP post\] · 2026-09-19
- \[S174\] [https://www.rch.org.au/kidsinfo/fact\_sheets/Bedwetting/](https://www.rch.org.au/kidsinfo/fact_sheets/Bedwetting/) · Royal Children's Hospital Melbourne — Kids Health Info \[VERBATIM\] · 2026-11-16
</content>
</page>
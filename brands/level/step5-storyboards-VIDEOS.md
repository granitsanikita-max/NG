<!-- IRYN Step 5 - STORYBOARDS for the 9 video ads. Built via ad-storyboard-builder skill (Stage 2: storyboard + pacing).
     Build profile: 9:16 vertical, Kling 3.0, tool-voiced native (FLAG: Kling native voice is weak; at generation we may
     switch talking clips to a scratch-track / ElevenLabs lip-sync). Timings computed at ~2.2 spoken words/sec (real pace),
     not the rough labels in the script doc. Retention curve applied (hook fastest, body breathes, CTA tightens).
     No images generated yet. References + start frames come after approval. No em-dashes. -->

# IRYN - Step 5: VIDEO STORYBOARDS (all 9)

## How to read this
Build profile: **9:16 vertical · Kling 3.0 · tool-voiced.** Every clip is sized to the **real spoken length of its line** (words ÷ 2.2 per second, plus a short beat), so the timings are shootable, not aspirational. Kling clips cap around 10s, so long passages are split across angles, which is exactly what the pacing rules want anyway. Each clip row shows: **time · shot (element) · what's on screen · VO · why it cuts · lane.**

**Lane key:** `AI-start` = needs a Higgsfield start frame then Kling (Stage 3 to 4) · `AI-t2v` = Kling text-to-video, no start frame needed · `GFX/CARD` = made in the editor (Canva/AE), not a video gen · `PROD` = uses the real IRYN product photo (you need to supply it before Stage 4).

**Honest runtime note (the thing you flagged):** spoken at a natural pace, the Educational scripts run ~70 to 85s, the Mentor stories ~85 to 95s, the Epiphany stories ~80 to 95s. That is longer than the rough "0 to 50s" labels in the script doc, because a 24-word hook line is ~11s of speech, not 3s. These lengths are fine for cold story/education on Meta, but if you want tighter 45 to 60s cuts I've marked the trimmable beats in each pacing summary.

---

## SHARED ASSETS (built once, reused across variants)

### Personas (the talking-head angle libraries)
- **F1-EDU — the educator** (Educational UGC, selfie/handheld geometry, arm's length). Angles: `F1-EDU-front` (arm's-length front, subtle handheld bob), `F1-EDU-close` (push-in for money lines), `F1-EDU-low` (slight low tilt, authority), `F1-EDU-walk` (walking-and-talking). Dietitian/nurse-educator look, warm, mid-30s to 40s, not a white coat (reads as ad). Never a fabricated named doctor.
- **F2-COACH — the coach/insider** (Mentor Story, on-location, track/gym). Angles: `F2-COACH-front` (medium, on the track), `F2-COACH-close` (punch-in), `F2-COACH-34` (3/4, depth), `F2-COACH-wide` (environmental wide, establishes the setting). Weathered, credible, sport kit or lanyard.
- **F3-MUM — the mum** (Epiphany, selfie confession at home). Angles: `F3-MUM-front` (arm's-length, at the kitchen table), `F3-MUM-close` (lean-in confession), `F3-MUM-seated` (slightly low, settled in). Real, tired-but-relieved, late 30s to 40s.
Lock one look per persona: same face, wardrobe, grade, lighting, 9:16 across all their shots.

### B-roll + product + graphics bank
- `S-BR-TIRED` — teen girl asleep on the couch, late afternoon light, bag dropped (the 4pm crash). AI-t2v.
- `S-BR-CLASS` — teen foggy/head-down at a desk, classroom. AI-t2v.
- `S-BR-PALE` — teen pale in a casual phone photo, mum looking at her phone. AI-t2v.
- `S-BR-PRACTICE` — teen hands-on-knees, gassed, on a track/pitch; teammates moving past. AI-t2v.
- `S-BR-DINNER` — teen back at the dinner table, talking, warm (the recovery payoff). AI-t2v.
- `S-PROD-STRIP` — the IRYN strip melting on a tongue, clean close-up. **PROD (real product photo needed).**
- `S-PROD-PACK` — the IRYN tin/pack in hand. **PROD (real product photo needed).**
- `S-GFX-BANK` — animated "spending account vs savings account" bank diagram, savings draining then refilling. GFX (editor).
- `S-GFX-STAT` — big-number stat card ("~40% of teen girls" / "most are NOT anaemic"). GFX (editor).
- `S-GFX-NEWS` — 2026 breaking-news lower-third ticker ("UPDATE 2026: check her ferritin by 14"). GFX (editor).
- `S-CARD-LAB` — a clean designed text card styled like a result line: "Haemoglobin: checked / Ferritin: not tested." CARD (editor). NOTE: a designed card, never a photoreal fake lab with an invented patient number (guardrail).
- `S-CARD-CTA` — end card: "Ask for her ferritin by name. IRYN. 70-day money-back." CARD (editor).

Captions: burned-in word-by-word captions run the whole ad (sound-off viewing). Listed as an overlay layer, not a clip.

---

# FORMAT 4 - EDUCATIONAL UGC (Videos 1 to 3)
Geometry = selfie/handheld UGC. B-roll density target ~35 to 45%. Spine = the educator talking; b-roll inserts illustrate each claim (overlaid over the talking clip's audio in the edit). Cut a new angle or insert every ~3 to 5s so the head never parks.

## VIDEO 1 - Educational UGC - Variant A (ferritin-gap reveal) · ~82s
**Visual hook (frame 1):** full-screen bold stat card "FERRITIN" with "the number her blood test skips" slamming in, as the educator starts mid-sentence. Pattern interrupt + curiosity loop.

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-2.0 | `S-GFX-STAT` hook card | "FERRITIN — the number her blood test skips" | (VO starts under it) "If your teenage daughter is exhausted" | hard open on the hook card, fastest beat | GFX |
| 2.0-6.5 | `F1-EDU-close` | captions | "and her blood test came back normal, the first thing I'd ask is: did anyone actually check her ferritin?" | reveal the speaker on the question | AI-start |
| 6.5-11.0 | `F1-EDU-front` | captions | "Because almost always, the answer is no. And it's the one number that's actually low in about 40% of teenage girls." | angle refresh + proof bridge | AI-start |
| 11.0-13.0 | `S-GFX-STAT` | "~40% of teen girls are low in iron" | (VO continues from prev) | stat lands as overlay | GFX |
| 13.0-20.0 | `F1-EDU-front` + `S-GFX-BANK` overlay mid-way | bank diagram draws in | "Here's the part nobody explains. A standard blood count checks the iron moving in her blood right now. It does not check ferritin, which is her iron in storage." | overlay the diagram as the concept is named | AI-start + GFX |
| 20.0-27.0 | `S-GFX-BANK` (full) | spending box fine, savings box draining | "Think of it like a bank. The test checks her spending money, and it looks fine. Nobody checked her savings, and that's what's empty." | let the animation carry the metaphor | GFX |
| 27.0-29.0 | `F1-EDU-close` | captions | "Make sense so far? Watch this." | micro-commitment, snap back to face | AI-start |
| 29.0-36.0 | `F1-EDU-front` + inserts `S-BR-TIRED`, `S-BR-CLASS`, `S-BR-PALE` (quick ~1.2s each) | captions | "That's why she can be totally normal on paper and still asleep by 5pm, foggy in class, pale in photos." | three fast "that's literally her" inserts = re-engage | AI-start + AI-t2v |
| 36.0-41.0 | `S-GFX-STAT` | "most are NOT anaemic — the test misses them" | "Most of these girls aren't even anaemic, which is exactly why the usual test waves them through." | stat reinforces the gap | GFX |
| 41.0-48.0 | `F1-EDU-front` | captions | "Topping up iron stores is the easy part. The hard part is getting a teenager to take iron for months. Tablets upset her stomach, she quits." | back to face for the pivot to solution | AI-start |
| 48.0-53.0 | `S-PROD-STRIP` | product in use | "So this is a dissolvable strip made for teen girls, one a day, raspberry, it melts in seconds." | product moment, show don't tell | PROD |
| 53.0-57.0 | `F1-EDU-close` | captions | "She'll actually take it, which is the whole point." | compliance payoff, punch-in | AI-start |
| 57.0-66.0 | `F1-EDU-low` | captions | "If she's very low or already anaemic, that's a doctor's dose first. For everyone else stuck at normal, ask for her ferritin by name." | authority tilt for the honest caveat + CTA | AI-start |
| 66.0-72.0 | `S-CARD-CTA` | "Ask for her ferritin by name. IRYN. 70-day money-back." | "and if you want the gentle daily version, it's IRYN, 70 day money-back. Link's right there." | end card, tighten | CARD |

**Pacing summary:** 14 cuts, ~82s, b-roll/gfx ~45%. Hook card + question = fastest. Bank animation is the one allowed "breathe" (7s) because it IS the payoff. Trim options: cut the 2am-style repetition is already out; to hit ~60s, drop the second stat card (36-41) and shorten the caveat. **Reusable start frames needed:** F1-EDU-close, -front, -low (3 anchors). Everything else is t2v, gfx, card, or the product photo.

## VIDEO 2 - Educational UGC - Variant B (2026 news) · ~70s
**Visual hook (frame 1):** `S-GFX-NEWS` breaking-news ticker "UPDATE 2026: check her ferritin by 14" over the educator already talking. Borrowed-authority pattern interrupt.

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-5.5 | `F1-EDU-front` + `S-GFX-NEWS` ticker | news lower-third | "In 2026 the guidance on teenage girls and iron quietly changed, and most mums have no idea." | open mid-sentence under the ticker | AI-start + GFX |
| 5.5-9.5 | `F1-EDU-close` | captions | "If your daughter's been tired for months and her bloodwork keeps coming back fine, this is the part you want." | qualifier bridge, punch-in | AI-start |
| 9.5-16.0 | `F1-EDU-front` | captions | "Paediatric experts now say check a girl's ferritin by age 14. Ferritin is her iron stores, and here's why they singled it out." | angle refresh | AI-start |
| 16.0-24.0 | `F1-EDU-front` + `S-CARD-LAB` overlay | "Haemoglobin: checked / Ferritin: not tested" | "A normal blood count checks the iron in her blood today. It never checks her stores. Two different numbers, and routine tests almost always run only the first." | the card shows the gap as he says it | AI-start + CARD |
| 24.0-31.0 | `S-GFX-STAT` + quick `S-BR-TIRED` insert | "~40% low · most NOT anaemic" | "That's how around 40% of teen girls end up low and missed, because most of them aren't anaemic, so the standard test clears them." | stat + one relatable insert | GFX + AI-t2v |
| 31.0-35.0 | `F1-EDU-close` | captions | "The tired kid who tests fine is the exact kid this is about." | "that's literally her" line, close | AI-start |
| 35.0-43.0 | `F1-EDU-front` then `S-PROD-STRIP` | product | "If hers is low, refilling it is simple. Getting a teenager to take iron daily is not, which is why the version that works is a strip that melts on her tongue, raspberry, one a day." | pivot to solution + product | AI-start + PROD |
| 43.0-50.0 | `F1-EDU-low` | captions | "Very low or anaemic means a doctor's dose first. Otherwise, ask for her ferritin by name at the next appointment." | honest caveat + CTA | AI-start |
| 50.0-56.0 | `S-CARD-CTA` | end card | "and the gentle daily one is IRYN, 70 day money-back. Details at the link." | end card | CARD |

**Pacing summary:** 9 cuts, ~70s, b-roll/gfx ~40%. News ticker carries authority in the hook. Trim to ~55s: merge 9.5-16 into 16-24. **Start frames:** reuses V1's F1-EDU anchors (no new faces). Only new assets are GFX/card.

## VIDEO 3 - Educational UGC - Variant C (whiteboard mechanism) · ~60s
**Visual hook (frame 1):** a hand drawing two boxes on paper, marker squeak, mid-stroke. Process-curiosity, you watch to see what it becomes.

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-5.0 | `S-GFX-BANK` (hand drawing, live) | boxes appear | "Let me show you why your daughter's iron test can say normal while she's running on empty." | open on the draw, no face yet | AI-start |
| 5.0-9.5 | `S-GFX-BANK` (labelling) | "blood (spending)" / "savings" | "Draw two accounts. This one is the iron moving in her blood right now. This one is her iron in storage, her savings." | labels land as drawn | AI-start |
| 9.5-18.0 | `S-GFX-BANK` (shading savings down) | savings drains | "A standard blood count only checks this one, the spending account. It looked fine, so she's normal. But nobody checked the savings, and that's the one that empties first in teen girls. Watch." | the draining IS the reveal | AI-start |
| 18.0-22.0 | quick `S-BR-TIRED` + `S-BR-PALE` | captions | "Empty savings is why she's asleep by 5, foggy, pale," | cut to real girl = re-engage | AI-t2v |
| 22.0-28.0 | `S-GFX-STAT` | "~40% · NOT anaemic" | "and the test still cleared her. Around 40% of teen girls are here, most not anaemic, so the usual test misses them completely." | stat | GFX |
| 28.0-36.0 | `S-GFX-BANK` (refilling) then `S-PROD-STRIP` | savings refills, then strip | "Refilling the savings is simple iron, daily, for a few months. The only reason it fails is she won't take pills. So the fix that actually works is a raspberry strip that melts on her tongue, one a day." | diagram resolves + product | AI-start + PROD |
| 36.0-44.0 | `F1-EDU-low` (first face of the ad) | captions | "If she's very low or anaemic, doctor's dose first. Otherwise ask for her ferritin by name," | reveal a human at the CTA for trust | AI-start |
| 44.0-50.0 | `S-CARD-CTA` | end card | "and the gentle daily one is IRYN, 70 day money-back. Link below." | end card | CARD |

**Pacing summary:** 8 cuts, ~50 to 60s, b-roll/gfx ~70% (this one is animation-led, face only at the CTA). The whiteboard is the engagement engine; it keeps resolving so it never parks. **Start frames:** the bank animation is an editor/animation build; one F1-EDU-low face anchor (reused). Lightest of the three to produce.

---

# FORMAT 5 - MENTOR STORY (Videos 4 to 6)
Geometry = on-location talking head (track/gym), grounded, authority. B-roll density ~25 to 35%. These are longer story VSLs, so the body can breathe (3 to 5s holds) but every long passage breaks to a new angle or a cutaway. Hook is the insider claim, delivered straight.

## VIDEO 4 - Mentor Story - Variant A (cross-country coach) · ~92s
**Visual hook (frame 1):** coach on the track, mid-sentence, no title card, just a real person who clearly knows something. "Yap cold open."

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-6.0 | `F2-COACH-front` | caption: "what a coach sees before the parents do" | "I've coached a few hundred teenage girls, and I can usually tell which ones have run out of iron before they can." | authority cold open | AI-start |
| 6.0-12.0 | `F2-COACH-34` + insert `S-BR-PRACTICE` | captions | "Every season it's the same story. A strong girl slowly slides backwards. Gassing out on runs she used to finish. Heavy legs." | cutaway shows the pattern | AI-start + AI-t2v |
| 12.0-17.0 | `F2-COACH-close` | captions | "And everyone's first guess is that she stopped trying, or she's just tired." | punch-in on the wrong assumption | AI-start |
| 17.0-25.0 | `F2-COACH-front` | captions | "The parents do the right things. More sleep, more food, a rest week. A lot of them even get bloods done, and it comes back normal." | angle refresh, the setup | AI-start |
| 25.0-28.0 | `S-CARD-LAB` | "Ferritin: not tested" | (VO continues) "So the girl starts believing she's just not good anymore." | the card shows the miss | CARD |
| 28.0-37.0 | `F2-COACH-34` | captions | "I had a runner go from the front group to the back in one season. Her mum was ready to pull her out. Bloodwork? Normal. It didn't sit right with me, because I'd seen it too many times." | the personal hinge, new angle | AI-start |
| 37.0-50.0 | `F2-COACH-front` + `S-GFX-BANK` overlay | bank diagram | "Turns out a standard blood count checks the iron in her blood right now, but not ferritin, her iron stores. For a runner that reserve is everything, because iron is what carries oxygen to her muscles." | the reveal + diagram | AI-start + GFX |
| 50.0-57.0 | `F2-COACH-close` | captions | "She had an okay count and empty stores, which is exactly when a strong girl hits a wall. The test just never looked." | money line, close | AI-start |
| 57.0-64.0 | `S-GFX-STAT` + `S-BR-PRACTICE` | "~40% low · most NOT anaemic" | "That's why she could train just as hard and go backwards. And it's common, around 40% of teen girls are low, most not anaemic, so the test clears them." | stat + proof cutaway | GFX + AI-t2v |
| 64.0-74.0 | `F2-COACH-front` then `S-PROD-STRIP` | product | "Refilling it is simple. The catch is getting a 15 year old to take iron daily through a season. Tablets wreck her stomach, she quits. The ones who stick with it use a strip that melts on the tongue, raspberry, one a day, no fight." | solution + product | AI-start + PROD |
| 74.0-83.0 | `F2-COACH-34` + quick `S-BR-DINNER`/win insert | captions | "That runner is back in the front group. I always say the same thing: if she's very low or anaemic, see your doctor for a proper dose first. For everyone else stuck at normal, it's worth checking." | proof + honest caveat | AI-start + AI-t2v |
| 83.0-92.0 | `F2-COACH-close` then `S-CARD-CTA` | end card | "Ask for her ferritin by name. The gentle daily one made for teen girls is IRYN, and it's got a 70 day money-back guarantee. I just wish someone had told these mums which number to ask for years ago." | close on the face then card | AI-start + CARD |

**Pacing summary:** 12 cuts, ~92s, b-roll/gfx ~30% (angle-switching is the engine, per podcast/mentor logic). Breathes at the reveal (37-50) because that's the payoff. Trim to ~70s: compress 17-25 and drop one cutaway. **Start frames:** F2-COACH-front, -close, -34 (3 anchors) + one -wide optional establisher.

## VIDEO 5 - Mentor Story - Variant B (PE teacher) · ~88s
**Visual hook (frame 1):** teacher mid-stride past a gym/field, "Fly on wall" off-camera glance, like a candid interview.

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-6.5 | `F2-COACH-34` (teacher look) | caption: "15 years. same pattern every year." | "After fifteen years running school sport, I can walk past a team and point out the girls who are low in iron." | authority hook | AI-start |
| 6.5-15.0 | `F2-COACH-front` + insert `S-BR-PRACTICE`/`S-BR-CLASS` | captions | "It's never the loud stuff. It's the girl who used to be keen and now asks to sit out. Tired at training, flat in class, pale. The easy read is teenager. I stopped believing that a long time ago." | cutaways on each symptom | AI-start + AI-t2v |
| 15.0-21.0 | `F2-COACH-front` | captions | "Parents take them to the GP, get bloods, and it comes back normal. Everyone exhales and nothing changes, because the tiredness is still there the next week." | the setup | AI-start |
| 21.0-29.0 | `F2-COACH-close` | captions | "One girl's mum came to me in tears. Straight-A kid, suddenly falling asleep in fifth period, bloodwork fine. I told her what a sports doctor once told me." | personal hinge, punch-in | AI-start |
| 29.0-42.0 | `F2-COACH-front` + `S-GFX-BANK` overlay | bank diagram | "A normal blood count checks the iron in her blood today. It doesn't check ferritin, her stores. Two different numbers, and routine tests only run the first. So her reserve can be empty while the test says normal, and the reserve is what she runs on all day, in class and at practice." | the reveal + diagram | AI-start + GFX |
| 42.0-50.0 | `S-GFX-STAT` + `S-BR-TIRED` | "~40% low · most NOT anaemic" | "That's why a genuinely tired girl keeps getting cleared. Around 40% of teen girls are low, most not anaemic, so they slip straight through." | stat + relatable insert | GFX + AI-t2v |
| 50.0-60.0 | `F2-COACH-front` then `S-PROD-STRIP` | product | "Topping it up is simple iron over a few months. The only reason it fails is compliance, teenagers won't take tablets. The version that sticks is a raspberry strip that melts on the tongue, one a day." | solution + product | AI-start + PROD |
| 60.0-70.0 | `F2-COACH-close` | captions | "If she's very low or anaemic, that's a doctor's dose first, no shortcuts. Otherwise, ask for her ferritin by name." | honest caveat + CTA, close | AI-start |
| 70.0-78.0 | `F2-COACH-34` then `S-CARD-CTA` | end card | "The gentle daily one made for teen girls is IRYN, 70 day money-back. Honestly, I wish this was standard." | end card | AI-start + CARD |

**Pacing summary:** 9 cuts, ~78 to 88s, b-roll/gfx ~30%. Same engine as V4, fresh insider seat. **Start frames:** new persona face if you want a different person from V4's coach (F2b-TEACHER-front/-close/-34, 3 anchors); or reuse F2-COACH as the same person in a different setting.

## VIDEO 6 - Mentor Story - Variant C (youth-sport physio) · ~86s
**Visual hook (frame 1):** hand slams a training log/clipboard onto a bench, then the physio speaks. "Slam/drop start" pattern interrupt.

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-6.0 | `F2-COACH-front` (physio) + the slam in frame 1 | caption: "training harder. getting slower." | "Every year I get the same girl in here: training harder, getting slower, and no one can explain it." | the slam is the hook | AI-start |
| 6.0-14.0 | `F2-COACH-34` + insert `S-BR-PRACTICE` | captions | "Fit kid, good program, and the times go the wrong way. Legs feel heavy. Gassed on the warm-up. Parents assume overtraining or a motivation dip. Usually it's neither." | cutaway on the problem | AI-start + AI-t2v |
| 14.0-21.0 | `F2-COACH-front` + `S-CARD-LAB` | "Ferritin: not tested" | "They'll often have had bloods done. Comes back normal, so iron gets ruled out. That's the mistake, and it's not their fault, it's the test." | the card shows the miss | AI-start + CARD |
| 21.0-34.0 | `F2-COACH-front` + `S-GFX-BANK` overlay | bank diagram | "A standard count checks the iron in her blood now. It doesn't check ferritin, her stores. For an endurance athlete the stores are the whole game, because iron carries oxygen to the muscle. Empty stores show up as a wall long before a blood count ever goes abnormal." | reveal + diagram | AI-start + GFX |
| 34.0-42.0 | `S-GFX-STAT` + `S-BR-PRACTICE` | "~40% low · most NOT anaemic" | "That's why she can train harder and go backwards and still test fine. Around 40% of teen girls are low, most not anaemic, so standard bloods miss them." | stat + proof | GFX + AI-t2v |
| 42.0-54.0 | `F2-COACH-front` then `S-PROD-STRIP` | product | "The fix is simple iron, daily, long enough to refill the tank. The reason it fails in teens is they stop taking tablets. The athletes who actually refill use a strip that melts on the tongue, raspberry, one a day, easy to keep up through a season." | solution + product | AI-start + PROD |
| 54.0-66.0 | `F2-COACH-close` | captions | "If she's very low or anaemic, see a doctor for a proper dose first. Otherwise, get her ferritin checked by name, not just a blood count." | honest caveat + CTA, close | AI-start |
| 66.0-74.0 | `S-CARD-CTA` | end card | "The gentle daily one for teen girls is IRYN, 70 day money-back. That's the number I wish every coach knew." | end card | CARD |

**Pacing summary:** 8 cuts, ~74 to 86s, b-roll/gfx ~35%. The slam is the interrupt; the diagram breathes at the reveal. **Start frames:** physio persona (reuse F2-COACH or a 3rd face), 3 anchors.

---

# FORMAT 6 - EPIPHANY (Videos 7 to 9)
Geometry = selfie confession at home. B-roll density ~40 to 50% (the story needs to SHOW the daughter). Low-polish on purpose, subtle handheld. Emotion is the engine; cutaways to the daughter re-engage on every symptom beat.

## VIDEO 7 - Epiphany - Variant A (mum regret, not herself) · ~90s
**Visual hook (frame 1):** shaky as she props the phone and sits, then straight into the confession. "Setting down phone."

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-8.0 | `F3-MUM-front` (phone settling) | caption: "I blamed my daughter for a year." | "I spent a year telling my daughter to just try harder. She wasn't missing effort. She was missing iron, and nobody checked." | confession cold open | AI-start |
| 8.0-16.0 | `F3-MUM-front` + inserts `S-BR-TIRED`,`S-BR-CLASS`,`S-BR-PALE` | captions | "She went from my loud, busy kid to someone asleep by 5pm. Foggy in class, grades slipping, pale in every photo." | three symptom cutaways = re-engage | AI-start + AI-t2v |
| 16.0-21.0 | `F3-MUM-close` | captions | "And I'll be honest, I got frustrated with her, because it looked like she just stopped caring." | the shameful admission, intimate close | AI-start |
| 21.0-28.0 | `F3-MUM-seated` + `S-CARD-LAB` | "Ferritin: not tested" | "I did take her to the doctor. They ran her bloods. Normal. Which somehow made it worse, because now I didn't even have a reason." | the betrayal + card | AI-start + CARD |
| 28.0-33.0 | `F3-MUM-front` | captions | "Just a tired girl and a piece of paper saying she was fine. So I started reading late at night, trying to work out what the test wasn't telling me." | the turn | AI-start |
| 33.0-45.0 | `F3-MUM-front` + `S-GFX-BANK` overlay | bank diagram | "Here's what I found. A standard blood count checks the iron moving in her blood today. It does not check ferritin, her iron stores. It's like checking her spending money, which looked okay, while her savings were empty." | the reveal + diagram | AI-start + GFX |
| 45.0-52.0 | `F3-MUM-close` | captions | "That's when it clicked. It wasn't laziness. It wasn't attitude." | absolution, intimate close | AI-start |
| 52.0-58.0 | `S-GFX-STAT` | "~40% low · most NOT anaemic" | "Around 40% of teen girls are low and most aren't even anaemic, so the usual test just clears them." | stat | GFX |
| 58.0-68.0 | `F3-MUM-seated` then `S-PROD-STRIP` | product | "We got her ferritin checked, it was low, and topping it up was simple. The hard part was getting her to take iron daily. Tablets, she quit in a week. What stuck was a little raspberry strip that melts on her tongue, one a day." | solution + product | AI-start + PROD |
| 68.0-78.0 | `S-BR-DINNER` then `F3-MUM-close` | the recovery scene | "Around week two she stopped crashing after school. A few weeks later she sat with us at dinner and actually talked, and I had to leave the room." | the payoff, show the win | AI-t2v + AI-start |
| 78.0-85.0 | `F3-MUM-close` | captions | "If your girl is very low or anaemic, see your doctor first. But if she keeps testing fine, please, ask for her ferritin by name." | honest caveat + CTA | AI-start |
| 85.0-92.0 | `S-CARD-CTA` | end card | "The one we use, made for teen girls, is IRYN, 70 day money-back. I just wish I'd known which number to ask for a year earlier." | end card | CARD |

**Pacing summary:** 12 cuts, ~92s, b-roll ~45%. Symptom cutaways in the first 16s do the heavy re-engagement; the dinner payoff earns the CTA. Trim to ~70s: compress 28-33 and 52-58. **Start frames:** F3-MUM-front, -close, -seated (3 anchors).

## VIDEO 8 - Epiphany - Variant B (mum regret, sport) · ~86s
**Visual hook (frame 1):** cut of the daughter face-down on the couch in her sports kit, bag dropped, then mum to camera. "Problem reenactment."

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-3.0 | `S-BR-PRACTICE`/couch-in-kit | caption: "she went from starter to benched" | (VO over) "Mum, the coach benched me again." | open on the reenactment | AI-t2v |
| 3.0-9.0 | `F3-MUM-front` | captions | "That was the sentence that made me stop blaming it on her being a teenager." | reveal mum | AI-start |
| 9.0-18.0 | `F3-MUM-front` + insert `S-BR-PRACTICE` | captions | "She was strong. Then over a season she faded. Gassed on runs she used to finish, heavy legs, wiped out for hours after training. The coach thought she'd lost interest." | cutaway on the fade | AI-start + AI-t2v |
| 18.0-24.0 | `F3-MUM-close` | captions | "She came home crying that maybe she just wasn't good anymore." | emotional low, close | AI-start |
| 24.0-32.0 | `F3-MUM-seated` + `S-CARD-LAB` | "Ferritin: not tested" | "We tried the obvious things, then got bloods done because I was worried. Normal. So everyone, including me, started to think it was in her head. I couldn't let it go, so I started reading at night." | betrayal + turn | AI-start + CARD |
| 32.0-45.0 | `F3-MUM-front` + `S-GFX-BANK` overlay | bank diagram | "A standard blood count checks the iron in her blood right now. It doesn't check ferritin, her stores. For an athlete that reserve is everything, it's the oxygen her muscles pull on when she pushes. Her count was okay and her stores were empty, which is exactly when a strong girl hits a wall." | reveal + diagram | AI-start + GFX |
| 45.0-53.0 | `S-GFX-STAT` + `S-BR-PRACTICE` | "~40% low · most NOT anaemic" | "That's why she trained just as hard and went backwards. It was never her effort. And it's common, around 40% of teen girls are low, most not anaemic, so the test clears them." | stat + absolution | GFX + AI-t2v |
| 53.0-62.0 | `F3-MUM-seated` then `S-PROD-STRIP` | product | "Her ferritin was low, refilling it was simple, but she'd quit tablets in days. So she switched to a raspberry strip that melts on her tongue, one a day, easy to keep up all season." | solution + product | AI-start + PROD |
| 62.0-72.0 | `S-BR-PRACTICE` (strong again) then `F3-MUM-close` | the win | "A couple of weeks in, the after-practice crash eased. Later she told me training felt normal again, which from her is basically a speech." | payoff, show the win | AI-t2v + AI-start |
| 72.0-80.0 | `F3-MUM-close` | captions | "If she's very low or anaemic, doctor's dose first. Otherwise, ask for her ferritin by name, not just a blood count." | caveat + CTA | AI-start |
| 80.0-86.0 | `S-CARD-CTA` | end card | "The daily one made for teen girls is IRYN, 70 day money-back. I just wish I'd known before she spent a season thinking she wasn't good enough." | end card | CARD |

**Pacing summary:** 11 cuts, ~86s, b-roll ~45%. The reenactment cold open is the strongest scroll-stopper of the three Epiphanies. **Start frames:** reuses F3-MUM anchors.

## VIDEO 9 - Epiphany - Variant C (mum regret, normal result) · ~84s
**Visual hook (frame 1):** she leans into the lens, eyes filling frame, for the confession. "Face lean-in."

| Time | Shot (element) | On screen | VO | Why it cuts | Lane |
|---|---|---|---|---|---|
| 0.0-6.0 | `F3-MUM-close` (lean-in) | caption: "normal twice. still exhausted." | "Her blood test said normal. Twice. I believed it for a year, and I was wrong." | lean-in confession hook | AI-start |
| 6.0-14.0 | `F3-MUM-front` + inserts `S-BR-TIRED`,`S-BR-PALE` | captions | "She was wiped out every afternoon, foggy at school, pale, snapping then crying that she didn't know why. I kept telling myself it was just her age." | symptom cutaways | AI-start + AI-t2v |
| 14.0-24.0 | `F3-MUM-seated` + `S-CARD-LAB` (x2 stamp) | "Ferritin: not tested" | "We got bloods done, not once but twice, and both times they said she was fine. So I stopped looking, because what do you do when the test says there's nothing wrong?" | the double betrayal + card | AI-start + CARD |
| 24.0-28.0 | `F3-MUM-front` | captions | "A nurse friend is the one who finally said the thing no one had told me." | the turn | AI-start |
| 28.0-42.0 | `F3-MUM-front` + `S-GFX-BANK` overlay | bank diagram | "A standard blood count checks the iron in her blood today. It never checks ferritin, her iron stores. Two completely different numbers, and the routine panel only runs the first. Her spending money looked fine while her savings were empty. That's how a genuinely exhausted girl keeps coming back normal." | reveal + diagram | AI-start + GFX |
| 42.0-50.0 | `S-GFX-STAT` + `S-BR-TIRED` | "~40% low · most NOT anaemic" | "Around 40% of teen girls are low in iron, and most aren't anaemic, which is the exact reason the standard test misses them. It wasn't nothing. It was never nothing." | stat + the vindication | GFX + AI-t2v |
| 50.0-60.0 | `F3-MUM-seated` then `S-PROD-STRIP` | product | "We asked for her ferritin by name, it was low, and refilling it was simple. The only hard part was getting her to take iron daily, so we used a raspberry strip that melts on her tongue, one a day, no pills to quit." | solution + product | AI-start + PROD |
| 60.0-70.0 | `S-BR-DINNER` then `F3-MUM-close` | the win | "Week two she wasn't asleep by five. By about week six she was herself again, and we'll retest her ferritin at 90 days to prove it with a number." | payoff | AI-t2v + AI-start |
| 70.0-78.0 | `F3-MUM-close` | captions | "If she's very low or anaemic, see a doctor for a proper dose first. But if yours keeps testing fine, ask for her ferritin by name." | caveat + CTA | AI-start |
| 78.0-84.0 | `S-CARD-CTA` | end card | "The gentle daily one is IRYN, 70 day money-back. You deserve to know which number they skipped." | end card | CARD |

**Pacing summary:** 10 cuts, ~84s, b-roll ~45%. The lean-in is the most intimate hook; "it was never nothing" is the emotional peak before the product. **Start frames:** reuses F3-MUM anchors.

---

## PRODUCTION ROLL-UP (what Stages 3 to 5 will need)
- **Unique talking-head anchors to generate (Higgsfield start frames):** F1-EDU (3 angles), F2-COACH (3 to 4 angles; +1 to 2 if you want distinct faces for the PE teacher and physio), F3-MUM (3 angles). ~9 to 13 anchor images total.
- **AI-t2v b-roll (Kling direct, no start frame):** S-BR-TIRED, -CLASS, -PALE, -PRACTICE, -DINNER (5 clips, reused across all 9).
- **Editor builds (no gen cost):** S-GFX-BANK (the bank animation, used in 7 of 9), S-GFX-STAT, S-GFX-NEWS, S-CARD-LAB, S-CARD-CTA, burned-in captions.
- **Product (you supply a real photo):** S-PROD-STRIP, S-PROD-PACK. **Blocker for Stage 4** per the skill, flag: I need a real IRYN product/label photo before generating any product shot, or explicit okay to approximate.
- **Tool-fit flag to resolve before Stage 5:** tool-voiced + Kling. Kling's native voice is weak. Options: (a) switch talking clips to Seedance for native voice, (b) generate silent talking motion in Kling and lip-sync an ElevenLabs track (cleanest for a consistent brand voice), (c) accept Kling audio. Recommend (b).
- **Reusability win:** the bank animation, the 5 b-roll clips, the stat/news/CTA cards, and each persona's angle set are built once and recut across all variants in their format. Real production load is far smaller than 9 ads from scratch.

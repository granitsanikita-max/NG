<!-- IRYN Step 8 (v2) - Kling 3.0 NATIVE-AUDIO talking-head prompts + credit estimate.
     Build: Kling 3.0, std mode (720p), 9:16, sound ON (avatar speaks), image-to-video from Step 7 start scenes.
     The talking clips carry the FULL narration; b-roll + cards are overlaid on top in the edit. No ElevenLabs. No em-dashes. -->

# IRYN - Step 8 (v2): Kling 3.0 native-audio talking-head prompts + estimate

## Settings (every clip)
- Model **Kling 3.0** · mode **std (= 720p)** · aspect **9:16** · **sound ON** (the avatar speaks the line) · image-to-video.
- Feed the clip's start frame as `start_image`. Kling caps at 15s; every line is chunked under that.
- Cost at these settings: **2.0 credits / second** (10 / 5s, ~30 / 15s).
- Workflow: these talking clips speak the WHOLE script. B-roll (your real teen clips), the stat/bank/lab/news/CTA cards, and the product strip are overlaid ON TOP in editing. That's why some clips below are marked "[overlay: ...]" - the avatar keeps talking underneath.

## Voice lock (keep each persona's voice identical across all their clips)
- **Educator:** warm, calm, knowledgeable American-English female voice, mid-30s.
- **Coach:** grounded, confident American-English female voice, mid-40s.
- **Mum:** warm, sincere, emotional American-English female voice, late 30s.
> If Kling gives an inconsistent voice between clips, regenerate the odd one; or set a fixed voice if your Kling plan exposes a voice picker. Accent set to American for the US test; say the word and I'll switch to Australian.

## Start frames
EDU-front = s-edu-front.png · EDU-close = s-edu-close.png · EDU-low = s-edu-low.png
COACH-gym = s-coach-front-gym.png · COACH-clinic = s-coach-front-clinic.png
MUM-front = s-mum-front.png · MUM-close = s-mum-close.png · MUM-seated = s-mum-seated.png
EDU-hold-tin = s-edu-front-product.png · MUM-hold-tin = s-prod-tin-in-hand.png

## Prompt shape (what every block below already follows)
`Image-to-video, feed {FRAME} as start_image. The exact same woman from the reference image - identical face, hair, wardrobe and background - talks straight to camera in a {voice}. {shot + motion}. She says this line clearly with natural matching lip-sync: "{LINE}" Natural mouth movement, {expression}, natural blink, subtle head movement. No on-screen text or captions. Photorealistic, 9:16.`

---

# FORMAT 4 - EDUCATIONAL UGC

## VIDEO 1 - EDU-A (ferritin-gap reveal)

**V1-C1** · EDU-close · 12s · curious, leaning in
> Image-to-video, feed s-edu-close.png as start_image. The exact same woman from the reference image, identical face, hair, navy blazer over cream top, same kitchen, talks straight to camera in a warm, calm, knowledgeable American-English female voice, mid-30s. Intimate chest-up framing, very slight handheld sway. She says this line clearly with natural matching lip-sync: "If your teenage daughter is exhausted, and her blood test came back normal, the first thing I'd ask is: did anyone actually check her ferritin?" Natural mouth movement, curious engaged expression, natural blink, subtle head movement. No on-screen text or captions. Photorealistic, 9:16.

**V1-C2** · EDU-front · 11s · matter-of-fact
> Image-to-video, feed s-edu-front.png as start_image. Same woman, identical face/hair/navy blazer/kitchen, warm calm knowledgeable American-English female voice. Arm's-length selfie framing, slight handheld sway. She says clearly with natural lip-sync: "Because almost always, the answer is no. And it's the one number that's actually low in about 40% of teenage girls." Natural mouth movement, matter-of-fact expression, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: ~40% stat card at the end]

**V1-C3** · EDU-front · 14s · explaining
> Image-to-video, feed s-edu-front.png as start_image. Same woman, identical look. Arm's-length selfie, slight sway. Clear natural lip-sync: "Here's the part nobody explains. A standard blood count checks the iron moving in her blood right now. It does not check ferritin, which is her iron in storage." Natural mouth movement, explaining expression, small hand beat, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: bank diagram draws in]

**V1-C4** · EDU-front · 12s · the metaphor, warm
> Image-to-video, feed s-edu-front.png as start_image. Same woman, identical look. Clear natural lip-sync: "Think of it like a bank. The test checks her spending money, and it looks fine. Nobody checked her savings, and that's what's empty." Natural mouth movement, warm explaining expression, natural blink, subtle head movement. No on-screen text. Photorealistic, 9:16. [overlay: full bank animation]

**V1-C5** · EDU-close · 3s · micro-commitment
> Image-to-video, feed s-edu-close.png as start_image. Same woman, identical look, chest-up. Clear natural lip-sync: "Make sense so far? Watch this." Natural mouth movement, slight knowing smile, natural blink. No on-screen text. Photorealistic, 9:16.

**V1-C6** · EDU-front · 10s · relatable
> Image-to-video, feed s-edu-front.png as start_image. Same woman, identical look. Clear natural lip-sync: "That's why she can be totally normal on paper and still asleep by 5pm, foggy in class, pale in photos." Natural mouth movement, empathetic expression, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: fast b-roll inserts tired/class/pale]

**V1-C7** · EDU-front · 8s · proof
> Image-to-video, feed s-edu-front.png as start_image. Same woman, identical look. Clear natural lip-sync: "Most of these girls aren't even anaemic, which is exactly why the usual test waves them through." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: "most NOT anaemic" stat]

**V1-C8** · EDU-front · 13s · pivot
> Image-to-video, feed s-edu-front.png as start_image. Same woman, identical look. Clear natural lip-sync: "Topping up iron stores is the easy part. The hard part is getting a teenager to take iron for months. Tablets upset her stomach, she quits." Natural mouth movement, knowing expression, natural blink. No on-screen text. Photorealistic, 9:16.

**V1-C9** · EDU-front · 8s · solution
> Image-to-video, feed s-edu-front.png as start_image. Same woman, identical look. Clear natural lip-sync: "So this is a dissolvable strip made for teen girls, one a day, raspberry, it melts in seconds." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip b-roll]

**V1-C10** · EDU-close · 5s · payoff
> Image-to-video, feed s-edu-close.png as start_image. Same woman, identical look, chest-up. Clear natural lip-sync: "She'll actually take it, which is the whole point." Natural mouth movement, slight smile, natural blink. No on-screen text. Photorealistic, 9:16.

**V1-C11** · EDU-low · 12s · authority, honest caveat
> Image-to-video, feed s-edu-low.png as start_image. Same woman, identical look, slight low angle. Clear natural lip-sync: "If she's very low or already anaemic, that's a doctor's dose first. For everyone else stuck at normal, ask for her ferritin by name." Natural mouth movement, calm authoritative expression, natural blink. No on-screen text. Photorealistic, 9:16.

**V1-C12** · EDU-low · 8s · CTA
> Image-to-video, feed s-edu-low.png as start_image. Same woman, identical look. Clear natural lip-sync: "And if you want the gentle daily version, it's IRYN, 70 day money-back. Link's right there." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA end card]

## VIDEO 2 - EDU-B (2026 news)

**V2-C1** · EDU-front · 8s · newsy, slightly urgent
> Feed s-edu-front.png. Same educator, identical look, warm calm American-English voice. Arm's-length selfie. Clear natural lip-sync: "In 2026 the guidance on teenage girls and iron quietly changed, and most mums have no idea." Natural mouth movement, slightly urgent expression, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: breaking-news ticker]

**V2-C2** · EDU-close · 6s · qualifier
> Feed s-edu-close.png. Same educator, chest-up. Clear natural lip-sync: "If your daughter's been tired for months and her bloodwork keeps coming back fine, this is the part you want." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16.

**V2-C3** · EDU-front · 11s · explaining
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "Paediatric experts now say check a girl's ferritin by age 14. Ferritin is her iron stores, and here's why they singled it out." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16.

**V2-C4** · EDU-front · 13s · the gap
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "A normal blood count checks the iron in her blood today. It never checks her stores. Two different numbers, and routine tests almost always run only the first." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: lab card]

**V2-C5** · EDU-front · 11s · proof
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "That's how around 40% of teen girls end up low and missed, because most of them aren't anaemic, so the standard test clears them." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat + tired b-roll]

**V2-C6** · EDU-close · 6s · relatable punch
> Feed s-edu-close.png. Same educator, chest-up. Clear natural lip-sync: "The tired kid who tests fine is the exact kid this is about." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16.

**V2-C7** · EDU-front · 9s · pivot
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "If hers is low, refilling it is simple. Getting a teenager to take iron daily is not." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16.

**V2-C8** · EDU-front · 9s · product
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "Which is why the version that works is a strip that melts on her tongue, raspberry, one a day." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip]

**V2-C9** · EDU-low · 9s · caveat + CTA
> Feed s-edu-low.png. Same educator, low angle. Clear natural lip-sync: "Very low or anaemic means a doctor's dose first. Otherwise, ask for her ferritin by name at the next appointment." Natural mouth movement, calm authoritative, natural blink. No on-screen text. Photorealistic, 9:16.

**V2-C10** · EDU-low · 7s · CTA
> Feed s-edu-low.png. Same educator. Clear natural lip-sync: "And the gentle daily one is IRYN, 70 day money-back. Details at the link." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card]

## VIDEO 3 - EDU-C (whiteboard) - face only at the CTA; the rest is the educator's VO under the bank animation
**V3-C1** · EDU-front · 8s · teaching
> Feed s-edu-front.png. Same educator, warm calm voice. Clear natural lip-sync: "Let me show you why your daughter's iron test can say normal while she's running on empty." Natural mouth movement, teaching expression, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: hand drawing two boxes]

**V3-C2** · EDU-front · 11s · labelling
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "Draw two accounts. This one is the iron moving in her blood right now. This one is her iron in storage, her savings." Natural mouth movement, teaching, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: whiteboard labels]

**V3-C3** · EDU-front · 10s · the reveal
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "A standard blood count only checks this one, the spending account. It looked fine, so she's normal." Natural mouth movement, teaching, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: whiteboard]

**V3-C4** · EDU-front · 9s · the drain
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "But nobody checked the savings, and that's the one that empties first in teen girls. Watch." Natural mouth movement, teaching, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: savings drains]

**V3-C5** · EDU-front · 10s · symptoms
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "Empty savings is why she's asleep by 5, foggy, pale, and the test still cleared her." Natural mouth movement, empathetic, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: b-roll]

**V3-C6** · EDU-front · 9s · stat
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "Around 40% of teen girls are here, most not anaemic, so the usual test misses them completely." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat]

**V3-C7** · EDU-front · 9s · refill
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "Refilling the savings is simple iron, daily, for a few months. The only reason it fails is she won't take pills." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: savings refills]

**V3-C8** · EDU-front · 8s · product
> Feed s-edu-front.png. Same educator. Clear natural lip-sync: "So the fix that actually works is a raspberry strip that melts on her tongue, one a day." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: strip]

**V3-C9** · EDU-low · 8s · caveat
> Feed s-edu-low.png. Same educator, low angle, first clear face of the ad. Clear natural lip-sync: "If she's very low or anaemic, doctor's dose first. Otherwise ask for her ferritin by name," Natural mouth movement, calm authoritative, natural blink. No on-screen text. Photorealistic, 9:16.

**V3-C10** · EDU-low · 7s · CTA
> Feed s-edu-low.png. Same educator. Clear natural lip-sync: "and the gentle daily one is IRYN, 70 day money-back. Link below." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card]

---

# FORMAT 5 - MENTOR STORY (coach). Angles map to your two kept frames: COACH-gym (default) and COACH-clinic (punch-in / physio).

## VIDEO 4 - COACH-A (cross-country coach)

**V4-C1** · COACH-gym · 10s · authority cold open
> Feed s-coach-front-gym.png. The exact same woman, identical face, navy polo, whistle, visor, gym background, grounded confident American-English female voice, mid-40s. Medium shot, small weight shift. Clear natural lip-sync: "I've coached a few hundred teenage girls, and I can usually tell which ones have run out of iron before they can." Natural mouth movement, confident expression, natural blink. No on-screen text. Photorealistic, 9:16.

**V4-C2** · COACH-gym · 11s · the pattern
> Feed s-coach-front-gym.png. Same coach, identical look. Clear natural lip-sync: "Every season it's the same story. A strong girl slowly slides backwards. Gassing out on runs she used to finish. Heavy legs." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: practice b-roll]

**V4-C3** · COACH-clinic · 6s · wrong assumption (push-in)
> Feed s-coach-front-clinic.png. Same coach, navy quarter-zip, clinic background, slow push-in. Clear natural lip-sync: "And everyone's first guess is that she stopped trying, or she's just tired." Natural mouth movement, slightly wry, natural blink. No on-screen text. Photorealistic, 9:16.

**V4-C4** · COACH-gym · 9s · the setup
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "The parents do the right things. More sleep, more food, a rest week. A lot of them even get bloods done, and it comes back normal." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: lab card near the end]

**V4-C5** · COACH-gym · 13s · personal hinge
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "I had a runner go from the front group to the back in one season. Her mum was ready to pull her out. Bloodwork? Normal. It didn't sit right with me, because I'd seen it too many times." Natural mouth movement, serious, natural blink. No on-screen text. Photorealistic, 9:16.

**V4-C6** · COACH-gym · 14s · the reveal
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "Turns out a standard blood count checks the iron in her blood right now, but not ferritin, her iron stores. For a runner that reserve is everything, because iron is what carries oxygen to her muscles." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: bank diagram]

**V4-C7** · COACH-clinic · 7s · money line (push-in)
> Feed s-coach-front-clinic.png. Same coach, slow push-in. Clear natural lip-sync: "She had an okay count and empty stores, which is exactly when a strong girl hits a wall. The test just never looked." Natural mouth movement, emphatic, natural blink. No on-screen text. Photorealistic, 9:16.

**V4-C8** · COACH-gym · 12s · stat + solution lead-in
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "That's why she could train just as hard and go backwards. And it's common, around 40% of teen girls are low, most not anaemic, so the test clears them." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat + practice b-roll]

**V4-C9** · COACH-gym · 14s · solution + product
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "Refilling it is simple. The catch is getting a 15 year old to take iron daily through a season. Tablets wreck her stomach, she quits. The ones who stick with it use a strip that melts on the tongue, raspberry, one a day, no fight." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip]

**V4-C10** · COACH-gym · 11s · proof + caveat
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "That runner is back in the front group. I always say the same thing: if she's very low or anaemic, see your doctor for a proper dose first. For everyone else stuck at normal, it's worth checking." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: win b-roll]

**V4-C11** · COACH-clinic · 12s · close + CTA
> Feed s-coach-front-clinic.png. Same coach. Clear natural lip-sync: "Ask for her ferritin by name. The gentle daily one made for teen girls is IRYN, and it's got a 70 day money-back guarantee. I just wish someone had told these mums which number to ask for years ago." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card at end]

## VIDEO 5 - COACH-B (PE teacher)

**V5-C1** · COACH-gym · 9s · authority hook
> Feed s-coach-front-gym.png. Same coach/teacher, grounded confident voice. Clear natural lip-sync: "After fifteen years running school sport, I can walk past a team and point out the girls who are low in iron." Natural mouth movement, confident, natural blink. No on-screen text. Photorealistic, 9:16.

**V5-C2** · COACH-gym · 13s · symptoms
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "It's never the loud stuff. It's the girl who used to be keen and now asks to sit out. Tired at training, flat in class, pale. The easy read is teenager. I stopped believing that a long time ago." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: practice/class b-roll]

**V5-C3** · COACH-gym · 9s · setup
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "Parents take them to the GP, get bloods, and it comes back normal. Everyone exhales and nothing changes, because the tiredness is still there the next week." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16.

**V5-C4** · COACH-clinic · 10s · personal hinge (push-in)
> Feed s-coach-front-clinic.png. Same coach, push-in. Clear natural lip-sync: "One girl's mum came to me in tears. Straight-A kid, suddenly falling asleep in fifth period, bloodwork fine. I told her what a sports doctor once told me." Natural mouth movement, serious, natural blink. No on-screen text. Photorealistic, 9:16.

**V5-C5** · COACH-gym · 14s · the reveal
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "A normal blood count checks the iron in her blood today. It doesn't check ferritin, her stores. Two different numbers, and routine tests only run the first. So her reserve can be empty while the test says normal." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: bank diagram]

**V5-C6** · COACH-gym · 10s · stat
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "That's why a genuinely tired girl keeps getting cleared. Around 40% of teen girls are low, most not anaemic, so they slip straight through." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat + tired b-roll]

**V5-C7** · COACH-gym · 12s · solution + product
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "Topping it up is simple iron over a few months. The only reason it fails is compliance, teenagers won't take tablets. The version that sticks is a raspberry strip that melts on the tongue, one a day." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip]

**V5-C8** · COACH-clinic · 10s · caveat + CTA
> Feed s-coach-front-clinic.png. Same coach. Clear natural lip-sync: "If she's very low or anaemic, that's a doctor's dose first, no shortcuts. Otherwise, ask for her ferritin by name." Natural mouth movement, calm authoritative, natural blink. No on-screen text. Photorealistic, 9:16.

**V5-C9** · COACH-gym · 8s · close + CTA
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "The gentle daily one made for teen girls is IRYN, 70 day money-back. Honestly, I wish this was standard." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card]

## VIDEO 6 - COACH-C (youth-sport physio) - default COACH-clinic

**V6-C1** · COACH-clinic · 8s · the slam hook
> Feed s-coach-front-clinic.png. Same coach as physio, navy quarter-zip, clinic. Clear natural lip-sync: "Every year I get the same girl in here: training harder, getting slower, and no one can explain it." Natural mouth movement, direct, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: clipboard slam in frame 1]

**V6-C2** · COACH-gym · 11s · the problem
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "Fit kid, good program, and the times go the wrong way. Legs feel heavy. Gassed on the warm-up. Parents assume overtraining or a motivation dip. Usually it's neither." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: practice b-roll]

**V6-C3** · COACH-clinic · 9s · the miss
> Feed s-coach-front-clinic.png. Same coach. Clear natural lip-sync: "They'll often have had bloods done. Comes back normal, so iron gets ruled out. That's the mistake, and it's not their fault, it's the test." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: lab card]

**V6-C4** · COACH-clinic · 14s · the reveal
> Feed s-coach-front-clinic.png. Same coach. Clear natural lip-sync: "A standard count checks the iron in her blood now. It doesn't check ferritin, her stores. For an endurance athlete the stores are the whole game, because iron carries oxygen to the muscle. Empty stores show up as a wall long before a blood count goes abnormal." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: bank diagram]

**V6-C5** · COACH-gym · 9s · stat
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "That's why she can train harder and go backwards and still test fine. Around 40% of teen girls are low, most not anaemic, so standard bloods miss them." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat + practice b-roll]

**V6-C6** · COACH-gym · 14s · solution + product
> Feed s-coach-front-gym.png. Same coach. Clear natural lip-sync: "The fix is simple iron, daily, long enough to refill the tank. The reason it fails in teens is they stop taking tablets. The athletes who actually refill use a strip that melts on the tongue, raspberry, one a day, easy to keep up through a season." Natural mouth movement, knowing, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip]

**V6-C7** · COACH-clinic · 12s · caveat + CTA (push-in)
> Feed s-coach-front-clinic.png. Same coach, slow push-in. Clear natural lip-sync: "If she's very low or anaemic, see a doctor for a proper dose first. Otherwise, get her ferritin checked by name, not just a blood count." Natural mouth movement, calm authoritative, natural blink. No on-screen text. Photorealistic, 9:16.

**V6-C8** · COACH-clinic · 8s · close + CTA
> Feed s-coach-front-clinic.png. Same coach. Clear natural lip-sync: "The gentle daily one for teen girls is IRYN, 70 day money-back. That's the number I wish every coach knew." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card]

---

# FORMAT 6 - EPIPHANY (mum). Angles: MUM-front, MUM-close, MUM-seated.

## VIDEO 7 - MUM-A (not herself)

**V7-C1** · MUM-front · 11s · confession cold open
> Feed s-mum-front.png. The exact same woman, identical face, hair, draped blouse, kitchen, warm sincere emotional American-English female voice, late 30s. Arm's-length selfie, slight sway. Clear natural lip-sync: "I spent a year telling my daughter to just try harder. She wasn't missing effort. She was missing iron, and nobody checked." Natural mouth movement, regretful sincere expression, natural blink. No on-screen text. Photorealistic, 9:16.

**V7-C2** · MUM-front · 11s · symptoms
> Feed s-mum-front.png. Same mum. Clear natural lip-sync: "She went from my loud, busy kid to someone asleep by 5pm. Foggy in class, grades slipping, pale in every photo." Natural mouth movement, pained, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: tired/class/pale b-roll]

**V7-C3** · MUM-close · 7s · the admission
> Feed s-mum-close.png. Same mum, lean-in close-up. Clear natural lip-sync: "And I'll be honest, I got frustrated with her, because it looked like she just stopped caring." Natural mouth movement, ashamed sincere, natural blink. No on-screen text. Photorealistic, 9:16.

**V7-C4** · MUM-seated · 10s · the betrayal
> Feed s-mum-seated.png. Same mum, seated at table. Clear natural lip-sync: "I did take her to the doctor. They ran her bloods. Normal. Which somehow made it worse, because now I didn't even have a reason." Natural mouth movement, defeated, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: lab card]

**V7-C5** · MUM-front · 9s · the turn
> Feed s-mum-front.png. Same mum. Clear natural lip-sync: "Just a tired girl and a piece of paper saying she was fine. So I started reading late at night, trying to work out what the test wasn't telling me." Natural mouth movement, searching, natural blink. No on-screen text. Photorealistic, 9:16.

**V7-C6** · MUM-front · 14s · the reveal
> Feed s-mum-front.png. Same mum. Clear natural lip-sync: "Here's what I found. A standard blood count checks the iron moving in her blood today. It does not check ferritin, her iron stores. It's like checking her spending money, which looked okay, while her savings were empty." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: bank diagram]

**V7-C7** · MUM-close · 7s · absolution
> Feed s-mum-close.png. Same mum, close-up. Clear natural lip-sync: "That's when it clicked. It wasn't laziness. It wasn't attitude." Natural mouth movement, emotional relief, natural blink. No on-screen text. Photorealistic, 9:16.

**V7-C8** · MUM-seated · 7s · stat
> Feed s-mum-seated.png. Same mum. Clear natural lip-sync: "Around 40% of teen girls are low and most aren't even anaemic, so the usual test just clears them." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat]

**V7-C9** · MUM-seated · 13s · solution + product
> Feed s-mum-seated.png. Same mum. Clear natural lip-sync: "We got her ferritin checked, it was low, and topping it up was simple. The hard part was getting her to take iron daily. Tablets, she quit in a week. What stuck was a little raspberry strip that melts on her tongue, one a day." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip]

**V7-C10** · MUM-close · 10s · the payoff
> Feed s-mum-close.png. Same mum, close-up, emotional. Clear natural lip-sync: "Around week two she stopped crashing after school. A few weeks later she sat with us at dinner and actually talked, and I had to leave the room." Natural mouth movement, tearful smile, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: dinner b-roll before this]

**V7-C11** · MUM-close · 11s · caveat + CTA
> Feed s-mum-close.png. Same mum. Clear natural lip-sync: "If your girl is very low or anaemic, see your doctor first. But if she keeps testing fine, please, ask for her ferritin by name. The one we use, made for teen girls, is IRYN, 70 day money-back. I just wish I'd known which number to ask for a year earlier." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card at end]

## VIDEO 8 - MUM-B (sport)

**V8-C1** · MUM-front · 6s · reveal mum
> Feed s-mum-front.png. Same mum, warm sincere voice. Clear natural lip-sync: "That was the sentence that made me stop blaming it on her being a teenager." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: couch-in-kit reenactment before this]

**V8-C2** · MUM-front · 13s · the fade
> Feed s-mum-front.png. Same mum. Clear natural lip-sync: "She was strong. Then over a season she faded. Gassed on runs she used to finish, heavy legs, wiped out for hours after training. The coach thought she'd lost interest." Natural mouth movement, pained, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: practice b-roll]

**V8-C3** · MUM-close · 6s · emotional low
> Feed s-mum-close.png. Same mum, close-up. Clear natural lip-sync: "She came home crying that maybe she just wasn't good anymore." Natural mouth movement, heartbroken, natural blink. No on-screen text. Photorealistic, 9:16.

**V8-C4** · MUM-seated · 13s · betrayal + turn
> Feed s-mum-seated.png. Same mum, seated. Clear natural lip-sync: "We tried the obvious things, then got bloods done because I was worried. Normal. So everyone, including me, started to think it was in her head. I couldn't let it go, so I started reading at night." Natural mouth movement, defeated then searching, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: lab card]

**V8-C5** · MUM-front · 14s · the reveal
> Feed s-mum-front.png. Same mum. Clear natural lip-sync: "A standard blood count checks the iron in her blood right now. It doesn't check ferritin, her stores. For an athlete that reserve is everything, it's the oxygen her muscles pull on when she pushes. Her count was okay and her stores were empty." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: bank diagram]

**V8-C6** · MUM-seated · 11s · stat + absolution
> Feed s-mum-seated.png. Same mum. Clear natural lip-sync: "That's why she trained just as hard and went backwards. It was never her effort. And it's common, around 40% of teen girls are low, most not anaemic, so the test clears them." Natural mouth movement, matter-of-fact, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat + practice b-roll]

**V8-C7** · MUM-seated · 11s · solution + product
> Feed s-mum-seated.png. Same mum. Clear natural lip-sync: "Her ferritin was low, refilling it was simple, but she'd quit tablets in days. So she switched to a raspberry strip that melts on her tongue, one a day, easy to keep up all season." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip]

**V8-C8** · MUM-close · 10s · the win
> Feed s-mum-close.png. Same mum, close-up. Clear natural lip-sync: "A couple of weeks in, the after-practice crash eased. Later she told me training felt normal again, which from her is basically a speech." Natural mouth movement, warm smile, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: strong-again practice b-roll before this]

**V8-C9** · MUM-close · 12s · caveat + CTA
> Feed s-mum-close.png. Same mum. Clear natural lip-sync: "If she's very low or anaemic, doctor's dose first. Otherwise, ask for her ferritin by name, not just a blood count. The daily one made for teen girls is IRYN, 70 day money-back. I just wish I'd known before she spent a season thinking she wasn't good enough." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card at end]

## VIDEO 9 - MUM-C (normal result)

**V9-C1** · MUM-close · 8s · lean-in confession hook
> Feed s-mum-close.png. Same mum, intimate lean-in close-up, eyes filling frame, warm sincere voice. Clear natural lip-sync: "Her blood test said normal. Twice. I believed it for a year, and I was wrong." Natural mouth movement, raw sincere, natural blink. No on-screen text. Photorealistic, 9:16.

**V9-C2** · MUM-front · 11s · symptoms
> Feed s-mum-front.png. Same mum, arm's-length. Clear natural lip-sync: "She was wiped out every afternoon, foggy at school, pale, snapping then crying that she didn't know why. I kept telling myself it was just her age." Natural mouth movement, pained, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: tired/pale b-roll]

**V9-C3** · MUM-seated · 13s · double betrayal
> Feed s-mum-seated.png. Same mum, seated. Clear natural lip-sync: "We got bloods done, not once but twice, and both times they said she was fine. So I stopped looking, because what do you do when the test says there's nothing wrong?" Natural mouth movement, defeated, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: lab card x2 stamp]

**V9-C4** · MUM-front · 5s · the turn
> Feed s-mum-front.png. Same mum. Clear natural lip-sync: "A nurse friend is the one who finally said the thing no one had told me." Natural mouth movement, searching, natural blink. No on-screen text. Photorealistic, 9:16.

**V9-C5** · MUM-front · 15s · the reveal
> Feed s-mum-front.png. Same mum. Clear natural lip-sync: "A standard blood count checks the iron in her blood today. It never checks ferritin, her iron stores. Two completely different numbers, and the routine panel only runs the first. Her spending money looked fine while her savings were empty. That's how a genuinely exhausted girl keeps coming back normal." Natural mouth movement, explaining, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: bank diagram]

**V9-C6** · MUM-seated · 11s · stat + vindication
> Feed s-mum-seated.png. Same mum. Clear natural lip-sync: "Around 40% of teen girls are low in iron, and most aren't anaemic, which is the exact reason the standard test misses them. It wasn't nothing. It was never nothing." Natural mouth movement, emotional conviction, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: stat + tired b-roll]

**V9-C7** · MUM-seated · 13s · solution + product
> Feed s-mum-seated.png. Same mum. Clear natural lip-sync: "We asked for her ferritin by name, it was low, and refilling it was simple. The only hard part was getting her to take iron daily, so we used a raspberry strip that melts on her tongue, one a day, no pills to quit." Natural mouth movement, warm, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: product strip]

**V9-C8** · MUM-close · 10s · payoff
> Feed s-mum-close.png. Same mum, close-up. Clear natural lip-sync: "Week two she wasn't asleep by five. By about week six she was herself again, and we'll retest her ferritin at 90 days to prove it with a number." Natural mouth movement, warm relief, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: dinner b-roll before this]

**V9-C9** · MUM-close · 12s · caveat + CTA
> Feed s-mum-close.png. Same mum. Clear natural lip-sync: "If she's very low or anaemic, see a doctor for a proper dose first. But if yours keeps testing fine, ask for her ferritin by name. The gentle daily one is IRYN, 70 day money-back. You deserve to know which number they skipped." Natural mouth movement, sincere, natural blink. No on-screen text. Photorealistic, 9:16. [overlay: CTA card at end]

---

# CREDIT ESTIMATE (Kling 3.0, std 720p, sound ON = 2.0 credits/sec)

Because the avatar speaks natively, every clip is its own generation and the talking clips carry the full narration (b-roll overlays on top, no separate voice track).

| Video | Clips | Spoken seconds |
|---|---|---|
| V1 EDU-A | 12 | ~116 |
| V2 EDU-B | 10 | ~89 |
| V3 EDU-C | 10 | ~86 |
| V4 COACH-A | 11 | ~123 |
| V5 COACH-B | 9 | ~95 |
| V6 COACH-C | 8 | ~85 |
| V7 MUM-A | 11 | ~110 |
| V8 MUM-B | 9 | ~96 |
| V9 MUM-C | 9 | ~98 |
| **Total** | **~89 clips** | **~898 sec** |

- First-pass generation: **~898s x 2.0 = ~1,800 credits.**
- Realistic with retries/variants (~25%): **~1,800 to 2,250 credits.**
- Current balance ~3,500, so one full pass fits with room to spare, but this is the real cost of native Kling speech throughout (speech seconds, not just on-camera seconds, are billed).

### The one honest flag (not re-litigating, your call stands)
Native Kling audio bills every spoken second (~898s) and can vary voice/quality clip to clip. The reason the earlier silent + ElevenLabs path was ~150 to 300 Kling credits is that audio there is near-free and you only render visible talking footage. You've chosen native Kling; this estimate reflects it. If any clip's voice comes out wrong, we regenerate just that clip.

### To cut the number without changing the plan
- Trim each script to the ~55 to 60s versions (the storyboards mark the trim points) to roughly halve spoken seconds to ~500s to ~600s, i.e. **~1,000 to 1,200 credits**.
- Or generate V1, V4, V7 first (one per format, ~360s, ~720 credits), test them, then do the other 6 only if the format works.

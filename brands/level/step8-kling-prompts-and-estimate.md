<!-- IRYN Step 8 - Kling 3.0 talking-head video prompts + credit estimate.
     Build: Kling 3.0, std mode (720p), aspect 9:16, sound OFF (silent), image-to-video from the Step 7 start scenes.
     Voice/lip-sync added after in ElevenLabs. No em-dashes. -->

# IRYN - Step 8: Kling 3.0 talking-head prompts + credit estimate

## Settings (every clip)
- Model: **Kling 3.0** · mode **std (= 720p)** · aspect **9:16** · sound **off** (silent, we lip-sync after) · image-to-video.
- Cost at these settings: **1.5 credits per second** (7.5 / 5s, 15 / 10s). Kling caps at 15s, so every beat fits one clip.
- Each clip feeds its start frame as `start_image`. The prompt only drives performance (talking motion), never the look.

## The 8 start frames (reference images) these map to
| Angle code | Start frame file |
|---|---|
| EDU-front | s-edu-front.png |
| EDU-close | s-edu-close.png |
| EDU-low | s-edu-low.png |
| COACH-gym | s-coach-front-gym.png |
| COACH-clinic | s-coach-front-clinic.png |
| MUM-front | s-mum-front.png |
| MUM-close | s-mum-close.png |
| MUM-seated | s-mum-seated.png |
| EDU-hold-tin | s-edu-front-product.png (product beat) |
| MUM-hold-tin | s-prod-tin-in-hand.png (product beat) |

> Coach note: the storyboard was written for track front/close/34. You kept only **gym + clinic**, so coach beats map to those two looks. For a "close/punch-in" feel on a key coach line, the prompt adds a slow subtle push-in rather than a new frame.

---

## MASTER PROMPTS (one per angle, reused on every beat of that angle)
Because we lip-sync after, Kling only needs natural talking motion. The spoken words do not matter to Kling. Generate each angle once (or twice for variety), reuse under the lip-sync.

### EDU-front (FEED s-edu-front.png)
> The woman in the image is talking naturally to the camera as if filming a casual handheld selfie video. Natural mouth and jaw movement of someone mid-conversation, subtle eyebrow and head movement, steady eye contact with the lens, occasional natural blink, very slight handheld camera sway. She stays in place, warm and engaged. Keep her face, hair, navy blazer, cream top and the kitchen background identical to the start frame. No large gestures, no walking. Photorealistic, natural indoor daylight, 9:16.

### EDU-close (FEED s-edu-close.png)
> Same woman, intimate chest-up framing, talking naturally and sincerely to the camera with a very slow subtle push-in. Natural speaking mouth movement, small head nods, natural blink, one calm hand gesture near her chest settling back down. Keep face, hair, wardrobe and background identical to the start frame. Photorealistic, soft daylight, 9:16.

### EDU-low (FEED s-edu-low.png)
> Same woman, slight low angle, talking calmly and with authority to the camera, measured pace. Natural speaking mouth movement, steady gaze, minimal head movement, natural blink, very slight handheld sway. Keep face, hair, wardrobe and background identical to the start frame. Photorealistic, soft daylight, 9:16.

### COACH-gym (FEED s-coach-front-gym.png)
> The woman in the image is talking straight to the camera, confident and grounded, as if being interviewed in the sports hall. Natural speaking mouth and jaw movement, subtle head movement, steady eye contact, natural blink, small weight shift. She stays in place. Keep face, navy polo, whistle, visor and the gym background identical to the start frame. Photorealistic, soft indoor light, 9:16.

### COACH-clinic (FEED s-coach-front-clinic.png)
> Same woman, talking to the camera calmly and professionally in the treatment room, with an optional very slow push-in for emphasis. Natural speaking mouth movement, subtle head movement, natural blink. Keep face, navy quarter-zip and the clinic background identical to the start frame. Photorealistic, soft indoor light, 9:16.

### MUM-front (FEED s-mum-front.png)
> The woman in the image is talking to the camera as if filming a heartfelt selfie at her kitchen table. Natural speaking mouth and jaw movement, warm sincere expression, subtle head movement, natural blink, very slight handheld sway. She stays in place. Keep face, hair, draped blouse and kitchen background identical to the start frame. Photorealistic, soft daylight, 9:16.

### MUM-close (FEED s-mum-close.png)
> Same woman, intimate lean-in close-up, talking emotionally and sincerely to the camera, slight slow push-in. Natural speaking mouth movement, small head movement, glassy sincere eyes, natural blink. Keep face, hair, blouse and background identical to the start frame. Photorealistic, soft daylight, 9:16.

### MUM-seated (FEED s-mum-seated.png)
> Same woman, seated at the kitchen table, slightly lower angle, talking calmly to the camera with hands resting on the table. Natural speaking mouth movement, subtle head movement, natural blink, hands mostly still with one small settle. Keep face, hair, blouse and background identical to the start frame. Photorealistic, soft daylight, 9:16.

### EDU-hold-tin (FEED s-edu-front-product.png) - product beat
> Same woman holding the small IRYN tin near her chest, talking warmly to the camera, gently turning the tin a few degrees so the label stays readable. Natural speaking mouth movement, subtle head movement, natural blink. Keep her face, wardrobe, the small tin and its label, and the kitchen identical to the start frame. Do not distort or change the label text. Photorealistic, soft daylight, 9:16.

### MUM-hold-tin (FEED s-prod-tin-in-hand.png) - product beat
> Same woman holding the small IRYN tin at chest height, talking warmly to the camera, holding the tin steady with the label readable. Natural speaking mouth movement, subtle head movement, natural blink. Keep face, blouse, the small tin and its label, and the kitchen identical to the start frame. Do not distort the label. Photorealistic, soft daylight, 9:16.

---

## PER-VIDEO BEAT MAP (talking-head clips only; b-roll = real footage, GFX/cards = editor)
Durations are the storyboard beat lengths. Expression notes tell you the performance for that beat.

### VIDEO 1 - EDU-A (~82s) - 8 talking clips, 45s
1. 4.5s EDU-close - the opening question, curious
2. 4.5s EDU-front - proof bridge, matter-of-fact
3. 7.0s EDU-front - the "bank" explainer (bank diagram overlaid in editor)
4. 2.0s EDU-close - "make sense? watch this", micro-commitment
5. 7.0s EDU-front - symptom list (b-roll inserts over it)
6. 7.0s EDU-front - pivot to the compliance problem
7. 4.0s EDU-close - "she'll actually take it", payoff
8. 9.0s EDU-low - honest caveat + CTA, authority

### VIDEO 2 - EDU-B (~70s) - 7 clips, 43s
1. 5.5s EDU-front - 2026 news open (ticker in editor)
2. 4.0s EDU-close - qualifier bridge
3. 6.5s EDU-front - "check ferritin by 14"
4. 8.0s EDU-front - two-numbers explainer (lab card overlaid)
5. 4.0s EDU-close - "the tired kid who tests fine"
6. 8.0s EDU-front - pivot to solution (strip b-roll after)
7. 7.0s EDU-low - caveat + CTA

### VIDEO 3 - EDU-C (~60s) - 1 clip, 8s (rest is bank animation = editor)
1. 8.0s EDU-low - first face of the ad, caveat + CTA

### VIDEO 4 - COACH-A (~92s) - 10 clips, 82s
1. 6.0s COACH-gym - authority cold open
2. 6.0s COACH-gym (3/4 feel) - the pattern
3. 5.0s COACH-clinic (push-in) - wrong assumption
4. 8.0s COACH-gym - the setup
5. 9.0s COACH-gym (3/4 feel) - personal hinge
6. 13.0s COACH-gym - the reveal (bank overlay)
7. 7.0s COACH-clinic (push-in) - money line
8. 10.0s COACH-gym - solution (strip after)
9. 9.0s COACH-gym (3/4 feel) - proof + caveat
10. 9.0s COACH-clinic - close + card

### VIDEO 5 - COACH-B (~88s) - 8 clips, 70s
1. 6.5s COACH-gym - authority hook
2. 8.5s COACH-gym - symptom cutaways over it
3. 6.0s COACH-gym - the setup
4. 8.0s COACH-clinic (push-in) - personal hinge
5. 13.0s COACH-gym - the reveal (bank overlay)
6. 10.0s COACH-gym - solution (strip after)
7. 10.0s COACH-clinic - caveat + CTA
8. 8.0s COACH-gym - close + card

### VIDEO 6 - COACH-C (~86s) - 6 clips, 58s
1. 6.0s COACH-clinic - the slam hook (slam in editor)
2. 8.0s COACH-gym - the problem
3. 7.0s COACH-clinic - the miss (lab card)
4. 13.0s COACH-clinic - the reveal (bank overlay)
5. 12.0s COACH-gym - solution (strip after)
6. 12.0s COACH-clinic (push-in) - caveat + CTA

### VIDEO 7 - MUM-A (~90s) - ~10 clips, 74s
1. 8.0s MUM-front - confession cold open
2. 8.0s MUM-front - symptom cutaways over it
3. 5.0s MUM-close - the shameful admission
4. 7.0s MUM-seated - the betrayal (lab card)
5. 5.0s MUM-front - the turn
6. 12.0s MUM-front - the reveal (bank overlay)
7. 7.0s MUM-close - absolution
8. 10.0s MUM-seated - solution (strip after)
9. 5.0s MUM-close - after the dinner b-roll, the payoff line
10. 7.0s MUM-close - caveat + CTA

### VIDEO 8 - MUM-B (~86s) - ~8 clips, 64s
1. 6.0s MUM-front - reveal mum after the reenactment
2. 9.0s MUM-front - the fade (practice cutaway)
3. 6.0s MUM-close - emotional low
4. 8.0s MUM-seated - betrayal + turn (lab card)
5. 13.0s MUM-front - the reveal (bank overlay)
6. 9.0s MUM-seated - solution (strip after)
7. 5.0s MUM-close - after the win b-roll, payoff line
8. 8.0s MUM-close - caveat + CTA

### VIDEO 9 - MUM-C (~84s) - ~8 clips, 65s
1. 6.0s MUM-close - lean-in confession hook
2. 8.0s MUM-front - symptom cutaways over it
3. 10.0s MUM-seated - double betrayal (lab card x2)
4. 4.0s MUM-front - the turn
5. 14.0s MUM-front - the reveal (bank overlay)
6. 10.0s MUM-seated - solution (strip after)
7. 5.0s MUM-close - after dinner b-roll, payoff
8. 8.0s MUM-close - caveat + CTA

---

## CREDIT ESTIMATE (std 720p, silent)

### Approach A - generate every beat fresh (the literal storyboard)
- Total talking-head footage: **~509 seconds** across ~58 clips.
- 509 x 1.5 = **~765 credits** first pass.
- Add ~25% for retries/variants: **~765 to 950 credits.**

### Approach B - generate each angle once or twice, reuse + lip-sync (recommended, far cheaper)
- 8 angles (+2 product) = 10 looks. Generate ~2 silent talking bases each at 10s for variety = ~20 clips.
- 20 x 10s x 1.5 = **~300 credits.** One base per angle = ~150 credits.
- Then lip-sync each storyboard beat's ElevenLabs audio onto the matching base clip (reused). Lip-sync is a separate tool cost, not Kling credits.
- Net Kling spend: **~150 to 300 credits** instead of ~765 to 950. Same 9 finished ads.

### Recommendation
Approach B. The talking motion is interchangeable once we lip-sync, so regenerating the same angle 6 times is wasted money. Generate 2 bases per angle, cut and lip-sync per beat. Keeps Kling spend under ~300 and leaves plenty of the ~3,500 balance for b-roll touch-ups and retries.

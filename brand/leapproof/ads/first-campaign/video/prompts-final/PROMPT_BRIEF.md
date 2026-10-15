# Leapproof — Kling 3.0 IMAGE-TO-VIDEO prompt brief (overnight build, 2026-10-15)

Goal: ONE bulletproof Kling 3.0 image-to-video prompt per delivered start-scene image, for all 6 ads.
Nikita runs them himself tomorrow. **Nothing is generated tonight — do not call any generation tool.**

All paths below are relative to `SB = /tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/sb`
unless absolute.

## 1. Kling 3.0 facts (Higgsfield model id `kling3_0`, verified tonight)
- Inputs: `start_image` (we always use one) + optional `end_image`; text prompt.
- Duration: ANY whole number of seconds from **3 to 15**. Minimum is 3 s.
- Mode: std / pro / 4k → recommend **Pro** for every clip (realism matters).
- Sound: `on` / `off`. `off` = silent and cheaper.
- Aspect: 9:16.
- Higgsfield exposes no negative-prompt field (Kling's own app does). So give BOTH: an inline `Avoid:` sentence at
  the end of the main prompt, AND a separate NEGATIVE line he can paste if his UI has the field.

## 2. Inputs you must use
- **Start images (what he uploads):** full-res PNGs in `SB/vid/deliver/<AD>/<file>.png`.
  View the 720 px copies: `/home/user/NG/brand/leapproof/ads/first-campaign/video/start-scenes/<AD>/<file>.jpg`.
  **Open (Read) EVERY image for your ad before writing its prompt.** The prompt must describe what is ACTUALLY in that
  frame (pose, props, wardrobe, framing, what is in hand, where each character sits) — not what the storyboard hoped.
  If the image deviates from the storyboard, write to the image and record the deviation in `image_deviation_flags`.
- **Storyboard (intent, motion, sfx, dialogue):** `SB/out/<AD>.json` (fields: shot_id, t_in, t_out, what_we_see,
  motion_inside_shot, vo_or_dialogue, sfx, cut_reason, source_lane, on_screen_text).
- **Earlier draft video prompts (written before images existed):** `SB/vid/<AD>.json` — reuse good ideas and any
  `editor_note` about merged/punch-in shots, but rewrite against the real image.
- **Format 1 real timing:** `SB/timing/V1_cutlists.json` — on-screen durations for V1 shots come from HERE
  (they override the storyboard t_in/t_out; they are anchored to Nikita's actual ElevenLabs recordings).
- **Start-scene manifest:** `/home/user/NG/brand/leapproof/ads/first-campaign/video/start-scenes/START_SCENES.md`.

## 3. Format rules
### FORMAT 1 = V1-a, V1-b, V1-c (voiceover-over-b-roll ads)
- **Sound OFF on every clip.** The narration is a separate ElevenLabs track laid in CapCut.
- **No dialogue, voice, lip-sync or audio instructions in the prompt at all.** Picture + motion + camera only.
- Nobody talks to camera. People are mid-life, turned away, side-on — that is correct b-roll.
- Exception, V1-b F1 (restaurant laugh): she belly-laughs with her mouth open and moving (the ElevenLabs line
  "Stop! I'll pee myself!" is laid over it). Prompt big natural laughter; do NOT script specific words.
- Look: native phone b-roll — subtle handheld micro-drift or locked-off, natural light, no cinematic camera tricks.

### FORMAT 2 = V2-a, V2-b, V2-c (Pixar liner-vs-underwear duet)
- **Sound ON only when an on-screen character speaks with a visible mouth.** Embed the exact line.
- **Sound OFF** for: reaction shots with no line, shots where the line is off-screen VO, back-to-camera lines
  (mouth hidden), and every live-action woman shot. Their audio comes from ElevenLabs or a neighbouring clip.
- One speaker per clip. The other character, if in frame, stays silent, mouth closed, small listening reactions only.
- Copy every spoken line VERBATIM from the storyboard `vo_or_dialogue` (strip stage directions/timings only).
- Paste these voice blocks VERBATIM in every speaking prompt so the voices stay consistent clip to clip:
  - LINER: `a higher-pitched, fussy, fast-talking, slightly anxious young adult female cartoon voice, bright and comedic, clear American accent`
  - UNDERWEAR: `a warm, dry, calm, unhurried adult female voice, low-mid pitch, confident and kind, clear American accent`
- Spoken-line format inside the prompt:
  `Audio: the [LINER|UNDERWEAR] character speaks, lip-synced, [voice block]: "<exact line>". No music, no score; soft natural room tone only.`
- If a storyboard AI shot has no start image because it was planned as a punch-in / continuation of another clip,
  fold its line into that clip (longer duration) and say so in `covers_shots`. If it is genuinely missing, list it
  in `uncovered_storyboard_shots`.

## 4. Duration rule (goes in the header of every prompt)
- On-screen duration D: Format 1 = cut list `dur`; Format 2 = storyboard t_out − t_in (+ any shots this clip covers).
- Speaking clips (F2): K = max(3, ceil(words / 2.6 + 0.8)) seconds — the full line must fit with a breath of handle.
- Silent clips: K = 3 by default. If the key action must COMPLETE inside a short on-screen window, write the motion at
  a natural but brisk pace, keep K = 3–4, and give an EDIT note: "use a–b s @ N% speed". Speed-ups max 200 %;
  if it would need more, ask for a brisker motion in the prompt instead. Long holds (end cards, 3 s+ windows):
  K = ceil(D + 0.5).
- K is always a whole number 3–15.

Header format (exactly these three lines, then the prompt):
```
⏱ GENERATE: K s · Kling 3.0 · Pro · 9:16 · Sound OFF|ON
🎬 ON-SCREEN: D s (ad timecode t_in–t_out) · EDIT: <use a–b s @ N%  |  use from 0.0 s, trim to D>
🖼 START IMAGE: <AD>/<file>.png   ·   END IMAGE: none
```

## 5. Prompt anatomy (what makes it bulletproof)
1. Open with: `Animate the provided start image.` + a lock: the first frame matches the image exactly; keep the
   same framing, set, light, wardrobe, character design and product design throughout.
2. ONE primary action, physically described in order with rough timing ("over ~1.5 s she…, then…"), real weight and
   physics, and the END STATE of the motion.
3. Camera: one move or locked ("locked-off with a subtle handheld micro-drift" / "slow push-in 100→105 %"). No cuts.
4. Frame-specific continuity locks: avatar face/hair when visible; hands keep five fingers; BOTH legs stay fully
   clothed and fully in frame, never cut off; objects obey gravity, nothing floats or hangs; the product stays plain
   black seamless matte microfibre with laser-cut raw edges and ruched side gathers, no lace, no logo, no band.
   Pixar: underwear face stays on the upper front panel under the waistband, never on the gusset; liner pure clean
   white, no stains; in visual descriptions call the liner "the white oval soft-pad mascot" (moderation-safe).
5. F2 speaking clips: performance (eyes, brows, mouth shapes, small body squash/stretch) + the Audio line.
6. End with `Avoid:` + the frame-relevant failure list.
- Main prompt 70–170 words. Concrete, present tense, most important instruction first. No lists of 30 adjectives.
- NEGATIVE line (separate, pasteable): `morphing, face change, identity drift, extra fingers, fused fingers, extra
  limbs, cut-off leg, missing leg, warped body, melting objects, floating objects, flicker, text, captions, subtitles,
  logo, watermark, brand marks, scene cut, heavy camera shake, motion blur smear, stains, leak, children, nudity,
  crotch focus, buttock focus` (+ shot-specific items).

## 6. Failure modes already hit on this project — prevent them
- Leggings shots: a leg got "cut off"/chopped → both legs fully clothed and visible for the entire move.
- Car boot: grocery bag hanging off the car unrealistically → the bag goes INTO the boot and rests on the floor.
- Product drift: lace, logos or an elastic logo band appearing → lock the garment in the prompt.
- Pixar liner prompts were moderation-flagged when "panty liner" sat next to body/limp/flop/stumble verbs → visual
  descriptions say "white oval soft-pad mascot"; keep verbs wholesome (spoken lines stay verbatim even if they say
  "panty liner").
- V2-a image 17 (end card) shows the underwear with small cartoon arms (off its armless sheet) → do not animate
  arms/hands; keep them still or tucked; flag it (a re-roll is on offer).
- Restaurant: sparkling water only, never wine/alcohol. No children anywhere. No on-screen text in any frame
  (captions are added in CapCut).
- Clips under ~1 s on screen: give the motion a strong readable shape in the first second (hook-speed b-roll).

## 7. Output
Return the structured object requested by the workflow (one entry per start image, in ad order), plus
`uncovered_storyboard_shots`. Every `prompt` must be complete and copy-pasteable on its own (no "same as above").

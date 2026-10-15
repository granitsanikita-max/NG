# Shared spec for Leapproof video start-scene + Kling 3.0 prompts

You write the AI start-scene IMAGE prompts (Nano Banana Pro) and the Kling 3.0 VIDEO prompts for ONE ad. Follow this spec exactly. Output JSON only (schema at the end).

## The pipeline
Each AI shot = a Nano Banana Pro **start-scene image** (9:16, 2K) → animated in **Kling 3.0** (native audio: the spoken line goes IN the video prompt so we get voice). B-roll is NOT generated — it's real Pexels footage, so for b-roll shots output only a short `pexels_search` line, no image/video prompt.

## Source of truth
- Your ad's storyboard JSON: `/tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/sb/out/<AD>.json`. Use its `shots`: `vo_or_dialogue` is the exact spoken line, `on_screen_text` is the caption (caption is added in CapCut, NEVER in a prompt or in the video's audio), `visual_shot`/`angle_or_room`/`what_we_see` describe the frame.
- Only write prompts for shots whose `source_lane` is `AI start frame + motion`. For `owned-phone` and `AI text-to-video` shots, output a `pexels_search`. For `editor` shots (cards, freezes, punch-ins, wipes), output nothing but a one-line `editor_note`.

## Reference images (attach by role `image_references` in Nano Banana)
- **AVATAR** `avatar` (media_id `98bea1e7-0b44-425d-8fe3-79e888d44073`): THE woman. Real, natural, mid-30s; long wavy dark-blonde hair with lighter ends past the shoulders; blue eyes; fair skin with light freckles across nose/cheeks; soft natural makeup; slim-average; warm everyday face (not a glossy model). Attach to EVERY shot where the woman's face or body appears, and in the prompt say "Reference AVATAR is the exact woman — copy her face, hair, skin and age precisely."
- **POSE-CARBOOT** `85f5b73b-1489-48b6-8c67-52dc02d52b39`: a woman loading groceries into a white-hatchback boot in a car park (this reference woman is a brunette — use ONLY for pose/composition/setting, the face comes from AVATAR). Attach on V1-a's car-boot shots.
- **POSE-RESTAURANT** `4a9a7b43-5b13-4d95-a7e7-132cab3b4dab`: a woman mid-belly-laugh at a restaurant table (brunette — pose/setting only, face from AVATAR). Attach on V1-b's restaurant shots. NOTE the ref is dim/warm; our prompt must say BRIGHT golden early-evening window light, not dim candlelight.
- **PRODUCT-STORE** `9c8550ca-f332-4543-aefb-507d8490b0f5` and **PRODUCT-REAL** `44506ee7-fca6-40ec-8514-f8adabd89e86`: the exact black underwear. Attach to every shot where the real underwear or the V2 underwear-character appears. Say "copy the garment exactly: plain black seamless matte-satin microfibre, laser-cut raw edges (no elastic band, no lace, no logo), smooth front panel, short ruched gathers on the side seams, mid-rise."
- **LINER-CHAR** and **UNDIES-CHAR**: the two approved Pixar character anchors (we'll paste their media_ids in at generation time; in the prompt just say "match the approved LINER character sheet" / "match the approved UNDIES character sheet"). For V2 character shots, list them under `references` as `LINER-CHAR` / `UNDIES-CHAR` so we wire them.

## Nano Banana start-scene prompt rules (make them bulletproof)
- Compose the start scene as **frame ONE of the motion** (the action about to happen, or just beginning).
- 9:16 vertical, 2K. Say it.
- Realism block on every PHOTOREAL (non-cartoon) prompt: `photorealistic, real unretouched skin with visible texture, natural imperfections, documentary/editorial realism, shot on 35mm, soft natural light, shallow depth of field, NOT airbrushed, no plastic skin, no text, no logo, no watermark`.
- Pixar character prompts: `premium 3D Pixar-style render, cinematic lighting, soft subsurface shading, shallow depth of field, photoreal blurred real-world set behind, no text, no logo, no watermark, no human`.
- Face/skin lock: whenever the woman appears, repeat her physical description AND attach AVATAR.
- Product lock: whenever the underwear appears, repeat the garment description AND attach the product refs.
- Body shots: side-on, waist-to-knee, getting dressed only, top/hip covered, no crotch or buttock framing, no leak shown.
- No children, no alcohol, no real brand logos, no medical props.

## Kling 3.0 video prompt rules
- One clear action/camera move per clip (Kling does one motion well). State the camera move and the motion.
- **Audio: embed the exact spoken line** from `vo_or_dialogue`. Format: `Spoken aloud, <voice description>: "<exact line>"`. Voices:
  - V1 brand narrator (VO over b-roll): warm, wry, natural 30s American woman. For VO-over-b-roll shots the audio is a voiceover, not lip-synced — say "voiceover, no one speaks on camera".
  - V1-b dinner woman: her one diegetic line, spoken through laughter, lip-synced (she's on camera).
  - V2 LINER: higher, fussy, fast, slightly anxious. V2 UNDIES: warm, dry, calm, unhurried. One speaker per clip; the non-speaker stays silent, mouth closed.
- Also specify: ambient sound + a short music cue if the beat calls for it.
- Keep captions OUT of the audio and out of the prompt (CapCut adds them).
- Duration: compute spoken seconds = words ÷ 2.4 + ~0.7s handle; give `kling_seconds` (round to 5s or 10s — Kling clip lengths).
- If a shot has no dialogue, say "no dialogue; ambient + music only".

## Output JSON (write to `/tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/sb/vid/<AD>.json`)
```
{
 "ad_id": "...",
 "shots": [
   {"shot_id": "...", "lane": "ai|broll|editor",
    "references": ["AVATAR","PRODUCT-STORE", ...],         // only for lane ai
    "image_prompt": "full Nano Banana Pro prompt ...",      // only for lane ai
    "video_prompt": "full Kling 3.0 prompt WITH the spoken line embedded ...", // only for lane ai
    "kling_seconds": 5,
    "pexels_search": "...",                                  // only for lane broll
    "editor_note": "..."                                    // only for lane editor
   }
 ],
 "anchors_first": ["which 1-2 of THIS ad's images define the look and should be generated/approved first"],
 "generation_count": {"ai_images": 0, "broll_clips": 0}
}
```
Validate: JSON loads; every `ai` shot has image_prompt + video_prompt + references; dialogue lines are copied verbatim from the storyboard (after the word-swaps already in the storyboard: underwear not briefs, panty liner not liner). Then reply with the file path and 2 lines on choices.

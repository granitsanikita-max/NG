# Leapproof · Storyboard brief (shared by all 6 storyboards)

You are storyboarding ONE finished, locked ad script for Leapproof (leak-resistant plain black underwear for 30–45 women who leak a little on a sneeze/laugh/jump). The script is the source of truth: keep every spoken line and its meaning. Your job is to turn it into the most engaging, fast-cut, shot-by-shot storyboard possible, plan how the visual hook gets built, and give the best scroll-stopping text hook. NO generation of any kind (no Higgsfield, no ElevenLabs, no video/image tools). Read-only research + writing JSON.

## Inputs
- Scripts (final, chiefed): `/home/user/NG/brand/leapproof/ads/first-campaign/scripts/scripts_v1_v2.json` — a list; pick yours by `ad_id`. Use `beats`, `pulled`, `cuts`, `end_card`, `compliance_check`, `open_questions_for_nikita`.
- Miro visual-hook library: `/tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/plan/miro_hooks_compact.json` (fields: no, name, what_you_see, why_it_works, use_it, examples with WinningHunter links).
- Reference-ad contact sheets (1 frame/second, first 24s, 6 columns × 4 rows, read left→right): `/tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/sb/vids/<ad_id>.sheet.jpg`. Ref cards/transcripts: `/tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/adlab/kits/<ad_id>/card.txt`. LOOK at your refs' sheets (Read the jpg).
- Proven hook wording: `/home/user/NG/brand/leapproof/ads/AD_RESEARCH.md` §3.
- Brand rules: CLAUDE.md (already in your context) + `/home/user/NG/brand/leapproof/BRAND_BIBLE.md` (voice, banned words, §17 brand look).

## What the research measured (ffmpeg scene-cut detection on the actual reference videos)
| Ref | What it is | Avg shot | Cuts 0–3s | Cuts 3–10s | Look |
|---|---|---|---|---|---|
| 896552676720439 UltraDries (video **#6** by impressions on its page) | VO over b-roll, real-UGC look | **2.6s** | 0 | **8** | Hook = woman tossing a handful of pads AT the lens, held 3.0s with a white-box caption mid-frame on frame 0. Then a new location/person/subject on EVERY cut: factory, woman pulling down disposables, hands holding a pair up, doctor's office, older woman to camera, woman in black underwear. Never the same room twice in a row. |
| 1206351388295667 Everdries (video #14, 275 days) | POV problem-object hook + hands b-roll | 5.5s | 0 | 2 | Hook = POV down at underwear with a stained pad, emoji pops in at ~1s, text "it's 2025! Why are you still using pads?" held 3.4s. Then hands handling a pad on a bed (with in-shot motion: flip, point, unwrap), then on-body pull-ups. |
| 1730018818434803 Everdries (not in top 30) | Hand demo, one long take | **18s** | 0 | 0 | ANTI-PATTERN: a 41s unbroken hold. This is what we are NOT doing. |
| 1400650075258672 UltraDries Pixar (video **#4**, 104 days) | 3D talking pad + grandma | 3.6s | 0 | 2 | Word-by-word yellow captions centre. EVERY cut moves the talking pad to a NEW ROOM (living room → bathroom vanity → bedroom → kitchen table → bedside), with the woman in the background reacting. Character changes angle/size each cut. |
| 1700150534480418 Everdries (208 days) | Talking objects (pad, liner, diaper) | 3.8s | 1 | 1 | Each object lives in its own room (pad on marble bathroom counter, liner on tub edge, diaper on a washing machine). Pink pill caption per phrase. Weakness: each speaker holds ~7s — too long. |
| 1691171645641479 UltraDries | Pad vs Underwear talking duet on a bed | 4.8s | 0 | 2 | Title strap "Disposable Pad Vs ULTRADRIES Underwear" top. White-box captions mid-frame. Both characters in a two-shot; reframes/punch-ins every ~2–3s on the speaker, then cuts to a human/demo insert. |

**Pacing law for our storyboards (research + the storyboard skill's pacing brain, reconciled):**
1. **The hook is ONE continuous shot (~1.5–3s) with 2–3 motion events INSIDE it** (jolt, grab, lunge, push-in, emoji/text pop) — a visual change roughly every 0.7–1s without breaking the frame-1 read. Every top ref holds its hook shot ~3s; none hard-cuts inside 0–3s. Frame 0 is never static, never dark, and carries the text hook.
2. **3–10s is the fastest section**: a new visual every 1–2s (the #6 winner puts 8 cuts here). This is where we lose people, so this is where we cut hardest.
3. **10s→CTA**: 2–3s shots. A product hold may run 3–4s only if something moves in it (stretch, turn, pull-up). **No frame ever sits static >3s.**
4. **Talking characters / any on-camera person**: never hold one angle >2.5–3s. Change angle (wide two-shot / MCU / CU / ECU lean-in / low-angle hero / high-angle deflated / over-the-shoulder) or **change room/location** on line changes, like the #4 Pixar winner. An edit-side punch-in (110–125% scale) on an emphasis word counts as an angle change and costs no generation — use them, but generate at the highest resolution so punch-ins stay sharp.
5. **End card**: 3–5s, with motion (button pulse, product slide-in, character micro-action). Button on screen the whole time.
6. **B-roll density**: V1 is faceless VO-over-b-roll: target 70%+ of runtime is b-roll/product, the rest cards. V2 is a character duet: target ≥25–35% non-two-shot coverage (inserts, location hops, real-look product cuts) so it never feels like one static set.
7. Cut on the VO/dialogue beat (word-locked), and put an SFX on every cut in the first 10s.
8. Check VO fits: spoken words ÷ ~2.4 words/sec must fit each shot's duration. Flag any beat where the line doesn't fit and propose the trim (don't silently rewrite lines).

## Caption / text style (what winners use → ours)
Winners: high-contrast boxed captions mid-frame (white box + black text), a pink pill per phrase, or word-by-word yellow. Ours: Hanken Grotesk ExtraBold, Plum Ink #231017 on a Warm Cream #F5EDE6 box (body captions), or a **Claret #A33154 pill with cream text** for the HOOK (max contrast). Fraunces only for the brand line on the end card. Safe zone: 9:16 frame, keep all text inside the centre 4:5 crop, between ~14% and ~62% from the top (clear of the IG/FB bottom UI and top bar). Max ~7 words readable in 0.5s for the hook. Captions are added in the editor (CapCut), NEVER inside an AI prompt.

## Word rule (Nikita, 2026-10-14 — applies to ALL on-screen text and VO)
Nikita doesn't know the words "brief" or "liner" and neither does the ICP in Australia. So:
- "brief / briefs / black brief" → **"underwear" / "black underwear" / "plain black underwear"** everywhere (captions, VO, labels, end card). The V2 character is "the underwear" (label "underwear").
- "liner" → **"panty liner"** on the first on-screen mention / label (hook text, character label), plain "liner" is fine after that in fast captions only if space is tight. "pad" is the umbrella word the ICP knows ("Not a pad, not a diaper." stays).
- List every swap you apply in `word_swaps_applied` (old → new, where).

## Hard rules (compliance; any break = rewrite the shot)
- Never: "incontinence", "discreet", "dignity", "protection" in any text/VO. No absolute leak claims ("never leak", "100%", "leakproof"). "leak-resistant" and "for the sneeze, the laugh and the jump" stay OUT until the wear test is logged. "hold" only inside the 30-night guarantee line. "diaper" only as "not a diaper".
- CJ claims column: no mechanism (no Leak-Lock, no layers diagram), no ml/volume, no pour/water demo, no "built for pee, not blood", no attacking period underwear, no claim that pads fail (form-only attributes are OK: bunches, shifts, feels like a diaper, in the trash).
- No fake doctors, reviews, stars, urgency, prices, gifts on screen. No children. No alcohol props. No stains/yellowing on any liner. No real brand logos.
- Body shots: side-on, waist-to-knee, getting dressed only (leggings pull-up), top covering the hip, never crotch/butt framing, no leak acted, no sneeze/jump/laugh performed AFTER the product appears.
- A human acting the leak moment = "Dramatization" label on those frames. AI people/characters = AI disclosure ("AI-generated" label per script) + C2PA kept on export.
- Meta personal-attributes rule: text must not assert the viewer's condition ("you leak", "your bladder"). Third-person / moment-led is fine ("Sneeze. Little pee." / "For anyone who's crossed her legs before a sneeze").
- Product = the real CJ SKU CJNSNYNK00343: plain black, no lace, no logo. Every product frame is built from the 5 real sample photos (NOT in hand yet → mark those shots BLOCKED-on-photos and give the fallback).

## Production lanes + tools (generator NOT confirmed by Nikita → every tool is a RECOMMENDATION, write no tool prompts)
Tag every shot with one `source_lane`:
- `editor` — text cards, end card, freeze-frames, punch-ins, rewinds, wipes done in CapCut/Premiere (no generation cost).
- `owned-phone` — real product b-roll Nikita films on his phone when the samples land (preferred for hands-on-product shots: zero AI drift, cheapest, most real).
- `AI start frame + motion` — Nano Banana Pro still (Higgsfield, 9:16, 2k) locked first frame, then animate.
- `AI text-to-video` — generic b-roll the video tool can start itself (no start frame needed).
Recommended motion tools (to confirm): Kling 2.x/3.0 for one-action b-roll (5s min clip: generate 5s, use the best 1–2s), Veo 3.1 (~8s, start frame, native audio) for any shot with a spoken line or lip-sync-critical face, Seedance (~15s, multi-cut, @elements, native audio) if Nikita wants multi-shot character sequences in one gen. Voices: ElevenLabs (V1 brand narrator; V2 two distinct character voices — liner higher/fussy, underwear warm/dry). Multi-speaker rule: two distinct voices; one speaker per talking clip (the non-speaker reacts silently); never single-track lip-sync two faces.
Credits gate: list ≤2 look-defining ANCHORS to generate first (approve before batching). Count an honest generation estimate (stills + video gens + lip-sync passes).

## Shot naming
People: `F#-ROLE-angle` (e.g. F3-WOMAN-side-waist). Product/b-roll/graphic/card: `S#-PROD-*`, `S#-BR-*`, `S#-GFX-*`, `S#-CARD-*`. V2 characters: `F#-LINER-mcu`, `F#-UNDIES-lowangle`, `F#-DUO-wide`.

## Output
Write ONE JSON file (UTF-8, valid JSON, use json.dump via python to be safe) to `/tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/sb/out/<AD_ID>.json` with exactly this shape:
```
{
 "ad_id": "...", "title": "short human title",
 "format_analysis": {
   "format": "what format this is, in plain words",
   "how_it_should_look": "the look & feel: realism level, lighting, palette, camera feel (phone-grain / locked tripod / Pixar), caption style, sound bed",
   "runtime_main": "e.g. 35s", "aspect": "9:16 (4:5-safe)",
   "build_profile": "per section: faceless vs on-camera; voice path; who/what voices it",
   "reference_ads": [{"id": "...", "url": "https://www.facebook.com/ads/library/?id=...", "what_we_take": "the specific move we copy"}]
 },
 "text_hook": {
   "recommended": {"text": "...", "on_screen_timing": "0.0s–…", "style": "pill/box, colour, size, position", "why": "why it stops the scroll; which proven hook it's built on"},
   "alternates": [{"text": "...", "why": "...", "proven_anchor": "exact proven hook + days live it's built on"}],
   "note": "if the recommended differs from the locked script, say so: Nikita chiefs it"
 },
 "visual_hook_build": {
   "miro": "#NN Name", "frame_1": "exactly what frame 1 shows",
   "build_steps": ["step 1 ...", "step 2 ..."], "lane_and_tool": "...", "fallback": "...", "failure_modes_to_reject": ["..."]
 },
 "shots": [ {"shot_id": "S1-BR-handbag-pov", "t_in": 0.0, "t_out": 1.4, "section": "HOOK|SETUP|BODY|REVEAL|PROOF|CTA|END",
   "shot_type": "ECU/CU/MCU/wide/POV/insert/card", "angle_or_room": "...", "what_we_see": "...", "motion_inside_shot": "...",
   "on_screen_text": "...", "vo_or_dialogue": "... (speaker)", "sfx": "...", "cut_reason": "why it cuts exactly here",
   "source_lane": "editor|owned-phone|AI start frame + motion|AI text-to-video", "tool_rec": "...", "blocked_on": "" } ],
 "pacing_check": {"total_shots": 0, "avg_shot_len_s": 0, "longest_hold_s": 0, "cuts_0_3s": 0, "cuts_3_10s": 0, "cuts_10s_end": 0, "broll_or_insert_share": "e.g. 72%", "vo_fit_issues": ["..."], "notes": "how this beats the refs"},
 "broll_map": ["each b-roll/insert scene and the exact second it lands"],
 "anchors_first": ["≤2 look-defining anchors to generate and approve first, and why"],
 "assets_needed": [{"asset": "...", "lane": "...", "status": "ready / needs CJ photos / needs Nikita"}],
 "generation_estimate": "stills N, video gens N, lip-sync passes N (floor)",
 "word_swaps_applied": ["old → new (where)"],
 "compliance_flags": ["anything in the script or your board that needs Nikita's call"],
 "open_for_nikita": ["max 4 crisp decisions"]
}
```
Storyboard the MAIN cut only (its full runtime, every second accounted for, no gaps/overlaps in t_in/t_out). Mention how the long cut differs in ONE line inside pacing_check.notes. Be concrete and visual in every shot ("hand lunges from bottom-right, closes on the panty liner, motion blur") — no vague "b-roll of product". After writing, re-open the file with python and validate: JSON loads, shots contiguous from 0 to the runtime, every shot ≤3.0s except product holds with motion (≤4s) and the end card (≤5s). Fix and rewrite until it passes. Your final message: the file path + 3 lines on the biggest choices you made.

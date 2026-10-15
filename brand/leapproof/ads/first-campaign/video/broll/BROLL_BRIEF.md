# Leapproof — B-ROLL HUNT brief (overnight, 2026-10-15)

Goal: for every b-roll slot in your group, find the best REAL stock clips, **actually watch them** (frame sheets),
and pick a PRIMARY + 2 BACKUPS with exact in/out seconds. Nikita cuts these into the ads tomorrow.
**Do not generate anything** (no Higgsfield/Kling/image generation calls).

`SB = /tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/sb`

## Inputs
- Slots: `SB/broll/broll_needs.json` — filter to your group (`group` field). Each slot has the ad, shot_id,
  `on_screen_s` (real on-screen duration from the recorded VO), `vo_over_it`, and the storyboard brief
  (`what_we_see`, `angle`, `motion`, `on_screen_text`, `sfx`, `cut_reason`), `is_our_product`, `priority`.
  `priority: core` = Format 1 (do these first and best). `bonus (Format 2)` = do after the core slots.
- Brand context is in the repo CLAUDE.md you were given (palette: cream #F5EDE6, blush #E7CFC9, claret, plum).
  Ad audience: active women 30–45 who leak a little on a sneeze/laugh/jump. Tone: warm, wry, everyday, bright.

## Tools (scripts in `SB/broll/tools`; run as `python3 -I <script>`; work ONLY inside your own dir `SB/broll/dl/<GROUP>/`)
- `search.py pexels "query" --orient portrait --n 40` (also `--orient landscape|any`)
- `search.py pixabay "query" --n 40` · `search.py mixkit "query"` · `search.py coverr "query"`
  → JSONL lines: src, id, page, dur, w, h, thumbs[], sd (small mp4 for watching), hd (direct download link).
  Save each search to a .jsonl file so you can sheet it.
- `sheet.py out.jpg cands.jsonl` → contact sheet of up to 24 candidates (Pexels shows first/mid/last frame;
  others one poster). Use it to triage quickly. Read the jpg.
- `frames.py out.jpg "<sd_url>" [every_s] [max_frames]` → downloads to a temp dir, extracts timestamped frames,
  builds a sheet, deletes the video. **Run it on every finalist before choosing — you must see what happens across
  the whole clip** (people walking in, logos appearing, faces turning to camera, lighting changes, blood, etc.).
  Read the jpg. Use `every_s` 0.4–1.0 depending on clip length.
- Pexels API key is shared across all hunters (25k/month, fine) — still, don't loop thousands of calls.

## Search strategy
- ≥ 4 query variants per slot across ≥ 2 sites. Start with Pexels `--orient portrait` (native 9:16, often 4K),
  then Pexels any/landscape, Pixabay, Mixkit, Coverr. Think like an editor: synonyms, the object, the action,
  the setting, the mood ("pantyliner", "sanitary pad", "feminine pad", "pad in hand", "peeling sticker",
  "trash can lid", "pedal bin", "woman purse inside", "laundry airer", etc.).
- Triage with `sheet.py`, then watch 3–6 finalists per slot with `frames.py`.
- If one clip serves several slots (e.g. the bin series, recurring handbag), say so and give separate in/out
  windows per slot — consistent footage across a sequence is GOOD.

## Hard rules (reject a clip if it breaks one — unless trivially croppable; then say exactly how)
1. No visible brand names, logos, or readable packaging text.
2. No blood, no red or blue liquid "absorbency" demos, no period framing (tampons, menstrual cups, period calendars),
   no medical/clinical settings, no pills.
3. No children.
4. **No identifiable faces of stock models.** Hands / POV / objects / back-of-head / cropped-below-the-chin are fine.
   This is a bladder-leak ad: showing an identifiable stock person implies they have the condition (stock licence
   "sensitive use" problem + Meta personal-attribute risk).
5. Look: bright, warm or neutral natural light; cream / blush / beige / soft neutrals fit; avoid dark, gritty,
   clinical, neon, cluttered. Clean, believable homes.
6. Must be 9:16 native OR croppable to 9:16 with the subject inside the centre third — state the crop
   ("4K 16:9 → centre crop, subject at x≈0.45").
7. The usable segment must be ≥ the slot's `on_screen_s` (or ≥ on_screen_s/1.5 if a ≤150 % speed-up still looks
   natural — state the speed).
8. Licence: Pexels, Pixabay, Mixkit, Coverr = free for commercial use, no attribution. Avoid Vecteezy, Videvo,
   Shutterstock, Freepik etc. (licence friction) unless nothing else exists — then flag it.
9. First-person hands should read as one adult woman: ideally fair skin (the AI woman is fair with light freckles),
   natural nails, no loud nail art, no men's hands.
10. Panty liners must look like clean, thin, white liners (wingless preferred); never soiled, never coloured liquid.
11. **Our product** (`is_our_product: true` — plain black seamless briefs, laser-cut raw edges, ruched side gathers,
    no lace, no logo, no elastic logo band): stock can NEVER show our exact product. Find the closest stand-ins
    (plain black, no lace, no logo, full brief cut, on cream/neutral backgrounds, hands handling them), set verdict
    `stand_in`, and say the real path: film the CJ samples (SKU CJNSNYNK00343) on a phone, or AI-generate it.

## Per-slot output (verdict + picks)
- `verdict`: `stock_ok` (great fit) | `stock_partial` (usable with a caveat) | `stand_in` (product stand-in only) |
  `no_stock` (nothing usable — needs AI or own phone footage).
- `primary` and `backups` (up to 2): src, id, page_url, hd_url (direct mp4 download), clip_duration, resolution,
  use_in, use_out (seconds in the SOURCE clip), speed_pct, crop_note, what_happens (what YOU saw in the frame sheet,
  by time), fit_score (1–10), why_it_fits, risks.
- `queries_tried`.
- `ai_fallback_prompt` — REQUIRED whenever verdict ≠ stock_ok: a Kling 3.0 **text-to-video** prompt (9:16, Pro,
  Sound OFF, give the seconds 3–5) that would create the exact shot (photoreal, phone-b-roll look, the same brand
  rules: no faces, no logos, clean white liner / generic beige cotton briefs for "the old way" shots, never black
  briefs for liner shots so nobody confuses them with our product).
- Also return `group_notes`: consistency advice for the editor (grading, which shots should share a clip, etc.).

# Leapproof first campaign — VO timing & cut lists (from Nikita's ElevenLabs recordings, 2026-10-15)

Recordings: Erin – Warm & Calm, ElevenLabs v4. Word timing via Whisper large-v3 word timestamps, cross-checked against the audio's real silence boundaries (Whisper word *ends* absorb pauses, so cuts are anchored to speech onsets).

## Runtimes (all 6 ads)

| Ad | Format | Recording | VO length | Final runtime | VO edit needed |
|---|---|---|---|---|---|
| V1-a | 1 · VO over b-roll | rec1_111733.mp3 (ElevenLabs 11:17:33) | 29.73s | **30.5s** | None. Use the recording as-is from 0.00. Optional: trim the opening [sigh] (0.12-0.61) for a snappier hook — every time below then shifts -0.5s. |
| V1-b | 1 · VO over b-roll | rec2_111901.mp3 (ElevenLabs 11:19:01) | 32.03s | **33.6s** | ONE EDIT: split the VO at 2.80 (right after 'myself!') and insert 1.00s of silence (record-scratch SFX + freeze frame). Everything after 'myself!' shifts +1.00s. Without it the freeze caption gets only 0.47s and can't be read. |
| V1-c | 1 · VO over b-roll | rec3_111941.mp3 (ElevenLabs 11:19:41) | 28.60s | **31.7s** | Place the VO starting at 2.40s (the first 2.40s is the silent text hook + sneeze/swipe SFX, per storyboard). No other edits. |
| V2-a | 2 · Pixar duet | — (Kling voices the characters) | — | **30.0s** (storyboard) | Off-screen lines via ElevenLabs |
| V2-b | 2 · Pixar duet | — (Kling voices the characters) | — | **31.2s** (storyboard) | Off-screen lines via ElevenLabs |
| V2-c | 2 · Pixar duet | — (Kling voices the characters) | — | **33.0s** (storyboard) | Off-screen lines via ElevenLabs |

Kling 3.0 can't make clips shorter than 3s, so every Format 1 AI clip is generated at 3s+ and trimmed (or sped up ≤200%) to its on-screen window. Exact per-clip settings are in the prompt doc.


## V1-a — cut list (30.5s)

**VO placement:** None. Use the recording as-is from 0.00. Optional: trim the opening [sigh] (0.12-0.61) for a snappier hook — every time below then shifts -0.5s.

| In | Out | Dur | Source | Shot | VO over it |
|---|---|---|---|---|---|
| 0.00 | 2.95 | 2.95s | B-roll | S1-BR-handbag-pov | [ACHOO SFX 0.00-0.30] [sigh] 'Sneeze. Little pee.' |
| 2.95 | 5.15 | 2.20s | B-roll | S2-BR-car-liner-holdup | 'Still packing a spare panty liner?' |
| 5.15 | 6.85 | 1.70s | B-roll | S3-BR-bed-stick-topdown | 'Here's that liner's day.' |
| 6.85 | 7.95 | 1.10s | B-roll | S4-BR-bed-bunch-ecu | 'It bunches.' |
| 7.95 | 8.90 | 0.95s | B-roll | S5-BR-vanity-shift | 'It shifts.' |
| 8.90 | 10.55 | 1.65s | B-roll | S6-BR-gymbag-crinkle | 'It feels like a diaper.' |
| 10.55 | 12.25 | 1.70s | B-roll | S7-BR-bin-night | 'Another one in the trash.' |
| 12.25 | 12.55 | 0.30s | Product b-roll | S8-PROD-flash-stretch | (0.3s flash under 'Tomorrow,') |
| 12.55 | 13.55 | 1.00s | B-roll | S9-BR-hallway-drop | 'Tomorrow, a new one.' |
| 13.55 | 14.00 | 0.45s | B-roll | S10-BR-handbag-pov-zip | (silent zip beat) |
| 14.00 | 15.95 | 1.95s | Product b-roll | S11-PROD-stretch-hands | 'Or... it could just be underwear.' |
| 15.95 | 17.65 | 1.70s | Product b-roll | S12-PROD-flatlay-smooth | 'Plain black underwear.' |
| 17.65 | 18.48 | 0.83s | AI clip (Kling) | F13-WOMAN-side-waist | 'Pull them on' |
| 18.48 | 18.48 | 0.00s | — dropped — | F14-WOMAN-side-waist-punchin | DROPPED — the read has no comma pause after 'on' |
| 18.48 | 19.30 | 0.82s | AI clip (Kling) | F15-WOMAN-carboot-wide | 'and go about' |
| 19.30 | 19.95 | 0.65s | AI clip (Kling) | F16-WOMAN-boot-pov-low | 'the day.' |
| 19.95 | 20.85 | 0.90s | AI clip (Kling) | F17-WOMAN-boot-close-mcu | 'Not a pad.' |
| 20.85 | 21.95 | 1.10s | AI clip (Kling) | F18-WOMAN-walkoff-wide | 'Not a diaper.' |
| 21.95 | 23.05 | 1.10s | Product b-roll | S19-PROD-fold-cream | 'Take the quiz.' |
| 23.05 | 25.20 | 2.15s | CapCut/editor | S20-GFX-quiz-chips | 'It finds your size and how many pairs.' |
| 25.20 | 30.50 | 5.30s | CapCut/editor | S21-CARD-end | 'Wear them through your moment for 30 nights. If they don't hold, you get your money back.' (+0.8s hold) |

## V1-b — cut list (33.6s)

**VO placement:** ONE EDIT: split the VO at 2.80 (right after 'myself!') and insert 1.00s of silence (record-scratch SFX + freeze frame). Everything after 'myself!' shifts +1.00s. Without it the freeze caption gets only 0.47s and can't be read.

| In | Out | Dur | Source | Shot | VO over it |
|---|---|---|---|---|---|
| 0.00 | 2.80 | 2.80s | AI clip (Kling) | F1-WOMAN-wide-side-twoshot | 'Stop! I'll pee myself!' (ElevenLabs line plays as her laugh-shout) |
| 2.80 | 3.95 | 1.15s | CapCut/editor | S2-GFX-freeze-scratch | (inserted 1.0s gap: freeze F1's last frame + record scratch; caption pops) |
| 3.95 | 4.60 | 0.65s | CapCut/editor | S3-GFX-rewind-smear | 'Three hours' |
| 4.60 | 7.15 | 2.55s | B-roll | S4-BR-liner-at-lens | '...earlier. The plan?' |
| 7.15 | 8.45 | 1.30s | B-roll | S5-BR-liner-peel-ecu | 'A panty liner.' |
| 8.45 | 10.05 | 1.60s | B-roll | S6-BR-liner-press-in-topdown | 'But a panty liner' |
| 10.05 | 10.98 | 0.93s | B-roll | S7-BR-liner-bunch-ecu | 'bunches.' |
| 10.98 | 12.15 | 1.17s | B-roll | S8-BR-liner-shift-side | 'It shifts.' |
| 12.15 | 13.30 | 1.15s | B-roll | S9-BR-liner-pinch-side | 'It feels like a' |
| 13.30 | 14.30 | 1.00s | CapCut/editor | S9-BR-liner-pinch-punch | 'diaper.' (CapCut punch-in on S9 footage) |
| 14.30 | 15.24 | 0.94s | B-roll | S10-BR-liner-fold-night | 'And by tonight,' |
| 15.24 | 16.75 | 1.51s | B-roll | S11-BR-bin-drop | 'it's in the trash.' |
| 16.75 | 19.95 | 3.20s | Product b-roll | S12-PROD-reveal-match | 'Or... just underwear. Plain black underwear.' |
| 19.95 | 21.95 | 2.00s | Product b-roll | S13-PROD-turn-mcu | 'Not a pad, not a diaper.' |
| 21.95 | 24.20 | 2.25s | AI clip (Kling) | F9-WOMAN-side-waist-pullup | 'Just underwear. Wash, hang,' |
| 24.20 | 25.10 | 0.90s | B-roll | S14-BR-hall-clutch-grab | 'wear again.' |
| 25.10 | 26.25 | 1.15s | AI clip (Kling) | S15-BR-table-clutch-set | 'For the woman who'd rather' |
| 26.25 | 28.00 | 1.75s | AI clip (Kling) | F12-WOMAN-34-single | 'laugh than cross her legs.' |
| 28.00 | 28.00 | 0.00s | — dropped — | F12-WOMAN-34-single-punch | DROPPED — the read has no breath before the end card |
| 28.00 | 33.60 | 5.60s | CapCut/editor | S16-CARD-end | 'Not a pad, not a diaper. 30 nights to see if they hold. Find my match.' (+0.7s hold) |

## V1-c — cut list (31.7s)

**VO placement:** Place the VO starting at 2.40s (the first 2.40s is the silent text hook + sneeze/swipe SFX, per storyboard). No other edits.

| In | Out | Dur | Source | Shot | VO over it |
|---|---|---|---|---|---|
| 0.00 | 1.20 | 1.20s | B-roll | S1-PROD-liner-at-lens | (no VO; sneeze SFX; pill 'The sneeze-pee plan: a sticker.') |
| 1.20 | 2.40 | 1.20s | Product b-roll | S2-PROD-underwear-wipe-reveal | (no VO; 'Or... underwear. Not a pad, not a diaper.') |
| 2.40 | 3.40 | 1.00s | B-roll | S3-BR-peel-sticker | 'A panty liner' |
| 3.40 | 4.40 | 1.00s | B-roll | S4-BR-bin-3q-lid-open | 'lasts a day.' |
| 4.40 | 5.45 | 1.05s | B-roll | S5-BR-bin-topdown-MON | 'Then it's gone.' |
| 5.45 | 6.58 | 1.13s | B-roll | S6-BR-bin-3q-115-TUE | 'It bunches.' |
| 6.58 | 7.50 | 0.92s | B-roll | S7-BR-bin-topdown-WED | 'It shifts.' |
| 7.50 | 8.45 | 0.95s | B-roll | S8-BR-bin-3q-130-THU | 'It feels like a' |
| 8.45 | 9.55 | 1.10s | B-roll | S9-BR-bin-topdown-130-pile | 'diaper.' |
| 9.55 | 11.35 | 1.80s | B-roll | S10-BR-bin-3q-dusk-lid-slam | 'By tonight, the bin.' |
| 11.35 | 13.15 | 1.80s | B-roll | S11-PROD-liner-at-lens-FRI | 'Tomorrow, a new one.' |
| 13.15 | 16.30 | 3.15s | Product b-roll | S12-PROD-underwear-rewipe-turn | 'Or there's underwear. Plain black underwear.' |
| 16.30 | 17.20 | 0.90s | B-roll | S13-BR-wash-drum | 'Wash,' |
| 17.20 | 17.85 | 0.65s | B-roll | S14-BR-hang-airer | 'hang,' |
| 17.85 | 18.70 | 0.85s | B-roll | S15-BR-drawer-wear-again | 'wear again.' |
| 18.70 | 20.25 | 1.55s | Product b-roll | S16-PROD-flatlay-front | 'One pair. Washed,' |
| 20.25 | 22.15 | 1.90s | Product b-roll | S17-PROD-flatlay-flip-back | 'worn again, not binned.' |
| 22.15 | 23.25 | 1.10s | AI clip (Kling) | F1-WOMAN-side-waist-pullup | 'Not a pad.' |
| 23.25 | 24.55 | 1.30s | AI clip (Kling) | F2-WOMAN-ecu-waistband-snap | 'Not a diaper.' |
| 24.55 | 25.30 | 0.75s | AI clip (Kling) | F3-WOMAN-hall-wide-tote | 'Just get' |
| 25.30 | 26.20 | 0.90s | AI clip (Kling) | F4-WOMAN-ots-door-sun | 'dressed and go.' |
| 26.20 | 27.10 | 0.90s | AI clip (Kling) | F5-WOMAN-ext-friend-coffee | 'The 30-night' |
| 27.10 | 27.90 | 0.80s | Product b-roll | S18-PROD-bookend-at-lens | 'leak test.' |
| 27.90 | 31.70 | 3.80s | CapCut/editor | S19-CARD-endcard | '30 nights to see if they hold. Find your match.' (+0.9s hold) |

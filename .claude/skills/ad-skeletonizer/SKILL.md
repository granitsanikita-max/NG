---
name: ad-skeletonizer
description: >-
  The second half of Nikita's swipe pipeline. Reads the APPROVED rows in his Notion "Ad Finds — To
  Review" database (ads the ad-finder skill logged and Nikita greenlit), watches each ad, tears it
  into an exact copyable beat-by-beat skeleton (every beat's function, the loops, the authority, the
  psychology, the pivot words, core rules, and how to steal it with our product), files each skeleton
  into the Notion Ad Swipe File, and flips the row to Filed. Use whenever Nikita says "skeletonize my
  approved ads", "run the skeletonizer", "tear down my approved finds", "turn my ad finds into
  structures", "process the ad finds", or after he's reviewed the Ad Finds list and approved rows.
  Can also skeletonize one specific ad link on demand.
---

# Ad Skeletonizer

Takes the ads Nikita approved in **Ad Finds — To Review** and turns each into a blueprint he can build his own ad from, then files it into the swipe file. This is the teardown step — deliberately separate from finding, so Nikita only spends teardown effort on ads he's already judged worth it.

The output is the whole point: a **surgical, copyable skeleton** (not a summary). Read `references/skeleton-format.md` before writing a single one and follow it exactly — it defines the format, the depth, and the levers to capture (loops, authority, proof, pivot words, belief, enemy, blame removal, community, product placement).

## Step 1 — Pull the approved finds

Query the **Ad Finds — To Review** database for rows where `Status = Approved`.
- Data source: `collection://32981cf7-fc4d-4e06-a849-5f6173a312a6`. **Fetch it first** to confirm the live schema, then query.
- If Nikita instead pasted a specific ad link, skip the query and just work that link.
- If there are no Approved rows, tell him plainly and stop — nothing to do until he approves some.

## Step 2 — Watch each ad

For each approved ad you need the real content, not the metadata:
- If Winning Hunter has a transcript for it: `get_ad_transcript`.
- Otherwise run the **`watch` skill** on the ad's video URL (`--detail balanced`) for a timestamped transcript + frames (text overlays, cuts, shot types, pacing). Caption-less ads need the Whisper key set (see the watch skill).
- You need BOTH the words and the visuals — the skeleton captures spoken beats AND on-screen/text-overlay beats.

## Step 3 — Tear it into a copyable skeleton

Follow `references/skeleton-format.md` precisely. Non-negotiables (they're what make it copyable, not just readable):
- **Derive the beats from the evidence** — map what the ad actually does, in order. Never force a preset template.
- **Every beat names its FUNCTION** (what it does to the viewer), not just its content.
- **Track the loops** — mark where each curiosity loop opens and closes; surface the "never close a loop without opening another" law if the ad uses it.
- **Tag the psychology** on each beat — authority (self/outside), proof (picture-able?), belief tapped, common enemy, blame removal, pivot words ("but"/"so"), community, where the product finally enters.
- **End with "STEAL THIS"** — map each beat to Nikita's own product/offer, grounded in his real brand research, never invented specs, so it's ready to write against.

## Step 4 — File it into the Ad Swipe File

Use the `add-to-notion` skill's conventions (fetch each destination's schema first; never guess IDs):
1. **Whole Ad Structures page** — add the full skeleton as a `## Heading` (the structure's name) + a fenced code block holding the beat-by-beat text, matching the style already on that page.
2. **Video Ad Formats DB** — add a row: Name, Niche, Format Type, Hook Type, Advertiser (the store), Source Link, Why It Works ("run [X], [store] does [$Y]/mo"), Status = Swiped. Leave Awareness/Funnel blank unless the ad makes the stage genuinely obvious (Nikita's rule: don't guess the stage).

## Step 5 — Close the loop on the row

For each ad processed, update its row in **Ad Finds — To Review**: set `Status = Filed` (so it's never processed twice and the list stays a clean queue). Then report one line per ad: structure name → where filed → row marked Filed.

## Guardrails
- **Only process Approved rows** — never auto-process New ones; the whole point of the split is Nikita's QA gate.
- **Depth over speed** — a shallow skeleton defeats the purpose. If an ad's transcript/frames are too thin to map real beats, say so and leave the row Approved rather than filing a weak skeleton.
- **Never invent** metrics, beats, or product specs. Ground the "steal this" in real brand research.

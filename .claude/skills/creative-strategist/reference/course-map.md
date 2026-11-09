# Course map — BBA Creative Strategy module (6.01–6.07)

Everything the course teaches, in order. The skill's rules come from here.
Sources: transcripts 6.01, 6.02, 6.04, 6.05, 6.06, 6.07 read in full (6.03 Awareness Levels was never captured; awareness content comes from 6.06 + 6.07), plus the BBA docs: Market Analysis prompts #1–5, DETAILED Image Ad Generation Prompt (Step 2), 6.3 Primary Text & Headline prompt (BOFU tab), Ad Tracking Strategy Master sheet, Mass Desire × Angle output spread.

## 1. What creative strategy is (6.01)
- The decision layer **before** copy or design. Answers "what idea should I test?", not "how should the ad look?".
- For brands already getting sales but stuck on what to test next. Goal: map 25 distinct creatives for any product in under 30 minutes (planning time).
- Random testing → random results: you can't isolate why something won, so you can't repeat it. Scale needs a structured system, not more creativity.
- If you don't know what creative to make next, you have no creative strategy.

## 2. Problems vs desires (6.01)
- **Problems** explain what's broken. They decide **how to speak** (how aware the customer is, how much context they need). They do NOT explain why people buy.
- **Desires** explain motivation: what the customer wants to achieve or become. The transformation is what's sold. Desires decide **creative direction** and which story is worth telling.
- Selling only to problems = commodity advertising; you only reach people already about to buy.
- Every creative must activate ONE desire. Pain-only ads make people nod and scroll on confused; close the loop with the desirable outcome.

## 3. Mass desires (6.02)
- Markets are emotionally fragmented: different segments buy the same product for different reasons. One desire = one slice of the addressable market; that's why single winners fatigue fast.
- A mass desire is a want that **already exists**, shared by a large group, not created by your product. (Examples for a waterproof dog collar/leash: aesthetic identity, public confidence, embarrassment avoidance.)
- Each mass desire = one **creative bucket**. Every ad belongs to exactly one bucket, or a winning bucket can't be read or replicated.
- Find **5 mass desires**: multiple entry points into the same market.
- Example from the course: "I want to stop being physically overpowered by my dog on every walk." Segment: the physically overwhelmed owner, typically women with medium-to-large breeds, recurring arm/wrist/shoulder pain. Deep because it ties to fears of being inadequate, weak, incompetent.

## 4. Angles (6.02, 6.04)
- An angle = **one specific story that activates a desire in a recognisable situation**, a moment of realisation where the viewer connects. NOT a hook or headline; it defines the whole creative idea.
- Same desire, different life situations → different stories trigger it for different people. Multiple angles stop reliance on one narrative that fatigues.
- **5 angles per desire → 25 ads.** Five explore different contexts, fears and moments of realisation, and show which story *patterns* repeat (patterns = confident scaling, vs one-off spikes).
- The angle must unlock a transformation, but the transformation happens at the **desire** level. People recognise the angle (the story); they feel the desire.
- The spreadsheet name of an angle is not enough. Each angle needs full depth:
  - target audience
  - story arc (course example "The Invisible Injury": walks her Labrador for 3 years, walks "work", but her right shoulder aches for months; ices it, blames work tension; sharp pull reaching a shelf; at the physio, lists job/posture/sleep, then, almost embarrassed, mentions the dog walks)
  - unique problem mechanism (cumulative physical trauma from asymmetrical load: same arm, same wrist)
  - unique solution mechanism (changes where/how force is distributed, redirecting the dog through geometry, not grip strength, so the body absorbs near-zero impact)
  - key emotional moment (in the physio's office, realising something she did daily as a "responsible owner" was quietly injuring her)
  - headline candidates pulled from the story: "My dog wasn't being bad. My body was breaking down." / "I was doing the right thing every morning and it was hurting me every morning."

## 5. The research prompt chain (6.04)
Run in ONE chat, web search on, the strongest model available. Read every output yourself: Claude is the strategist's *assistant*, not the strategist.
1. **Market research.** Inputs: product, niche, main competitor + product URL, problem space. Understand the competitor's customers' emotional landscape and the underlying problems the product addresses. Exclude posts complaining about products/brands/specific solutions; prefer detailed emotional narratives over brief mentions; capture internal emotional state, language patterns, specific vocabulary.
2. **Analyse 20 discussions** (mostly Reddit): 20–30 most common phrases, recurring words, demographic-specific jargon, primary emotions, intensity levels, emotional progression (how feelings evolve). Save to its own doc = brand source of truth. Course example summary: loss of physical control on leash, pre-walk/pre-hike dread, dog slipping out of gear, public shame, lifestyle/identity loss ("can't hike anymore"), physical injury from pulling, fear of catastrophic gear failure, guilt and self-blame.
3. **Train Claude as a copywriter** + unique mechanism frameworks. Core psychological shift: "I've tried everything and nothing works" → "Oh, *that's* why nothing worked" → "This is different." The mechanism makes the shift believable and handles objections.
4. **5 dominant mass desires**, with foundational docs + customer avatar docs attached, in a fixed format. Paste into the desire × angle spreadsheet.
5. **5 angles per desire**, one desire at a time, five times. Paste into the spreadsheet (D1A1…D5A5), and keep the full angle detail in a doc.
- Every output goes into its own doc (the 20-discussion analysis especially) = the brand's source of truth, reused later for copy, store and funnel optimisation.
- Prompt #2 needs no edits; it runs in the same chat right after #1. Prompt #4 needs the foundational + customer-avatar docs attached.
- After the 25 are mapped: "understand different creative formats … so that we can **keep the formats consistent**." During the 25-ad test, hold the medium constant (static images) so the only variable is the message (desire × angle).

## 6. Formats × awareness (6.07)
- Different formats do different jobs. **Statics** win on clarity and speed (strongest mid/bottom funnel: offers, benefits, proof, comparisons). **Videos** win on context and emotion (strongest top/mid: UGC, demos, founder stories, mashups). General rules, not laws.
- Static sub-formats:
  - **offer-led**: ready-to-buy; simple, high contrast, offer impossible to miss
  - **product benefits**: 3–5 benefit callouts plus a headline speaking to the audience
  - **before/after**: show the transformation, realistic and compliant
  - **review statics**: trust plus objection handling in the customer's words
  - **organic-looking**: screenshots or stories that blend into the feed; best top of funnel
- Video sub-formats: UGC selfie, product demo, founder story, skit/entertainment, mashup/montage.
- 5 awareness stages: unaware → problem aware → solution aware → product aware → most aware. Meet them where they are; skipping stages fails (an offer means nothing to someone who doesn't know they have the problem). Markets get more sophisticated with exposure, which means more skepticism, so they need more proof.
- **Matrix:**

| Awareness | Static format | Video format |
|---|---|---|
| Problem unaware | Organic screenshot / native | Relatable UGC hook |
| Problem aware | Benefit callouts | Testimonial / UGC |
| Solution aware | Comparison (us vs them) | Product demo / explainer |
| Product aware | Reviews / proof | Founder story / proof |
| Most aware | Offer + urgency | Mashup (reviews + testimonials + offer) |

- Testing: keep it simple, cover every stage with at least one format, avoid over-segmenting. **Group ad sets by message (desire), not by format.** The message is the high-leverage learning; format only matters for how people consume. Scale winners, refresh hooks, recycle footage.

## 7. Making the 25 image ads (6.05)
- Test the messages with **static image ads first**: fast and cheap. Winning desires/angles later get video, carousel, UGC and other formats.
- The old way (pasting competitor ads into the image prompt with no direction) made ads that won without anyone knowing why. The new way injects ONE desire and ONE angle per ad.
- In the detailed image-generation prompt: the angle's **headline** goes in the headline-logic / "new mechanism" slot; the **desire** goes in the desire slot.
- Into Claude: the filled prompt, a clean high-res product photo on plain background, a competitor ad to model, and the brand foundational docs → Claude writes the image-generation prompt.
- Into **Nano Banana Pro**: that prompt plus the same product photo and competitor ad.
- Course example output: headline "My dog wasn't being bad, my equipment was", the desire line, and a proof badge ("47,000+ calmer walks"). Proof numbers must come from the brand's real data.
- If you forget the foundational docs, the prompt asks for them. Never run it without them.
- Repeat 25 times, one by one ("to maintain maximum creative focus and quality"). **Each desire = one ad set** (5 ads). Monitor spend, CTR, CPC, ROAS.
- Image prompt rules (Master Architect doc): product = exact replica (don't over-describe it); hybrid ad with graphic layers (3D badges, ✓/✗ icons, CTA button); max 3 focal points; before = painful, after = aspirational; show the UMS in the "after"; headline = [New Mechanism] + [Angle] with exact placement, bold font and colour; mirror the competitor layout exactly; hyper-real models with dramatised emotion; **always 1:1**; commercial photography (85mm, f/1.8), no stock vibes; high-contrast colours for CTR.

## 8. Tracking, copy, iteration (6.06)
- Tracking sheet (Ad Tracking Strategy Master) columns: ICP Description · Awareness Level · Funnel Stage · Desire · Problems · Angle · Key Objections · Headline · Primary Text · Ad Name · Ad Folder · Spend · ROAS (+ a winner column). Example row: ICP = a named person with age, job, situation and goal ("Sarah, 34, corporate job, 20 iPhone alarms, seniors noticed her late, wants to be seen as reliable"); Problems = the problem-mechanism beliefs as a numbered list; Key Objections = in the customer's own voice ("Nothing works for me because I'm not a morning person…"). It's a template; adapt it.
- Images go into named folders with unique, identifiable names; headline and primary text sit next to each image.
- Mass Desire × Angle output spread: per desire, 5 angle rows with SPEND · CTR · CPC · ROAS.
- The awareness level sets the funnel stage (course example: unaware → problem aware at the physio = TOFU), and the funnel stage picks the headline/primary-text prompt tab. Attach foundational docs + the desire and angle; it generates per desire; pick the one for this ad's desire and give it direction. There's a native long-form option for native-style image ads.
- **Iteration is where scale happens.** Initial testing reveals which *desires* resonate, not just which ads win. Scaling = repeating what works across more angles.
- Reading results:
  - multiple angles win under one desire → strong desire → create more angles (new stories) for it
  - only one angle wins → expand that story before discarding the desire
  - no angles win → the desire is weak, not the execution
  - early wins but no desire with 2–3 winning angles → the mechanism isn't convincing → refine the mechanism to the awareness level
- Budget: **80% iterations, 20% new** (new angles under proven desires, or new desires).
- Loop: test 25 → find the strongest desire/angle patterns → new angles around what repeats → refine awareness and mechanism → repeat 80/20.
- Final rule: not knowing what to make next means a missing clear desire, a missing clear angle, or a mechanism that doesn't land.
- Desires and angles carry over to any format: video scripts (UGC, BSL, testimonial). The core message converts, not the format.

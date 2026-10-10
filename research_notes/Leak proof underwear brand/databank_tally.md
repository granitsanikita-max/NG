# §2C Customer Data Bank — Tally & Swipe File

**Source CSV:** `customer_data_bank.csv` · **Total snippets (real `wc`/csv row count):** 155

All counts below are produced by `python3`/`csv` and `jq` run directly on the CSV (not estimated). Market: US women's leak-proof / stress-incontinence underwear for the active 30s–40s woman (postpartum / early-perimenopause) who leaks on a sneeze/laugh/jump/run and rejects BOTH the diaper/elderly/clinical frame AND the period-underwear frame.

## 1. Totals & source-type breakdown
- **Total rows:** 155  (target was 100+, aim 150+ — met)
- **Solidity:** VERBATIM (page opened, wording confirmed) = 88 · SNIPPET (search-result text) = 67

By source type:
- Reddit: 55
- Trustpilot: 32
- Amazon: 25
- Press/Medical/Blog authority: 18
- Walmart (retail reviews): 10
- PissedConsumer (complaint forum): 5
- Social (IG/FB/Quora): 4
- X/Twitter: 3
- TikTok/YouTube: 3

Review-star splits (the §2C-required Amazon 1–2★ vs 4–5★, plus Walmart retail reviews):
- Amazon 1–2★: 14
- Amazon 4–5★: 9
- Amazon (stars not confirmable — 'Customers say' summary rows): 2
- Walmart 1–2★: 2
- Walmart 4–5★: 7

> Note on sourcing: this product/market skews ELDERLY/postpartum on review sites (Everdries, Because, Always, Attn:Grace are the Amazon/Walmart players), while the *active 30s–40s ICP* lives mostly on Reddit (r/xxfitness, r/crossfit, r/running, r/XXRunning, r/Perimenopause, r/orangetheory) and social. The databank therefore leans Reddit for the ICP voice and review sites for failed-solution / objection evidence.

## 2. Tag tallies (jq/python counts on the file)

### Triggers (what makes her leak) — keyword-grouped
- sneeze: 15
- jump/jumping jacks: 11
- run/running: 10
- cough: 9
- laugh: 7
- deadlift/squat/lift: 7
- double unders: 6
- trampoline: 4
- workout class (OTF/gym): 3
- box jumps: 2
- standing up: 2
- dance: 1
- out all day/errands: 1

_rows carrying a `trigger` tag: 41_

### Pains — keyword-grouped
- leak on sneeze/laugh/cough: 12
- leak jumping/trampoline: 11
- leak when running: 8
- wet feeling / stays wet: 8
- uncomfortable/rides up/bunches: 5
- pee down legs / puddle: 4
- crossing legs / avoiding activity: 4
- leak lifting/deadlift: 3
- visible wet patch at gym: 3
- leaks through / soaked: 3
- had to change/carry spares: 1

_rows carrying a `pain` tag: 78_

### Objections — keyword-grouped
- leaks through / out the sides: 20
- doesn't absorb / no absorbency: 8
- sizing runs small/large/inconsistent: 7
- quality decline / falls apart: 6
- still need a pad: 6
- expensive / waste of money: 6
- wet feeling / feels like diaper: 6
- false advertising / scam / marketing: 5
- only works for tiny leaks: 5
- too thick/bulky/hot/uncomfortable: 4
- PFAS / toxic / UTI / safety: 4
- waistband rolls/tight: 2
- loses absorbency after washes: 1

_rows carrying an `objection` tag: 67_

### Failed solutions — keyword-grouped
- Everdries: 20
- period underwear (Thinx/Knix/Modibodi/Bonds): 19
- pads (period or incontinence): 15
- pelvic floor PT / kegels: 3
- pee before activity: 3
- HRT / surgery / medical: 2
- Always / Depends / Poise / Tena: 2
- cloth diapers / absorbent pants: 2
- spare underwear / carry backup: 1
- tampon / internal support: 1
- Finess patch: 1

_rows carrying a `failed_solution` tag: 65_

### Emotional state (controlled vocab)
- anger: 20
- shame: 11
- desire: 10
- pride: 10
- grief: 8
- fear: 5
- guilt: 1

_rows carrying an `emotional_state` tag: 65_

### Awareness stage (controlled vocab)
- problem-aware: 29
- solution-aware: 20
- product-aware: 19
- most-aware: 4

_rows carrying an `awareness_stage` tag: 72_

### Burned / skeptical
- yes: 46
- skeptical: 3

_rows carrying a `burned` tag: 49_

### Desires — top recurring labels
- confidence: 2
- not have to carry spares: 1
- run and jump without leaking: 1
- comfortable + dry: 1
- worry free: 1
- run without leaking: 1
- quality+comfort+effective: 1
- protection + confidence: 1
- durable daily wear: 1
- replace all other incontinence underwear: 1
- confidence out and about: 1
- it works: 1
- dry and comfy entire run: 1
- never use single-use pads again: 1
- comfortable, works: 1

_rows carrying a `desire` tag: 39_

### Needs — top recurring labels
- workout underwear: 1
- urine-specific absorbency: 1
- workout absorbent underwear: 1
- absorbent for running: 1
- real absorbency for more than a dribble: 1
- coverage for gushes: 1
- better side coverage: 1
- workout underwear for leaks: 1
- wicking/dry feel: 1
- stay-put fit: 1
- absorbent but invisible: 1

_rows carrying a `need` tag: 11_

### Misconceptions — top recurring labels
- period underwear = incontinence underwear: 1
- diet coke caused it: 1
- period pads work for urine: 1
- safe product: 1
- US sizing: 1
- pee-proof = feels like diaper: 1
- leaking is a normal part of aging: 1
- leaking is part of aging: 1
- too thin to work: 1
- menstrual pads work for urine: 1
- pee just happens: 1
- leaking is permanent after birth: 1

_rows carrying a `misconception` tag: 16_

### Beliefs — top recurring labels
- 1 in 4 women have it: 1
- keep it secret: 1
- we have all done it: 1
- leaking is not inevitable: 1
- common post-childbirth and in young women: 1
- common but not normal, fixable: 1
- a lifeline: 1
- brand cutting costs: 1
- brand hid chemicals: 1
- marketing lied: 1
- brand untrustworthy: 1
- brand quality dropped: 1

_rows carrying a `belief` tag: 27_

### Authorities she trusts
- pelvic floor PT: 5
- Always: 2
- Knix: 2
- urogynecologist: 2
- pelvic floor therapist: 1
- Midi NP: 1
- Poise/Always/Tena: 1
- Knix/Thinx: 1
- doctor: 1
- friend recommendation: 1
- pelvic floor physio: 1
- Runner's World: 1
- oncology nurse: 1
- Franciscan Health: 1
- SIU Medicine: 1

_rows carrying an `authority` tag: 31_

### Buyer groups
- runner: 8
- crossfit woman: 5
- postpartum: 5
- postpartum runner: 4
- perimenopause: 3
- pregnant: 2
- mom runner: 2
- postpartum mom: 2
- orangetheory woman: 2
- active 30s woman: 1
- mom of multiple: 1
- menopause: 1
- crossfit mom 30s: 1
- lifter: 1
- medical/dialysis: 1
- older woman: 1
- pelvic floor physio: 1
- female runner: 1

_rows carrying a `buyer_group` tag: 58_

## 3. Great-phrase swipe list (her exact vivid words)
Total `great_phrase` entries: 100

Recurring THEMES across phrases (★ = theme appears in 3+ snippets):
- ★ pee when I sneeze/laugh/cough/jump/run (the trigger litany) — 10 snippets
- ★ doesn't absorb / no absorbency / goes right through — 8 snippets
- ★ confidence / out and about / worry-free — 4 snippets
- ★ common but NOT normal / don't have to pee yourself — 3 snippets
- changed my life / lifeline — 2 snippets
- trampoline / jump rope avoidance — 1 snippets

Full swipe list (verbatim phrases):
- "pee when I cough, sneeze, laugh, jump, run, or get startled"
- "urine is higher in volume than [blood]"
- "1 in 4 women have it"
- "stress urinary incontinence"
- "spent $$$. It worked as long as I kept going"
- "leaking when I jump/cough/sneeze/breathe/whatever"
- "peed in 7 pairs of underwear in the last 3 days"
- "pee when I sneeze problem for years"
- "do all the things without leaking pee"
- "absolutely pee myself during double unders"
- "Trying for a squat PR, pee your pants"
- "I pee myself almost every deadlift"
- "a little leak that might look like a crotch sweat"
- "We. Do. Not. Have. To. Pee. Ourselves."
- "absorb urine so much better than period pads"
- "far more comfortable than incontinence pads"
- "leaked straight through and soaked my pants"
- "completely worry free"
- "the pee will be running down my legs"
- "common but not normal"
- "The concept of going out all day is a fantasy"
- "who has used nylon in underwear beyond the 1970s"
- "severe UTI from the product fabric in the gusset"
- "Chinese produced rubbish"
- "Even with the extra pad they don't hold water"
- "the WHOLE front of them was soaked right through"
- "scared of what would happen if I couldn't get to the bathroom in time"
- "have been a lifeline"
- "confidence it gives me when I am out and about"
- "take ages to dry"
- "rolled right off the pad and out the ill fitting leg"
- "cutting costs on the most important part"
- "PFAS concerns surrounding Thinx"
- "the band around the waist is so unforgiving"
- "I was misled by their marketing"
- "they basically became regular underwear"
- "right through the Thinx underwear as if it was plain underwear"
- "does nothing to absorb even a light amount of incontinence"
- "Leaked so bad on first use, I had to change clothes"
- "hot and uncomfortable"
- "doesn't correlate with American women's clothing sizes"
- "might fit a 12-year-old skinny little girl"
- "gusset did not extend far enough back"
- "walking around in a wet diaper"
- "lose all of their sponge capabilities"
- "the feeling of putting on wet underwear"
- "cold/wet feeling when I use the bathroom and pull them back up"
- "Nothing - I mean nothing - leaked through"
- "I leaked out the sides"
- "they will ruin your pants"
- "leaked so bad over night"
- "all over white towels. Not embarrassing at all"
- "takes all the anxiety away"
- "a level of confidence that is wonderful"
- "FINALLY A PAD THAT REALLY WORKS"
- "can't contain a gravity gusher"
- "when you first stand up in the morning"
- "leaked out the side of the gusset"
- "so disappointed as they claim no leaks"
- "NEVER considered normal"
- "crossing their legs every time they cough or laugh"
- "Bladder Leaks Aren't A Normal Part of Aging"
- "no absorbency at all"
- "I peed on my floor - right through the underwear 3 times this morning"
- "I really wanted to like these"
- "pee will go down your legs"
- "Does not live up to hype"
- "I'm so tired of false ads"
- "I fell for the marketing because I really wanted them to work"
- "I forget I am wearing special underwear"
- "makes me feel more confident when I leave the house"
- "fit like regular underwear without any bulkyness"
- "they feel like a thin overnight pad"
- "what kind of voodoo magic is going on here"
- "Menstrual pads can't absorb thin, fast-flowing urine"
- "I have never leaked through any of them"
- "the waist band rolls down when you move"
- "sick and tired of peeing myself every time I sneeze"
- "just accept that you'll be peeing every time you sneeze for the rest of your life"
- "had to run to bathroom"
- "Children destroy women's bladders"
- "You think twice before jumping rope or hitting the trampoline park"
- "If you wee yourself, you just rock on"
- "I had to quit Orange Theory"
- "I told her with tears in my eyes"
- "Leaking pee while exercising is normal. No."
- "I'd assume you were just sweaty"
- "too strong of a pelvic floor"
- "so, so embarrassed"
- "just because it's common, it doesn't mean it's normal"
- "frustrated, irritated, and embarrassed me for years"
- "basically undetectable under clothing"
- "I hate wearing incontinence products"
- "more protection than a pad offers"
- "Finally a product that really works as advertised"
- "No leaks. No smell. No stress."
- "changed my life"
- "I wish someone had shown me this before my first baby"
- "Adult diapers or incontinence pads. Uhhh, no thanks."
- "worrying that running or sneezing would leave me needing fresh underwear"

## 4. Tools log
- ✅ Firecrawl MCP `firecrawl_search` — ran many queries across Reddit, Amazon, Walmart, Trustpilot, PissedConsumer, X, TikTok, forums, medical sites.
- ✅ Firecrawl MCP `firecrawl_scrape` — opened & confirmed verbatim wording on Trustpilot (Everdries, THINX, Modibodi, Knix), Walmart (Everdries, Attn:Grace), PissedConsumer (Everdries), and Amazon /dp/ 'Customers say' + review quotes (Everdries B0DHYFDYTB, Because B0CL163VVX) via `formats:[query]` directQuote.
- 🔁 agent-reach — SUBSTITUTED by Firecrawl (its CLI is not installed in this env), per instructions.
- 🔁 product-pulse — SUBSTITUTED by Firecrawl scrape of Amazon/Walmart 'Customers say' + review pages.
- ❌ TikTok / YouTube COMMENT text (the comment threads themselves) — could NOT load: comments are JS-rendered/behind auth and did not appear in scrape markdown. Captured TikTok/IG/FB *video captions & discover-page text* instead (tagged SNIPPET) and leaned on Reddit + review sites for depth, as instructed.
- ❌ Reddit full-thread fetch — Reddit serves a login wall to the scraper; used search-result snippet text (tagged SNIPPET) with thread URL + title preserved, per instructions.

## 5. Honest gaps
- 155 rows from 9+ platforms / 6+ source types (Reddit, Trustpilot, Amazon 1-2★ & 4-5★, Walmart, PissedConsumer, X, TikTok/social, press/medical). Target (100+, aim 150+) MET.
- VERBATIM vs SNIPPET is honestly tagged per row. ~57% VERBATIM.
- Dates: review-site rows carry real dates; Reddit SNIPPET rows often lack a visible date (left blank rather than invented); thread URL+title preserved so date is recoverable.
- Star ratings: present for Trustpilot/Walmart/most Amazon review rows; Amazon 'Customers say' summary rows and a few blog/press rows have no confirmable star (left blank).
- The active 30s–40s ICP is under-represented on retail-review sites (those skew 60+); her voice is carried mainly by Reddit fitness/running/perimenopause subs — a real market signal, not just a data gap: the ACTIVE leaker rarely reviews elderly-coded incontinence products.
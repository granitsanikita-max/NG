# Step 1 "Deep Market Research" checklist: gap analysis (RAW)

**Audited file:** `notion/step-1-deep-market-research.ORIGINAL-2026-09-22.md` (all 86 lines read)
**Audit date:** 2026-10-04
**Scope:** This audits the checklist itself. The Bunion Corrector output only shows the symptoms.
**Method:** I checked each claim against primary or near-primary sources, and every source URL below was opened or returned by search during this audit. Where something rests on agency or secondary sources rather than the original, I say so.

---

## PART A: What the checklist gets wrong or misattributes

### A1. §6 "Consciousness level" links to David Hawkins' "Map of Consciousness". It is pseudoscience, and copywriting doesn't use it (HIGH)
- **Checklist:** "§6 Consciousness level: The deeper belief stage she's at… [Map](substackcdn…6869b8ab…jpeg). (Awareness = how much she knows. Consciousness = the belief-stage map.)"
- **What the link actually is:** I downloaded the image. It is titled *"Map of Consciousness, Developed By David R. Hawkins"*. It lists levels from Shame (20) up to Enlightenment (700–1000), with columns for "Energetic Log", "God-view" and "Process". It is a spiritual scale from *Power vs. Force*. It is not a belief-stage map, and it has no connection to Schwartz or any other direct-response framework.
- **Why it's invalid:** Hawkins "calibrated" the levels with applied-kinesiology muscle testing. Under blinded conditions this method does not hold up, because it is driven by ideomotor effects and the tester's expectations. Source: https://www.quora.com/How-did-Dr-David-R-Hawkins-calibrate-consciousness (summarizes the method and the criticism).
- **Effect on an AI executor:** The section has no instructions, no inputs and no output format. The executor will either invent an "energetic level" for the avatar or skip the section. Either way it adds noise.
- **Fix:** Delete §6. If the goal was "the emotional state she's in", that already exists as the Emotional Journey in §14. If the goal was "a cynical market that has stopped believing claims", that is Schwartz sophistication Stage 5 (identification), which belongs in §8.

### A2. §8 has the wrong Schwartz sophistication stages (HIGH)
- **Checklist:** "Stage 4–5 (crowded) = you NEED a new **unique mechanism**."
- **What Schwartz actually says (*Breakthrough Advertising*, 1966):**
  - **Stage 1:** a simple direct claim.
  - **Stage 2:** enlarge the claim.
  - **Stage 3:** **introduce a new mechanism**, "a new way to make the old promise work".
  - **Stage 4:** **elaborate and enlarge the mechanism**, making it easier, faster, surer, or "a better mechanism".
  - **Stage 5:** the market is exhausted and no longer believes claims or mechanisms, so you sell **identification** with the prospect's self-image (his example is Postum's "Why Men Crack").
- **Sources:**
  - https://www.motiveinmotion.com/market-sophistication/ (quotes Schwartz: "the elaboration is concentrated on the mechanism, rather than on the promise" for Stage 4)
  - https://www.linkedin.com/pulse/explained-five-levels-market-sophistication-kobi-simmat (Stage 3 = "a new mechanism"; Stage 5 = identification)
  - https://valchanova.me/breakthrough-advertising-copywriting-book-review/
- **Why it matters:** For a Stage 5 market, the checklist sends the executor off to build yet another mechanism. Under Schwartz, that market needs identity and brand. The checklist's own §4B (Liquid Death) is the correct Stage 5 play, but nothing in §8 routes the executor there.
- **Fix (paste into §8):**
  > **8 · Sophistication stage (with evidence)** — Count it, don't guess: # of active advertisers in Ad Library for the core keyword, and list the 5 most-repeated claims/mechanisms. Stage 1–2 = lead with the (bigger) claim. **Stage 3 = new mechanism. Stage 4 = a bigger/faster/easier version of the mechanism.** Stage 5 = claims are dead → sell identification (route to §4B). Write the stage + the evidence.

### A3. §5's "Discourse-volume proxy" mixes up awareness with sophistication (HIGH)
- **Checklist:** "Pages and pages of threads = high awareness (solution/product-aware, high skepticism, they've been burned)".
- **Why it's wrong:** In Schwartz's framework, *awareness* describes the prospect: what she knows about her problem and about products that solve it. *Sophistication* describes the market: how many similar claims she has already heard. "High skepticism, they've been burned" is sophistication. Lots of Reddit threads about a problem only shows that people know they have the problem. It does not show they know about your solution or product.
- **Sources:** https://betweenthelinescopy.com/blog/stages-of-awareness/ and https://www.motiveinmotion.com/market-sophistication/
- **The "AI distribution" method is fabrication.** "Have ChatGPT/Claude scan the market and return a rough % split across the 5 stages" asks a model to invent numbers. That breaks the page's own **One Rule** ("Every answer must come from a real source… No guessing"). The Bunion output never produced the split at all.
- **Fix (paste into §5, replacing the two methods):**
  > **Measure awareness from search + ad evidence** — Tally real query volume by stage (Google Trends / TikTok Keyword Insights): symptom queries ("why does my big toe hurt") = problem-aware; category queries ("bunion corrector") = solution-aware; brand queries = product-aware. Report the counts + where competitor ads enter. Burned/skeptical = §8 sophistication, not awareness. No AI-estimated percentages.

### A4. §16 "Psychological solution (Hormozi)" is correctly attributed, but the description is wrong and the section is in the wrong step (LOW)
- **The attribution is correct.** *$100M Offers* uses logical vs. psychological solutions, with the faster elevator vs. the mirror in the elevator. Source: https://www.alexhyett.com/book-notes/100-m-offers/
- **But Hormozi didn't originate the idea.** His train example (pay models to host the trip) is Rory Sutherland's Eurostar argument from his 2009 TED talk. Source: https://bhanders.com/2015/05/14/the-eurostar-giselle-a-bottle-of-chateau-petrus-a-new-vision-for-the-nhs/
- **The checklist's description is off.** It says "the emotional fix underneath". Hormozi's idea is changing how the problem is *perceived* instead of fixing the thing itself. That is a lever for designing the offer and the experience, not a research finding.
- **Fix:** Move it into the new Offer section (G6) as a single row: "1 psychological fix that changes perceived value at ~zero cost."

### A5. §0 "need vs. want" test conflicts with Schwartz's core rule (MEDIUM)
- **Checklist:** "make sure the market… is really needing a solution… not just a want".
- **What Schwartz says:** Copy cannot create desire. It can only *channel* a mass desire that already exists. He grades a desire on three dimensions:
  - **urgency/intensity:** how badly she wants it now
  - **staying power:** whether it keeps coming back, or can't be satisfied once and for all
  - **scope:** how many people share it

  Lots of huge DTC markets are "wants", such as vanity and status, and they score very high on all three.
- **Sources:**
  - https://taylorpearson.me/bookreview/breakthrough-advertising/ ("three dimensions to mass desire: urgency, intensity… staying power… scope")
  - https://deepreadbooks.com/books/breakthrough-advertising-eugene-swartz/learn
- **Fix:** see G10.

### A6. Smaller accuracy issues
- **§13 mechanism with no type or proof requirement.** The section asks for "the hidden CAUSE of her problem + your named FIX". For a sourced product, that invites invented biology. Todd Brown separates three kinds of mechanism:
  - **Actual:** a real unique part of the product.
  - **Unspoken:** a real feature competitors simply don't talk about (from Claude Hopkins).
  - **Transubstantiated:** a reframing of an ordinary feature.

  The checklist doesn't distinguish them. Sources: https://www.scribd.com/document/895713866/Big-Idea-Book and https://podcast.lifterlms.com/mastering-modern-marketing-todd-brown-e5-method/
- **§13B discovery story.** It tells the executor to "craft a believable discovery narrative (founder journey…)" even for a sourced product.
  - Georgi does put a background story in his Brief: https://thecopywriterclub.com/sales-letters-stefan-georgi/
  - But presenting a made-up founder or expert story as fact is a material misrepresentation under FTC Act §5.
  - Since July 2023, the revised Endorsement Guides define an endorser as anyone who "appear[s] to be an individual, group, or institution". That includes fictitious people. Source: https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising
  - This is the root cause of the invented Bunion founder story. See G5.

---

## PART B: Contradictions and ambiguities that make an AI executor skip or misread steps

| # | Where | Problem | Fix |
|---|---|---|---|
| B1 | Line 7 "done" condition | It points to a "⭐ One-Pager at the bottom", but the page has no One-Pager. The executor can never meet the done condition, so it improvises or ignores it. | Add the One-Pager block (G-Final). |
| B2 | Line 7 vs. the numbering | The One-Pager needs "the offer", but no offer section exists. §15 is missing (the numbering goes 14 → 16), and Step 2 is said to own the offer (line 86). | Restore §15 Offer and Economics (G6). Say Step 1 *researches* the offer and Step 2 *builds* it. |
| B3 | Line 82 | "1. the exact full funnel structure your going to make fill this out -" is garbled. Markdown renders it as an ordered list item "1.", so a parser can read it as Step 1. The Funnel Map that follows has a placeholder ("Ad (does x)"), no number and no output spec. | Replace it with "**21 · Funnel Map**: for each touchpoint, write its ONE job + the belief from §9B it moves." |
| B4 | Lines 5, 11, 19, 22 | Four different things claim to come first: "Do this first, every time"; `research-doc` "Start here"; "Audit first", which is a step hidden inside the *Skills* list; and "§1 Competitor scan (do this first)", which comes after §0. | Make one numbered order. Turn Audit into step §0C, and drop "do this first" from §1. |
| B5 | §2, §4, §4B come before §10/§10B | Decisions come before the evidence they need. §4B says to "Find the enemy inside the category's own 1★ reviews", but 1★ mining doesn't happen until §10B and §11. §2 picks the "Avatar gap" before §3 and §10 define the customer. The executor will invent these to keep moving. | Reorder: **Demand → Competitors → VoC (§10, §10B, §11, §14, §18) → Segments → Gap / Positioning / Mechanism → Offer → One-Pager.** RMBC does Research before Mechanism: https://www.stefanpaulgeorgi.com/the-rmbc-method-for-better-copy/ |
| B6 | Line 9 vs. §5, §13B, §19 | The One Rule ("No guessing") is broken by three steps: the AI % split (§5), "craft a believable discovery narrative" (§13B), and "Build an AI bot with her traits, interview it" (§19). | Remove all three, or label any synthetic output "HYPOTHESIS, unverified" and keep it out of copy. |
| B7 | Line 16 vs. line 9 and line 10 | The "Amazon trick" (paste reviews into ChatGPT) loses the source URLs and the counts. It also contradicts "run these, don't do it by hand". | Rewrite it as coded mining with a tally (G2). |
| B8 | §3 vs. §2 | §3 asks for "One real person, not everyone", but the §2 avatar-gap step and Andromeda-era delivery both need several segments. The Bunion output then mixed nurses, 70-year-olds and young women into one person. | Add §3A Segments (G3), then the primary ICP. |
| B9 | §5 vs. §7; §9 vs. §9B; §10 vs. §11 vs. §14 | Overlapping sections: funnel level repeats awareness; beliefs appear twice; objections and quotes are collected in three places. This is why the output ran to about 25 sections. | Merge §7 into §5 and §9 into §9B. §11 and §14 should pull from the coded VoC sheet instead of re-mining. |
| B10 | §20 Verify | "Nothing ships unverified" never defines what verified means. | Define it: every claim has an [S#] source; every stat has a URL and date; anything without one is marked UNVERIFIED and doesn't reach the One-Pager. |
| B11 | §6 | It is a link only, with no instructions, and the link is to pseudoscience (A1). | Delete it. |
| B12 | §4B "which reviews you show" | Read literally, this tells the executor to curate the store's review display. Hiding negative reviews while implying the rest are representative is unlawful under 16 CFR 465.7(b) (G5). | Add: "show all reviews; filter only by rating-neutral rules". |
| B13 | Whole page | There is no output format, length limit or summary. | Add "Top 5 takeaways" at the top, numbered sources at the bottom, and a word cap per section. |

---

## PART C: Gaps, ranked by impact

Each gap gives: (1) what's missing, (2) why it matters for a dropshipper running ads, (3) text you can paste into the page, (4) sources.

### HIGH

**G1. No traceability rule for sources**
- (1) Line 9 says "Every answer must come from a real source", but nothing makes the executor record the source. The Bunion quotes had no URLs.
- (2) Without a URL you can't tell a real quote from an invented one. Using an invented "customer quote" in an ad is a fake testimonial under 16 CFR 465.2 (G5).
- (3) Paste:
  > **Cite or cut** — Every quote, stat and claim carries a tag [S#] → Sources list at the bottom (URL · platform · date · star rating/upvotes). Quotes are verbatim, typos kept. No [S#] = delete it.
- (4) https://www.govinfo.gov/content/pkg/FR-2024-08-22/html/2024-18519.htm

**G2. No coding of voice-of-customer data and no frequency counts**
- (1) §10 and §14 collect pains and quotes, but nothing ranks them. The executor never learns which pain is #1.
- (2) Your first ads should lead with the pain mentioned most often. Without counts, the pick is a guess.
- (3) Paste:
  > **Code + count (VoC sheet)** — Mine ≥ 150 snippets (Amazon 1–3★ & 4–5★ of top 3 competitors, Reddit, TikTok comments). One row each: quote · [S#] · code (pain / desire / objection / failed solution / trigger / phrase) · theme. Tally themes → rank Top 5 pains, desires, objections by count ("23/150"). Leads go to the top count, not the loudest quote.
  >
  > **Message mining** — Highlight phrases that are vivid, repeated, or oddly specific ("sticky"); these become hooks and headlines word-for-word.
- (4) https://copyhackers.com/2014/10/amazon-review-mining/ · https://copyhackers.com/write-copy-amazon-review-mining/ · https://cxl.com/blog/voice-of-customer/

**G3. No segmentation and no multiple personas**
- (1) §3 asks for one person.
- (2) Andromeda is Meta's retrieval engine, announced December 2024. It matches creative to people, so diverse concepts aimed at different personas are now the main way to reach new buyers.
  - Meta's engineering blog confirms the retrieval change.
  - Agencies report that near-duplicate ads get treated as one ad. Note: the "Entity ID" and similarity-threshold numbers come from agencies, not from Meta documentation.
  - One avatar means one cluster of concepts, which caps how far you can scale.
- (3) Paste:
  > **3A · Segments (before the ICP)** — List 3–5 sub-avatars found in the VoC sheet (who / situation / trigger / top pain / their words). Score each 1–5 on size (mention count) × pain intensity × reachability (can an ad call her out without naming a health condition?). Pick the primary for §3; keep the rest as angle seeds for G7.
- (4) https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ · https://www.tryatria.com/blog/andromeda-meta-ads (agency) · https://adsuploader.com/blog/meta-andromeda (agency)

**G4. No data on demand, market size or seasonality**
- (1) §1 only says to "Confirm real demand exists (winning ads / scaled stores are out there)". There's no number and no time view.
- (2) This is the go/no-go question, and it decides when to launch. A seasonal product launched off-season burns ad spend while testing.
- (3) Paste:
  > **0B · Demand & seasonality (numbers only)** — (a) Google Trends, 5 yrs, your country: trend direction + peak months (note: 0–100 is relative, keep window/geo fixed). (b) Amazon: "X bought in past month" for top 5 listings + total review counts. (c) TikTok Shop: 30-day units/GMV for top 3 SKUs (Kalodata / FastMoss / WinningHunter). (d) TikTok Creative Center Keyword Insights + Top Products. (e) # active advertisers in Meta Ad Library. Verdict: growing / flat / dying · seasonal Y/N · best launch window.
- (4) https://meetglimpse.com/google-trends/ · https://easyparser.com/blog/amazon-bought-in-past-month-explained · https://www.intentwise.com/blog/amazon-ui-feature/amazon-is-displaying-sales-data-in-search-heres-what-to-know/ · https://www.smartscout.com/blog/tiktok-shop-analytics-tools · https://ads.us.tiktok.com/help/article/creative-center

**G5. No compliance gate, and the page tells the executor to fabricate**
- (1) Nothing on the page screens claims. Worse, §13B asks for a "crafted" origin story, §18B asks for "suppressed cure" angles, §4B says "which reviews you show", and §3 collects religion and politics with no ad-copy rule.
- (2) Failing any of these can cost you the ad account or bring FTC penalties:
  - **FTC health claims** need "randomized, controlled human clinical testing". The 2022 guidance is still live on ftc.gov; I found no withdrawal. An orthotic that "realigns" a bunion is making a health claim.
  - **Testimonials** can't claim results you couldn't substantiate yourself. Atypical results need a disclosure of what people can generally expect.
  - **16 CFR 465 (effective Oct 21, 2024):** bans fake or AI-written reviews and testimonials, and bans reviews from people with no real experience of the product. It also bans implying that displayed reviews are representative while suppressing reviews based on rating. The penalty is up to $51,744 per violation (the 2024 figure, adjusted for inflation each year).
  - **Meta Personal Attributes:** ads can't assert or imply the viewer's health condition, religion, age or financial status. Meta's own example: "Do you have diabetes?" is rejected and "Depression counseling" is allowed.
  - **FTC Mail Order Rule:** you need a reasonable basis for any shipping time you state, or must ship within 30 days if you state none. This hits dropshippers directly.
- (3) Paste:
  > **22 · Compliance table (required, can't be "pending")** — 3 columns: CLAIM WE WANT · ALLOWED WORDING · BANNED WORDING + why (FTC health substantiation / Meta personal attributes / review rule). Also: shipping-time promise we can actually prove; reviews shown unfiltered by rating; no "you/your + condition" hooks.
  >
  > **13B (replace) · True story only** — Use a REAL origin: why we picked this product, what we tested, what we rejected, or a real customer's story (with permission, linked [S#]). No invented founder, doctor, or "discovery." If there's no true story, use a customer story or skip.
  >
  > **18B guardrail** — "Lost/suppressed cure" angles are hook research only; never imply a health product cures/treats anything without RCT-level proof.
- (4) https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance · https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising · https://www.govinfo.gov/content/pkg/FR-2024-08-22/html/2024-18519.htm · https://www.goodwinlaw.com/en/insights/publications/2024/09/alerts-practices-cldr-ftc-finalizes-rule-on-consumer-reviews · https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/ · https://ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule

**G6. No offer, no price ladder and no unit economics (§15 was deleted)**
- (1) There's no offer section, no value equation, no price ladder and no break-even numbers. The Bunion KPIs were left "pending".
- (2) A dropshipper's customer can find the same item on AliExpress or Amazon. The price ladder, and the objection "why pay 3× for this?", decide whether the business is viable. Without break-even ROAS you can't judge a test.
- (3) Paste:
  > **15 · Offer & economics** — (a) **Price ladder:** same/similar item on AliExpress → Amazon → TikTok Shop → top 3 DTC stores (price, bundle, guarantee, ship time) [S#]. (b) **Value equation score 1–10** for us vs. top competitor: Dream outcome × Likelihood ÷ (Time delay × Effort). Name the one lever we raise. (c) **Unit economics:** COGS + shipping + fees + returns % → contribution margin → **break-even ROAS & CPA**. Never "pending." (d) One psychological fix (perceived-value change at ~0 cost).
- (4) https://infinitemediaresources.com/business-books/alex-hormozi-value-equation-explained/ · https://www.alexhyett.com/book-notes/100-m-offers/

**G7. No bank of angles and hooks**
- (1) Line 17 says to steal high-view thread titles as hooks, but there's no section where they're stored. Step 3 starts from nothing.
- (2) Andromeda rewards concepts that are genuinely different, and research is where those come from.
- (3) Paste:
  > **23 · Angle & hook bank** — Matrix: segment (3A) × top desire/pain (G2) × awareness entry (§5) × format. Min 15 distinct angles; each with 3 hooks written in her verbatim words [S#], a trigger event (§18), and compliance check (22). Flag 5 to test first.
- (4) https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ · https://www.tiereleven.com/creative-diversification (agency)

**G8. Mechanism has no type and no proof inventory (§13)**
- (1) Nothing forces the executor to tie the mechanism of the solution (UMS) to a real, provable product feature.
- (2) Without that, the executor makes up science. That's an FTC risk, and it also gets torn apart in the comments.
- (3) Paste:
  > **13 · Mechanism type + proof** — Label it: **Actual** (a real unique part), **Unspoken** (a real feature competitors don't mention), or **Reframed** (an ordinary feature, newly explained). Prefer Actual/Unspoken for sourced products. List every proof asset [S#]: spec, material, study (RCT? on THIS product?), demo, real reviews. Each UMP/UMS sentence must map to a proof row or be cut.
- (4) https://www.scribd.com/document/895713866/Big-Idea-Book · https://www.stefanpaulgeorgi.com/the-rmbc-method-for-better-copy/

### MEDIUM–HIGH

**G9. Jobs-to-be-Done forces: anxiety and habit are missing**
- (1) The page covers push (pains) and partly pull (desires). It never asks about **habit**, the inertia of doing nothing (only touched in §10B), or about **anxiety** about switching as something separate from general objections. It also never maps the purchase timeline.
- (2) For a cheap impulse product, habit and "it'll be junk" anxiety lose more sales than lack of desire. A switch happens only when push + pull is greater than anxiety + habit.
- (3) Paste:
  > **18 · Trigger events → Switch timeline** — From long first-person posts/reviews, map: first thought → passive looking → active looking → decision. Then the 4 forces, each with quotes [S#]: **Push** (what made now the moment) · **Pull** (what attracted her) · **Anxiety** (what almost stopped her) · **Habit** (why she kept doing nothing). Ads hit push/pull; page + offer kill anxiety/habit.
- (4) https://jobstobedone.org/ · https://jobstobedone.org/radio/unpacking-the-progress-making-forces-diagram/

**G10. No step that chooses a mass desire (replaces the §0 need-vs-want test)**
- (3) Paste:
  > **0A · Pick the mass desire** — List the 3–5 desires in the VoC sheet. Score each 1–5 on **urgency** (how badly now), **staying power** (keeps coming back, can't be satisfied once), **scope** (how many share it — use G2 counts + G4 demand). Channel the top scorer; copy can't create desire, only point existing desire at the product.
- (4) https://taylorpearson.me/bookreview/breakthrough-advertising/ · https://deepreadbooks.com/books/breakthrough-advertising-eugene-swartz/learn

**G11. No single "One Belief" sitting above the Belief Chain**
- (1) §9B lists up to six beliefs but never compresses them into the one big idea.
- (2) Without one central idea, the ads, advertorial and product page drift apart, and the One-Pager has nothing to anchor on.
- (3) Paste:
  > **9C · One Belief** — One sentence: "[New opportunity] is the key to [her #1 desire], and it's only attainable through [our mechanism]." Every §9B belief must support it. This line tops the One-Pager.
- (4) https://theinvisiblementor.com/lessons-from-the-16-word-sales-letter-by-evaldo-albuquerque/ · https://www.scribd.com/document/471754127/The-16-Word-Sales-Letter-Ebook-pdf

**G12. Competitor ad evidence has no rules for reading it (§1)**
- (1) The page treats "longest-running = proven" as fact. It never records start dates or notes what the Ad Library can't show.
- (2) An executor working from screenshots will overstate what's winning.
- (3) Paste:
  > **Ad Library evidence** — For each competitor log: ad start date, days active, # of near-duplicate variants, platforms, and ad URL [S#]. ≥ 30–45 days active = likely profitable (a proxy, not proof). For EU-delivered ads, open the EU transparency panel for reach by age/gender — real segment data for 3A.
- (4) https://adriselab.com/blog/meta-ad-library-competitor-analysis · https://adlibrary.com/posts/what-meta-ad-library-doesnt-show-you-2026 · https://transparency.meta.com/researchtools/ad-library-tools/

**G13. Customer research uses a fake respondent instead of real buyers (§19)**
- (3) Paste (replacing §19):
  > **19 · Real stories** — Before you have buyers: collect 5+ long first-person stories (Reddit posts, 300+ word reviews, video comments) and read them as switch interviews (G9) [S#]. After the first 20 orders: a 3-question post-purchase survey ("What almost stopped you?", "What else did you try?", "What made you buy today?"). No AI personas.
- (4) https://jobstobedone.org/ · https://copyhackers.com/how-to-write-a-long-form-sales-page-using-survey-data/

### MEDIUM

**G14. No go/no-go gate.** Paste:
> **Go / No-Go** — Score: demand trend (G4) · margin ≥ break-even at realistic CPA (G6) · desire score (0A) · claims we can legally make (22) · distinct angles ≥ 15 (G7). Any red = stop or change product before Step 2.

**G15. Objections specific to dropshipping are missing from the §11 list.** Paste:
> **Add to §11 checklist:** ship time · "is this the $8 AliExpress one?" · where it ships from · return shipping cost/who pays · fit/sizing · counterfeit/quality fear. Answer each with something true and provable (Mail Order Rule applies to ship-time claims).

Source: https://ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule

**G16. No rules for output structure.** Paste:
> **Format** — Top: "Top 5 takeaways" (written last). Each section ≤ 150 words + its table. Bottom: Sources [S#]. Anything without a source = UNVERIFIED and stays out of the One-Pager.

**G17. Words she never uses.** This adds to §14. Paste:
> **Anti-swipe** — 10 words/phrases competitors use that she never does (clinical/marketing jargon); banned from our copy.

### LOW

**G18.** Keep the "5th–8th grade reading level" rule, but move it to Step 4 (scripts). It's a writing rule, not research.

**G19.** In §3, keep the Worldview research, but add: "Use to *sound* like her. Never state her religion, politics, age or health back to her in an ad (Meta Personal Attributes)."

---

## PART D: The missing ⭐ One-Pager (fixes B1 and B2), ready to paste at the bottom of the page

> **⭐ One-Pager (done = every line filled, each with [S#])**
> 1. **One Belief** (9C)
> 2. **Primary segment** + 2 backup segments (3A)
> 3. **Mass desire** + score (0A) · **Top 3 pains by count** (G2)
> 4. **Awareness entry + sophistication stage**, each with evidence (§5, §8)
> 5. **Mechanism**: UMP / UMS, type, top proof (13)
> 6. **Positioning line** (4B)
> 7. **Offer**: price vs. ladder, guarantee, break-even ROAS (15)
> 8. **Top 3 objections** + answers (§11)
> 9. **5 angles to test first** (23)
> 10. **Compliance red lines** (22) · **Go/No-Go** verdict

---

## Recommended section order (fixes B4 and B5)

**Opening checks:** 0 Product → 0A Mass desire → 0B Demand → 0C Audit

**Market:** 1 Competitors + Ad evidence → 15-econ (price ladder and margin early, to kill bad products fast)

**Voice of customer:** VoC sheet (10, 10B, 11, 14, 18 switch forces) → 3A Segments → 3 ICP

**Diagnosis:** 5 Awareness → 8 Sophistication

**Strategy:** 2 Gap → 4 / 4B Positioning → 9B / 9C Beliefs → 12 Authority → 13 Mechanism + proof → 13B True story → 15 Offer → 17 Features → 18B Curiosity

**Close-out:** 22 Compliance → 23 Angle bank → 21 Funnel Map → Go/No-Go → 20 Verify → ⭐ One-Pager

**Deleted:** §6 · §7 (merged into §5) · §9 (merged into §9B) · §16 (folded into §15) · the AI-bot part of §19

---

## Source notes
- Andromeda's retrieval change is confirmed by Meta Engineering. The "Entity ID", similarity-threshold numbers and "Meta says creative diversification is the best lever" all come from agency or secondary write-ups. Treat them as practitioner consensus, not Meta policy.
- I couldn't scrape Reddit, which blocked the scraper. The Schwartz quotes on the three dimensions of desire are confirmed through Taylor Pearson's and DeepRead's summaries instead.
- I confirmed on 2026-10-04 that the FTC Health Products Compliance Guidance is still live on ftc.gov. I found no withdrawal; the only related withdrawal I found, in Sept 2026, was a separate health-apps breach policy statement.

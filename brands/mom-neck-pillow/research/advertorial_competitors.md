# Advertorial / Pre-Sell Teardown — Competitors to RecoverMama

**Brand:** mom-neck-pillow (RecoverMama) · **Scope:** competitor advertorials, listicles and "pre-sell" landers for neck pillows, neck-pain devices, and new-mom/postpartum products
**Compiled:** 2026-11-08 · **Method:** Firecrawl scrape of each URL (markdown, live fetch 2026-11-08) + WinningHunter `search_landers` / `search_facebook_ads` / `get_store_top_ads` for ad-volume signals and discovery.
**Rule:** Every claim is tied to the URL scraped. Anything not on the page is marked **INFERENCE**. This file does NOT write our advertorial.

---

## 0. Index of pages analyzed (15)

| # | Brand | URL | Live? | Format | Authority device | Ad-volume / longevity signal |
|---|---|---|---|---|---|---|
| 1 | Groove | groovepillows.com/pages/probably-your-pillow | Live | Editorial "Sleep Health" article (hybrid editorial + sales page) | "Dr. Lauren Whitaker, Sleep Posture Contributor" + 2 real meta-analyses cited + physio testimonial + 1,000 practitioners + awards | WH: 5 active ads (down from 9 a month ago), 151 days running; page "Neck Pain Relief with the Groove Pillow" (106 active ads) |
| 2 | Derila | derila.com/articles/in-tears-every-night | Live (derilashop.com path is **404**) | First-person wife story | None (anonymous wife narrator); "tons of people worldwide" reviews | Brain: Derila ~1,191 ads, live creatives since 2024-02 |
| 3 | Derila | derila.com/article/derila-military-sleep-method | Live | First-person story with byline | "Martin Brown, Home & Lifestyle Editor" byline; "ex-military buddies"; "European scientists"; Trustpilot/Amazon counts | Same account. "UPDATE Tuesday, June 7, 2023" stamp → page in rotation ≥2.5 yrs (**INFERENCE**) |
| 4 | Restora | sleeprestora.com/pages/adv1 | Live | First-person male story (car crash → snoring) | "✅ Verified by Martin H., Sleep Science Specialist"; unnamed "specialist"/"my doctor" | Brain: 10 near-identical ads each running 320+ days (persona "Laura J. Mitchell, PhD"); account now pivoted to supplements |
| 5 | Restora | sleeprestora.com/pages/adv4 | Live | "Myth-busting" / "3 Big Lies" expert piece | "Verified by Martin H., Sleep Science Specialist"; "small group of sleep specialists" | Same |
| 6 | Restora | sleeprestora.com/pages/adv5 | Live | Q&A "guide" with doctor byline, fake-news chrome | "By Dr. Daniel Foster" + "Trending in the US" + "1,628 Ratings" | Same |
| 7 | Mellow | mellowsleep.com/pages/wp-adv-2 | Live | First-person story + chiropractor reveal ("My Chiropractor Told Me…") | Named chiropractor "Dr. Heather Heim" (real-looking face, also a reviewer + advertiser page "Heim Health") | WH: 109 active ads, 215 days, +419% in 90d; store $19–36M/mo est. |
| 8 | Mellow | mellowsleep.com/pages/heim-adv-1 | Live | "Chiropractor-recommended" long sales page (GiddyUp template) | "Heather Heim — Board-Certified Chiropractor"; "As seen in" FOX/CBS/TikTok/Grommet; invented awards | WH: 142 active ads, 267 days, +238% in 90d |
| 9 | Dosaze | dosaze.com/pages/3-reasons-why-thousands-choose-dcop → **redirects** to /pages/sleep-better-wake-up-ache-free | Live (listicle gone; redirect) | Long sales page (same template family as #8) | "Dr. Jandi R., Licensed Chiropractor" quote; "Best Pillow of 2026" | Brain: ~1,320 Meta ads; "Moms Need a Better Pillow" test ads routed here |
| 10 | Neckline | neckline-us.com/neckline-usa/adv-opt | Live | Fake news "investigation" ("Doctors Keep Missing This") | "Dr. Michael Chen, Stanford Medical Center" + "Dr. Richardson's team" + "engineer Thomas Keller" + fabricated study stats | WH: 52 active ads, 132 days; ads run from a page called **"The Daily Health Post"** + persona pages |
| 11 | Cevera | trycevera.com/pages/adv-womens-wellness-report | Live | Fake publication masthead ("Women's Wellness Report™") + long-form DPT sales letter | "Sarah Mitchell, DPT — 22 yrs, 3,400 patients, Nashville"; ads from page "Carol M. Bennett, PT" | WH: **150 active ads**, 159 days, +233% in 90d |
| 12 | Blissy | latest.blissy.com/pillow-reasons → **redirects** to try.blissy.com/checkout-15 | Live (listicle URL now lands on a sales page) | Long sales page | Independent 28-day study (Kosmoscience, report # cited); "As seen in" Forbes/Oprah Daily etc.; 2 named chiropractors | WH: 13 active ads (down from 32), 41 days |
| 13 | Frilume "Cervicare" | Meta ad from page **"Sarah's Wellness Journal"** → frilume.com/products/cervicare | Ad: last seen 2026-09-10; Frilume pages now 0 active ads. PDP **not scrapeable** (TLS cert error) | Long-copy native ad (the advertorial lives in the ad body) — first-person new mom | Persona page name "Sarah's Wellness Journal"; mom-to-mom voice | WH: page also runs menopause/weight stories (Mar 2026) — a rented "journal" persona |
| 14 | 8 Sheep Organics | 8sheep.com/pages/5-reasons-every-postpartum-mom-should-keep-up-her-belly-care | Live | Listicle ("5 Reasons…") | Byline "Emily Taylor" w/ photo; ingredient science; "$1.57/day" | WH: ads started 2026-05-26, last seen 2026-11-07 (~165 days live) |
| 15 | 8 Sheep Organics | 8sheep.com/pages/true-belly-serum-advertorial | Live | Mom pull-quote opener + education article | Real PubMed Central quote with PMC ID; real Stamped reviews (4.6★, incl. 1★s) | WH: multiple ads to this URL, last seen 2026-11-04/07 |

Not found / no advertorial:
- **Neurogena (neurogena.us):** WH `search_landers` returns only PDPs (`/products/lumbarlock`, `/products/knee-system`); top ads go to PDPs. **No advertorial found** for the mom-roller funnel — it is ad → PDP (brain: `/products/massage-roller`).
- **Derila `derilashop.com/articles/*`:** 404. Articles now live on **derila.com/article(s)/…**. WH also shows a new Derila funnel on **derila-ergo.com** (`/article/derila-ergo-sleep-apnea-2-gif` — 69 active ads, 14 days, EU-language; `/fnl/adv/jp-apnea-1` — Japanese). Not scraped (non-US language variants).
- **Derila `/articles/wake-up-refreshed`:** not scraped (time budget; same template family as #2 — **INFERENCE**).

---

## 1. Per-page teardowns

### 1. Groove — "Waking Up With Neck Pain? It's Probably Your Pillow."
- **URL:** https://www.groovepillows.com/pages/probably-your-pillow · Live. WH: 5 active ads, 151 days running.
- **Format:** Editorial article on the brand domain, dressed as a health site section — breadcrumb `Sleep Health | Editorial · Home › Health › Sleep & Posture`. Hybrid: editorial first half, product page second half.
- **Authority device:** byline **"By Dr. Lauren Whitaker · Sleep Posture Contributor · 6 hours ago · 5 min read."** No credentials, no photo in markdown. Whitaker does not appear elsewhere on the page. Backed by: 2 real systematic reviews (Pang 2021 *Clinical Biomechanics*; Radwan 2021 *Eur J Integrative Med*) with DOIs, plus Cleveland Clinic & Sleep Foundation; "recommended by more than 1,000 chiropractors, physical therapists"; a "Jack Parker · Physiotherapist · Verified Buyer" review; awards "Best Pillow For Neck Pain" from Sleep Foundation, Good Housekeeping, Men's/Women's Health; Trustpilot 4.6 / 2,268.
  - Fabrication read: "Dr. Lauren Whitaker" + "6 hours ago" (a rolling timestamp) = **likely a pen-name persona (INFERENCE)**. Studies and Trustpilot count are real and checkable. Most credible page in the set.
- **Headline/subhead/byline/disclosure:** H1 above; subhead = "If you sleep on your side and wake up stiff… the problem may not be your age, your posture, or your stress. It may be the pillow…". Trust bar under byline: "4.8 · 13,588 verified reviews · 500,000+ customers · 100-night risk-free trial". **No "Advertorial"/"Sponsored" label anywhere in the scraped text.**
- **Structure:**
  1. Hero image + caption ("That stiff neck before your first cup of coffee…")
  2. "5:55 a.m." — a body "audit" bullet list (right shoulder tight / base of skull / left side clicks)
  3. Reframe: "Not your phone. Not your chair. Not your age… Your pillow."
  4. "The Back-and-Side Sleeper Trap" — mechanism (shoulder gap; one height can't serve both positions; 3 a.m. numb arm)
  5. Infographic: one flat pillow can't do both
  6. "The Pillow For Back AND Side Sleepers" — product named here (**~35–40% down**), 4 zones (Head Cradle, Ergonomic Groove, Lateral Raises, Shoulder Underhang)
  7. CTA 1 "Check Availability & Save Up to 55%"
  8. "Neck Pain Relief, Backed By Science" — 2 reviews of studies + 1,000 practitioners + physio quote
  9. "500,000 Customers Have Already Switched" — reviews, Trustpilot, awards, 5 testimonials (osteopath / physio recommended)
  10. "Risk Free With A 100 Night Trial" → product card → CTA 2 "See the Side-Sleeper Groove →" → footnotes (5 refs) → sticky CTA 3 "Check Offer →"
- **Mechanism:** shoulder-gap / two-positions-one-pillow; "your neck is not getting the recovery it needs" (overnight recovery framing).
- **Proof:** real studies, review counts, Trustpilot, awards, practitioner endorsements, named testimonials (incl. medical conditions: C6/7, cervical spondylosis).
- **Objections handled:** "You've seen a hundred pillow ads this year" (ad fatigue), "takes about a week to settle" (adjustment), price via 100-night trial.
- **Offer/urgency:** "Save up to 55%", "Up to 55% off for a limited time only", "In stock". Soft urgency only.
- **CTAs:** 3 (Check Availability & Save Up to 55% / See the Side-Sleeper Groove → / Check Offer →), all to `/pages/groove-pillow-side-sleeper`.
- **Visual/native traits:** health-site breadcrumb + editorial byline + read time; infographics; footnoted references at bottom like a journal article. No comment section, no sidebar (markdown).
- **Why it works:** opens on a sensory morning ritual the reader recognises, kills competing explanations, gives a simple geometric mechanism, then stacks *real* third-party proof. Calm tone, low hype.
- **Compliance flags:** likely persona "Dr." byline with fake-recency timestamp; no ad disclosure; testimonials naming diagnosed conditions (spondylosis, C6/7) imply therapeutic claims. Otherwise the most defensible page.

### 2. Derila — "I Was In Tears Every Night Because Of My Husband's Snoring… Until A Random Gift Changed Our Lives"
- **URL:** https://derila.com/articles/in-tears-every-night · Live (derilashop.com path = 404). `noindex`.
- **Format:** first-person confessional (wife POV), blog-post style.
- **Authority device:** none — relatability only. Date shows today's date (2026-11-08) next to 5-star image → **auto-updating date (INFERENCE)**.
- **Headline/disclosure:** H1 above; no subhead/byline. Bottom-of-page boilerplate: "This is an advertisement and not an actual news article, blog, or consumer protection update… Any photographs of persons used on this site are models." Small, footer-only.
- **Structure:** husband snores 5 yrs → escalates (daughter's room, couch, near-divorce) → "ugly crying" → coworkers gave "anti-snoring pillow" as a joke (**product appears ~45% down**, named ~55%) → first night both slept → bought 4 more → "Why Does It Work So Well?" (airway/alignment, memory foam) → "Derila is perfect for" bullets (snorers, bad sleepers, headaches) → "So what are you waiting for?" → "How to get your Derila" → CTA "Receive a 70% discount if you order today!" → 9 reviews with avatars/photos → CTA → disclosure → sticky "#1 Way to Snoring-Free Sleep / Buy now / Check availability".
- **Mechanism:** vague — "align your head and shoulders to keep your airways as open as possible."
- **Proof:** 9 named reviews with photos; no stats, no studies.
- **Offer/urgency:** 70% discount "if you order today"; "Get genuine Derila only at the official site". Almost every product mention is a hyperlink (~15 inline links).
- **CTAs:** ~4 explicit buttons + ~15 inline text links + every image linked.
- **Why it works:** emotional relationship stakes (marriage), "accidental discovery" removes salesperson suspicion, gift angle (buy 4).
- **Compliance flags:** auto-date; footer-only disclosure; health claims (headaches, nasal congestion) hedged with "may"; "70% off" vs. perpetual discount (**INFERENCE** — brain notes Derila's 70% slab is evergreen).

### 3. Derila — "From Despair to Discovery: Unveiling the Life-Altering 'Military Sleeping Technique'…"
- **URL:** https://derila.com/article/derila-military-sleep-method · Live. `noindex`.
- **Format:** first-person story with an editor byline; "method/secret" hook.
- **Authority device:** "Written By **Martin Brown**, Home & Lifestyle Editor" (photo thumbnail) — a fake editorial role on the brand's own domain; borrowed authority from "the military"/"Navy SEALs"; "created by a group of European scientists that specialize in sleep"; "380 5-star reviews on Trustpilot, 1798 on Amazon, featured in Sleep Hero.co, Health News." **Fabrication read: high (INFERENCE)** — narrator is simultaneously "editor", "mechanic", and ex-military friend group.
- **Headline/date/disclosure:** top bar "UPDATE – Derila is currently on a LIMITED TIME SALE"; date = today (auto); "WAREHOUSE CLEARANCE SALE: 70% OFF Until Stock Runs Out" right under H1. Same footer disclosure as #2 + "Derila Legal Disclaimer".
- **Structure:** cliffhanger (ambulance) → "I thought it was over" → warning signs (social life, work) → breaking point / hospital "ruined my spine health" → chiropractor/exercise failed → "accidentally found" the military method → "one mistake most people make" = **muscle tension** → "How Can You Replicate…" → product named (**~50% down**) "based on the same concept… muscle targeting… through reflexology" → skeptical → first night "quicksand" → 4 ✔️ benefit blocks (reflexology butterfly design, molds, cooling, shipping/service) → CTA → "Is Derila for you?" 5-item ✅ quiz → "UPDATE Tuesday, June 7, 2023 … 763,419 cushions sold… 70% discount while stocks last" → 5 reviews with flags → CTA → "EDITOR'S NOTE: LAST CHANCE" → fake "Comments" (4) → ORDER NOW → disclosure → sticky "Warehouse Clearance – 70% OFF… Once stock runs out – the sale is over".
- **Mechanism:** borrowed method ("military sleep method" = muscle relaxation) mapped onto pillow via pseudo-science ("reflexology").
- **CTAs:** ~8 buttons/banners + many linked images.
- **Why it works:** curiosity hook (secret method), dramatic stakes (job loss, hospital), self-quiz to self-identify.
- **Compliance flags:** fake editor byline; auto-dated; "reflexology" claims; "vertigo/migraine" in quiz; fake comments section; "Warehouse clearance" perpetual scarcity; old "UPDATE" date contradicts auto-date.

### 4. Restora — adv1 "How My Snoring Nearly Ruined My Life (And the Simple Overnight Fix That Finally Stopped It)"
- **URL:** https://sleeprestora.com/pages/adv1 · Live. Brain: Restora ran 10 near-identical advertorial ads 320+ days; account now pivoting to liver-supplement advertorials (fading).
- **Format:** first-person male story.
- **Authority device:** badge "✅ **Verified by Martin H.** — Sleep Science Specialist" (no surname/credential); an unnamed "specialist"/"my doctor" is quoted throughout ("You're not getting enough oxygen to your brain"). Note: brain recorded persona "Laura J. Mitchell, PhD" — **the persona has since been rotated (INFERENCE)**.
- **Disclosure:** word "Advertorial" as first line (small, top) + the same long "This is an advertisement…" footer as Derila (identical wording → shared template/agency, **INFERENCE**).
- **Structure:** stock-urgency banner ("50% OFF TODAY ONLY") → H1 → verified badge → CTA bar → car crash cold open → "wake-up call" (wife Olivia, 24 years, basement couch) → "Doctor's Warning" (oxygen to brain) → "Warning Signs" (headaches, fog, blood pressure) → "None Of The Solutions Worked" (CPAP, strips, mouthguards) → "Simple Solution I Discovered" via forum (**product ~45% down**) + fake Facebook-style forum thread (Brenda/Jenna/Ben) → First night → "30-Day Journey" timeline (Day 1 / Week 1 / Week 2 / Day 30) → "Why It Works" (**"optimal 26° angle"**) → "Science Behind Better Sleep" 5 zones → "What Impressed My Doctor" → 6 testimonials (city-tagged) → "Offer That Makes It a No-Brainer" (50% + free shipping + 60-night MBG + multi-buy) → "Limited Time… over 30,000 people last month" → ORDER NOW → 2 more reviews → "Think About It This Way" cost stack (sleep specialist $200–300, CPAP $500–1,000, chiro $70) → "My Wife's Final Words" → CTA → fake FB comments (5, with like counts/timestamps).
- **Mechanism:** neck alignment at a "26°" angle opens airway → stops snoring and oxygen deprivation.
- **Proof:** testimonials, fake forum + fake comments, doctor quotes, timeline.
- **CTAs:** ~8 (mostly "50% OFF").
- **Compliance flags:** heavy — implied sleep-apnea / blood-pressure / oxygen-deprivation claims; doctor "now recommends it to patients"; fabricated social comments; unsupported "26°" number; "TODAY ONLY" perpetual.

### 5. Restora — adv4 "Why Everything You've Been Told About Fixing Snoring Is Wrong (And Making It Worse)"
- **URL:** https://sleeprestora.com/pages/adv4 · Live.
- **Format:** contrarian "industry lies" expert piece (no first-person story until a late "Mark" vignette).
- **Authority device:** same "Verified by Martin H., Sleep Science Specialist" badge; "a small group of sleep specialists"; enemy = "$4 billion snoring industry".
- **Structure:** promise ("By the end of this article you'll understand…") → "Three Big Lies" (nose, jaw, CPAP — with "dentists love… profit margins") → "What IS the real problem?" = **26-degree cervical curve** + gravity → "Here's what's really scary" (brain oxygen 200–400×/night, **dementia risk**) → wife "came to me in tears" vignette → "What Actually Works" (**product ~60% down**) → results timeline Night 1 / Week 1 / Week 2–3 / Month 1 → "Your Brain Is Counting on You" (50% off, 60-day guarantee, "sold out within days", "thousands reading this same article") → 2 CTAs → footer disclosure.
- **CTAs:** 3–4.
- **Why it works:** enemy framing + "it's not your fault" + fear escalation.
- **Compliance flags:** "Your snoring stops completely" on Night 1; dementia/cognitive-decline fear; disparages dentists/CPAP (medical devices); fabricated statistic "26-degree angle".

### 6. Restora — adv5 "I Tried Everything to Stop Snoring — CPAPs, Bulky Mouthguards, Nose Strips. Then My Doctor Recommended This."
- **URL:** https://sleeprestora.com/pages/adv5 · Live.
- **Format:** news-style Q&A explainer (each H2 is a reader question: "Okay – but if snoring is caused by my neck position, will sleeping on my side fix it?").
- **Authority device:** "**By Dr. Daniel Foster**" with headshot + green tick + date (September 20, 2025, printed twice) + "1,628 Ratings" stars + "Trending in the US" badge + "Advertorial" label at top. Fabrication read: high (**INFERENCE**: no credential, no institution).
- **Structure:** sub "If you're still snoring in 2025, read this brief guide…" → symptom checklist → prevalence stat (44% M / 27% F) → "why haven't we cured it?" → root cause = neck → side-sleeping objection → CPAP vs cervical pillows ("two medically-validated approaches") → "what are cervical pillows?" → price objection ($150–$300; insurance doesn't cover) → "3 choices" (ignore = hypertension/heart disease/cognitive decline; pro pillow $250–350; Option 3 = Restora, **product ~55% down**) → "what makes it different" → vs regular cervical pillows → "what's the cost?" → "under $65" → 3 reviews (2 duplicated text: James K./David R. identical) → 50% "under $50" (contradicts "under $65") → 30-day **and** 60-day guarantee (contradictory) → "Remember why this matters" → 2 CTAs → **16 fake Facebook comments** incl. objection-seeded ones ("Anyone worried about durability?" → "mine has held up great").
- **CTAs:** ~6.
- **Why it works:** Q&A format pre-empts objections in the reader's own voice; "3 choices" close; comment section does objection handling socially.
- **Compliance flags:** fake doctor; fake comments; contradictory prices & guarantees; duplicated testimonials; serious disease-claim fear.

### 7. Mellow — wp-adv-2 "My Chiropractor Told Me to Stop Wasting Money on Pillows. Then She Showed Me This One."
- **URL:** https://mellowsleep.com/pages/wp-adv-2 · Live. WH: **109 active ads, 215 days, +419% in 90 days**; advertisers include "Anthony Moll", "Heim Health", "Kayla Vashti", "Dr. Ralph Napolitano" (405k IG), "Jess's Favorite Finds" — i.e. **whitelisted creator/doctor pages** running the same lander. Store est. $19–36M/mo.
- **Format:** first-person story + expert reveal. OG title "The Pillow That Saved My Neck"; OG description "I didn't want to end up like my uncle."
- **Authority device:** **"Dr. Heather Heim"** — "chiropractic degree plus specialized certifications in postural neurology and ergonomic design… nearly two decades." Heim also appears as a Loox reviewer ("Dr. Heather H. — I've been recommending this to all of my patients") and as an ad-running page "Heim Health" (17.8k IG). Looks like a **real, paid practitioner partner (INFERENCE)** — the most credible "doctor" in the pillow set.
- **Headline/byline/disclosure:** "Advertorial" label above H1 (small); subhead "There's a reason most 'memory foam' and 'orthopedic' pillows don't work…"; byline "By Jackie S | Sun, November 1, 2026" (recent, plausibly rotated).
- **Structure:** "car accident in my sleep" symptoms (stiff neck, numb arm, ibuprofen) → 7 months → cycle (aging at 38, work, partner) → "Tried everything" (Amazon memory foam, contour pillow "hard plastic mold", chiro 2×/week) → fear (uncle's cervical surgery; gave up tennis; blind-spot driving) → went to Dr. Heim → named mechanism **"shoulder gap mismatch"** + "fixed curve fits 10% of people" → she pulls pillow from cabinet (**product ~65% down**) → features (3.5"/4.3" dual height, "arm tunnel", side wings, dense foam) → results at 14 days → gratitude/travel → CTA "Relieve Your Neck Pain" → "Here's How it Works" → review images → "Stock Is Running Low… viral" → 30-day MBG → 2 CTAs.
- **Mechanism:** "shoulder gap mismatch" (named, ownable) + dual height to fit your body.
- **Proof:** chiropractor endorsement, review screenshots (images), social virality claim.
- **CTAs:** 4 (Relieve Your Neck Pain / See Availability / Finally Free Yourself of Neck Pain / See Availability) → PDP.
- **Why it works:** pre-empts the #1 objection ("I've tried contour pillows — they're hard plastic molds") by attacking contour pillows itself; the expert *gatekeeper* ("I don't usually recommend specific products") gives permission to buy.
- **Compliance flags:** "Relieve your neck pain" claims; surgery fear; "selling out" scarcity; anecdotal "hundreds of patients". Disclosure present but tiny.

### 8. Mellow — heim-adv-1 "Sleep Better Tonight: Chiropractor-Recommended Cloud Align Pillow"
- **URL:** https://mellowsleep.com/pages/heim-adv-1 · Live. WH: **142 active ads, 267 days, +238% 90d**. `noindex`. Built on the **GiddyUp** template ("CloudAlign Pillow has partnered with GiddyUp, a curator of innovative products").
- **Format:** not an article — a long "pre-sell sales page" with embedded buy box (same skeleton as Dosaze #9 and Blissy #12).
- **Authority device:** "Heather Heim — Board-Certified Chiropractor" with photo + quote; "AS SEEN IN" TikTok, Grommet, FOX, CBS logos; "Award-Winning Softest Pillow of 2025"; "Best Pillow 2025"; "Innovation in Sleep Award — Winner of the 2025 SleepTech Summit" (unverifiable, **likely fabricated — INFERENCE**); "Patented Ergonomics"; "#1 Selling Pillow On TikTok"; "Rated 5 Stars By 99%".
- **Structure:** countdown "Today Only 50% OFF" → H1 + sub → pull-quote review → CLAIM YOUR DISCOUNT → As Seen In → 4 trust icons → "Why Chiropractors Recommend Cervical Alignment" → "Notice the difference on night one" slider → "The Wrong Pillow Can Keep Muscles On Guard All Night" (too flat / too tall / too soft / too hot) → benefits list → "Patented 3-in-1 Design" 3 zones → "Reduces Snoring, Boosts Energy… Relieves Snoring & Symptoms of Sleep Apnea" → Chiropractor Review video → OEKO-TEX cooling → comparison table vs "Others" → sleep-style cards → reviews → awards → "Designed By Chiropractors… While other doctors treat symptoms" → 6-tile guarantee (30-night, 1-yr warranty, free shipping…) → buy box ($49.99 vs $100; bundles 2/4; "Only 12 pillows left at this price"; "Order within 01:58") → Loox reviews → FAQ.
- **Product first appears:** in H1 (0%).
- **CTAs:** ~8 + buy box.
- **Compliance flags:** "Relieves… Symptoms of Sleep Apnea"; likely fabricated awards/"As seen on" news logos; fake stock counter; fake countdown.

### 9. Dosaze — (formerly "3 reasons why thousands choose…") now "Sleep Better & Wake Up Completely Pain-Free"
- **URL scraped:** https://dosaze.com/pages/3-reasons-why-thousands-choose-dcop → **301 to** https://dosaze.com/pages/sleep-better-wake-up-ache-free · Live. The listicle the brain cited (target of the "Moms Need a Better Pillow" ads) is **no longer served**; mom ads now land on a generic sales page.
- **Format:** GiddyUp-style long sales page (near-identical section headings to Mellow #8 and Blissy #12: "You'll Feel The Difference On Night One", "YOU'LL NEVER GO BACK!", "Stop Waking Up In Pain — Start Sleeping Like…", "Perfect For Every Type Of Sleeper", "99% Of Customers Give X 5 Stars!", "Sleep Like You're In A Luxury Hotel", "Your Satisfaction is Our Priority", "MISSION-DRIVEN").
- **Authority device:** "Designed & Endorsed By Top Chiropractors" — quote from "**Dr. Jandi R.**, Licensed Chiropractor" (first name + initial only); "Award-Winning Best Pillow of 2026"; "#1 Selling Pillow On Google"; "Over 500K Pillows Sold"; "patented design was created by chiropractors and sleep researchers"; "2 Years of R&D, 50+ Foam Tests"; CertiPUR-US/OEKO-TEX.
- **Structure:** BOGO countdown → H1/sub → review quote → CTA → 4 trust badges → night-one claim → chiro quote → "Real Science Meets Deep Comfort" → pain-free promise → 3 sleep zones → "Relieves Pain, Reduces Snoring" → comparison table → sleep-style cards → reviews → materials → R&D → 6 guarantees (60-night, 10-yr warranty) → buy box ($119.99 single; BOGO $139.99; "Only 12 pillows left at this price") → Okendo-style reviews (4.92/1,820).
- **Mom angle on page:** **none** (grep for mom/nurs/baby/feed returned only unrelated hits). Confirms brain: mom angle exists only in ad creative.
- **Compliance flags:** "Completely Pain-Free"; anonymized doctor; unverifiable award; fake stock count.

### 10. Neckline — "Doctors Keep Missing This: The 15-Minute Solution Eliminating Mystery Symptoms in Over 47,000 People"
- **URL:** https://neckline-us.com/neckline-usa/adv-opt · Live (Funnelish). WH: 52 active ads, 132 days; **ad pages named "The Daily Health Post" (27 ads), "Chris Walters", "Barbara Smith", "Brian Davidson"** — fake publication + fake-person pages. Store small ($18–30k/mo).
- **Format:** fake-news "investigation" with "Advertorial" + "Trending in the US" header, dated "June 2026".
- **Authority device:** "**Dr. Michael Chen**, a brain and nerve specialist at **Stanford Medical Center**, recently studied 847 patients" + "Dr. Richardson's team tested it on 50 patients" + "medical device engineer Thomas Keller"; "Research from **Johns Hopkins** found…heat increased neck blood flow by 47%". Uses real institution names. **Fabrication read: very high / most dangerous in set (INFERENCE).**
- **Structure:** "huge problem in medicine" → "The culprit? Your neck." → Dr. Chen study (89% given antidepressants) → "Your Neck Controls More Than You Think" (cascade effect) → "Why Doctors Get It Wrong" (Sarah Mitchell, 43) → "Why Normal Treatments Don't Work" (chiro "can cause a stroke") → "Four-Part Solution" (EMS, heat, massage, traction) → "$3,000/Month Clinical Solution Now $119.99" (**product ~55% down**) → device features → "94% less neck pain… 79% less anxious" → 2 testimonials (ER visits, panic attacks) → why it works → cost stack → 30-day guarantee ("<1.3% refunds") → "What Happens If You Don't Act" (permanent nerve damage) → "Your Two Choices" → 3 CTAs.
- **CTAs:** 4–5 ("Get Neckline at 50% off…", "Apply Discount & Check Availability", "Check Availability").
- **Compliance flags:** fabricated doctor at a real institution, fake study, disease claims (anxiety, dizziness, palpitations, herniated discs), fear of permanent damage, disparaging medical care. **Do not imitate.**

### 11. Cevera — "Women's Wellness Report™" / "Top Physical Therapists: 'This Is the Fastest Way to Reduce Your Neck Hump For Good'"
- **URL:** https://trycevera.com/pages/adv-womens-wellness-report · Live. WH: **150 active ads**, 159 days, +233% 90d; ad pages "Carol M. Bennett, PT" (46 ads), "Posture After 60", "Barbara Linfield", "Posture Health Daily", "Robert Callahan". Store tiny (~$2–4k/mo est., NL-based) — volume ≠ revenue.
- **Format:** fake publication masthead + breadcrumb (`Women's Wellness Report™ · Home › Health › Posture & Spine`) + date/time + view count ("231,893") → then a classic long-form sales letter ("Dear Friend With a Neck Hump").
- **Authority device:** "Written by **Sarah Mitchell, DPT** — 22 years, 3,400 patients, Nashville, taught at two PT schools"; emotional family proof (her mother Dorothy, 72, couldn't place the Christmas star); "Jennifer R., DPT" testimonial; "peer-reviewed manual therapy journals" (none cited).
- **Disclosure:** only at the bottom, in caps: "THIS IS AN ADVERTISEMENT AND NOT AN ACTUAL NEWS ARTICLE…" + "The story depicted on this website is illustrative. Results portrayed are illustrative" — i.e. **the page admits the DPT story is fiction**.
- **Structure:** "Dear Friend" conditional list → "will make you angry… $47 billion industry… they bury it" → credentials → "The Night Everything Changed" (mother) → failed experts (chiro $2,280/yr, PT, brace, PCP "it's part of aging") → "Mind-Blowing Discovery" ($14,000 research) → root cause (suboccipital contracture, "10 lb per inch") → "10-Minute Miracle" (**product ~60% down**) → "Pissing off an industry" → "$47 billion, they come for you" (licensing complaint, lawyers) → product mechanism → minute-by-minute protocol → stats (91%, 4,800+ reviews, <1%) → 4 testimonials → cost table → "50% 'In Their Face' Discount" → 90-day guarantee → "The Catch" (72 hours, 4,200 units) → "Two paths" → 6-step "what to do next" → sign-off + P.S./P.P.S./P.P.P.S. → sticky sidebar.
- **CTAs:** ~8.
- **Why it works:** intensely emotional, identity-based (vanity + aging + family), villain narrative, and a single tiny daily ritual.
- **Compliance flags:** fictional DPT (self-admitted "illustrative"), fabricated industry persecution, "reverses your neck hump" claims; fake masthead/view count. Its disclaimer is the template to note: *"Testimonials are from real customers… The story depicted… is illustrative."*

### 12. Blissy — listicle URL "pillow-reasons" → "Sleep Better & Wake Up Totally Ache-Free!"
- **URL:** https://latest.blissy.com/pillow-reasons → redirects to try.blissy.com/checkout-15 (Next.js headless). WH: 13 active ads (from 32 a month ago), 41 days. Store ~$1.1–1.7M/mo.
- **Format:** classified by WH as listicle, but **the live URL serves a long sales page** (same GiddyUp-family skeleton). The "reasons" listicle is either A/B-routed or retired (**INFERENCE**).
- **Authority device:** **independent 28-day home study by Kosmoscience (ISO 9001 / REBLAS-accredited), Report TR-BSY006-26-F-1-R0**, dermatologist-reviewed, "0 adverse events" — numbers framed as *perceived* effectiveness (86% slept better, 94% neck comfort, 91% less stiffness). Plus "As Seen In" Forbes/Oprah Daily/Allure/Good Housekeeping/Glamour/Marie Claire; 2 named chiropractors (Dr. Krystal Phillips, Dr. Kenneth Paul Wark); 3M+ customers, 230k+ reviews.
- **Compliance read:** the cleanest "science" device in the set — specific lab, report number, and correct "perceived effectiveness… individual results may vary" phrasing. Still carries "Relieves snoring & symptoms of sleep apnea" bullet (red flag).
- **CTAs:** ~6 + buy box (bundles, 55% off "Today Only" countdown).

### 13. Frilume "Cervicare" — Meta ad from "Sarah's Wellness Journal" (advertorial-in-the-ad)
- **Source:** WinningHunter `search_facebook_ads` (pagename "Sarah's Wellness Journal"): image ad, started & last seen **2026-09-10**, US; caption **"Read this if you have neck pain ☝️"**; description "Frilume"; destination **frilume.com/products/cervicare**. Frilume's pages now show **0 active ads** (`get_store_top_ads`). PDP scrape failed (site TLS certificate error) — **page content unverified**.
- **Format:** long-copy **native Facebook post** that *is* the advertorial (WH stores ~2,000 chars; truncated there). First-person **new mom**:
  - Opening line: "**Advice to new moms who want their pain free neck back - from a mom who almost accepted it.**"
  - Beats in captured copy: 11 PM after an hour of rocking → heating pad, phone above face, YouTube "neck and shoulder pain relief" → PT with 3M views, "Fix your neck in 15 minutes" → did it while baby in bouncer → relief for an hour → nap-window consistency problem → **obsessive nursing posture checklist "at every single feed — 2 AM, 4 AM, half asleep in the glider"** → switching football hold / side-lying / cross-cradle → icing → heating pad "47,000 reviews" … (truncated before product reveal).
- **Authority device:** none expert — persona page named like a personal blog ("Sarah's Wellness Journal"), *peer* authority ("from a mom who almost accepted it"). The same page ran menopause/bloating/mood stories for 44–49-year-old women in March 2026 → **rented, multi-product persona page (INFERENCE)**.
- **Why it matters for us:** this is the **only competitor piece in the set written in a new-mom voice with real feeding-night specifics** — and it was for a traction *device*, not a pillow, and it appears to have been switched off after one day of tracking (**INFERENCE**: test that didn't scale, or account issue).
- **Compliance flags:** persona page name implies an independent journal; product is a cervical traction device (medical-adjacent).

### 14. 8 Sheep Organics — "5 Reasons Every Postpartum Mom Should Keep Up Her Belly Care (Even When Life Gets Crazy)"
- **URL:** https://8sheep.com/pages/5-reasons-every-postpartum-mom-should-keep-up-her-belly-care · Live. WH: ads 2026-05-26 → last seen 2026-11-07 (~165 days, still running). Brand page "8 Sheep Organics" (real brand, Indiana/DE address).
- **Format:** listicle, brand-site native (no fake masthead), "5 Minute Read".
- **Authority device:** byline "**Emily Taylor** | March 31, 2026" with circular headshot (role unstated → ambiguous persona, **INFERENCE**); concept authority via a **time-window mechanism** ("first 12 months = wet cement"); "2 ingredients with clinical evidence"; cost reframe "$1.57/day vs $200–$500 per laser session".
- **Structure:** subhead "Most moms stop their skincare routine the day baby arrives…" → empathy ("disappeared somewhere between the 3am feeds and the mountain of laundry") → Reason 1 (remodeling window; wet-cement analogy + two-column "Cement Is Wet / Has Set" + stat strip) → CTA → Reason 2 (red marks still "active") → CTA → Reason 3 (C-section scar collagen; safety note "wait until incision is fully closed") → CTA → Reason 4 (skin tightening) → CTA → Reason 5 (most products wrong ingredients) → **product named in Reason 5 (~60% down)** → ingredient cards → comparison table incl. **"Safe while breastfeeding"** row → embedded buy box (bundles 10–20% off) → 100-day guarantee ("Even if you've used up the entire bottle… No need to return the product") → FAQ (breastfeeding safety, C-section timing).
- **CTAs:** 6 identical "Try True Belly Serum Risk-Free".
- **Why it works:** a *time-limited biological window* creates urgency without fake countdowns; mom-specific safety objections (breastfeeding, C-section) answered inline; modest discounts; hedged language ("may help", "supports").
- **Compliance flags:** low. Byline role unclear; "clinically studied ingredients" (not product) is the standard compliant phrasing.

### 15. 8 Sheep Organics — "Most Moms Stop Their Belly Care Too Early… And They Only Realize It When It's Too Late."
- **URL:** https://8sheep.com/pages/true-belly-serum-advertorial · Live, indexed. WH: multiple ads, last seen 2026-11-04/07.
- **Format:** brand-site editorial (breadcrumb "Pregnancy › Skincare", "6 minutes to read"), opens with an **unattributed mom pull-quote** ("I was so focused on the baby I completely forgot about myself…").
- **Authority device:** a **real, citable PubMed Central quote** with PMC ID (PMC11643272, 2024) shown with a "PMC – PubMed Central" logo; real Stamped reviews visible with full distribution (4.6★, 470 reviews, **including 21 one-star**); founder voice in guarantee ("send me an email").
- **Structure:** pull-quote → "you are not alone" → reframe (skin keeps changing) → 12-month window → 3 outcomes (stretch marks, C-section scars, loose skin) → product "made for this exact stage" (**~50% down**) → 2 ingredients w/ PMC quote → "Loved By Moms Across The US" → CTA → 4 trust ticks → UGC "Wall of love" → CTA "Check for Availability" → full review widget + Q&A → final product card.
- **CTAs:** 4–5.
- **Why it works:** emotional mom-identity hook ("forgot about myself") + regret framing + verifiable science + honest reviews → high trust.
- **Compliance flags:** minimal. Shows what a compliant mom pre-sell looks like.

---

## 2. Synthesis

### 2a. The dominant authority angles (ranked by prevalence in this set)

1. **Invented / thinly-sourced "doctor" persona (Dr., DPT, "Sleep Science Specialist")** — Groove (Dr. Lauren Whitaker), Restora (Martin H.; Dr. Daniel Foster; historically "Laura J. Mitchell, PhD"), Neckline (Dr. Michael Chen @ Stanford), Cevera (Sarah Mitchell, DPT — self-admitted "illustrative"), Dosaze (Dr. Jandi R.). 5 of 12 non-mom pages. The name **"Sarah Mitchell"** appears in three different funnels (Neckline patient, Cevera DPT, Restora commenter) — a tell of templated copy.
2. **Chiropractor-as-gatekeeper** — Mellow (Dr. Heather Heim, looks like a real paid partner with her own ad page), Dosaze, Blissy, Groove ("1,000 practitioners", physio reviews). The chiro "who doesn't usually recommend products" gives permission to buy. Mellow (the biggest spender by far) leans hardest on it.
3. **Relatable first-person sufferer story** — Derila (wife, mechanic), Restora adv1 (husband), Mellow wp-adv-2 (Jackie S), Frilume ("a mom who almost accepted it"), 8 Sheep (mom pull-quote). Usually combined with #1 or #2 at the reveal.
4. **Borrowed institutional/media proof** — "As Seen In" FOX/CBS/Forbes/Oprah logos (Mellow, Blissy), awards of uncertain origin ("SleepTech Summit", "Best Pillow of 2026"), "#1 on TikTok/Google", fake publication mastheads ("Women's Wellness Report™", "The Daily Health Post", "Sarah's Wellness Journal").
5. **Real, checkable science** — only Groove (2 systematic reviews + DOIs), Blissy (named lab + report #) and 8 Sheep (PMC ID). These are the most credible pages and none of them needed a fake doctor to carry the argument.

### 2b. Credible vs scammy (spectrum)

- **Most credible:** 8 Sheep (both), Groove, Blissy. Pattern: real citations, real review distributions, hedged language, long guarantees, modest or no countdowns.
- **Middle (real brand, aggressive template):** Mellow (both), Dosaze. Real reviews/practitioner but stacked fake-feeling awards, "only 12 left" counters, countdowns, "relieves sleep apnea symptoms".
- **Scammy:** Derila (military/reflexology, fake editor, auto-dates, fake comments), Restora (fake doctors, fake comments, disease fear, contradictory prices/guarantees), Neckline (fake Stanford doctor & study — worst), Cevera (fictional DPT, persecution narrative, self-admitted illustrative). Derila + Restora share the **identical footer disclosure text** ("…MARKETING DISCLOSURE: This website is a market place…"), suggesting a shared agency/template (**INFERENCE**).

### 2c. Structural patterns

- **Two templates dominate:**
  - **A. Story advertorial** (Derila, Restora adv1/4/5, Mellow wp-adv-2, Neckline, Cevera, 8 Sheep adv): cold open → symptom mirror → failed-solutions list (chiro, PT, CPAP, Amazon pillows, exercises, braces) → named hidden cause/mechanism → discovery via authority or accident → product reveal at **~45–65% down the page** → timeline of results (Night 1 / Week 1 / Month 1) → testimonials → cost-stack vs "what you're spending now" → guarantee → scarcity → 2–3 final CTAs → (fake) comments.
  - **B. GiddyUp-style "pre-sell sales page"** (Mellow heim-adv-1, Dosaze, Blissy, Groove's second half): product in H1, then benefit modules, "too flat/too tall/too soft" diagnosis, 3-zone diagram, us-vs-them table, reviews, guarantees tiles, embedded buy box. Headings are near-verbatim across Mellow/Dosaze/Blissy.
- **Listicles are fading in pillows:** Dosaze's "3 reasons" and Blissy's "pillow-reasons" URLs both now redirect to Template B sales pages. The only live, ad-receiving listicle in the set is 8 Sheep's postpartum "5 Reasons".
- **Length:** story advertorials ~1,500–3,500 words (Cevera longest, ~4,500); Template B pages are shorter in prose but very long in modules.
- **Mechanism vocabulary (pillows):** "shoulder gap" (Groove, Mellow "shoulder gap mismatch", Dosaze), "26° cervical curve" (Restora), "too flat/too tall/too soft/too hot" (Mellow), "dual height" (Mellow 3.5"/4.3", Dosaze 3"/4.5", Groove 4 zones), "arm tunnel/cut-out" (Mellow, Groove, Restora), "muscle tension / reflexology" (Derila). Groove alone frames it as **overnight recovery** ("your neck is not getting the recovery it needs").
- **Offer mechanics:** 50–70% off is near-universal; countdown timers and "only 12 left" (Mellow, Dosaze use the *same* "Only 12 pillows left at this price" string); BOGO (Dosaze); guarantees 30–100 nights (Groove 100, 8 Sheep 100 days no-return, Restora 30/60 contradictory, Mellow 30, Dosaze/Blissy 60).
- **CTA count:** 3 (Groove) to ~15+ linked elements (Derila). Median ≈ 5–8 buttons. Wording is almost always availability/discount-framed ("Check Availability", "Claim Your 50% Discount", "See If Units Are Left").
- **Disclosure:** "Advertorial" label appears on Restora, Mellow wp-adv-2, Neckline (small, top). Derila/Restora/Cevera rely on a footer boilerplate. **Groove, Dosaze, Mellow heim-adv-1, Blissy, 8 Sheep show none** (they are on the brand's own domain and branded, which is arguably self-disclosing — **INFERENCE**).

### 2d. Gaps — what NONE of the pillow advertorials do (especially for a new mom)

1. **No pillow advertorial is written for a new mom.** All pillow pages cast generic sufferers: snoring husbands, mechanics in their forties, 38-year-old office workers, 60+ women with neck humps. Dosaze's mom ads land on a page with **zero** mom content. The only new-mom neck story found (Frilume / "Sarah's Wellness Journal") sold a traction device, lived in the ad body, and appears to have stopped (last seen 2026-09-10).
2. **No one uses the nighttime-feeding reality as the mechanism.** The Frilume ad lists it (2 AM / 4 AM feeds, glider, football hold, side-lying, posture checklist at every feed) but as *symptoms*, not as a "why sleep can't repair it" mechanism. Groove's "your neck is not getting the recovery it needs" is the closest recovery framing — generic, not mom.
3. **No peer-mom authority.** Every authority is a clinician (real or invented) or an anonymous sufferer. Nobody uses a mom community voice (e.g. lactation consultant, postpartum doula, pelvic-floor/postpartum PT, or "moms in my group") — and 8 Sheep shows a mom-to-mom brand voice + real citation converts in the adjacent category.
4. **No mom-specific objections handled.** None of the pillow pages answer: "Can I use it side-lying next to the bassinet?", "Will it help when I fall asleep mid-feed in the glider/sofa?", "Is it safe around the baby / co-sleeping guidance?", "Washable for spit-up/milk?", "I have no time for a 2-week adjustment period". 8 Sheep proves the format: answer breastfeeding and C-section safety inline in a FAQ/table.
5. **No time-window urgency.** All pillow pages use fake scarcity (countdowns, "12 left", "warehouse clearance"). 8 Sheep's "first 12 months = wet cement" shows a *biological/life-stage* urgency that needs no fake timer — no pillow brand uses a life-stage window (fourth trimester / first year of feeds).
6. **No honesty signals.** Only 8 Sheep shows its 1★ reviews and a founder's email. None of the pillow pages show negatives, real customer photos of moms, or a named real founder/mom — an easy credibility gap.
7. **No identity/permission frame.** Cevera hits identity (aging, photos) for older women; nobody tells the new mom "your recovery matters too" — the brain's locked §4 positioning is unoccupied in advertorial form.

### 2e. Compliance red flags to avoid (observed)
Fabricated doctors (esp. at real institutions — Neckline/Stanford, Johns Hopkins); fabricated studies/stats ("26°", "47,000 people", "94% less anxious"); disease claims (sleep apnea, dementia, hypertension, anxiety, herniated discs); auto-updating dates and "6 hours ago" bylines; fake comment sections (Restora adv1/adv5, Derila); fake publication mastheads (Women's Wellness Report™, The Daily Health Post, Sarah's Wellness Journal); persecution narratives (Cevera); perpetual "today only"/countdown/"12 left" scarcity; unverifiable awards and news-logo "As seen on"; footer-only disclosure; contradictory prices/guarantees (Restora adv5).

---

## 3. Sources (all scraped/queried 2026-11-08)
- Firecrawl: groovepillows.com/pages/probably-your-pillow · derilashop.com/articles/in-tears-every-night (404) · derila.com/articles/in-tears-every-night · derila.com/article/derila-military-sleep-method · sleeprestora.com/pages/adv1 · /adv4 · /adv5 · mellowsleep.com/pages/heim-adv-1 · mellowsleep.com/pages/wp-adv-2 · dosaze.com/pages/3-reasons-why-thousands-choose-dcop (→ /pages/sleep-better-wake-up-ache-free) · neckline-us.com/neckline-usa/adv-opt · trycevera.com/pages/adv-womens-wellness-report · latest.blissy.com/pillow-reasons (→ try.blissy.com/checkout-15) · 8sheep.com/pages/5-reasons-every-postpartum-mom-should-keep-up-her-belly-care · 8sheep.com/pages/true-belly-serum-advertorial · frilume.com/products/cervicare (FAILED: TLS certificate error).
- WinningHunter: `search_landers` (pillow/advertorial; neck/advertorial US; derila; neurogena; posture/advertorial/Health; pillow/listicle; groovepillows.com url; sleeprestora.com url; frilume; postpartum) · `search_facebook_ads` (pagename "Sarah's Wellness Journal"; adtext "postpartum" funnels US; landingurl "frilume") · `get_store_top_ads` (frilume.com, neurogena.us).
- Brain context: brain/01-market-and-competition.md, brain/04-brand-offer-funnel.md.

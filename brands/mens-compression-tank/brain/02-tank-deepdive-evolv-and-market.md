# TANK DEEP-DIVE: men's compression slimming tank / undershirt

Date: 2026-10-28. Ad window: last_seen 2026-10-14..2026-10-28 (en; US where filtered).
Raw data: /tmp/claude-0/-home-user-NG/d2b4b092-9cc3-516e-bf3f-dd82c1be3fba/scratchpad/hunt2/tank/ (ev*.json, evp1-4.json, k_*.json, tp_neg.md)

## 0. HEADLINE CORRECTION TO PRIOR RESEARCH

men-desire.md said there was "one heavy DTC incumbent on Meta and no visible second DTC garment seller". **That is wrong.**
The earlier check searched "gynecomastia" in ad text. Only Evolv uses that word, which is why it looked like a single seller.
A search for "compression tank" turns up a crowded market (section 3):

| Seller | 30d revenue (WH est.) | Live ads on page | Price |
|---|---|---|---|
| **North Alpine** (north-alpine.com) | **$6.2M–10.3M** | 1,180 | $29.90 |
| Evolv (evolv-off.com) | $2.2M–3.8M | 347 | $60 |
| Selure Wear (selurewear.com) | $1.8M–3.6M | 171 | $19.95–29.95 |
| InShape (in-shape.co) | $25–50k | 1,739 | $44.90 |
| Rounderbum | not checked | 357 | $59 |
| Alphacore (big guys) | $3–7k | 321 | $24.95 |
| Nebility | not checked | 173 | not seen |
| Qore Logiq (tall) | $24–42k | 108 | $32.99 |
| Temu | n/a | n/a | n/a |

Evolv is **not** the leader. North Alpine is an Evolv clone that launched in March 2026 at half the price, and it is now 2–3x Evolv's size.

---

## 1. EVOLV TEARDOWN

### Store (get_store_details evolv-off.com)
- **Revenue:** 30d estimate $2.2M–3.8M; 1d estimate $79k–136k; WH AOV estimate $40.79.
- **Traffic:**

  | Month | Visits |
  |---|---|
  | 2025-12 | 123k |
  | 2026-01 | 320k |
  | 2026-03 | 328k |
  | 2026-06 | 167k |
  | **2026-08** | **539k (peak)** |
  | 2026-09 | 360k (−33% MoM) |

  100% of traffic is US, although ads also target CA, AU and NZ.
- **Products:** 8. V-Boost v2 ($60, tags "Program") is #1. The rest:

  | Product | Price |
  |---|---|
  | Package insurance add-on | $2.99 |
  | V-Short | $24.99 |
  | V-Shirt | $26.95 |
  | V-Shape | $29.99 |
  | V-Boost V-Neck | $70 |
  | V-Socks | $25 |
  | V-Boost Long Sleeve | $41.99 |

- **Apps:** Klaviyo, GoAffPro, **Recharge Subscriptions**, **Kaching Bundles**, Essential Countdown Timer, UpCart, Parcel Panel returns, Intelligems (A/B testing), Triple Whale. The theme is "Motion | AB Test || NEW".
- **Trustpilot:** 3.4 (317 reviews). There are 103 negative reviews, and Evolv replied to 68% of them.
  - Its Trustpilot "competitors" list: North Alpine (1,144 reviews), Shaperluv, Selurewear, Mars Men, tryevolv.com.
- **Trustpilot gap_links (WH AI clusters), product-related only:**

  | Complaint | Reviews |
  |---|---|
  | Lack or absence of advertised compression | 5 + 6 + 3 + 2 + 3 = **19** |
  | Rides up | 6 + 3 = **9** |
  | Inconsistent sizing | 8 + 4 + 3 + 2 = **17**, including "color-specific sizing" and "2 of 3 shirts smaller" |
  | Too short for torso / tall | 5 + 2 = **7** |
  | Thin fabric / poor durability | 5 + 3 + 1 = **9** |
  | Misleading claims | 3 + 1 = **4**, plus "suspected scam" 6 |
  | **Armholes too tight for larger customers** | 2 |
  | **Visible V-neck under open-collar shirts** | 1 |
  | **Visible blue markings through white work shirts** | 1 |
  | Skin irritation | 1 |

### Product page (scraped 2026-10-28)
- **Price:** $60 flat for every size and colour. The 5 colours are Black, White, Grey, Red and Blue.
  - The page has no compare-at price.
  - A sitewide bar reads "Early Halloween Sale. Save up to 70% on bundles".
  - The bundle ladder comes from Kaching and did not render in the scrape. The ads show **Buy 2 Get 1 Free**.
  - There is a 🚨 "OFFER ENDS IN" countdown and "Best Seller – Over 5000 sold this week!".
- **Sizing:** sizes run S–5XL **by body weight only**: S 110–154, M 154–198, L 198–243, XL 243–287, 2XL 287–331, 3XL 331–375, 4XL 375–419 and 5XL 419–463 lbs.
  - The page advises "if near the upper end go one size up".
  - Two ads contradict this: one says "order one size below yours, if you're really big come down two".
  - There are no chest, waist or torso-length measurements.
- **Material:** the page contradicts itself. It says "90% polyester, 10% spandex" in the Overview but "80% nylon, 20% spandex" in the FAQ. A Trustpilot reviewer says the label reads 90/10 polyester.
- **Claims:**
  - Bullets: "Promotes weight loss", "Reduces gynecomastia", "GET RID OF DAD BOD".
  - Technology claims: "Ionic Ice technology… boosts circulation, activates your muscles", "mineral-infused fibers", "Enhanced action on love handles to **break down fat cells**".
  - Stats: "91% noticed visible weight loss in 30 days", "John Smith – dropped 30 lbs in 2 months" (stock photo).
  - Logos: "Featured in" press logos.
  - It also carries a "vs cheap knockoffs" comparison image.
- **Guarantee:** "60-day money-back guarantee". In practice it is "unworn, unwashed, original tags".
  - Evolv's own reply says this.
  - Reviewers call it "a two-minute guarantee".
  - Returns are at the customer's cost, and refunds are partial.
- **Other offer elements:**
  - Free shipping in 5–8 or 6–8 business days.
  - "100,000+ Happy Customers" vs "50,000 satisfied" vs "25,000 customers" (Trustpilot about-page), so the social-proof numbers are inconsistent.
  - Package insurance at $2.99.
- **Subscription / pre-ticks:** Recharge is installed and the product is tagged "Program". No subscribe option was visible in the scraped PDP HTML, and checkout was not reachable. **Unverified** whether a subscription or a pre-ticked box is offered.
- **Advertorial:** https://evolv-off.com/pages/lp-v-boost-5-reasons (2 of 80 sampled ads point there).

### Evolv Meta ads
- **Page:** Evolv, page_id 407694675756821, created 2024-08-06. **347 active ads**.
  - Landing-URL search "evolv-off.com" = 601 matches in the window.
- **Sample:** 4 pages sorted by top rank, giving 80 distinct ads covering ranks 1 to about 100.
- **Format:**

  | Format | Ads | Share |
  |---|---|---|
  | Image | 39 | 49% |
  | Video | 36 | 45% |
  | DCO | 4 | 5% |
  | Carousel | 1 | 1% |

- **Countries:** all 80 ads target US, CA, AU, NZ (and AX); 5 also target GB.
- **Landing:** 78 of 80 go to the PDP and 2 to the advertorial.
- **Freshness:** 26 of the 80 launched in October and 20 in August. The oldest live ad dates from 2025-09. This is heavy, ongoing creative testing.
- **Body copy:** about 85% use one template: "Say goodbye to beer belly, love handles and men's breasts… eliminating stubborn belly fat, back pain, and gynecomastia".
- **Headline:** every ad leads with the offer. "2+1 FREE TODAY" appears in 47 ads and "Buy 2, GET 1 FREE" in 16; the others are Black Friday, Halloween and "Make 2026 your year".
- **Link description:** "Over 100.000+ satisfied customers" in 53 ads.
- One DCO description lists spec claims: "S-5XL | True to size | Invisible under any shirt | **Anti-slip grip technology** | Targeted compression zones | **Medium compression**".
- **Correction to men-desire.md ("one tired angle"):** the body copy is one template, but the **video creatives are varied**.
- **Hooks from 7 transcripts (Whisper):**

  | Ad (rank) | Hook | Angle |
  |---|---|---|
  | 1434518311834071 (#3) | "If you wear this strange-looking compression tank that nobody talks about every day instead of that gym membership…" | Day 1 → Week 4 timeline: posture, coworkers ask, "wife does a double take", fake study claim ("Hirosaki Univ… 5.67x more weight"), "stop avoiding family photos", "stop living in XL shirts" |
  | 1069015275648232 (#4) and 1085328553842710 (#5) | "Bro is 250 pounds… I'm 6'3"" | UGC big-guy try-on: same shirt without vs with tank, zone panels, a bend/arms-up/twist test ("Big as I am, it doesn't ride up"), "My wife noticed" |
  | 908814305497586 (#15) | "What happens in 30 days to the guy who drops 400 pounds of gut on his wife during sex…" | Day 3 "tucks his shirt in for the first time in 10 years"; Day 7 "stopped tugging his shirt down"; "drops four fingers below the waistband, which is why it doesn't ride up"; "wears t-shirts in his actual size"; "every other one stopped at his navel" |
  | 1767851007783140 (#19) | "His girlfriend laughed… called it results without doing anything" | The shirt "he could only wear with the bottom button undone. It buttoned."; woman at work asks; mirror; gets in photos; costs less than one gym payment |
  | 2467279207096631 (#24, 3:47 song) | Country-ballad story of a divorced 49-year-old whose ex-wife doesn't recognise him at his son's game | "You're not fat, you're just folded"; "Week one the polo quit pulling, week two I tucked it in" |
  | 1073742625723896 (#16) | "Believe it or not, that belly and those man boobs are under this shirt right now" | Invisible under a dress shirt or polo; 3 zones; "no bulge, no roll line" |
  | 1476557027711339 (#28) | "Stop! That compression tank you're about to buy is not the real V-Boost" | Anti-knockoff: "$10 on AliExpress, Amazon, Temu… one cheap tube… rolls up over your gut by lunch… ours is cut long past your waistband" |

- **Personas:**
  - Men about 40–55: married dads, a divorced 49-year-old, and a 250-lb 6'3" big guy.
  - Office or work settings (coworkers), and men who avoid the gym.
- **Life moments:** tucking the shirt in, a button that finally closes, the polo not pulling, the son's game, family photos, sex with the lights on, the gym, work.
- **Read on the ads:** Evolv already sells **shirt-fit moments** (tuck, button, polo, photos). It does so inside a body-shame and transformation frame, with fat-loss and gyno overclaims.

---

## 2. WHO BUYS (evidence)

Caveat: Reddit blocked both the scrape and the JSON fetch. The Reddit lines below are **search-engine excerpts** of the threads, not full reads. Trustpilot reviews were read in full.

### Evolv Trustpilot (read in full)
1. "I'm **6'2"** tall and the shirt rides up a good bit… I wish there was a **tall option**." [4★] https://www.trustpilot.com/reviews/6adac9127e246979b443065c
2. "Perfect fit and i appear a lot slimmer." [5★] https://www.trustpilot.com/reviews/6adca9eaeb3fda30d2ec16f0
3. "The large size was very small… I have a **38 waist and 46 chest**. The product seemed designed for a much smaller frame." https://www.trustpilot.com/reviews/6ad94faba52487838381d794
4. "All that marketing that says it holds all the right places is not true. I did purchase two with one free. What a waste." https://www.trustpilot.com/reviews/6ad613a29819fd49f50b4fc6
5. "They make me **sit up straighter** and feel very comfortable." https://www.trustpilot.com/reviews/6ad2e79fcf60a2e22543a870
6. "Has improved my posture." https://www.trustpilot.com/reviews/6ad1470f47d8d40fba3126e1
7. "Wish it would be a little **tighter around mid section**… the advertisement doesn't really equal the product." https://www.trustpilot.com/reviews/6acf8da981d9dcac4993e12e
8. "It is good but does **ride up** when wearing it." https://www.trustpilot.com/reviews/6ace7344f57c3ce2cd8b56d7
9. "The shirts **need to be longer**." [5★] https://www.trustpilot.com/reviews/6acd55b5db54e894f1214eae
10. "Ordered the 3 shirt deal and **two out of the three shirts were smaller** than the third… white and blue smaller than the grey." https://www.trustpilot.com/reviews/6acd278e63bcd03834bdb4f4
11. "Feels great… looks even better!" https://www.trustpilot.com/reviews/6acd083074c2f85206930283
12. "Keeps **rolling up** and not a comfortable fit. No results!" https://www.trustpilot.com/reviews/6ac92448040b32d417360f8f
13. "Sizing was correct, but the **length is way too short and rides up over my belly button**." https://www.trustpilot.com/reviews/6abbabf912b38c6818f98388
14. "Too short and ride up… **all day had to keep pulling it down**." https://www.trustpilot.com/reviews/6ab1375b535f95e93632b5c1
15. "I order by weight… **the shirt won't cover my stomach**." https://www.trustpilot.com/reviews/6aaaf5ef4d9a7ef825fa50a1
16. "I got **90% polyester and 10% elastane not 80% Nylon and 20% spandex**." https://www.trustpilot.com/reviews/6aa9653b2ebeaba98d2c5b62
17. "Three pack of white compression shirts solely because the advertisements on Facebook were so impressive… **super thin and hardly any compression**. I had originally bought two off Amazon that are pretty darn good." https://www.trustpilot.com/reviews/6a9f66c8dfd9df857d1b3d46
18. "Just some **mild compression** and the shirt is very short in length. My tummy [peeks] from the bottom." https://www.trustpilot.com/reviews/6a960751a1884c1d732c7543
19. "They promise incredible, life changing results in weeks but only guarantee it arrives and fits." https://www.trustpilot.com/reviews/6add49f2eb216b3e937ebc36
20. "Nothing more special about it than a spandex shirt. **The visual outlines on the front and back**…" (summary card) https://www.trustpilot.com/review/evolv-off.com
21. "Can't believe I paid £26 for this rubbish 90% polyester 10% elastic badly fitting vest." (summary card, same URL)
22. "I'm noticing quite a bit of abdominal definition as I wear the shirts more often." https://www.trustpilot.com/reviews/6acd5db536c487479e70eea7
23. WH gap clusters: "**Visible blue markings through white work shirts**", "**Visible V-neck under open-collar shirts**", "**Armholes too tight for larger customers**" (evolv-off.com store details).

### Reddit / forums / retail (search excerpts)
24. "First time i put it on under a shirt… my silhouette looked way smoother — fewer rolls, less jiggle, i stood up straighter… it made a fat difference." https://www.reddit.com/r/bigmenfashionadvice/comments/1ku3lsw/
25. "Compression shirts that work… compress. It doesn't just feel like a tight…"; "It will even out much of the larger bulges, but only subtly." https://www.reddit.com/r/bigmenfashionadvice/comments/1esugrx/
26. (Wife buying) "My husband prefers his jeans under his gut… I absolutely recognize this is a bandaid… help him lose weight." https://www.reddit.com/r/bigmenfashionadvice/comments/1ke7jwj/
27. "Hide my stomach and back fat that hangs over a little." https://www.reddit.com/r/bigmenfashionadvice/comments/1tkvb4w/
28. "Hold things together and make myself look less flabby"; "look up mens **gyno tank tops** on Amazon." https://www.reddit.com/r/bigmenfashionadvice/comments/j385yh/
29. "Shaperluv tanks… evens out my shape and I kind of low key like how it grips my belly." https://www.reddit.com/r/bigmenfashionadvice/comments/1gns9qj/
30. "BUT, **it rides up and im tired of it** lol"; "Tusq Apparel… built specifically for big and tall guys." https://www.reddit.com/r/bigmenfashionadvice/comments/1rihuv0/
31. "Had a Harbor Bay shirt… **rides up, no compression**"; "DXL sells a shirt that has compression just in the belly." https://www.reddit.com/r/bigmenfashionadvice/comments/1i8yz2d/
32. "I have a **62" chest** and order a 2XL, it's a bitch to get on but my chest is flat"; "Under Armour never offers enough compression." https://www.reddit.com/r/bigmenfashionadvice/comments/1ll1co4/
33. "My chest is about 53–54 inches." https://www.reddit.com/r/bigmenfashionadvice/comments/1lj1kjm/
34. (Gyno) "Compression tanks under my shirt. These were uncomfortable and **very hot in the summer**." https://www.reddit.com/r/AskMen/comments/1i0rvou/
35. "I'm on the overweight side (5'10 200 lbs close to 30ish% body fat)"; "undershirt or compression half shirt from underworks." https://www.reddit.com/r/malefashionadvice/comments/1g9f8bj/
36. "Under Armor compression shirt a size down under the garment." https://www.reddit.com/r/gynecomastia/comments/117ymj1/
37. "Crew neck from Underworks… **no lines** and super compression." https://www.reddit.com/r/gynecomastia/comments/11qrtai/
38. "They make you look good if you are lean enough, otherwise you look like a **stuffed sausage**." https://www.reddit.com/r/workout/comments/1vfwsgp/
39. "Compression shirts won't hide your excess fat. They may actually accentuate it." https://www.reddit.com/r/AskMen/comments/o6d2yc/
40. (Wedding) "Look into a compression shirt to wear underneath [the dress shirt]." https://www.reddit.com/r/weddings/comments/1mn4na3/
41. "Even when I went to the 'Big and tall' result for underarmor, there did not seem to be any **tall sizes**." https://www.reddit.com/r/tall/comments/1l6gdx/
42. "I bought a compression shirt from amazon and I actually really like having it under my shirts." https://forum.gynecomastia.org/gynecomastia-talk/1/minor-gyno-fit-guy-my-story-pics/33619
43. "Now 30 years old and still have gyno." (Underworks review) https://www.underworks.com/compression-body-shirt
44. "**Bought for my husband** and he loves them… not easy to get on, designed to be TIGHT." (Insta Slim 3-pack, 4.4★ on 1,408 ratings) https://www.amazon.com/dp/B00E0RVA6C
45. "A **66-year-old man's** review of compression shirts"; "Now at **41** years old, I see photos of myself and think 'wow'." https://www.facebook.com/groups/1939825456286012/posts/4440702926198240/
46. "I'm 6'1" and currently around 98 kg, 34 years old." (Kocles) https://www.facebook.com/Kocles/posts/1651687676960844/
47. "I am now 31 years old and put some of that weight back on." (Esteem gyno shirt) https://www.desertcart.in/products/657702180-esteem-apparel-original-men-s-chest-compression-shirt-to-hide-gynecomastia-moobs-shapewear
48. "My husband was tired of stiff dress shirts…" (Veroshape FB creator post) https://www.facebook.com/josievonloweryhaus/videos/1477181007846849/

### Synthesis
- **Who buys:**
  - Mostly overweight men, roughly 200–300+ lb with 46–62" chests.
  - Two age clusters show up: 30s (gyno, regain) and 40–66 (dad bod, photos, divorce). Evolv's ads skew 40–55.
  - Many are big **and tall** (6'1"–6'3").
  - **Wives buy for husbands** (Insta Slim review, Reddit wife, Veroshape FB).
  - A distinct gyno sub-segment exists, younger and often normal-weight.
- **Why (desire underneath):**
  - **They want to look "normal" in their clothes without anyone knowing they're wearing anything.**
  - They want the shirt to sit right: tuck it in, button it, the polo doesn't cling, no jiggle, no visible chest.
  - Under that sits avoiding judgment, mostly from a spouse, coworkers or photos.
  - Posture and "standing up straighter" is a frequent, unprompted positive.
  - Nobody in the organic evidence expects fat loss; Evolv's 5★ "abdominal definition" review is the exception.
- **Failure modes (stable across Evolv, North Alpine and Selure):**
  1. Too short / rides up / rolls (the #1 product complaint everywhere).
  2. Compression too weak.
  3. Sizing inconsistent, including by colour; weight-based sizing fails.
  4. Thin fabric, poly instead of nylon.
  5. Heat.
  6. Visible lines or neckline under work shirts.
  7. Tight armholes for big men.

---

## 3. OTHER SELLERS (Meta, live in window)

| Seller (page) | Live ads | Price | 30d revenue (WH est.) | Traffic trend | Angle |
|---|---|---|---|---|---|
| **North Alpine** "NorthPower" (north-alpine.com) | 1,180 | $29.90 (compare-at $60); T $39.90; V-neck $29.90; LS $49.99 | **$6.2M–10.3M** | Mar 9k → Jul 1.93M → Sep 1.10M | Evolv clone ("Feel the Power of Confidence, Shape & Control"); "Say goodbye to dad bod, love handles and man boobs"; "I used to avoid mirrors and fitted shirts… coworker asked if I'd been working out" |
| **Selure Wear** (selurewear.com), via "Prime Men's Journal" advertorial page | 171 | Shaping Tank 2.0 **$19.95**; SlimFlex $29.95; cotton fitted tank 3-pack $49 / 6-pack $75; stretch dress shirt $34.95 | **$1.8M–3.6M** | Jul 1.19M → Sep 416k | "Men over 35 are discovering this trick. It's not diet. It's not the gym. It's what they wear under their shirts." |
| **InShape** (in-shape.co) | **1,739** | $44.90; 3-pack $99.90; 5-pack $149.90 | **$25k–50k** | 9k visits, ~50% PH | **Already runs our "shirt-fit / menswear" angle:** "More men are wearing this under their polos… so the polo sits clean"; "What guys actually wear under the shirt on **date night**"; "**After 50**, it settles in the chest, gut and sides… for men who still care how their clothes fit"; LP `/pages/clothes-that-fit-better`; "Moobs are common. Surgery isn't the only answer" |
| Rounderbum USA (rounderbum.com) | 357 | $59 (cotton version $31–39) | not checked | not checked | "Look sharp, feel unstoppable… smooth, defined silhouette in seconds" |
| Alphacore (alphacore-store.com, FR-owned) | 321 | $24.95; 3-tank bundle | $3k–7k | 247 → 6.9k | **Big guys:** "Made by and for big guys… up to 5XL… doesn't ride up"; "Halloween deal for big guys" |
| Nebility (nebility.com) | 173 | B2G1 | not checked | not checked | "**Upgrade your base layer**… Wear it under a tee, a button-down, or alone. Breathable, invisible" |
| **Qore Logiq** (qorelogiq.com, AU) | 108 | Tank **Tall Length** $32.99; Regular $28.90; Tall 3-pack $94.05 | $24k–42k | 12k → 6.5k | **Tall:** "Being 6'3" and finding a compression tank that actually fits? Nearly impossible" |
| Temu (Shoptemu page) | n/a | n/a | n/a | n/a | "Men Round Neck Compression Tank Top" link-out ads |
| Stack Good Days | 13 | $27.95 | not checked | not checked | Gym compression, not shapewear |
| Primal Viking | 5,173 | n/a | n/a | n/a | "Man boobs melter" supplement, not a garment |

- **Searches with zero live ads:** "shapewear for men" and "body shaper men" (adtext).
- **"Gynecomastia" (adtext):** 288 ads, all Evolv. Only Evolv names the condition.
- **Seen in organic and search but not checked on Meta:** Shaperluv, Veroshape, WaistSculpt, Tusq, Esteem, Underworks, SculpMe, Insta Slim, Kocles, Core Armour and Maynox all sell the same garment.
- **Saturation verdict:** **crowded.** At least 4 heavy sellers (100+ ads) sell the same garment, and 3 of them are confirmed above $300k per 30 days.
- **Price is collapsing:** $60 → $29.90 → $19.95.
- **Category traffic is falling from a summer peak:**
  - Evolv −33% (Aug → Sep).
  - North Alpine −43% (Jul → Sep).
  - Selure −65% (Jul → Sep).
  - This could be seasonal or fatigue. **Unverified** which.

---

## 4. POSITIONING TEST

**Hypothesis:** not a body-fix. Instead "a better undershirt that makes every shirt fit better, invisibly": a menswear essential, sold on shirt-fit moments, as a 3-pack like True Classic.

### What the evidence says
1. **The desire supports it, as an outcome.**
   - What buyers praise and what Evolv's best videos dramatise are shirt-fit moments: tuck, button, polo, photos, "invisible under a dress shirt".
   - Organic buyers do not expect fat loss.
   - The "menswear essential, 3-pack" model is already proven at scale. Selure sells cotton fitted tank 3- and 6-packs plus a dress shirt; InShape sells 3- and 5-packs.
2. **The stronger pain sits one layer down, and it is what stops the scroll.**
   - The top Evolv ads open on belly, man boobs, wife, sex, divorce and 250 lb, then pay off with shirt moments.
   - The biggest sellers lead with body pain: North Alpine ("dad bod, love handles and man boobs"; "avoid mirrors and fitted shirts") and Evolv.
   - **The seller running the purest shirt-fit / menswear framing, InShape, has the most ads (1,739) but the lowest revenue estimate ($25–50k).**
   - This is weak evidence: WH revenue for a store with 50% PH traffic may be wrong. But it is the only direct test available, and it points against a pure "nice undershirt" pitch.
3. **The angle is not empty.** InShape (polo, date night, after 50, "clothes that fit better") and Nebility ("upgrade your base layer… under a tee, a button-down") already run it. It is not a gap.

### Verdict: MODIFY (do not run a pure menswear-essential pitch; do not run a body-fix overclaim)
- **Best version:** "**The shirt problem, not the body problem.**"
  - Hook on the visible pain in clothing: a shirt clinging at the chest, a button pulling, an untucked shirt, tugging the hem down, photos.
  - Resolve it with a demo (same shirt, with and without the tank, then a movement test).
  - Close on proof that it **stays down and reaches the belt**.
  - Make no fat-loss, gyno-reduction, "break down fat cells" or posture-medical claims.
  - Sell a 3-pack as "one on, one in the wash, one in the drawer".
- **Why this beats both extremes:** it keeps the pain intensity that drives the winners' hooks. It also keeps Meta compliance and stays deliverable: the product really does what the ad shows.

### Segments

| Segment | Status on Meta | Evidence of need | Verdict |
|---|---|---|---|
| **Big & Tall (6'0"+ / 2XL–6XL, "reaches your belt")** | Thin. Alphacore (big, ~$3–7k/30d) and Qore Logiq (tall, ~$24–42k/30d) are small. The big sellers size by weight only and are short in the body. Evolv *claims* "cut long past your waistband" in ads, but reviews contradict it. | Strongest. #1 complaint across Evolv (rides up 9, too short 7), North Alpine (too short 2 + 6, rides up 3) and Selure (short and rolls up 3 + 3); Trustpilot 6'2"; r/tall; Reddit 53–62" chests; "armholes too tight for larger customers". At least 5 independent sources. | **Top untargeted segment.** Weakness: the two sellers already in it are small, so niche size is **unverified**. |
| **White-shirt / work-shirt guys** (office, sales, church) | Partly covered: InShape (polo), Evolv (1 video "dress shirt or polo"). Nobody owns "invisible under a white dress shirt". | Evolv gaps: "visible blue markings through white work shirts", "visible V-neck under open collar"; Underworks "no lines"; MFA undershirt-colour norms. 3–4 sources. | Good **secondary angle and spec point** (nude/heather colourway, deep scoop neck, no contrast lines), not a standalone niche. |
| Wedding / event / formal | **No compression-tank ad found.** | Only 2 sources (r/weddings excerpt, WaistSculpt blog). | Seasonal and low-evidence. Usable as an ad hook only. **Unverified** as a segment. |
| Men 50+ | Covered: InShape "After 50", Selure "over 35", Evolv 49-year-old. | Yes (66-year-old FB group). | Not a gap. |
| Dads / dad bod | Covered heavily: Evolv, North Alpine, InShape. | Yes. | Not a gap. |
| Gyno-specific | Evolv owns the adtext (288 ads), and InShape runs "Moobs are common". | Yes (r/gynecomastia, r/AskMen, gyno forum, Underworks reviews). | Not a gap. Highest Meta risk. |
| Wives buying for husbands | No ad found speaking to the buyer-wife. | 3 sources (Amazon Insta Slim review, Reddit 1ke7jwj, Veroshape FB creator). | Interesting gift/"for your husband" angle (Black Friday, Christmas, Father's Day). Demand volume **unverified**. |

**Sharper niche, if any:** "**The tall/big compression tank that actually reaches your belt and stays there**". It combines the #1 complaint (a product fix) with the big-and-tall segment. The size of the niche is unproven. Treat it as a **positioning wedge inside the broad market**, not a separate small market.

### Meta policy notes (each angle)
- **Personal attributes:**
  - Do not assert or imply the viewer's body or condition. Examples to avoid: "Got man boobs?", "your beer belly", "your gynecomastia".
  - Evolv's "Got a beer belly, love handles or man boobs? 🤔" is a textbook violation risk, even though it is running.
  - Use third person or a story ("he", "this guy") or object-focused lines ("shirt clinging at the chest?").
- **Body image / negative self-perception:**
  - Avoid shirtless "before/after" body framing (Evolv's PDP gallery has "before-after… shirtless").
  - Show the same shirt with and without the tank, in clothes.
- **Weight-loss claims:** "promotes weight loss", "lost 30 lbs", "break down fat cells" and the fake study claims are restricted (18+ targeting) and are deceptive claims. **Do not use them.**
- **Health claims:** "reduces gynecomastia", "relieves back pain" and "improves circulation" are medical claims. Do not use them.
- **Shirt-fit angle:** lowest risk. **Gyno angle:** highest risk; avoid naming the condition in the primary text.
- **Big & tall:** "for big guys" is fine as a product description, as Alphacore shows. Avoid "you're fat".

---

## 5. PRODUCT SPEC (beats the incumbents' complaints) + SOURCING

### Spec
| Complaint (source) | Spec answer |
|---|---|
| Rides up / too short (Evolv 16, NA 11, Selure 6) | **Long body:** about 3" longer than standard so it sits below the belt line; a **Tall variant** with +2". **2–3 cm silicone-dot grip band** inside the hem. |
| Weak compression (Evolv about 19, NA about 20) | **Double-layer power-net front panel** (chest and belly), medium-firm on the sides, X-band back. **75–80% nylon / 20–25% spandex**, ≥220 gsm. No 90/10 polyester. |
| Inconsistent sizing (Evolv 17, NA 16) | Size chart by **chest and waist inches plus height**, not weight. Lot-checked across colours. Sizes **S–6XL** (NA and Evolv stop at 5XL; Reddit shows 62" chests). |
| Tight armholes for big men (Evolv) | Wider armhole cut and broader shoulder straps (Selure complaint: "narrow uncomfortable straps"). |
| Visible under white work shirts / open collar (Evolv) | **Nude/skin-tone and heather-grey colourways**, deep scoop neck, **no contrast print lines**, flatlock seams. |
| Hot in summer (Reddit gyno) | Breathable mesh side and back zones. Lower priority. |

### Supplier listings found (all **unverified** for silicone hem and tall length; no stock SKU with both was found)

| Listing | Price | Notes |
|---|---|---|
| Waistdear (Xiamen Heailun Garments), "Custom Logo Compression Tummy Control Men Seamless Body Shaper Tank" https://www.alibaba.com/product-detail/Waistdear-Custom-Logo-Compression-Tummy-Control_1601766513092.html | **US$5.05** | MOQ 2. Spandex/nylon, seamless, OEM accepted. Best candidate to request a custom long + silicone-hem sample. |
| Huizhou Youli Clothing, "Men's Breathable Compression Tummy Control Undershirt Slimming Body Shaper Sleeveless Tank" https://www.alibaba.com/product-detail/N-Men-s-Breathable-Compression-Tummy_1601712461416.html | US$4.69 | MOQ 1. Specs not retrieved (provider error). |
| Shijiazhuang Aofeite, "Seamless Gynecomastia Compression Shirts For Men, Tank Top Body Shaper" https://www.alibaba.com/product-detail/Popular-Seamless-Gynecomastia-Compression-Shirts-For_1601794769165.html | US$1.63–2.17 | MOQ 100. Spandex, S–3XL only, 6 colours including skin. "Accept Custom Styles". Too small in size range unless customised. |
| Shijiazhuang Aofeite, "Compression Slimming Mens Body Shaper Tank Top Shapewear" https://www.alibaba.com/product-detail/Compression-Slimming-Mens-Body-Shaper-Slimming_1601384383968.html | US$1.49–1.99 | MOQ 200. |
| Alibaba PLA "Men's Plus Size Seamless Compression Vest 3-Row Hook" https://www.alibaba.com/pla/Mens-Plus-Size-Seamless-Compression-Vest_1600931413487.html | US$4.08 | MOQ 2. Hook front, so a different style. |
| AliExpress YBFDO "Men Body Shaper Slimming Compression Vest Undershirt Seamless" https://www.aliexpress.com/item/1005006967285829.html | Unverified (Pinterest shows $4.10) | 4.9★ on 8,963 ratings. Dropship-ready. |
| AliExpress category "Compression Shirts for Fat Men" https://www.aliexpress.com/w/wholesale-compression-shirts-for-fat-men.html | not captured | Says "sizes up to 6XL… non-slip hem". The listing-level scrape timed out, so **unverified**. |
| AliExpress "Men Compression Shirts… Chest Abdomen Control… Tank" https://www.aliexpress.com/category/200003066/2-203533018%2525252525252C14-350853.html | US$12.09 | |
| Benchmark: Qore Logiq already sells a "Compression Shirt Tank Top \| Tall Length" | $32.99 | Proves a tall pattern is sourceable. |

- **Landed cost:**
  - Dropship single: about $5–12 unit + $9–11 shipping = **about $15–22**.
  - 3-pack parcel (about 450g): about $15–36 units + about $13–15 shipping = **about $30–50**.
  - A custom silicone-hem / tall run likely needs a 100–300 pc MOQ at about $4–7 per unit plus a 3PL. That is **unverified** and cash-intensive for a low-budget solo operator.

### Economics check (front-end)
- **Competitor ladder:** Evolv $60 single / B2G1 ($40/unit); North Alpine $29.90; Selure $19.95; InShape $44.90 or 3-pack $99.90; Qore tall 3-pack $94.05. WH AOV estimates: Evolv $40.79, NA $36.27, Selure $39.46, InShape $49.65.

| Offer | Price | Landed cost | CM | Margin |
|---|---|---|---|---|
| Single | $39.95 | $18 | about $20 | 50% (borderline) |
| Single | $49.95 | $18 | about $30 | 60% |
| 3-pack | $89–99 | about $40 | about $45–56 | about 50–57% |

- **Market AOV of about $36–50 means many orders land near the $20 CM floor.** Prior research's $49.95 single assumed higher prices than the market now pays.

---

## BIGGEST RISKS
1. **Saturation and price collapse.**
   - North Alpine ($6–10M, 1,180 ads, $29.90), Evolv, Selure ($19.95), InShape (1,739 ads), Temu and others already target the same US men on Meta.
   - Prior research's "single incumbent" premise is false.
   - Front-end CM is squeezed by $20–30 anchors.
2. **Category traffic is down 33–65% from a Jul/Aug peak** at all three big stores. It could be seasonal (summer?) or saturation; **unverified**.
3. **The spec edge is mostly invisible in an ad.** Evolv already *claims* "anti-slip grip" and "cut long past your waistband".
   - Our fix only wins if the sample really outperforms, and if the creative shows it (movement test, belt-line shot).
   - Requires sampling 3–4 suppliers, and probably a custom long + silicone-hem run, which is **unverified** at the low-budget scale.
4. **Meta:** body-pain hooks that convert (man boobs, belly, sex, wife) collide with the personal-attributes and body-image rules. The compliant version is weaker by default.
5. Info only (AI-creative note): the converting creatives are real-body try-ons and movement tests, which are hard to fake with AI.

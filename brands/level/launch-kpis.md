# IRYN: Ads Operating Guide. KPIs, kill / fix / scale, and when to launch the ABO campaign

$1,500 US test, October 2026. Main purchase campaign live since Oct 5 at $50/day.

Built on:
- Nikita's Step 5 playbook and his Kill or Scale tool. Same stairway (creative → page → cart → economics), same "fix before kill" rule.
- The live offer in `current-live-offer.md`.
- A landed cost of about AUD $10 per tin.

All money is in **AUD** unless marked. The store charges AUD. If the ad account is in USD, use the USD column (AUD × 0.66, approximate).

---

## 0. The 6 rules that matter most

1. **Find the first leak, fix only that.** Work top to bottom: ad → page → cart → checkout → economics. ROAS and CPA are outputs. You fix inputs.
2. **Fixable problems never get a kill.** Only kill an ad when the ad itself is the leak.
3. **One ad failing = kill the ad. Every ad failing at the same step = fix the store.** New ads can't fix a broken page.
4. **Don't judge early.** Under the minimum spend an ad has told you nothing.
5. **One change at a time.** Change five things and a better result teaches you nothing.
6. **Don't touch the main campaign for the first 4 days.** No edits, no new ads, no budget changes. Edits reset learning.

---

## 1. Your numbers (where every threshold comes from)

| | Revenue | Profit after the tin and payment fees |
|---|---|---|
| Subscribe, first order | $29.56 | $18.23 |
| Subscribe, each renewal | $35.96 | $24.40 |
| One-time (incl. ~$6 shipping charged) | $45.95 | $34.04 |

Assumptions: about 70% of buyers subscribe, and payment fees are about 3.5% + $0.30.

| Measure | AUD | USD (approx) |
|---|---|---|
| Break-even CPA, first order only | $23 | $15 |
| Break-even CPA if subscribers place 2 / 2.5 / 3 orders | $40 / $49 / $57 | $26 / $32 / $38 |
| **Target CPA** (pays back on the first renewal) | **$40** | **$26** |
| **Kill CPA** (3-day rolling, 3+ purchases) | **over $55** | **over $36** |
| Break-even ROAS on the first order (blended AOV ≈ $34) | about 1.5x | |

You will lose money on most first orders. That is how a subscription offer works. The money is in the renewals, so judge on the target CPA, not first-order ROAS. Refunds (70-day promise) and early cancels are not in these numbers yet. Re-check on day 14.

### Spend gates (how long before you're allowed to judge)

| Gate | AUD | USD | What you can judge |
|---|---|---|---|
| Too early | under $20 or under 1,000 impressions | under $13 | Nothing. Leave it. |
| Gate 1 (1x target) | $40 | $26 | Creative metrics, and whether it got an add to cart |
| Gate 2 (2x target) | $80 | $53 | Whether it gets checkouts and purchases |
| Gate 3, hard stop (3x target) | $120 | $79 | No ad keeps spending past this without a purchase |

---

## 2. Set up Ads Manager once (5 minutes)

Make a saved column preset called **"IRYN daily"**:
- Amount spent, Impressions, CPM, Frequency
- 3-second video plays, ThruPlays (to work out hook and hold rate)
- Link clicks, CTR (link click-through rate), CPC (cost per link click)
- Landing page views
- Adds to cart, Checkouts initiated, Purchases
- Cost per add to cart, Cost per purchase, Purchase conversion value, Purchase ROAS

Attribution setting: 7-day click, 1-day view (the default). Always read the same date ranges: **"Last 3 days"** for decisions and **"Lifetime"** for spend gates.

**Shopify:** Analytics → Reports → Conversion funnel (sessions → added to cart → reached checkout → purchased). Use Shopify for the page and cart rates. Use Meta for the per-ad numbers.

Hook rate = 3-second plays ÷ impressions. Hold rate = ThruPlays ÷ 3-second plays.

---

## 3. The daily 10-minute check (same time every day)

1. **Emergencies first.** Any of these means stop and fix today:
   - an ad rejected or the account restricted;
   - spend stuck at $0;
   - Shopify shows orders but Meta shows 0 purchases (the pixel or CAPI is broken).
2. **Spend pacing.** Is each campaign spending roughly its budget?
3. **Per ad:** run the Ad Scorecard (section 4) on every ad past Gate 1.
4. **Store funnel:** run the Store Scorecard (section 5) once there are 300+ sessions.
5. **Write it down.** One line per day in a log: date, spend, purchases, CPA, what you changed. Never change something without logging it.

**Days 1 to 4:** look only. The only actions allowed are emergencies and a page or cart fix from the Store Scorecard. A page fix doesn't touch the campaign, so it doesn't reset learning.

---

## 4. Ad Scorecard: kill, fix or keep each ad

Read top to bottom. Stop at the first red. That is the only thing you act on.

| Step | Metric | Judge at | Good | Watch | Act |
|---|---|---|---|---|---|
| 1 Stop | Hook rate (video) | 1,000 impr. | 30%+ | 20 to 30% | under 20% |
| 2 Hold | Hold rate (video) | 1,000 impr. | 25%+ | 15 to 25% | under 15% |
| 3 Click | Link CTR | Gate 1 | 1.5%+ (2%+ great) | 1.0 to 1.5% | under 1.0% |
| 4 Click cost | CPC (link) | Gate 1 | under $2.30 (US$1.50) | $2.30 to $3.50 | over $3.50 |
| 5 Cart | Adds to cart | Gate 1 ($40) | 1+ | | 0 |
| 6 Buy | Purchases | Gate 2 ($80) | 1+ | 0 but has adds to cart: allow to Gate 3 | 0 adds to cart and 0 purchases |
| 7 Profit | CPA, 3-day, 3+ purchases | 3 purchases | $40 or less | $40 to $55 | over $55 |

### What to do at each red

| Red at | What it means | Action |
|---|---|---|
| Hook rate | Nobody stops | Keep the body, recut only the first 3 seconds (new opening line or visual). Turn the old one off when the recut goes live in the ABO campaign. |
| Hold rate | They stop, then leave | The middle is slow, or the hook promised something the video doesn't pay off. Recut the middle. |
| CTR / CPC | They watch but don't click | The ad doesn't make them want the answer, or the CTA is weak. New angle or stronger CTA. If 3+ hooks on the same angle all fail CTR, **kill the angle**, not just the ad. |
| 0 adds to cart at $40 | Clicks, but the page doesn't continue the ad | Check whether other ads get adds to cart. **If yes → kill this ad** (its promise and the page don't match). **If no ad gets adds to cart → page problem, go to section 5.** |
| No purchase by $80 / $120 | Carts but no buys | If other ads buy, kill this one at $120. If none buy, it's the cart or checkout, so go to section 5. |
| CPA over $55 | It sells, but too expensively | Kill it once it has 3+ purchases and stays over $55 for 3 days. |

### Patterns to know

- **High CTR + low sales** = page or offer problem, not the ad.
- **Frequency over 2.5 on cold traffic + CTR falling** = the ad is tired. Make new versions of it.
- **High CPM** (over about $60 / US$40) = the audience is too narrow, or Meta rates the creative as weak.
- **An ad gets almost no spend** (under 10% of its ad set): Meta has already decided it's weaker. You can't judge its CPA. If you still believe in it, retest it in the ABO campaign, where it gets forced spend.
- **"Learning limited"** is normal at this budget (Meta wants about 50 purchases a week). Ignore it. Don't restructure because of it.

---

## 5. Store Scorecard: when to fix the page, cart or checkout

Judge this across **all ads combined**, once the store has 300+ sessions from ads (or 20+ adds to cart for the cart rows).

| Step | Metric (source) | Good | Watch | Fix |
|---|---|---|---|---|
| A Load | Landing page views ÷ link clicks (Meta) | 80%+ | 70 to 80% | under 70% |
| B Page | Add-to-cart rate = adds to cart ÷ sessions (Shopify) | 10%+ | 6 to 10% | under 6% |
| C Cart | Reached checkout ÷ adds to cart (Shopify) | 60%+ | 45 to 60% | under 45% |
| D Checkout | Purchases ÷ checkouts started (Shopify) | 50%+ | 35 to 50% | under 35% |
| E Overall | Purchases ÷ adds to cart | 25%+ | 20 to 25% | under 20% |

If ads land on the advertorial first, add a step before B: clicks from advertorial to product page ÷ advertorial sessions. Fix the advertorial if under 20%.

### The fix list for each red (one fix at a time)

**A. Load (under 70%).** The page is slow or broken on mobile.
- Test it on your own phone on mobile data. Compress the hero images and video.
- Cut extra apps and scripts.
- Check every ad's link opens the right page.

**B. Page (add to cart under 6%).** The interest dies on the page.
1. **Message match first.** Does the top of the page continue the ad's exact words and angle? Each angle needs its own hero. See `homepage-architecture.md`.
2. **Price shock.** The AUD prices: does a US buyer understand "$29 AUD today"? Watch for this.
3. **Buy box clarity.** Subscribe pre-selected, the $1.20/day, the 3 gifts with their values, the 70-day promise under the button.
4. **Proof above the fold.** The real review count or a real expert line.
5. **Answer the top objection** (will she actually take it, is it safe) near the buy box.

**C. Cart (under 45%).** Something in the cart scares them.
- Remove the "You may also like" row that shows the $0 gift products (Theme editor → Cart template → remove the section).
- Check nothing surprising appears: a price change, a shipping cost, a currency switch.
- The cart must show the same price as the product page.

**D. Checkout (under 35%).** Friction or a surprise at payment.
- Do a real test purchase yourself, on mobile.
- Is the one-time shipping (~$6) a surprise? It must show on the product page before checkout.
- Is AUD a surprise at payment? Are Shop Pay, Apple Pay and PayPal on?
- Is the subscription renewal ($36 a month) stated plainly?

After any fix, re-read after about $100 more spend or 2 days. Don't stack a second fix on top before you know if the first one worked.

---

## 6. Campaign structure and when to launch the ABO campaign

### The two campaigns

| | Main campaign (live) | ABO test campaign (new) |
|---|---|---|
| Job | Sell with proven ads | Give new ads a fair, forced test |
| Budget | $50/day, set at campaign or ad-set level as it is now | $20 to $25/day **per ad set** (ad set budget = ABO) |
| What goes in | Batch 1 now. Later, only ads that passed the ABO test | Every new ad: batch 2, statics, recut hooks, winner variations |
| Edits | Hands off days 1 to 4. After that: kill losers, add graduates, raise budget slowly | Kill and add freely. It exists to be messy |

### When to launch the ABO campaign (any ONE of these triggers)

1. **Day 5 (scheduled).** The main campaign has had 4 clean days. Launch batch 2 and the statics.
2. **Day 3, early trigger.** Every ad in main is red on CTR at Gate 1. That's a creative problem, so get fresh hooks testing now. Leave main running.
3. **A winner shows up.** An ad hits CPA $40 or less with 3+ purchases. Test 3 or 4 variations of it in ABO: same body, new hooks.

**Do NOT launch the ABO campaign while the Store Scorecard is red at B, C or D.** New ads will hit the same wall. Fix the store first.

### How to build the ABO campaign (step by step)

1. New campaign → objective **Sales** → **turn Advantage campaign budget OFF** (that's what makes it ABO).
2. Name it `IRYN | TEST | ABO | [date]`.
3. Ad set settings:
   - Conversion location: Website. Pixel event: **Purchase**.
   - Budget: $20 to $25/day.
   - Audience: broad US women 35 to 55 (the same audience as main).
   - Placements: Advantage+.
   - Exclusions (Rule 0): past buyers, you and your team.
4. **One angle per ad set**, so you learn which angle wins. Example:
   - Ad set 1: the best-CTR angle from main.
   - Ad set 2: the statics.
5. **3 to 5 ads per ad set.** Name each ad `concept | angle | format | hook#`.
6. Every ad links to the page whose hero matches its angle.
7. Use the same pixel, UTMs and offer as main.
8. Let each ad set spend at least $80 (Gate 2) before judging the ad set as a whole.

### Moving a winner from ABO into the main campaign ("graduating")

- **Graduate an ad** when it reaches CPA $40 or less with 3+ purchases over 3 days.
- **How:** add it to the main campaign with **"Use existing post"** (its post ID). That way its likes and comments come with it.
- Keep the ABO copy running for 2 to 3 days, until the main copy is spending and holding its CPA. Then turn the ABO copy off.
- This is the one edit to main that's allowed after day 4. It causes a small learning reset, and that's fine.

---

## 7. Scaling rules

- **Scale the main campaign** when its 3-day blended CPA is $40 or less and it has at least one graduated winner.
- **How:** raise the budget 20 to 30% every 48 to 72 hours, while the CPA holds. **Never double overnight.**
- **Stop raising** if the 3-day CPA goes over $48 (target + 20%). Hold the budget for 3 days. If it comes back, keep scaling. If it reaches $55, go back to the last budget that worked.
- **Scale out (more creative), not just up:** every winner goes back to Step 4 for 3 or 4 new hooks, which you test in ABO.
- **Fatigue signs on a winner:** frequency over 2.5, CTR down 30% from its own first week, CPA rising 3 days in a row. Swap in a graduated variation. Don't just raise the budget.

---

## 8. The 14-day calendar

| Day | Main ($50/day) | ABO | What you do |
|---|---|---|---|
| 1 to 2 | Learning | | Daily check. Emergencies only. |
| 3 | Learning | Early trigger? | If every ad is red on CTR → launch the ABO campaign with fresh hooks. Store Scorecard if 300+ sessions. |
| 4 | First full read | | Run the Ad Scorecard. Kill the red ads that are past their gate. Fix the store if it's red. |
| 5 | Running | **Launch**: 2 ad sets at $20 to $25 | Batch 2 + statics on the best-CTR angle. |
| 6 to 7 | Running | Learning | Daily check. Store fixes only. |
| 8 | Graduate winners in | Kill losers at Gate 2/3 | Winner (3+ purchases, CPA $40 or less) → main via post ID. |
| 9 to 11 | Scale +20% if CPA holds | Test 3 to 4 variations of the winner | Brief the winner variations (Step 4). |
| 12 to 13 | Scale +20% if CPA holds | Graduate or kill | |
| 14 | **Product decision** (section 9) | | Pull the full numbers into the log. |

Total spend is about US$100/day from day 5, which keeps the test inside $1,500. Hold about $300 back for scaling a winner.

---

## 9. Day 14: the product decision

| Result after the full test | Decision |
|---|---|
| Blended CPA $40 or less over the last 7 days, with 20+ purchases | **Scale.** Raise the budget past the test, keep feeding new creative. |
| Blended CPA $40 to $55, store funnel healthy | **Iterate.** Run more angles and fix the offer before more spend. For example, build a bigger first order, such as a multi-tin option. |
| Blended CPA over $55 and the store funnel is healthy | **Don't scale.** People want it, but the economics fail at this price. Rework the offer or the product before spending more. |
| Store funnel red the whole time | **Not a product verdict.** The test was blocked by the page or cart. Fix it, then rerun a smaller test. |
| Every angle red on CTR after 3+ hooks each | **The angle or product has no pull in the feed.** Rethink the angles from `research.md` before any more spend. |

Also check on day 14:
- How many first-month subscribers have cancelled? If more than 30% cancel before the first renewal, the target CPA is too high. Re-run section 1 with the real numbers.
- Refund requests.

---

## 10. Never do this

- Don't run "warm-up" engagement or page-like campaigns. They train Meta toward people who engage, not people who buy.
- Don't edit the main campaign in days 1 to 4.
- Don't kill an ad before its spend gate.
- Don't kill good ads to fix a store problem.
- Don't change more than one thing at once.
- Don't double a budget overnight.
- Don't use fake timers, fake stock or invented reviews. Use real urgency and real proof only. Fake versions are what get ad accounts and Shopify Payments frozen.
- Don't let any ad spend past $120 (Gate 3) without a purchase.

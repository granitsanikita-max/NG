# Landing page — paste list v4.1 (words only, top to bottom)

Full reasoning, HTML blocks and launch flags: `LANDING_PAGE_COPY_SHORT.md`. This file is just the words.

Native buttons (hero, mobile hero): set the action to go to the **Quiz** step, not a typed URL.
The 4 Custom HTML blocks in `blocks/landing/` already link to the quiz by path, so they work on any domain:
L0 top bar (very top) · L1 strip (under the cards) · L2 footer (bottom) · L3 sticky bar (anywhere).

---

## HERO (desktop)

**Top bar** (thin plum strip, if the template has one)
`30-Night Leak-Test · Money back if they don't hold`
(AU-only ads later: `Free shipping · 30 nights, money back if they don't hold`)

**"Buy Product" button** — delete. (If it won't delete: `Find my match` → quiz.)

**Eyebrow tag (timer icon)**
`LEAK-RESISTANT UNDERWEAR · 2-MIN QUIZ`
(If it wraps: `2-MIN UNDERWEAR QUIZ`)

**H1** (line 1 italic, no quote marks)
```
Stop! I'll pee myself!
Common? Yes. Normal? No.
Find your match.
```

**Subhead**
```
Black cotton briefs for women who'd rather laugh than cross their legs. The quiz works out your size and how many pairs you need. Then 30 nights to see if they hold.
```

**Bullets**
- (icon-check) `Looks like regular black underwear`
- (icon-loop) `No pad to bunch. Nothing to throw away.`
- (icon-swap) `Wrong size? One free size swap.`

**Button** — `Find my match`

**Under the button**
`About 2 minutes · No email needed to see your match · 30-Night Leak-Test`

**Proof row** (replace "Loved by 1.2k" — no avatars, no stars)
`New brand, no reviews yet. We won't fake any.`
(Fallback: `We're new. Straight answers, no fake reviews.`)

---

## 3 CARDS (no photo, no name, no stars)

**Card 1**
- Label: `STRAIGHT ANSWER · 1 of 3`
- Headline: `Isn't this for older women?`
- Body: `Ever watched from the side at the trampoline park? About 1 in 3 women leak after having a baby.¹ Plumbing, not a verdict. So, not just older women. It's for women who aren't done jumping.`
- Small line: `From the Leapproof team. Not a customer review. ¹From research, not our customers. Source at the bottom.`

**Card 2**
- Label: `STRAIGHT ANSWER · 2 of 3`
- Headline: `Why trust a brand you've never heard of?`
- Body: `Fair question. You shouldn't, yet. So we don't ask you to. No sale that ends at midnight. No fake doctors. On your own sneeze, laugh or run, you see if they hold.`
- Small line: `From the Leapproof team. Not a customer review.`

**Card 3**
- Label: `STRAIGHT ANSWER · 3 of 3`
- Headline: `What if they leak anyway?`
- Body: `The cost is on us. The quiz checks your size first. A big sneeze in the cereal aisle is the test. Wear them through your moment for 30 nights. If they don't hold, you get your money back. You keep the pairs. Nothing to send back.`
- Small line: `From the Leapproof team. Not a customer review. · Full terms at the bottom`

Card colours: Card 1 plum bg / cream text / label Rose #E7879F / small line Blush #E7CFC9. Cards 2–3 cream or blush bg / plum text / label Deep Claret #872845 / small line Plum.

---

## STRIP (under the cards)

**H2** (first sentence italic)
`Leaking is just normal now. Says who?`

**Quote**
`Leaking is "NEVER considered normal."`

**Source line (small)**
`Ridgeview Medical Center², a US hospital · not connected to Leapproof`

**Body**
`So nobody has to just live with it. A doctor or pelvic-floor therapist can help with the cause. Underwear is for the moment.`

**Label** — `FIND YOUR LEAK MATCH`

**H3** — `About 2 minutes to find. 30 nights to test.`

**Steps**
1. `Tell us when it happens.`
2. `See your size and how many pairs.`
3. `Wear them through your moment for 30 nights. If they don't hold, you get your money back.`

**Small line under steps**
`If we don't carry your size, or it's more than a little leak, we'll tell you.`

**Button** — `Find my match`
**Under it** — `About 2 minutes · No email needed to see your match · 30-Night Leak-Test`

---

## MOBILE HERO (image block, phone only)

- Chip (top right, plum): `LEAK-RESISTANT UNDERWEAR`
- Caption 1 (plum label, cream italic): `Stop! I'll pee myself!`
- Caption 2 (plum label, cream): `Common? Yes. Normal? No.`
- Button (bottom): `Find my match`
- Directly under the image: `About 2 minutes · No email needed to see your match · 30-Night Leak-Test`
- Nothing over either woman's face, hand or body.

**Sticky bar** — label `About 2 minutes` · button `Find my match`

---

## FOOTER

`Not a treatment. It's underwear. For heavier leaks, these aren't enough on their own.`

`The quiz isn't a medical assessment. It matches you to underwear. If leaking is new, painful or getting worse, talk to a doctor or a pelvic-floor therapist.`

`Sizes S to 2XL. They run small, so don't go by the letter on your other underwear. The quiz checks your size against the chart for this exact pair. If we don't carry your size, it tells you before you pay.`

`Fabric: [copy from the sewn-in label]. Imported.`

`The Straight Answer cards near the top are notes from the Leapproof team, not customer reviews.`
`The image at the top is AI-generated. It doesn't show real customers.`

**The 30-Night Leak-Test** (anchor `#leak-test`)
`Wear them through your moment for 30 nights. If they don't hold, you get your money back. You keep the pairs. Nothing to send back.`

**The Fit Promise**
`Wrong size? We'll send the right one first. No need to send the other back.`

**The terms, in plain words**
- `Your 30 nights start the day your set arrives (the delivered date on your tracking). Wear them day or night, through your real moments.`
- `If they don't hold, email [support email] with your order number and what happened.`
- `You can claim any time during your 30 nights, or up to 14 days after your 30th night.` ← PENDING your OK. If no: `You can claim any time during your 30 nights.`
- `We refund the full amount you paid for your set and any extra pairs you added, to your original payment method. A claim costs you nothing.`
- `One claim per customer.`
- `The Fit Promise covers one free size swap per order.`
- `Shipping: AU — free shipping on every set. US — any shipping cost shows at checkout, before you pay.`
- `The 30-Night Leak-Test and the Fit Promise are in addition to your other rights and remedies under the law.`

**Your rights**
- AU: `Our goods come with guarantees that cannot be excluded under the Australian Consumer Law. You are entitled to a replacement or refund for a major failure and compensation for any other reasonably foreseeable loss or damage. You are also entitled to have the goods repaired or replaced if the goods fail to be of acceptable quality and the failure does not amount to a major failure.`
- US: `The 30-Night Leak-Test is a limited warranty. It gives you specific legal rights, and you may also have other rights which vary from state to state. Nothing on this page limits your rights under federal or state law.`

`[Registered business name] · ABN [ ] · [business address] · [phone] · [support email]`

**Button** — `Find my match` · under it: `About 2 minutes · No email needed to see your match`

**Sources**
- `¹ A review of studies of leaking between 6 weeks and 1 year after giving birth. Moossdorff-Steinhauser et al., International Urogynecology Journal, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8295150/ (accessed 11 Oct 2026). Research results, not Leapproof customers.`
- `² Ridgeview Medical Center, "Coughing, laughing or sneezing shouldn't cause peeing", https://www.ridgeviewmedical.org/health-eviews/coughing-laughing-or-sneezing-shouldnt-cause-peeing/ (accessed 11 Oct 2026). The words "NEVER considered normal." are copied from this page.`

`Words in quote marks next to a named source are copied exactly from that source. Leapproof isn't connected to, or endorsed by, any source named on this page.`

`Privacy · Terms · Contact` · `© 2026 leapproof`

---

## PAGE SETTINGS

- Title: `Find Your Match | leapproof`
- Meta / share description: `Black cotton briefs for the sneeze, the laugh and the jump. A 2-minute quiz finds your size and how many pairs you need. 30 nights to see if they hold.`
- Hero image alt text: `Two women laughing on a sunny footpath, holding takeaway coffees`
- Slug: `/match` · no popup, no exit-intent, no countdown

# Leapproof Landing Page — SHORT (v4.1, final)

*Point sentence: a cold ad brings an active woman who leaks a little when she laughs, sneezes or jumps. She leaves believing four things. It's common, but not normal. It's not her fault. A quick match finds her size and how many pairs she needs. If they don't hold, she gets her money back. Then she taps. Every button and link goes to https://leepproof.myfunnelish.com/quiz-2891028289-1791612140998314 (NUMBER_SHEET §12b; flag 6 covers the domain spelling). The page has 6 blocks. Gifts, prices, set sizes, outcome scenes and specs wait for the quiz and the product page.*

## 1. Top bar (AU line + US line)

**Default, shown to every visitor in both markets:** 30-Night Leak-Test · Money back if they don't hold (50)
**AU only, shown when the URL has `mk=au`:** Free shipping · 30 nights, money back if they don't hold (56)

Build it as a thin Plum Ink #231017 strip with Warm Cream text in 13px Hanken Grotesk. It sits above everything and doesn't stay fixed on scroll. The whole strip is one link to `#leak-test` in the footer. That block ends in a quiz button, so the strip is never a dead end.

Measured at 13px on a 375px phone, with 343px free: the default line is 292px wide and the AU line is 320px (319px in the Arial-metric fallback). Both fit on one line. The AU line also fits at 360px, where 328px is free.

Paste-ready (Block A, a Custom HTML element at the very top of the page). It swaps its own line, so it doesn't depend on Block B:
```html
<!-- Leapproof landing v4.1 FINAL · Block A · top bar (self-contained: swaps its own line on mk=au) -->
<style>.lptb{background:#231017;text-align:center;padding:8px 16px;font-family:'Hanken Grotesk',Arial,sans-serif;font-size:13px;line-height:1.35}.lptb a{color:#F5EDE6;text-decoration:none}</style>
<div class="lptb"><a href="#leak-test"><span id="lp-tb-all">30-Night Leak-Test &middot; Money back if they don&rsquo;t hold</span><span id="lp-tb-au" style="display:none">Free shipping &middot; 30 nights, money back if they don&rsquo;t hold</span></a></div>
<script>(function(){try{if((new URLSearchParams(location.search).get('mk')||'').toLowerCase()!=='au')return;var d=document.getElementById('lp-tb-all'),u=document.getElementById('lp-tb-au');if(d&&u){d.style.display='none';u.style.display='inline';}}catch(e){}})();</script>
```
Add `&mk=au` to the URL of every AU ad set. Until US free shipping is confirmed in NUMBER_SHEET §5, every other visitor sees the default line, which makes no shipping claim. If the script doesn't run, the default shows.

*Why: screen 1 says in plain words what happens if they fail (Kill 8, Universal F5/F8). The condition "if they don't hold" sits right beside "money back". Both lines carry the 30-night limit: the default through the Leak-Test name, the AU line in plain words. So neither can read as an open-ended promise or a no-strings free trial (FTC 239 "clear and conspicuous", ACL s29(1)(m)). Free shipping appears only where it is true (Universal C10). Kills O8 and O1. Names B3.*

## 2. Hero — native template slots

- **Hero image alt text** (the locked photo; this is not a new image): Two women laughing on a sunny footpath, holding takeaway coffees
  *Why: screen readers and broken-image fallback. It describes the photo as fact. It has no "leak" or "pee", so nothing about her condition is read aloud or indexed (O14).*

- **Logo (note only):** lowercase wordmark. "leap" is upright Fraunces in Plum Ink and "*proof*" is italic Claret. Not linked. Hidden on mobile, where the image block carries a light version.
  *Why: same brand to the edges (Universal F19), and one less exit (F18, Kill 9).*

- **Nav button: delete (note).** Remove "Buy Product" completely. If the slot can't be removed, set it to **Find my match**, point it at the quiz URL and hide it on mobile.
  *Why: one job and one door, with no buy door and no side exit (Universal F1/F18, Kill 9, Quiz "many doors, one intake").*

- **Eyebrow tag (timer icon), desktop:** LEAK-RESISTANT UNDERWEAR · 2-MIN QUIZ (37)
  It measures 241px at 12px and 321px at 14px with wide tracking (Hanken Grotesk 600), so it should sit on one line in the desktop right column. Check it in the editor. **Fallback if it still wraps:** 2-MIN UNDERWEAR QUIZ (20)
  **Mobile chip (no timer icon):** LEAK-RESISTANT UNDERWEAR (24)
  *Why: it says what the product is, tells her a quiz comes next, and puts the sheet's real time next to the timer icon instead of "quick" (Kill 8, Quiz R2/R3, 00 T20). "QUIZ" sits right after the time, so it can't read as "leak-resistant for 2 minutes". No "you" and no named source (Meta test, FUNNEL_PLAN §8.1). Kills O13.*

- **H1** (3 lines. Line 1 is Fraunces italic because it's her own line: italics, no quote marks. Lines 2–3 are upright. All Plum Ink, so the button stays the only claret on screen.)
  ***Stop! I'll pee myself!***
  **Common? Yes. Normal? No.**
  **Find your match.**
  (64 characters including the spaces between lines)
  *Why: line 1 says out loud what the locked photo shows (laughing hard, hand up, knees together) in her own verb (#14, #17, #119 "pee myself"). The photo and the words make one joke she's in on, not a shame cue (F2 slippery slide, "open on the moment", T13 communicates > says). Line 2 flips the belief with her tribe's own words (#125, #134). Card 1 proves "Common" and the Ridgeview quote in §4 proves "Normal? No." Line 3 hands off to the button. It's first person, so it passes the Meta "you" test. Kills O12 and O14. Installs B1.*

- **Subhead:**
  Black cotton briefs for women who'd rather laugh than cross their legs. The quiz works out your size and how many pairs you need. Then 30 nights to see if they hold.
  (165 characters)
  *Why: it gives her identity as a third-person choice (capable, joyful, not shrinking), using the exact habit in the photo and her own words ("crossing their legs every time they cough or laugh", #90). It replaces "brace", which means something good to a lifter. "How many pairs" replaces "set", which reads as lingerie. "See if they hold" sets up the guarantee's real condition, not a free trial (FTC 239). No "you" about her condition (Meta test). Kills O11, O13 and O1. Installs B4. Names B3.*

- **Trust bullet 1** (icon: check): Looks like regular black underwear (34)
  [Fallback, if the sample doesn't look everyday laid flat and worn: **Black cotton brief, lace on the hips** (36)]
  *Why: it links the product to something she already owns, in her words (#103, #106 "regular underwear"). "Not a diaper, not a patient" lands without planting the word (Sugarman linking). Kills O10 and O11. Installs B4.*

- **Trust bullet 2** (icon: loop): No pad to bunch. Nothing to throw away. (39)
  *Why: the locked enemy sentence, compressed as "X without the Y" (PDP Zone 7, F13), in words that work in both markets. It's the page's only enemy line. Held behind the wear test (flag 1). Kills O6. Plants B2.*

- **Trust bullet 3** (icon: swap): Wrong size? One free size swap. (31). Link it to `#leak-test` if the template allows links.
  [If Nikita picks one-pair swaps in flag 3: **Wrong size? One pair swapped free.** (34)]
  *Why: it answers sizing on screen 1 as the question she's really asking (#65 "xl more like a small"). It uses the sheet's own term ("one free size swap per order"), which is true under either Fit Promise option (Kill 13). Kills O17.*

- **CTA button text:** Find my match (13) → quiz URL. Claret #A33154, full width on mobile, at least 48px tall.
  *Why: it names what she gets, not homework (Quiz F1). It repeats H1 line 3 and hands off to the quiz's "Start my match". "Leak" stays off the button text that Meta's automatic events read. Kills O13.*

- **Micro-copy under CTA:** About 2 minutes · No email needed to see your match · [30-Night Leak-Test](#leak-test)
  *Why: the locked under-button line answers the three fears that peak at the button (time, spam, "what if it fails"), with the terms one tap away (Universal F8, PDP F7). Kills O13 and O8.*

- **Proof row line** (small "lp" monogram. No avatars, no stars. Delete the old widget completely; don't leave it rendering empty):
  - **Primary (PENDING Nikita's OK):** New brand, no reviews yet. We won't fake any. (45)
  - **Fallback (doesn't say "no reviews"):** We're new. Straight answers, no fake reviews. (45)
  *Why: it names the biggest flaw before she spots it and turns it into trust (Sugarman #1/#8, Universal F15). "Straight answers" labels the STRAIGHT ANSWER cards right below. "No fake reviews" limits the honesty claim to reviews, so a sceptic can't catch it out (Kill 6, Kill 11). Kills O8. Installs B3.*

## 3. Carousel — 3 cards (label · headline · body · small attribution line · the entry objection it kills · Founding-30 casting brief for the real review that replaces it in week 2)

**Build:**
- Delete every photo box, name, "Rate 4.9" and star. Turn autoplay off.
- Stack the cards on mobile. Show them 3 across on desktop if the block allows (Kill 13). If it has to slide: arrows on, the next card's edge peeking in, start on Card 1.
- Set equal-height slides on desktop, or a min-height that fits Card 3. Card 3 is the longest (229 characters, against 187 and 162). On mobile the cards are stacked, so height doesn't matter there.
- Type only. Headline in Fraunces, body in Hanken Grotesk at 16px or larger.
- **Card 1:** Plum Ink background, Warm Cream type. Label in Rose #E7879F, attribution in Blush #E7CFC9, at least 13px.
- **Card 2:** Warm Cream background, Plum Ink type. **Card 3:** Blush #E7CFC9 background, Plum Ink type. On both, the label is Deep Claret #872845 and the attribution is Plum Ink, at least 13px.
- No Rose Taupe on any card. No seal or badge (it would read as a certification).

**Founding-30 rules for all three replacements (FUNNEL_PLAN §8.2):**
- A free set for an honest review at any rating. Ask only the 6 open questions, and never show a reviewer an example line.
- Publish every review, including 2–3★. Feature only her unedited words.
- First name and last initial.
- The consent form says in plain words that her words about leaking will be published with her first name, last initial and (only if she ticks it) her photo, on the website and in ads, and that she can withdraw at any time. Offer a no-photo option.
- Label every card "Received a free set to test", plus "Friend of the founder" or "Paid partner" where true.
- Stars only if she gave a rating. Never "Verified buyer".
- Tag every card "Wearing: Leapproof Brief, size [X]".
- Never feature "never leaked", "100%" or "zero leaks", a brand name, or a knock on period underwear.
- When a real review goes in, the label changes from STRAIGHT ANSWER to FOUNDING TESTER, and the proof row shows the real, un-rounded count (NUMBER_SHEET §10).

### Card 1: identity mirror (the trampoline she watches)
- **Label:** STRAIGHT ANSWER · 1 of 3
- **Headline:** Isn't this for older women?
- **Body:** Ever watched from the side at the trampoline park? About 1 in 3 women leak after having a baby.¹ Plumbing, not a verdict. So, not just older women. It's for women who aren't done jumping.
  (187 characters. Set the stat sentence at one type size, so "after having a baby" can't be skimmed past. ¹ links to `#src1`.)
- **Attribution line:** From the Leapproof team. Not a customer review. ¹From research, not our customers. Source at the bottom.
- **Kills:** O11, "it's for old women, not me" (and lightly O12).
- **Week-2 casting:**
  - A woman aged 30–45 who matches the ad angle (after a baby, trains, runs, in her 40s) and fits the measured chart.
  - Feature her own words naming her age or life stage, plus one moment.
  - Prefer someone who says, without being asked, that she thought these were for older women. To ask that directly, first add "What did you think this kind of underwear was for, before you tried it?" to FUNNEL_PLAN §8.2.

  *Why: the scene comes first, as something she has done (#123, #125). The page's one footnoted stat backs it up (00 T12, Quiz normalize). "Plumbing, not a verdict." is the BRAND_BIBLE §5 worldview, and it's the page's not-her-fault beat about the leak itself. It sits right next to the stat it explains, on screen 1–2, in the third person, so it passes the Meta "you" test. Then the honest verdict: "not just older women" is true, and "not done jumping" means capable, not old (BRAND_BIBLE §11). Installs B4 and B1.*

### Card 2: burned skeptic
- **Label:** STRAIGHT ANSWER · 2 of 3
- **Headline:** Why trust a brand you've never heard of?
- **Body:** Fair question. You shouldn't, yet. So we don't ask you to. No sale that ends at midnight. No fake doctors. On your own sneeze, laugh or run, you see if they hold.
- **Attribution line:** From the Leapproof team. Not a customer review.
- **Kills:** O8, "scam / I've been burned / I fell for the marketing."
- **Week-2 casting:**
  - A woman who has tried 2 or more things before (pads, liners, other underwear) and says she's wary of ads.
  - Feature her answers to Q1 ("Did they hold… Be honest") and Q6 ("What didn't you like?").
  - Publish it even at 2–3★.

  *Why: it agrees she's right to be wary (anger → relief, BRAND_BIBLE §6) and turns down hype she can picture (white-coat "doctor" ads). Then it puts the test on her own moment (Pre-sales beat 11, 08 T23/T24). It talks only about us, so it stays inside the CJ column and needs no OK. Installs B3.*

### Card 3: it held on the moment (the sneeze in the aisle)
- **Label:** STRAIGHT ANSWER · 3 of 3
- **Headline:** What if they leak anyway?
- **Body:** The cost is on us. The quiz checks your size first. A big sneeze in the cereal aisle is the test. Wear them through your moment for 30 nights. If they don't hold, you get your money back. You keep the pairs. Nothing to send back.
  (229 characters)
- **Attribution line:** From the Leapproof team. Not a customer review. · [Full terms at the bottom](#leak-test)
- **Kills:** O1, "it'll just leak anyway" (plus O17 and O8).
- **Week-2 casting:**
  - A woman who names her exact moment (a sneeze in a shop, the trampoline, a run, box jumps) and how many times she wore them through it.
  - Feature her answers to Q1 (did they hold) and Q4 (ride up, roll down, dig in). Prefer one who mentions fit at the legs.
  - Typicality rule: Card 3 may feature a "they held" review only if most testers who wore them through their moment said they held. Show the real tally under it at the same type size: "[X] of [Y] testers said they held on their moment." If most didn't, Card 3 stays the team note.

  *Why: it follows the plan's O1 order: name the fear, then fit, then the guarantee (FUNNEL_PLAN §5). "The cost is on us" takes the blame off her and limits the promise to money. The cereal aisle turns the test into a picture (Involvement T4). The locked §4 v5 guarantee is word for word, including "You keep the pairs. Nothing to send back.", which is the strongest answer to "what if it fails". Held behind the wear test (flag 1). Installs B3.*

## 4. Below-hero strip (Custom HTML block): cited belief line + 3 one-line steps + CTA + micro-copy

**Copy, in order:**

***Leaking is just normal now.*** **Says who?**
Leaking is "NEVER considered normal."
Ridgeview Medical Center², a US hospital · not connected to Leapproof
So nobody has to just live with it. A doctor or pelvic-floor therapist can help with the cause. Underwear is for the moment.

FIND YOUR LEAK MATCH
**About 2 minutes to find. 30 nights to test.**
1. **Tell us when it happens.**
2. **See your size and how many pairs.**
3. **Wear them through your moment for 30 nights. If they don't hold, you get your money back.**

<small>If we don't carry your size, or it's more than a little leak, we'll tell you.</small>

**[ Find my match ]**
About 2 minutes · No email needed to see your match · [30-Night Leak-Test](#leak-test)

Measured at 17px bold on a 375px phone, with 303px free beside the number: step 1 is 183px and step 2 is 264px, so each fits on one line. Step 3 wraps to about 3 lines. It is left that way on purpose: it is the locked guarantee sentence, and FUNNEL_PLAN §8.1 requires identical words everywhere.

*Why: the H2 sets the myth against the cited fact in the same words ("Leaking is…"), and no one answers "Says who?" with a "no" (00 T15). The exact Ridgeview words prove the hero's "Normal? No." right at the claim (Universal R8, brief item 7). Only the words inside the quote marks are marked as Ridgeview's. "Nobody has to just live with it" turns "not normal" into relief, not "something's wrong with me". The doctor line keeps the page from implying the underwear treats the cause (FUNNEL_PLAN §13, R8 qualify at the claim). The steps sell the quiz in three short lines: her moment, her match, then the locked guarantee sentence. The small line under them admits both limits, size and heavy leaks (Quiz F10, Kill 14, F15). The enemy line lives in hero bullet 2 and the not-her-fault beat lives in Card 1, so the strip repeats neither. Kills O12, O13, O17 and O1. Installs B1 and B3.*

**Paste-ready (Block B).** It also runs the quiz-link script, which passes `a` and `mk` to every quiz link once the whole page has loaded.
```html
<!-- Leapproof landing v4.1 FINAL · Block B · below-hero strip + quiz-link passthrough · ONE Funnelish Custom HTML element, directly under the cards -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,500&family=Hanken+Grotesk:wght@400;600;700&display=swap');
.lps{background:#F5EDE6;color:#231017;font-family:'Hanken Grotesk',Arial,sans-serif;padding:48px 16px;line-height:1.5}
.lps *{box-sizing:border-box;margin:0;padding:0}
.lps .w{max-width:560px;margin:0 auto}
.lps h2{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:26px;line-height:1.2;margin-bottom:18px}
.lps h2 em{font-weight:500}
.lps .q{font-family:'Fraunces',Georgia,serif;font-size:24px;line-height:1.3}
.lps .qq{box-shadow:inset 0 -8px 0 #E7CFC9}
.lps .src{font-size:13px;color:rgba(35,16,23,.75);margin:8px 0 18px}
.lps p{font-size:17px;margin-bottom:12px}
.lps .lab{font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#872845;margin:30px 0 6px}
.lps h3{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:22px;line-height:1.25;margin-bottom:14px}
.lps ol{list-style:none;counter-reset:s}
.lps li{counter-increment:s;position:relative;padding:2px 0 12px 40px;font-size:17px;line-height:1.4}
.lps li::before{content:counter(s);position:absolute;left:0;top:0;width:28px;height:28px;border-radius:50%;background:#231017;color:#F5EDE6;font-weight:700;font-size:15px;display:flex;align-items:center;justify-content:center}
.lps .note{font-size:14px;color:rgba(35,16,23,.75);margin:0}
.lps .btn{display:block;text-align:center;background:#A33154;color:#fff!important;text-decoration:none!important;font-weight:700;font-size:18px;padding:16px;min-height:52px;border-radius:0;margin-top:20px}
.lps .micro{font-size:14px;color:rgba(35,16,23,.75);text-align:center;margin-top:10px}
.lps .micro a{color:inherit;text-decoration:underline}
.lps sup a{color:inherit;text-decoration:none}
</style>
<section class="lps"><div class="w">
  <h2><em>Leaking is just normal now.</em> Says who?</h2>
  <p class="q">Leaking is <span class="qq">&ldquo;NEVER considered normal.&rdquo;</span></p>
  <p class="src">Ridgeview Medical Center<sup><a href="#src2">2</a></sup>, a US hospital &middot; not connected to Leapproof</p>
  <p>So nobody has to just live with it. A doctor or pelvic-floor therapist can help with the cause. Underwear is for the moment.</p>
  <p class="lab">Find Your Leak Match</p>
  <h3>About 2 minutes to find. 30 nights to test.</h3>
  <ol>
    <li><strong>Tell us when it happens.</strong></li>
    <li><strong>See your size and how many pairs.</strong></li>
    <li><strong>Wear them through your moment for 30 nights. If they don&rsquo;t hold, you get your money back.</strong></li>
  </ol>
  <p class="note">If we don&rsquo;t carry your size, or it&rsquo;s more than a little leak, we&rsquo;ll tell you.</p>
  <a class="btn" id="lp-strip-cta" href="https://leepproof.myfunnelish.com/quiz-2891028289-1791612140998314">Find my match</a>
  <p class="micro">About 2 minutes &middot; No email needed to see your match &middot; <a href="#leak-test">30-Night Leak-Test</a></p>
</div></section>
<script>
(function(){
  function run(){
    var p=new URLSearchParams(location.search);
    var a=(p.get('a')||'').toLowerCase(), mk=(p.get('mk')||'').toLowerCase();
    var keep={}; if(/^[a-z]{1,4}$/.test(a))keep.a=a; if(mk==='au')keep.mk='au';
    document.querySelectorAll('a[href*="/quiz-2891028289"]').forEach(function(l){try{var x=new URL(l.href);for(var k in keep)x.searchParams.set(k,keep[k]);l.href=x.toString();}catch(e){}});
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',run);}else{run();}
  window.addEventListener('load',run);
})();
</script>
```
*Why: one Warm Cream band with one claret button. Fraunces for the quote and headings, and Deep Claret for small text on cream (BRAND_BIBLE §17). All small text has at least 7:1 contrast. The script waits for the footer and sticky buttons to exist, so every quiz link keeps the angle (relay rule, Quiz T1). Only neutral codes are passed (privacy).*

## 5. Footer (disclaimers · #leak-test terms block · consumer-law text · links · footnotes)

**Not a treatment. It's underwear.** For heavier leaks, these aren't enough on their own.

The quiz isn't a medical assessment. It matches you to underwear. If leaking is new, painful or getting worse, talk to a doctor or a pelvic-floor therapist.

Sizes S to 2XL. They run small, so don't go by the letter on your other underwear. The quiz checks your size against the chart for this exact pair. If we don't carry your size, it tells you before you pay.

Fabric: [copy exactly from the sewn-in label, e.g. 95% cotton, 5% spandex; include the lining's fibres if the label lists them]. Imported.

The Straight Answer cards near the top are notes from the Leapproof team, not customer reviews.
[If the hero image is AI-generated:] The image at the top is AI-generated. It doesn't show real customers.
[If it is a licensed photo of models:] The women in the photo are models, not customers.

---

**`#leak-test` (anchor)**

**The 30-Night Leak-Test**
Wear them through your moment for 30 nights. If they don't hold, you get your money back. You keep the pairs. Nothing to send back.

**The Fit Promise**
Wrong size? We'll send the right one first. No need to send the other back.

**The terms, in plain words**
- Your 30 nights start the day your set arrives (the delivered date on your tracking). Wear them day or night, through your real moments.
- If they don't hold, email [support email] with your order number and what happened.
- You can claim any time during your 30 nights, or up to 14 days after your 30th night. [PENDING: Nikita OKs the 14 days, then adds them to the NUMBER_SHEET §4 CJ row. If she doesn't, this line reads exactly: "You can claim any time during your 30 nights." Never cut the line.]
- We refund the full amount you paid for your set and any extra pairs you added, to your original payment method. A claim costs you nothing.
- One claim per customer.
- The Fit Promise covers one free size swap per order. [PENDING, flag 3. Pick one and add it to NUMBER_SHEET §4: **(A)** "We send your whole set again in the new size, first." or **(B)** "We send one pair in the new size first, so you can check the fit." If B, change hero bullet 3 as noted in §2.]
- Ask for your swap within [__] days of the day your set arrives. [PENDING, flag 3]
- If no size of this pair fits you, we refund your set instead. [PENDING, flag 3]
- Shipping:
  - **AU:** Free shipping on every set.
  - **US, until confirmed:** Any shipping cost shows at checkout, before you pay. [PENDING: "We also refund the shipping you paid." OR "Shipping you paid isn't refunded."]
- The 30-Night Leak-Test and the Fit Promise are in addition to your other rights and remedies under the law.

**Your rights**
- **AU:** Our goods come with guarantees that cannot be excluded under the Australian Consumer Law. You are entitled to a replacement or refund for a major failure and compensation for any other reasonably foreseeable loss or damage. You are also entitled to have the goods repaired or replaced if the goods fail to be of acceptable quality and the failure does not amount to a major failure.
- **US:** The 30-Night Leak-Test is a limited warranty. It gives you specific legal rights, and you may also have other rights which vary from state to state. Nothing on this page limits your rights under federal or state law. [PENDING: US counsel confirms the Magnuson-Moss designation before any US traffic.]

[Registered business name] · ABN [ ] · [business address] · [phone] · [support email]

**[ Find my match ]** (id `lp-foot-cta`)
About 2 minutes · No email needed to see your match

**Sources** (every URL opens in a new tab: `target="_blank" rel="noopener"`)
- ¹ *(anchor `#src1`; default and every angle page except `t`)* A review of studies of leaking between 6 weeks and 1 year after giving birth. Moossdorff-Steinhauser et al., International Urogynecology Journal, 2021. PMC8295150, https://pmc.ncbi.nlm.nih.gov/articles/PMC8295150/ (accessed 11 Oct 2026). Research results, not Leapproof customers.
  - *On the `t` page only, and only after the corrected CrossFit line is in NUMBER_SHEET §11 (flag 14), ¹ reads instead:* Two reviews of studies of women who do CrossFit. Álvarez-García & Doğanay, Archivos Españoles de Urología, 2022, PubMed 35173077, https://pubmed.ncbi.nlm.nih.gov/35173077/; Dominguez-Antuña et al., International Urogynecology Journal, 2023, PubMed 35635565, https://pubmed.ncbi.nlm.nih.gov/35635565/ (both accessed 11 Oct 2026). Research results, not Leapproof customers.
- ² *(anchor `#src2`)* Ridgeview Medical Center, "Coughing, laughing or sneezing shouldn't cause peeing", https://www.ridgeviewmedical.org/health-eviews/coughing-laughing-or-sneezing-shouldnt-cause-peeing/ (accessed 11 Oct 2026). The words "NEVER considered normal." are copied from this page.

Words in quote marks next to a named source are copied exactly from that source. Leapproof isn't connected to, or endorsed by, any source named on this page.

Privacy · Terms · Contact (US traffic adds: **Consumer Health Data Privacy**)
© [year field] leapproof

*Page settings:*
- *Title tag:* Find Your Match | leapproof
- *Meta description (151):* Black cotton briefs for the sneeze, the laugh and the jump. A 2-minute quiz finds your size and how many pairs you need. 30 nights to see if they hold.
- *OG title:* Find Your Match | leapproof
- *OG description:* same as the meta description.
- *OG image:* the locked hero photo (a 1200×630 crop of the same file, with both faces and the raised hand fully in frame). It is not a new image. It replaces any template skincare image, so a shared link never pulls skincare text or pictures.
- *Slug* /match · no popup, no exit-intent, no countdown.

*Why: compliance doubles as trust (Universal 3.3). Every material term of the guarantee and the Fit Promise is in plain words, one tap from every mention (FTC 16 CFR 239, ACL s18/s29(1)(m)). The terms run in this order: guarantee → promise → terms → rights → warrantor details, then the button, so nothing splits the warranty text (reg 90). The heavy-leak limit is now impersonal ("For heavier leaks…"), so it passes the page's own Meta "you" rule. The heavy-leak limit, the size ceiling and "runs small" are the honest "not for you if" lines (F15, NUMBER_SHEET §13). The fabric line covers the US textile rules for "cotton". The image line is true whichever origin is confirmed. The tab title, share title, description and alt text all avoid "leak" and "pee", so a glanced or shared screen never names her condition (O14). The only exits are the legal links (Kill 9). Kills O8, O1 and O17. Installs B3 and B6.*

## 6. Mobile hero overlay text + sticky mobile CTA text

**Build order (do this first):**
- In Funnelish, drag the image block ABOVE the split-hero section and set it to Mobile only.
- In the split hero, hide these on mobile: image, logo, nav button, eyebrow, H1, CTA and micro-copy.
- On a phone, the order must be: top bar → image block (logo + chip, caption 1, caption 2, button) → micro-copy → subhead → 3 bullets → proof row → cards (stacked) → strip → footer.
- If the image block can't be moved above the split hero, don't use it on mobile. Show the split hero's own eyebrow, H1, CTA and micro-copy first, with the image below the micro-copy.

**Image:** the locked photo, 4:5 (`hero-mobile-4x5.jpg`, 1080×1350).
**Alt text:** Two women laughing on a sunny footpath, holding takeaway coffees

Positions measured on the file:
- The friend's hair starts about 27% down, right of centre. The laughing woman's hair starts about 34% down, on the left.
- The raised hand ends about 38% down.
- Her knees sit at about 78–88%.

**Top band, on the sky.** Plum Ink gradient: 75% at the top edge, fading to 0% at 26% height.
- **Row 1 (2–8% height):** on the left, the light logo ("leap" in Warm Cream, "*proof*" in italic Rose #E7879F). On the right, a Plum Ink chip with Warm Cream 10–11px caps: **LEAK-RESISTANT UNDERWEAR**. Both must fit on one row at 375px.
- **Caption 1 (about 10–17% height, left-aligned):** ***Stop! I'll pee myself!*** in a solid Plum Ink #231017 caption label (92% opacity, 8px corner radius, 6px 12px padding), Warm Cream Fraunces italic 24px, one line. A caption label, not a speech bubble.
- **Caption 2 (about 19–25% height, directly under it):** **Common? Yes. Normal? No.** in the same label style, Warm Cream Fraunces 22px upright, one line. It must end above 26%, so it clears the friend's face.
- Never set Warm Cream text straight on the sky or the branches.

**Bottom band:**
- Plum Ink gradient: 0% at 76% height, rising to 70% at the bottom edge.
- **Button only:** **Find my match**. Claret, full width minus the 16px gutters, at least 48px tall, bottom edge about 4% above the image's bottom.
- No text over either woman's body. H1 line 3 is dropped on mobile because the button says it.

**Keep clear:** both faces and the raised hand stay fully uncovered.

**Directly under the image (rebuilt inside the image block):** About 2 minutes · No email needed to see your match · [30-Night Leak-Test](#leak-test) (Plum Ink at 75%, 14px).

**Fallback:** use this if Funnelish can't place a button on the image, or if the image licence doesn't cover a caption beside her face (flag 5):
- Move caption 1 and the button into a Plum Ink band directly under the image, in that order.
- Keep caption 2 on the sky.
- Re-check that the button is on screen 1 at 375px.

**Sticky mobile bar:**
- Left label: **About 2 minutes** (14px, Plum Ink at 75%) · button: **Find my match**
- It appears once the image-block button scrolls away. It hides while `#lp-strip-cta` or `#lp-foot-cta` is on screen.

*Why: a stacked 4:5 image would push the button below the fold (Universal F16). The meme split keeps the product chip, the moment, the belief flip, the action and the risk line on screen 1 without covering a face (Kill 8). Solid caption labels keep the hook readable over the bright, busy sky (about 12:1 instead of about 2.3:1). "Normal? No." sits on the sky, never over her body, so it can't read as a verdict on her (never shame). The sticky bar keeps the one next step under her thumb (Universal 3.7). Kills O13.*

## 7. Ad-angle H1 swaps (?a=) — impersonal, no "you", Meta-safe

**Launch with the default H1 plus `m` only**, as the Meta A/B. Build every other row only when an ad carrying that exact line is live. Until then, unknown codes fall back to the default.

Funnelish's native text slots can't read `?a=`, so build each live angle one of two ways:
- clone the page per angle (/match-m and so on) and set that page's H1, Card 1 and footer source ¹ by hand, or
- give the H1, Card 1 and the footer's ¹ line IDs (if the editor allows) and add a text swap keyed on `?a=`.

Before any ad uses `s` or `j`, add them to the FUNNEL_PLAN §6 code table and to the QUIZ_FUNNEL_BUILD §4 intro headline map.

Only the default, `m` and `r` sit naturally over the laugh photo. On mobile, line 1 goes in caption 1 and line 2 in caption 2. If a line 2 wraps at 375px, keep its label in the left 60% of the image so it clears the friend's face.

**Card 1 body on every row** = scene line + stat¹ + "Plumbing, not a verdict." + close.

| `?a=` | H1 (3 lines) | Chars | Card 1 scene line | Card 1 stat¹ | Card 1 close | Build |
|---|---|---|---|---|---|---|
| default (laugh / this photo) | ***Stop! I'll pee myself!*** / Common? Yes. Normal? No. / Find your match. | 64 | Ever watched from the side at the trampoline park? | About 1 in 3 women leak after having a baby. | So, not just older women. It's for women who aren't done jumping. | launch |
| `m` sneeze-laugh-jump | Sneeze. Laugh. Jump. / A little leak is common. *Not normal.* / Find your match. | 74 | same as default | same as default | same | launch (A/B) |
| `s` sneeze | *Achoo.* Legs crossed. / A little leak? Common. *Not normal.* / Find your match. | 72 | same as default | same as default | same | when ad is live |
| `j` trampoline | Trampoline? *I'll watch.* / A little leak? Common. *Not normal.* / Find your match. | 75 | Ever crossed your legs before a sneeze? | same as default | same | when ad is live |
| `p` after a baby | Sneeze. Laugh. Jump. / After a baby, a little leak is common.¹ *Not normal.* | 72 | same as default | same as default | same | when ad is live |
| `t` lift / CrossFit | Double-unders. PRs. / A little leak is common. *Not normal.* / Find your match. | 73 | Ever sat out the box jumps? | PENDING §11 fix (flag 14): Two reviews put it at about 1 in 3 up to nearly half of women who do CrossFit. Until it's in §11: same as default. | So, not just older women. It's for women who aren't done lifting. | when ad is live |
| `run` | Hills. Sprints. / A little leak is common. *Not normal.* / Find your match. | 69 | Ever cut a run short, just in case? | same as default (§11 has no running stat) | So, not just older women. It's for women who aren't done running. | when ad is live |
| `r` 40s | Run. Lift. Laugh. / A little leak is common. *Not normal.* / Find your match. | 71 | Ever sat one out, just in case? | same as default | same as default | when ad is live |
| `n` belief test | Sneeze. Laugh. Jump. / A little leak? Common isn't the same as normal. | 68 | same as default | same as default | same | A/B in ads first |

Notes:
- On `p`, the ¹ in the H1 points to the postpartum review, because that line makes a prevalence claim. Card 1 repeats the same stat, so the footnote doesn't change.
- On `t`, once the corrected CrossFit line is in §11, the ¹ marker stays the same and the footer's ¹ line swaps to the two CrossFit reviews (§5).
- `p` and `n` drop line 3. The subhead carries the promise.

*Why: one swappable hero over one shared body (Universal 3.5, Kill 1). Every line opens on the moment, using a first-person saying or an impersonal fragment. No named source. No age, postpartum or condition statement in the second person (FUNNEL_PLAN §6). `s` and `j` name the leak, so "Common" has something to point at. A lifter gets a lifter's stat as soon as §11 can back one. Until then, and for runners, the true postpartum stat stays, which beats an unsupported number. Kills O12. Names O1.*

## 8. Headline ingredient audit — H1 + subhead vs Nikita's 7 (curiosity, call out the pain, promise the solution, specificity, simplicity, credibility, timeframe): name the exact words for each present; minimum 5, honestly

**H1:** Stop! I'll pee myself! / Common? Yes. Normal? No. / Find your match.
**Subhead:** Black cotton briefs for women who'd rather laugh than cross their legs. The quiz works out your size and how many pairs you need. Then 30 nights to see if they hold.

| Ingredient | Present? | Exact words |
|---|---|---|
| Call out the pain | YES (H1 + sub) | "Stop! I'll pee myself!" · "rather laugh than cross their legs" |
| Curiosity | YES (H1) | "Common? Yes. Normal? No." (if it's common, why isn't it normal? Paid off by Ridgeview in §4) · "your match" (matched how? Paid off by the 3 steps) |
| Promise the solution | THIN (H1 + sub) | "Find your match." plus "works out your size and how many pairs you need". It promises a match, not relief. The outcome is only implied by "rather laugh than cross their legs" and "see if they hold". It can't get stronger until the wear test passes (flag 1). After that, A/B line 3 as "Find what holds." |
| Specificity | YES (sub) | "Black cotton briefs" · "your size and how many pairs" · "30 nights" |
| Simplicity | YES | 64-character H1 in 3 short lines; 6 short sentences; almost all one- and two-syllable words |
| Timeframe | YES (sub) | "Then 30 nights to see if they hold." ("2-MIN QUIZ" sits in the eyebrow right above the H1, and "About 2 minutes" is in the micro-copy, but neither is counted here.) |
| Credibility | NO | By design: there's no named source, number or rating in the H1 or subhead. On screen 1, credibility sits around the headline instead: the top bar ("Money back if they don't hold", with its 30-night limit), the micro-copy link to the terms, the honest proof row and Card 1's footnoted stat. |

**Honest score:**
- 6 of 7 across H1 + subhead, with Promise marked thin. That clears the floor of 5.
- The H1 alone scores 4: pain, curiosity, simplicity and a thin promise.
- Swaps: `m`, `s`, `j`, `t`, `run` and `r` add specificity in the H1 (named moments), so they score 5. `p` and `n` score 4. All of them score 6 with the shared subhead.

**Reading level** (eyebrow through proof row: 87 words, 24 sentences and fragments): about 3.6 words per sentence, and about 6% of words have 3+ syllables. Gunning Fog is about 4, below the year 5–6 target.

## 9. Launch flags (only what still blocks traffic)

1. **In-house wear test (BLOCKER).**
   - Wear at least 3 pairs through real light leaks (sneeze, laugh, jump, run, lift), washing between wears.
   - Log every wear in writing (date, moment, pair, result, washes so far) and keep the log. It is the evidence behind every performance word on the page.
   - Lines that depend on it: "LEAK-RESISTANT" (eyebrow and chip), "No pad to bunch" (bullet 2), "see if they hold" (subhead, Card 2 and the meta/OG description), Card 3 and strip step 3.
   - A founder test supports "leak-resistant" only. It never supports "holds", "dry", "stops leaks" or "for light leaks" as a claim.
   - If the pairs fail, this SKU doesn't launch for this use.
2. **Measure a real pair (BLOCKER).**
   - Measure relaxed and at comfortable stretch, then rebuild the quiz size chart from those measurements.
   - Until then, the subhead's "works out your size", Card 3's "checks your size" and the Fit Promise all rest on CJ's unverified chart.
   - Never publish US/AU size numbers or body-fit numbers on this page.
3. **Fit Promise scope (BLOCKER).** Nikita decides three things, then adds them to NUMBER_SHEET §4:
   - (a) whole set (A) vs one pair (B). §4 currently costs it as a single-pair reship (~$9.79), so A costs more.
   - (b) the swap request window.
   - (c) a refund when no size fits (2XL ≈ US12 is the ceiling).
   - Then fill the three PENDING footer lines. If B, change hero bullet 3.
4. **Guarantee paperwork + doc sync (BLOCKER).**
   - Nikita OKs the 14-day claim window, and it goes into the §4 CJ row first. Otherwise use the exact fallback line; never cut it.
   - Fill in the business name, ABN, address, phone and a staffed support email.
   - Set up stop-loss tracking (10% of the first 50 orders).
   - Use identical guarantee and Fit Promise words in:
     - QUIZ_FUNNEL_BUILD (lines 151, 171, 185)
     - PRODUCT_INFO_MAP (24, 76)
     - FUNNEL_PLAN Card A
     - OFFER.md (43)
   - In FUNNEL_PLAN:
     - Change §2 line 62, "30-Day Leak-Test (terms D2)" → "30-Night Leak-Test, keep the pairs (NUMBER_SHEET §4 LOCKED v5)".
     - Change every "[30/60]" to "30" (lines 87, 197, 200, 222, 306, 307, 335, 364).
     - Use the full locked sentence in lines 306 and 335.
     - Change the §11 volunteered negative "If you leak a lot, these aren't enough on their own." → "For heavier leaks, these aren't enough on their own." (the old line fails the §6 "you" test).
5. **Hero image origin (BLOCKER).**
   - The file has no metadata. It came from the generated before/after pair (commit 886c9d4), so it is probably AI. Confirm in writing.
   - If AI: use the AI footer line.
   - If it's a licensed photo of models: confirm the licence or release covers a bladder-leak use AND a caption beside her face. Otherwise use the §6 fallback (caption 1 under the image) and keep line 1 as plain H1 text on desktop.
6. **Quiz domain (BLOCKER).**
   - "leepproof.myfunnelish.com" looks like phishing to a burned skeptic. Move the quiz to a leapproof.com subdomain and update NUMBER_SHEET §12b.
   - Then update every button: hero, mobile block, Block B, footer, sticky bar and nav fallback.
7. **Market (BLOCKER for US traffic).**
   - Every AU ad-set URL carries `&mk=au`. Apply the same rule to the quiz intro trust row: "Free shipping" only on `mk=au`.
   - Run US ad sets only after these are done:
     - US free shipping confirmed (§5)
     - AUD vs USD settled on the reveal
     - US shipping-refund line picked
     - Magnuson-Moss designation confirmed by counsel
     - fabric line copied from the label
     - Consumer Health Data Privacy link live and the privacy page reviewed
8. **Proof row.** Nikita OKs "New brand, no reviews yet. We won't fake any." or the fallback ships. Card 2 needs no OK.
9. **The quiz must keep this page's promises.**
   - The gate's Skip works on a phone, or "No email needed" is false.
   - Size and pairs really change with her answers (Kill 14).
   - Build the "we don't carry your size" branch and the Q4 "more than a little leak" line.
   - Time a real run-through to confirm "about 2 minutes" (and "2-MIN" in the eyebrow).
   - On the intro screen, cut "what it needs to handle" and "your price and free gifts". Lift "Find your match" into the intro headline. The quiz reads `a` and `mk`.
10. **Mobile build and check.**
    - Follow the §6 build order.
    - At 375px and 390px, inside the Instagram and Facebook in-app browsers, check:
      - the chip and both captions sit on the sky and are readable;
      - the button is on screen 1;
      - no text covers a face or the raised hand;
      - the micro-copy shows directly under the image.
    - Confirm the `?a=`/`mk` passthrough reaches Funnelish's native buttons. If it doesn't, turn on URL-parameter forwarding.
    - Load the page with `?mk=au` and confirm the AU top-bar line shows. Load it without and confirm the default shows. If the AU line doesn't appear, Funnelish isn't running scripts inside Custom HTML. The safe default shows, so nothing false goes live, but fix it (or clone a /match-au page with the AU line typed in) before AU ads run.
    - Check the eyebrow sits on one line in the desktop pill. If it doesn't, use "2-MIN UNDERWEAR QUIZ".
11. **Template clean-up.**
    - Delete these with no empty widgets left behind: stars, "Rate 4.9", avatars, "Loved by 1.2k customers", "Buy Product", the "Quick Quiz" labels, skincare icons, and the card photo, name and rating slots.
    - Logo unlinked. Carousel without autoplay, equal-height slides, stacked on mobile if possible. No popup, exit-intent or countdown.
    - Set the alt text, meta description, OG title, OG description and OG image (§2, §5, §6), so no template skincare text or image survives in a shared link.
12. **Pixel and privacy.** Turn off Meta "Track events automatically without code" and automatic advanced matching. Slug /match. Only neutral `?a=`/`mk` codes; never put quiz answers in URLs or event names.
13. **Rebuild the pasted blocks.**
    - Block A (new, with its own `mk=au` script) goes at the top.
    - L1 is replaced by Block B.
    - L2 gets the new footer order, the PENDING lines, the fabric and image lines, the "For heavier leaks" line, sources ¹–² only (Franciscan removed), new-tab source links and the `lp-foot-cta` button.
    - L3's label goes to `rgba(35,16,23,.75)` 14px, and the bar hides on `#lp-strip-cta` and `#lp-foot-cta`.
    - Update HERO_PASTE_LIST.
14. **Sources.**
    - Confirm "a US hospital" (Ridgeview, Waconia, Minnesota) on its About page.
    - Add footnotes ¹–² to NUMBER_SHEET §11. Add "31% weighted average" there first if ¹ should ever quote it.
    - **What's wrong with the §11 CrossFit line:** its lower end, "about 1 in 5", isn't supported. The two CrossFit reviews checked on 11 Oct 2026 found 32.1% (Álvarez-García & Doğanay 2022, PubMed 35173077) and 44.5% (Dominguez-Antuña et al. 2023, PubMed 35635565). Neither supports "1 in 5", so shipping the line as written would put an unsupported number on the page. Proposed §11 line: "Two reviews put it at about 1 in 3 up to nearly half of women who do CrossFit.*" Once Nikita puts it in §11, the `t` page's Card 1 uses it (§7) and its footer ¹ swaps to both reviews (§5). The same fix is needed in quiz Card 1 (Athlete) and FUNNEL_PLAN's Athlete line.
    - §11 has no running stat, so `run` keeps the postpartum stat. Add a sourced running line to §11 first if one is wanted.
15. **Sample checks.**
    - Bullet 1 must hold up laid flat and worn (lace hips, higher back). If not, use the fallback.
    - "Cotton" and the fabric line come from the sewn-in label.
    - Confirm the lining runs front to back.

## 10. Chief log

| Lens | Issue | What I changed (or why I rejected it) |
|---|---|---|
| fundamentals | MAJOR: mobile block order never stated; H1 and CTA fall off screen 1 | Applied in full: the image block moves above the split hero, split-hero items are hidden on mobile, the micro-copy is rebuilt under the image, the phone order is listed, and there's a fallback if the block can't move (§6). |
| fundamentals | MAJOR: H1 line 1 unreadable on the bright sky (about 2.3:1) | Applied: solid Plum Ink caption labels (92%) for line 1 and line 2, and a 75%→0% gradient at 26% for the logo and chip. No Warm Cream text straight on sky or branches. |
| fundamentals | MAJOR: no way to swap the AU and US top bars | Applied with ICP's wording: a US-safe default line for everyone, and the AU line only on `mk=au` via script. The cloned /match-au page is mentioned as an alternative. The same rule is set for the quiz intro trust row (flag 7). |
| fundamentals | MAJOR: card disclosure and label colours fail contrast | Applied: Card 1 label Rose and attribution Blush. Cards 2–3 label Deep Claret and attribution Plum Ink. All at least 13px. No Rose Taupe. |
| fundamentals | minor: "QUICK MATCH" vague; timer icon with no time | Merged with ICP (name the quiz): desktop "LEAK-RESISTANT UNDERWEAR · QUIZ: ABOUT 2 MINUTES". "QUIZ:" ties the time to the quiz, so it can't read as "leak-resistant for 2 minutes". Mobile chip "LEAK-RESISTANT UNDERWEAR". (Shortened in Patch v4.1.) |
| fundamentals | minor: Card 1 "You're not the only one." repeats quiz Card 1 | Cut. All three chiefs agreed. |
| fundamentals | minor: Card 3 "finds your size" is false above 2XL | "First, the quiz checks your size." True for everyone; the ceiling is admitted in step 2 and the footer. (Reworded in Patch v4.1.) |
| fundamentals | minor: strip H2 is a question many answer "no" | Replaced with "*Leaking is just normal now.* Says who?". Nobody answers it "no", it has no "you" (which fixes compliance's major too), and it echoes the quote's "Leaking is…". |
| fundamentals | minor: "never" four times | "NEVER" now appears only inside the Ridgeview quote. The payoff is "So nobody has to just live with it." and the fault line was "If they didn't feel right, that's not on you." (moved to Card 1 as "Plumbing, not a verdict." in Patch v4.1). |
| fundamentals | minor: step 2 "Not your size? We'll say so." ambiguous | "If we don't carry your size, or it's more than a little leak, we'll tell you." Clear on one read, and it carries compliance's heavy-leak limit without "you leak". (Moved under the steps in Patch v4.1.) |
| fundamentals | minor: passthrough script runs before later buttons exist | Applied (DOMContentLoaded + load) and extended to pass `mk` and swap the top bar. |
| fundamentals | minor: small strip text fails contrast; L3 label | Applied `rgba(35,16,23,.75)` (about 7.5:1) to .src, .micro and the sticky label. The strip label moved to Deep Claret. |
| fundamentals | minor: `s`/`j` "Common?" has no referent | Applied "A little leak? Common. *Not normal.*" on both. |
| fundamentals | minor: no build mechanism for swaps | Applied: clone per angle or an ID-keyed swap. `s`/`j` are added to the FUNNEL_PLAN §6 and quiz intro maps before use. Combined with ICP: launch default + `m` only. |
| fundamentals | minor: audit overstates Promise as "YES" | Marked THIN, with the A/B path after the wear test. |
| fundamentals | minor: footer repeats the strip's "not a medical assessment" | Resolved the other way round: the line is cut from the strip (per ICP, so no clinical words sit at the button), and the footer keeps the page's only copy. |
| fundamentals | minor: source links are exits; ¹ not linked | Applied: new tab with `rel="noopener"`; footnote markers link to their #src anchors. |
| fundamentals | minor: FUNNEL_PLAN still says "30-Day" and "[30/60]" | Added the exact line edits to flag 4. |
| icp-depth | MAJOR: no plain "money back" on screen 1; "every set" undefined | Applied "Money back if they don't hold" to both top-bar lines and dropped "every set". Kept the name "30-Night Leak-Test" in the default bar and the micro-copy so the terms link stays named. |
| icp-depth | MAJOR: subhead "set", "brace", "jump than watch" | Applied "laugh than cross their legs" (the exact pose in the photo and #90) and "how many pairs you need". The trampoline lives in Card 1. Also took compliance's "see if they hold". Moving the time to the eyebrow made room for "The quiz works out…", which names the next step. |
| icp-depth | MAJOR: "So *just live with it*…" reads as an instruction | Took the fix but not the wording: "So nobody has to just live with it." Rejected ICP's "you don't have to just live with it": its "it" assumes her condition in the second person, the same flaw compliance found in the old H2. |
| icp-depth | MAJOR: Card 1 opens on an italic saying with no quote marks; filler | Applied "Ever watched from the side at the trampoline park?" and `r` "Ever sat one out, just in case?". Cut the filler. |
| icp-depth | MAJOR: Card 3 "this pair's own chart", doubled instruction, too long | Merged with fundamentals and compliance: "Then the cost is on us. First, the quiz checks your size. Then a big sneeze in the cereal aisle is the test." plus the locked guarantee. The scene stays; the extra scaffolding is gone. (Tightened again in Patch v4.1.) |
| icp-depth | MAJOR: strip carries more than the brief allows | Partly applied in v4, finished in Patch v4.1 (see below). In v4: cut the button disclaimer, made step 3 the locked sentence, and added the "a US hospital" descriptor. Kept "not connected to Leapproof" at the quote, because a non-endorsement disclosure belongs at the claim (R8, FTC). Kept compliance's doctor/underwear line, because it qualifies the treatment claim at the claim. |
| icp-depth | minor: "Stop, I'm going to pee!" reads as "off to the toilet" | Applied "Stop! I'll pee myself!" (22): her own verb, unambiguous, still one line on mobile. |
| icp-depth | minor: eyebrow should name the quiz | Merged into the quiz-plus-time eyebrow (see the fundamentals row and Patch v4.1). |
| icp-depth | minor: Card 2 "made-up experts" abstract; "real life" | Applied "No fake doctors." and "On your own sneeze, laugh or run, you see if they hold." Rejected "Then you decide." per compliance (it implies a refund at her option). |
| icp-depth | minor: proof-row fallback reads like a slogan | Merged with compliance: "We're new. Straight answers, no fake reviews." It hands off to the STRAIGHT ANSWER cards, has two beats instead of three, and limits the honesty claim to reviews. |
| icp-depth | minor: bullet 3 "Fit Promise" is a label | Applied "Wrong size? One free size swap." It's the sheet's own term and true under either flag-3 option. |
| icp-depth | minor: bullet 1 "everyday black brief" | Applied "Looks like regular black underwear" (#103, #106). |
| icp-depth | minor: "Normal? No." laid over her body; line 1 low on the gradient | Applied the intent differently: both H1 lines sit on the sky in labels (top 0–25%). Only the button sits low, below the knees. H1 line 3 is dropped on mobile. Rejected moving line 2 under the image, because that pushes the belief flip off screen 1. |
| icp-depth | minor: 9 swap variants is too much build | Applied: launch default + `m`; build the rest only once a matching ad is live. |
| icp-depth | minor: attribution lines inconsistent | Applied one wording on all three. Card 1 adds "¹From research, not our customers. Source at the bottom." |
| icp-depth | minor: footer size line uses single-pair wording | Merged with compliance's runs-small line, using "if we don't carry your size". |
| icp-depth | minor: flag 1 dependency list out of date | Applied, with the new subhead and Card 2 wording. |
| compliance | BLOCKER: Fit Promise unkeepable as written (scope, window, no remedy above 2XL) | The terms now carry the PENDING (A)/(B) scope, a request window and a refund if no size fits. Hero bullet 3 states only the sheet's literal term. Flag 3 is a BLOCKER that sends all three to NUMBER_SHEET §4 first. |
| compliance | BLOCKER: misleading S–2XL; sizing claim rests on an unmeasured chart | Footer: "They run small, so don't go by the letter…". Restored "Measure a real pair" as BLOCKER flag 2, naming every line that depends on it. |
| compliance | MAJOR: "Nothing faked." unscoped next to a likely AI image | Replaced with "no fake reviews" (limited to reviews). |
| compliance | MAJOR: photo framing; speech line beside her face | Added the AI and model footer lines. Caption 1 is a label, not a bubble, and the fallback moves it under the image. Flag 5 is a BLOCKER (no metadata found; the file came from the generated pair). |
| compliance | MAJOR: "not normal" + underwear implies treatment | Added at the claim: "A doctor or pelvic-floor therapist can help with the cause. Underwear is for the moment." |
| compliance | MAJOR: heavy-leak limit dropped | The steps block now has "or it's more than a little leak". The footer leads with the heavy-leak limit (reworded in Patch v4.1). |
| compliance | MAJOR: trial framing ("test them… then you decide") | The subhead now says "see if they hold". Card 2 drops "Then you decide". Step 3 is the locked sentence with its condition. The top bar states the condition. |
| compliance | MAJOR: strip H2 presumes her condition in the second person | The impersonal myth line replaces it (see the fundamentals row). |
| compliance | MAJOR: Card 1 "not the only one" + stat; "So, no." denies the age link | Cut the first. Applied "So, not just older women.", which is true against NUMBER_SHEET §11. |
| compliance | MAJOR: no AU/US switch | One page with a US-safe default bar plus the AU line on `mk=au`. Compliance itself allowed "one page uses the US line for everyone". US ad sets wait on flag 7. |
| compliance | MAJOR: "cotton" triggers US fibre disclosure | Footer: "Fabric: [from label]. Imported." |
| compliance | MAJOR: Magnuson-Moss written warranty; US shipping refund unstated | Added the US "limited warranty" text plus a two-option shipping line, both PENDING counsel/Nikita (flag 7). |
| compliance | MAJOR: Founding-30 typicality and consent | Added both rules (Card 3 tally rule; plain-words consent naming leak content, placements and withdrawal). |
| compliance | minor: blockquote marks our words as Ridgeview's | Applied the span markup; only the quoted words are highlighted. |
| compliance | minor: start date, "full price", cutting the window | Applied: tracking delivered date; "the full amount you paid… original payment method"; exact fallback line, never cut. |
| compliance | minor: CTA splits the warranty text | Applied the order: Leak-Test → Fit Promise → terms → rights → warrantor details → button → sources. |
| compliance | minor: ¹ is a review, not "a study" | Changed to "A review of studies…". Held "31%" off the page until it is in NUMBER_SHEET §11 (CLAUDE.md number rule). |
| compliance | minor: "It's on us" implies covering damage | Changed to "the cost is on us". |
| compliance | minor: wear-test dependency list incomplete; no evidence log | Applied: bullet 2 and "see if they hold" added; a written wear log is required; a founder test supports "leak-resistant" only. |
| merge | Top bar: default "Fit Promise on every set" (fundamentals) vs money back (ICP) vs Fit Promise BLOCKER (compliance) | Chose money back. It serves the tap best and puts no unsettled Fit Promise term on screen 1. |
| merge | Where "about 2 minutes" goes (eyebrow vs subhead) | Eyebrow plus micro-copy only, so it isn't said three times on screen 1. The subhead's timeframe is "30 nights". Both timeframes still show on screen 1. |
| merge | Line 3 "Find your match." on mobile | Dropped from the overlay because the button says "Find my match" right below. That saves vertical room so both H1 lines clear the friend's face. |
| Patch v4.1 | WRONG (brief 1d): strip ran past "one cited belief line + 3 one-line steps": 6 extra belief sentences plus a hidden Franciscan quote | Cut it to the H2, the Ridgeview quote and source, and one line: "So nobody has to just live with it. A doctor or pelvic-floor therapist can help with the cause. Underwear is for the moment." Cut the enemy-sentence paragraph (hero bullet 2 already says "No pad to bunch. Nothing to throw away."), "that's not on you" and "Let's find what does." Removed the Franciscan block, its `?a=r` script line and footnote ³. `r` now uses the default strip. |
| Patch v4.1 | WRONG (brief 1d): steps ran 85–111 characters and wrapped to 3–4 lines | Now bold one-liners: "Tell us when it happens." / "See your size and how many pairs." / the locked guarantee sentence. Measured at 17px bold on a 375px phone: steps 1–2 fit on one line (183px and 264px of 303px). Step 3 wraps to about 3 lines because it is the locked sentence word for word (FUNNEL_PLAN §8.1). That is intentional and noted under the strip. The size and heavy-leak line moved to one small 14px line under the list and was kept (Kill 14, F15). |
| Patch v4.1 | WEAK (brief item 2): no not-her-fault line about the leak itself; the only one was about pads, and it sat below the cards | Card 1 now reads "…after having a baby.¹ Plumbing, not a verdict. So, not just older women…". That's the BRAND_BIBLE §5 worldview, in the third person, so it passes the Meta "you" test, and it sits on screen 1–2 next to the stat it explains. It's carried into every `?a=` Card 1 (§7 formula). |
| Patch v4.1 | WRONG (the page's own Meta "you" rule): footer "If you leak a lot…" | Now "For heavier leaks, these aren't enough on their own." Added the matching FUNNEL_PLAN §11 edit to flag 4. |
| Patch v4.1 | RISK/WRONG: AU top bar dropped the 30-night limit | Now "Free shipping · 30 nights, money back if they don't hold" (56). Measured 320px at 13px in Hanken Grotesk and 319px in the Arial-metric fallback, against 343px free at 375px (328px at 360px). It fits on one line. |
| Patch v4.1 | RISK: the 48-character eyebrow will wrap in a pill sized for "Quick Quiz" | Now "LEAK-RESISTANT UNDERWEAR · 2-MIN QUIZ" (37), measured at 241–321px depending on size and tracking. Fallback if it still wraps in the editor: "2-MIN UNDERWEAR QUIZ" (20). "QUIZ" still follows the time directly, so it can't read as "leak-resistant for 2 minutes". The check is added to flag 10. |
| Patch v4.1 | MINOR: Card 3 at 240 characters, clunky "Then… Then…", uneven slide height | Now "The cost is on us. The quiz checks your size first. A big sneeze in the cereal aisle is the test." + the locked guarantee (229). The cereal-aisle moment is kept. Kept "You keep the pairs. Nothing to send back.", the locked v5 wording and the strongest O1 answer. Added equal-height slides on desktop to the build notes; mobile is stacked. |
| Patch v4.1 | MISSING: alt text; meta description; OG title | Added alt text for both crops of the locked photo (§2, §6), plus a meta description, OG title, OG description and OG image (the locked hero photo, cropped; not a new image) in §5 page settings. None of them says "leak" or "pee", matching the "Find Your Match" title tag (O14). Template clean-up is added to flag 11. "See if they hold" in the description is added to flag 1. |
| Patch v4.1 | MINOR (swap table): `t` and `run` used the postpartum mirror; flag 14 vs §11 | Explained what's wrong with §11 instead of shipping it: the "about 1 in 5" lower end isn't supported by either CrossFit review checked (32.1%, PubMed 35173077; 44.5%, PubMed 35635565). Proposed a corrected §11 line. `t` Card 1 switches to it, with ¹ swapped to both reviews, as soon as Nikita adds it. `run` keeps the postpartum stat because §11 has no running stat. Added a "Card 1 stat" column to §7 and rewrote flag 14. |
| Patch v4.1 | MINOR (build check): the Block B script might not reach Block A inside Funnelish | Moved the `mk=au` swap into Block A itself, so the top bar no longer depends on another Custom HTML element. Block B keeps only the quiz-link passthrough. Flag 10 now says to load `?mk=au` and confirm the AU line shows. If the script doesn't run, the safe default shows. |
| Patch v4.1 | NOTE (doc hygiene, no page change): computed constraint notes (§3, §7 item 3) still say "Do NOT say keep the pairs" | No change. The page follows NUMBER_SHEET §4 CJ row LOCKED v5 ("keep the pairs, nothing to send back"), checked again today; the older notes are stale. The 14-day window is still not in §4, so it stays PENDING (flag 4). |

Files used:
- /home/user/NG/brand/leapproof/funnel/LANDING_PAGE_COPY.md (v3 base, read in full; v3 flag 11 and Patch v3 rows for the CrossFit source check)
- /home/user/NG/brand/leapproof/funnel/NUMBER_SHEET.md (§4 LOCKED v5 re-checked, §5, §11 re-checked, §12, §12b, §13)
- /home/user/NG/brand/leapproof/assets/landing/funnelish/hero-mobile-4x5.jpg (viewed; face, hand and knee positions measured for the overlay)
- /home/user/NG/brand/leapproof/assets/landing/hero-before-laugh-brace.webp (no origin metadata; commit 886c9d4)
- Blocks to rebuild: /home/user/NG/brand/leapproof/funnel/blocks/landing/L1-how-it-works-mini.html, L2-footer-terms-sources.html, L3-sticky-mobile-bar.html
- Text-width checks: Hanken Grotesk 400/600/700 (fontsource) and Liberation Sans (Arial metrics), measured with PIL in /tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/measure.py
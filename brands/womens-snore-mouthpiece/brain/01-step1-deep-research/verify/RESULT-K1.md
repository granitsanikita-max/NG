# RESULT-K1: adversarial fact-check (wedge, market, competition, economics, offers)

Checker: K1 · 2026-11-23 · Brief: briefs/K1.md (refute, don't confirm).
Tools used:
- Meta Ad Library API (`mcp__facebook__ads_library_search`, client_conversation_id Sn0reW0menRes2611Ab): 30 fresh queries, keyword and page-scoped, for GB / AU / NZ (+US to identify pages).
- Headless Playwright renders of 17 Ad Library snapshots, for body text. Script and output are in scratchpad/k1raw/.
- Firecrawl: Amazon UK/AU search pages, 12 competitor pages and policies, 4 TGA ARTG records, 2 searches.
- Shopify `.js` product JSON (curl) for 10 stores.
- openFDA 510k and registrationlisting (curl).
- A live FX rate (open.er-api.com).
- Python recomputation of every KPI cell and of the Google-Trends block averages from the raw provider JSON.

Fixes: verify/fix_K1.json, 15 exact replacements. Each `old` string occurs exactly once in the current docs (dry run checked). None of them overlaps fix_K2.json. I did not edit the docs.

**Totals: 62 claim lines checked · 52 CONFIRMED · 8 CORRECTED (#7, 10, 25, 28, 29, 30, 52, 59 → 15 text replacements; 3 of them are upgrades that mark ARTG numbers as DB-verified) · 2 UNVERIFIABLE (#27, #62), plus 1 sub-claim (the live UK "snoring mouth guard" 1,600+ badge sum).**

**Headline: no women-first mouthpiece advertiser was found in AU or NZ beyond Honex's one women-label ad. The wedge's "uncontested in AU/NZ" (CONDITIONAL) verdict survives.**
- The corrections are about competitor counts and coverage:
  - Honex has a second page.
  - 4 AU mouthpiece and tongue-device advertisers were missing from the AU list.
  - SnoreMedic does advertise in AU.
  - The menopause-airway "why" has been seen once in AU, on a non-mouthpiece ad.
- The economics have no arithmetic errors.

Format: claim · doc+section · verdict · URL · note

## 1. Wedge and gate (doc1 §1, §2, LOCK; doc4 §15 A)
1. AirVex/Uk Sleep Forum runs 186 "menopause" / 325 "women" active GB ads · D1 §1 TAKEN map, §2 · CONFIRMED · Meta API, page 1266231016574537, GB, ACTIVE, terms "menopause" and "women" · The estimated counts are exactly 186 and 325 today. Top ads are titled "Menopause Snoring?" (e.g. https://www.facebook.com/ads/library/?id=917610098009198).
2. AirVex total GB 1,271 · D1 §0B, §1 · CONFIRMED · same page, GB, ACTIVE · 1,276 today, which is drift and needs no fix.
3. AirVex women angle "since 23 Oct 2026" · D1 §1, §2 · CONFIRMED (earliest found) · https://www.facebook.com/ads/library/?id=2160609094834247 (adlog) · The API can't sort oldest-first, so an earlier start can't be ruled out. Note only.
4. AirVex 0 ads in AU/NZ · D1 §2 gate · CONFIRMED · page 1266231016574537, AU+NZ, ALL statuses = 0.
5. SnoreSolvers 0 GB / 0 AU · D1 §1, §2 · CONFIRMED · page 436160256252945 (GB, AU) = 0; its persona page "Better Sleep Daily" 693087250565441 = 0 in AU, GB and NZ · The US menopause ads ("How I fixed my snoring after Menopause") run only outside our regions.
6. Beauty Sleep 341 GB / 540 AU / 391 NZ · D1 §0B, §1; D4 §15 · CONFIRMED · page 492545827284520, ACTIVE · 342 / 541 / 392 today.
7. "Honex 202 active AU ads" (also 201 in D1 §1/§0B) · D1 Audit §1 re-check, §0B, §1, LOCK; D4 §15 A · **CORRECTED** · Meta API, AU, ACTIVE: page 1155262701012872 = 203, plus the second Honex page 945981008608521 = 32 → **~235**; NZ 184 + 32 = **216** · The GB figure (242) already adds both pages, so AU/NZ were undercounted. The conclusion gets stronger: the women ad is 1 of ~235. Fixes 1, 5, 6, 8, 10.
8. AU/NZ: no women-first mouthpiece except Honex's ONE women-label ad · D1 §2, LOCK · CONFIRMED (refutation attempt failed) · Queries run in AU and/or NZ, ACTIVE: "snoring women mouthpiece", "menopause snoring", "women snore", "perimenopause snoring", "she snores", "ladies snoring", "snoring wife", "anti snoring mouth guard", "snoring mouthpiece" (NZ), "snoring" (NZ), plus page-scoped "women" on both Honex pages · Every snoring advertiser surfaced was rendered and read. None is a women-first mouthpiece:
   - HiZuu: tongue device, unisex.
   - "Slublonin Gritmultlades": Waxlify, a Honex clone, "so did my wife".
   - "Dr. Sofie Laursen": male CPAP story, snorefree.au.
   - Histrips: nasal strips for the partner of a snorer.
   - Modern Health Lab / Avanera: unisex mouthpiece.
   - SnoreMedic: unisex/partner.
   - Ray Whitfield / Jennifer Miller: getduvella.com CPAP advertorial.
   - Snoring Health Forum: wedge pillow.
   - Jen Walsh: grounding sheet, about HER husband's snoring.
   - Clean Home Review: dust-mite cards.
   - Noosa Mum: menopause tea.
   - My NUMY: vibrator.
   - Honex page A: 0 "women" ads.
9. Honex women ad 2922841231402680 still active in AU · D1 §1, §2 · CONFIRMED · https://www.facebook.com/ads/library/?id=2922841231402680 (returned by the AU and Honex+"women" queries today).
10. "The women-specific 'why' (menopause → airway muscle tone) … AU: not seen" · D1 §2 gap 2 · **CORRECTED** · https://www.facebook.com/ads/library/?id=1165313076190182 · Myo Munchee (AU, AUD, active since 16 Nov 2026, <100 impressions) runs a podcast promo: "as oestrogen changes through menopause, changes in muscle tone may also affect the muscles supporting the upper airway. For some women, things like … snoring …". It is not on a mouthpiece offer, so the gap holds, but "not seen" is wrong. Fix 7.
11. Snoring Health Forum menopause story in AU/NZ since 19 Nov 2026, sells a wedge pillow · D1 LOCK · CONFIRMED · ids 2778815335854291 etc. (AU query "snoring women mouthpiece", currency GBP, started 2026-11-19).
12. Honex women ad = generic fit claim, no menopause/spare room · D1 §2 · CONFIRMED (re-read via gate snapshots; no new copy found).

## 2. "The market is real" (doc1 §0, §0B)
13. UK women 40–60 = 9,536,916 (ONS mid-2025) · D1 §0 · CONFIRMED · data/ons_uk_female_40_60_nomis.csv (Nomis NM_2002_1) · I re-summed the 21 single-year rows and they match exactly.
14. AU women 40–60 = 3,644,987 (ABS ERP 2026-Q1) · D1 §0 · CONFIRMED · data/abs_au_female_40_60_erp.csv · I re-summed and it matches.
15. 9,536,916 × 14% / 25% = ~1.3M / ~2.4M · D1 §0 · CONFIRMED · 1,335,168 / 2,384,229 (arithmetic).
16. 3,644,987 × 17% = 619,648 · D1 §0 · CONFIRMED · 619,647.8 (arithmetic). The rate sources themselves are K2's scope.
17. GB "snoring" 52-wk averages 51.2→53.4→56.1→51.0→54.5, STABLE · D1 §0B · CONFIRMED · data/trends/firecrawl_trends_raw_GB_AU_US_5y.json · My recompute gives 51.3/53.5/55.9/51.1/54.7. The small gap is block alignment.
18. AU "snoring" 70.7→…→73.3 STABLE · D1 §0B · CONFIRMED · same · 70.9/74.8/75.1/71.3/73.0.
19. US 58.8→74.1, +16% · D1 §0B · CONFIRMED · same · 63.7→74.1 = +16.3%.
20. Mouth tape GB 38.4→20.3 (−47% YoY); AU 67.4→59.4 · D1 §0B · CONFIRMED · producterms JSON · 38.2→20.3 (−47%); AU 67.8→59.1. The peak weeks match.
21. Nasal strips GB 5.6→13.2; AU 5.4→34.6 · D1 §0B · CONFIRMED · same · 5.6→13.2; 5.4→34.3.
22. "snoring women" below threshold 250/262 GB weeks; "anti snoring mouthpiece" 241/262 · D1 §0, §0B · CONFIRMED · exact no-data week counts.
23. Peak months GB Jan 63.2 / Feb 64.4 / Dec 59.1 (trough Jun 44.5); AU Jul 88.4 / Aug 86.4 / Jun 83.0 (trough Feb 58.4); US Feb 73.0 / Jan 71.5 · D1 §0B · CONFIRMED · same · Exact match.
24. amazon.co.uk "anti snoring mouthpiece" ~2,400+/month, 0 women-only listings · D1 §0B · CONFIRMED · https://www.amazon.co.uk/s?k=anti+snoring+mouthpiece · The top-8 sum is 2,400+. The full page 1 sums to about 2,750+ (a lower bound either way). No women-only listing; the only "women" titles are "Men & Women".
25. "snoring mouth guard": Snoreeze 3.1★ 1.1K; "every other mouthpiece ≤61 ratings" · D1 §0B · **CORRECTED** (overstated) · same URL as #24 · On the same-day UK page 1, TheSleepGuard's anti-snore guard has 1K ratings and Somnofit-S 1.5K. "≤61" holds only within that query's top 10. Fix 9.
26. amazon.com.au "anti snoring mouthpiece" 400+, top slots sponsored strips/tape · D1 §0B · CONFIRMED · https://www.amazon.com.au/s?k=anti+snoring+mouthpiece · Mouthpiece badges are 100+, 200+, 100+ and 50+ (≥450). The first slots are sponsored Breathe Right strips.
27. GB keyword counts (820 / 6,802 / 877 / 3,568 / 261) · D1 §0B · UNVERIFIABLE (live drift) · Meta API · I didn't re-run each one: they are fuzzy estimated_total_count values and change hourly, and nothing rests on the exact figure.
28. "AU: 8 confirmed (… Honex 201 …)" · D1 §0B · **CORRECTED** · Meta API, AU, ACTIVE, page-scoped · The list misses 4 advertisers, and Honex is two pages (235):
   - SnoreMD: 33 (page 130493594295391).
   - Modern Health Lab / Avanera Pro: 42 (page 1004212102781463). This is a QuietLab Pro rebrand; the tryavanera.com image is named "QuietLab_Pro_Sales_Page".
   - HiZuu SnoreSnoozer tongue device: 16 (page 266144636730650; ad 1680943129611036 has run since 3 May 2026, 204 d).
   - SnoreMedic: 2.
   None is women-first. Fix 2.
29. QuietLab region "US" only (US 181 · GB 0) · D1 §1 long-list · **CORRECTED** · https://www.facebook.com/ads/library/?id=3024059601291216 · Its page "Modern Health Lab" runs 42 active AU ads. Fix 3.
30. SnoreMedic "≥1 (US-reached) · 117 d" (D1) / "no AU Meta page found" (D4 §15) · D1 §1, D4 §15 A · **CORRECTED** · https://www.facebook.com/ads/library/?id=1686206309083131 · Page 506129352576752 has 2 active AU ads (AUD), one since 3 Jun 2026 (173 d). The ad promises "📦 Free shipping both ways", but the live refund policy says "all shipping costs associated with the return are at your expense" (https://snoremedic.com.au/policies/refund-policy). Fixes 4, 14.
31. Longest-running seen: Zcomfort 447 d; Honex 194 d · D1 §0B, §1 · CONFIRMED (as "seen") · Zcomfort ad 1348613710203858 (from 2025-09-15) is still returned as ACTIVE in AU today. HiZuu's 204-day AU ad (#28) beats Honex's 194 d. That is covered by fix 2, and the label "longest *seen*" stays honest.

## 3. Economics (doc1 Pre-0; doc4 §15 re-run)
32. FX 1 AUD = 0.50690108 GBP · D1 Pre-0, D4 §15 · CONFIRMED · https://open.er-api.com/v6/latest/AUD → 0.506932 (23 Nov 2026 00:02 UTC).
33. AUD/USD 1.50359 (Shopify presentment) · D4 §15 · CONFIRMED · same → 1.5070 (within 0.3%).
34. Real supplier price used, not the welcome-deal teaser · D1 Pre-0 · CONFIRMED · The table uses CJ A$20.57 landed (the higher, conservative cost). The AliExpress line uses A$14.37 (the brief), inside the non-teaser A$13.90–16.71 cards; the A$1.49 "new shopper" price is explicitly ignored.
35. Pre-0 KPI table, all 44 cells (CM $, CM %, BE ROAS, BE CPA, kill/scale CPA and ROAS × 4 variants) · D1 Pre-0 · CONFIRMED · Recomputed. For example, AU single: 89 − 20.57 − 2.67 = 65.76; 73.9%; 1.35; 47.96 / 1.86; 39.06 / 2.28. UK 2-pack: 69 − 20.854 − 2.07 = 46.08; 66.8%; 1.50; 32.28 / 2.14; 25.38 / 2.72. Every cell matches to the cent.
36. AliExpress scenario (CM % 80.9/72.8/82.1/75.9; BE 1.24/1.37/1.22/1.32; scale CPA 45.26/50.99/25.55/31.66) · D1 Pre-0 · CONFIRMED · all 12 values match.
37. 2-pack extra CM +A$8.53 / +£8.98 · D1 Pre-0 · CONFIRMED.
38. D4 §15 re-run table, 7 variants × 7 cells (incl. AU trio A$149: 82.82 / 55.6% / 1.80 / 53.02 / 2.81 / 38.12 / 3.91 and GB £59 pair: 36.38 / 61.7% / 1.62 / 24.58 / 2.40 / 18.68 / 3.16) · D4 §15 · CONFIRMED · all 49 cells match.
39. Refund line, 10% refunds with the device not recovered: CM A$56.86 / 62.39 / 67.92; BE 1.57 / 1.91 / 2.19 · D4 §15 · CONFIRMED · arithmetic. (Processing fees on refunded orders are ignored, which is immaterial.)
40. Post-purchase spare +A$17.26 (A$39) / +A$7.56 (A$29) / +£8.00 (£19) · D4 §15 · CONFIRMED.
41. AliExpress pair BE 1.37, trio 1.47 · D4 §15 · CONFIRMED.
42. Ladder maths: pair A$59.50/unit; Happy Sleep A$79.50 each; SnoreMedic A$63.96 each; +A$29 over Honex (≈A$60); £49 = 1.6× £29.99; A$119 ≈ US$79 · D4 §15 · CONFIRMED.
43. CJ £10.43/unit, AliExpress £7.28 · D1 Pre-0 · CONFIRMED · 20.57 × 0.5069 = 10.427; 14.37 × 0.5069 = 7.284.

## 4. Offers spot-check (doc4 §15; 12 competitors, GB + AU)
44. Happy Sleep A$87.99, 2-pack A$159, 30 nights, ARTG 230839, free AU shipping · D4 §15 A · CONFIRMED · https://www.happysleep.au/products/anti-snoring-mouthpiece(.js) · "$87.99 One-time purchase · free shipping … Try Happy Sleep for 30 nights … ARTG 230839"; `.js` 1 Pack 87.99 · 2 Pack 159.00.
45. Good Sleep Co A$139 (→ A$111.20 BF); 14 nights, worn OK, return postage paid by her · D4 §15 A · CONFIRMED · goodsleepco.health/products/hushd-avera.js (13900) + /policies/refund-policy: "within 14 nights of delivery — even if you've molded and worn it. Return postage is paid by the customer."
46. SnoreMD 30-day guarantee, "no need to return your device", ARTG 525206 · D4 §15 A · CONFIRMED · https://snoremd.com.au/ ("Try SnoreMD risk-free for 30 days … ARTG ID# 525206") + https://snoremd.com.au/30-day-money-back-promotion-terms-conditions/ (snippet: "no need to return your device").
47. SnoreMedic A$79.95 (A$159.95); 60 nights; she pays the return; original packaging · D4 §15 A · CONFIRMED · snoremedic.com.au/products/snoremedic-plus.js (7995/15995) + the refund policy quoted in #30.
48. Honex Women Edition US$39.95 (compare US$79.90) · D4 §15 A · CONFIRMED · honexcompany.com/products/w-the-quiet-anti-snoring-mouthpiece-universal-size.js (3995/7990).
49. Beauty Sleep AU A$39.90 (A$49.90); B2G2 A$79.80; 99 nights · D4 §15 A · CONFIRMED · beautysleepclub.com/products/beauty-sleep-mouth-tape.js (3990/4990); homepage "Buy 2, Get 2 FREE … $79.80 … 99-night money-back guarantee" · The B2G2 compare-at shows A$227.50 on the homepage card vs A$273.50 in the doc. That is anchor drift; no fix.
50. AirVex £59.99 → £29.99; 60 days incl. opened, "dispose of it responsibly at home" · D4 §15 B · CONFIRMED · airvex.shop/products/airvex-pro%E2%84%A2-1.js (5999) + https://www.airvex.shop/policies/refund-policy ("we voluntarily extend our 60-Day Satisfaction Guarantee to opened items … You do not need to send the product back … dispose of it responsibly at home").
51. Feliora £33.69 / B2G2 £49.94 (£107.80); used/opened cannot be returned · D4 §15 B · CONFIRMED · feliorauk.com/products/feliora-anti-snoring-mouthpiece.js + https://feliorauk.com/pages/return-refund-policy ("products that have been used or had their packaging opened cannot be returned").
52. Hushly £29.95 (£39.95), BOGO £39.95, FDA APPROVED claim, 60-day guarantee · D4 §15 B · **CORRECTED** (BOGO tier) · https://hushlystore.com/products/hushly%C2%AE-anti-snoring-mouthpiece (live, GB) · Single £29.95 (£39.95) is confirmed, and so are B2G2 £59.90 and B4G4 £119.80, "FDA APPROVED!" and the 60-Day guarantee. But the 2-item tier now reads "£29.95 £79.90", not £39.95. Fix 15.
53. The Soothie £30.50 (£74) · D4 §15 B · CONFIRMED · thesoothie.com/products/anti-snoring.js (3050/7400).
54. SleepPro Easifit £39.99; 2 for £59.98; + Chin Strap £54.98 · D4 §15 B · CONFIRMED · sleeppro.com/products/sleeppro-easifit.js.
55. Zcomfort £29.99 (£58.99); B2G1 £56.99; + SmartWatch £51.99; + Mask £47.00 · D4 §15 B · CONFIRMED · zcomfort.co/products/zcomfort.js.
56. "Almost every GB 60-day guarantee is void once opened" / "7 of 11 GB" · D4 §4, §15 offer inputs · CONFIRMED · The Feliora, AirVex (the exception) and Honex policies were re-opened; for the rest I re-read the saved policy captures. 7 of 11 is right. SleepPro Woman ("original packaging") could arguably make it 8. AirVex is the one GB seller that covers opened devices.
57. "AU: nobody combines 60 nights + opened/worn covered + no cost to her" · D4 §15 · CONFIRMED · These are the closest, and none has all three:
   - SnoreMD: 30 days, extendable; no return.
   - SnoreMedic: 60 nights, but she pays the return and must send the packaging, and its ad claims free shipping both ways.
   - Good Sleep: 14 nights, worn OK, she pays postage.

## 5. Certifications (data/competitor_certs.md; doc4 §15) and ARTG/FDA numbers
58. ARTG 230839 (Happy Sleep): Sleep Sound Pty Ltd, MAD, Class 1, since 19 Nov 2014 · D4 §15 · CONFIRMED · https://www.tga.gov.au/resources/artg/230839.
59. ARTG 525206 (SnoreMD), 315118 (SleepDoctor), 156350 (Ripsnore), marked "page-shown; not DB-checked" · D4 §15 · CONFIRMED + **CORRECTED** (upgraded to verified) · Details:
   - 525206 (https://www.tga.gov.au/resources/artg/525206): APAC Health and Medical Distributors Pty Ltd, MAD; manufacturer AMEC Plastics; Class 1; since 1 Apr 2026.
   - 315118 (https://www.tga.gov.au/resources/artg/315118): United Pacific Industries Pty Ltd, MAD; manufacturer Passion For Life Healthcare (UK), the Snoreeze maker; Class 1; since 5 Mar 2019.
   - 156350 (https://www.tga.gov.au/resources/artg/156350): Ripsnore Pty Ltd, "Antisnoring device"; manufacturer 2Brasil Trade; Class 1; since 29 Oct 2008.
   All three are status A. Fixes 11–13.
60. 510(k) numbers: K181396, K231138, K252161, K232025, K201719, K170825, K253868, K180124, K213088, K190058, K233850, K253355, K061688, K121761, K132506 · D4 §15, certs · CONFIRMED · https://api.fda.gov/device/510k.json?search=k_number:<K> · All 15 exist, all product code LRK, and the applicant and device names match the certs file:
   - Passion For Life = Oral Device.
   - Oscimed = Anti-Snore Mouthguard+.
   - Good Sleep CO Pte = Hushd Avera / Hushd Pro Avera.
   - Snore Reliever Co = Vital Sleep.
   - Apnea Sciences = SnoreRx.
   - QuietLab LLC = QuietLab Pro.
   - Sleeping Well = ZQuiet / ZQuiet Advance.
   - Sleep Science Partners = PureSleep.
   - Fissiontech = Difiney ×2.
   - Tomed ×2.
   - Michael D Williams DDS = "SLEEPPRO" brand.
   The listing for K231138 includes SNORELESSNOW LLC (FEI 3027579589).
61. Hushly "FDA APPROVED" and Zcomfort "FDA-cleared" have no clearance; SnoreMeds and AirVex/Honex have none either · certs, D4 §15 · CONFIRMED · openFDA 510k (device_name / applicant) and registrationlisting (proprietary_name) all return NOT_FOUND.
62. UK PARD entries (Snoreeze Class I; SomnoGuard UKRP PMF Consultants) · certs · UNVERIFIABLE by K1 · I did not re-query PARD (a JS app); I rely on the cert agent's saved JSON in data/certs/pard/. MHRA is K2's regulatory scope.

UNVERIFIABLE (2 + 1 sub-claim): #27 (live keyword estimates drift), #62 (PARD not re-queried), and the 1,600+ badge sum in the UK "snoring mouth guard" Amazon row. A live re-fetch (stealth proxy) returned a non-localised page with no badges, so the 1,600+ figure couldn't be reproduced live; it stands on the agent's 08:4x capture.

## So What → do this
- The wedge verdict holds: a women-first mouthpiece in AU/NZ is still Honex's single generic ad. My hardest refutation attempt found only other categories (pillow, tea, grounding sheet, strips, tongue devices) or unisex mouthpieces.
- Apply fix_K1.json. The Honex AU count should read ~235 across 2 pages, and the AU competitor list should add SnoreMD, Avanera/QuietLab, HiZuu and SnoreMedic.
- Add Myo Munchee to the weekly AU re-check list, because it is the first AU advertiser putting "menopause → airway muscle tone → snoring" in front of women. Add HiZuu too (a 204-day AU runner).
- The economics are clean. The only open items are the ones the docs already flag: CJ destination, refunds, gifts, VAT/GST.

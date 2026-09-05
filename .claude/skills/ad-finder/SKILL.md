---
name: ad-finder
description: >-
  Hunts the best, LONGEST-RUNNING winning ads from 7–8 figure stores in a given niche, using BOTH
  Winning Hunter AND the Facebook Ad Library, and drops each one as a row (link + metadata) into
  Nikita's Notion "Ad Finds — To Review" database for weekly review. This skill ONLY finds and logs
  ads — it does not tear them down (the ad-skeletonizer skill does that after Nikita approves rows).
  Can hunt by NICHE, by ad CONCEPT/format (storytelling, VSL, listicle, street interview, UGC
  testimonial, founder story, etc.), or both. Use whenever Nikita wants to find or hunt winning/proven
  ads, fill his ad-finds list, or discover long-running ads — phrasings like "find winning ads in
  [niche]", "hunt [concept] ads", "find the best VSLs in [niche]", "get me storytelling ads",
  "fill my ad finds", "what's been running forever in [niche]". Before hunting it asks a couple of
  intake questions (concept + niche + depth) to sharpen the search. Longest run time is the #1 filter —
  an ad running for months is a proven money-maker.
---

# Ad Finder

The first half of Nikita's swipe pipeline. This skill fills the **"Ad Finds — To Review"** Notion database with proven, long-running ads — by niche, by ad concept, or both — so he can eyeball them and approve the good ones. `ad-teardown` then tears down what he approves. Keeping find and teardown separate lets Nikita QA the finds before spending time (and Winning Hunter credits) tearing them down. (For a hands-off, one-command run of the whole chain — find → teardown → file — he uses the `swipe-pipeline` skill, which reuses this skill's hunt logic.)

**This skill does NOT tear ads down or write skeletons.** It finds, logs a link + metadata, and stops. Resist the urge to analyze the creative here — that's the next skill's job.

## The one rule that matters: longevity = profit

Nobody keeps paying to run a losing ad. So the strongest signal of a winner is **how long it has been running**. Rank everything by run length; a boring ad running 6 months beats a flashy one running 6 days. This is the whole filter.

## Step 1 — Intake (ask first, then hunt)

Sharpen the search before spending calls. Unless Nikita already gave these in his message, ask with **one `AskUserQuestion`** (batch the questions, don't drip them):

1. **Concept** — what ad format to hunt: Storytelling / Personal Story · Long-form VSL · UGC Testimonial · Listicle ("X reasons") · Street Interview · Founder Story · Demo/Unboxing · Myth-Buster · **Any format**. (This maps to the *Video Ad concepts* genres and becomes the Video Format when it's later filed.)
2. **Niche** — niche / product / keyword (e.g. neuropathy, pet odor, eczema). Accept "any / surprise me."
3. **Depth** — how many to log (default 10–15; the finder is cheap — over-collect, he filters).

Optional 4th only if unclear: **must still be active?** (default: prioritise still-active long-runners, but a proven ad that recently went dark still counts).

Confirm one line and go: `Hunting longest-running [concept] ads in [niche] across Winning Hunter + FB Ad Library → Ad Finds — To Review.`

## Step 1b — Concept → hunt recipe

Translate the chosen concept into concrete `search_facebook_ads` filters + how to confirm it from the creative. Always keep `sort_by=longestrunning`, `sort_order=desc`, `media_type=videos` (except image-heavy concepts). If concept = **Any format**, skip the concept filters and hunt purely on niche + longevity.

| Concept | Filters to add | Keyword cues (searchkeyword=adtext) | Confirm from creative |
|---|---|---|---|
| Storytelling / Personal Story | `min_copy_length` ~250 | "my", "I", "years ago", "story", "changed my life" | first-person narrative arc in transcript |
| Long-form VSL | `min_video_length` 180; often `page_type=funnels` | "watch", "presentation", "discovered" | video ≥3 min, advertorial/funnel LP |
| UGC Testimonial | short/mid video | "I tried", "I've been using", "obsessed" | selfie/handheld talking head |
| Listicle ("X reasons") | — | "reasons", "things", "ways", numeric | numbered on-screen list |
| Street Interview | — | "asked", "stopped people", "on the street" | interviewer + public |
| Founder Story | `min_copy_length` ~250 | "I started", "I founded", "our founder" | founder narrator |
| Demo / Unboxing | video | "how it works", "watch this", "unboxing" | product demo B-roll |
| Myth-Buster | — | "myth", "stop doing", "you're wrong", "lie" | claim → correction structure |

The concept is a **filter + a confirmation check**, not a guarantee — verify each kept ad actually IS that concept (scan the copy/creative) before logging; drop ones that don't match. Record the confirmed concept in the row's **Notes** (e.g. "Concept: Long-form VSL") so the teardown files it under the right Video Format.

## Step 2 — Hunt both sources

Load `winning_hunters` and `facebook` tools via ToolSearch if not present.

**Winning Hunter:**
- `find_winning_products` — trending winners in the niche → the stores behind them.
- `search_shopify_stores` / `find_similar_stores` — bigger stores in the niche.
- `get_store_details` — **confirm 7–8 figure revenue.** Only log ads from proven operators; drop small stores.
- `get_store_top_ads` — a store's top ads (Meta / TikTok / Google).
- `search_facebook_ads` — search the niche/angle; scan for the **oldest first-seen / longest run time**.

**Facebook Ad Library** (`ads_library_search`):
- Search the niche keyword or a specific store's page.
- The Ad Library shows each ad's **"Started running on" date** — the cleanest longevity signal anywhere. Prioritise the oldest ads that are **still active**.

## Step 3 — Rank, then log rows

Rank the pool by: **run length (primary) → store revenue tier → number of variations the store runs of the same structure** (many variants = they've scaled it = it works). Take the top N.

For each, append a row to the **Ad Finds — To Review** database.
- Data source: `collection://32981cf7-fc4d-4e06-a849-5f6173a312a6` (parent: Ad Swipe File). **Fetch the data source first** to confirm the live schema before writing (schemas change; never write from a cached ID blind).
- Fill: **Name** (short label, e.g. "PetLab — dog itch UGC"), **Link** (see below — must be a working link), **Store**, **Niche**, **Platform** (Meta/TikTok/Google/FB Library), **Run Length** (e.g. "running since Jan 2026 — 8 months"), **Revenue** (store tier, e.g. "~$1.2M/mo"), **Date Found** (today), **Status = New**, **Notes** (start with `Concept: [concept] ·` then the hook line + FB advertiser-page backup link).

**The Link must open ONE individual ad — this is the #1 thing to get right (confirmed broken twice).** Two hard facts learned the hard way:

  1. WinningHunter's `productid` is **NOT** a Facebook Ad Library archive ID — `facebook.com/ads/library/?id=<productid>` is a dead "ad isn't on Facebook" link.
  2. Facebook Ad Library **no longer isolates a single ad at all.** Even a *real* archive ID (`?id=<real_library_id>`) now renders the advertiser's entire grid ("~460 results"), not one ad. And `view_all_page_id=<page_id>` is a pure advertiser list with no target ad. Neither gives Nikita the one ad he wants.

  **So log the WinningHunter single-ad share URL** — it opens exactly one ad, and Nikita is logged into WH:

  `https://app.winninghunter.com/ad/<productid>?platform=meta`

  Use the specific target ad's `productid` (the longest-running creative for that store). This is also a link the ad-teardown skill accepts directly. Put the store's FB Ad Library page (`…view_all_page_id=<page_id>`) and the ad's start date + hook in **Notes** as a backup reference. Never log a bare `facebook.com/ads/library/?id=…` link — it will not show a single ad.
- **Dedup:** before adding, query the database for the Link; if it's already there, skip it (don't create duplicate rows). Since the Link is now per-advertiser, also skip if the same **Store** is already logged for this niche unless it's a genuinely different product/angle.

## Step 4 — Report

One line per ad logged: label · run length · store revenue · link. Then a summary: "Logged N new finds to Ad Finds — To Review. Review them and set the good ones to Approved; then run ad-teardown's 'process my approved finds'."

## Guardrails
- **7–8 figure stores only** — confirm with `get_store_details` before logging. A long-running ad from a tiny store is noise.
- **Longevity over virality** — a viral one-off is not proven; a long-running ad is.
- **Never invent run length or revenue.** If you can't confirm, write "unconfirmed" rather than a made-up number — the whole point is that Nikita trusts these are real winners.
- **Don't tear anything down here.** Link + metadata only. Stop at the row.

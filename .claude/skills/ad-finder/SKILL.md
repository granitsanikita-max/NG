---
name: ad-finder
description: >-
  Hunts the best, LONGEST-RUNNING winning ads from 7–8 figure stores in a given niche, using BOTH
  Winning Hunter AND the Facebook Ad Library, and drops each one as a row (link + metadata) into
  Nikita's Notion "Ad Finds — To Review" database for weekly review. This skill ONLY finds and logs
  ads — it does not tear them down (the ad-skeletonizer skill does that after Nikita approves rows).
  Use whenever Nikita wants to find or hunt winning/proven ads, fill his ad-finds list, or discover
  long-running ads in a niche — phrasings like "find winning ads in [niche]", "hunt ads for [product]",
  "fill my ad finds", "find long-running ads from big stores", "what's been running forever in [niche]".
  Longest run time is the #1 filter — an ad running for months is a proven money-maker.
---

# Ad Finder

The first half of Nikita's swipe pipeline. This skill fills the **"Ad Finds — To Review"** Notion database with proven, long-running ads so he can eyeball them weekly and approve the good ones. The second skill (`ad-skeletonizer`) then tears down only what he approves. Keeping find and teardown separate lets Nikita QA the finds before spending time (and Winning Hunter credits) skeletonizing.

**This skill does NOT tear ads down or write skeletons.** It finds, logs a link + metadata, and stops. Resist the urge to analyze the creative here — that's the next skill's job.

## The one rule that matters: longevity = profit

Nobody keeps paying to run a losing ad. So the strongest signal of a winner is **how long it has been running**. Rank everything by run length; a boring ad running 6 months beats a flashy one running 6 days. This is the whole filter.

## Step 1 — Scope

Get from Nikita (ask only if missing): the **niche / product / keyword** to hunt, and **how many** to log this run (default 10–15 — the finder is cheap; over-collect, then he filters). Confirm one line and go:
`Hunting longest-running ads in [niche] across Winning Hunter + FB Ad Library, logging to Ad Finds — To Review.`

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
- Fill: **Name** (short label, e.g. "PetLab — dog itch UGC"), **Link** (see below — must be a working link), **Store**, **Niche**, **Platform** (Meta/TikTok/Google/FB Library), **Run Length** (e.g. "running since Jan 2026 — 8 months"), **Revenue** (store tier, e.g. "~$1.2M/mo"), **Date Found** (today), **Status = New**.

**The Link must actually open — this is the #1 thing to get right (confirmed broken once).** WinningHunter's `productid` is **NOT** a Facebook Ad Library archive ID. Building `facebook.com/ads/library/?id=<productid>` produces a dead "this ad isn't on Facebook" link. Do not do it. Instead, log the **advertiser's Ad Library page**, built from the ad's `page_id`:

  `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=<PAGE_ID>`

  This always resolves and shows every ad that advertiser is running (the winner will be near the top by longevity). Put the specific ad's identifying details — start date, hook line, format — in **Notes** so the exact creative is findable on that page (the ad-teardown skill's browser pull then binds to the specific ad by its real `deeplink_ad_archive` id). For a Winning Hunter link, use the `app.winninghunter.com/ad/<id>` share URL instead — that one resolves inside WH. Never invent or guess a `?id=` archive link.
- **Dedup:** before adding, query the database for the Link; if it's already there, skip it (don't create duplicate rows). Since the Link is now per-advertiser, also skip if the same **Store** is already logged for this niche unless it's a genuinely different product/angle.

## Step 4 — Report

One line per ad logged: label · run length · store revenue · link. Then a summary: "Logged N new finds to Ad Finds — To Review. Review them and set the good ones to Approved; then run ad-teardown's 'process my approved finds'."

## Guardrails
- **7–8 figure stores only** — confirm with `get_store_details` before logging. A long-running ad from a tiny store is noise.
- **Longevity over virality** — a viral one-off is not proven; a long-running ad is.
- **Never invent run length or revenue.** If you can't confirm, write "unconfirmed" rather than a made-up number — the whole point is that Nikita trusts these are real winners.
- **Don't tear anything down here.** Link + metadata only. Stop at the row.

---
name: ecom-radar
description: >
  Daily X (Twitter) ecom intelligence for Nikita. Pulls the last day's
  dropshipping / ad-creative / store / product-research posts, throws out
  guru-bait and flexing, scores what's left for "can I actually do this
  today," hands back a short Do-Today list, and files every genuinely new
  tactic into a compounding knowledge log. Trigger on "/ecom-daily", "run
  the ecom radar", "what's new in ecom on X today", or any request to scan
  X for fresh dropshipping/marketing tactics.
---

# ecom-radar — daily X ecom intelligence

Turns the firehose of daily ecom X posts into (1) a short list of things
worth doing today and (2) a knowledge log that compounds so Nikita is always
picking up NEW tips, never re-reading the same ones.

Nikita's filter (everything is judged against this): he runs AI dropshipping
— sources trending China products, builds a store brand, makes the ads. His
priorities are **running dropshipping brands from scratch**, **mastering ad
marketing (Meta/TikTok UGC creative)**, and **systematizing onboarding**. If
a post doesn't move one of those, it doesn't make the cut.

## The engine (how it fetches X here)

This environment has **no X login and no agent-reach CLI**. Do not try
`twitter`, `opencli`, or `agent-reach` — they aren't installed. Fetch with
**Firecrawl** (`mcp__Firecrawl__firecrawl_search`), which surfaces the X posts
that actually got indexed/traction — which is what we want, not literally
every post.

- Site-filter with `includeDomains: ["x.com","twitter.com"]`.
- Recency with `tbs` from config (`qdr:d` = last 24h; fall back to `qdr:w`
  if a query returns nothing).
- **EXACT POST LINKS ONLY.** Every link handed to Nikita or written to the
  knowledge log / Notion page MUST be a direct post URL — the
  `x.com/<user>/status/<id>` (or `x.com/i/status/<id>`) form. NEVER a bare
  profile (`x.com/handle`), a `/with_replies`, `/reposts`, or `?lang=` URL —
  he should click and land on the exact post, not scroll a profile. If a
  search hit is only a profile/reply URL, run another search for that post's
  text to resolve the `/status/` link. If you genuinely can't resolve the
  exact post, drop the item rather than ship a profile link. Strip tracking
  params and `/photo/1` suffixes down to the clean `/status/<id>`.
- To read a full thread (not just the search snippet), fetch the post URL
  with `mcp__Firecrawl__firecrawl_search` `related:` / or `WebFetch` the URL.
  Only do this for posts that pass the first-pass filter — don't fetch bodies
  for stuff you're going to reject anyway.

## Pipeline (run in order)

1. **Load config** — `.claude/skills/ecom-radar/config.yaml`. Use its
   queries, recency, limits, domains.
2. **Load memory** — read `ecom-radar/knowledge.md`. This is the dedupe set:
   anything already logged is NOT new, skip it in the output.
3. **Pull** — run every query in config, site-filtered, at the config
   recency. Batch the calls (independent → parallel). Collect all hits.
4. **First-pass filter** — drop anything matching `reject_signals` in config
   (course shills, income flexing, mindset fluff, engagement bait, or already
   in knowledge.md). Be ruthless — most of X ecom is noise. A post survives
   only if it names a concrete, testable tactic.
5. **Read bodies** — for survivors, read the full post/thread so you score
   the actual method, not the hook line. Prioritize `watch_accounts`.
6. **Score** each survivor 0–3 on each axis, sum (max 12):
   - **Actionable** — can Nikita do a concrete version of this today? (0 = vibe, 3 = step-by-step)
   - **Relevant** — hits dropshipping / ad creative / store / product / offer / scaling for HIS model
   - **Novel** — not already in knowledge.md, not a tactic everyone already knows
   - **Credible** — operator sharing real mechanics > anon flexing. Screenshots without method ≠ credible.
7. **Output the digest** (format below). **Do Today** = only score ≥ 8 AND
   Actionable ≥ 2. Cap at 5 — if fewer than 5 clear the bar, show fewer. Never
   pad with filler; a 3-item honest list beats a 5-item padded one.
8. **File to knowledge** — append every NEW distinct tactic (survivors, even
   the ones that didn't make Do-Today) to `ecom-radar/knowledge.md` so the
   dedupe set grows. Also save the full digest to
   `ecom-radar/digests/YYYY-MM-DD.md`.

## Output format (what Nikita sees)

```
# Ecom Radar — <date>
Scanned <N> posts across <M> queries. <K> survived the filter.

## 🔥 Do Today (<count>)
1. **<one-line tactic>**  — score X/12
   - What it is: <1 sentence, concrete>
   - Why it's worth it for you: <tie to dropshipping brand / ad creative / systematizing>
   - Do this: <the exact action — a test to run, a hook to steal, a page change>
   - Source: <x.com link> (@handle)

## 📌 Worth knowing (logged, not urgent)
- <tactic> — <one line> — <link>

## 🗑 Filtered out: <count> (guru bait / flexing / already known)
```

Keep it tight. Nikita's preference: direct, no fluff, specific to him. Don't
explain what dropshipping is. Don't hedge. If a day is genuinely dead, say
"slow day — nothing worth doing landed" rather than inventing tactics.

## Knowledge log format

`ecom-radar/knowledge.md` grows one bullet per distinct tactic, newest on top:

```
## <date>
- [<bucket>] <tactic in one line> — <the mechanism in 1 sentence> — src: <link>
```

The dedupe rule: before logging, check if the SAME mechanism is already there
(not just the same words). Two people saying "test 3 hooks per creative" is one
tactic, logged once.

## The "learn it yourself" mode

When Nikita says "learn this one" / "go deep on X" about a tactic from the
digest: read the full thread + any linked video (use the `watch` skill for
video, with his platform key) + the author's recent posts, then write a short
how-to into `ecom-radar/lessons/<slug>.md` — what it is, why it works, exact
steps to run it on his stack (Shopify + Meta/TikTok), and how to measure if it
worked. That turns a tip into something he can execute without re-researching.

---
description: Scan X for today's ecom/dropshipping tactics, rank the actionable ones, and log new ones.
---

Run the **ecom-radar** daily pipeline.

Invoke the `ecom-radar` skill and follow it end to end:

1. Load `.claude/skills/ecom-radar/config.yaml` and `ecom-radar/knowledge.md`.
2. Pull the last day's X posts for every configured query via Firecrawl
   (`mcp__Firecrawl__firecrawl_search`, site-filtered, recency from config).
   Run the query calls in parallel.
3. Filter hard (guru bait / flexing / mindset / engagement bait / already
   known), read the survivors' full threads, score them 0–12 on
   Actionable / Relevant / Novel / Credible.
4. Print the digest in the skill's format: **Do Today** (score ≥ 8 &
   Actionable ≥ 2, max 5), **Worth knowing**, and the filtered-out count.
5. Append every new distinct tactic to `ecom-radar/knowledge.md` (newest on
   top, dedupe by mechanism) and save the full digest to
   `ecom-radar/digests/<today>.md`.

Args (optional): `$ARGUMENTS`
- a bucket name (e.g. `ad_creative`) → only run that bucket's queries
- `week` → use `qdr:w` recency instead of `qdr:d`
- `learn <tactic>` → skip the scan, go deep on that tactic per the skill's
  "learn it yourself" mode and write a lesson file.

Keep the output tight and specific to Nikita's dropshipping/ad-creative work.
No fluff, no hedging. If the day is slow, say so — don't pad the list.

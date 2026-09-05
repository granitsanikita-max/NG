---
description: Scrape X + Reddit for everything people say about a product and return a voice-of-customer breakdown.
---

Run the **product-pulse** skill on the product in `$ARGUMENTS`.

If no product was given, ask for it in one line (generic name + brand/URL),
then proceed. Invoke the `product-pulse` skill and follow it end to end:

1. Expand the product into generic category term(s) + brand name(s) + the
   problem it solves.
2. Search X + Reddit across the config angles (reviews, worth-it, complaints,
   results, comparisons, problem-first). Run calls in parallel.
3. Filter out noise (keyword matches that aren't real buyers talking about
   this product), read the strongest Reddit threads' comments.
4. Cluster into the VoC buckets and output the breakdown in the skill's format,
   every claim backed by a real quote + EXACT permalink (no profiles/subreddits).
5. End with the **So what — angles this hands you** section.
6. Save the report to `product-research/<slug>-<date>.md` and give the path.

Keep it tight and specific. Quote real people, never invent quotes.

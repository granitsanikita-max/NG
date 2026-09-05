---
name: product-pulse
description: >
  Voice-of-customer research on a specific product for Nikita. Give it the
  product he's currently running and it scrapes X (Twitter) + Reddit for
  everything real people say about it — praise, complaints, objections,
  the exact words they use — filters out the noise, and returns one concise
  breakdown he can turn into ad angles and page copy. Trigger on
  "/product-pulse <product>", "what are people saying about <product>",
  "research this product", "run a pulse on <product>", or any request to
  find real customer chatter / reviews / complaints about a product.
---

# product-pulse — voice-of-customer research on one product

Feed it the product Nikita is running. It goes to **X + Reddit**, pulls what
real people say about it (good, bad, everything), strips the noise, and hands
back a tight breakdown organized so he can lift ad angles, hooks, objections
to preempt, and page copy straight out of it.

Why it matters for Nikita: the words customers already use are the highest-
converting ad copy and page copy that exist. Their complaints are the
objections his page must kill. Their dream outcome is his hook. This turns a
product into an angle bank.

## Engine (how it fetches here)

No X/Reddit login, no agent-reach CLI in this env. Use **Firecrawl**
(`mcp__Firecrawl__firecrawl_search`) — it reaches both. Both are confirmed
working.

- Reddit: `includeDomains: ["reddit.com"]` — the strongest channel (threaded,
  honest, long-form). NOTE: direct fetching is BLOCKED here — Reddit 403s
  `WebFetch` and `r.jina.ai`, and there's no scrape tool. So depth comes from
  running MANY targeted `firecrawl_search` queries: each result's description
  IS a real top comment, and the URL is the exact thread permalink. To go
  deeper on one thread, search quoted phrases from it (`"exact phrase"`) or
  its title — that surfaces more comments from the same thread. Budget for
  ~12-20 searches per product to build real depth, not 4.
- X: `includeDomains: ["x.com","twitter.com"]` — catches customer reviews and
  complaints but drags in noise (games, cars, unrelated "reviews"). Filter hard.
- No recency filter by default — old chatter is still valid VoC. Add `tbs`
  only if Nikita asks for recent-only.

## Input

The product Nikita gives. Before searching, expand it into a small term set —
this is the difference between shallow and deep research:
1. **Generic category term(s)** — what the thing actually is ("posture
   corrector", "red light mask", "car headrest pillow"). Dropship products
   sell under many brand names; the honest chatter lives under the generic
   term, so ALWAYS include it.
2. **Brand name(s)** it's sold under, if known (from Nikita or the product URL).
3. **The problem it solves** — the pain phrasing ("back pain slouching",
   "how to fix posture") — because buyers talk about the problem, not the SKU.

If the product is ambiguous, ask Nikita one line: generic name + the brand/URL.
Don't guess a product and burn a scan on the wrong thing.

## Pipeline

1. **Expand** the product into the term set above.
2. **Search WIDE — this is the whole point.** Nikita wants the AVERAGE of
   what everyone says, not one loud commenter. So gather a large sample:
   **run 25-45 searches minimum** (budget ~150-300 comment snippets after
   dedup). Each `firecrawl_search` result description is a real comment, so
   more searches = more comments. Hit every angle below, on BOTH X and Reddit,
   AND vary the phrasing (each rephrase surfaces different comments from the
   same and new threads):
   - `<term> review` / `<term> honest review` / `<term> real review`
   - `<term> worth it` / `does <term> work` / `is <term> a gimmick`
   - `<term> complaints` / `<term> problems` / `<term> scam` / `<term> waste of money` / `<term> returned it` / `<term> regret`
   - `<term> before after` / `<term> results` / `<term> life changing`
   - `<term> vs <alternative>` / `best <term> which one`
   - problem phrasing: `how to fix <problem>`, `<problem> what worked`, `<problem> desperate`
   - re-run the winners with the brand names and with each specific sub-audience
     term (e.g. crochet, gaming, arthritis, gift for mom).
   Run in parallel batches of ~4-5. If you hit HTTP 429, pause and continue —
   don't stop the sweep early. Do NOT declare the pulse done after 4-6
   searches; that's a sample of one opinion, which is exactly what Nikita said
   not to do. See `config.yaml` for the editable template and subreddit hints.
3. **Relevance filter** — drop anything that only keyword-matches but isn't
   about this product or its category (the X noise: game reviews, car reviews,
   LLM reviews, etc.). A hit survives only if a real person is talking about
   using / buying / considering THIS product or type of product.
4. **Dedup + aggregate — report the AVERAGE, not anecdotes.** Collect all
   comment snippets, dedup by thread+text. Then for each bucket, count how
   many DISTINCT comments express each theme and report it with rough
   frequency, not as one person's line:
   - Lead each point with the consensus + weight: "Most common complaint
     (~N of the ~M comments on this): …", "Recurring across K threads: …",
     "A minority (~X) say …".
   - Give an overall **sentiment split** at the top (rough % positive /
     mixed / negative) based on the sample.
   - Only AFTER the aggregated claim, back it with 1-2 representative verbatim
     quotes + exact links. Quotes illustrate the average; they are not the
     finding. Never build a bucket from a single comment — if only one person
     said it, label it "isolated, low signal" or drop it.
   State the sample size honestly ("based on ~N comments sampled across M
   threads"). If the sample is thin, say so rather than overclaiming a consensus.
5. **Cluster** everything into these VoC buckets:
   - **💚 What they love** — praise, results, delight, what over-delivers
   - **💢 Complaints / pain points** — what fails, breaks, disappoints, returns
   - **🤔 Objections before buying** — skepticism, "is it a scam", price, "does it really work", trust
   - **🎯 Why they buy / dream outcome** — the job-to-be-done, the after-state they want
   - **👤 Who it's for / use cases** — segments, situations, contexts
   - **⚖️ Alternatives they mention** — competitors, DIY, substitutes
   - **❓ Questions they ask** — unanswered ones = FAQ + ad-angle gold
   - **🗣 Their exact words** — verbatim phrases to lift into ads & page copy
6. **Output** the breakdown (format below), concise, each claim backed by 1-3
   real quotes with EXACT source links.
7. **So-what** — end with a short, punchy section: the 3-5 ad angles / hooks
   this research hands him, and the objections his page must kill. This is the
   payoff — don't skip it.
8. **Save + publish to Notion.** Save the full report to
   `product-research/<product-slug>-<date>.md` AND write it to the Notion page
   **"Comments from X"** (page id `3d2d5312-3cd6-8133-ae12-e2fc78d14bf6`) —
   this is the running home for all product-pulse research. Add each product as
   its own new section at the TOP of that page (`notion-update-page`,
   `insert_content`, `position: start`), newest first, so older reports stay
   below. Tell Nikita the local path and confirm it's on the Notion page.

## EXACT LINKS ONLY

Every link handed to Nikita or saved MUST be a direct permalink to the exact
post/thread/comment — `x.com/<user>/status/<id>`, `x.com/i/status/<id>`, or a
`reddit.com/r/<sub>/comments/<id>/...` thread/comment URL. NEVER a bare profile
(`x.com/handle`), a subreddit landing page (`reddit.com/r/<sub>`), a
`/with_replies` / `/reposts`, or a `?lang=` URL. He wants to click and land on
the exact thing, not scroll. If a hit only resolves to a profile/subreddit,
search its text to get the permalink, or drop it. Strip tracking params and
`/photo/1` suffixes to the clean permalink.

## Output format

```
# Product Pulse — <product>
Sample: ~<N> comments across <M> threads. Sentiment: ~<x>% positive / <y>% mixed / <z>% negative.

## 💚 What they love
- **Most common:** <theme> (~N of ~M) — "<representative quote>" — <exact link>
- <next most common theme, with weight> — <link>

## 💢 Complaints / pain points
- ...

## 🤔 Objections before buying
## 🎯 Why they buy / dream outcome
## 👤 Who it's for / use cases
## ⚖️ Alternatives they mention
## ❓ Questions they ask
## 🗣 Their exact words (copy-paste for ads & page)
- "<phrase>" — <link>

## 🚀 So what — angles this hands you
1. <ad angle / hook grounded in the research above>
2. <objection your page must kill, and how>
...
```

Nikita's style: direct, no fluff, specific. Don't pad a bucket to look full —
if there's nothing real for "alternatives", say "nothing notable" and move on.
Quote real people; never invent a quote. If a product is too niche and the
web is quiet, say so honestly rather than manufacturing chatter.

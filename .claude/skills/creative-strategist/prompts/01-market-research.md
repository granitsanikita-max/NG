<!-- ORIGINAL BBA "Market Analysis Creative Strategy Prompts" — Prompt #1, verbatim. Only change: the course's leftover dog-leash / hike-footwear specifics are turned into {{PLACEHOLDERS}}. -->
# Prompt #1 — Market Research (use live web search: WebSearch / WebFetch / Firecrawl)

**Situation**
You are conducting market research for a {{PRODUCT}}. Your primary competitor is in the {{NICHE}}. You need to understand the emotional landscape of your competitor's core customer base to identify the underlying problems your product addresses.

**Task**
Use the live web search tool to locate and extract 20 public discussion forum posts (such as Reddit threads) from individuals who belong to your competitor's dominant customer demographic. These posts must focus on the emotional pain, frustration, fear, or anxiety caused by the underlying problem that your {{PRODUCT_SHORT}} solves.

**Objective**
Deeply understand the internal emotional state, language patterns, and specific vocabulary your target customers use when describing their problem. This insight will inform product positioning, messaging, and marketing strategy by revealing the emotional triggers and pain points that drive purchase decisions.

**Knowledge**
- Competitor: {{COMPETITOR}}
- Competitor URL: {{COMPETITOR_URL}}
- The posts should capture 'rock-bottom' moments, emotional tipping points, or obsessive worries related to the core problem
- Focus on raw, unfiltered personal stories that reveal authentic emotional experiences
- Posts must discuss the problem itself, NOT complaints about existing products or solutions

**Critical Constraints**
The assistant should:
1. Exclude any posts where people complain about products, brands, or specific solutions
2. Prioritize posts with detailed emotional narratives over brief mentions
3. Focus on the problem space that a {{PRODUCT_SHORT}} would solve (e.g., {{PROBLEM_SPACE_EXAMPLES}})
4. Extract posts that use vivid, specific language to describe their emotional experience
5. Ensure posts come from the demographic that overlaps with {{COMPETITOR}} customers ({{COMPETITOR_DEMOGRAPHIC}})

**Output (pipeline addition):** for each of the 20 posts: URL, title, the key verbatim passages, and a one-line note on the emotional moment. These 20 URLs feed Prompt #2.

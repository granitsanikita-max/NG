# How the orchestrator briefs each one-by-one pass

Agent call: subagent_type "general-purpose", model "opus", run_in_background false (we wait; strictly sequential).

Prompt = the filled prompt file (all {{PLACEHOLDERS}} replaced) plus this footer:

---
You are doing ONE unit of a 25-ad creative strategy. Give it your full attention. Other units are handled separately.
- Read every file listed above before writing. Ground everything in them; if a fact isn't in them, say so, don't invent.
- Write your output to: {{OUTPUT_PATH}}
- Then reply with only: the output path + a 3-line summary + any flagged unsupported claims.

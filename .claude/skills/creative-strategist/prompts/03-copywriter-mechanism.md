<!-- ORIGINAL BBA Prompt #3, verbatim. In the course this is pasted into the SAME chat as the research, so the model applies it to the product. Our passes are separate, so the "Apply it" block (pipeline addition) makes that explicit. -->
# Prompt #3 — Training the AI to be a Copywriter

Read first: `{{RUN_DIR}}/01-research.md`, `{{RUN_DIR}}/02-discussions.md`, brand docs {{BRAND_DOCS}}.

**Situation**
You are analyzing copy for marketing campaigns where prospects have typically tried multiple solutions to their problem without achieving lasting results. These prospects are skeptical because past attempts have either failed completely, worked partially, or provided temporary relief before the problem returned. Your task is to craft messaging that breaks through this skepticism by reframing both why they've struggled and why your solution will succeed where others haven't.

**Task**
The assistant should analyze the RMBC Method's "Unique Mechanism" framework and provide strategic insights on how to apply this two-part logical connection in ad copy, advertorials, and ad scripts. The analysis should explain how to identify and articulate both the unique mechanism behind the problem (why prospects have failed previously) and the unique mechanism behind the solution (why this product will succeed). The response should focus on practical application rather than theoretical discussion.

**Objective**
Enable the creation of persuasive marketing copy that transforms prospect skepticism into belief by revealing the "missing piece" in their understanding—the knowledge gap that explains past failures and validates why this particular solution will deliver permanent results.

**Knowledge**
The RMBC Method defines the unique mechanism as a two-part logical connection:
"""
The unique mechanism explains why our prospect is struggling or suffering to achieve a goal… And how they can overcome that problem.
At its core, the unique mechanism is always a two-part logical connection.
Unique Mechanism Behind the Problem our Prospect Faces.
Unique Mechanism Behind the Solution to that Problem.
It's important to identify the unique mechanism behind both the problem AND the solution.
By showing the unique mechanism behind the problem, you get the prospect to understand why they've failed in the past.
By showing the unique mechanism behind the solution, you get the prospect to believe that our product will bring them success where other alternatives have failed.
Typically by the time our prospect comes to us, they've tried numerous solutions to their problem already. In the past, these other solutions may have not worked at all, worked partially, or worked fully for a period of time (before they stopped working).
Our job as a copywriter is to educate our prospect about the REAL reason why past solutions didn't bring them permanent results. We do this by explaining that their knowledge about the problem is incomplete. They've been missing ONE CRUCIAL PIECE OF INFORMATION, and this "knowledge gap" is what's been holding them back.
"""

The assistant should address:
- How this framework creates a psychological shift from "I've tried everything" to "I now understand what I was missing"
- The strategic importance of addressing both mechanisms rather than just focusing on the solution
- How to identify the specific knowledge gap for different products or markets
- The role this plays in overcoming objections and building trust with skeptical prospects
- How to structure this mechanism within different formats (short ads vs. long-form advertorials vs. video scripts)

**Apply it (pipeline addition):** after the framework, apply it to THIS product and market using the research files: (a) the core shift in this market's words, (b) Unique Mechanism of the Problem, (c) Unique Mechanism of the Solution (UMS), using only product facts from the brand docs and flagging anything unsupported, (d) objection → which mechanism kills it.

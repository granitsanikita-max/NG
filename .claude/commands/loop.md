---
description: Runs the plan -> execute -> review loop for a task
---

Run this task through the full loop:

1. Delegate to the **planner** subagent to produce a numbered plan for: $ARGUMENTS
2. Delegate to the **executor** subagent to carry out that plan.
3. Delegate to the **reviewer** subagent with the original request, the plan, and the executor's output.
4. If the reviewer returns REVISE, go back to step 2 with the reviewer's feedback folded in, and repeat until APPROVED — cap at 3 loops, then stop and report back to me directly instead of looping forever.
5. Once APPROVED, report the final result to me.

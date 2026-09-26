## RESUME / DEEP-HUNT NOTE (read after IMAGE_HUNT_INSTRUCTIONS.md)
A previous agent already worked on these formats and was cut off (or fell short). Each format in your task has
"already_found" = verified winners already saved in hunt2/<orig task>.json (orig task = the matching I1..I10 file that contains
that format name; "orig_task" is given for some). Read those entries first: do NOT re-deliver ids already there, and read their
"searched"/"rejected"/"notes" so you don't repeat dead-end searches. Your job: deliver ADDITIONAL verified winners so each format
reaches >= 5 total (already_found + yours). Write ONLY your new matches to hunt2/<YOUR TASK>.json (same schema, same exact format names).
Save credits: first re-screen the saved search pools from all agents (hunt2/*_pool.jsonl and other saved result files in hunt2/),
then run new searches. Try many more phrasings, niches, pagename searches for typical brands, sort_by toprank/lastseen as well as
longestrunning (longestrunning lists dead old ads first). Use include_filter_reference=true so results save to a file.
Update your JSON after each format. If a format truly cannot reach 5, say exactly how many and what you tried.

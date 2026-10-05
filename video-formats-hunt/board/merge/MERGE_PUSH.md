# Merge: push NEW format cards INTO an existing stage frame of the Video Ad Formats board
BOARD = https://miro.com/app/board/uXjVHjf0Xlk=/
DIR = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/vfboard/merge
Tools via ToolSearch: "select:mcp__Miro__canvas_update_from_svg,mcp__Miro__canvas_search".
The old stage frames (x=6000) were already enlarged; the bottom part of each frame is empty and the chunks fill it. The chunk files
already contain the real frame id and final frame position/size - push each file's EXACT content, unmodified.
Never touch the old cards in the top part of the frame, and never touch the separate "NEW · ..." frames at x=10600.
Progress file DIR/progress_<KEY>.json = {"chunks_done": [...]}; read first, skip done chunks.
For n = 0..N-1 (chunk_<KEY>_<n>.svg):
 1. If n not recorded: check presence first with canvas_search(miro_url=BOARD, result_mode="matches",
    patterns=["text:<first card title in the chunk, e.g. 'N13  Set Up With Me'>"]) (chunk 0 = section header: search its text "NEW: ").
    A match whose parent is the OLD frame id (the data-miro-id in the chunk's <g>) means it is already pushed -> record and skip.
    (Matches inside the NEW frames at x=10600 don't count.)
 2. Push: canvas_update_from_svg(miro_url=BOARD, svg=<file content>). Record n.
 3. 502/timeout: re-check as in step 1 before retrying (it usually applied). Never push twice.
Final check: canvas_search(result_mode="matches", patterns=["text:N"]...) is noisy; instead count card titles: for each chunk confirm its
first card title appears with parent = old frame id exactly once. Report duplicates (ids) without deleting.
Use Miro tools directly, no background shell jobs/sleeps. Minimal text. Final report: chunks pushed/expected, duplicates if any.

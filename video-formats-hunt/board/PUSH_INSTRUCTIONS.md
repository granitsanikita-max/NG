# Push one NEW-formats frame (cards only) to the Video Ad Formats board
BOARD = https://miro.com/app/board/uXjVHjf0Xlk=/
DIR = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/vfboard
Tools via ToolSearch: "select:mcp__Miro__canvas_update_from_svg,mcp__Miro__canvas_search".
The board already has OLD frames at x 6000-10120 - never touch them. Your frame lives at x = 10600.
Progress file: DIR/progress_<KEY>.json = {"frame_id":..., "chunks_done":[...], "images":{}}. Read it first if it exists; skip finished chunks.
Chunks: DIR/chunk_<KEY>_<n>.svg, n = 0..N-1 (ls them).
1. chunk 0 (if not done): pass the EXACT file content as `svg` to canvas_update_from_svg(miro_url=BOARD). It creates the frame. Take the
   frame's data-miro-id from result_svg (the <g ... data-frame=...> element) and save it as frame_id in the progress file.
2. n >= 1: sed 's/data-miro-id="FRAMEID"/data-miro-id="<frame_id>"/' into DIR/<KEY>_tmp_<n>.svg and push that EXACT content. One push per chunk.
   Record n in chunks_done after each success.
3. Error/timeout: it may still have applied. Before retrying run canvas_search(miro_url=BOARD, result_mode="matches",
   patterns=["text:<title of first card in that chunk, e.g. 'N3  Recipe Reel'>"], target_id=<frame_id>) and re-push only if absent.
4. Final check: canvas_search(result_mode="matches", patterns=["re:<rect[^>]*width=\"1964\""], target_id=<frame_id>) count == number of cards
   (grep -c 'width="1964"' over your chunk files). Fix gaps; delete only your own exact duplicates.
Do not edit SVG content. Minimal text output. Final report: frame_id, cards pushed/expected.

## RESUME NOTE (after a container restart)
The previous run may have pushed a chunk without recording it. Before pushing ANY chunk not in chunks_done, first check presence:
canvas_search(miro_url=BOARD, result_mode="matches", patterns=["text:<title text of the FIRST card in that chunk>"], target_id=<frame_id>)
(card titles are the <text ... font-size="38"> lines, e.g. "N13  Something"). If present, record it as done and skip.
Never use data-deleted; if you find duplicates, just report them (ids) in your final message.
Use the Miro tools directly (no background shell jobs or sleeps).

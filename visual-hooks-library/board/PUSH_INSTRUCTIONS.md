# (REBUILD v2) Push one frame of the Visual Hooks Library to Miro (your frame key is given in your task: g_text / g_pattern / g_motion / g_fx / g_unique)
BOARD = https://miro.com/app/board/uXjVHhmCPn0=/
DIR = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hooks/hboard
Load tools via ToolSearch: "select:mcp__Miro__canvas_update_from_svg,mcp__Miro__canvas_search,mcp__Miro__canvas_read_as_svg,mcp__Miro__image_get_upload_url,mcp__Miro__image_create".
IMPORTANT: this is a rebuild. The OLD layout (same frame titles) sits at x < 5000 and will be deleted later by someone else: never touch, read-modify or count items there. Your NEW frame is created by chunk 0 at x = 5000. When searching, always pass target_id=<your new frame_id> so old items are never matched (for step A3 before your frame exists, check the result of chunk 0 itself).
Progress file: DIR/progress_<KEY>.json = {"frame_id":..., "chunks_done":[n,...], "images":{"<name>":"<item_id>"}}. Read it first if it exists and skip finished steps (you may be a resumed run).

## A. Cards (chunks DIR/chunk_<KEY>_<n>.svg, n = 0..N-1)
1. chunk 0: cat the file and pass its EXACT content as `svg` to canvas_update_from_svg(miro_url=BOARD). It creates the frame. Get the frame's data-miro-id from result_svg (the <g ... data-frame=...> element) and save it as frame_id in the progress file.
2. For n >= 1: in the file replace the literal FRAMEID with the frame id (sed into a temp copy named <KEY>_tmp_<n>.svg), then push that EXACT content. One push per chunk.
3. If a push errors (502/timeout), it MAY still have applied: before retrying, run canvas_search(result_mode="matches", patterns=["text:<title of the first card in that chunk, e.g. '12  Tier List Board'>"]) and only re-push if absent.
4. Don't edit the SVG content otherwise. Don't touch anything outside your frame. Never delete anything except your own duplicates/orphans.
5. After all chunks: canvas_search(result_mode="matches", patterns=["re:font-size=\"40\" font-weight=\"bold\"[^>]*>\\d\\d\\d?  "], target_id=<frame_id>) or similar and confirm the card count equals the number of cards in your frame (count `rx="16"` card rects with width="2004" across your chunk files). Fix gaps.

## B. Images (DIR/plan.json entries whose "frame" == KEY)
For each entry: file = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hooks/<entry.file>, x = entry.cx, y = entry.cy, width = entry.width, url = BOARD + "?moveToWidget=" + frame_id.
1. image_get_upload_url(miro_url=url, content_type="image/jpeg", x=x, y=y, width=width)
2. Bash: curl -sS -o /dev/null -w "%{http_code}" -X PUT -H 'Content-Type: image/jpeg' --data-binary @<file> '<upload_url>'  -> must be 200
3. image_create(miro_url=url, image_token=<token>)
4. parent in the result must be non-null (your frame). If null: delete that image (<image data-miro-id="ID" data-deleted="true"/> via canvas_update_from_svg on BOARD) and redo (max 2 retries).
Record each created id in progress file images[name] right away (so a resumed run never double-uploads). At most 3 images per turn; minimal text output.
6. Final check: canvas_search(result_mode="matches", patterns=["re:data-type=\"image\""], target_id=frame_id) -> image count must equal plan entries for KEY. Extra images at the same slot = duplicate: delete the one not recorded in your progress file.

Final report (short): frame_id, cards pushed / expected, images placed / expected, any failures.

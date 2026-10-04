# Upload playable GIF clips into a NEW-formats frame on the Video Ad Formats board
BOARD = https://miro.com/app/board/uXjVHjf0Xlk=/
DIR = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/vfboard
Tools via ToolSearch: "select:mcp__Miro__image_get_upload_url,mcp__Miro__image_create,mcp__Miro__canvas_update_from_svg,mcp__Miro__canvas_search".
Your task gives KEY, FRAME_ID and an index range [a, b) into the list L = [e for e in plan.json if e["frame"] == KEY] (in file order).
Progress file DIR/img_<KEY>_<a>.json = {"<entry id>": "<created image item id>"}; read it first and skip done entries (you may be resumed).
For each entry e in L[a:b]:
  file = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/<e.file>   (animated GIF; never convert it)
  url = BOARD + "?moveToWidget=" + FRAME_ID
  1. image_get_upload_url(miro_url=url, content_type="image/gif", x=e.cx, y=e.cy, width=e.width)
  2. Bash: curl -sS -o /dev/null -w "%{http_code}" -X PUT -H 'Content-Type: image/gif' --data-binary @<file> '<upload_url>'  -> must be 200
  3. image_create(miro_url=url, image_token=<token>)
  4. The result's parent must be FRAME_ID. If parent is null/other: delete that image via canvas_update_from_svg(miro_url=BOARD,
     svg='<svg xmlns="http://www.w3.org/2000/svg"><image data-miro-id="ID" data-deleted="true"/></svg>') and redo (max 2 retries).
  5. Write the created id into the progress file immediately.
On 502/timeout of image_create: the image may exist anyway. Check with canvas_search(miro_url=BOARD, result_mode="matches",
patterns=["re:data-type=\"image\""], target_id=FRAME_ID) for an image at that slot before redoing; never leave two images on one slot.
Up to 3 entries per turn, minimal text output. Touch nothing else on the board. Final report: placed/expected, failures.

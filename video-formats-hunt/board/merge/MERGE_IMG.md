# Merge: upload playable GIF clips into the merged stage frames (cards are already there)
BOARD = https://miro.com/app/board/uXjVHjf0Xlk=/
DIR = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/vfboard/merge
Tools via ToolSearch: "select:mcp__Miro__image_get_upload_url,mcp__Miro__image_create,mcp__Miro__canvas_update_from_svg,mcp__Miro__canvas_read_as_svg".
L = [e for e in DIR/plan.json if e["frame"] == KEY] (file order); your range [a,b). e.frame_id = target frame; e.cx/e.cy are frame-relative.
Progress DIR/img_<KEY>_<a>.json = {"<entry id>": "<new image id>"}; read first, skip done.
For each entry:
 url = BOARD + "?moveToWidget=" + e.frame_id
 1. image_get_upload_url(miro_url=url, content_type="image/gif", x=e.cx, y=e.cy, width=e.width)
 2. curl -sS -o /dev/null -w "%{http_code}" -X PUT -H 'Content-Type: image/gif' --data-binary
    @/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/<e.file> '<upload_url>'  -> must be 200 (GIF as-is)
 3. image_create(miro_url=url, image_token=token). Parent must be e.frame_id; if not, delete that new image
    (canvas_update_from_svg svg='<svg xmlns="http://www.w3.org/2000/svg"><image data-miro-id="ID" data-deleted="true"/></svg>') and retry.
 4. Record immediately.
On 502/timeout of image_create, check the slot with canvas_read_as_svg (scope = frame origin + cx/cy ±150; frame origins in DIR/layout.json)
before redoing; never leave two images in one slot. Use Miro tools directly, no background jobs. Final report: placed/expected, failures.

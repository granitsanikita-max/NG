# Fix: GIF clips hidden BEHIND card shapes on the Video Ad Formats board (NEW frames at x=10600)
BOARD = https://miro.com/app/board/uXjVHjf0Xlk=/
DIR = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/vfboard
Problem: many GIF images were created BEFORE their card's grey card rect / black slot rect, so those shapes sit on top and the
viewer sees a black box. Fix = upload the same GIF again (a new image is created on top of everything) and delete the old hidden image.
The user explicitly asked for this fix and for removing duplicates, so deleting the OLD hidden image ids listed in DIR/img_<KEY>_*.json
(and the duplicate card copies named in your task) is authorized. Never delete anything else.
Tools via ToolSearch: "select:mcp__Miro__canvas_read_as_svg,mcp__Miro__canvas_update_from_svg,mcp__Miro__canvas_search,mcp__Miro__image_get_upload_url,mcp__Miro__image_create".
Frame absolute origins (x, y): n_TOF (10600,380) id 3458764685980662063 · n_TOF_MOF (10600,14527) id 3458764685980747040 ·
n_MOF (10600,27387) id 3458764685980746990 · n_MOF_BOF (10600,34852) id 3458764685982909491.
Entries: L = [e for e in DIR/plan.json if e["frame"] == KEY]; your range [a,b). Old image id for entry e = value for key e["id"] in any of
DIR/img_<KEY>_*.json files. Progress file DIR/fix_<KEY>_<a>.json = {"<entry id>": {"old": id, "new": id or "ok"}}; read first, skip done.
For each entry:
 1. Check z-order: canvas_read_as_svg(miro_url=BOARD, scope_x=X0+e.cx-150, scope_y=Y0+e.cy-150, scope_width=300, scope_height=300)
    (X0,Y0 = frame origin). Elements are listed bottom-to-top. If the old <image> is listed AFTER every <rect> in the result -> it is
    visible: record {"old": id, "new": "ok"} and skip.
 2. Otherwise re-upload: url = BOARD + "?moveToWidget=" + FRAME_ID; image_get_upload_url(miro_url=url, content_type="image/gif",
    x=e.cx, y=e.cy, width=e.width); curl -sS -o /dev/null -w "%{http_code}" -X PUT -H 'Content-Type: image/gif' --data-binary
    @/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/<e.file> '<upload_url>' (must be 200);
    image_create(miro_url=url, image_token=token). Parent must be FRAME_ID (else delete the new one and retry).
 3. Delete the OLD image: canvas_update_from_svg(miro_url=BOARD, svg='<svg xmlns="http://www.w3.org/2000/svg"><image data-miro-id="OLD" data-deleted="true"/></svg>')
 4. Record {"old": OLD, "new": NEW} immediately.
On 502/timeouts: re-check with canvas_read_as_svg on that slot before redoing; never leave two images in one slot.
Use Miro tools directly, no background shell jobs or sleeps. Minimal text. Final report: checked / re-uploaded / already-ok / failures.

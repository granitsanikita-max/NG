# Upload thumbnails to Miro (one batch file per agent)
Load tools via ToolSearch: "select:mcp__Miro__image_get_upload_url,mcp__Miro__image_create,mcp__Miro__canvas_update_from_svg".
Your batch file is a JSON list of {i, url, file, x, y, width}. For EACH entry:
1. mcp__Miro__image_get_upload_url(miro_url=url, content_type="image/jpeg", x=x, y=y, width=width)
2. Bash: curl -sS -o /dev/null -w "%{http_code}" -X PUT -H 'Content-Type: image/jpeg' --data-binary @<file> '<upload_url>'  -> must be 200
3. mcp__Miro__image_create(miro_url=url, image_token=<token>)
4. CHECK the image_create result: parent_miro_url must be non-null (it must name the frame). If it is null, the image landed outside the frame:
   delete it with mcp__Miro__canvas_update_from_svg(miro_url="<BOARD_URL>", svg='<svg xmlns="http://www.w3.org/2000/svg"><image data-miro-id="<item_id>" data-deleted="true" /></svg>')
   and redo steps 1-3 for that entry (max 2 retries).
Record every final item id (python, merge into your OWN results file named in your task) as {"<i>": "<item_id>"}; never write to other agents' files and give any helper scripts a name prefixed with your batch name.
At most 3 images per turn; minimal text output. Do not delete anything except your own orphaned (parent null) images.
Final report: count created, count of parent-null retries, any failures by i.

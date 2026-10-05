# Remove the now-redundant separate "NEW · ..." frames (their content was rebuilt inside the main stage frames)
BOARD = https://miro.com/app/board/uXjVHjf0Xlk=/
The user asked to merge the two tables into one per stage. The merged version now lives in the main frames at x=6000.
Delete EVERYTHING inside the frames you are given (all shapes, texts, textAreas, images), then the frame itself. These frames sit at x=10600.
Never touch anything at x < 10500 (the merged main frames).
Tools via ToolSearch: "select:mcp__Miro__canvas_search,mcp__Miro__canvas_update_from_svg,mcp__Miro__canvas_read_as_svg".
1. List child ids: canvas_search(miro_url=BOARD, result_mode="matches", patterns=["re:data-miro-id"], target_id=<frame id>), page through
   next_cursor until done (each result has id + type + parent). Save ids to DIR/clean_<frame id>.json as you go.
   DIR = /tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/vf2/vfboard/merge
2. Delete in batches of ~25 via canvas_update_from_svg(miro_url=BOARD, svg='<svg xmlns="http://www.w3.org/2000/svg">' + one element per id
   with the right tag (<rect .../> for shape, <text/> for text, <textArea/> for textArea, <image/> for image) carrying data-miro-id and
   data-deleted="true" + '</svg>'). Every child's parent must be your frame id - skip anything else.
3. Deletes often return 502 / "not confirmed" yet apply later: re-list before retrying; never fail on already-gone items.
4. When the frame is empty, delete the frame: <g data-miro-id="FRAME" data-deleted="true" />. Re-check it is gone.
Use Miro tools directly, no background shell jobs. Final report: per frame children deleted, frame deleted yes/no.

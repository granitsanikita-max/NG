# IMAGE FORMATS HANDOFF: give this whole folder (or the zip) to Claude and say "do everything in README_START_HERE.md"

## What Nikita wants (his words, condensed)
- Image Ad Formats Miro board: https://miro.com/app/board/uXjVHjfyDy4=/
- For EVERY image format (85 in formats_image.json): at least 5 references, and they must be WINNING ads, meaning long-running
  and still live, not "shit ads". Maximum effort and accuracy, no matter how long it takes.
- Remove the old Instagram/Notion screenshot references and replace them with our own Winning Hunter references.
- Look for NEW image formats not in the list, and get 5+ winning references for those too (mark them NEW).
- Keep the Notion page link and the original swipe links on every card.
- "Make everything bulletproof": save every reference image permanently in his Google Drive, one folder per format, and put a
  "💾 Saved copy" link under each thumbnail.
- Before saying it's done: go through everything and check that every link, image and card is there and correct.
- Style: direct, concise, honest about weak spots. Don't pad formats with non-winners; say which ones fell short.

## Reference: the finished VIDEO board (same design; copy it exactly)
https://miro.com/app/board/uXjVHjf0Xlk=/ : new layout at x >= 6000, six funnel frames (TOF, TOF→MOF, MOF, MOF→BOF, BOF, ANY).
Each format = a wide card (1964×938) holding:
- up to 6 thumbnails (300×520 slots);
- a "▶ Watch · N days live" pill (for images the generator writes "↗ View") linking the Winning Hunter single-ad page
  `https://app.winninghunter.com/ad/<id>?platform=meta`;
- under each pill, the advertiser name (links to their FB Ad Library page) and "💾 Saved copy" (links to the Drive file);
- a Links row: More winners · Original swipes · Notion page.
reference/formats2_video.json + reference/drive_done.json show the exact data shape that was used.

## Setup (lead session)
1. WORK = your scratchpad dir + /work. Copy scripts/* , formats_image.json , UPLOAD_INSTRUCTIONS.md into WORK;
   mkdir WORK/hunt2 WORK/imgs2 ; copy tasks/I*_task.json into WORK/hunt2/.
2. Tools needed (load with ToolSearch): mcp__winning_hunters__* (search_facebook_ads, scan_ad, get_store_details),
   mcp__Miro__* (canvas_search, canvas_read_as_svg, canvas_update_from_svg, image_get_upload_url, image_create),
   mcp__composio__COMPOSIO_REMOTE_WORKBENCH (Google Drive account googledrive / granitsanikita@gmail.com).
   Check Winning Hunter credits first (mcp__winning_hunters__check_credits); the video phase used roughly 1-2k credits of the 18.7k.
3. python deps: pillow, imageio_ffmpeg (pip install if missing).

## Pipeline
A. HUNT: spawn 10 background agents in parallel (I1..I10), each: "Read WORK/IMAGE_HUNT_INSTRUCTIONS.md (replace WORK with the real
   path). Your task name is I<n>; task file WORK/hunt2/I<n>_task.json." Plus one discovery agent E1 (new formats; same file,
   'Discovery task' section). Copy IMAGE_HUNT_INSTRUCTIONS.md into WORK too.
   When they finish: re-hunt any format with < 5 winners with a focused deep-hunt agent (more phrasings, niches, pagename searches).
B. QA: build contact grids of every format's winners (PIL) and LOOK at them yourself. Remove anything that isn't the format.
C. MERGE: `cd WORK && python3 merge_hunt2.py image` -> formats2_image.json (new formats appended with new=true; cross-format dedupe).
   Check the printed ISSUES. Keep every "why" to ONE short line (long text overlaps the thumbnails).
D. DRIVE BACKUP (before building the board, so the links exist): use scripts/img_drive_lib.py (paste its full code at the start of EVERY workbench call: the sandbox resets; it rebuilds state from Drive so re-runs never duplicate). Jobs from scripts/img_drive_jobs.py. Root folder id is set in the lib. Original notes:
   "Image Ad Formats - Winning References" with one subfolder per format; upload each ref with
   run_composio_tool('GOOGLEDRIVE_UPLOAD_FROM_URL', {source_url: <image_url>, name: "<days>d - <advertiser> - <id>.jpg",
   parent_folder_id, mime_type: 'image/jpeg'}). Response: data.id. Save {ad_id: {id, link: "https://drive.google.com/file/d/<id>/view"}}
   to WORK/drive_done.json. Persist progress to /mnt/files/*.json in the sandbox (the sandbox resets between sessions).
   If a source URL fails: scan_ad for a fresh one. Verify count == number of unique ref ids and no file < 20 KB.
E. GENERATE: `cd WORK && python3 gen_board2.py image` -> board2_image/header.svg, frame_f_*.svg, plan.json, frames.json, adv.json
   (the Saved-copy links are baked in because drive_done.json exists).
F. PUSH TO MIRO (board https://miro.com/app/board/uXjVHjfyDy4=/):
   - first canvas_search overview to see what's there; the old layout sits left of x=5000; the new one goes at x=6000.
   - push header.svg with canvas_update_from_svg.
   - big frames: `cd board2_image && python3 ../split.py f_TOF 4` (etc.) -> chunk_*_N.svg; push chunk 0 (creates the frame),
     read the new frame id from result_svg, replace FRAMEID in later chunks, push them one by one. ONE push per chunk: a 502 can
     still apply, so read the board before retrying or you get duplicates. Save frame ids to board2_image/frame_ids.json.
   - thumbnails: build upload batch files from plan.json ({i, frame, file: WORK/imgs2/<file>, x: cx, y: cy, width,
     url: BOARD?moveToWidget=<frame id>}) and spawn 3-5 agents on UPLOAD_INSTRUCTIONS.md (replace <BOARD_URL>). Each records
     placed_<batch>.json. If an agent dies midway, upload only the entries missing from its placed file.
G. DELETE THE OLD LAYOUT (Nikita approved replacing it): every frame/item with absolute x < 5000 on the image board, including the
   old header and "Jump to" nav. Read each old frame (widget_ids=[frameId]) to collect child ids, delete in batches of <= 150
   with <tag data-miro-id="ID" data-deleted="true" />, then the frame. Never touch x >= 5000.
H. AUDIT (mandatory, fix and re-audit until clean):
   - canvas_search result_mode="areas" with patterns ["re:data-type=\"image\""], ["winninghunter.com/ad/"], ["Saved copy"],
     ["Notion page"] -> per-frame counts must equal the plan (images per frame == plan entries per frame; pills == refs shown;
     Saved copy == refs shown; Notion page == cards with a Notion id).
   - Extra images in a frame = duplicates from interrupted uploads: find them with result_mode="matches" + the image regex
     inside that frame and delete the extra one at the same slot.
   - Only 6 frames on the board (canvas_search matches "re:data-type=\"frame\"[^>]*"), nothing at x < 5000.
   - Spot-read one card per frame with canvas_read_as_svg and check the links.
I. REPORT to Nikita: formats done, total winning refs, NEW formats found, which formats are under 5 and why, the Drive folder link,
   and the honest weak spots.

## Gotchas learned on the video board
- The WH last_seen filter is misleading (record update date). Always check started/lastSeen by hand.
- WH-hosted media sometimes 404s and fbcdn URLs expire within days: download the creative immediately, and use scan_ad for fresh links.
- image_create sometimes returns parent_miro_url null (image outside the frame): delete it and redo.
- Area reads fail above 500 widgets: use widget_ids reads or narrow bands.
- Agents sharing helper-file names overwrite each other's files: always prefix helper files with the batch/task name.
- A 502 from canvas_update_from_svg may still have applied: read before retrying.
- Usage limits can kill all agents at once. Every agent must write progress files as it goes so the work can resume.

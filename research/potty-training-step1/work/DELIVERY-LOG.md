# Delivery log — 2026-10-06
Folder: https://drive.google.com/drive/folders/1j-rhDFMF_bqcKUGOezrgPlJur7h0trOK
- Doc 1 — Market & Competition: https://docs.google.com/document/d/1RZ05O6JyejdqXlMChVyWg9m-w5b77wviOxCO310N9Wo/edit
- Doc 2 — The Customer: https://docs.google.com/document/d/1tdTqMh39ESjYC01GT1lICK7RKL7_oEkVsfzNG4mtqEg/edit
- Doc 3 — Persuasion: https://docs.google.com/document/d/1aRGzVQtHJ2jyr6ZsYjZLA_jgh0blzvOJk62KQx_fzZ0/edit
- Doc 4 — Brand, Offer & Funnel: https://docs.google.com/document/d/1AhHGErJeYFb2ZWJ7hupZhq3tz8F5XCljn70zrQ4NmSs/edit
- §2C Data Bank Sheet: https://docs.google.com/spreadsheets/d/1aTu0NTsyn5Ma_jgUgebmRxEd6nBm9OX37o0HtOs-X60/edit
- .md copies: 1pa4eWJeTYLwU1eU4El0-0_gLrWbNlY8d · 1cyfhhjww7C9u0ZWPggNdLLhimJ1RwPJ0 · 1O70V-tMwFOoQXUqiagrXXhZXnSp6iYzo · 1gLIJLFOr3EfP1s_0P48ibuoVGoQieJrr (byte sizes = source)

Method: md → HTML (build/to_html.py, `$` escaped as &#36; — the importer otherwise drops text between dollar signs) → server-side import (Composio GOOGLEDRIVE_UPLOAD_FROM_URL from the pushed commit). Inline create_file was abandoned: retyping 110–160 KB per doc got cut off mid-call.
Verification: every non-table line + every table cell of each .md found in the exported Doc text (0 missing of 1912 / 1095 / 985 / 1237); `$` counts equal; Sheet 602 rows identical to CSV. Partial/test uploads trashed.

# Store Images: Hero Carousel Sweep (Oct 2026)

Slide-by-slide breakdown of the product carousels on ~38 nine-figure DTC brands, classified into 20 image-format types. Feeds the Notion doc "Reference — Store Images (Hero Carousel Formats)" (Product Launch Playbook → reference guides): https://app.notion.com/p/3f4d53123cd68114a682d816f3a0f9bf

- `GALLERY_TAXONOMY.md` — the 20 image-format types used to classify.
- `REPORT_s1.md` — supplements/health (LMNT, Grüns, Ryze, Bloom, Create, im8, Hiya, ARMRA; AG1/Seed failed).
- `REPORT_s2.md` — food/bev (Javy, Olipop, Chomps, Graza, Fly By Jing, Liquid Death, David, MUD\WTR, Jinx; Magic Spoon failed).
- `REPORT_s3.md` — beauty/personal care (Dr. Squatch, Native, Jones Road, Nécessaire, Mando, Lume, Blueland; Manscaped/Hims failed).
- `REPORT_s4.md` — sleep/home (Miracle, Brooklinen, Cozy Earth, Bearaby, Oura, GroundingWell; Hatch/Ollie/Eight Sleep failed).
- `REPORT_s5.md` — apparel/kitchen/pet (True Classic, Tecovas, Vuori, Gymshark, Nomatic, Our Place, Caraway, HexClad; Ridge failed, Farmer's Dog has no carousel).
- `gallery.py` — the mobile carousel extractor (Playwright; captures hero + gallery slide files + full-page tiles).

Method: rendered each PDP at mobile width, pulled the product-gallery slide images, read every slide, classified format + on-image text. Carousel-only (inline/down-page images excluded).

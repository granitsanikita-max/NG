# Section Reference Boards

Built 2026-10-24 by the Daily Tasks station. Two private claude.ai boards of mobile section screenshots
from verified 7–9 figure brands (fashion excluded), sorted by section type, each type with a
"What the top stores do" patterns box.

- **Store board** (homepages, product pages, offer/landing pages, quizzes): https://claude.ai/artifact/AQYEuixw4bu8Bmz82pVTCi
- **Pre-sell board** (advertorials, listicles): https://claude.ai/artifact/SxXR7k1vGvWPSN2qpqX8hQ

Files here:
- `INDEX.md`: text index of every board example by section type (store, tier, page, pattern note, live URL). Use it to pull references without opening the boards.
- `taxonomy.json`: the section-type taxonomy (store and pre-sell boards) with descriptions.
- `STORES.md`: every brand that appears on the boards, with revenue tier.

How it was built: stores came from WinningHunter (revenue = 30-day estimate ×12, a third-party estimate). Ad landing pages
came from each store's top Meta ads. Pages were captured with Playwright at an iPhone viewport (390px) and split into
whole sections: a section is kept in one piece from its heading to its end (a full ingredient list, a full hero with the
buy box, a full review widget), never cut at the screen edge. Tall sections are captured as several screen-height shots
stitched into one image, with popups, cookie banners and sticky bars removed before each shot.
Each section was classified by vision review, then two QA passes checked every board pick and dropped broken,
popup-covered or duplicate tiles.

Using the boards: tiles show the whole section by default ("Tiles: Whole section"); switch to "Compact preview"
to scan faster. Click a tile for the side panel: "Fit whole section" shrinks it to one screen, "Full width" shows it at
readable size to scroll through. Screens are a snapshot from 2026-10-24, so the live pages may have changed since.

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
came from each store's top Meta ads. Pages were captured with Playwright at an iPhone viewport and split into sections.
Each section was classified by vision review, then a QA pass checked every board pick and dropped broken or duplicate tiles.
Screens are a snapshot from 2026-10-24, so the live pages may have changed since.

# NG — Brand Operating System

This repo is the **shared brain** for all of Nikita's dropshipping sessions.

Each session is one **station** on an assembly line. A brand is a **work order**
that moves from station to station. Every station reads the same brand folder,
does its one job, writes its own file, and hands off. This file is the operating
manual — **every session obeys it.**

---

## THE 7 GOLDEN RULES — never break these

1. **One active brand at a time.** Before any brand work, state it out loud:
   `ACTIVE BRAND: <slug>`. Everything you do belongs to that brand until it is
   committed and the context is cleared.

2. **The brand brain is law.** Before doing ANYTHING on a brand, read
   `brands/<slug>/BRAND.md`, `brands/<slug>/STATE.md`, and **every file in
   `brands/<slug>/brain/`**. Ground every output in them. Never invent a fact
   that contradicts the brain. If the brain doesn't answer something, say so —
   do not guess.

3. **Pull before, push after.** Sessions share state only through git. Run
   `git pull` before you read a brand, and `git add -A && git commit && git push`
   the moment Nikita CONFIRMS the work (see rule 7). Skip this and you either
   work on stale data or confirmed work is invisible to every other session.

4. **Stay in your lane.** Only write the file(s) your station OWNS (see table
   below). Read upstream files freely. Never overwrite another station's file.

5. **Leave a trail — of CONFIRMED work only.** When Nikita has confirmed a
   piece of work, update the brand's `STATE.md` (stage · status · next action ·
   date · your station) and its row in `brands/_BOARD.md`, then commit + push.
   Drafts and proposals do not get a trail entry.

6. **Never mix brands.** To switch brands: finish → commit → push, then Nikita
   runs `/clear` before loading the next brand. Two brands never share a context.

7. **NOTHING goes into the brain until Nikita confirms it.** The repo (every
   brand file, `STATE.md`, `_BOARD.md`, `brain/`) holds ONLY finalized,
   confirmed decisions — never drafts, proposals, "v1 pending approval", open
   options, or things you *think* he'll do. Unconfirmed work poisons every other
   session: they read it as fact and build on it.
   - **While working:** keep drafts in your session scratchpad (outside the
     repo) and show them to Nikita in chat. Do NOT commit them.
   - **Confirmation = Nikita says so explicitly** ("lock it", "confirmed",
     "that's final", "add it to the brain"). Silence, "looks good", or moving on
     to another topic is NOT confirmation — ask: "Want me to lock this into the
     brain?"
   - **Then** write only the confirmed parts (not the rejected options or open
     questions) into the file you own, update STATE + board, commit, push.
   - **If he changes his mind later,** edit the brain to match — never leave a
     superseded decision sitting there looking current.
   - **Facts too:** never write a claim about the store, product, shipping or
     numbers into the brain unless it was verified (checked live, or Nikita
     told you). Unverified = don't write it.

---

## START-OF-BRAND RITUAL (do this every time, in order)

1. `git pull` — get the latest brain, board, and upstream station output.
2. Read `sessions/<your-charter>.md` — remind yourself of your exact job.
3. Read `brands/<slug>/BRAND.md`, `STATE.md`, and all of `brands/<slug>/brain/`.
4. Read the upstream files your station depends on (see table).
5. State `ACTIVE BRAND: <slug>` and, in 1–2 lines, what you're about to do.

## HANDOFF RITUAL (only after Nikita confirms — see rule 7)

0. Not confirmed yet? STOP here. Draft stays in your scratchpad; ask Nikita
   whether to lock it. Nothing gets committed.
1. Write the CONFIRMED output into the file your station OWNS.
2. Update `brands/<slug>/STATE.md`: current stage, status, the exact next action
   for the next station, today's date, your station name.
3. Update the brand's row in `brands/_BOARD.md`.
4. `git add -A && git commit -m "<brand>: <what you did>" && git push`.
5. Tell Nikita in 2–3 lines what you did and what's ready next.

---

## BRAND FOLDER LAYOUT

```
brands/
  _BOARD.md            <- dispatch board: every brand + its current stage
  _TEMPLATE/           <- copy this to start a new brand
  <brand-slug>/
    brain/             <- Nikita's raw research docs (SOURCE OF TRUTH, read-only)
    BRAND.md           <- identity: name, niche, target customer, positioning
    STATE.md           <- stage · status · next action · last touched
    PRODUCT.md         <- owned by Product Research
    RESEARCH.md        <- owned by Deep Research
    OFFER.md           <- owned by Offer/Funnel Design
    FUNNEL.md          <- owned by Offer/Funnel Design
    COPY.md            <- owned by Copywriting
    STORE.md           <- owned by Store Build
    AD_RESEARCH.md     <- owned by Ad Research
    SCRIPTS.md         <- owned by Ad Scripting
    STORYBOARDS.md     <- owned by Storyboarding & B-roll
    CREATIVES.md       <- owned by Ad Prompting & Creation
    ECONOMICS.md       <- owned by Economics & Analytics
```

## FILE OWNERSHIP — who writes what, who reads what

| Station (session)              | OWNS (writes)            | READS (upstream)                          |
|--------------------------------|--------------------------|-------------------------------------------|
| Product research & validation  | PRODUCT.md               | brain/                                    |
| DEEP research & offer research | RESEARCH.md              | brain/, PRODUCT.md                        |
| Offer, store & funnel design   | OFFER.md, FUNNEL.md      | brain/, PRODUCT.md, RESEARCH.md           |
| Copywriting for funnel & store | COPY.md                  | brain/, OFFER.md, FUNNEL.md, RESEARCH.md  |
| Store & funnel build           | STORE.md                 | brain/, FUNNEL.md, COPY.md, OFFER.md      |
| Ad research & planning         | AD_RESEARCH.md           | brain/, PRODUCT.md, RESEARCH.md, OFFER.md |
| Ad scripting                   | SCRIPTS.md               | brain/, AD_RESEARCH.md, OFFER.md, COPY.md |
| Ad storyboarding & B-roll      | STORYBOARDS.md           | brain/, SCRIPTS.md, OFFER.md              |
| Ad prompting & creation        | CREATIVES.md             | brain/, STORYBOARDS.md, SCRIPTS.md        |
| Economics & analytics planning | ECONOMICS.md             | brain/, PRODUCT.md (front), live numbers (back) |
| Daily random tasks             | scratch/ only            | anything, but only via the load ritual    |

**Golden rule 4 restated:** if a file isn't in your OWNS column, you do not write it.
The two exceptions every station writes are `STATE.md` and `_BOARD.md` (the trail).

---

## STARTING A NEW BRAND

1. Pick a short slug (lowercase, hyphens): e.g. `glow-roller`.
2. `cp -r brands/_TEMPLATE brands/<slug>`
3. Drop Nikita's research docs into `brands/<slug>/brain/` exactly as given.
4. Fill `brands/<slug>/BRAND.md` (name, niche, target, one-line positioning).
5. Add a row to `brands/_BOARD.md`.
6. Commit + push.

Whichever session Nikita is in when he starts a new brand does this setup, then
proceeds with its own station's job.

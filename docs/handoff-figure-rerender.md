# Handoff: re-render the sibling-conflict figures for the web

**From:** session rooted in `cascadia-curiosities`, 2026-08-12 through 2026-08-13.
**For:** a session rooted in `RobbinsAnalytics.github.io`. Separate because hooks
and `CLAUDE.md` load only from the primary working directory — Part 1 could not
safely touch the site repo, and this session should not either.
**Author:** Aaron Robbins. Aaron does not write code and does not run scripts; he
approves decisions, the agent executes. Ambiguity stops the work and asks. Never
end with "now run this."

## Status: Part 1 is complete. This document now covers Part 2 only.

Everything below the fold that used to describe Part 1 — prerequisites, the build,
the panel — is done and committed in `cascadia-curiosities`:

- `33e8382`, `634fbbe` — scoped the work, corrected a figure name.
- `5a7cb9f` — first web renders, Panel v3 (19 findings, one a verified
  mathematical error: the sibling-pairs count is the *subset* of configurations
  in which both sides are single children, not an independent quantity).
- `c4f1e0e` — reworded the figures to fix that and three other v3 findings, added
  a worked-example figure (all 6 configurations for 3 children) that both panels
  had asked for.
- `e68cc0e` — propagated the corrected wording everywhere, revised the manuscript
  itself (Aaron's call: nothing was formally submitted, so the paper could
  change), added the n=4 worked example for print, ran Panel v4 (17 findings, 11
  fixed — the strongest signal was all four seats independently reporting no key
  existed for the circle fill states).
- `ce1dad9` — ran the Cascadia checklist, found and fixed three INVARIANT
  failures (a typed axis bound, a sub-3:1 contrast pairing, a missing
  provenance-strip date), found five sub-12px type elements and fixed those too,
  and issued verdicts.

Read `governance/chart-review.md` and `governance/panel-returns.md` in this repo
for the full record. What follows is what Part 2 actually needs.

## What ships, per the checklist verdict

**Manuscript figures — SHIPS.** Not your concern; they're in the manuscript PDF.

**Web renders — ship as artifacts, page-level publish is blocked** on three
things only the site repo can resolve (below).

**Narrow renders (`figure1_narrow.png`, `figureA_narrow.png`) — DO NOT SHIP.**
They are currently live on the page and have been failing check 5.3 (12px type
floor) the whole time — their smallest element renders at 10.25px in the 324px
column they're actually served at. Replacing them is the point of this handoff.

## The three assets to bring over

All in `cascadia-curiosities/curiosities/sibling-conflict-combinatorics/figures/`:

| File | Replaces | Note |
|---|---|---|
| `figure1_web.png` | `sibling-conflict-figure1-narrow.png` | n = 1–8 line chart, corrected title and wording |
| `figureA_web.png` | `sibling-conflict-figureA-narrow.png` | n = 1–4 line chart, corrected title and wording |
| `figure_n3_web.png` | *(nothing — new)* | Worked example, all 6 configurations for 3 children. Both panels asked for this. It is **not a repoint**, it's a new figure with no existing slot on the page |

The design-size siblings (`figure1_design.png`, `figureA_design.png`) are what
the `<img>` fallback in each `<picture>` block should point at — same role the
`-figureA.png` / `-figure1.png` assets in `RobbinsAnalytics.github.io/assets/`
play now, just regenerated with brand fonts and corrected wording.

## Already done in the site repo's working tree — uncommitted

**Breakpoint fixed.** Both `<source media="(max-width: 600px)">` in
`projects/sibling-conflict.qmd` are now `760px`. Checklist note 8 found the
design render doesn't clear the 12px floor until its column reaches 712px (the
provenance strip is the binding element) — 600px left a band from 601–763px
where neither render passed 5.3. This is why the breakpoint moved and where the
number comes from. **This part of the interim fix is still correct and should
not be reverted** — it's independent of which files the `<source>` tags point
at.

Nothing else was touched. No asset was copied, no `<source>` was repointed, no
prose was edited, nothing was committed, nothing was published.

## Part 2 — do this in a session rooted in `RobbinsAnalytics.github.io`

1. **Copy the three web-size PNGs and the two design-size PNGs** into `assets/`,
   named consistently with the existing `sibling-conflict-figure1.png` /
   `-figureA.png` convention. `figure_n3_web.png` needs a new name and a new
   `<picture>` block — there's no existing slot for it.

2. **Repoint the two existing `<source>` elements** at the new narrow-slot PNGs.
   The breakpoint is already `760px`; don't change it back.

3. **Add the n=3 worked-example figure.** Where it goes on the page is a design
   call — it could sit beside the n=1–8 chart as the concrete instance both
   panels wanted, or stand alone under its own heading. Surface this to Aaron
   rather than deciding it; it's the kind of placement call this repo's own
   `CLAUDE.md` would want asked rather than assumed.

4. **Fix the caption that still says "Figure B."** The `<picture>` block for the
   n=1–8 chart reads `<figcaption>Figure B — the full range...`. Aaron confirmed
   in this session's Part 1 that this piece has no Figure B; it's Figure 1
   throughout the manuscript and the other figures. Rename it.

5. **The alt text on both existing figures is now wrong** — it quotes the old
   titles and value labels verbatim ("Eight children allow 3,025 possible
   conflict configurations, but form only 28 sibling pairs..."). The titles
   changed (see the commits above: "Of the 3,025 ways eight children can take
   sides, just 28 are one against one"). Alt text needs to describe what the new
   renders actually show, not what the old ones did.

6. **The prose in "What it doesn't claim" does not currently mention DejaVu at
   all** — the original version of this handoff (2026-08-12) described a
   sentence that either predates this page's current text or was never written
   the way that draft assumed. Read the section fresh rather than searching for
   a sentence to edit. What *is* true and worth adding: the manuscript PDF
   linked from this page is still DejaVu (Part 1 never touched it, by design —
   it's the artifact the editors received), while the web figures on this page
   now are not. If the page is going to say anything about typography, that's
   the accurate distinction to draw.

7. **Four checklist items are recorded `NOT ASSESSED`, not passed, because
   they're page-level properties Part 1 couldn't verify from this repo.**
   Resolving them is part of finishing Part 2, not optional polish:
   - **K8** — Open Graph tags and a favicon on this page.
   - **5.2** — the image `alt` text stays at levels L1–L3 (chart type, encodings,
     axis ranges, units; then extrema and comparisons; then trend/shape where it
     helps) and never reaches L4 (what the data means, implications). Once the
     alt text is rewritten per item 5, check this against the rule, not just
     against readability.
   - **5.7** — dark mode, if the site has one: hue preserved, not an inverted or
     algorithmically transformed light palette.
   - **The page half of 5.1** — a real `<table>` of the data belongs on the page,
     not only a text summary. The qmd already has one (the children/pairs/
     configurations table); check its column headers still match the corrected
     framing ("one against one" now, not "sibling pairs" as an independent
     count) before assuming it clears this on its own.

8. **Check 3.2's exception on the web renders depends on that data table
   existing on the page and naming its basis.** It's the same table as item 7 —
   two checks, one fix, don't do it twice.

9. `/publish`. The push is the deploy and the single approval; this repo's
   `CLAUDE.md` forbids improvising a shorter version.

## Decisions Aaron has not made yet

- Where the n=3 worked-example figure sits on the page (item 3 above).
- Whether the web renders' point sizes should also replace the print/narrow
  build entirely, or whether a narrow target stays for some other use. It's
  currently unused by anything — the web renders supersede it for every purpose
  it served on this page — but no one has decided to delete `build_lines.py`'s
  `narrow` target, so it still exists and still builds.

# Handoff: re-render the sibling-conflict figures for the web

**From:** session rooted in `cascadia-curiosities`, 2026-08-12
**For:** two sessions — Part 1 rooted in `cascadia-curiosities`, Part 2 rooted in
`RobbinsAnalytics.github.io`. They are separate because hooks and `CLAUDE.md`
load only from the primary working directory.
**Author:** Aaron Robbins. Aaron does not write code and does not run scripts; he
approves decisions, the agent executes. Ambiguity stops the work and asks. Never
end with "now run this."

## Why this exists

Two defects in the same artifacts, fixed by the same re-render:

1. **The figures are typeset in DejaVu**, substituting for Source Serif 4 and
   Segoe UI. `governance/chart-review.md` line 127 records it and says to
   re-render with brand fonts if the figure is ever reused on a Cascadia web
   property. It now has been.
2. **The in-chart type is too small on mobile.** Measured on the live page at a
   375 px viewport, before the interim fix below.

Do them as one job. Two re-renders means two reading panels for one set of
charts.

## The measurement

The figure column is 324 px wide at a 375 px viewport. In-chart type converts as
`css_px = points × (dpi ÷ 72) × (display_width ÷ natural_width)`.

| In-chart element | Design render, 1050 px | Narrow render, 540 px | Page caption |
|---|---|---|---|
| Chart title | 8.7 px | 12.5 px | — |
| Chart subtitle | 6.8 px | 9.8 px | 15.3 px |
| Value labels (90/301/966) | 6.1 px | 9.5 px | 15.3 px |
| End labels | 6.8 px | 10.3 px | 15.3 px |
| Source strip | 5.5 px | 8.5 px | 15.3 px |

Page body is 17 px. The chart's own subtitle was rendering at 40% of the size of
the caption printed directly beneath it.

**The governance point:** the panels read these charts at 1050 px and 540 px. The
site was displaying one at 324 px — a width no reading panel has ever read them
at. That is the Rule 7.4 failure arriving through CSS rather than through the
chart, and it is the reason step 4 below is not optional.

## Already done — the interim fix

**Status: edited and verified in the site repo working tree, NOT committed, NOT
published.** A session rooted in the site repo must run `/publish` to deploy it;
that command owns the deploy and its `CLAUDE.md` forbids improvising a shorter
version.

- Copied `figure1_narrow.png` → `assets/sibling-conflict-figure1-narrow.png` and
  `figureA_narrow.png` → `assets/sibling-conflict-figureA-narrow.png`.
- Replaced both `![...](...)` blocks in `projects/sibling-conflict.qmd` with raw
  HTML `<picture>` blocks carrying
  `<source media="(max-width: 600px)" srcset="...-narrow.png">`, wrapped in the
  same `quarto-figure quarto-figure-center` / `figure.figure` structure Quarto
  emits, so existing styling is untouched.
- **Figure 1's alt text changed**: it quoted the annotation verbatim, and the two
  renders word it differently ("triples the space of possible conflicts" vs
  "triples the possibilities"). Alt applies to whichever source loads, so the
  quotation became a description. Figure A's alt was accurate for both and is
  unchanged.
- Verified against a local build served over localhost: fresh load at 375 px
  fetches both `-narrow` files; fresh load at 1280 px fetches both design files
  and renders at 799 px, identical to today's desktop behaviour.

This buys ~1.6× and carries **no panel debt** — `chart-review.md` records every
seat reading both widths, so the narrow renders are panel-cleared artifacts. It
is not a fix: 9.8 px is still well under the 15.3 px caption.

## Part 1 — in `cascadia-curiosities`

### 1. Prerequisites (needs Aaron's approval; both are installs)

- **matplotlib** — not installed on this machine. The figures were never built
  here; the handoff records the original work as a Cowork session, whose sandbox
  ships DejaVu and nothing else. That is the whole explanation for the font
  substitution.
- **Source Serif 4** — not installed as a system font. Segoe UI is (it ships with
  Windows). The site has only ever used Source Serif 4 as a webfont, which is why
  it appeared available: matplotlib reads neither CSS nor webfonts.

### 2. Build web variants — a third target

Keep `build_figure.py`, `build_figureA.py`, `build_narrow.py` producing exactly
what they produce now. Add web builds alongside; do not repoint the existing
ones.

Author at **twice the display slot** so the image stays crisp on 2× screens. At
`dpi=150` with `natural_width = 2 × display_width`, the conversion collapses to
`css_px ≈ points` — so point sizes can be read straight off the target:

| Element | Target |
|---|---|
| Chart subtitle | 13 pt → ~13.5 px |
| Annotations, value labels, end labels | 12 pt → ~12.5 px |
| Chart title | 18 pt → ~18.75 px |
| Source strip | 11 pt → ~11.5 px |

For the 324 px mobile slot that is `figsize=(4.32, H)` at `dpi=150`. Set
`SERIF="Source Serif 4"` and `SANS="Segoe UI"`, and **assert the fonts actually
resolved** — matplotlib silently falls back to DejaVu and prints only a warning,
which is exactly how this defect shipped the first time.

### 3. Do not touch the manuscript figures

`figure1_design.pdf` and `figureA_design.pdf` are in the compiled PDF the editors
received, and the paper is under consideration. Changing figures mid-query buys
nothing and costs the "this is what they received" property. The web renders are
additional artifacts, not replacements.

### 4. Rule 7.4 reading panel on the new renders

Required — these are charts no panel has read. Use the
`cascadia-reading-panel` skill.

**Give the seats the mobile display width — ~324–355 px — as one of the widths.**
A panel that reads at 1050 px will pass a chart that is unreadable on the page.
That is the gap that produced this handoff.

Record pre-panel notes **before** the panel runs. Panel v2's N is unmeasured
because that was skipped; `chart-review.md` records the gap honestly and it must
not be reconstructed. Do not repeat it.

### 5. Record it

New "Panel v3 — web renders" block in `governance/chart-review.md`, full returns
in `governance/panel-returns.md`, same shape as v1 and v2. Stage by name; never
`git add -A` or `git add .`.

## Part 2 — in `RobbinsAnalytics.github.io`

1. Copy the approved web renders into `assets/`.
2. Repoint the `<source>` elements in `projects/sibling-conflict.qmd` at them.
   The `<picture>` scaffolding is already in place from the interim fix.
3. **Update the prose.** The page currently says, under "The figures went through
   the same review as the dashboards":

   > One exception carries onto this page. Both figures were typeset in
   > DejaVu…

   That becomes wrong for the web renders and stays true for the manuscript
   figures. It needs to distinguish the two, not be deleted — the manuscript PDF
   is linked from the same page and is still DejaVu.
4. `/publish`. The push is the deploy and the single approval.

## Decisions Aaron has not made yet

- Whether the web renders should also become the **narrow print** renders, or
  whether print keeps DejaVu. Print and web have different type-size needs, and
  the journal may impose its own typography anyway.
- Whether Figure A and Figure B should keep the portrait 540×630 aspect on
  mobile, or get a web-specific aspect. The panel is the right place to surface
  this, not a decision to make in advance.

# Chart review — Figure 1, "Sibling conflict combinatorics" (Mathematical Intelligencer submission)

**Reviewed under CHART-REVIEW.md v2.5 / VIZ-PRINCIPLES.md v2.5 · 2026-08-12**
Author of record: Aaron Robbins. Chart built and panel run by agent; **dispositions below are ratified by Aaron, both panel rounds, 2026-08-12** — per Rule 7.4, disposition belongs to the author.

---

## READING PANEL — Figure 1 (two renders) — 2026-08-12

Decision served (Rule 0.1): a Mathematical Intelligencer reader — editor, referee, or general mathematical reader — deciding whether the paper's central quantitative claim (the conflict-configuration space grows exponentially while pairwise relationships grow quadratically) is credible, well-defined, and worth publishing; secondarily the lay reader the paper's conclusion explicitly addresses.
Nature: **simulated** (all seats)
Widths given: 1050 px (design, 7.0 in) and 540 px (narrow, 3.6 in single-column) — both renders to every seat.

  Seat 1  Mathematics magazine editor (15 yrs)   — why: owns the accept/reject decision; tests whether the figure carries its claim for a broad mathematical readership and survives print production
  Seat 2  Quantitative family-studies researcher (12 yrs) — why: the paper asks this community to test the framework; tests whether the figure claims more about actual families than the math supports
  Seat 3  Parent of five, non-technical           — why: the conclusion addresses "parents seeking context"; sits where the least technical real reader's visualization literacy sits
  Seat 4  visualization — canvas only; no tables, no data, no finding

Blindness confirmed: design system ☑ · review and build notes ☑ · source data ☑ · intended finding ☑ · other reviewers' output ☑
Run: parallel ☑ (all four seats spawned in a single message)

### Pre-panel notes (builder's list, recorded before the panel ran)
1. Rain series hugs zero, may read as baseline. 2. n=1–4 values indistinguishable from zero. 3. "Roughly triples" not verifiable by eye. 4. "3,025" is 4 sig figs vs Rule 2.9. 5. DejaVu font substitution. 6. Relationship declaration ambiguity (magnitude vs change).

### Return highlights (full returns in panel-returns.md)
- Seat 1 SENTENCE: "the number of ways eight kids can split into two warring camps is over three thousand, while the number of sibling pairs is only 28" — carries the title's claim: **yes**. NUMBER: 3,025, "printed right at the end of the green curve … agrees with where the last dot sits, just above the 3,000 gridline."
- Seat 2 SENTENCE: "…it's arithmetic, not data about anything siblings actually do" — carries the claim: **yes**, with the intended caveat self-generated. NUMBER: 3,025, end-of-line label + endpoint dot vs axis.
- Seat 3 SENTENCE: "with eight kids there are three thousand different ways they could split up and fight … the ways they can gang up on each other explodes" — carries the claim: **yes**. NUMBER: 3,025, end label + dot at the 3,000 mark.
- Seat 4: title and picture agree; 3,025 "genuinely on the plot"; grayscale survives on line weight + direct labels.

All four sentences carried the title's claim; all four numbers were located on the canvas (marks/labels, not tables). 7.1's test passes.

### Disposition table

| # | Finding, in the reviewer's words | Seat(s) | Consensus | Defect? | Disposition | Rule |
|---|---|---|---|---|---|---|
| 1 | "If the answer is 'some kids are neutral,' that needs to be on the page" / "the formula implies a third category exists but the prose never says so" | 1, 2 | 2 | yes | **fixed** — subtitle now reads "two opposing sides, others uninvolved" on both renders | 4.3 |
| 2 | "the shortened wording ['Two-sided splits'] now says something the formula next to it contradicts" | 1 | 1 | yes | **fixed** — narrow subtitle rewritten; formula moved off the narrow canvas into the manuscript caption | 3.2 / 4.3 |
| 3 | "the tripling is asserted, not shown" / "I have to take its word for it" / "the current form asks for faith" / "triples from what?" | 1, 2, 3, 4 | 4 | yes | **fixed** — value labels added at n=5, 6, 7 (90, 301, 966); 301 → 966 → 3,025 is now checkable on the canvas | 3.4 |
| 4 | "the chart is about families like mine and I still can't find my own family on it" | 3 | 1 | yes | **fixed (partial)** — n=5 now reads 90 on the canvas; n≤4 remain unlabeled at this scale, values carried by the manuscript's Table 1; residual accepted. *Author overrode the residual acceptance 2026-08-12: "the chart doesn't display values for the vast majority of actual parents." Resolved by adding Figure A (n = 1–4) as a separate figure — see Panel v2 below.* | 0.1 |
| 5 | "is there any family data behind this at all, or is the family framing a metaphor?" / "a math fact, not a parenting fact" | 2, 3 | 2 | yes | **fixed** — subtitle carries "a possibility space — no claim about actual conflicts" on both renders | 4.3 |
| 6 | "the plot supports 'negligible,' not '28'" / "a flat smear at zero" | 4, 1 | 2 | yes | **accepted** — the contrast IS the claim; the exact value travels on the direct end label; a log axis or inset would trade away the magnitude message the title makes | 2.3.6 / 3.6 |
| 7 | "the wrapped 'Sibling pairs: 28' label floats … I had to look twice to confirm which mark it belonged to" (narrow) | 4 | 1 | yes | **fixed** — single-line label seated tight to the line end | 3.6 |
| 8 | "the annotation now occupies the whole upper-left quadrant … dominates the plot area" (narrow) | 4, 3 | 2 | yes | **fixed** — annotation shortened; plot area enlarged | 3.4 |
| 9 | "on newsprint (3ⁿ − 2·2ⁿ) could easily read as (3 − 2·2) … I'd want that set as a real equation" | 1 | 1 | yes | **fixed (narrow)** — formula removed from narrow subtitle, typeset equation in the LaTeX caption; **accepted (design)** — vector PDF, legible at production sizes | — |
| 10 | "no bridge from [OEIS/Stirling] to 'conflicts'" | 1 | 1 | no | **rejected** — the derivation is Section 2 of the manuscript; a chart footer cannot carry a proof, and no wrong conclusion follows from the gap (4.3 test); the strip's job is a recognizable source, which OEIS is for this readership | — |
| 11 | "the fine print about 'OEIS A000392' means nothing to me" | 3 | 1 | no | **rejected** — audience mismatch: the declared reader (0.1) is the Intelligencer's mathematical readership, for whom OEIS is recognizable; the manuscript's prose carries the plain-language bridge | — |
| 12 | "the arrow could be misread as saying something specific about n=7" | 4 | 1 | yes | **accepted** — the leader must land somewhere (3.4 redundant linkage); n=7 is in the only steep region and adjacent to the labeled 966 where the tripling is checkable | 3.4 |

### Panel summary

```
PANEL: 4 seats, simulated · 1 chart (2 widths) · findings 12 · defects 10 · novel 7
       fixed 8 (one partial, one narrow-only) · accepted 3 · rejected 2
       D = 10.0 defects/chart · N = 0.70 novel share · R = 0.17 rejected share
       Widths read: 1050 px, 540 px
```

Highest-consensus finding (4 of 4 seats): the unverifiable "roughly triples" annotation. Fixed before anything else, per the consensus-drives-fix-order rule.

---

## CASCADIA CHART REVIEW v2.5 — figure1 (design + narrow renders) — 2026-08-12

Class: detailed · Quadrant: explanatory · Relationship: magnitude (two counts compared as n grows; form is paired curves over ordered n — recorded, form and title agree that the comparison of magnitudes at n=8 is the claim)
States reached: static figure — n/a (no interaction)
Widths reached (K6): 540 px, 1050 px (print figure; no breakpoints declared)
Once per publish (K7, K8): N/A — print manuscript, no page
Reading panel (7.4): above · 2026-08-12 · simulated

INVARIANTS
  0.1  PASS — decision recorded in roster block
  0.2  PASS — explanatory
  0.3  PASS — detailed
  1.1  PASS — magnitude; title compares two magnitudes both plotted
  1.4  N/A — not correlation
  2.1  PASS — magnitude/gap claim; zero baseline included anyway; bounds derived (max×1.06)
  K1   PASS — y-axis 0–3,207 contains 0–3,025; x-axis 1–8 contains all n; bounds computed from series
  2.2  PASS — single value axis
  2.3.1 PASS — Evergreen slot 1 (emphasis), Rain (context); no re-dealing possible
  2.3.2 N/A — no sentiment encoding
  2.3.3 PASS-BY-EXCEPTION — Evergreen/Rain pair at 2.2 px stroke: separation carried by lightness (51.5 vs 71.4 L*) and direct labels, not hue alone
  2.3.4 N/A — two series, not small-symmetric-mark palette case
  2.3.5 PASS — two encoded categories
  2.3.6 PASS-BY-EXCEPTION — Rain at 2.45:1 carries direct label "Sibling pairs: 28" in Slate moss at 5.82:1
  2.5  PASS — flat marks, no decoration
  2.6  N/A — not part-to-whole
  3.1  PASS — finding sentence, top
  3.2  PASS — 3,025 and 28 both on-canvas as end-of-line labels attached to plotted marks; "possible … configurations" qualified on the canvas by the subtitle's possibility-space caveat
  3.3  PASS — one saturated series (the title's), context series Rain with direct label, annotation colour-matched Evergreen (5.18:1 as text, clears 2.3.7)
  3.4  PASS — one dominant primary annotation at the data, leader + proximity linkage, ≤14 words, mechanism at the mark, claim in the title
  3.5  PASS — the two series share one frame; the compared marks are the two line ends, adjacent to their labels
  3.6  PASS — direct end-of-line labels, no legend
  4.1  PASS — no missing data; counts exact by construction
  4.2  PASS — strip bottom-left: Evergreen tick · OEIS A000392, S(n+1, 3) · computed 2026-08-12 · exact counts, nothing estimated
  K5   PASS — three segments declared, three rendered (both widths)
  4.3  PASS — possibility-space caveat and neutral-children definition on the canvas after panel fixes 1 and 5
  4.5  N/A — every value exact by construction
  5.1  PASS (print analog) — manuscript body is the text summary; Table 1 in the manuscript is the data table; keyboard layer N/A in print
  5.2  N/A — print figure, no alt-text channel in the figure itself (manuscript caption is L1–L2)
  K2   PASS — every figure in title/subtitle/labels computed by build script from the formula, none typed
  5.3  PASS (print-applicable subset) — all text ≥ 12 px at design render (min 9.5 px labels at 150 dpi = 14 px equivalent); contrast per 2.3.7 table
  5.6  N/A — static
  5.7  PASS — light palette on Paper; no dark mode claimed
  7.1  PASS — second arrangement viewed by author-agent (log-scale replot considered and rejected: it would erase the magnitude contrast the title claims); panel run; author occupied no seat
  7.2  PASS — chart is agent-built; full checklist run, no presumption
  K6   PASS — reviewed at 540 px and 1050 px, recorded
  7.4  PASS — roster cast from brief with reasons; 3 domain + 1 viz seat; blindness and parallel spawn per skill; four items per seat with located numbers; all findings dispositioned; both widths supplied

PREFERENCES
  1.2  PASS — position on common scale
  1.3  PASS-BY-EXCEPTION (recorded) — not a time series; aspect chosen for label room; average-slope banking not meaningful for one exponential segment
  2.4  PASS — zero gridlines; endpoint and point labels carry decoding
  2.7  N/A — no categorical sort
  2.8  PASS — all text horizontal
  2.9  PASS-BY-EXCEPTION — "3,025" and "966" exceed 3 sig figs; exactness is the message (audit-table logic): these are exact combinatorial counts and the paper's credibility rests on them being exact
  5.4  PASS — Evergreen (L* 51.5) vs Rain (L* 71.4) separate in grayscale; both series direct-labeled; weights differ
  5.5  PASS — narrow render is a designed adaptation (drop order: formula off subtitle, annotation shortened, ticks thinned 4→3, labels reseated); no form change
  K4   PASS — ticks chosen per width by the build scripts, collision-checked at both renders

N/A: 1.4, 2.3.2, 2.3.4, 2.6, 4.5, 5.2, 5.6, 2.7

INVARIANT FAILURES: 0
PREFERENCE SCORE: 0 (three PASS-BY-EXCEPTION recorded above)

**Written exceptions carried by this figure:**
1. Type: DejaVu Serif / DejaVu Sans substitute for Source Serif 4 / Segoe UI — brand fonts unavailable in the build environment; serif-voice/sans-data pairing preserved. Re-render with brand fonts if this figure is ever reused on a Cascadia web property.
2. Print-safe application (author's decision, 2026-08-12): encodings chosen to survive grayscale print (lightness + weight + direct labels); no deviation from v2.5 was ultimately required.

VERDICT: SHIPS

---

# PANEL v2 — two-figure artifact (Figure A: n=1–4 · Figure B: n=1–8) — 2026-08-12

Trigger: author direction ("Try two charts. One for N=1-4, and one for N=1-8"; later: "Don't stack the charts. Just create 2 different charts"). Figure A built new; Figure B unchanged from v1 post-fix state. Material change to the artifact → fresh panel.

Roster: identical cast to v1 (same Rule 0.1 decision; reasons unchanged), **fresh agent instances** — no seat carried v1 context. Nature: simulated. Run: parallel, single spawn message. Widths given: both figures at 1050 px and 540 px (four renders per seat).
Blindness confirmed: design system ☑ · notes ☑ · source data ☑ · intended finding ☑ · other reviewers ☑

Pre-panel notes: **not recorded for this run** — the builder wrote no fresh defect list before spawning. N is therefore **not measured**, per the skill's instruction that a reconstructed N is worse than a missing one.

7.1 test: all four seats' sentences carried the titles' claims on both figures; all quoted numbers were located on canvas marks/labels. Seat 1 and Seat 2 independently verified the formula/ratios from the canvas ("I did the arithmetic in the margin and it held"; "301/90 ≈ 3.3, 966/301 ≈ 3.2, 3025/966 ≈ 3.1 — that checks out").

### Disposition table — v2

| # | Finding, in the reviewer's words | Seat(s) | Consensus | Defect? | Disposition | Rule |
|---|---|---|---|---|---|---|
| 1 | "Show me one of the 25 … one concrete instance and the whole thing lands" / "I'd want the person to walk me through one example" | 1, 3 | 2 | yes | **fixed** — worked example of the six n=3 configurations added to manuscript Section 2 (chart unchanged; a canvas cannot carry an enumeration) | 4.3 (manuscript-level) |
| 2 | "the single labels sitting on those shared points made me pause … which line owned them" / "a reader may wonder where the grey line starts" | 1, 4 | 2 | yes | **fixed** — shared-point labels at n=1, 2 set in neutral ink (Slate moss), owned by neither series | 3.6 |
| 3 | "as a parent of five, I fall in the crack between them … only the second chart has my number on it, in tiny print" | 3 | 1 | yes | **accepted** — figure ranges are the author's decision (typical range n≤4; full range n≤8); 90 is labeled on Figure B and Table 1 carries every value | 0.1 |
| 4 | "'double' is doing rhetorical work for a comparison of two quantities that aren't in the same units" | 2 | 1 | no | **rejected** — both series are counts over the same sibling set; a ratio of two counts is well-defined and the annotation states it accurately (6 vs 3) | — |
| 5 | "Does the grey line need to be on this chart at all? … it reads like a line that failed to plot" / "the pairs comparison did its work in Chart 1 … decoration" | 1, 2 | 2 | yes | **accepted** — the pairs line vanishing at scale IS Figure B's claim; removing it orphans the title's second clause; its readable values live in Figure A and Table 1 | 3.2 |
| 6 | "the titles are nearly identical sentences with different numbers … may take them for a repeated figure" | 1 | 1 | yes | **accepted** — parallel titles are deliberate (same claim shape, different range); captions and body text sequence the figures explicitly | 3.1 |
| 7 | "the '966' label crowds against the steep green segment" (narrow) | 3, 4 | 2 | yes | **fixed** — label moved clear of the segment in the narrow render | 5.5/K4 |
| 8 | "the disclaimer in nine-point subtitle text is the only thing standing between the reader and ['conflict factories'] … I'd want the surrounding article text to carry that caveat" | 2 | 1 | yes | **accepted (already satisfied)** — manuscript Section 3 carries the caveat in body text, as the seat recommends | 4.3 |
| 9 | "the annotation's leader line ends vaguely in the space between n=6 and n=7" (narrow) | 4 | 1 | yes | **accepted** — minor; partially improved by the same label move; the note is about the whole series | 3.4 |
| 10 | "Chart 1 could live as an inset in Chart 2's empty upper-left" | 1 | 1 | no | **rejected** — author decision 2026-08-12: figures stay separate ("Don't stack the charts") | — |

### Panel summary — v2

```
PANEL v2: 4 seats, simulated · 2 charts (2 widths each) · findings 10 · defects 8 · novel n/m
          fixed 3 · accepted 5 · rejected 2
          D = 4.0 defects/chart · N = not measured (no pre-panel list recorded) · R = 0.20
          Widths read: 1050 px, 540 px (both figures)
```

### Figure A checklist note

Figure A was run through Checklist A with the same mechanics as Figure B (same build pipeline, palette, type, strip, labels). Deltas worth recording: 2.9 needs no exception (all values ≤2 significant figures); K1 PASS (y 0–27.25 contains 0–25, derived); 3.2 PASS — 25 and 6 both carried by end-of-line labels on plotted marks, and the annotation's "double" is verifiable from the printed 6 and 3. Same three written exceptions carry over (fonts; print-safe application; banking N/A). INVARIANT failures 0 · preference score 0.

VERDICT (both figures): SHIPS

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

---

# PANEL v3 — web renders (figure1_web · figureA_web) — 2026-08-13

Trigger: a third build target added for the web — brand fonts (Source Serif 4 / Segoe UI, previously substituted by DejaVu) and in-chart type sized for the 324 px mobile slot. New artifacts no panel had read → fresh panel.

**Why the widths matter here.** v1 read at 1050 px and v2 at 1050/540 px. The live page displays the figure column at **324 px** — a width no panel had ever read these charts at. That is the gap this panel exists to close, and it is why the seats were given 324 px and 355 px and nothing else.

```
READING PANEL — sibling-conflict web renders — 2026-08-13
Decision served (Rule 0.1): whether a general reader of the public essay accepts the
  piece's claim and understands it as a combinatorial possibility space rather than a
  prediction about their own household; and whether a mathematically literate reader
  arriving from the linked manuscript trusts the piece enough to read it.
Charts panelled: 2   States: static renders at 324 px and 355 px
Nature: simulated

  Seat 1  Parent of four, non-technical      — simulated — why this seat: the least
          technical real reader, and the person the artifact is literally about. Rule 0.1
          names a general essay audience; a roster of three experts would assume a
          literacy this page does not have.
  Seat 2  Research mathematician,            — simulated — why this seat: the reader who
          enumerative combinatorics                       arrives from the Intelligencer
          submission and decides whether the popular presentation is one they would cite
          without embarrassment. Owns the question of whether the counted object matches
          the stated formula.
  Seat 3  Family therapist, 20 years         — simulated — why this seat: the decision has
          clinical practice                              a harm dimension no analyst seat
          reaches — what a distressed parent believes after reading it. Orthogonal to both
          the maths and the design.
  Seat 4  visualization reader               — simulated — canvas only; tables and
                                                           arithmetic excluded

Blindness asserted: design system ☑ · review and build notes ☑ · source data ☑ ·
                    intended finding from outside the artifact ☑ · other seats' output ☑
Run: parallel ☑ (single spawn message, four fresh agents)
Author's pre-panel notes recorded: ☑  (pre-panel-notes.md, 2026-08-13, 12 items, written
                    before any seat was cast — so N is measured for this panel)

Roster caveat, recorded rather than smoothed over: the domain-seat prompt says "in a
meeting". For Seat 1 that framing is nonsense — a parent meets this page on a phone —
so the encounter clause was changed for that seat and left verbatim elsewhere. No other
deviation from the skill's seat prompts.
```

### Two seat claims verified before disposition, not taken on trust

Seat 2 asserted that the grey series is a **sub-count of the green one**. Checked by brute-force enumeration over all 3ⁿ assignments rather than from the closed form: the count of configurations in which both opposing sides are singletons equals C(n,2) at every n from 1 to 8 — 28 at n = 8, 6 at n = 4. It is exact, and the enumeration also reproduced the published formula at every n.

Seat 2 and Seat 4 independently asserted that **"roughly triples" is asymptotic**. Also confirmed: successive ratios run 6.00, 4.17, 3.60, 3.34, 3.21, 3.13, approaching 3 from above. Across Figure A's entire plotted range the growth factor is 6.00 then 4.17.

### Disposition table — v3

Sorted by consensus descending. Charts: **1** = figure1_web (n = 1–8), **A** = figureA_web (n = 1–4).

| # | Finding, in the reviewer's words | Seats | n | Chart | Defect? | Novel? | Disposition | Rule |
|---|---|---|---|---|---|---|---|---|
| 1 | *"the word 'conflict' is in the title, in the label on the line, and in the note in the middle of the chart, and that's what I'll remember an hour from now — not the disclaimer"* / *"the subtitle is the third thing she reads and it's in grey"* | 1, 3 | **2** | 1, A | yes | yes | **escalated** — the caveat already sits in manuscript body text (v2 finding 8) and in the page prose, but both seats reached the same place independently and Seat 3 states the harm concretely. Renaming the plotted quantity is an editorial change to a term used throughout a manuscript under query. Author's call | 3.2 |
| 2 | *"The grey series carries no visual information at all; it is a text label with a line drawn under it"* / *"I could not read 28 off the plot at all"* | 2, 4 | **2** | 1 | yes | no | **accepted** — unchanged from v2 finding 5: the pairs line vanishing at scale *is* Figure 1's claim, and removing it orphans the title's second clause. Figure A carries the readable values | 3.2 |
| 3 | *"the growth factor is 6 then 4.17, nowhere near three, and there's nothing here telling a reader that the tripling is asymptotic"* / *"a reader who took 'each added child' literally across the whole x-range would be misled by a claim they cannot see"* | 2, 4 | **2** | 1, A | yes | yes | **escalated** — verified above. The annotation wording is shared with the manuscript figure, so this cannot be fixed in the web render alone without the two disagreeing. Author's call | 3.2, 3.4 |
| 4 | *"I couldn't tell whether n = 4 is a deliberate second case or just the first chart zoomed"* / *"Why am I being shown the same chart twice, and which of the two am I supposed to be taking the point from?"* | 1, 2 | **2** | 1, A | yes | yes | **accepted** — page prose sequences the two figures, consistent with v2 finding 6. Noted as a genuine 4.3 exposure: on the web these travel further apart than in the manuscript, and an embed carries neither | 4.3 |
| 5 | *"The '966' label collides with the curve. The annotation's leader line runs straight through it"* / *"966 and 301 are pressed so close to the line I had to squint"* | 1, 4 | **2** | 1 | yes | no | **fixed** — label moved below-right of its own marker, clear of both the segment and the leader. First attempt (directly above the marker) only relocated the collision; the segment climbs through that space too | 5.5 |
| 6 | *"Nothing telling me how many of those 3,025 have ever actually occurred in a real household"* / *"how many of those three thousand ever actually happen, and there isn't one"* | 1, 3 | **2** | 1, A | no | — | **rejected** — the subtitle states the chart is a possibility space and the piece makes no empirical claim. Supplying an occurrence rate would be a different piece resting on data that does not exist. The convergence is noted: it is the question the framing invites, which is what finding 1 is about | — |
| 7 | *"a 6-year-old and a 15-year-old aren't the same kind of pairing, and this counts them as identical"* / *"The chart treats all eight children as interchangeable pieces"* | 1, 3 | **2** | 1, A | no | — | **rejected** — the combinatorial model is over unlabelled children by construction; a chart cannot carry an assumption the model does not make. Worth a sentence in the prose, not a change to the figure | — |
| 8 | *"Do you know that your grey line is a sub-count of your green line? C(8,2) = 28 is exactly the number of configurations in which both opposing sides are singletons … So this isn't '3,025 possibilities versus 28 pairs,' it's 'all faction splits versus the two-person ones'"* | 2 | 1 | 1, A | yes | yes | **escalated** — verified exactly, above. The strongest finding in the panel and the only one that touches the claim rather than its presentation: the title's "but form only" contrasts a set with its own subset. Single-seat, but a verified mathematical fact does not need consensus. Cannot be resolved in the web render without diverging from a manuscript under query. **Author's call, and it is the one that should be made first** | 3.2, 1.1 |
| 9 | *"'28' sits below the axis line, at the same height as the '8' tick label, which makes it momentarily read as part of the axis rather than as a series endpoint. I looked at it twice"* | 4 | 1 | 1 | yes | yes | **fixed** — introduced by this build's measured gutter, which wrapped the short end label onto two lines. The gutter now also has to hold that label whole, so it no longer reaches axis height. Incidentally resolves the pre-panel note that Figure 1 wrapped it and Figure A did not | 3.6 |
| 10 | *"The grey '3' label is the weakest text on either chart … the vertical stack of 6-over-3 near x = 3 momentarily reads as one series' labels"* | 4 | 1 | A | yes | yes | **fixed** — the "3" moved clear of the "6". The seat's reason for weighting it is the right one: the annotation's doubling claim is verifiable only from those two numbers | 3.4 |
| 11 | *"The grey series is occluded from n=1 to n=4 … A reader could reasonably conclude the grey series starts at 5"* | 4 | 1 | 1 | yes | yes | **accepted** — at a 0–3,025 scale both series sit inside a percent of the baseline through n = 4. This is the condition Figure A was created to answer (v2), and it answers it | 3.6 |
| 12 | *"The endpoint at 25 sits above the highest labelled tick (20) … the reader estimates by extending the spacing"* | 4 | 1 | A | yes | yes | **accepted** — y-ticks match the design and narrow renders, ylim contains the value (v2 recorded K1 PASS), and the endpoint carries a direct label. Half a tick of extrapolation | 2.4 |
| 13 | *"children are integers, and the connecting line invites reading a value at 4.5 children"* | 4 | 1 | 1, A | yes | yes | **accepted** — markers are drawn at every integer and the line is a reading aid, unchanged from the renders v1 and v2 cleared. Recorded because no prior panel raised it | 4.1 |
| 14 | *"you need both conventions pinned down for S(n+1,3) to be the right answer, and the subtitle gives neither … that is a pointer, not a definition"* | 2 | 1 | 1, A | yes | yes | **accepted** — the manuscript defines the construction and the page prose carries it. Recorded as the same 4.3 exposure as finding 4: the chart alone does not define its own object | 4.3 |
| 15 | *"the crossing happens at n = 3 and the word 'already' reads to me like it happened earlier than expected, when in fact it's the first place anything separates at all"* | 2 | 1 | A | yes | yes | **escalated** — correct on the arithmetic (n=1 is 0 v 0, n=2 is 1 v 1, n=3 is 6 v 3). Annotation wording is shared with the manuscript's Figure A. Author's call | 3.4 |
| 16 | *"'6' appears twice on this chart for two different things … I read the grey 6 first and briefly thought the lines had met"* | 2 | 1 | A | yes | yes | **accepted** — both are true values on their own marks, in different inks, and finding 10's fix increases the separation. Retained as a known read hazard of the n ≤ 4 range | 3.6 |
| 17 | *"I got stuck for a second on 'Ways n children can split' … I haven't done letters-instead-of-numbers since school and I nearly stopped reading there"* | 1 | 1 | 1, A | yes | yes | **accepted** — subtitle wording is shared with the narrow renders and the manuscript. Flagged rather than fixed because it is the only finding that reports a reader nearly stopping, and Rule 0.1 puts this seat's literacy at the centre of the decision | 0.1 |
| 18 | *"No y-axis title. Defensible here, since the axis carries two different units"* | 4 | 1 | 1, A | no | — | **rejected** — both series are counts over the same sibling set (v2 finding 4 rejected on the same basis) and each carries a direct end label. The seat reached the same conclusion itself | — |
| 19 | *"The green series' value at n=1 is 0 and is unlabelled, so the curve appears to start 'at the axis' without saying so"* | 4 | 1 | 1 | no | — | **rejected** — the value is zero and it is drawn at zero. Figure A labels it, for the range where it matters | — |

### Panel summary — v3

```
PANEL v3: 4 seats, simulated · 2 charts (2 widths each) · findings 19 · defects 15 · novel 13
          fixed 3 · accepted 8 · escalated 4 · rejected 4 · multi-seat defects 5
          D = 7.50 defects/chart · N = 0.87 novel share · R = 0.21 rejected share
          Widths read: 324 px, 355 px (both figures)
```

**`escalated` is not one of the skill's three dispositions.** It is recorded here rather than folded into `accepted` because four findings — 1, 3, 8, 15 — cannot be settled by the agent: each would change wording or a claim shared with a manuscript currently under query at The Mathematical Intelligencer, where changing the figures mid-query costs the "this is what they received" property. Calling them `accepted` would assert a judgement nobody made. **The panel is therefore open, not closed.**

**On D = 7.50, against v1's and v2's 4.0.** The rise is not a regression in the charts. Three causes, in the order they contribute: the reading width dropped to 324 px and surfaced collisions no 1050 px panel could see; pre-panel notes were recorded this time, so N is measured rather than absent and the disposition was stricter about what counts; and Seat 4 was unusually thorough. D is a count of candidate defects, not a quality score, and three of the fifteen were introduced by this build and fixed within it.

**Visualization-seat share, per the skill's instruction to track it:** Seat 4 raised 10 of 19 findings (53%), against the ~68% recorded on the Deal Desk panel. The three domain seats produced findings 1, 4, 6, 7, 8, 14, 15, 16, 17 between them, including the one verified mathematical error. On this run the domain floor of three earned its place — a two-seat roster that dropped the mathematician would have missed finding 8 entirely.

**7.1 note.** All four seats' sentences carried the titles' claims, and every quoted number was located on a mark, an axis or a label — except Seat 2's and Seat 4's 28 on Figure 1, which both stated plainly they could not read off the plot. That is finding 2, and it is the return doing exactly the work the "where did you get it" field exists to do.

### No verdict is issued for v3

The checklist has not been run against the web renders, and four findings are open pending the author. Recording `SHIPS` here would carry a claim neither the panel nor the checklist supports. The renders are built, three panel defects are fixed, and the remaining decisions are Aaron's.

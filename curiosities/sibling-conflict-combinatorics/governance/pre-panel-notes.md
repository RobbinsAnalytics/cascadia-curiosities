# Pre-panel notes — builder's own defect list, recorded before the panel ran
2026-08-12 · figure1 (design + narrow renders) · author of record: Aaron Robbins; chart built by agent

1. The Sibling pairs (Rain) series hugs the zero line and is nearly flat at this scale; a reader may not register it as a series at all, only as a baseline.
2. Values for n = 1–4 on the Evergreen series are visually indistinguishable from zero; the sixfold jump from 1 to 6 configurations is invisible at this y-range.
3. The annotation's "roughly triples" mechanism is not verifiable from the marks by eye; ratios between successive points are not readable on a linear scale.
4. "3,025" is four significant figures against Rule 2.9's three; defended as exact combinatorial counts (exactness is the message).
5. Type substitution: DejaVu Serif/Sans stand in for Source Serif 4/Segoe UI (fonts unavailable in build environment).
6. Declared relationship is "magnitude" but the two-line-over-n form reads like change-over-time; possible 1.1 ambiguity.

---

2026-08-13 · figure1_web + figureA_web · author of record: Aaron Robbins; charts built by agent

Recorded before Panel v3 ran and before any seat was cast. These are the web
renders for the 324 px mobile slot, at brand fonts and larger in-chart type.

Carried over from the design and narrow renders, unchanged by this re-render:

1. The Sibling pairs (Rain) series still hugs the zero line on figure1_web and reads as a baseline rather than a series.
2. Values for n = 1–4 on the Evergreen series remain visually indistinguishable from zero at this y-range; Figure A exists to carry them.
3. "roughly triples" is still not verifiable from the marks by eye — successive ratios are not readable on a linear scale.
4. "3,025" is four significant figures against Rule 2.9's three; same defence as before, the counts are exact and the exactness is the message.
5. Declared relationship is "magnitude" but the two-line-over-n form still reads like change-over-time; the 1.1 ambiguity is unchanged.

Closed by this re-render:

6. Type substitution is gone. Source Serif 4 and Segoe UI both resolve, asserted by family and by glyph coverage at build time. This remains open for the manuscript figures, which are deliberately untouched.

New, introduced by this re-render — my own list, not the panel's:

7. The plot occupies only ~52% of the canvas width; the end labels claim a 1.18 in gutter. The charts may read as mostly text with the marks squeezed.
8. "Sibling pairs: 28" wraps to two lines on figure1_web while "Sibling pairs: 6" stays on one on figureA_web. The two figures are meant to be read together and this is visibly inconsistent.
9. The chart subtitle at ~13.5 css px is still smaller than the 15.3 px page caption printed directly beneath it. Better than the 9.8 px it replaces, but the hierarchy is still inverted against the page.
10. On figure1_web the 90 / 301 / 966 value labels sit close to both the curve and the annotation's leader line; possible crowding at 324 px.
11. Aspect is held at the narrow renders' 540×630 portrait. That was inherited, not designed for this type size, and the plot is now short relative to its width.
12. Wording follows the narrow renders, so the annotation reads "triples the possibilities" where the manuscript figure reads "triples the space of possible conflicts". A reader moving between the page and the linked PDF sees two wordings.

# Research record — Sibling Conflict Combinatorics — 2026-08-12

The research phase behind the manuscript, recorded so the trail from spec to submission is complete. Aaron spec'd the problem (research tasks 1–5 in `original-handoff.md`); the agent executed; Aaron approved dispositions and the final write-up.

## 1. Formula verification

Two independent confirmations of C(n) = (3^n − 2·2^n + 1)/2:

- **Brute force.** Enumerated all 3^n assignments of n children to {side A, side B, uninvolved}, kept those with both sides nonempty, halved for label symmetry. Matches the formula exactly for n = 1–8: 0, 1, 6, 25, 90, 301, 966, 3025. (Script logic preserved in the manuscript's derivation; original run 2026-08-12.)
- **Closed form.** The sequence is the Stirling numbers of the second kind S(n+1, 3), OEIS A000392, whose listed formula a(n) = (1 + 3^(n−1) − 2^n)/2 gives a(n+1) = (3^n − 2·2^n + 1)/2. The OEIS entry (comment by Navarrete) characterizes a(n+1) as the number of disjoint unions of two nonempty subsets of an n-set — exactly the conflict-configuration definition. https://oeis.org/A000392

## 2. Citations vetted

Game theory / coalition structure:
- Rahwan, Michalak, Wooldridge & Jennings, "Coalition structure generation: A survey," *Artificial Intelligence* 229 (2015) 139–174. https://www.sciencedirect.com/science/article/pii/S0004370215001198
- Sandholm, Larson, Andersson, Shehory & Tohmé, "Coalition structure generation with worst case guarantees," *Artificial Intelligence* 111 (1999) 209–238.
- OEIS A000392 (above).

Family systems / sibling relations:
- Minuchin, *Families and Family Therapy* (1974) — coalitions in structural family therapy.
- Caplow, *Two Against One: Coalitions in Triads* (1968) — coalition theory applied to families; the bridge source. https://www.journals.uchicago.edu/doi/10.1086/224888
- McHale, Updegraff & Whiteman, "Sibling relationships and influences in childhood and adolescence," *JMF* 74 (2012) 913–930.
- Bank & Kahn, *The Sibling Bond* (1982).

Empirical grounding (Section 3 of the manuscript):
- Hank & Steinbach, "Sibling estrangement in adulthood," *JSPR* 40 (2023) 1277–1287 — 28% of German panel respondents estranged from ≥1 sibling. https://journals.sagepub.com/doi/full/10.1177/02654075221127863
- Jensen, Ashby, Noorda & Jasperson, "The more, the merrier? Young adults' sibling relationship quality in medium to large families," *JSPR* (2026). https://journals.sagepub.com/doi/10.1177/02654075241302240

## 3. Novelty check — the load-bearing finding

No published work found connecting opposing-sides coalition counting to sibling conflict. **Close prior art exists and is cited rather than hidden:**
- Bossard, "The Law of Family Interaction," *AJS* 50 (1945) 292–294 — family relationships grow as n(n−1)/2. https://www.journals.uchicago.edu/doi/abs/10.1086/219621
- Kephart, "A Quantitative Analysis of Intragroup Relationships," *AJS* 55 (1950) 544–549 — extended to possible subgroupings. https://doi.org/10.1086/220616

Consequence: the paper's novelty claim was narrowed from "not addressed" to "extends the Bossard–Kephart tradition to opposing-sides configurations." Adjacent formalism noted and distinguished: three-way conflict analysis (Pawlak tradition; Lang, Miao & Cai 2017), which analyzes a given conflict rather than counting the space.

## 4. Publication landscape (as of 2026-08-12)

Prestige (realistic for a non-academic): *The Mathematical Intelligencer* (chosen; queried 2026-08-12), *Journal of Humanistic Mathematics* (verified open, publishes non-academics, no fees — fallback; requires anonymization, abstract, and their reference style), *Recreational Mathematics Magazine* (active, Issue 22 June 2026), *Math Horizons*.

Widest readership: Nautilus (open to themed pitches, pays), Aeon/Psyche (ideal fit, closed to pitches at check date), Chalkdust (open to anyone), Plus Magazine, The Aperiodical, self-publication.

Constraint: both target journals require exclusive submission — one at a time.

## 5. Process notes

- Figures built to Cascadia VIZ-PRINCIPLES v2.5, print-safe application; reviewed under CHART-REVIEW v2.5. Two Rule 7.4 reading panels run (v1 single-figure, v2 two-figure pair); full records in `../governance/chart-review.md` and `../governance/panel-returns.md`.
- Springer preprint policy verified: posting the submitted version on a personal site is permitted and is not prior publication; disclose at formal submission. https://www.springer.com/gp/editorial-policies/preprint-sharing

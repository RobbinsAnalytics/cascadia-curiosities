# Cascadia Curiosities

**Work built to the Cascadia standard that isn't a business-intelligence
module.** Papers, essays, and one-off charts — the same governance, a different
subject.

The Cascadia module repos publish analytics. This one publishes curiosity: a
question worth counting, worked properly. What carries over is the method — a
declared reader, a chart that has to survive a blind reading panel before it
ships, and a research record that shows the trail from question to result,
including the parts that didn't hold up.

## Layout

```
curiosities/
  sibling-conflict-combinatorics/
    manuscript/       manuscript.tex and the compiled PDF as sent
    figures/          figure PDFs and PNGs (design + narrow), and the scripts that build them
    governance/       chart review, reading-panel returns, pre-panel notes
    research/         research record, the original spec, the working draft
    correspondence/   what was sent, and to whom — status lives here
docs/                 the handoff that created this repo
```

Every piece is self-contained: its own governance, its own research record, its
own correspondence. A piece can be read start to finish without leaving its
folder.

## The resident

### The Combinatorics of Sibling Conflict

Four children, each two years apart, and a question that started at a kitchen
table: how many distinct ways can they take sides against each other? The answer
for four children is 25. In general, the number of ways *n* children can split
into two opposing sides with the rest uninvolved is

> (3ⁿ − 2·2ⁿ + 1) / 2

which is the Stirling number of the second kind *S*(*n*+1, 3), OEIS
[A000392](https://oeis.org/A000392). Four kids form 6 sibling pairs but allow 25
conflict configurations; eight kids form 28 pairs and allow 3,025. Pairs grow
quadratically, conflict configurations grow exponentially.

The paper extends the Bossard (1945) and Kephart (1950) counting tradition to
opposing-sides configurations and connects it to coalition-structure generation
in cooperative game theory. It is explicit about its own limits: it measures a
possibility space, not behavior. It does not predict how often real siblings
fight, or how badly.

**Status: queried to *The Mathematical Intelligencer* on 2026-08-12; awaiting
reply.** Status is tracked in the piece's `correspondence/` folder, which is the
thing to read before acting on this piece.

## The standard behind it

The visualization rules — `VIZ-PRINCIPLES.md` and `CHART-REVIEW.md`, currently
v2.5 — live in `cascadia-standards` and are read-only reference from here. The
part worth knowing without opening them: **a chart ships only after a blind
reading panel**, where reviewers who have seen nothing but the rendered image
write down what they think it says. If their sentence isn't the chart's claim,
the chart is the defect. Both figures in the resident paper were changed by that
process, and the second figure exists only because a panelist said the first one
couldn't show them their own family.

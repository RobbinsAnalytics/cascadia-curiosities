# Reading panel — verbatim returns — Figure 1 — 2026-08-12

Four seats, simulated, run in parallel from a single spawn message. Each seat saw only the two rendered PNGs (1050 px design, 540 px narrow). Charts referred to as Chart 1 (design) and Chart 2 (narrow).

---

## Seat 1 — Mathematics magazine editor

**Chart 1 (full size)**

1. The sentence. It's a nice "combinatorial explosion versus linear intuition" figure — the number of ways eight kids can split into two warring camps is over three thousand, while the number of sibling pairs is only 28, and the green curve shooting up against a flat grey line makes that point at a glance.

2. The number. 3,025 — it's printed right at the end of the green curve, in the label "Conflict configurations: 3,025," and it agrees with where the last dot sits, just above the 3,000 gridline on the left axis. I'd also repeat 28, from the "Sibling pairs: 28" label at the end of the grey line. Both numbers are also in the title, which is where I'd actually have got them first.

3. The question. What exactly counts as a "conflict configuration"? The subtitle gives me a formula — (3ⁿ − 2·2ⁿ + 1)/2 — and says "two opposing sides," but the 3ⁿ tells me some children must be sitting out, and nothing on the figure says that in words. A general reader will wonder why splitting 8 kids into two sides gives 3,025 rather than 2⁷ − 1 = 127. If the answer is "some kids are neutral," that needs to be on the page.

4. The gap. Any readable values for the grey line. The sibling-pairs line is the other half of the comparison the title makes, and on this scale it's a flat smear at zero — I can't see it go from 1 to 28, I just have to take the end label's word for it. I also looked for the annotation's "roughly triples" claim to be checkable and it isn't, really: the only labelled points are the endpoints, so the tripling is asserted, not shown. And the source line cites OEIS A000392 and "S(n+1, 3)" — Stirling numbers — with no bridge from that to "conflicts," which will stop exactly the readers of a math magazine who go look it up.

**Chart 2 (single-column width)**

1. The sentence. Same figure squeezed into a column, and it survives — the title, the 3,025 endpoint, the flat grey line, and the tripling note all still read.

2. The number. Still 3,025, from the "Conflict configurations: 3,025" label beside the top of the green curve, sitting just above the 3,000 tick. The y-axis here has only three labels — 0, 1,500, 3,000 — but the endpoint label does the work, so I don't miss the ticks.

3. The question. Same as the wide version — what is a conflict configuration, and where do the "neutral" children in that 3ⁿ go? The subtitle got compressed to "Two-sided splits of n children," which is actually *more* misleading than the long version: a two-sided split of 8 children is not 3,025 things, so the shortened wording now says something the formula next to it contradicts.

4. The gap. Same as the wide one — no readable grey line, no intermediate values to verify the tripling. Nothing new broke at column width; the footer wraps to two lines and the annotation crowds the curve a bit, but I could read everything. My only production note is that everything hangs on the small superscript ⁿ in the subtitle formula — at this size it's already borderline, and on newsprint (3ⁿ − 2·2ⁿ) could easily read as (3 − 2·2), which turns the formula into nonsense. I'd want that set as a real equation, not superscript unicode in a caption font.

If I had to give a verdict: the figure earns its space — the takeaway is in the title and the picture backs it up — but the definitional gap in question 3 is the thing I'd bounce it back for, on both versions.

---

## Seat 2 — Quantitative family-studies researcher

**Chart 1 (figure1_design.png, full size)**

1. The sentence. I'd tell a colleague it's a chart showing that the number of mathematically possible two-sided splits of a sibling group explodes as family size grows — 3,025 for eight kids versus 28 pairwise relationships — and that it's arithmetic, not data about anything siblings actually do.

2. The number. 3,025 — it's printed right on the end of the green line, in the label "Conflict configurations: 3,025" at the top right, and it's also in the title. The endpoint dot sits just above the 3,000 gridline on the left axis, so the label and the axis agree.

3. The question. What licenses calling a two-sided partition a "conflict configuration"? In my literature, sibling conflict is overwhelmingly dyadic; whole-family coalitional splits into exactly two opposing camps are rare and hard to observe even in small families. If this is meant to say anything about families rather than about the number 3^n, I'd want to know whether even one of those 3,025 configurations has an observed base rate attached to it. The subtitle formula and the footer ("OEIS A000392, S(n+1, 3), exact counts, nothing estimated") tell me this is pure combinatorics — so I'd ask, bluntly: is there any family data behind this at all, or is the family framing a metaphor?

4. The gap. Any empirical quantity. I looked for a frequency, a prevalence, an observed count of coalitional conflicts in real sibling groups — anything that would connect "possible" to "actual" — and there is none. The chart is internally honest about that (it says the counts are exact and computed), but the title's phrasing "eight children allow 3,025 possible conflict configurations" invites a behavioral reading the chart has no data to support. I also couldn't find a definition of what one "side" is — does a child abstaining count, since the formula appears to allow children on neither side? The formula implies a third category exists but the prose never says so.

**Chart 2 (figure1_narrow.png, single-column width)**

1. The sentence. Same figure squeezed to column width — combinatorial possible two-way splits of n children shooting up to 3,025 at n=8 while pairwise relationships crawl along at 28 — and it survives the shrink; I'd say the same thing about it I said about the big one.

2. The number. Again 3,025, from the "Conflict configurations: 3,025" label on the line's endpoint at top right, which sits at the 3,000 gridline. The 28 comes only from the "Sibling pairs: 28" label — at this width the gray line is visually indistinguishable from zero, so the label is the only place that number exists on the chart.

3. The question. Same as before — what is a "conflict configuration" operationally — plus one specific to this version: the subtitle here says "two-sided splits" where the wide version spelled out "two opposing sides." If this is the version going to print, that terser phrasing does even less to signal that this is a hypothetical possibility space, so I'd ask whether the caption in the manuscript carries the disclaimer the chart itself doesn't.

4. The gap. Beyond the missing empirical anchor (same as Chart 1): the y-axis here has only three labeled values — 0, 1,500, 3,000 — so the intermediate points at n=5, 6, 7 can't really be read off the axis; the annotation says "roughly triples" and I have to take its word for it, since the n=7 point (somewhere near 950?) is the only intermediate value I could even estimate. I looked for the actual values at n=5 through 7 and couldn't recover them from this version. Legible, but the shape is all it communicates below n=8.

One overall note, since both are the same figure: as a piece of math the chart is clean and self-documenting — exact counts, formulas shown, source given. My reservation isn't with the chart's execution; it's that "conflict configuration" is doing rhetorical work no construct definition supports, and I could not establish from either version whether the authors intend a behavioral claim or a metaphor.

---

## Seat 3 — Parent of five, non-technical

**Chart 1 (full size)**

1. The sentence. It's a chart saying that with eight kids there are three thousand different ways they could split up and fight, even though there are only 28 actual pairs of kids — basically, the more kids you have, the ways they can gang up on each other explodes.

2. The number. The 3,025 — it's written right at the end of the green line at the top right, in the label that says "Conflict configurations: 3,025," and the dot it's attached to sits right at the 3,000 mark on the left axis. That's the one I'd repeat: eight kids, over three thousand ways for a fight to shape up.

3. The question. I have five kids, not eight — what's my number? The line for five looks like it's barely off the floor, and I honestly can't read a value off it. The dot at 5 is squashed down near zero, so I'd ask them to just tell me what five children works out to.

4. The gap. Two things I looked for. First, the number for my own family size — five — and I couldn't read it because everything below six kids is flattened against the bottom of the chart. Second, anything about how often fights actually happen. This is all "possible" configurations, which is a math fact, not a parenting fact. I wanted something that told me whether the refereeing in my house is normal, and this doesn't say anything about real fights, just how many are theoretically available. Also that subtitle with the formula — (3 to the n minus something over 2) — went straight past me; I skipped it and read the title instead, which carried the whole thing anyway.

**Chart 2 (narrow, single-column)**

1. The sentence. Same chart, same takeaway — eight kids means about three thousand possible ways a conflict can line up, but only 28 pairs of siblings — it still reads fine at the smaller size.

2. The number. Again the 3,025, from the "Conflict configurations: 3,025" label at the end of the steep green line, top right, with the dot sitting at the 3,000 gridline. The "Sibling pairs: 28" label at the end of the flat grey line is the other one I'd quote — those two together are the whole story.

3. The question. Same as before — where do five kids land on this? If anything it's harder to tell here, because the chart is smaller and the dots at 4, 5, and even 6 are all mashed down near zero. And a second small one: the note in the middle says each added child "roughly triples" the possibilities — triples from what, and does that mean going from five to six kids triples my problems?

4. The gap. Same gaps as the big version. No readable numbers for anything under about seven kids — the left half of the chart is just dots on the floor — and nothing connecting "possible conflicts" to actual conflicts. The italic note about tripling now sits stacked over the middle of the chart and its little pointer line points at the dot for 7, which took me a second to follow, but it didn't stop me reading. The fine print at the bottom about "OEIS A000392" means nothing to me — I'd have liked one plain-English line saying where this math comes from or why I should trust it, though the "exact counts, nothing estimated" bit did register.

Overall, honestly: both versions are clear on the one thing they're saying, and the narrow one holds up. My only real complaint is that the chart is about families like mine and I still can't find my own family on it.

---

## Seat 4 — Visualization reader (canvas only)

**Chart 1 — figure1_design.png (full size)**

1. What is it about? Before reading the title: two series against "Number of children" (1–8) on the x-axis. A green curve that hugs zero until about n=5 and then explodes to ~3,000, and a grey line that stays flat along the baseline. Clearly a "combinatorial explosion vs. linear-ish growth" picture. Then the title: "Eight children allow 3,025 possible conflict configurations, but form only 28 sibling pairs." That matches what I inferred — the title and picture agree.

2. Does the picture support the title? The title makes three claims:
- *3,025 conflict configurations at eight children* — visible. The green curve terminates at x=8 with a dot at just above the 3,000 gridline, and a direct label reads "Conflict configurations: 3,025." Supported by the plot, not just the label.
- *Only 28 sibling pairs* — half supported. The grey line is drawn and labelled "Sibling pairs: 28," but on a 0–3,000 axis, 28 is indistinguishable from zero. I can see that it is small; I cannot see that it is 28, or even that it grows at all. The number 28 is taken entirely on faith from the end label. That is arguably the point of the chart — the contrast is the message — but the second series contributes no readable information beyond "flat."
- *Eight children* — visible; x-axis runs 1 to 8 and the endpoint sits at 8.

The annotation "Each added child roughly triples the space of possible conflicts" is a fourth claim. On a linear axis a constant ratio reads as a curve, so the tripling cannot be verified visually — the step from 7 (~950) to 8 (~3,000) is plausibly a tripling, but the earlier steps are all squashed into the baseline. A log axis would show tripling as a straight line; this axis asks me to take it on faith.

3. Right kind of chart? Mostly yes. The claim is a *contrast in magnitude and growth rate*, and a two-series line chart shows that. But there is a tension: the linear axis dramatizes the gap at n=8 while destroying everything else — the tripling claim, the sibling-pairs series, and the first five points of the green series are all illegible at this scale. If the message is "the gap is enormous," this chart works. If the message includes "roughly triples each time," the form contradicts the annotation.

4. Hard to read?
- The sibling-pairs series is a flat grey line at zero — its shape, its values, even whether it has markers, all unreadable.
- Green data points at n=1 through 4 sit on top of each other at the baseline; I cannot read any of them.
- The subtitle's formula, "(3ⁿ − 2·2ⁿ + 1)/2," is legible but dense; fine for a technical audience.
- The annotation's leader line points at the n=7 point, which is slightly odd — the sentence is about the whole series, and the arrow could be misread as saying something specific about n=7.
- Minor: the y-axis has labels at 0, 1,000, 2,000, 3,000 with no visible gridlines (or extremely faint ones), so "just above 3,000" is read against the tick label alone.

5. Survives grayscale? Yes. Dark green becomes dark grey, light grey stays light grey, and the weights differ (thick vs. thin). The direct end-labels name each series, so no legend-to-line colour matching is required. This one is safe.

6. The number. 3,025 conflict configurations at 8 children — read from the endpoint dot at x=8, sitting just above the 3,000 y-axis tick, confirmed by the adjacent label "Conflict configurations: 3,025." That number is genuinely on the plot. The 28, by contrast, exists only as text; the plot itself would let you claim anything from 0 to ~50 for that series.

**Chart 2 — figure1_narrow.png (single-column width)**

Same figure, so the substantive answers to 1–3 carry over: same title, same two series, same claims, same supported/on-faith split. What changes at this width:

2/3 (differences from Chart 1). The subtitle is rewritten — "Two-sided splits of n children" instead of "Ways to split n children into two opposing sides" — a genuine adaptation, not just reflow. The y-axis now ticks at 0, 1,500, 3,000 instead of thousands, which is slightly coarser but adequate since only the endpoint matters. Everything the title claims is still on the chart.

4. Hard to read?
- The annotation now occupies the whole upper-left quadrant, four lines deep, and its leader line has to travel a long way down to the curve. It dominates the plot area at this size.
- The endpoint dot at 3,025 sits very close to the top edge; the "Conflict configurations: 3,025" label is pushed right against the chart boundary. Nothing is actually cut off, but it is tight.
- The "Sibling pairs: 28" label now wraps to two lines and sits above the x=8 area, floating some distance from the flat grey line it names — I had to look twice to confirm which mark it belonged to.
- The n=1–5 baseline pile-up is worse at this size; points 1 through 5 are effectively one smear.
- Footer text wraps to two lines but remains legible. This is a competently adapted narrow version, not a naive shrink.

5. Survives grayscale? Same as Chart 1 — yes, on line weight and direct labels.

6. The number. Same one: 3,025 at x=8, endpoint dot against the 3,000 tick plus its label. And the same caveat: 28 is quotable only from the text label, not from anything drawn.

Summary: both charts are the same figure at two widths, and both are fundamentally sound: title, annotation and plot tell one consistent story, they survive grayscale, and the headline number (3,025) is readable off the plot. The recurring findings, in order of weight: (1) the "28 sibling pairs" half of the title is carried by a text label, not by the drawing; (2) the "roughly triples" annotation cannot be verified on a linear axis; (3) narrow version only: the annotation block is oversized for the plot area, and the wrapped "Sibling pairs: 28" label floats away from its line.

*Note: returns above describe the pre-fix renders. Findings 1, 3, 5, 7, 8 and 9 in the disposition table were fixed in the shipped renders; the panel was not re-run (a re-run after fixes would no longer be blind).*

---
---

# PANEL v2 — verbatim returns — two-figure artifact — 2026-08-12

Fresh agent instances, same roster cast. Four renders per seat: Chart 1 = figureA (n=1–4) design + narrow; Chart 2 = figure1 (n=1–8) design + narrow. Returns describe the pre-fix v2 renders; disposition-table fixes 1, 2 and 7 were applied afterward without a further panel.

## Seat 1 — Mathematics magazine editor

CHART 1 (Four children / 25 configurations / 6 pairs)

1. The sentence. If a colleague asked, I'd say: it's a counting chart showing that the number of ways siblings could line up against each other grows much faster than the number of sibling pairs — by four children you've got 25 possible fights but only 6 pairs.

2. The number. 25 conflict configurations at four children. I got it from the label at the end of the green line — "Conflict configurations: 25" — and it's restated in the title, so I'd repeat it with some confidence. I'll note the chart let me check it, too: the subtitle gives the formula, and (3⁴ − 2·2⁴ + 1)/2 does come out to 25. For a mathematics magazine that's the right instinct — I did the arithmetic in the margin and it held.

3. The question. "Show me one of the 25." The subtitle tells me the formula and tells me what it isn't — "no claim about actual conflicts" — but nobody in a general readership will assemble a mental picture of a 'conflict configuration' from "(3ⁿ − 2·2ⁿ + 1)/2, others uninvolved." One concrete instance — with three children, {Amy} vs {Ben}, Carol staying out of it, that's one of the six — and the whole thing lands. Without it the reader is trusting a formula.

4. The gap. A worked example, as above — that's what I looked for and didn't find. Smaller thing: the two lines share their first two points (0 and 1 at one and two children), and the single labels sitting on those shared points made me pause for a second over which line owned them. I sorted it out, but I stopped.

The narrow version survives fine. Everything I read at full size I could read at column width.

CHART 2 (Eight children / 3,025 configurations / 28 pairs)

1. The sentence. Same construction pushed out to eight children: the possibility space explodes — three thousand and change — while the pairs line just lies on the floor at 28.

2. The number. 3,025 at eight children, from the end-of-line label (and the title). I'd also repeat "each added child roughly triples the possible conflicts," from the annotation — and again the chart let me spot-check it: 966 to 3,025 is close enough to triple that I believe the "roughly."

3. The question. Does the grey line need to be on this chart at all? At this scale it is indistinguishable from the x-axis, and the only way I know it's worth anything is the "Sibling pairs: 28" label floating at the end. If the point is "the pairs line vanishes at this scale," fine, that's a legitimate point — but then say that's the point, because right now it reads like a line that failed to plot.

4. The gap. Anything readable in the left half. Children one through four are dots sitting on the axis; I looked for where the green curve actually leaves the floor and what the small values were, and I couldn't get them off this chart. Chart 1 is clearly meant to be the answer to that, which brings me to the pair.

The narrow version also holds up — labels and annotation stay legible, and the 0 / 1,500 / 3,000 axis is honest.

THE PAIR

They work, and the mechanism is the classic one: Chart 1 is the magnified bottom-left corner of Chart 2. The annotations even hand off — "already double at three" then "roughly triples each time" — which is one continuous story told in two frames. That's the right structure.

Two things I'd raise before it goes to layout. First, the titles are nearly identical sentences with different numbers — "Four children allow 25... but only 6" and "Eight children allow 3,025... but only 28." A reader flipping past will register the same shape twice and may take them for a repeated figure. One of the two titles should announce the relationship instead — something like "...and by eight children it's 3,025" — so the second chart reads as a continuation, not a duplicate. Second, and it's the page-space question: Chart 1's entire content is four numbers, two of which are shared between the lines. If space gets tight, Chart 1 could live as an inset in Chart 2's empty upper-left, and the article loses nothing. As submitted, both survive print; whether both earn a full slot is an editorial call, and I'd want the authors to have an answer ready.

One thing that genuinely helped: "exact counts, nothing estimated" in the source line. For our readership that one clause forestalls the most common letter we'd otherwise get.

## Seat 2 — Quantitative family-studies researcher

**Chart 1 (four children, 25 configurations vs 6 pairs)**

1. The sentence. It's a counting chart — it shows that the number of ways four children could mathematically line up two-sides-against-each-other (25) already dwarfs the number of sibling dyads (6), and it's explicit that this is combinatorics, not observed conflict.

2. The number. 25 conflict configurations at four children — I got it from the label sitting right on the endpoint of the green line, "Conflict configurations: 25," and it's also in the title. The smaller values (0, 1, 6) are printed on the points too, so I didn't need a table for anything.

3. The question. What counts as a "conflict configuration" substantively — the subtitle gives me the formula and says "two opposing sides, others uninvolved," but before I'd use this in anything I'd want to know why coalitional splits are the right unit rather than, say, dyadic conflicts, and whether "others uninvolved" is a defensible assumption about how sibling disputes actually work. The math is fine; the mapping from math to family process is the thing I'd press on.

4. The gap. Any connection to data on real families. I looked for even a gesture at observed base rates — how often multi-child coalitional conflicts actually occur versus dyadic ones — and there isn't one. To the chart's credit, it says so itself: "a possibility space — no claim about actual conflicts," and the source line says "exact counts, nothing estimated." So the gap is acknowledged rather than hidden, which I appreciate. The one thing that made me pause: the annotation "at three children, the possible conflicts already double the pairs" — 6 vs 3, fine — but "double" is doing rhetorical work for a comparison of two quantities that aren't in the same units, so the ratio doesn't mean much.

The narrow version holds up; everything is still legible at single-column width.

**Chart 2 (eight children, 3,025 configurations vs 28 pairs)**

1. The sentence. Same construction extended to eight children — the combinatorial possibility space explodes to 3,025 while pairs creep to 28, so it's really a chart about the growth rate of the formula, and again it says so plainly.

2. The number. 3,025 configurations at eight children, from the endpoint label "Conflict configurations: 3,025" — with the intermediate values 90, 301, 966 printed on the curve, which let me sanity-check the "roughly triples" annotation myself (301/90 ≈ 3.3, 966/301 ≈ 3.2, 3025/966 ≈ 3.1). That checks out.

3. The question. Given that the interesting part of Chart 2 is the growth rate, why compare against sibling pairs at all here? The gray line is flat against this axis and carries no information — the pairs comparison did its work in Chart 1. I'd ask whether the second chart should instead be a log-scale or ratio chart, because on a linear axis everything below n=5 is unreadable and the pairs line is decoration.

4. The gap. Two things. First, the same substantive gap as Chart 1 — no bridge to actual family behavior — again explicitly disclaimed, so it's honest. Second, at eight children I found myself wanting some acknowledgment that families of eight are rare; the x-axis extends the formula into territory where the "family" framing gets thin, and nothing on the chart marks that. Also, the values at n=1 through 4 are invisible on this axis; if I hadn't seen Chart 1 first I couldn't have recovered them.

**As a pair**

They work as a zoom-out: Chart 1 establishes the construct at readable scale with every point labeled, Chart 2 shows where the formula goes. The ordering is right — Chart 2 alone would be unreadable at the low end, and Chart 1 supplies exactly those values. The subtitles are identical (the formula, the "no claim about actual conflicts" disclaimer), which makes the pairing legible and keeps both honest. My one pairing-level concern is rhetorical: two charts whose titles both lead with "conflict" and whose message is "possibilities explode" will be read by a lay audience as saying large families are conflict factories, and the disclaimer in nine-point subtitle text is the only thing standing between the reader and that inference. The data support a statement about a possibility space; the emotional weight of the pair points somewhere the data don't go. I'd want the surrounding article text to carry that caveat, not just the subtitle. Otherwise, as pure combinatorics presented as combinatorics, both charts are fine.

## Seat 3 — Parent of five, non-technical

**Chart 1 (the one with four children)**

1. The sentence. I'd say: apparently with four kids there are 25 different ways they could line up against each other in a fight, even though there are only 6 pairs of siblings — so the fighting possibilities pile up way faster than the kids do.

2. The number. The 25. It's printed right at the top of the green line, next to the label "Conflict configurations: 25," and it's also in the title, so it's hard to miss. That's the one I'd repeat — "four kids, 25 ways to have a fight."

3. The question. What actually counts as a "conflict configuration"? The little subtitle has a formula with a 3 to the n in it, and honestly that part washed right over me. I get that it's kids splitting into two sides with some kids staying out of it, but I'd want the person to walk me through one example — like, name the four kids and show me what two of the 25 look like. Also the subtitle says "no claim about actual conflicts," so — is this telling me anything about my house, or is it just math?

4. The gap. I have five kids, and this chart stops at four. I immediately looked for the "5" on the bottom and it isn't there. That's genuinely the first thing I did — count over to find my family — and I couldn't. Also I looked for anything about how often these fights actually happen, and there's nothing; it's all "possible," which the fine print admits.

The narrow version reads the same as the big one for me — nothing got lost, the labels are still readable. The note about "at three children the possible conflicts already double the pairs" I could verify myself: 6 vs 3 are both printed right there at the 3 mark, so that felt fair.

**Chart 2 (the one with eight children)**

1. The sentence. I'd say: it's the same chart as the first one but carried out to eight kids, and by then the number of possible ways to fight has exploded to over three thousand while the pairs line just lies flat along the bottom.

2. The number. 3,025 — it's labeled at the tip of the green line ("Conflict configurations: 3,025") and it's in the title too. Although honestly the number I'd actually repeat to another parent is the one for MY family: five kids is 90. It's printed in small green right above the dot at 5 on this chart. That's the number I walked away with — my house has ninety possible fight lineups. That kind of explains my life.

3. The question. The note says "each added child roughly triples the space of possible conflicts" — so what I'd ask is: does that mean anything in practice? Does the actual fighting in real families grow like this, or is that curve just what the math allows? Because if my refereeing load really triples with each kid, that's a very different article than "here's a fun counting fact."

4. The gap. Two things. First, the gray "Sibling pairs: 28" line is so flat on this chart that I can't read any of its in-between values — I know it's 28 at eight kids because the label says so, but what is it at five? It's squashed into the axis. (Ironically the pairs were the readable line on Chart 1 and here they've vanished.) Second, same as before: nothing about actual, observed conflict — who fights, how often. The fine print keeps telling me it's only a "possibility space," and I believe it, but then I'm left wondering why I'm looking at it.

The narrow version of this one is fine too; the 966 label crowds the line a bit but I could still read everything.

**How they work as a pair**

They clearly are a pair — same shape, same green-and-gray lines, same fine print, same source line. Chart 1 walks you in gently with small numbers you can check, and Chart 2 delivers the punchline. That worked on me; by the second chart I already knew how to read it. Two things I noticed, though. The second chart makes the first one look pointless in hindsight — everything on Chart 1 (the 0, 1, 6, 25 up to four kids) is sitting on Chart 2 anyway, just squashed flat near the bottom. And it's a little odd that the first chart stops at four and the second goes to eight — as a parent of five, I fall in the crack between them, and only the second chart has my number on it, in tiny print. If the article is aimed at parents like me, I'd have led with the family sizes people actually have.

The one thing I never found on either chart: any connection to real fights. Both charts are careful to say they're not claiming that, which I respect, but it means after two charts I still don't know if the refereeing in my house is normal. That's the question I brought to the table, and the charts politely declined to answer it.

## Seat 4 — Visualization reader (canvas only)

**Chart 1 (figureA)**

1. What it's about. Before reading the title: two counts growing with the number of children, one growing gently (grey) and one taking off (green). The shape says "one of these things explodes combinatorially, the other doesn't." Then the title: that is exactly the claim — possible conflict groupings vs. sibling pairs. Title and picture match; no gap. The subtitle's hedge ("a possibility space — no claim about actual conflicts") is doing honest work, since "conflict" is a loaded word and the picture alone can't tell you it's hypothetical.

2. Does the picture support the title?
- "Four children allow 25" — visible. The green line ends at n=4, marked with a dot and the label "Conflict configurations: 25", and the dot sits plausibly above the 20 gridline.
- "only 6 sibling pairs" — visible. Grey endpoint labelled "Sibling pairs: 6", and there's a nice internal cross-check: it sits at the same height as the green n=3 point, which is labelled 6. The chart is consistent with itself.
- "conflict configurations" meaning what the subtitle's formula says — on faith. No plot can show that the counting rule is right; the source line ("exact counts, nothing estimated") is an assertion, not evidence.
- The annotation "At three children, the possible conflicts already double the pairs" — checkable from the printed labels: 6 vs 3. Exactly double, so "already double" is if anything understated. Fine.

3. Right kind of chart? Yes. Two series against a common integer x-axis, direct-labelled at the ends, linear y-axis that comfortably holds both series — a paired line chart is the natural form. The x is discrete (you can't have 2.5 children) so the connecting lines are interpolation fiction, but the dots at each integer keep that honest. Sound; no complaint.

4. Hard to read?
- At n=1 and n=2 the two series have identical values, so the grey line is hidden under the green one. The lone labels "0" and "1" belong to *both* series, but nothing says so — a reader may wonder where the grey line starts, or read those as green-only labels. It resolves itself, but I looked twice.
- The subtitle formula "(3ⁿ − 2·2ⁿ + 1)/2" is dense. Notably, the narrow version *drops the formula* from the subtitle — so the two widths carry slightly different subtitles. Not wrong, but worth knowing the single-column reader never sees the definition.
- Minor: 25 sits above the last labelled gridline (20), so the axis alone can't confirm it; the direct label does.

Nothing is cut off or overlapping at either width; the narrow render holds up well.

5. Grayscale? Survives. The contrast is dark-green vs. light-grey, which is really a lightness contrast already, and both series are direct-labelled at their right ends. No legend to lose, nothing depends on hue.

6. The number. I'd quote 25 conflict configurations at four children — read from the green terminal dot at x=4, confirmed by its direct label. Fully readable off the plot.

**Chart 2 (figure1)**

1. What it's about. Before the title: a classic hockey stick. One series is essentially exponential and one is flat on the floor. First impression: "this quantity explodes; the comparison series is negligible by n=8." The title says the same thing with numbers. They match.

2. Does the picture support the title?
- "3,025 at eight children" — visible: green endpoint at x=8, direct label, dot just above the 3,000 gridline. Good.
- "only 28 sibling pairs" — this one you take almost entirely on faith. The grey series is a flat line indistinguishable from zero at this scale. You cannot read 28 off the plot — not from the axis, not from the shape. Only the end label asserts it. The *rhetorical* point ("negligible next to 3,025") is vividly shown; the *number* 28 is printed, not plotted.
- The annotation "Each added child roughly triples the space of possible conflicts" — checkable, but from the printed labels (90 → 301 → 966 → 3,025, ratios ≈3.3, 3.2, 3.1), not from the drawing. On a linear axis, "roughly triples" has no visual signature; every exponential-ish curve looks like this hockey stick.
- Everything below n=5 is squashed into the axis — the green values at n=1–4 are unlabelled and unreadable here.

3. Right kind of chart? This is the one genuine design tension in the pair. For the *title's* claim — a contrast of magnitudes — the linear axis is the right choice; a log axis would tame the drama and can't show the zeros at n=1. But the *annotation's* claim is multiplicative, and a log scale is the only chart on which "roughly triples" is visible (as constant slope). As drawn, the annotation leans entirely on the four printed labels. Defensible choice, but the chart is carrying two claims and only natively supports one of them.

4. Hard to read?
- The grey series is unreadable as data along its whole length — flat on the zero line, its markers merging with the green markers for n=1–4. You get its endpoint label and nothing else.
- Narrow version: the "966" label crowds against the steep green segment and I had to look twice to attach it to the n=7 dot. The annotation's leader line ends vaguely in the space between n=6 and n=7, pointing at nothing in particular — tolerable since the note is about the whole series.
- The narrow version rewords the annotation and changes the y-ticks. Neither is wrong; just be aware the two widths are not identical text.
- Same as Chart 1: the formula disappears from the subtitle at narrow width.

---

# PANEL v3 — verbatim returns — web renders — 2026-08-13

Charts as given to the seats: **Chart 1 = figure1_web (n = 1–8)**, **Chart 2 = figureA_web (n = 1–4)**.
Each seat received both charts at **324 px and 355 px** — the display widths, not the 648 px natural size.
Roster recast for this artifact; no seat carried v1 or v2 context. Returns are unedited.

## Seat 1 — Parent of four, non-technical

**Chart 1 — the one that goes up to eight children**

1. The sentence. It's saying that with eight kids there are over three thousand ways they could take sides against each other, even though there are only 28 actual pairs of them — and the line barely moves until about six children and then shoots straight up off the top.

2. The number. 3,025. I got it twice without looking hard: it's in the big bold title at the top, and it's on the right-hand end of the green line where the label says "Conflict configurations: 3,025". The other one I'd probably repeat is 28, from the grey label at the end of the flat line ("Sibling pairs: 28"). I could not have got either of those off the vertical axis — that only has 0, 1,500 and 3,000 on it, so the little numbers along the bottom of the green line (90, 301, and 966 sitting right up against the steep bit) are the only way to know what's happening down there, and at the smaller size 966 and 301 are pressed so close to the line I had to squint to be sure which was which.

3. The question. Is this telling me anything about my actual house, or is it just counting? Because the small grey print says "a possibility space, not actual conflicts", but the word "conflict" is in the title, in the label on the line, and in the note in the middle of the chart, and that's what I'll remember an hour from now — not the disclaimer.

4. The gap. Where four children is. My lot are four and there's no number on the line at 4 — it's flat on the floor along with 1, 2 and 3, and the axis is so stretched by the 3,000 at the top that everything under about five children looks like nothing at all. I also looked for some sense of how many of those three thousand ever actually happen, and there isn't one. And I got stuck for a second on "Ways n children can split" in the grey line under the title — I haven't done letters-instead-of-numbers since school and I nearly stopped reading there.

**Chart 2 — the one that goes up to four children**

1. The sentence. It's the same chart as the other one but stopping at four children, which is what I've got — 25 ways to fall out and 6 pairs of siblings — and the green line pulls away from the grey one somewhere around three.

2. The number. 25, from the bold title and again from the green label at the top right end of the line ("Conflict configurations: 25"). And 6, from the grey "Sibling pairs: 6" at the end of the grey line. This one I could half-check off the axis too — the green dot at 4 children sits just under the 20-something mark, which fits.

3. The question. Why am I being shown the same chart twice, and which of the two am I supposed to be taking the point from? If the answer is "this is your family, the other is a big family", fine, but nobody said that.

4. The gap. What any of it means in practice. It tells me my four kids have 25 possible ways of splitting into sides, and I don't know whether that's a lot, whether it's more than it should be, or what I'm meant to do differently. It also doesn't tell me anything about ages, and mine are 6 to 15 — a 6-year-old and a 15-year-old aren't the same kind of pairing, and this counts them as identical. And with the line stopping at 4, I couldn't tell from this chart alone that it carries on going up like a rocket; I only know that because I saw the other one.

**Both charts.** The one thing that genuinely nagged me across both: they're the same picture with two different sizes of number, and the honest small print at the bottom ("exact counts, nothing estimated", "not actual conflicts") is doing a lot of quiet work against a title that reads like my house is a powder keg. If someone showed me these while I was reading on my phone, what I'd walk away with is "eight kids, three thousand ways to argue" — not the caveat.

## Seat 2 — Research mathematician, enumerative combinatorics

**Chart 1**

1. The sentence. It's a Stirling-number growth curve dressed up as a family-dynamics fact — the count is S(n+1,3) for splitting n children into two opposing camps with the rest sitting out, and it's correct, but the "but only 28 pairs" framing puts two different kinds of object side by side without saying how they relate.

2. The number. 3,025 — I got it from the green callout at the right-hand end of the curve, the two-line label reading "Conflict configurations: 3,025". I'd also repeat 966, which is printed just above the green line at n = 7. I could not read 28 off the plot at all; I got it from the grey text label on the right, not from the axis, because on a 0–3,000 scale the grey line is indistinguishable from the baseline.

3. The question. Do you know that your grey line is a sub-count of your green line? C(8,2) = 28 is exactly the number of configurations in which both opposing sides are singletons — the two-person quarrels. So this isn't "3,025 possibilities versus 28 pairs," it's "all faction splits versus the two-person ones," and that's a much better sentence than the one on the chart. I'd want to know whether that was understood and left out, or not noticed.

4. The gap. The definition. I had to reconstruct for myself whether the two sides are ordered or unordered and whether the uninvolved group is allowed to be empty — you need both conventions pinned down for S(n+1,3) to be the right answer, and the subtitle gives neither. The source line names A000392 and S(n+1,3), which I appreciate, but that is a pointer, not a definition, and a reader who can't decode Stirling notation gets nothing. I also went looking for a log axis, or at least a second panel, because on this scale everything below n = 5 is flat against zero and the chart shows me one interesting point and six dead ones.

**Chart 2**

1. The sentence. Same quantity truncated to n ≤ 4, and honestly it reads better than the eight-child version because on a 0–25 scale you can actually see both series and watch the green one pull away from the grey.

2. The number. 6 — from the label sitting just above the green line's third point, at n = 3. Though I'll say that "6" appears twice on this chart for two different things: 6 conflict configurations at n = 3 on the green line, and "Sibling pairs: 6" as the grey end label at n = 4. I read the grey 6 first and briefly thought the lines had met.

3. The question. Your annotation says "At three children the possible conflicts already double the pairs" — at n = 3 it's 6 against 3, which is exactly double, and at n = 2 it's 1 against 1. Is "already" meant to mark the crossing point? Because the crossing happens at n = 3 and the word "already" reads to me like it happened earlier than expected, when in fact it's the first place anything separates at all.

4. The gap. Why this chart exists next to the other one. Given both, I couldn't tell whether n = 4 is a deliberate second case or just the first chart zoomed, and nothing on either says "this is the same curve, first four points." I also looked for the ratio being asserted — the other chart says the possibilities roughly triple per child, which is true in the limit (the ratios run 6, 4.17, 3.6, 3.33, 3.21, 3.13), but on this chart's range the growth factor is 6 then 4.17, nowhere near three, and there's nothing here telling a reader that the tripling is asymptotic rather than what they're looking at.

## Seat 3 — Family therapist, 20 years clinical practice

**Chart 1**

1. The sentence. It's a maths chart that has been dressed up in the language of family conflict — it counts the ways you could theoretically sort eight kids into two opposing camps, calls that number "conflict configurations," and the headline reads like a warning about big families even though the small print underneath admits it isn't describing any actual conflict.

2. The number. "Conflict configurations: 3,025" — the green label at the top right, at the end of the rising line, which matches the 3,025 in the title. I'd also repeat 966, which is printed just above the line at 7 children on the horizontal axis. The other side of the comparison, "Sibling pairs: 28," I only got from the grey label on the right — I could not read 28 off the vertical axis, because on a scale that goes to 3,000 the grey line sits flat on the baseline and I can't tell it apart from zero.

3. The question. What is one configuration, in a family? If I picture the Murrays, with their six, what real thing in that house is one of those 301 — an argument, an alliance that lasted an afternoon, a seating arrangement that could occur in principle? Because if the honest answer is "none of them, it's an arrangement that could exist on paper," then I want to know why the word "conflict" is in the label at all.

4. The gap. Anything connecting the count to what happens. No frequency, no time — 3,025 what, per week, ever, in a lifetime? Nothing telling me how many of those 3,025 have ever actually occurred in a real household, which I'd guess is a tiny fraction, and that fraction is the interesting number and it isn't here. And nothing about the thing families actually vary on: two of the eight might be at each other constantly and the other six never take a side. The chart treats all eight children as interchangeable pieces.

I also want to flag what I think a parent does with this, because it's the part that worries me most. A mother of five who is already frightened that she has made her house unmanageable reads the title, sees a line going nearly vertical, reads "each added child roughly triples the possibilities," and takes away that she has multiplied her family's suffering by having another baby. The subtitle says "a possibility space, not actual conflicts," but the subtitle is the third thing she reads and it's in grey.

Both sizes read the same to me. At the smaller one the "966" label sits tight against the line but I could still read it.

**Chart 2**

1. The sentence. Same chart with the numbers small enough to be believable, which paradoxically makes it more misleading — at four children the two lines are close enough that it looks like a real comparison of two real quantities, and the annotation tells me conflicts already "double" the pairs, which is a sentence about actual conflict that the data underneath doesn't support.

2. The number. The "6" printed just above the green line at 3 children, with the "3" just below the grey line at the same point — that's the doubling the annotation is talking about. And "Conflict configurations: 25" from the green label at the end of the line at four children.

3. The question. The annotation says "At three children the possible conflicts already double the pairs" — did you mean "possible conflicts" there? The title says "configurations" and the subtitle says these aren't conflicts, but the note in the middle of the chart, which is the bit my eye went to first, says conflicts. That's the sentence a parent will quote back to me, and as written it says a family of three has six conflicts.

4. The gap. The thing I actually wanted, which is what happens between two children versus three. That's the real clinical question — whether adding a third genuinely changes the dynamic, and it does, in ways I see weekly: triangulation, the odd-one-out, two kids forming a bloc against a parent. This chart has a number sitting right there at three children that looks like it answers that, and it doesn't; it's counting arrangements, not describing what a third child does to a household. I also couldn't find any indication of whether anyone has ever counted a real family against this, or whether the whole thing is arithmetic from a formula. The source line says "exact counts, nothing estimated," which I read as honest about the maths and silent about the families.

## Seat 4 — Visualization reader (canvas only)

**Chart 1**

1. What it is about. Before reading the title: a single steep hockey-stick curve in dark green rising from a flat floor to a point at the top right, with a second, essentially flat grey line running along the baseline. My first read was "something grows explosively with the count on the x-axis while a second thing stays at nothing." The x-axis is labelled *Number of children*, 1 through 8. Then the title: *"Eight children allow 3,025 possible conflict configurations, but form only 28 sibling pairs."* That matches what I saw, with one addition the picture alone did not give me — that the flat grey line is not zero but 28. The subtitle does real work here and I'd count it as part of the title: it tells me this is a possibility space, not observed conflicts. Without it I would have read the green curve as a count of things that happened.

2. Does the picture support the claim.
- *"Eight children"* — yes, x = 8 is the last tick and both endpoint markers sit on it.
- *"3,025 possible conflict configurations"* — partly. The green endpoint marker sits just above the 3,000 tick, so the geometry supports "a bit over three thousand." The precise 3,025 comes from the text label, not the plot.
- *"only 28 sibling pairs"* — on faith entirely. The grey endpoint is on the zero baseline. At a scale whose ticks are 0 / 1,500 / 3,000, 28 is one pixel of nothing. The plot cannot distinguish 28 from 2 or from 0. The grey series carries no visual information at all; it is a text label with a line drawn under it.
- *"but form only"* — the contrast the word "only" asserts is the one thing the picture does convey powerfully, arguably too powerfully: it reads as "3,025 versus nothing" rather than "3,025 versus 28."
- The in-chart annotation, *"Each added child roughly triples the possibilities,"* is **not checkable from the plot**. A constant multiplicative ratio has no visual signature on a linear axis — an exponential and a cubic both look like this hockey stick. The reader can partially verify it by dividing the printed labels (90 → 301 → 966 → 3,025), which is arithmetic on labels, not reading a chart. And the labelled portion is the only place it holds: the earlier, unlabelled part of the curve grows much faster than 3× per step (1 → 6 at n=2→3 is sixfold), so a reader who took "each added child" literally across the whole x-range would be misled by a claim they cannot see.

3. Right form for the claim. Two claims are being carried and the form serves only one. For the magnitude contrast, a linear line chart works — the gap is the message. For the growth-rate claim in the annotation, it is the wrong form: a log y-axis would render "roughly triples" as a straight line of constant slope and would simultaneously rescue the grey series from the baseline, letting 28 be *seen*. That is a real trade — a log axis costs a lay reader something — but as drawn, the chart asserts a ratio and draws only a silhouette. Secondary point: children are integers, and the connecting line invites reading a value at 4.5 children. The markers are drawn, which mitigates it, but the line is doing interpolation that the underlying quantity does not admit.

4. Hard to read.
- **The "966" label collides with the curve.** The annotation's leader line runs straight through it, and the label sits flush against the steepest segment of the green line. This is the worst spot on the chart and it is tighter at 324px than at 355px.
- **The grey series is occluded from n=1 to n=4.** It only becomes separately visible around x=5; before that it is underneath the green line. A reader could reasonably conclude the grey series starts at 5.
- **"28" sits below the axis line**, at the same height as the "8" tick label, which makes it momentarily read as part of the axis rather than as a series endpoint. I looked at it twice.
- The value labels 90 / 301 / 966 are roughly 9px at 324px — legible, but at the floor.
- The green series' value at n=1 is 0 and is unlabelled, so the curve appears to start "at the axis" without saying so.
- No y-axis title. Defensible here, since the axis carries two different units (configurations and pairs), but it means the reader must get the units entirely from the two end labels.

5. Grayscale. Survives. I converted it and checked. Dark-green versus light-grey separates cleanly on lightness alone, and both series are labelled directly at their right ends, so nothing depends on hue or on a legend. One small loss: the italic annotation is green, tying it to the green series by colour; in grayscale it becomes the same tone as the subtitle and axis text, and the tie has to be made from the word "possibilities" instead.

6. The number. I would quote: **at eight children, the green *Conflict configurations* marker sits just above the 3,000 tick on the y-axis** — so, a little over three thousand. That is the most I can get from the plot itself; the exact 3,025 is read off the text label beside the marker, not off the geometry. For the second figure I have to say it plainly: **28 is not readable from this plot.** The grey endpoint at x = 8 lies on the zero baseline and there is no axis resolution anywhere near it. That number exists only as text.

**Chart 2**

1. What it is about. Before the title: same construction as Chart 1, but only four x positions, and now both series are actually visible as separate curves — a green one bending upward and a grey one rising gently below it, diverging after x = 2. My read was "two counts that start together and separate." Title: *"Four children allow 25 possible conflict configurations, but form only 6 sibling pairs."* No divergence from what I saw. This is the same series and the same source line as Chart 1, restricted to n = 1–4.

2. Does the picture support the claim.
- *"Four children"* — yes, x = 4 is the last tick.
- *"25 possible conflict configurations"* — yes, readable. The green endpoint is roughly a quarter of the 0-to-20 span above the 20 tick, which estimates to about 25. It requires extrapolating the tick spacing past the last label, but it works.
- *"only 6 sibling pairs"* — yes, and this is the important difference from Chart 1. The grey endpoint sits at about six-tenths of the way from 0 to 10. I can read 6 off the plot.
- *"but form only"* — the contrast here is honest: roughly four-to-one, and it looks roughly four-to-one.
- The annotation, *"At three children the possible conflicts already double the pairs,"* **is checkable from the plot.** At x = 3 the green marker is at 6 and the grey at 3, both labelled, and the green marker sits at visibly twice the height of the grey one. The picture and the sentence agree.

3. Right form for the claim. Yes. Because the two series are within one order of magnitude, the linear line chart shows the divergence as an actual widening gap, which is exactly the claim. The same integer-interpolation caveat applies — the line implies values between whole children — but with only four x positions and prominent markers it is a small cost.

4. Hard to read.
- **The grey "3" label is the weakest text on either chart.** It is light grey, roughly 9px at 324px, and sits directly under the dark "6". At the small size the vertical stack of 6-over-3 near x = 3 momentarily reads as one series' labels before the colour separates them. That the annotation's whole verifiability rests on those two numbers makes this the label I would least want to be faint.
- **The endpoint at 25 sits above the highest labelled tick (20)** with no tick above it, so the reader estimates by extending the spacing. At 324px the marker is also close to the top of the plot area — not clipped, but tight.
- The annotation block sits close to the curve; its leader line is legible at 355px and slightly cramped at 324px.
- Same absence of a y-axis title, same reason, same acceptability.

5. Grayscale. Survives, and I checked it converted. The dark/light separation holds and both series are end-labelled. The one degradation: the grey "3" label, already low-contrast in colour, is the first thing that would go on a mediocre print or a low-brightness phone screen — and losing it removes half the evidence for the annotation's doubling claim.

6. The number. I would quote: **at three children there are 6 conflict configurations against 3 sibling pairs** — read from the green marker sitting a little past halfway between the 0 and 10 ticks at x = 3, and the grey marker just under a third of the way, cross-checked against the "6" and "3" labels at those markers. Unlike Chart 1, I get this from the plot; the labels confirm rather than substitute.

**One cross-chart observation.** These are the same series at two x-ranges, and the difference in x-range is what decides whether the chart works. At n ≤ 4 both quantities are visible and the comparison is drawn. At n ≤ 8 the second quantity collapses onto the baseline and the comparison is only asserted in text. If both ship, Chart 1's "28" is the weak point in the pair.

5. Grayscale? Survives, same reasons as Chart 1. Ironically the grey series is already nearly invisible in colour, so grayscale loses nothing that wasn't lost.

6. The number. I'd quote 3,025 possible configurations at eight children — green endpoint at x=8, sitting just above the 3,000 axis tick, direct label. The 28, by contrast, I could *not* get off the plot itself — only off its text label — and I'd say so if quoting it.

**As a pair**

They agree everywhere they overlap, and the overlap is checkable: Chart 1's headline point (n=4: 25 vs 6) exists in Chart 2 at x=4, where both dots sit on the floor — no contradiction, and the zoom-in/zoom-out sequence is actually a good editorial structure. Subtitles, source lines, series names, colours and label conventions are identical across the two, so nothing forces a re-orientation.

Two small pair-level notes: a reader who just absorbed "25 is the big number" from Chart 1 meets Chart 2, where 25 is a dot indistinguishable from zero — that's the point, but a half-sentence in the article would land it; and the annotations make different claims ("double at three children" vs. "triples per child") that could momentarily read as competing rules — they aren't, but a skim-reader might blur them.

Both charts are honestly labelled, self-consistent, and survive narrow width and grayscale. The only substantive weakness is Chart 2's reliance on printed labels for both its "28" and its "triples" claims.

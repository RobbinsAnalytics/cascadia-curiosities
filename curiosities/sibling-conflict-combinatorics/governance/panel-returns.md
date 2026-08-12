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

5. Grayscale? Survives, same reasons as Chart 1. Ironically the grey series is already nearly invisible in colour, so grayscale loses nothing that wasn't lost.

6. The number. I'd quote 3,025 possible configurations at eight children — green endpoint at x=8, sitting just above the 3,000 axis tick, direct label. The 28, by contrast, I could *not* get off the plot itself — only off its text label — and I'd say so if quoting it.

**As a pair**

They agree everywhere they overlap, and the overlap is checkable: Chart 1's headline point (n=4: 25 vs 6) exists in Chart 2 at x=4, where both dots sit on the floor — no contradiction, and the zoom-in/zoom-out sequence is actually a good editorial structure. Subtitles, source lines, series names, colours and label conventions are identical across the two, so nothing forces a re-orientation.

Two small pair-level notes: a reader who just absorbed "25 is the big number" from Chart 1 meets Chart 2, where 25 is a dot indistinguishable from zero — that's the point, but a half-sentence in the article would land it; and the annotations make different claims ("double at three children" vs. "triples per child") that could momentarily read as competing rules — they aren't, but a skim-reader might blur them.

Both charts are honestly labelled, self-consistent, and survive narrow width and grayscale. The only substantive weakness is Chart 2's reliance on printed labels for both its "28" and its "triples" claims.

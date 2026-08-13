"""Worked example: all six ways three children can take sides.

The figure both prior panels asked for. v2's top finding was "Show me one of the
25 ... one concrete instance and the whole thing lands"; v3's therapist seat
asked "What is one configuration, in a family?". Neither line chart can answer
that, because a canvas plotting counts cannot enumerate them.

At n = 3 the enumeration also *shows* the subset relation that Panel v3 found and
that the line charts only assert: six configurations, of which exactly three are
one child against one — and those three are the sibling pairs. Laying the six out
as two rows of three puts that on the page without a word of argument.

n = 3 rather than n = 4 because twenty-five cells do not stay legible in a 324 px
mobile column; six do.

Geometry is in inches throughout, on an equal-aspect axes covering the whole
canvas, so the circles are round and nothing has to be corrected for the figure's
aspect ratio.

Run from inside figures/ — the output filename is bare.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

from cascadia_fig import (EVERGREEN, RAIN, BASALT, SLATE, MIST, PAPER, SERIF, SANS,
                          SERIF_B, SANS_R, SANS_B, wrap, require_glyphs, require_inside)

TITLE_PT=18.0; SUB_PT=13.0; CAVEAT_PT=12.5; HEAD_PT=12.0; CAP_PT=11.0; SOURCE_PT=11.0
W=4.32; DPI=150                  # 648 px wide, displayed at 324 px; H is derived

KIDS = ("A", "B", "C")

# (side one, side two, uninvolved). The three one-against-one cases first: they
# are the sibling pairs, and the row break is what makes them a visible subset.
CONFIGS = [
    (("A",), ("B",), ("C",)),
    (("A",), ("C",), ("B",)),
    (("B",), ("C",), ("A",)),
    (("A",), ("B", "C"), ()),
    (("B",), ("A", "C"), ()),
    (("C",), ("A", "B"), ()),
]
ROWS = [("One against one — the sibling pairs", CONFIGS[:3]),
        ("One against two", CONFIGS[3:])]

assert len(CONFIGS) == 6, "n=3 has six configurations"
assert sum(1 for a, b, _ in CONFIGS if len(a) == 1 and len(b) == 1) == 3, "three are 1v1"

R = 0.115          # circle radius, inches
GAP = 0.325        # centre-to-centre spacing

LEFT = 0.25
text_w = W - 2*LEFT

TOP_MARGIN=0.22; CELL_H=0.92; BOT_MARGIN=0.135
LEAD_TITLE=1.24; LEAD_SUB=1.30; LEAD_CAVEAT=1.30; LEAD_HEAD=1.25; LEAD_SRC=1.30
GAP_SUB=0.06; GAP_CAVEAT=0.05; GAP_GRID=0.20; GAP_RULE=0.10

title = "Three children can take sides in six ways, and three of those are one against one"
subtitle = "Every possible split into two opposing sides, with anyone left over staying out of it."
caveat = "These are possibilities, not arguments that happened."
src = ("Source: the six configurations for three children, enumerated · "
       "OEIS A000392 · exact counts, nothing estimated")

# Two passes. The first wraps every string on a throwaway canvas of the right
# width so the height can be derived from the content; the second draws it. The
# first cut of this figure was hand-sized and the bottom row landed on top of the
# provenance strip — require_inside said nothing, because an internal collision
# never leaves the canvas.
_probe = plt.figure(figsize=(W, 12), dpi=DPI)
tl = wrap(_probe, title, text_w, fontsize=TITLE_PT, family=SERIF, weight="bold")
sl = wrap(_probe, subtitle, text_w, fontsize=SUB_PT, family=SANS)
cl = wrap(_probe, caveat, text_w, fontsize=CAVEAT_PT, family=SANS, weight="bold")
srcl = wrap(_probe, src, text_w - 0.13, fontsize=SOURCE_PT, family=SANS)
headl = [wrap(_probe, h, text_w, fontsize=HEAD_PT, family=SANS, weight="bold")
         for h, _ in ROWS]
plt.close(_probe)

src_step = SOURCE_PT * LEAD_SRC / 72
src_block = src_step * len(srcl)
H = (TOP_MARGIN
     + len(tl)*TITLE_PT*LEAD_TITLE/72 + GAP_SUB
     + len(sl)*SUB_PT*LEAD_SUB/72 + GAP_CAVEAT
     + len(cl)*CAVEAT_PT*LEAD_CAVEAT/72 + GAP_GRID
     + sum(len(h)*HEAD_PT*LEAD_HEAD/72 + GAP_RULE + CELL_H for h in headl)
     + src_block + BOT_MARGIN)

fig = plt.figure(figsize=(W, H), dpi=DPI); fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.set_aspect("equal"); ax.axis("off"); ax.set_facecolor(PAPER)

for s in tl: require_glyphs(SERIF_B, s, "title")
for s in sl: require_glyphs(SANS_R, s, "subtitle")
for s in cl: require_glyphs(SANS_B, s, "caveat")
for s in srcl: require_glyphs(SANS_R, s, "source strip")

y = H - TOP_MARGIN
for line in tl:
    ax.text(LEFT, y, line, ha="left", va="top", fontsize=TITLE_PT,
            family=SERIF, weight="bold", color=BASALT)
    y -= TITLE_PT * LEAD_TITLE / 72

y -= GAP_SUB
for line in sl:
    ax.text(LEFT, y, line, ha="left", va="top", fontsize=SUB_PT, family=SANS, color=SLATE)
    y -= SUB_PT * LEAD_SUB / 72

# Panel v3 findings 1 and 3: the caveat was grey small print and read third or
# not at all. It now carries the weight of a statement, in the body ink.
y -= GAP_CAVEAT
for line in cl:
    ax.text(LEFT, y, line, ha="left", va="top", fontsize=CAVEAT_PT,
            family=SANS, weight="bold", color=BASALT)
    y -= CAVEAT_PT * LEAD_CAVEAT / 72


def draw_cell(cx, top, side_a, side_b, out):
    """One configuration: three fixed-position children, encoded by fill, with the
    split spelled out underneath. Fill style and the caption both carry it, so
    nothing depends on colour alone."""
    role = {k: "out" for k in KIDS}
    for k in side_a: role[k] = "a"
    for k in side_b: role[k] = "b"

    cy = top - R
    x0 = cx - GAP
    for i, k in enumerate(KIDS):
        x = x0 + i*GAP
        r = role[k]
        if r == "a":
            ax.add_patch(Circle((x, cy), R, facecolor=EVERGREEN, edgecolor=EVERGREEN,
                                lw=1.4, zorder=3))
            ink = PAPER
        elif r == "b":
            ax.add_patch(Circle((x, cy), R, facecolor=PAPER, edgecolor=EVERGREEN,
                                lw=1.8, zorder=3))
            ink = EVERGREEN
        else:
            ax.add_patch(Circle((x, cy), R, facecolor=MIST, edgecolor=MIST,
                                lw=1.4, zorder=3))
            ink = SLATE
        ax.text(x, cy, k, ha="center", va="center", fontsize=CAP_PT,
                family=SANS, weight="bold", color=ink, zorder=4)

    cap = f"{'+'.join(side_a)} vs {'+'.join(side_b)}"
    ax.text(cx, cy - R - 0.13, cap, ha="center", va="top", fontsize=CAP_PT,
            family=SANS, weight="bold", color=BASALT)
    tail = f"{out[0]} stays out" if out else "nobody left out"
    ax.text(cx, cy - R - 0.29, tail, ha="center", va="top", fontsize=CAP_PT*0.92,
            family=SANS, color=SLATE)


y -= GAP_GRID
for (head, group), lines in zip(ROWS, headl):
    for s in lines:
        require_glyphs(SANS_B, s, "row header")
        ax.text(LEFT, y, s, ha="left", va="top", fontsize=HEAD_PT,
                family=SANS, weight="bold", color=EVERGREEN)
        y -= HEAD_PT * LEAD_HEAD / 72
    ax.plot([LEFT, W - LEFT], [y - 0.02, y - 0.02], color=MIST, lw=1.0, zorder=1)
    y -= GAP_RULE
    for i, (a, b, out) in enumerate(group):
        draw_cell(LEFT + (i + 0.5) * (text_w / 3), y, a, b, out)
    y -= CELL_H

src_top = BOT_MARGIN + src_block
# The guard require_inside cannot give: the last row of cells must clear the
# provenance strip. On the first cut it did not, and nothing failed.
if y < src_top - 1e-9:
    raise SystemExit(f"grid overruns the source strip by {src_top - y:.3f} in "
                     f"(grid bottom {y:.3f}, strip top {src_top:.3f})")

ax.add_patch(FancyBboxPatch((LEFT, BOT_MARGIN), 0.035, src_block*0.86,
                            boxstyle="square,pad=0", facecolor=EVERGREEN,
                            edgecolor="none", zorder=3))
ys = BOT_MARGIN + src_block*0.86
for line in srcl:
    ax.text(LEFT + 0.10, ys, line, ha="left", va="top", fontsize=SOURCE_PT,
            family=SANS, color=SLATE)
    ys -= src_step

require_inside(fig)
fig.savefig("figure_example_web.png", facecolor=PAPER, dpi=DPI)
plt.close(fig)
print(f"figure_example_web.png: {int(W*DPI)}x{int(H*DPI)} px  ->  {int(W*DPI/2)} px slot")
print(f"    title {len(tl)} lines, subtitle {len(sl)} lines, caveat {len(cl)} lines, "
      f"source {len(srcl)} lines")

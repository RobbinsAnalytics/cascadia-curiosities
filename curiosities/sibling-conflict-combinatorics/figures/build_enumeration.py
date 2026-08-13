"""Worked examples: every way three (and four) children can take sides.

Replaces build_example.py, which did the n = 3 web render only.

Both prior panels asked for a concrete instance. v2's top finding was "Show me
one of the 25 ... one concrete instance and the whole thing lands"; v3's
therapist seat asked "What is one configuration, in a family?". No line chart can
answer that, because a canvas plotting counts cannot enumerate them.

The enumeration also *shows* the subset relation that Panel v3 found and that the
line charts can only assert: the one-against-one cases are a labelled row, and
their count is exactly the sibling-pair count. At n = 3 that is 3 of 6; at n = 4
it is 6 of 25.

    n3 web     324 px column   — the six cases, two rows
    n3 design  manuscript      — the same six, print type
    n4 design  manuscript only — all twenty-five, four rows by class

n = 4 is not built for the web: twenty-five cells cannot stay legible in a 324 px
column, which is the whole reason n = 3 carries the mobile slot.

Geometry is in inches on an equal-aspect axes covering the canvas, so circles are
round regardless of the figure's aspect ratio. Height is derived from the wrapped
content rather than hand-set — the first cut of this figure was hand-sized and
its bottom row landed on the provenance strip, which require_inside cannot catch
because an internal collision never leaves the canvas.

Run from inside figures/ — output filenames are bare.
"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

from cascadia_fig import (EVERGREEN, BASALT, SLATE, MIST, PAPER, SERIF, SANS,
                          SERIF_B, SANS_R, SANS_B, width_in, wrap,
                          require_glyphs, require_inside)

matplotlib.rcParams["pdf.fonttype"] = 42

DPI = 150


def configurations(kids):
    """Every unordered pair of disjoint nonempty subsets, with the rest uninvolved.

    Enumerated rather than formula-driven, so the figure and the count are
    independent of equation (1) and can disagree with it loudly if either is wrong.
    """
    n = len(kids)
    seen, out = set(), []
    for mask in range(3**n):
        a, b, m = [], [], mask
        for k in kids:
            side = m % 3; m //= 3
            if side == 0: a.append(k)
            elif side == 1: b.append(k)
        if not a or not b:
            continue
        key = frozenset((frozenset(a), frozenset(b)))
        if key in seen:
            continue
        seen.add(key)
        rest = tuple(k for k in kids if k not in a and k not in b)
        out.append((tuple(a), tuple(b), rest))
    return out


def by_class(configs, order):
    """Group by the shape of the split, smallest side first, one-against-one first.

    Sides are ordered by size then by their first child, and the cells within a
    class are sorted the same way, so the reading order is A-first throughout
    rather than whatever order the base-3 enumeration happened to produce.
    """
    rank = {k: i for i, k in enumerate(order)}
    def key(side): return (len(side), [rank[k] for k in side])
    groups = {}
    for a, b, rest in configs:
        lo, hi = sorted((tuple(sorted(a, key=rank.get)), tuple(sorted(b, key=rank.get))),
                        key=key)
        groups.setdefault((len(lo), len(hi)), []).append((lo, hi, tuple(sorted(rest, key=rank.get))))
    for g in groups.values():
        g.sort(key=lambda c: (key(c[0]), key(c[1])))
    return [(k, groups[k]) for k in sorted(groups)]


CLASS_LABEL = {
    (1, 1): "One against one — the sibling pairs",
    (1, 2): "One against two",
    (1, 3): "One against three",
    (2, 2): "Two against two",
}


def build(stem, kids, W, title_pt, sub_pt, caveat_pt, head_pt, cap_pt, source_pt,
          cols, pdf=False):
    configs = configurations(kids)
    rows = by_class(configs, kids)

    n = len(kids)
    assert len(configs) == (3**n - 2*2**n + 1)//2, "enumeration disagrees with C(n)"
    pairs = sum(1 for k, g in rows if k == (1, 1) for _ in g)
    assert pairs == n*(n-1)//2, "one-against-one count is not the sibling-pair count"

    LEFT = 0.25
    text_w = W - 2*LEFT
    cell_w = text_w / cols
    R = min(0.115, cell_w/(2.6*n))
    GAP = R * 2.85

    TOP=0.22; BOT=0.135
    L_TITLE=1.24; L_SUB=1.30; L_CAV=1.30; L_HEAD=1.25; L_SRC=1.30
    G_SUB=0.06; G_CAV=0.05; G_KEY=0.13; G_GRID=0.16; G_RULE=0.10
    cell_h = 2*R + 0.13 + cap_pt*1.30*2/72 + 0.12

    title = (f"{('Three' if n == 3 else 'Four')} children can take sides in "
             f"{len(configs)} ways, and {pairs} of those are one against one")
    subtitle = "Every possible split into two opposing sides, with anyone left over staying out of it."
    # Panel v4, Seat 3: "six configurations, and none of them is 'no conflict'. A
    # parent will scan this and see six ways their children can be in opposition and
    # no way for them not to be." The set genuinely excludes peace by construction,
    # so the figure says so rather than letting the omission speak.
    caveat = ("These are possibilities, not arguments that happened — and the commonest "
              "case of all, nobody taking sides, is not among them.")
    src = (f"Source: all {len(configs)} configurations for {'three' if n == 3 else 'four'} "
           f"children, enumerated · OEIS A000392, S(n+1, 3) · exact counts, nothing estimated")

    probe = plt.figure(figsize=(W, 20), dpi=DPI)
    tl = wrap(probe, title, text_w, fontsize=title_pt, family=SERIF, weight="bold")
    sl = wrap(probe, subtitle, text_w, fontsize=sub_pt, family=SANS)
    cl = wrap(probe, caveat, text_w, fontsize=caveat_pt, family=SANS, weight="bold")
    srcl = wrap(probe, src, text_w - 0.13, fontsize=source_pt, family=SANS)
    # Panel v4, three seats: the block sizes are the combinatorial content of the
    # page and were recoverable only by counting tiles, which the 4+2 wrap fights.
    heads = [f"{CLASS_LABEL[k]}  ({len(g)})" if k != (1, 1)
             else f"{CLASS_LABEL[k]} ({len(g)} of {len(configs)})"
             for k, g in rows]
    headl = [wrap(probe, h, text_w, fontsize=head_pt, family=SANS, weight="bold")
             for h in heads]
    key_w = {s: width_in(probe, s, fontsize=cap_pt, family=SANS)
             for s in ("one side", "the other side", "staying out")}
    plt.close(probe)

    src_step = source_pt * L_SRC / 72
    src_block = src_step * len(srcl)
    grid_h = sum(len(h)*head_pt*L_HEAD/72 + G_RULE
                 + cell_h * -(-len(g) // cols)
                 for h, (_, g) in zip(headl, rows))
    H = (TOP + len(tl)*title_pt*L_TITLE/72 + G_SUB
         + len(sl)*sub_pt*L_SUB/72 + G_CAV
         + len(cl)*caveat_pt*L_CAV/72
         + G_KEY + 2*(R*0.86) + 0.06 + G_GRID
         + grid_h + src_block + BOT)

    fig = plt.figure(figsize=(W, H), dpi=DPI); fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_facecolor(PAPER)

    for s in tl: require_glyphs(SERIF_B, s, "title")
    for s in sl: require_glyphs(SANS_R, s, "subtitle")
    for s in cl: require_glyphs(SANS_B, s, "caveat")
    for s in srcl: require_glyphs(SANS_R, s, "source strip")

    y = H - TOP
    for line in tl:
        ax.text(LEFT, y, line, ha="left", va="top", fontsize=title_pt,
                family=SERIF, weight="bold", color=BASALT)
        y -= title_pt * L_TITLE / 72
    y -= G_SUB
    for line in sl:
        ax.text(LEFT, y, line, ha="left", va="top", fontsize=sub_pt, family=SANS, color=SLATE)
        y -= sub_pt * L_SUB / 72
    # Panel v3 findings 1 and 3: the caveat was grey small print, read third or
    # not at all. In body ink now, on its own line.
    y -= G_CAV
    for line in cl:
        ax.text(LEFT, y, line, ha="left", va="top", fontsize=caveat_pt,
                family=SANS, weight="bold", color=BASALT)
        y -= caveat_pt * L_CAV / 72

    def draw_cell(cx, top, side_a, side_b, rest):
        """Three or four fixed-position children, encoded by fill, with the split
        spelled out underneath. Fill style and the caption both carry it, so
        nothing depends on colour alone."""
        role = {k: "out" for k in kids}
        for k in side_a: role[k] = "a"
        for k in side_b: role[k] = "b"
        cy = top - R
        x0 = cx - GAP*(len(kids)-1)/2
        for i, k in enumerate(kids):
            x = x0 + i*GAP
            r = role[k]
            if r == "a":
                ax.add_patch(Circle((x, cy), R, facecolor=EVERGREEN, edgecolor=EVERGREEN,
                                    lw=1.4, zorder=3)); ink = PAPER
            elif r == "b":
                ax.add_patch(Circle((x, cy), R, facecolor=PAPER, edgecolor=EVERGREEN,
                                    lw=1.8, zorder=3)); ink = EVERGREEN
            else:
                ax.add_patch(Circle((x, cy), R, facecolor=MIST, edgecolor=MIST,
                                    lw=1.4, zorder=3)); ink = SLATE
            ax.text(x, cy, k, ha="center", va="center", fontsize=cap_pt*0.95,
                    family=SANS, weight="bold", color=ink, zorder=4)
        ax.text(cx, cy - R - 0.11, f"{'+'.join(side_a)} vs {'+'.join(side_b)}",
                ha="center", va="top", fontsize=cap_pt, family=SANS,
                weight="bold", color=BASALT)
        tail = f"{'+'.join(rest)} stays out" if rest else "nobody left out"
        ax.text(cx, cy - R - 0.11 - cap_pt*1.30/72, tail, ha="center", va="top",
                fontsize=cap_pt*0.92, family=SANS, color=SLATE)

    # Panel v4, all four seats: nothing said what the three circle states meant.
    # Every seat reverse-engineered it from the captions and every seat said so.
    y -= G_KEY
    kr = R*0.86
    kx = LEFT + kr
    for face, edge, ink, label in ((EVERGREEN, EVERGREEN, PAPER, "one side"),
                                   (PAPER, EVERGREEN, EVERGREEN, "the other side"),
                                   (MIST, MIST, SLATE, "staying out")):
        ax.add_patch(Circle((kx, y - kr), kr, facecolor=face, edgecolor=edge,
                            lw=1.6, zorder=3))
        ax.text(kx + kr + 0.055, y - kr, label, ha="left", va="center",
                fontsize=cap_pt, family=SANS, color=SLATE)
        kx += kr + 0.055 + key_w[label] + 0.16
    y -= 2*kr + 0.06

    y -= G_GRID
    for (key, group), lines in zip(rows, headl):
        for s in lines:
            require_glyphs(SANS_B, s, "row header")
            ax.text(LEFT, y, s, ha="left", va="top", fontsize=head_pt,
                    family=SANS, weight="bold", color=EVERGREEN)
            y -= head_pt * L_HEAD / 72
        ax.plot([LEFT, W - LEFT], [y - 0.02, y - 0.02], color=MIST, lw=1.0, zorder=1)
        y -= G_RULE
        for i, (a, b, rest) in enumerate(group):
            r, c = divmod(i, cols)
            draw_cell(LEFT + (c + 0.5)*cell_w, y - r*cell_h, a, b, rest)
        y -= cell_h * -(-len(group) // cols)

    src_top = BOT + src_block
    if y < src_top - 1e-9:
        raise SystemExit(f"{stem}: grid overruns the source strip by {src_top - y:.3f} in")

    ax.add_patch(FancyBboxPatch((LEFT, BOT), 0.035, src_block*0.86,
                                boxstyle="square,pad=0", facecolor=EVERGREEN,
                                edgecolor="none", zorder=3))
    ys = BOT + src_block*0.86
    for line in srcl:
        ax.text(LEFT + 0.10, ys, line, ha="left", va="top", fontsize=source_pt,
                family=SANS, color=SLATE)
        ys -= src_step

    require_inside(fig)
    fig.savefig(f"{stem}.png", facecolor=PAPER, dpi=DPI)
    if pdf:
        fig.savefig(f"{stem}.pdf", facecolor=PAPER)
    plt.close(fig)
    print(f"  {stem}: {int(W*DPI)}x{int(H*DPI)} px, {len(configs)} cells in "
          f"{len(rows)} classes, {cols} cols{'  (+pdf)' if pdf else ''}")


print("enumeration")
build("figure_n3_web", ("A", "B", "C"), 4.32, 18.0, 13.0, 12.5, 12.0, 11.0, 11.0, cols=3)
build("figure_n3_design", ("A", "B", "C"), 7.00, 13.5, 10.5, 10.5, 10.5, 9.5, 8.5,
      cols=3, pdf=True)
build("figure_n4_design", ("A", "B", "C", "D"), 7.00, 13.5, 10.5, 10.5, 10.5, 9.5, 8.5,
      cols=4, pdf=True)
print("enumeration ok")

"""Both line figures, at every target, from one measured layout.

Replaces build_figure.py, build_figureA.py, build_narrow.py and build_web.py.

Those four hardcoded their line breaks and label positions against DejaVu metrics
at one canvas size each. That was survivable while the text never changed. It
stopped being survivable when the wording changed and the fonts became available:
four scripts drifting apart is exactly how the web renders came to disagree with
the manuscript figures. Here the breaks and margins are measured, so a target is
a size and a set of point sizes, and the wording lives in one place.

Targets
    design  7.00 x 4.80 in  -> 1050 x 720 px, and the PDF the manuscript includes
    narrow  3.60 x 4.20 in  ->  540 x 630 px, the interim mobile render
    web     4.32 x 5.04 in  ->  648 x 756 px, authored at 2x for a 324 px column

Run from inside figures/ — output filenames are bare.
"""

import matplotlib
import matplotlib.pyplot as plt

from cascadia_fig import (EVERGREEN, RAIN, BASALT, SLATE, MIST, PAPER, SERIF, SANS,
                          SERIF_B, SERIF_I, SANS_R, SANS_B,
                          width_in, wrap, widest_word, require_glyphs, require_inside)

# Embed real TrueType rather than Type 3, so the PDF carries the brand faces and
# the text stays selectable and searchable.
matplotlib.rcParams["pdf.fonttype"] = 42

DPI = 150

# min_pt is the smallest point size any text may take on this target. On web it is
# set by check 5.3's 12 px floor at the 324 px display width: 12 / 1.0417 = 11.52.
# Design is a print target and carries journal type sizes; narrow is the superseded
# interim render and is not held to the screen floor.
TARGETS = {
    "design": dict(W=7.00, H=4.80, title=13.5, sub=10.5, caveat=10.5, anno=10.5,
                   source=8.5, min_pt=0, pdf=True),
    "narrow": dict(W=3.60, H=4.20, title=10.0, sub=7.8,  caveat=8.0,  anno=8.2,
                   source=6.8, min_pt=0, pdf=False),
    "web":    dict(W=4.32, H=5.04, title=18.0, sub=13.0, caveat=12.5, anno=12.0,
                   source=11.6, min_pt=11.6, pdf=False),
}

SUBTITLE = "Every possible split into two opposing sides, with anyone left over staying out of it."
CAVEAT = "These are possibilities, not arguments that happened."
# Panel v4: the green series was sourced to a formula and the grey one was not,
# so a reader had to supply n(n-1)/2 themselves.
SOURCE = ("Source: OEIS A000392, S(n+1, 3); one against one is n(n-1)/2 · "
          "computed 2026-08-12 · exact counts, nothing estimated")

n8 = list(range(1, 9))
configs = [(3**k - 2*2**k + 1)//2 for k in n8]
pairs = [k*(k-1)//2 for k in n8]
assert configs == [0, 1, 6, 25, 90, 301, 966, 3025]
assert pairs == [0, 1, 3, 6, 10, 15, 21, 28]

# Figure A's range, sliced from the same series rather than retyped.
A_HI, A_LO = configs[:4], pairs[:4]

# The pairs series is the one-against-one slice of the configurations, verified by
# enumeration in Panel v3. The titles say so rather than setting one against the
# other as if they were independent quantities.
FIGURES = {
    "figure1": dict(
        title="Of the 3,025 ways eight children can take sides, just 28 are one against one",
        # Panel v4: "sixfold at first, nearer three later" left two seats unable to
        # say which numbers it referred to. It now names them.
        note="Each child multiplies the total: 6x at first, nearer 3x by eight.",
        # v4 said a leader landing on the n=7 marker read as "this is about n=7".
        # Removing it broke check 3.4's linkage requirement, so it is back and
        # anchored mid-segment, between markers, where it can only mean the curve.
        leader=True,
        xs=n8, hi=configs, lo=pairs,
        yticks=[0, 1500, 3000], ylabels=["0", "1,500", "3,000"],
        # K1: bounds derived from the series, not typed. The literals these replace
        # were correct until the data moved and silent thereafter.
        xlim=(0.8, 8.2), ylim=(0, max(configs)*1.06),
        end_hi="All ways to take sides: 3,025", end_lo="One against one: 28",
        end_hi_xy=(8, max(configs)), end_lo_xy=(8, max(pairs)),
        note_xy=(7.5, 1995), note_rad=-0.10,   # on the segment, not on a marker
        # value label -> (data xy, offset xy), per target where the geometry differs
        values={"design": [("90", (5, 90), (5, 300), EVERGREEN),
                           ("301", (6, 301), (5.9, 560), EVERGREEN),
                           ("966", (7, 966), (7.3, 700), EVERGREEN)],
                "narrow": [("90", (5, 90), (4.85, 330), EVERGREEN),
                           ("301", (6, 301), (5.8, 600), EVERGREEN),
                           ("966", (7, 966), (7.35, 690), EVERGREEN)],
                "web":    [("90", (5, 90), (5, 280), EVERGREEN),
                           ("301", (6, 301), (5.88, 516), EVERGREEN),
                           ("966", (7, 966), (7.32, 700), EVERGREEN)]},
        # Landscape puts the note far from its anchor, so it sits lower there and
        # the leader stays short rather than sweeping across the whole plot.
        note_at={"design": (1.15, 2450), "narrow": (1.1, 2950), "web": (1.15, 3080)},
    ),
    "figureA": dict(
        # Panel v4: "just 6" described something the plot correctly draws as about a
        # quarter. The adjective was doing work the picture refused to support.
        title="Of the 25 ways four children can take sides, 6 are one against one",
        # v4: "the first to separate" was read as a claim about the children, not
        # about the two lines, and cost one seat twenty seconds to unpick.
        note="At three children the counts part company: six ways, three one against one.",
        leader=True,
        xs=[1, 2, 3, 4], hi=A_HI, lo=A_LO,
        yticks=[0, 10, 20], ylabels=None,
        xlim=(0.85, 4.15), ylim=(0, max(A_HI)*1.09),
        end_hi=f"All ways to take sides: {max(A_HI)}", end_lo=f"One against one: {max(A_LO)}",
        end_hi_xy=(4, max(A_HI)), end_lo_xy=(4, max(A_LO)),
        note_xy=(3, 6), note_rad=0.10,
        # v4: the 0 and 1 labels floated far enough above their markers to read as
        # values of their own on a 0-25 scale.
        values={t: [("0", (1, 0), (1, 0.9), SLATE), ("1", (2, 1), (2, 1.9), SLATE),
                    ("6", (3, 6), (3, 7.6), EVERGREEN), ("3", (3, 3), (3.30, 2.1), SLATE)]
                for t in TARGETS},
        note_at={"design": (1.05, 22.0), "narrow": (1.02, 26.0), "web": (1.05, 26.6)},
    ),
}


def block(fig, x, y, lines, pt, leading, **kw):
    step = pt * leading / (fig.get_figheight() * 72)
    for line in lines:
        fig.text(x, y, line, ha="left", va="top", **kw)
        y -= step
    return y


def build(name, spec, target):
    t = TARGETS[target]
    W, H = t["W"], t["H"]
    TITLE_PT, SUB_PT, CAVEAT_PT = t["title"], t["sub"], t["caveat"]
    ANNO_PT, SOURCE_PT = t["anno"], t["source"]
    # Check 5.3: nothing below the target's floor. Tick labels were the smallest
    # text on the canvas and were the element that breached it.
    TICK_PT = max(ANNO_PT*0.92, t["min_pt"])

    fig = plt.figure(figsize=(W, H), dpi=DPI); fig.patch.set_facecolor(PAPER)
    LEFT = 0.052 if W < 5 else 0.030
    text_w = (1 - 2*LEFT) * W

    tl = wrap(fig, spec["title"], text_w, fontsize=TITLE_PT, family=SERIF, weight="bold")
    sl = wrap(fig, SUBTITLE, text_w, fontsize=SUB_PT, family=SANS)
    cl = wrap(fig, CAVEAT, text_w, fontsize=CAVEAT_PT, family=SANS, weight="bold")
    srcl = wrap(fig, SOURCE, text_w - 0.13, fontsize=SOURCE_PT, family=SANS)

    end_kw = dict(fontsize=ANNO_PT, family=SANS, weight="bold")
    gutter = max(widest_word(fig, [spec["end_hi"], spec["end_lo"]], **end_kw), 0.22*W)
    hi_lines = wrap(fig, spec["end_hi"], gutter, **end_kw)
    lo_lines = wrap(fig, spec["end_lo"], gutter, **end_kw)

    xlim = spec["xlim"]
    ylab = spec["ylabels"] if spec["ylabels"] else [str(v) for v in spec["yticks"]]
    ax_left = max(width_in(fig, s, fontsize=TICK_PT, family=SANS)
                  for s in ylab)/W + LEFT + 0.02
    end_x = xlim[1] + 0.01*(xlim[1]-xlim[0])
    anchor = (end_x - xlim[0]) / (xlim[1] - xlim[0])
    ax_width = (1 - LEFT - 0.010 - gutter/W - ax_left) / anchor

    for s in tl: require_glyphs(SERIF_B, s, "title")
    for s in sl: require_glyphs(SANS_R, s, "subtitle")
    for s in cl: require_glyphs(SANS_B, s, "caveat")
    for s in srcl: require_glyphs(SANS_R, s, "source strip")
    for s in hi_lines + lo_lines: require_glyphs(SANS_B, s, "end label")
    require_glyphs(SERIF_I, spec["note"], "annotation")

    y = 0.982
    y = block(fig, LEFT, y, tl, TITLE_PT, 1.24, fontsize=TITLE_PT, family=SERIF,
              weight="bold", color=BASALT)
    y -= 0.014
    y = block(fig, LEFT, y, sl, SUB_PT, 1.30, fontsize=SUB_PT, family=SANS, color=SLATE)
    y -= 0.010
    y = block(fig, LEFT, y, cl, CAVEAT_PT, 1.30, fontsize=CAVEAT_PT, family=SANS,
              weight="bold", color=BASALT)

    src_step = SOURCE_PT * 1.30 / (H * 72)
    src_top = 0.020 + src_step * len(srcl)
    ax_bottom = src_top + (0.098 if H > 4.5 else 0.115)
    ax_top = y - 0.030
    if ax_top - ax_bottom < 0.15:
        raise SystemExit(f"{name}/{target}: no room left for the plot "
                         f"({ax_top - ax_bottom:.3f} of canvas height)")

    ax = fig.add_axes([ax_left, ax_bottom, ax_width, ax_top - ax_bottom])
    ax.set_facecolor(PAPER)

    # Panel v4, three seats: the grey series vanished under the green at low n, so
    # a reader concluded it started at 5. Grey is drawn on top, and dashed, so it
    # stays visible where the two coincide.
    ax.plot(spec["xs"], spec["hi"], color=EVERGREEN, lw=2.2, marker="o", ms=5, zorder=2)
    ax.plot(spec["xs"], spec["lo"], color=RAIN, lw=2.4, marker="o", ms=4.5, zorder=3,
            dashes=(4, 2))

    # Ink is stated per label, not inferred. Panel v2 finding 2 put the labels at
    # n = 1 and 2 in neutral ink because both series pass through those points and
    # a coloured label would claim them for one series.
    for label, xy, xytext, ink in spec["values"][target]:
        ax.annotate(label, xy=xy, xytext=xytext, fontsize=ANNO_PT, family=SANS,
                    color=ink, ha="center")

    ax.annotate("\n".join(hi_lines), xy=spec["end_hi_xy"], xytext=(end_x, spec["end_hi_xy"][1]*0.985),
                fontsize=ANNO_PT, family=SANS, color=EVERGREEN, va="top",
                weight="bold", annotation_clip=False)
    # Stacks upward from its anchor, so a wrapped line grows away from the axis
    # instead of landing at x-tick height (Panel v3, finding 9).
    ax.annotate("\n".join(lo_lines), xy=spec["end_lo_xy"],
                xytext=(end_x, spec["ylim"][1]*0.018),
                fontsize=ANNO_PT, family=SANS, color=SLATE, va="bottom",
                weight="bold", annotation_clip=False)

    # A multi-line annotation anchors at its bottom and grows upward, which walks
    # a longer note out of the plot. Hang it from a set top instead.
    ax.annotate("\n".join(wrap(fig, spec["note"], ax_width*W*0.62, fontsize=ANNO_PT,
                               family=SERIF, style="italic")),
                xy=spec["note_xy"], xytext=spec["note_at"][target],
                fontsize=ANNO_PT, family=SERIF, style="italic", va="top", color=EVERGREEN,
                arrowprops=(dict(arrowstyle="-", color=EVERGREEN, lw=0.8,
                                 connectionstyle=f"arc3,rad={spec['note_rad']}")
                            if spec["leader"] else None), zorder=4)

    ax.set_xlim(*xlim); ax.set_ylim(*spec["ylim"])
    ax.set_xticks(spec["xs"]); ax.set_yticks(spec["yticks"])
    if spec["ylabels"]: ax.set_yticklabels(spec["ylabels"])
    ax.tick_params(colors=SLATE, labelsize=TICK_PT, length=3)
    for lbl in ax.get_xticklabels()+ax.get_yticklabels():
        lbl.set_family(SANS); lbl.set_color(SLATE)
    ax.set_xlabel("Number of children", fontsize=TICK_PT, family=SANS, color=SLATE)
    for s in ["top", "right"]: ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]: ax.spines[s].set_color(MIST)

    fig.patches.append(plt.Rectangle((LEFT, 0.020), 0.007*(4.32/W),
                                     src_step*len(srcl)*0.86,
                                     transform=fig.transFigure, color=EVERGREEN,
                                     clip_on=False))
    ys = src_top - src_step*0.30
    for line in srcl:
        fig.text(LEFT + 0.023*(4.32/W), ys, line, ha="left", va="top",
                 fontsize=SOURCE_PT, family=SANS, color=SLATE)
        ys -= src_step

    require_inside(fig)
    stem = f"{name}_{target}"
    fig.savefig(f"{stem}.png", facecolor=PAPER, dpi=DPI)
    if t["pdf"]:
        fig.savefig(f"{stem}.pdf", facecolor=PAPER)
    plt.close(fig)
    print(f"  {stem}: {int(W*DPI)}x{int(H*DPI)} px, title {len(tl)}L, "
          f"plot {ax_width*W:.2f} in, gutter {gutter:.2f} in"
          f"{'  (+pdf)' if t['pdf'] else ''}")


for fname, spec in FIGURES.items():
    print(fname)
    for target in TARGETS:
        build(fname, spec, target)
print("lines ok")

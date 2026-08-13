"""Web renders of Figure 1 and Figure A — brand fonts, mobile-legible type.

A third target alongside build_figure.py / build_figureA.py / build_narrow.py.
Those are untouched: the design renders are in the manuscript the editors hold,
and the narrow renders are the panel-cleared interim artifacts on the site.

Authored at twice the 324 px mobile slot so the image stays crisp at 2x. At
dpi=150 with natural_width = 2 x display_width the point-to-css conversion
collapses to css_px = pt x (150/72) x (1/2) = pt x 1.042, so the point sizes
below can be read straight off the display targets:

    chart title 18 pt -> ~18.8 px      subtitle 13 pt -> ~13.5 px
    annotations, value and end labels 12 pt -> ~12.5 px
    source strip 11 pt -> ~11.5 px

against a 15.3 px page caption and 17 px body. The narrow renders put the
subtitle at 9.8 px, which is what made this re-render necessary.

Aspect is held at the narrow renders' portrait 540x630. Whether the web renders
should take a web-specific aspect instead is an open question for the panel, not
one to settle here.

Wording follows the narrow renders: these occupy the same mobile slot.

Run from inside figures/ — output filenames are bare.
"""

import matplotlib.pyplot as plt

from cascadia_fig import (EVERGREEN, RAIN, BASALT, SLATE, MIST, PAPER, SERIF, SANS,
                          SERIF_B, SERIF_I, SANS_R, SANS_B,
                          width_in, wrap, widest_word, require_glyphs, require_inside)

TITLE_PT=18.0; SUB_PT=13.0; CAVEAT_PT=12.5; ANNO_PT=12.0; SOURCE_PT=11.0
W=4.32; H=5.04; DPI=150          # 648 x 756 px, displayed at 324 px

n=list(range(1,9)); configs=[(3**k-2*2**k+1)//2 for k in n]; pairs=[k*(k-1)//2 for k in n]
assert configs==[0,1,6,25,90,301,966,3025] and pairs==[0,1,3,6,10,15,21,28]


def block(fig, y, lines, pt, leading, **kw):
    """Draw lines top-down from y (figure fraction). Returns the new cursor."""
    step = pt * leading / (fig.get_figheight() * 72)
    for line in lines:
        fig.text(0.052, y, line, ha="left", va="top", **kw)
        y -= step
    return y


def build(fname, title, subtitle, caveat, note, xs, series_hi, series_lo, yticks, ylabels,
          xlim, ylim, value_labels, end_hi, end_lo, note_xy, note_xytext, note_rad):
    fig = plt.figure(figsize=(W,H), dpi=DPI); fig.patch.set_facecolor(PAPER)

    text_w = 0.90 * W
    tl = wrap(fig, title, text_w, fontsize=TITLE_PT, family=SERIF, weight="bold")
    sl = wrap(fig, subtitle, text_w, fontsize=SUB_PT, family=SANS)
    cl = wrap(fig, caveat, text_w, fontsize=CAVEAT_PT, family=SANS, weight="bold")
    # words() keeps a lone separator with the word before it, so no line opens with "·".
    src = ("Source: OEIS A000392, S(n+1, 3) · computed 2026-08-12 · "
           "exact counts, nothing estimated")
    srcl = wrap(fig, src, text_w - 0.13, fontsize=SOURCE_PT, family=SANS)

    # The end labels sit outside the axes, so the axes get whatever width is left
    # over. The gutter cannot be narrower than the longest word in them
    # ("configurations:") — assuming otherwise is what clipped the first render.
    end_kw = dict(fontsize=ANNO_PT, family=SANS, weight="bold")
    # Panel v3 finding 9: the low label's second line landed at x-tick height and
    # read as part of the axis. Forcing it onto one line fixed that but spent a
    # third of the canvas on the gutter. It stacks upward from its anchor instead,
    # so a wrapped line grows away from the axis and the gutter stays modest.
    gutter = max(widest_word(fig, [end_hi[0], end_lo[0]], **end_kw), 1.10)
    hi_lines = wrap(fig, end_hi[0], gutter, **end_kw)
    lo_lines = wrap(fig, end_lo[0], gutter, **end_kw)
    for s in hi_lines + lo_lines: require_glyphs(SANS_B, s, "end label")

    # Left margin measured off the widest y-tick label rather than guessed, for
    # the same reason the gutter is: the labels changed and a hardcoded 0.175 was
    # spending width the plot needed.
    ylab = ylabels if ylabels else [str(t) for t in yticks]
    ax_left = max(width_in(fig, s, fontsize=ANNO_PT*0.92, family=SANS) for s in ylab)/W + 0.052

    # Fraction of the axes width at which the end-label text starts.
    anchor = max((end_hi[2][0] - xlim[0]) / (xlim[1] - xlim[0]),
                 (end_lo[2][0] - xlim[0]) / (xlim[1] - xlim[0]))
    ax_width = (1 - 0.028 - gutter/W - ax_left) / anchor

    for s in tl: require_glyphs(SERIF_B, s, "title")
    for s in sl: require_glyphs(SANS_R, s, "subtitle")
    for s in cl: require_glyphs(SANS_B, s, "caveat")
    for s in srcl: require_glyphs(SANS_R, s, "source strip")
    require_glyphs(SERIF_I, note, "annotation")

    y = 0.982
    y = block(fig, y, tl, TITLE_PT, 1.24, fontsize=TITLE_PT, family=SERIF, weight="bold", color=BASALT)
    y -= 0.014
    y = block(fig, y, sl, SUB_PT, 1.30, fontsize=SUB_PT, family=SANS, color=SLATE)
    # Panel v3 findings 1 and 3: two seats independently reported the caveat read
    # third and in grey, losing to a title that reads like a warning. In body ink
    # now, on its own line.
    y -= 0.010
    y = block(fig, y, cl, CAVEAT_PT, 1.30, fontsize=CAVEAT_PT, family=SANS,
              weight="bold", color=BASALT)

    # Source strip sits on the bottom margin; the axes take what is left between.
    src_step = SOURCE_PT * 1.30 / (H * 72)
    src_top = 0.020 + src_step * len(srcl)
    ax_bottom = src_top + 0.098          # clearance for the x-axis label
    ax_top = y - 0.030

    ax = fig.add_axes([ax_left, ax_bottom, ax_width, ax_top - ax_bottom]); ax.set_facecolor(PAPER)

    ax.plot(xs, series_hi, color=EVERGREEN, lw=2.2, marker="o", ms=5, zorder=3)
    ax.plot(xs, series_lo, color=RAIN, lw=2.2, marker="o", ms=4.5, zorder=2)

    for label, xy, xytext, color in value_labels:
        ax.annotate(label, xy=xy, xytext=xytext, fontsize=ANNO_PT, family=SANS,
                    color=color, ha="center")

    ax.annotate("\n".join(hi_lines), xy=end_hi[1], xytext=end_hi[2], fontsize=ANNO_PT, family=SANS,
                color=EVERGREEN, va=end_hi[3], weight="bold", annotation_clip=False)
    ax.annotate("\n".join(lo_lines), xy=end_lo[1], xytext=end_lo[2], fontsize=ANNO_PT, family=SANS,
                color=SLATE, va="bottom", weight="bold", annotation_clip=False)

    ax.annotate("\n".join(wrap(fig, note, ax_width*W*0.62, fontsize=ANNO_PT,
                               family=SERIF, style="italic")),
                xy=note_xy, xytext=note_xytext, fontsize=ANNO_PT, family=SERIF, style="italic",
                # A multi-line block anchors at its bottom by default, so it grows
                # upward and a longer note climbs out of the plot. Hang it instead.
                va="top", color=EVERGREEN,
                arrowprops=dict(arrowstyle="-", color=EVERGREEN, lw=0.8,
                                connectionstyle=f"arc3,rad={note_rad}"), zorder=4)

    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xticks(xs); ax.set_yticks(yticks)
    if ylabels: ax.set_yticklabels(ylabels)
    ax.tick_params(colors=SLATE, labelsize=ANNO_PT*0.92, length=3)
    for t in ax.get_xticklabels()+ax.get_yticklabels(): t.set_family(SANS); t.set_color(SLATE)
    ax.set_xlabel("Number of children", fontsize=ANNO_PT*0.92, family=SANS, color=SLATE)
    for s in ["top","right"]: ax.spines[s].set_visible(False)
    for s in ["left","bottom"]: ax.spines[s].set_color(MIST)

    fig.patches.append(plt.Rectangle((0.052, 0.020), 0.007, src_step*len(srcl)*0.86,
                                     transform=fig.transFigure, color=EVERGREEN, clip_on=False))
    ys = src_top - src_step*0.30
    for line in srcl:
        fig.text(0.075, ys, line, ha="left", va="top", fontsize=SOURCE_PT, family=SANS, color=SLATE)
        ys -= src_step

    require_inside(fig)
    fig.savefig(fname, facecolor=PAPER, dpi=DPI)
    plt.close(fig)
    print(f"{fname}: {int(W*DPI)}x{int(H*DPI)} px  ->  {int(W*DPI/2)} px slot\n"
          f"    title {len(tl)} lines, subtitle {len(sl)} lines, source {len(srcl)} lines\n"
          f"    gutter {gutter:.2f} in, plot {ax_width*W:.2f} in ({int(ax_width*W*DPI)} px)")


build("figure1_web.png",
      # v3 finding 8: the pairs are the one-against-one configurations, so the old
      # "but form only" set a total against its own subset. The title now says so.
      "Of the 3,025 ways eight children can take sides, just 28 are one against one",
      # v3 finding 17: the bare algebraic n nearly stopped the least technical seat.
      "Every possible split into two opposing sides, with anyone left over staying out of it.",
      "These are possibilities, not arguments that happened.",
      # v3 finding 3: the multiplier is asymptotic. It is 6.00 and 4.17 before it
      # is anywhere near 3, so "roughly triples" was not true over this range.
      "Each added child multiplies the total: sixfold at first, nearer three later.",
      n, configs, pairs,
      [0,1500,3000], ["0","1,500","3,000"],
      (0.8,8.2), (0, max(configs)*1.06),
      [("90",(5,90),(5,90+190),EVERGREEN),
       ("301",(6,301),(5.88,301+215),EVERGREEN),
       # v3 finding 7: was (6.72, 966+235), under the leader and against the steep
       # segment. Above the marker only moved the collision — the segment climbs
       # through that space too. Below-right of the marker is the open quadrant.
       ("966",(7,966),(7.32,700),EVERGREEN)],
      ("All ways to take sides: 3,025", (8,3025), (8.28,2980), "top"),
      ("One against one: 28", (8,28), (8.28,60), "center"),
      # The curve stays on the floor until n≈7, so the upper-left quadrant is the
      # one place a four-line note fits without crossing anything.
      (7,966), (1.15,3080), -0.18)

build("figureA_web.png",
      "Of the 25 ways four children can take sides, just 6 are one against one",
      "Every possible split into two opposing sides, with anyone left over staying out of it.",
      "These are possibilities, not arguments that happened.",
      # v3 finding 15: "already double" implied the crossing happened earlier than
      # expected; n = 3 is in fact the first point where the two counts separate.
      "Three children are the first to separate: six ways, three of them one against one.",
      [1,2,3,4], [0,1,6,25], [0,1,3,6],
      [0,10,20], None,
      (0.85,4.15), (0, 25*1.09),
      [("0",(1,0),(1,1.5),SLATE),
       ("1",(2,1),(2,2.6),SLATE),
       ("6",(3,6),(3,7.9),EVERGREEN),
       # v3 finding 10: stacked under the "6" it reads as one series' pair of
       # labels, and the annotation's doubling claim rests on both being legible.
       ("3",(3,3),(3.30,2.0),SLATE)],
      ("All ways to take sides: 25", (4,25), (4.16,24.8), "top"),
      ("One against one: 6", (4,6), (4.16,6), "center"),
      (3,6), (1.05,26.6), 0.15)

print("web ok")

"""Shared figure machinery for the web renders.

Extracted from build_web.py when a second web figure needed the same guards.
The design and narrow builds do not use this module — they are frozen artifacts
and are left exactly as they were.

Two silent failure modes are asserted against here, because both have already
shipped once in this piece: matplotlib substitutes DejaVu for an unresolved
family with only a warning, and a resolved face missing a glyph draws tofu just
as quietly. A third guard catches text running off the canvas, which is a
clipping bug that only looking at the PNG would otherwise find.
"""

import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import text as mtext

EVERGREEN="#1E7A4C"; RAIN="#9AA6A0"; BASALT="#232B27"; SLATE="#5B6660"; MIST="#E4E7E3"; PAPER="#FCFCFA"
SERIF="Source Serif 4"; SANS="Segoe UI"

DPI=150


def require_family(family, weight="normal", style="normal"):
    prop = font_manager.FontProperties(family=family, weight=weight, style=style)
    path = font_manager.findfont(prop, fallback_to_default=False)
    got = font_manager.get_font(path).family_name
    if not got.lower().startswith(family.lower()):
        raise SystemExit(f"font resolved to {got!r}, expected {family!r} ({weight}/{style})")
    return path


def require_glyphs(path, text, label):
    font = font_manager.get_font(path)
    missing = sorted({c for c in text if not c.isspace() and font.get_char_index(ord(c)) == 0})
    if missing:
        codes = ", ".join(f"{c!r} U+{ord(c):04X}" for c in missing)
        raise SystemExit(f"{label}: font at {path} lacks {codes}")


SERIF_R = require_family(SERIF)
SERIF_B = require_family(SERIF, weight="bold")
SERIF_I = require_family(SERIF, style="italic")
SANS_R  = require_family(SANS)
SANS_B  = require_family(SANS, weight="bold")


def width_in(fig, s, **kw):
    t = fig.text(0, 0, s, **kw)
    w = t.get_window_extent(fig.canvas.get_renderer()).width / fig.dpi
    t.remove()
    return w


def words(text):
    """Tokenise for wrapping, keeping a lone separator with the word before it
    so no wrapped line can open with a dangling bullet."""
    out=[]
    for w in text.split(" "):
        if not w: continue
        if out and len(w) == 1 and not w.isalnum():
            out[-1] = f"{out[-1]} {w}"
        else:
            out.append(w)
    return out


def wrap(fig, text, max_in, **kw):
    lines=[]; cur=""
    for word in words(text):
        trial = f"{cur} {word}" if cur else word
        if cur and width_in(fig, trial, **kw) > max_in:
            lines.append(cur); cur = word
        else:
            cur = trial
    if cur: lines.append(cur)
    return lines


def widest_word(fig, texts, **kw):
    """The narrowest column these strings can wrap into without a word clipping."""
    return max(width_in(fig, w, **kw) for t in texts for w in words(t))


def require_inside(fig, pad=1.0):
    """No text may run off the canvas. Labels placed outside the axes with
    annotation_clip off walk off the edge silently — which they did on the first
    web render, and which only looking at the PNG caught."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    edge = fig.bbox
    for t in fig.findobj(mtext.Text):
        if not t.get_visible() or not t.get_text().strip():
            continue
        bb = t.get_window_extent(r)
        if (bb.x0 < -pad or bb.y0 < -pad or bb.x1 > edge.x1 + pad or bb.y1 > edge.y1 + pad):
            raise SystemExit(
                f"text runs off the canvas: {t.get_text()!r}\n"
                f"    bbox x[{bb.x0:.0f}, {bb.x1:.0f}] y[{bb.y0:.0f}, {bb.y1:.0f}] "
                f"vs canvas [0, {edge.x1:.0f}] x [0, {edge.y1:.0f}]")

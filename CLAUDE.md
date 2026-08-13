# Cascadia Curiosities — what an agent needs to know

Non-BI work built to the Cascadia standard: papers, essays, one-off charts.
Each piece is self-contained under `curiosities/<piece>/` with its own
`governance/`. The repo publishes nothing on its own — pieces go out to
journals, or get linked from `robbinsanalytics.com` (site repo work, never done
from here).

## Piece status is a field, and it is load-bearing

**Read `curiosities/<piece>/correspondence/` before doing anything that touches
the outside world.** Every piece carries a status line there; the trailing
status note in the newest correspondence file is authoritative.

| Piece | Status |
|---|---|
| `sibling-conflict-combinatorics` | **Query sent 2026-08-12** to The Mathematical Intelligencer (co-EiCs Parshall and Tabachnikov). Awaiting reply. **Manuscript revised 2026-08-13** and now differs from what was queried — the revision has not been sent, and sending it is not an agent action. |

A piece under query has been sent to a human who is going to reply. **Do not
re-send, do not post it anywhere, do not draft a response to editors.** When a
reply arrives: log it in `correspondence/`, update the status line, and stop —
what to say back is Aaron's call in a fresh conversation.

Both target journals for this piece require exclusive submission, one at a time.
That is why a second submission is never a low-risk parallel action.

## cascadia-standards is read-only reference from here

`VIZ-PRINCIPLES.md` and `CHART-REVIEW.md` live in
`C:\Projects\cascadia-standards\design-system\` — **currently v2.5, and the two
ship together under one version number.** Read them there. Never edit that repo
from a session rooted here, and never commit in it: hooks and `CLAUDE.md` load
only from the primary working directory, so such a commit is unguarded by every
protection below.

**Every chart in this repo clears `CHART-REVIEW.md` before it ships, including
the Rule 7.4 reading panel.** No exception for "it's just a figure for a paper" —
the sibling-conflict figures went through two panels and the second one is why
Figure A exists at all.

## Building the manuscript

**The artifact that went out with the query is preserved by filename, not by a
build ban.** It is `manuscript/manuscript-as-queried-2026-08-12.pdf` (235,388
bytes) and it is never regenerated — nothing rebuilds that name. `manuscript.pdf`
and `Robbins-Combinatorics-of-Sibling-Conflict.pdf` track the current source and
may be rebuilt freely; they diverged from the queried version on 2026-08-13, when
the subset finding was fixed.

This replaces the earlier rule that forbade rebuilding in place. That rule existed
to protect the "this is what they received" property, which a dated filename
protects better, and it stopped being workable once the manuscript itself had to
change. Aaron's decision, 2026-08-13: nothing was formally submitted, so the paper
can be revised and the revision is what any future submission uses.

Build with the working directory set to `manuscript/` — the figure paths are
relative and resolve from the CWD, not from the output directory:

```
pdflatex -interaction=nonstopmode "-output-directory=<scratch>" manuscript.tex
```

run twice. **Quote the `-output-directory=` argument in PowerShell.** Unquoted,
`$scratch` is not expanded and pdflatex creates a literal `$scratch` directory
inside `manuscript/`.

**MiKTeX is user-scope and not on `PATH` for every shell**:
`%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe`. Installed
2026-08-12 with `[MPM]AutoInstall=1` so missing packages fetch instead of
blocking on a prompt. Verified 2026-08-13: two passes, 9 pages, converged, no
errors, all four figure PDFs resolved.

**`manuscript/` and `figures/` are separate folders, so `\graphicspath` carries
the figure resolution**, not the `\includegraphics` calls — those are bare
filenames and resolved from the same directory in the pre-migration submission
folder. Both paths are searched, so the source still works as a flat bundle when
a portal wants one file per upload.

**The `build_*.py` scripts write bare filenames into the current directory** —
run them from inside `figures/` or they scatter output into the repo root.

**Two build scripts, not five.** `build_lines.py` emits both line figures at all
three targets (design + PDF, narrow, web); `build_enumeration.py` emits the worked
examples (n=3 web and design, n=4 design). Shared font, glyph and off-canvas guards
live in `cascadia_fig.py`. The four per-figure, per-size scripts they replaced
hardcoded line breaks against DejaVu metrics at one canvas size each, and drifting
apart is exactly how the web renders came to disagree with the manuscript figures.

**The brand fonts are installed and asserted, so the DejaVu exception is closed.**
Source Serif 4 (Adobe 4.005, per-user install) and Segoe UI both resolve; every
build fails loudly rather than substituting, and also fails on a missing glyph.
Any new figure should import those guards rather than reimplement them.

## Committing

**Stage by name — never `git add -A` or `git add .`.** Both are denied in
`.claude/settings.json`, and a `PreToolUse` hook refuses any commit carrying a
whitespace-only diff. Verify with
`git diff --ignore-all-space --numstat -- <file>`; empty output means the diff
is noise and the file must not be staged.

## Naming

**The Control Tower company allow-list does not govern this repo** — there is no
Cascadia company universe here, and pieces are about whatever they are about.

**The calibration filer is never named, here or anywhere.** It is a real,
formerly-listed department-store operator whose published figures shape the
Control Tower generator. No Robbins repo records which company it is — that
rule is absolute and does not depend on the allow-list above.

## Aaron

**Aaron does not write code and does not run scripts.** He approves decisions;
the agent executes. Never end a task with "now run this."

**Prefer "I could not establish this" over inferring.** Ambiguity stops the work
and asks.

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
| `sibling-conflict-combinatorics` | **Query sent 2026-08-12** to The Mathematical Intelligencer (co-EiCs Parshall and Tabachnikov). Awaiting reply. |

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

## The manuscript does not compile on this machine

**`pdflatex` is not installed here** — no MiKTeX, no TeX Live, checked
2026-08-12. The committed `manuscript.pdf` was built elsewhere and is the
artifact that was actually sent to the editors. Do not claim a LaTeX build was
verified from this machine without installing a distribution first and saying so.

**`manuscript/` and `figures/` are separate folders, so `\graphicspath` carries
the figure resolution**, not the `\includegraphics` calls — those are bare
filenames and resolved from the same directory in the pre-migration submission
folder. Both paths are searched, so the source still works as a flat bundle when
a portal wants one file per upload.

**The `build_*.py` scripts write bare filenames into the current directory** —
run them from inside `figures/` or they scatter output into the repo root.

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

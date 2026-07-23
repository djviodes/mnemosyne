# AUTHORSHIP.md

A factual record of who wrote what in this repo, kept for transparency
alongside the working agreement in CLAUDE.md. Point-in-time as of
commit `df4b932` (2026-07-22) — update this file as new files or
exceptions are added.

## The rule

Per CLAUDE.md: David writes all implementation code. Claude's role in
this repo (Claude Code, in this conversation) is limited to code
review (reading, running the code to verify behavior, reporting
bugs), pointing to relevant concepts/docs, and — only when explicitly
asked, and only after the first two steps — offering small snippets
clearly labeled as illustrative rather than code to paste in. Project
documentation (this file included) is the one area Claude writes
directly, by David's explicit delegation.

Note the two distinct "Claude"s in this document: **Claude (web app)**
refers to a separate claude.ai conversation David used before this
repo existed, to draft initial scaffolding files. **Claude (Code)**
refers to this assistant, working directly in the repo across this
conversation. They're different sessions with no shared memory of
each other — everything Claude (Code) knows about the web-app
session's output, it learned by reading the files David committed.

## Documentation

| File | Author | Notes |
|---|---|---|
| `CLAUDE.md` | Claude (web app) | Drafted by claude.ai (not Claude Code) in a separate conversation, from David's prompt asking it to produce the introductory Markdown files for this repo. David then added the file to the repo. Claude Code has never edited its content. |
| `DESIGN.md` | Claude (web app), then Claude (Code) | Initial draft also came from that same claude.ai conversation. Substantially rewritten/maintained by Claude Code across this conversation, by explicit delegation ("I want you to handle that to leave my mental capacity for implementing the cache"). Decisions reflected in it were made by David in conversation; the words on the page are Claude's, in both phases. |
| `README.md` | Claude (web app), then Claude (Code) | Same basis as `DESIGN.md`. |
| `AUTHORSHIP.md` (this file) | Claude (Code) | Written at David's request. |
| `LICENSE` | Pre-existing | Standard MIT boilerplate, predates this conversation. |
| `.gitignore` | Claude (Code) | Added to exclude `__pycache__`/`*.pyc` generated while Claude was running tests. |

## Source code (`python/lru/`)

| File | Author | Notes |
|---|---|---|
| `cache.py` | David | 100%. Claude never used a file-editing tool on this file — only read it and ran it via the terminal to test behavior and report bugs. Every line, comment, and docstring is David's. |
| `doubly_linked_list.py` | David, with one documented exception below | Same basis as `cache.py` — read and tested, never edited by Claude — except for one comment block. |

### The one exception

The `CONSIDER(david)` comment above `remove_node` in `doubly_linked_list.py`
(~14 lines, documenting why the method trusts that a target node
belongs to the current list instance) was drafted verbatim by Claude
(Code), at David's explicit request, then pasted into the file by
David. This is a comment — it has no effect on program behavior — but
the exact text was Claude's, so it's called out here rather than
folded into "David wrote this."

### Not an exception (for contrast)

Earlier in the conversation, Claude (Code) was asked how it would
rewrite `cache.py`'s module-level header docstring, and gave an
illustrative example, explicitly labeled as not meant to be pasted in
directly. David wrote his own final wording instead — none of that
illustrative text made it into the file. Listed here only to make the
distinction clear: an example being *offered* isn't the same as an
example being *used*, and this repo has exactly one instance of the
latter (above).

## Summary

Every line of code in `python/lru/` — logic, comments, docstrings,
and design decisions about how that logic is shaped — was written by
David, with the single exception of the `CONSIDER(david)` comment
noted above. The project-level Markdown docs have a different
lineage: initially drafted by Claude (web app) from a one-line prompt,
before this repo or this conversation existed, then substantially
rewritten and maintained by Claude (Code) throughout this conversation
by David's explicit delegation.

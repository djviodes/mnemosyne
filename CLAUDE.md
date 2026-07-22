# Mnemosyne — Working Agreement

Small caching library, Python + Go implementations, built to develop
real fluency in caching strategies (LRU first) rather than just
reading about them. See README.md and DESIGN.md for scope and
architecture.

## How I want you to work with me here

I write all the code myself. This is deliberate skill-building, not a
delivery deadline — the whole point is closing a real gap (I didn't
know LRU or its standard implementation approach before this project).
Do not generate implementations for me, even if I ask directly.
Redirect me back to my own reasoning first.

### When I hit something I don't know how to implement

Follow this order, don't skip ahead:

1. **Point me to docs or the relevant concept only.** Name the pattern
   or data structure (e.g. "look at how a doubly linked list supports
   O(1) removal from an arbitrary node" or "look up Go's container/list
   package docs"), don't explain it yet.
2. **If I'm still stuck after that**, explain the underlying concept
   the way a professor would in office hours — build intuition, use
   analogies if useful, walk through *why* it works, not just what to
   type. Still no code handed to me directly at this stage — concept
   only.
3. Only after both of those, if I explicitly ask you to show a small
   illustrative snippet, keep it minimal and clearly labeled as
   illustrative, not something to paste in directly.

### Review role

Once I've written something, review it like a senior engineer doing a
PR review:
- Point out bugs, race conditions, unhandled errors, design issues
- Ask me to explain my reasoning on non-obvious decisions rather than
  just approving or rewriting them
- Flag when something works but isn't idiomatic Python or Go, or
  doesn't match the design goals in DESIGN.md
- Don't rewrite my code wholesale as the "fix" — tell me what's wrong
  and let me fix it

### What NOT to do

- Don't write functions, classes, or structs for me from scratch
- Don't "helpfully" complete a partial implementation I've started
- Don't skip straight to explaining a concept if I haven't tried
  finding it in docs first
- Don't suggest using a language's built-in shortcut (e.g.
  `OrderedDict`, `container/list`) as the first-pass solution — the
  point is understanding the mechanics manually first

## Engineering Conventions

### Error handling
- Errors MUST be handled, not ignored or silently swallowed
- Flag it in review if I've left an error unchecked or logged-and-forgotten
  without a real handling decision

### Testing
- Write tests for both best-case scenarios and failure modes, not just
  the happy path
- Cover boundary conditions explicitly: zero capacity, single-item
  capacity, updating an existing key, evicting under full load
- Run tests after any change, don't assume it works

### Design notes
- Use `CONSIDER(david):` comments to flag a future design question or
  tradeoff worth revisiting, instead of solving it immediately or
  leaving it undocumented

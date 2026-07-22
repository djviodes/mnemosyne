# DESIGN.md

## Goal

Build a small, genuinely reusable caching library, implemented in both
Python and Go, covering standard caching strategies with correct,
well-tested implementations — not a toy or a copy-paste exercise, but
something with a real, sensible API that could actually be dropped into
a future project.

## Scope (MVP)

Two independent cache types, each implemented for real in both
Python and Go — no throwaway translation step first:

- **LRU cache**: `.get()` / `.put()` / delete, fixed capacity, O(1)
  operations, capacity-based eviction only (no TTL — see Roadmap)
- **TTL / expiring cache**: `.get()` / `.put()` / delete, time-based
  expiration only (no capacity-based eviction — see Design Decisions)
- Explicit method API in both languages (not a dict/map-mimicking
  interface) — see Design Decisions
- Single-threaded / non-concurrent; no locking in the MVP — see
  Design Decisions
- Fixed, concrete key/value types for the first pass; generics
  deferred — see Design Decisions
- Unit tests covering: basic get/set, eviction/expiration behavior,
  capacity/duration boundary conditions, updating an existing key
  (should not evict), and any edge cases around zero/negative
  capacity or zero/negative TTL

## Roadmap

1. **MVP (current).** Build both cache types above, directly and for
   real, in Python and Go, following the Design Decisions below
   (manual data structures, no shortcuts, explicit API).
   Inspired by [MosheWorld/CacheStrategies](https://github.com/MosheWorld/CacheStrategies)'s
   two real implementations:
   - Its "In Memory Cache" (`Map`-backed, capacity-limited LRU) maps
     to this project's LRU cache — built here as pure LRU first,
     without the TTL it also bundles.
   - Its "Client Side Cache" (browser `localStorage` + 10s TTL
     wrapping an API call) maps to this project's TTL/expiring
     cache — renamed from "client-side" since there's no browser
     context in a Python/Go library; what's actually reusable here
     is the time-based expiration logic, not the browser storage.
   Its "Distributed Cache" folder is example use cases, not a real
   implementation, and isn't translated — see Post-MVP.
2. **Post-MVP.**
   - Combine LRU eviction and TTL expiration into one cache (matching
     how the reference's In Memory Cache does both at once), once
     each mechanism is solid on its own
   - LFU
   - Write-through vs. cache-aside patterns
   - Distributed caching backed by Redis (not hand-rolled — see
     Non-Goals)
   - Revisit generics and thread-safety (see Decided)

## Design Decisions

### Why LRU and TTL first
LRU is the most commonly needed eviction strategy in practice. A
TTL/expiring cache is a genuinely different mechanism (time-based,
no capacity limit) rather than a variation on LRU, so building both
now — separately — covers two real, distinct patterns before
combining or extending either.

### Why Python AND Go, not just one
The goal isn't just "have a caching library" — it's building real,
comparable fluency in implementing the same data structure and
algorithm correctly in two different language paradigms (dynamic vs.
statically typed, GC behavior differences, idiomatic interfaces in
each ecosystem).

### Implementation approach (Python) — LRU cache
Classic hash map + doubly linked list for O(1) get/put/evict. Avoid
relying on `collections.OrderedDict` as a shortcut for the first
pass — build the linked list and hash map manually to actually
understand the mechanics, even though `OrderedDict` would trivially
solve this in one line.

### Implementation approach (Go) — LRU cache
Same core structure (map + doubly linked list), written idiomatically
for Go — explicit struct definitions, no unnecessary abstraction,
consider using Go's `container/list` package only after implementing
it manually once, for the same "understand it before shortcutting it"
reason as the Python side.

### Implementation approach — TTL / expiring cache
Hash map of key → (value, expiration time). No linked list needed —
there's no ordering/eviction-by-position, just an age check on read
(and optionally an active background sweep, post-MVP). Keep this
implementation independent of the LRU cache's internals even though
both may eventually be combined post-MVP.

## Decided (2026-07-22)

- **Public API**: explicit method names (`.get()`, `.put()`, `.evict()`
  / `.delete()`), not a dict/map-mimicking interface.
- **Thread-safety**: none in the MVP — explicitly single-threaded /
  non-concurrent. Revisit post-MVP.
- **Generics**: fixed, concrete key/value types for the first pass.
  Revisit Go generics / Python `typing.Generic` post-MVP, once the
  concrete-type versions are correct.
- **TTL scope**: the LRU cache's MVP is pure capacity-based eviction
  only; TTL/expiration ships as its own separate cache type in the
  MVP, and merging the two (as the reference implementation does) is
  deferred to post-MVP.
- **Naming**: "client-side cache" (the reference repo's term) is
  called a TTL / expiring cache in this project, since the reusable
  part is the expiration logic, not browser storage. Similarly, the
  cache-type directories are named for eviction policy, not storage
  location — `lru/` and `ttl/` in both `python/` and `go/` — since
  both caches are in-memory and "in-memory" wasn't actually
  distinguishing anything.

## Open Questions

- None currently open — resolved decisions are captured above and in
  Roadmap; revisit generics/thread-safety/LRU+TTL merge post-MVP.

## Non-Goals (for now)

- Hand-rolled distributed/multi-node caching protocol — post-MVP
  distributed caching will be backed by Redis rather than built from
  scratch, matching how this is actually done in practice
- Persistence to disk (outside of what Redis itself provides, once
  that lands post-MVP)
- Production-grade performance tuning — correctness first

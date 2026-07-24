# Mnemosyne — A Caching Library in Python & Go

A small, focused caching library implementing common caching strategies
(starting with LRU, expanding from there) in both Python and Go — built
as a hands-on way to go deep on caching concepts and produce something
reusable across future projects in either language.

## Why This Exists

Caching strategies (LRU, LFU, write-through, cache-aside, etc.) come up
constantly in backend and systems design work, but "I've read about it"
and "I've implemented it correctly, twice, in two different languages"
are very different levels of understanding. This project exists to close
that gap directly, not just talk about it.

## What's Here

- **Python implementation** — `python/`, with `lru/` (LRU cache),
  `ttl/` (TTL/expiring cache), and `data_structures/` (shared,
  cache-agnostic building blocks — currently a hand-built doubly
  linked list, used by `lru/` for eviction ordering; lives outside
  `lru/` since it has no inherent connection to caching)
- **Go implementation** — `go/`, with `lru/` (LRU cache) and `ttl/`
  (TTL/expiring cache)
- Each implementation is self-contained, idiomatic to its language, and
  tested independently. The goal isn't a 1:1 port line-by-line — it's
  correctly implementing the same *concepts* in each language's natural
  style.

## Caching Strategies Covered

- [ ] LRU cache — MVP, in progress
- [ ] TTL / expiring cache — MVP, in progress
- [ ] LRU + TTL combined — planned, post-MVP
- [ ] LFU (Least Frequently Used) — planned, post-MVP
- [ ] Write-through vs. cache-aside patterns — planned, post-MVP
- [ ] Distributed caching (Redis-backed) — planned, post-MVP

## Status

Early stage, MVP in progress (full detail in DESIGN.md's Roadmap).
The MVP is two cache types, built for real (not a throwaway
translation) directly in Python and Go, loosely inspired by
[MosheWorld/CacheStrategies](https://github.com/MosheWorld/CacheStrategies)'s
two actual implementations:

- **LRU cache** — manual hash map + doubly linked list,
  capacity-based eviction only, no shortcuts (`OrderedDict` /
  `container/list`). Python implementation (`python/lru/`) is
  functionally complete — get/put/has/delete/clear/keys/size, with
  eviction and recency tracked entirely by the doubly linked list
  rather than borrowed from dict ordering — and manually verified
  across eviction, refresh, mid-list updates, boundary capacities, and
  clear/reuse. Unit tests not written yet; that's next. Go
  implementation not started.
- **TTL / expiring cache** — hash map with time-based expiration, no
  capacity eviction. Not started, in either language. (The reference
  repo calls its version of this "client-side caching," but that's a
  browser-storage concept that doesn't apply here — what's reusable is
  the TTL logic.)

Post-MVP: combine LRU + TTL into one cache, LFU, write-through vs.
cache-aside, and Redis-backed distributed caching (not hand-rolled).

## Usage

_(To be filled in once the first implementation has a stable API.)_

## License

MIT

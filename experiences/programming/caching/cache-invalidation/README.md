# Cache Invalidation

Cache invalidation matters when cached state can remain valid from the cache's point of view even after the underlying business data has changed.

The difficult part is often not that a cache exists. The difficult part is recognizing that a successful write to the source of truth does not guarantee every reader will immediately observe the new value.

## What to practice here

Use these scenarios to practice asking:

- Which system is the source of truth for this value?
- Which layers may hold copies of it?
- What event or rule makes a cached value obsolete?
- How long can stale data remain visible?
- Can different users or instances observe different versions at the same time?
- Does a temporary fix such as bypassing or restarting a cache reveal the real failure mode?
- Which correctness guarantees matter more than raw cache hit rate?

## Scenarios

- [Stale product price after an update](scenarios/stale-product-price.md) — a database update succeeds, but some requests continue to serve the old product price from stale cached state.

The goal is to build the recognition pattern: when writes look correct but reads disagree, map every place the value can exist before blaming the source of truth.
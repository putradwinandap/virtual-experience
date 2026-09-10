# Caching

Caching covers failures caused by keeping derived or copied state closer to where it is read.

A cache can improve latency and reduce load, but it also creates another place where application state can live. Once data exists in more than one place, engineers must reason about freshness, invalidation, ownership, failure boundaries, and what users may observe when those copies disagree.

The useful skill is not memorizing cache APIs. It is learning to recognize when apparently correct writes and inconsistent reads may point to stale state outside the primary source of truth.

## Topics

- [Cache Invalidation](cache-invalidation/) — recognizing when cached data outlives the change that made it obsolete and continues to influence application behavior.

The topics listed here are only those currently available in the repository.
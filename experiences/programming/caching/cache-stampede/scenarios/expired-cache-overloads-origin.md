---
title: "The Expired Cache That Overloaded the Origin"
domain: "programming"
area: "caching"
topic: "cache-stampede"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "cache-stampede"
  - "thundering-herd"
  - "request-coalescing"
---

# The Expired Cache That Overloaded the Origin

## Context

Many requests read the same expensive product summary from a shared cache with a fixed expiry.

## Situation

At expiry, a traffic burst causes many requests to miss simultaneously and query the database.

## Symptoms

- Origin traffic spikes at predictable expiry times.
- Cache hit rate drops sharply for a short window.
- Requests time out even though the cached object is small.

## Your Task

Reduce the synchronized refill without serving unsafe data indefinitely.

## Investigation

Compare expiry timestamps, miss rates, origin load, and key popularity. Check whether all callers refill independently.

## Root Cause

The cache used synchronized expiration and had no coordination around regeneration.

## Possible Approaches

Add request coalescing or a per-key lock, jitter expiry times, refresh asynchronously, and use short stale-while-revalidate windows where acceptable.

## Trade-offs

Locks add coordination and failure handling. Jitter spreads load but does not remove it. Stale data improves availability only when freshness limits are explicit.

## What Could Go Wrong

Do not create a global lock that serializes unrelated keys, and do not let stale data bypass business freshness requirements.

## Takeaway

Cache expiry is a traffic event. Design the refill path as carefully as the hit path.

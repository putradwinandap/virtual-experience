---
title: "Stale Product Price After an Update"
domain: "programming"
area: "caching"
topic: "cache-invalidation"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "caching"
  - "cache-invalidation"
  - "stale-data"
---

# Stale Product Price After an Update

## Context

An e-commerce application serves product details through several application instances. Product data is stored in a database, while frequently requested product records are cached to reduce database load and keep product pages fast.

An internal admin tool lets the merchandising team update product prices. Under normal conditions, customers should see a new price shortly after an approved update.

## Situation

A product's price is changed from Rp100.000 to Rp80.000 through the admin tool.

The admin receives a successful response and confirms that the database contains Rp80.000. Soon afterward, customer support reports that some customers still see Rp100.000.

An engineer refreshes the product page and sees Rp80.000, so the problem initially appears difficult to reproduce. Another engineer opens the same product from a different session and still sees Rp100.000.

## Symptoms

- The admin update completed successfully.
- A direct database query returns Rp80.000.
- Some product-page requests return Rp80.000 while others return Rp100.000.
- The stale response is otherwise valid: there is no application error or failed database query.
- Repeating the same request does not always reproduce the same value.
- Bypassing the caching layer returns Rp80.000 consistently.
- Restarting one application instance appears to fix requests handled by that instance, but reports continue elsewhere.

## Your Task

Production is still serving inconsistent prices. Before changing the database again or disabling caching globally, decide what evidence you need.

- Which component is authoritative for the product price?
- What systems can return a product value without reading the database?
- Why might two healthy requests observe different prices?
- What does the cache bypass tell you?
- Why would restarting only one instance improve only some requests?
- What should happen to cached product data when the admin changes a price?

## Investigation

Start by separating the write path from the read path.

The write trace shows:

```text
Admin -> application -> UPDATE product price -> database commits Rp80.000
Application -> admin: update successful
```

Nothing in that path indicates a failed transaction.

Next, compare requests that return different prices. Both application instances are healthy, but their cache state differs:

```text
Instance A cache: product:42 -> Rp80.000
Instance B cache: product:42 -> Rp100.000
Database:         product:42 -> Rp80.000
```

The read path checks the cache before the database. A cache hit therefore returns the stored value without consulting the authoritative row.

The admin update changes the database, but the write path does not reliably invalidate or refresh every cached copy of that product. A cache entry can remain internally usable until its expiration time even though the business data it represents has already changed.

Bypassing the cache consistently exposes the database value. Restarting one instance removes that instance's local cached copy, so its next request reloads Rp80.000. Neither action explains a database failure; both narrow the problem to stale state on the read path.

## Root Cause

The application has multiple copies of product state but no freshness guarantee that matches the price-update workflow.

The database update succeeds, yet at least one cached copy of `product:42` survives the change. Requests that hit that copy continue to receive Rp100.000 until the entry expires, is evicted, or is explicitly replaced.

The bug is therefore not that the cache returned corrupted data. It returned exactly what it had been told was cacheable. The system failed to make that cached value obsolete when the authoritative data changed.

## Possible Approaches

### Explicit invalidation after a successful write

After the database update commits, remove the affected product entry from the relevant cache so the next read repopulates it from the source of truth.

This can keep stale windows short, but the design must handle failures between the database commit and the invalidation action. Distributed or per-instance caches also require invalidation to reach every relevant copy.

### Refresh or update the cached value

Instead of deleting the entry, write the new value into the cache after the authoritative update succeeds.

This may avoid a cache miss immediately after the write, but it still creates coordination questions when several cache layers or instances exist. A delayed older update must not overwrite newer state.

### Time-based expiration

Use a TTL so cached values eventually disappear even when explicit invalidation fails.

TTL provides a bound on staleness only if that bound is acceptable for the business data. A ten-minute stale product description may be tolerable; a ten-minute stale price may create customer, operational, or compliance problems.

### Read-through or cache-aside with an invalidation strategy

Keep the common cache-aside read path, but make cache lifecycle part of the write design rather than an unrelated optimization.

The exact mechanism can vary, but the important property is that the system has an intentional answer for how a committed change becomes visible to readers using cached copies.

### Temporarily bypass caching for affected reads

During an incident, bypassing cache for the affected product or critical data can restore correctness while engineers repair invalidation.

This is an operational mitigation, not necessarily the long-term design. Removing caching globally can shift load abruptly to the database and create a second incident.

## Trade-offs

Explicit invalidation can provide fresher reads than a long TTL, but it couples the write workflow to cache lifecycle and introduces a new failure boundary after the database commit.

Updating the cache immediately can reduce misses, but coordinating multiple caches and concurrent writers is harder than simply replacing one local value. Ordering matters when updates can arrive asynchronously.

Short TTLs reduce the maximum stale window and limit damage from missed invalidations, but they also reduce cache effectiveness and increase source-of-truth load. Long TTLs improve hit rates while making stale data survive longer when invalidation is missing or broken.

Bypassing cache favors correctness and incident recovery, but doing it broadly can increase latency and database traffic. The right choice depends on how stale the data is allowed to be and how much load the authoritative system can safely absorb.

## What Could Go Wrong

- The application invalidates only the cache on the instance that processed the admin request while other instances keep stale copies.
- Cache invalidation runs before the database transaction commits, and another request repopulates the old value during the gap.
- The database commit succeeds but an invalidation message fails, leaving stale data with no retry or reconciliation path.
- A long TTL is treated as a complete invalidation strategy even though the business cannot tolerate that much stale pricing.
- Engineers clear the entire cache during an incident and cause a sudden database load spike.
- A delayed cache update carrying Rp100.000 arrives after the newer Rp80.000 update and makes the cache stale again.
- Monitoring checks only database correctness and never compares what customers actually receive.

## Takeaway

When the source of truth is correct but readers disagree, map every copy of the data before assuming the write failed.

A cache is part of application state, not merely a performance switch. For data that changes, always ask what makes each cached copy obsolete, how long stale values may survive, and what happens when the authoritative write succeeds but cache coordination does not.
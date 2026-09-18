---
title: "The Transfer That Waited Forever"
domain: "programming"
area: "concurrency"
topic: "deadlock"
difficulty: "advanced"
provenance:
  type: "illustrative"
concepts:
  - "deadlock"
  - "locking"
  - "lock-ordering"
---

# The Transfer That Waited Forever

## Context

Two workers transfer balances between accounts. Each transaction locks one account before acquiring a lock on the other.

## Situation

Transfers between accounts A and B intermittently stall. Restarting workers clears the problem, but it returns under load.

## Symptoms

- Database lock waits grow while CPU remains normal.
- One transaction holds A and waits for B; another holds B and waits for A.
- Requests time out without a clear application exception.

## Your Task

How would confirm a cycle, and what change prevents it without removing correctness protections?

## Investigation

Inspect active transactions and lock-wait graphs. Compare the order in which each code path acquires locks, including less obvious paths such as reversal or refund operations.

## Root Cause

Concurrent transactions acquired the same resources in opposite orders, creating a wait cycle.

## Possible Approaches

Enforce a global lock order, use a single atomic database operation where possible, and retry transactions aborted by deadlock detection.

## Trade-offs

Consistent ordering reduces cycles but constrains implementation. Retries improve resilience but require idempotent work and bounded backoff.

## What Could Go Wrong

Do not hide lock timeouts with unlimited retries. A new code path can reintroduce the cycle unless lock ordering is documented and tested.

## Takeaway

When work waits forever, inspect resource-acquisition order—not only individual query duration.

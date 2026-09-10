---
title: "Oversold Inventory During a Flash Sale"
domain: "programming"
area: "concurrency"
topic: "race-condition"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "race-condition"
  - "database-transaction"
  - "atomic-update"
  - "locking"
---

# Oversold Inventory During a Flash Sale

## Context

An online store is running a flash sale. One product has exactly **1 unit left**.

The purchase endpoint roughly does this:

1. Read the current stock.
2. Reject the purchase if stock is `0`.
3. Create the order.
4. Save `stock - 1`.

Under normal traffic, the flow appears to work.

## Situation

Two customers press **Buy** at almost the same moment. Both requests return success and both customers receive an order confirmation.

A few seconds later, operations notices that two orders were accepted for the final unit.

The inventory row itself shows `0`, not `-1`, so the obvious "negative stock" alert never fired.

## Symptoms

- Two valid-looking orders exist for one available unit.
- Both requests passed the stock check.
- The final stock value looks plausible.
- Replaying either request by itself does not reproduce the problem.
- The issue becomes easier to trigger as traffic increases.

## Your task

Before reading further, investigate the flow as if this happened in production.

- Which state is shared between the two requests?
- Which assumptions are made between reading stock and writing the new value?
- Can both requests be individually correct while their combined result is wrong?
- What invariant should the system protect?
- Where would you collect evidence to prove the ordering of events?

## Investigation

Suppose the requests interleave like this:

```text
Request A: read stock -> 1
Request B: read stock -> 1
Request A: stock > 0, create order A
Request B: stock > 0, create order B
Request A: write stock -> 0
Request B: write stock -> 0
```

Nothing in either request looks invalid in isolation. Each request observed one unit and calculated a new value of zero.

The important observation is that the business operation is larger than either the read or the write. The decision "stock is available, therefore this order may claim it" must remain valid until the claim is committed.

## Root cause

This is a **check-then-act race condition**.

The application treats reading stock, checking availability, accepting the order, and decrementing stock as though they were one indivisible operation. They are not. Two requests can observe the same stale state before either one protects or consumes the unit.

The invariant is not merely `stock >= 0`. A stronger business invariant is: **the system must not successfully allocate more units than are available**.

That distinction explains why a final stock value of `0` does not prove correctness.

## Possible approaches

### Conditional atomic update

Let the database perform the check and decrement as one statement, for example conceptually:

```sql
UPDATE products
SET stock = stock - 1
WHERE id = ? AND stock > 0;
```

Only create or finalize the order if exactly one row was updated.

This can be simple and efficient for a narrow inventory claim, but the surrounding order workflow still needs a transaction or compensation strategy so inventory and order state cannot drift apart.

### Pessimistic row locking

Start a transaction, lock the inventory row, check stock, create the order, decrement stock, and commit.

This makes the critical section explicit and is often straightforward to reason about. Under heavy contention, however, requests may wait on the lock, increasing latency and creating timeout or deadlock considerations.

### Optimistic concurrency control

Store a version or expected value and update only if it has not changed since it was read. A conflicting request fails its write and must retry or report that inventory is gone.

This avoids holding a lock while application work happens, but it moves complexity into conflict detection, retry policy, and user-visible behavior when contention is high.

## Trade-offs

There is no universal "use locks" answer. The choice depends on contention, database capabilities, transaction boundaries, latency requirements, and how much retry complexity the application can safely own.

A flash-sale product may have extreme contention, making a design that is comfortable under ordinary traffic behave poorly. A correct inventory claim also does not automatically make payment, order creation, and downstream events atomic; those boundaries need their own failure strategy.

## What could go wrong

- A transaction protects inventory but holds the lock while calling a slow payment provider.
- Automatic retries repeat side effects that are not idempotent.
- Inventory is decremented successfully but order creation fails afterward.
- The application checks affected rows incorrectly and still reports success.
- A cache is treated as the authoritative stock value while the database enforces a different state.
- Monitoring watches only for negative stock and misses excess successful allocations.

## Takeaway

When correctness depends on "read a value, make a decision, then write," ask what can happen between those steps.

The key mental model is to identify the **business invariant** and make the operation that protects it atomic at the appropriate boundary. A plausible final value does not guarantee that concurrent decisions were valid.
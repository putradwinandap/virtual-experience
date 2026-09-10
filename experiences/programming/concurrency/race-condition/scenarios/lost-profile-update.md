---
title: "Lost Profile Update From Concurrent Edits"
domain: "programming"
area: "concurrency"
topic: "race-condition"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "race-condition"
  - "lost-update"
  - "optimistic-concurrency"
  - "database-transaction"
---

# Lost Profile Update From Concurrent Edits

## Context

A customer profile stores several fields in one database row: name, phone number, shipping address, and notification preference.

The application has two independent interfaces:

- the customer can edit their own profile;
- a support agent can correct profile details from an internal dashboard.

Both interfaces load the full profile object and later submit the full object back when saving.

## Situation

A customer opens the profile page and changes their shipping address. At nearly the same time, a support agent opens the same profile and fixes the customer's phone number.

Both interfaces report **Saved successfully**.

Later, the customer discovers that the phone number has reverted to its old value. The audit trail shows two successful updates, and neither request produced an error.

## Symptoms

- Two users successfully changed different fields.
- No validation or database error occurred.
- One valid change disappeared.
- The last saved profile looks internally valid.
- The bug is timing-sensitive and difficult to reproduce sequentially.

## Your task

Investigate before assuming that one user entered the wrong value.

- What did each editor originally read?
- What exactly does each save request send?
- Does a save express "change this field" or "replace this profile with my copy"?
- How could both requests succeed while one user's work is lost?
- What evidence would distinguish a stale write from a frontend display bug?

## Investigation

Imagine both editors initially read this state:

```text
phone   = 0812-OLD
address = Old Street
```

Their actions then overlap:

```text
Customer loads: phone=0812-OLD, address=Old Street
Agent loads:    phone=0812-OLD, address=Old Street

Customer changes address locally -> New Street
Agent changes phone locally       -> 0812-NEW

Agent saves full profile:
phone=0812-NEW, address=Old Street

Customer saves stale full profile afterward:
phone=0812-OLD, address=New Street
```

The customer's save contains a phone number they never intended to edit. It is present only because their browser is carrying an older snapshot of the row.

## Root cause

This is a **lost update** caused by concurrent writes based on stale snapshots.

The system allows each editor to replace shared state without checking whether that state changed after it was read. The later whole-record write silently overwrites a valid earlier change.

Unlike the inventory scenario, there is no scarce unit to allocate and no obvious invalid final value. The failure is that a legitimate update disappears.

## Possible approaches

### Update only fields the user changed

If the customer's action means "change address," send and persist only the address rather than an entire stale profile snapshot.

This reduces accidental overwrites between independent fields and can be a good API design principle. It does not solve conflicts when two actors genuinely edit the same field or when multiple fields must satisfy a shared invariant.

### Optimistic concurrency control

Attach a version number or update token to the profile. A save succeeds only if the stored version still matches the version originally read.

When another writer has already changed the row, reject the stale save and let the caller reload, merge, or explicitly retry.

This makes conflicts visible without holding database locks across the time a human spends editing, but the product must define a usable conflict-resolution experience.

### Serialize writes where appropriate

For short machine-driven critical sections, locking or stronger transaction isolation can prevent overlapping updates.

Holding a database lock while a human edits a form is generally not practical, so the boundary and duration of coordination matter as much as the mechanism itself.

## Trade-offs

Partial updates are simple when fields are independent, but can hide domain rules that span multiple fields. Optimistic concurrency detects stale state cleanly, but callers must handle conflicts instead of assuming every save succeeds. Stronger serialization can simplify reasoning for short operations while reducing concurrency and increasing contention.

The right choice depends on what an update means in the domain, how often conflicts occur, whether automatic merging is safe, and how expensive it is to ask a human to resolve a conflict.

## What could go wrong

- A retry blindly resubmits the same stale full object and overwrites the newer state again.
- A frontend receives a conflict response but hides it behind a generic "save failed" message.
- Partial updates are used even though two fields must change together to preserve an invariant.
- A version check is performed, but the version increment and write are not atomic.
- Different services update the same record but do not participate in the same concurrency-control convention.
- An audit log records both requests as successful without preserving enough before/after state to diagnose the loss.

## Takeaway

A successful write is not proof that no other valid work was destroyed.

When multiple actors can edit shared state, ask whether each write represents an intentional change or a replacement based on an old snapshot. Make stale-state conflicts impossible, detectable, or explicitly resolvable rather than silently accepting last-writer-wins behavior.
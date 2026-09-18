---
title: "The Edit That Erased a Newer Edit"
domain: "programming"
area: "concurrency"
topic: "lost-update"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["lost-update", "optimistic-locking", "versioning"]
---

# The Edit That Erased a Newer Edit

## Context

Two operators edit the same customer profile using a read-edit-write form.

## Situation

The second save succeeds and silently removes a field changed by the first operator.

## Symptoms

- Both requests return success.
- The final record contains only one user's view of the data.

## Your Task

Preserve concurrent changes or make the conflict visible.

## Investigation

Compare read versions and update timestamps. Check whether the update predicate includes the version observed by the editor.

## Root Cause

A stale full-record write overwrote a newer write because no concurrency check existed.

## Possible Approaches

Use optimistic version checks, field-level patches, or explicit conflict resolution.

## Trade-offs

Conflict errors require user handling; patches reduce overwrites but complicate semantics.

## What Could Go Wrong

Do not fix this by always accepting the latest request; arrival order is not intent order.

## Takeaway

Successful writes can still lose work when the writer did not read the latest version.

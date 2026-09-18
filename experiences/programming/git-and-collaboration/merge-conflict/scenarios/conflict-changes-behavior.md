---
title: "The Conflict That Compiled but Changed Behavior"
domain: "programming"
area: "git-and-collaboration"
topic: "merge-conflict"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["merge-conflict", "code-review", "regression"]
---

# The Conflict That Compiled but Changed Behavior

## Context

Two branches modify validation and error handling in the same function.

## Situation

The merge tool reports a conflict. A resolution compiles and unit tests pass, but a client later receives an unexpected fallback response.

## Symptoms

- The conflict resolution removed one branch's condition.
- Existing tests cover each branch separately, not the combined behavior.

## Your Task

Reconstruct the intended behavior before choosing lines mechanically.

## Investigation

Read both parent versions, inspect the issue context, and add a test for the interaction. Ask whether the two changes should be composed, sequenced, or redesigned.

## Root Cause

A textual conflict was resolved without resolving the underlying behavioral conflict.

## Possible Approaches

Keep the resolution small, add interaction tests, and request review from both change owners.

## Trade-offs

Extra review delays the merge but lowers regression risk; a quick resolution preserves velocity only when intent is already clear.

## What Could Go Wrong

Do not assume “ours” or “theirs” represents the correct business behavior.

## Takeaway

Merge conflicts are design questions disguised as text-editing problems.

---
title: "The Fix That Was Reverted Too Quickly"
domain: "programming"
area: "git-and-collaboration"
topic: "reverted-production-fix"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["reverted-production-fix", "rollback", "observability"]
---

# The Fix That Was Reverted Too Quickly

## Context

An emergency change reduces errors but introduces a slower path for a smaller group of users.

## Situation

The team reverts immediately, and the original outage returns.

## Symptoms

- The first failure mode returns after rollback.
- The fix and its side effect were not measured separately.

## Your Task

Choose between rollback, mitigation, or a narrower follow-up change using evidence.

## Investigation

Compare error, latency, and affected-cohort metrics before and after the fix. Preserve the incident timeline and identify the safe part of the change.

## Root Cause

Rollback was treated as universally safe even though it restored a known failure.

## Possible Approaches

Keep the mitigation with a feature flag, narrow its scope, or prepare a corrected replacement.

## Trade-offs

Temporary complexity may be safer than oscillating between two known-bad states.

## What Could Go Wrong

Do not let urgency eliminate measurement or a clear owner for the temporary state.

## Takeaway

A rollback is a change with consequences, not automatically the absence of change.

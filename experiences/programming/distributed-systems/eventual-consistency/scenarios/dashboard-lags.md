---
title: "The Dashboard That Lagged Behind Reality"
domain: "programming"
area: "distributed-systems"
topic: "eventual-consistency"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["eventual-consistency", "replication", "read-after-write"]
---

# The Dashboard That Lagged Behind Reality

## Context

An order is written to a primary store and replicated to a read model used by an operations dashboard.

## Situation

An operator confirms an order, refreshes the dashboard, and sees the old status for several seconds.

## Symptoms

- The write response says the new status was accepted.
- Reads through the dashboard show the previous value.
- The value converges after replication catches up.

## Your Task

Decide whether the user needs a strongly consistent read or whether the interface should communicate propagation delay.

## Investigation

Compare write time, replication lag, read target, and request identity. Verify whether the dashboard reads a replica or derived projection.

## Root Cause

The system guarantees eventual convergence, not read-after-write consistency across every read path.

## Possible Approaches

Read the primary for the initiating user, carry a version token, or show an explicit pending/synchronizing state.

## Trade-offs

Strong reads cost latency and load. Version-aware reads add protocol complexity. Honest UI states preserve the consistency model.

## What Could Go Wrong

Do not “fix” stale reads by polling aggressively; that can amplify load without guaranteeing freshness.

## Takeaway

When a write succeeds but a read is old, identify the consistency guarantee before treating it as data loss.

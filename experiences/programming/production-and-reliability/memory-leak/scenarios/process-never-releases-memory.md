---
title: "The Process That Never Released Memory"
domain: "programming"
area: "production-and-reliability"
topic: "memory-leak"
difficulty: "advanced"
provenance:
  type: "illustrative"
concepts: ["memory-leak", "heap-growth", "profiling"]
---

# The Process That Never Released Memory

## Context

A long-running worker stores request metadata in an in-memory map keyed by job ID.

## Situation

Memory usage rises steadily even after traffic returns to normal.

## Symptoms

- Heap growth follows processed jobs, not concurrent jobs.
- Garbage collection becomes frequent and restarts increase.

## Your Task

Prove whether retained references, rather than a traffic spike, explain the growth.

## Investigation

Compare heap snapshots over time, inspect collection sizes, and identify objects retaining completed jobs.

## Root Cause

Completed entries had no eviction or lifecycle cleanup.

## Possible Approaches

Remove entries on completion, use bounded caches, and alert on sustained heap slope.

## Trade-offs

Cleanup must handle crashes and retries; bounds may discard data that callers still expect.

## What Could Go Wrong

Do not raise the memory limit as the only fix; it delays the failure.

## Takeaway

Memory growth correlated with lifetime, not current load, is a retention investigation.

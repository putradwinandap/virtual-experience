---
title: "The Lookup That Scanned Every Row"
domain: "programming"
area: "databases"
topic: "missing-index"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["missing-index", "query-plan", "selectivity"]
---

# The Lookup That Scanned Every Row

## Context

Requests find active jobs by tenant and scheduled time.

## Situation

As the jobs table grows, a previously fast poller consumes increasing database CPU.

## Symptoms

- Explain plans show a sequential scan.
- Reads and latency grow with total table size, not matching jobs.

## Your Task

Choose an index based on actual predicates and ordering.

## Investigation

Measure selectivity, query frequency, returned rows, and write cost. Inspect the real plan rather than assuming an index is used.

## Root Cause

The frequent filter had no suitable index.

## Possible Approaches

Add a composite index matching tenant, status, and schedule; verify with production-shaped data.

## Trade-offs

Indexes speed reads but consume storage and slow writes.

## What Could Go Wrong

An index with the wrong column order may not help; adding many indexes can harm writes.

## Takeaway

Performance tuning starts with workload evidence and query plans, not index folklore.

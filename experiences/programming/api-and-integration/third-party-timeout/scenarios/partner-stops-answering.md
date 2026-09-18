---
title: "The Partner That Stopped Answering"
domain: "programming"
area: "api-and-integration"
topic: "third-party-timeout"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["third-party-timeout", "circuit-breaker", "backpressure"]
---

# The Partner That Stopped Answering

## Context

Checkout synchronously calls a shipping provider.

## Situation

The provider becomes slow and application threads remain occupied waiting for responses.

## Symptoms

- Checkout latency approaches the client timeout.
- Connection pools fill and unrelated endpoints degrade.
- Retrying increases provider traffic.

## Your Task

Protect the application while preserving orders that can be completed later.

## Investigation

Separate connect, read, and total timeouts. Measure pool occupancy, dependency latency, and request volume.

## Root Cause

The dependency's latency was allowed to consume local resources without isolation or bounded waiting.

## Possible Approaches

Use strict timeouts, circuit breaking, bulkheads, and asynchronous completion where the product permits it.

## Trade-offs

Isolation preserves the rest of the system but may return degraded results. Async work improves resilience but changes user feedback.

## What Could Go Wrong

Do not use infinite timeouts or retries that turn a dependency outage into self-inflicted saturation.

## Takeaway

Every synchronous dependency call needs a failure budget and a plan for unavailable responses.

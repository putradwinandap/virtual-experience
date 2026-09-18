---
title: "The Healthy Service That Took Down Its Neighbor"
domain: "programming"
area: "production-and-reliability"
topic: "cascading-failure"
difficulty: "advanced"
provenance:
  type: "illustrative"
concepts: ["cascading-failure", "backpressure", "bulkhead"]
---

# The Healthy Service That Took Down Its Neighbor

## Context

An API depends on a slow reporting service and creates a request for each incoming user request.

## Situation

Reporting slows down; API workers queue requests until the API also fails.

## Symptoms

- The dependency has high latency, then the caller exhausts threads and connections.
- Services that do not directly call reporting begin timing out.

## Your Task

Stop propagation while preserving core traffic.

## Investigation

Map dependency calls, queue depth, pool saturation, and timeout/retry behavior across services.

## Root Cause

Unbounded synchronous waiting allowed one degraded component to consume shared capacity.

## Possible Approaches

Bulkheads, bounded queues, circuit breakers, load shedding, and asynchronous work.

## Trade-offs

Some requests will be rejected or degraded, but the system keeps critical paths available.

## What Could Go Wrong

Retries without budgets can multiply the load and accelerate the cascade.

## Takeaway

Reliability includes limiting how much one dependency can consume.

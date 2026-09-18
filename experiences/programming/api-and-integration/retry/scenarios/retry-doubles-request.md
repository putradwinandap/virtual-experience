---
title: "The Retry That Doubled the Request"
domain: "programming"
area: "api-and-integration"
topic: "retry"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "retry"
  - "timeout"
  - "idempotency"
---

# The Retry That Doubled the Request

## Context

An order service calls a partner API with a five-second client timeout. The partner may continue processing after the client stops waiting.

## Situation

The client retries timed-out requests and the partner reports duplicate orders.

## Symptoms

- Client logs show a timeout followed by success on retry.
- Partner logs show two accepted requests.
- Duplicate rate increases during latency spikes.

## Your Task

Decide when retrying is safe and how to distinguish an unknown outcome from a confirmed failure.

## Investigation

Classify errors as connection failure, timeout after transmission, explicit rejection, or rate limiting. Check whether the partner supports idempotency keys and inspect request IDs across both systems.

## Root Cause

The client treated every timeout as proof that the partner did nothing, although the request could have been accepted.

## Possible Approaches

Use idempotency keys, retry only transient failures with bounded exponential backoff, and query operation status when the outcome is unknown.

## Trade-offs

Retries improve availability but add load and duplicate risk. Status queries reduce ambiguity but require partner support and state tracking.

## What Could Go Wrong

Do not retry non-idempotent operations merely because the connection closed.

## Takeaway

A timeout describes what the caller knows, not what the dependency did.

---
title: "The Worker Processed One Message Twice"
domain: "programming"
area: "distributed-systems"
topic: "duplicate-message-processing"
difficulty: "advanced"
provenance:
  type: "illustrative"
concepts: ["duplicate-message-processing", "at-least-once-delivery", "idempotency"]
---

# The Worker Processed One Message Twice

## Context

A queue worker charges an account and then acknowledges a message.

## Situation

The worker crashes after charging but before acknowledgment. The broker redelivers the message.

## Symptoms

- The same message ID appears in two worker attempts.
- The account has two charges.

## Your Task

Prevent duplicate business effects while retaining redelivery for genuine failures.

## Investigation

Compare message delivery attempts, charge provider request IDs, and acknowledgment timing.

## Root Cause

The system used at-least-once delivery with a non-idempotent side effect.

## Possible Approaches

Use a durable idempotency key at the provider, record processed messages transactionally, or design the state transition to be repeat-safe.

## Trade-offs

Durable deduplication adds storage and cleanup; provider idempotency depends on retention and contract guarantees.

## What Could Go Wrong

Do not acknowledge before the effect is durable, or failures will lose work instead of duplicating it.

## Takeaway

Assume a distributed worker can see the same message again after any crash point.

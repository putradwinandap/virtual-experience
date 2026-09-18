---
title: "The Webhook Delivered Twice"
domain: "programming"
area: "api-and-integration"
topic: "webhook-duplication"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["webhook-duplication", "idempotency", "deduplication"]
---

# The Webhook Delivered Twice

## Context

An external provider sends payment-status webhooks and retries until it receives a successful response.

## Situation

The receiver times out after updating an order, so the provider sends the same event again.

## Symptoms

- Duplicate notifications or fulfillment jobs appear.
- The same event ID occurs more than once.

## Your Task

Make processing safe when delivery is at-least-once.

## Investigation

Record provider event IDs before applying side effects and inspect whether processing and acknowledgment are ordered safely.

## Root Cause

The receiver treated delivery as exactly-once and had no durable deduplication or idempotent handler.

## Possible Approaches

Store event IDs with a uniqueness constraint, make state transitions idempotent, and acknowledge only after durable acceptance.

## Trade-offs

Deduplication storage requires retention policy; idempotent transitions need careful business rules.

## What Could Go Wrong

Do not deduplicate only in process memory; restarts erase that protection.

## Takeaway

Webhooks are messages, not callbacks with exactly-once delivery guarantees.

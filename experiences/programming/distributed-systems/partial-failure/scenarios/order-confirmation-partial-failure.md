---
title: "A Partial Failure During Order Confirmation"
domain: "programming"
area: "distributed-systems"
topic: "partial-failure"
difficulty: "advanced"
provenance:
  type: "illustrative"
concepts:
  - "partial-failure"
  - "distributed-transaction"
  - "compensation"
---

# A Partial Failure During Order Confirmation

## Context

An order service reserves inventory, requests payment authorization, and marks an order confirmed through separate services. No single database transaction covers all three operations.

## Situation

Customers report that checkout sometimes shows an error, but inventory is no longer available and a payment authorization appears at the provider.

## Symptoms

- The order API returns a timeout or 5xx response.
- Inventory shows a reservation without a confirmed order.
- The payment provider has an authorization for the same checkout attempt.
- Retrying can create a second authorization unless the request is identified consistently.

## Your Task

What state transitions would you inspect first? How would you recover affected orders without assuming that retrying the whole workflow is safe?

## Investigation

Build a timeline using an order attempt ID, reservation ID, and payment idempotency key. Compare service logs, queue events, and provider status. Determine which steps completed, which response was lost, and whether each operation is safe to repeat or requires a compensating action.

## Root Cause

The workflow crossed multiple failure boundaries. A timeout after payment authorization did not mean authorization failed; it only meant the caller lacked a confirmed response. The system had no durable workflow state or reconciliation path to resolve the intermediate state.

## Possible Approaches

- Persist a state machine and resume from the last confirmed step.
- Use idempotency keys for repeatable commands.
- Add compensation, such as releasing a reservation or voiding an authorization.
- Run reconciliation for states that remain unresolved beyond a threshold.

## Trade-offs

Workflow state and reconciliation add storage, operational jobs, and more states to test. Compensation is not always immediate or perfectly reversible. A synchronous workflow is simpler to explain but still cannot remove distributed failure boundaries.

## What Could Go Wrong

Do not equate an API timeout with business failure. Do not blindly replay every step, and do not release inventory before checking whether payment and order creation completed elsewhere.

## Takeaway

When a distributed workflow fails, ask which transitions committed—not whether the whole request succeeded or failed. Recovery should continue from known state and reconcile uncertainty.

## Related Concepts

- [Idempotency](../../api-and-integration/idempotency/)

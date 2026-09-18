---
title: "The Email Sent Before the Transaction Committed"
domain: "programming"
area: "databases"
topic: "transaction-boundary-mistake"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["transaction-boundary-mistake", "outbox-pattern", "commit"]
---

# The Email Sent Before the Transaction Committed

## Context

An account update writes the database and sends a confirmation email inside one request handler.

## Situation

The email is delivered, then the database transaction rolls back.

## Symptoms

- Users receive confirmation for a change that is absent.
- Retry may send another email.

## Your Task

Align external side effects with durable commit.

## Investigation

Trace the transaction lifecycle and compare email timestamps with commit/rollback events.

## Root Cause

The external side effect ran before the database made the state durable.

## Possible Approaches

Write an outbox record in the transaction and publish it after commit; make delivery idempotent.

## Trade-offs

The outbox adds a worker and eventual delivery, but makes recovery observable and reliable.

## What Could Go Wrong

Do not assume a database rollback can undo an email or HTTP request.

## Takeaway

Transactions do not include external systems unless you explicitly build a coordination mechanism.

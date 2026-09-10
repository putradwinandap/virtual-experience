---
title: "Duplicate Order After a Client Retry"
domain: "programming"
area: "api-and-integration"
topic: "idempotency"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "idempotency"
  - "retry"
  - "resource-creation"
  - "request-identity"
---

# Duplicate Order After a Client Retry

## Context

A shopping application exposes an API endpoint that creates an order from the user's current checkout data.

When the backend accepts the request, it inserts a new order, reserves inventory, and returns the newly generated order ID to the client.

The mobile client has a retry mechanism for requests that fail because of unstable connectivity.

## Situation

A customer submits an order while their connection is switching between mobile data and Wi-Fi.

The loading indicator eventually reports a network error, so the client retries the submission. The second request succeeds and displays an order confirmation.

Later, the customer notices two different order numbers for the same checkout. Both orders are valid in the backend and both have reserved inventory.

## Symptoms

- Two order records have different generated IDs but nearly identical customer, items, totals, and timestamps.
- Both orders passed normal validation.
- Inventory was reserved for both orders.
- The first client request has no received success response.
- Server logs show that both create requests reached the application.
- Sending either request alone produces a perfectly valid order.

## Your task

Before assuming the client should simply stop retrying, reason about the boundary between one user intention and multiple network attempts.

- Did the first request actually fail?
- What evidence connects the two requests to the same user action?
- How does the server currently distinguish a retry from a second intentional purchase?
- Where should the identity of the logical order creation come from?
- What downstream effects have already happened by the time a duplicate is noticed?

## Investigation

The server trace shows this sequence:

```text
Client attempt A -> server creates order #18421
Server sends response for #18421 -> connection drops
Client receives no response
Client retry B -> server creates order #18422
Server sends response for #18422 -> client receives it
```

From the client's perspective, attempt A did not produce a known result. From the server's perspective, it completed normally.

The endpoint assigns a new order ID whenever a request reaches the creation handler. The retry contains the same business data, but the API has no stable identifier that says, "this is another transport attempt for the same checkout submission."

Comparing payloads after the fact is not a reliable identity mechanism. Two legitimate orders can contain the same products and total, while one logical order can also change in ways that make naive payload comparison unreliable.

## Root cause

The API equates **HTTP request identity** with **business operation identity**.

A transient communication failure caused one logical user action to produce multiple transport attempts. Because every attempt independently created a new resource, both requests produced valid but unintended orders.

The system lacks an idempotency boundary for order creation: a way to recognize repeated execution of the same logical intent and return or continue the existing result rather than creating another order.

## Possible approaches

### Client-generated operation key

Create a stable identifier when the user begins the order submission and send the same identifier with every retry of that submission.

The server can persist the identifier with the resulting order and enforce uniqueness so concurrent or delayed retries cannot create a second order for the same logical operation.

A genuinely new purchase must receive a new identifier even when its cart contents happen to be identical.

### Server-side idempotency record

Store the operation key separately with request state and the eventual response/resource reference. A retry can inspect that record and either return the completed result or report that the operation is still in progress.

This can support richer recovery behavior but introduces lifecycle, storage, concurrency, and retention decisions.

### Atomic uniqueness enforcement

Back the logical operation identity with a database uniqueness constraint or another authoritative atomic mechanism rather than relying only on an application-level "check whether this key exists" query.

Without atomic enforcement, two simultaneous retries can race and both pass the check before either writes the key.

## Trade-offs

A stable client-generated key clearly connects retries to one user action, but the client must manage its lifecycle correctly. Reusing a key for a later intentional purchase can suppress valid work; regenerating it on every retry removes the guarantee.

Server-side operation records make recovery explicit and can preserve the original response, but they require decisions about expiration, failed operations, payload mismatches, and concurrent requests using the same key.

Database uniqueness is a strong final guard for one logical identifier, but it does not by itself define what the API should return to a duplicate request or undo downstream side effects that occurred before the uniqueness boundary was enforced.

## What could go wrong

- The retry library automatically generates a fresh operation key for every HTTP attempt.
- A key is derived only from cart contents and accidentally treats two intentional identical purchases as one.
- The server checks for an existing key and then inserts without atomic uniqueness, creating another race condition.
- Order creation is deduplicated but inventory reservation or event publication happens outside the protected workflow and is repeated.
- The original operation is still processing when a retry arrives and both workers continue independently.
- Idempotency records are deleted too quickly, allowing a delayed retry to create a new order.
- The API silently accepts the same key with materially different request data.

## Takeaway

Retries are transport behavior; user intent is a business concept. They are not automatically one-to-one.

Whenever a resource-creation operation can be retried, ask how the server recognizes multiple attempts as the **same logical action**. Give that action a stable identity and enforce it at an authoritative boundary, while still allowing genuinely new actions to remain distinct.
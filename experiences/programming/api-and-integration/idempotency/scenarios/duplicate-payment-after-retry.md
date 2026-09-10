---
title: "Duplicate Payment After an Ambiguous Timeout"
domain: "programming"
area: "api-and-integration"
topic: "idempotency"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "idempotency"
  - "retry"
  - "partial-failure"
  - "reconciliation"
---

# Duplicate Payment After an Ambiguous Timeout

## Context

An e-commerce application accepts card payments through an external payment provider.

When checkout reaches the payment step, the backend sends a charge request to the provider. If the provider responds successfully, the application records the payment as paid and continues the order workflow.

Most payments complete in a few hundred milliseconds.

## Situation

During a period of elevated network latency, a customer submits a payment for one order.

The application waits for the payment provider but eventually times out and shows the customer a message that the payment could not be confirmed. The customer presses **Pay** again.

A few minutes later, the customer receives two charge notifications from their bank for the same purchase.

## Symptoms

- The application recorded one successful payment attempt after the retry.
- The payment provider shows two successful charges for the same amount and customer.
- The first application request ended with a timeout rather than a success response.
- No application log says that the first charge failed.
- Retrying the same flow under a healthy network usually creates only one charge.

## Your task

Treat the first timeout as an unknown outcome rather than immediately assuming what happened.

- What evidence would tell you whether the first request reached the provider?
- Which system knows whether money was actually charged?
- Does a timeout prove that the operation failed?
- How could the application distinguish a retry of the same logical payment from a genuinely new payment?
- Which states must be reconciled before automatically trying again?

## Investigation

Tracing the first request shows that the application sent the charge request before its timeout expired.

The payment provider's records show a successful charge with a timestamp just before the application abandoned the request. The provider's response arrived too late for the application to use it, so the local payment row was never moved to the expected paid state.

The second attempt created a fresh provider request. From the provider's perspective, it looked like another legitimate instruction to charge the card.

The important evidence is the disagreement between **what happened** and **what the caller observed**. The external side effect completed, but acknowledgement of that outcome was lost across the network boundary.

## Root cause

The workflow treats a timeout as though it means the payment failed and then retries an operation whose side effect can be repeated.

The first request left the application and successfully charged the customer. Because the response was not observed, the application could not distinguish that success from a request that never reached the provider.

The retry represented the same logical payment intent, but nothing gave that intent a stable identity across attempts. The provider therefore executed the side effect twice.

This is an idempotency problem created by an **ambiguous outcome** across a system boundary.

## Possible approaches

### Stable idempotency key

Generate an identifier for the logical payment attempt and reuse it when the same operation is retried. If the payment provider supports idempotency semantics, repeated requests with that key can resolve to the original operation instead of creating another charge.

The key must represent the logical intent, not merely one HTTP request. Generating a new key for every retry defeats the protection.

### Durable local operation state

Persist a payment-operation record with a stable identity and explicit states such as pending, confirmed, failed, or requiring reconciliation.

This gives retries and recovery logic a durable reference. It does not make the application database and provider atomic, but it prevents the workflow from relying only on one transient request/response exchange.

### Reconcile ambiguous outcomes

When a request times out after it may have reached the provider, query the provider using the stable operation identity before deciding to create another charge.

Reconciliation is especially important when the external system cannot participate in the application's database transaction.

### Controlled retry policy

Retries can still be useful for transient failures, but policy should account for whether the operation is safe to repeat and whether its previous outcome is known.

Backoff can reduce pressure during an outage, but backoff alone does not prevent duplicate side effects.

## Trade-offs

Provider-supported idempotency is powerful at the external boundary, but its guarantees depend on provider semantics such as key scope, retention duration, and whether changed request parameters are rejected or treated differently.

Durable operation records improve recovery and observability but add state-machine complexity and require careful handling of stuck or ambiguous states.

Reconciliation reduces blind retries but depends on the provider exposing a reliable lookup mechanism. It can also increase latency before the application can give the customer a definitive answer.

A robust workflow may combine these techniques rather than relying on one mechanism.

## What could go wrong

- The application generates a new idempotency key for every retry.
- The same key is accidentally reused for two genuinely different payment intents.
- The provider's idempotency retention window expires before a delayed retry.
- The application records the operation only after calling the provider and crashes between the external charge and the local write.
- A timeout handler immediately retries while a reconciliation worker is independently retrying the same operation.
- The UI says "payment failed" when the system only knows that the outcome is unconfirmed.
- Automatic retries are made faster or more frequent without making the underlying side effect safe to repeat.

## Takeaway

Across a network boundary, **timeout does not mean failure**. It often means the outcome is unknown.

When an operation has a non-repeatable side effect such as charging money, give the logical operation a stable identity and design explicitly for ambiguous outcomes, retries, and reconciliation. Ask not only "can this request fail?" but also "what if it succeeds and I never receive the answer?"
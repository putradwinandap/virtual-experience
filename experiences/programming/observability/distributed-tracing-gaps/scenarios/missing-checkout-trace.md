---
title: "The Missing Half of a Checkout Trace"
domain: "programming"
area: "observability"
topic: "distributed-tracing-gaps"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "distributed-tracing"
  - "correlation-id"
  - "asynchronous-processing"
  - "observability"
---

# The Missing Half of a Checkout Trace

## Context

You operate an online store with a checkout API. The API validates the cart, writes an order, and publishes a payment message. A worker consumes that message and calls the payment provider. Each service emits logs and participates in distributed tracing.

Normally, a checkout trace should show the API request, order creation, message publication, worker processing, and payment-provider call.

## Situation

After a deployment, checkout latency rises for a small percentage of customers. The API team opens a trace and sees the request reach order creation and then end shortly after the message is published. The payment worker reports increased processing time, but its logs contain no trace ID that matches the affected requests.

## Symptoms

- API traces appear to finish before payment completes.
- Worker latency is high, but the trace search shows no worker spans for those checkouts.
- Searching worker logs by the API trace ID returns nothing.
- Payment-provider metrics show calls occurring during the same period.
- Retrying the checkout sometimes creates a second payment attempt.

## Your Task

What would you investigate before concluding that the payment worker was not invoked? What short-term action could reduce customer impact while preserving enough evidence to find the problem?

## Investigation

Start with the message boundary. Compare the message publication timestamp, queue delivery timestamp, worker log fields, and payment-provider request ID for one affected order. Check whether the message carries the tracing context and whether the worker creates a child span from that context.

Also compare deployment versions. A common regression is a producer or consumer library upgrade that changes propagation headers, serializes them under a different field, or drops them when a message is rebuilt. The business work can continue successfully while the trace relationship is broken.

Use the order ID and payment-provider request ID as temporary correlation keys, but treat them as separate identifiers from the trace ID. Confirm whether duplicate payment attempts are caused by the operational retry, an application retry, or a legitimate redelivery.

## Root Cause

The checkout service publishes a message containing the business payload but not the current trace context. The worker therefore starts an unrelated trace, or emits logs without a trace ID. The payment call still happens, but the causal chain is invisible in the tracing system.

## Possible Approaches

- Restore trace-context injection at message publication and extraction at consumption.
- Add stable order and payment request identifiers to structured logs and span attributes.
- Add a queue-to-worker metric and alert so queue activity remains visible even when tracing is incomplete.
- Temporarily reduce or disable the risky retry path while confirming whether in-flight payments can still complete.

## Trade-offs

Trace propagation improves investigation quality but adds integration complexity across messaging libraries and service boundaries. Business identifiers make joins easier, but they must be handled as potentially sensitive data. Metrics and logs provide useful fallback signals, though they do not replace a connected causal trace. Disabling retries can reduce duplicates while increasing the chance of delayed or failed checkouts.

## What Could Go Wrong

Do not treat an absent span as proof that the operation did not happen. Do not “fix” the issue by adding a new trace ID in every worker without preserving parent context; that increases trace volume while keeping the causal gap. Avoid logging full payment payloads merely to make correlation easier. Finally, do not replay messages until you know whether the payment provider accepted the original request.

## Takeaway

When a distributed trace stops at a queue or worker boundary, ask whether the work disappeared—or only its context did. Reconstruct the path with message, business, and provider identifiers before retrying an operation that may already be in flight.

## Related Concepts

- [Idempotency](../../../api-and-integration/idempotency/)

# Idempotency

Idempotency matters when one logical operation may be attempted more than once but repeated execution should not create unintended additional effects.

The difficult part is often not the retry itself. The difficult part is uncertainty: a caller can lose the response even when the server already completed the work. From the caller's point of view, success, failure, and an unknown outcome can look similar.

## What to practice here

Use these scenarios to practice asking:

- Can this operation be attempted more than once?
- Can the caller lose the response even when the server completed the work?
- What happens if a timeout causes a retry?
- Is repeating the same request safe?
- What identifies the same logical operation across attempts?
- Where should duplicate execution be prevented, detected, or reconciled?
- Which side effects cross boundaries that cannot be made atomic together?

## Scenarios

- [Duplicate payment after an ambiguous timeout](scenarios/duplicate-payment-after-retry.md) — a payment succeeds externally, the response is lost, and retrying can charge the customer again.
- [Duplicate order after a client retry](scenarios/duplicate-order-after-client-retry.md) — a resource-creation request succeeds, its response is lost, and the client repeats the same logical action.

## Why both belong here

Both scenarios begin with uncertainty after an operation may already have succeeded, but the system boundaries differ. The payment case crosses into a third-party side effect that the application cannot atomically commit with its own database. The order case stays within the application's API boundary and focuses on identifying one logical resource-creation attempt across repeated requests.

Seeing both helps build the recognition pattern: when retries are possible, ask whether repeated execution is safe and how the system knows that two attempts represent the same intent.
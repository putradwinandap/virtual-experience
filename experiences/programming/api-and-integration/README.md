# API & Integration

API & Integration covers failures that emerge at boundaries between clients, services, third-party systems, and asynchronous workflows.

These boundaries introduce uncertainty. A request may leave one system, cause a real side effect somewhere else, and still return no usable response to the caller. Networks can delay, duplicate, drop, or interrupt communication, so application logic must often reason about outcomes it cannot observe directly.

The useful skill is not memorizing retry rules. It is learning to identify where uncertainty enters a workflow, which effects may already have happened, and what guarantees each system boundary actually provides.

## Topics

- [Idempotency](idempotency/) — recognizing when one logical operation may be attempted more than once and repeated execution must not create unintended additional effects.

The topics listed here are only those currently available in the repository.
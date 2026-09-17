# Distributed Tracing Gaps

Distributed tracing is useful only when the trace context survives the boundaries a request crosses. A trace that starts in one service and disappears at a queue, proxy, or background worker can make a multi-service failure look like unrelated local problems.

## Scenarios

- [The missing half of a checkout trace](scenarios/missing-checkout-trace.md) — a slow checkout is investigated through a trace that stops before the asynchronous payment worker.

Practice recognizing the difference between “the dependency was not called” and “the telemetry failed to follow the work.”

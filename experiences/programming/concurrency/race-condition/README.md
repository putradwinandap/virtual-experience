# Race Condition

A race condition happens when the correctness of a result depends on the timing or interleaving of operations that can run concurrently.

That definition is compact. Recognizing one in a real system is harder.

The visible symptom may be oversold inventory, a balance that loses an update, duplicate work, an impossible state, or a bug that disappears when you add logging. The important skill is not memorizing the phrase *race condition*. It is learning to notice when multiple actors can observe or change shared state without the operation being protected as one coherent unit.

## What to practice here

Use these scenarios to practice asking:

- What state is shared?
- Which operations can overlap?
- What assumptions are being made between a read and a write?
- Can two individually valid operations produce an invalid combined result?
- Where should correctness be enforced?
- What trade-offs come with stronger coordination?

## Scenarios

- [Oversold inventory during a flash sale](scenarios/oversold-inventory.md) — a scarce-resource invariant is violated when purchases overlap.
- [Lost profile update](scenarios/lost-profile-update.md) — valid edits silently overwrite one another through stale whole-record writes.

## Why both belong here

Both failures depend on concurrent operations over shared state, but they do not look the same from the outside. One accepts more orders than available inventory; the other quietly loses valid data.

Seeing both is the point of the topic/scenario model: recognizing the underlying concurrency pattern should not depend on memorizing a single famous example.
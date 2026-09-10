# Concurrency

Concurrency is the problem space created when multiple operations can make progress during overlapping periods of time. Code that looks correct when executed one step at a time can behave differently when requests, workers, processes, or transactions interleave.

The useful skill is not simply knowing that concurrency exists. It is learning to identify shared state, assumptions about ordering, operations that must behave atomically, and invariants that overlapping work can violate.

## Topics

- [Race Condition](race-condition/) — correctness depends on timing or interleaving between concurrent operations.

The topics listed here are only those currently available in the repository.
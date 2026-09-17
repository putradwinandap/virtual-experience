# Flaky Test

A flaky test sometimes passes and sometimes fails for the same apparent change. The intermittent result is a signal that the test, system under test, or environment contains an uncontrolled variable.

## Scenarios

- [The test that only fails on Tuesdays](scenarios/test-only-fails-on-tuesdays.md) — a scheduled CI test intermittently fails because it depends on shared state and wall-clock timing.

Practice separating useful reproduction evidence from the temptation to simply rerun until the test turns green.

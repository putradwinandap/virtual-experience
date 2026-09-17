---
title: "The Test That Only Fails on Tuesdays"
domain: "programming"
area: "testing"
topic: "flaky-test"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "flaky-test"
  - "test-isolation"
  - "shared-state"
  - "time-dependency"
---

# The Test That Only Fails on Tuesdays

## Context

Your team has an integration test for a weekly account-summary job. The test creates an account, runs the job, and expects exactly one summary record. It passes on developer machines and in most CI runs.

The test suite runs in parallel, and the CI environment reuses a database schema between jobs for speed.

## Situation

Every few weeks, the Tuesday morning CI build fails on the summary assertion. Rerunning the same commit usually passes. No product code changed between the failed and successful runs.

Someone suggests adding a retry to the test because the failure is slowing down merges.

## Symptoms

- The failure appears only on one scheduled CI workflow.
- The assertion finds two summary records instead of one.
- A rerun passes without any source change.
- The failure is more common when another integration job is running.
- The test does not log the database name, worker identity, or current time window.

## Your Task

What evidence would you collect before adding a retry? How would you decide whether the duplicate record is a product bug, a test-isolation bug, or both?

## Investigation

First preserve the failed run's evidence: the exact test input, database/schema identifier, timestamps, parallel job identifiers, and relevant worker logs. Compare those details with a passing rerun.

Inspect how the test creates its account and selects the summary window. A fixed account identifier, a shared database, or a query based on the current week can allow another test or a previous run to contribute a record. Check whether cleanup runs after failures and whether the job itself is safe to execute twice.

Run the test repeatedly with randomized data, isolated schemas, and a controlled clock. Then run it in parallel with the neighboring integration tests. Each experiment should remove one possible uncontrolled variable rather than merely increasing the number of retries.

## Root Cause

The test uses a fixed account identifier and a wall-clock-derived weekly window. The scheduled workflow overlaps with another job that uses the same database schema. Both executions can create a summary visible to the assertion, so the test observes two records even though each isolated execution would produce one.

The product job may still need idempotency protection, but the test cannot establish that reliably while sharing state and depending on the real clock.

## Possible Approaches

- Give each test run an isolated schema or database and unique test data.
- Inject a clock and use a fixed instant for the scenario.
- Make cleanup explicit and verify it, including cleanup after failed tests.
- Add a focused idempotency test for the job rather than relying on isolation tests to discover duplicates.
- Keep a retry only as a temporary diagnostic measure, with the original failure retained.

## Trade-offs

Isolation and clock control make tests more deterministic but require test infrastructure and dependency seams. Unique data reduces collisions but does not replace isolation. Strong cleanup can reduce cost but is fragile when a process crashes. Retries reduce noisy CI failures while hiding the frequency and shape of the underlying problem.

## What Could Go Wrong

Do not delete the duplicate record before recording which process created it. Do not classify every intermittent failure as a test problem; timing-sensitive production defects can also surface through flaky tests. Do not increase retry counts until the test becomes green and call that a fix. A retry can turn a useful warning into permanent blind confidence.

## Takeaway

When a test passes after a rerun, the rerun is evidence about nondeterminism—not proof that the first failure was harmless. Capture the environment, remove shared state and real-time dependencies, then give product-level idempotency behavior its own explicit test.

## Related Concepts

- [Idempotency](../../../api-and-integration/idempotency/)
- [Cache invalidation](../../../caching/cache-invalidation/)

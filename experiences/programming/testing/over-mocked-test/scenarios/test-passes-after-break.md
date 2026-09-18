---
title: "The Test That Passed After the Code Broke"
domain: "programming"
area: "testing"
topic: "over-mocked-test"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["over-mocked-test", "test-double", "contract-test"]
---

# The Test That Passed After the Code Broke

## Context

An API test mocks the repository, serializer, and dependency client, asserting that each method was called.

## Situation

The real serializer contract changes, but the test remains green.

## Symptoms

- Tests verify call choreography rather than returned behavior.
- Production fails at an integration boundary.

## Your Task

Move assertions toward meaningful behavior without making every test an end-to-end test.

## Investigation

List mocked boundaries and compare what each test actually proves against the production path.

## Root Cause

Mocks replaced the contracts under test, so the test could pass while collaborators were incompatible.

## Possible Approaches

Keep narrow mocks for failure cases, use fakes or contract tests for boundaries, and assert observable outcomes.

## Trade-offs

Integration coverage costs time and setup; excessive mocks are fast but brittle and misleading.

## What Could Go Wrong

Do not remove all test doubles indiscriminately; isolate the boundary that needs realism.

## Takeaway

A test is valuable for what it can fail on, not for how many mocks it verifies.

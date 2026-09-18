---
title: "The Test That Needed the Developer's Machine"
domain: "programming"
area: "testing"
topic: "environment-dependent-test"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["environment-dependent-test", "test-isolation", "hermeticity"]
---

# The Test That Needed the Developer's Machine

## Context

A test reads a configuration file and calls a local service that usually exists on developer machines.

## Situation

The test passes locally but fails in CI and on a new teammate's machine.

## Symptoms

- Failure depends on filesystem paths, timezone, or installed services.
- The test does not declare its prerequisites.

## Your Task

Determine whether to make the dependency explicit, replace it, or provision it in the test environment.

## Investigation

Record environment variables, clock, locale, filesystem, network, and service assumptions. Re-run in a clean environment to isolate the dependency.

## Root Cause

The test relied on ambient machine state rather than controlled fixtures.

## Possible Approaches

Inject configuration, use a temporary fixture/container, or separate a true integration test from a hermetic unit test.

## Trade-offs

Hermetic tests are fast and repeatable; integration tests provide realism but need setup and cleanup.

## What Could Go Wrong

Do not weaken assertions merely to make CI green, and do not share mutable fixtures across tests.

## Takeaway

A test that needs an undocumented machine is testing the machine as much as the code.

---
title: "The Field Removal That Broke an Older Client"
domain: "programming"
area: "architecture-and-design"
topic: "backward-incompatible-contract-change"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["backward-incompatible-contract-change", "api-contract", "compatibility"]
---

# The Field Removal That Broke an Older Client

## Context

An API removes a response field that the current client no longer displays.

## Situation

An older mobile client crashes while decoding the response.

## Symptoms

- Failures correlate with client version.
- Server tests cover only the current SDK.

## Your Task

Determine the supported compatibility window and introduce the change safely.

## Investigation

Inventory consumers, review contract usage, and compare response schemas across versions. Check whether telemetry identifies client versions reliably.

## Root Cause

The server treated current-client behavior as the whole contract and removed a field still required by supported consumers.

## Possible Approaches

Keep the field, version the contract, or deprecate it through a measured migration window.

## Trade-offs

Compatibility increases maintenance; versioning increases operational surface; deprecation requires consumer coordination.

## What Could Go Wrong

Do not infer “unused by us” means “unused by consumers.”

## Takeaway

An interface belongs to its consumers; compatibility work begins with discovering who they are.

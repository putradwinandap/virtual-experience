---
title: "The Instances With Different Rules"
domain: "programming"
area: "production-and-reliability"
topic: "configuration-drift"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["configuration-drift", "reproducibility", "deployment"]
---

# The Instances With Different Rules

## Context

An autoscaled service reads feature and timeout settings from local configuration.

## Situation

Only some instances reject a request because they were started with older values.

## Symptoms

- Errors correlate with instance ID.
- Restarting one instance changes its behavior.
- The deployment artifact is identical, but runtime configuration is not.

## Your Task

Find the source of configuration truth and make divergence visible.

## Investigation

Compare effective configuration hashes, startup timestamps, secret versions, and rollout mechanisms.

## Root Cause

Configuration changed outside the reproducible deployment path and instances were not converged.

## Possible Approaches

Centralize versioned configuration, validate at startup, and expose safe configuration fingerprints.

## Trade-offs

Central configuration adds a dependency; strict validation can prevent startup but avoids partial behavior.

## What Could Go Wrong

Never expose secret values while exposing configuration diagnostics.

## Takeaway

Identical code does not imply identical behavior when effective configuration drifts.

---
title: "The Deployment That Passed but Broke Requests"
domain: "programming"
area: "production-and-reliability"
topic: "bad-deployment"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "bad-deployment"
  - "backward-compatibility"
  - "rollback"
---

# The Deployment That Passed but Broke Requests

## Context

An API service is deployed behind a load balancer. Automated tests pass, health checks are green, and the deployment gradually shifts traffic to the new version.

## Situation

Shortly after the shift begins, a partner integration reports validation errors. Internal clients using the newest SDK work normally.

## Symptoms

- Error rates increase only for older client versions.
- New instances are healthy according to their endpoint checks.
- Logs show requests reaching the service but failing schema validation.
- Rolling back reduces errors, but the database contains records created by the new version.

## Your Task

What compatibility assumptions should you verify before choosing rollback? Which signals would distinguish an application defect from an incompatible contract change?

## Investigation

Compare requests by client version, route, and deployment version. Inspect the API and event contract diff, including removed fields, changed enum values, and stricter validation. Check whether the new code can read data written by the previous version and whether rollback can safely read data written by the new version.

## Root Cause

The new deployment tightened a response/request contract that older clients still depended on. Unit tests covered current clients but not the compatibility window. Health checks verified process readiness, not real contract compatibility.

## Possible Approaches

- Restore backward-compatible behavior and deprecate it gradually.
- Stop the rollout and route traffic to a known-compatible version.
- Use expand-and-contract changes for shared data and contracts.
- Add compatibility tests using supported client versions.

## Trade-offs

Compatibility layers preserve reliability but increase maintenance. A rollback is fast when safe, but can fail if schema or data changes are not backward-compatible. More contract tests and staged rollouts slow delivery slightly while reducing blast radius.

## What Could Go Wrong

Do not treat green health checks as proof that users can use the service. Do not roll back blindly after an irreversible data migration, and do not fix only the visible client while leaving other older consumers unsupported.

## Takeaway

A deployment is successful only when supported consumers remain compatible. Include real compatibility checks in rollout signals, not just process health and test-suite results.

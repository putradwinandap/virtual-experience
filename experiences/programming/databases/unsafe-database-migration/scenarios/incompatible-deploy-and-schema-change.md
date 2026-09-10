---
title: "Incompatible Deploy and Schema Change"
domain: "programming"
area: "databases"
topic: "unsafe-database-migration"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "database-migration"
  - "backward-compatibility"
  - "rolling-deployment"
---

# Incompatible Deploy and Schema Change

## Context

A service is deployed as several application instances behind a load balancer. Releases use a rolling deployment so capacity remains available while old instances are gradually replaced by new ones.

A new release changes how a customer profile field is stored. The team has prepared both application code and a schema migration and has tested the final combination successfully in staging.

During a rollout, however, the fleet is not replaced atomically. For several minutes, requests can reach either the old application version or the new one.

## Situation

The schema migration completes successfully and the new application instances begin entering service.

Most requests work, but some profile updates fail intermittently. Retrying the same request may succeed without any code or database change.

The failures disappear after the rollout finishes and all old instances have been terminated.

## Symptoms

- Errors begin only during the deployment window.
- The migration itself reports success and database lock waits are normal.
- Requests routed to some instances succeed while otherwise similar requests routed to other instances fail.
- Error logs reference a column or data shape that changed as part of the release.
- Both the old application version with the old schema and the new application version with the final schema pass their isolated tests.
- Rollout status shows old and new application instances serving traffic at the same time.
- After the final old instance exits, the intermittent failures stop.

## Your task

Do not treat migration success as proof that the rollout is safe.

- Which combinations of application version and schema state can exist from the start of deployment to the end?
- Can the old application run against the migrated schema?
- Can the new application run before every schema/data transition is complete?
- Are reads and writes compatible in both directions while versions overlap?
- What would happen if the application deployment had to be rolled back after new code had already written data in the new shape?
- Can the change be sequenced so every intermediate state is deployable?

## Investigation

Routing and instance logs show that failures correlate with requests handled by the old application version after the schema migration has changed the database shape it expects.

The release was designed around two stable endpoints:

```text
Before: old application + old schema
After:  new application + new schema
```

But the rolling deployment creates intermediate states as well:

```text
old application + transitional/new schema
new application + transitional/new schema
```

The old version still reads or writes the previous column contract. The migration removes or changes that contract before all old instances have stopped serving traffic. Requests therefore fail depending on which version receives them.

The final state is valid, which is why staging tests that jump directly from "before" to "after" can pass. The unsafe part is the path between those states.

Rollback analysis reveals another hazard: once new instances write data using the new representation, simply redeploying the old binary may not restore compatibility. Code rollback and data/schema rollback are not automatically equivalent operations.

## Root cause

The application change and schema migration are tightly coupled as though deployment were atomic.

The rollout temporarily runs multiple application versions against one evolving database, but the schema change removes compatibility before every old instance has left service. The release therefore contains an intermediate state in which a valid application version and a valid schema version are incompatible with each other.

The migration does not need to block traffic to be unsafe. The failure comes from sequencing and compatibility across rollout states.

## Possible approaches

### Expand and contract the schema

Split the change into stages. First expand the schema in a way that remains compatible with the old application. Then deploy code that can use the new shape while tolerating the old one as necessary. Migrate or backfill data if required. Only after old code no longer depends on the previous shape should a later release contract the schema by removing it.

The exact stages depend on whether the change affects reads, writes, constraints, data representation, or all of them.

### Make application versions tolerant during transition

New code can temporarily support both old and new representations, or writes can be coordinated so both versions observe a compatible contract during the overlap period.

Dual reads or writes may help in some migrations, but they introduce consistency and cleanup concerns and should not be added mechanically.

### Separate deployment and destructive migration

Treat a destructive schema step as a later rollout after telemetry confirms that no active application version depends on the old contract.

This increases the number of release steps but creates an explicit compatibility boundary instead of relying on deployment timing.

### Model rollback before rollout

Decide which states can safely roll back and what "rollback" means after data has been written in a new format. Sometimes the safer recovery action is to roll forward with a compatible fix rather than reverse a schema or data transformation.

The recovery plan should reflect actual data compatibility, not assume that reverting the application artifact restores the previous system state.

## Trade-offs

Expand-and-contract migrations reduce coupling between code and schema rollout, but they require multiple releases and leave temporary schema or compatibility code that must eventually be removed.

Supporting multiple representations increases application complexity and test combinations. If dual writes are used, partial failures can create divergence that needs detection and repair.

Delaying destructive cleanup keeps rollback options open longer but carries old columns, indexes, or code paths for additional time and can make ownership of cleanup less obvious.

A fast coordinated deployment may reduce the overlap window, but relying on a tiny window is fragile: health checks, autoscaling, rollback, slow shutdown, or deployment failures can extend coexistence unexpectedly.

## What could go wrong

- The new code can read both schema shapes but writes data that old code cannot interpret.
- A backfill is assumed complete before all rows are actually converted.
- A destructive migration runs based on expected deployment duration rather than evidence that old instances are gone.
- A rollback restores old application instances after new code has already written incompatible data.
- Dual writes update one representation but fail before updating the other.
- Temporary compatibility code becomes permanent because the contract step is never scheduled.
- Tests cover the before and after states but not the intermediate combinations that exist during rolling deployment.

## Takeaway

A database migration is part of a rollout timeline, not just a transition from one final schema to another.

When application instances are replaced gradually, enumerate the code-and-schema combinations that can exist in between. Prefer changes where old and new versions can coexist with the transitional schema, and treat destructive cleanup as a separate step once compatibility is no longer required. Always ask whether rollback remains valid after the data shape has changed.
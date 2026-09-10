# Unsafe Database Migration

A schema migration can be logically correct and still be operationally unsafe.

The risk often appears only when the change meets production-sized data, concurrent traffic, database-engine behavior, and a deployment where multiple application versions temporarily coexist. An operation that finishes almost instantly in development may scan or rewrite a large table, wait for a lock, block other work, or leave old application instances incompatible with the new schema.

## What to practice here

Use these scenarios to practice asking:

- Does this migration acquire locks, rewrite data, or scan a large table?
- How long can that work take on production-sized data?
- What happens to reads and writes while it runs?
- Which queries or transactions can delay the migration, and which can the migration delay?
- Can old and new application versions coexist with the schema throughout a rolling rollout?
- Is rollback actually safe after the schema or stored data has changed?
- Can the change be split into smaller, backward-compatible steps?
- What should be observed before, during, and after the rollout?

There is no universal safe-migration recipe. The answers depend on the database engine and version, the exact DDL operation, table size, workload, transaction behavior, deployment strategy, and the application's compatibility requirements.

## Scenarios

- [Migration locks production traffic](scenarios/migration-locks-production-traffic.md) — a migration that was fast in staging stalls under production data and traffic while requests accumulate behind database waits.
- [Incompatible deploy and schema change](scenarios/incompatible-deploy-and-schema-change.md) — a rolling deployment temporarily runs application versions with conflicting schema expectations, producing intermittent failures even though the migration itself completes.

## Why both belong here

Both scenarios involve schema evolution that appears reasonable in isolation but becomes unsafe when rollout context is considered.

The first is primarily an operational contention problem: the migration's database work and lock behavior interact with production scale and active queries. The second is primarily a compatibility problem: old code, new code, and changing schema must coexist during a rolling deployment.

Seeing both builds a broader recognition pattern: before treating a migration as a single SQL step, reason about the database work it performs and every application state that can exist while the change is rolling out.
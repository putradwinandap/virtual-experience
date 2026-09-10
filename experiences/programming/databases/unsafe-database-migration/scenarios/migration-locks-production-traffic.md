---
title: "Migration Locks Production Traffic"
domain: "programming"
area: "databases"
topic: "unsafe-database-migration"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "database-migration"
  - "database-locking"
  - "production-scale"
---

# Migration Locks Production Traffic

## Context

A web application stores customer activity in a relational database. One of its busiest tables has grown for several years and now contains tens of millions of rows.

A release needs a schema change on that table. The migration was tested in development and staging, where it completed in seconds and did not cause visible application errors.

Production receives steady reads and writes throughout the day, and normal requests are expected to finish quickly.

## Situation

The release begins during a normal traffic period. Shortly after the schema migration starts, application latency rises sharply.

Some requests time out. Workers that normally finish database operations in milliseconds remain active for much longer, and the connection pool starts filling with sessions that appear to be waiting rather than consuming significant CPU.

The migration process itself has not reported an error.

## Symptoms

- Request latency increased soon after the migration began.
- Read or write queries touching the affected table are accumulating in the database.
- Several database sessions are waiting on other sessions or on a schema-related operation.
- Application instances begin exhausting database connections as requests remain open longer.
- Database CPU is not necessarily saturated even though application throughput has fallen.
- The same migration completed quickly against staging data.
- Canceling unrelated application requests briefly reduces the queue, but waits build again while the migration continues.

## Your task

Production is degrading while a migration that looked safe in staging is still running.

- What would you inspect before deciding whether to wait, cancel the migration, or reduce application traffic?
- Which session is blocking which other sessions?
- Is the migration actively processing data, waiting to acquire a lock, or holding a lock while doing long-running work?
- Does the exact schema operation require scanning or rewriting the table on this database engine and version?
- How different are production table size, transaction duration, and traffic from staging?
- What secondary failures can occur if blocked queries continue consuming application resources?

## Investigation

Database activity shows that requests touching the table are queued around the migration operation. The wait graph reveals that the migration needs a lock mode that conflicts with normal application work for at least part of the operation.

The production table is far larger than its staging copy. On the database engine and version in use, the exact schema change cannot be treated as a constant-time metadata-only update: it performs work proportional to the existing data and keeps a conflicting lock long enough to affect live traffic.

A few ordinary application transactions also stay open longer than expected. Depending on timing, they can delay the migration from acquiring its required lock. Once the migration obtains the lock, other queries begin waiting behind it.

The application then amplifies the database wait. Requests hold worker capacity and database connections while blocked, retries add more work, and upstream timeouts make the incident look like a broad application outage even though the initial contention is concentrated around one table.

Staging did not reproduce the behavior because its smaller dataset and lighter concurrent workload made the lock window too short to become operationally visible.

## Root cause

The migration was evaluated mainly by whether its SQL was logically valid and whether it completed in smaller environments. Its production execution characteristics were not treated as part of the change.

On the actual database engine, version, table size, and workload, the schema operation performs long-running work while requiring a lock that conflicts with application queries. Production traffic therefore waits behind the migration, and those waits cascade into connection-pool pressure and request timeouts.

The unsafe assumption was not that all DDL blocks traffic. It was that fast completion in staging demonstrated that this particular DDL operation would have an acceptably short lock and execution window in production.

## Possible approaches

### Verify the engine-specific operation before rollout

Inspect documentation and test behavior for the exact database engine, version, table shape, and migration operation. Determine whether the change is metadata-only, scans existing rows, rewrites storage, or requires a blocking lock.

A production-sized rehearsal or representative copy can reveal duration and resource behavior that a small staging database cannot.

### Use an online or less-blocking migration mechanism when supported

Some engines, versions, or migration tools provide mechanisms that reduce how long conflicting locks are held or perform much of the work while traffic continues.

Their guarantees and limitations are engine-specific. "Online" does not necessarily mean zero locks, zero overhead, or zero operational risk.

### Split schema change and data movement

When the desired change permits it, introduce a backward-compatible schema shape first, such as a nullable column, and move expensive data population into a separate batched backfill.

Batches can bound transaction duration and reduce contention, while later steps enforce stronger constraints after the data is ready.

### Bound lock acquisition and execution risk

A lock timeout can make a migration fail rather than wait indefinitely for a dangerous lock window. Operational runbooks can define when to abort, retry, or reschedule based on observed contention.

This limits some failure modes but does not make a fundamentally expensive operation cheap.

### Choose a safer operational window and observe it

For operations that cannot avoid meaningful contention, lower-traffic periods can reduce impact. Monitor lock waits, query latency, connection utilization, replication or storage effects where relevant, and migration progress during rollout.

Scheduling is risk reduction, not a substitute for understanding the operation.

## Trade-offs

Online migration mechanisms can reduce blocking but may add tooling complexity, temporary storage, replication load, triggers or shadow structures, and engine-specific failure modes.

Batched backfills make work more controllable but turn one migration into a multi-step rollout that needs progress tracking, resumability, and compatibility between intermediate states.

Strict lock timeouts protect traffic from an indefinitely waiting migration, but repeated retries can still cause disruption if the underlying contention is not understood.

Running outside peak traffic reduces the number of affected requests but can increase operational burden and still fail if table size makes the operation intrinsically long.

A representative rehearsal provides better evidence than a tiny staging database, but production workload, transaction timing, hardware, and data distribution can still differ.

## What could go wrong

- A migration tool labels an operation "online," but the operation still takes short exclusive locks that become significant under the real workload.
- A backfill uses batches that are too large and recreates long transactions and contention.
- The migration waits behind one forgotten long-running transaction while new application queries queue behind the pending schema lock.
- Application retries multiply load while the database is already blocked.
- Engineers monitor CPU but miss lock waits and connection-pool exhaustion.
- A migration is canceled without checking whether the database can roll back the operation quickly or whether rollback itself requires substantial work.
- A successful production run is treated as proof that the same operation will always be safe as the table continues to grow.

## Takeaway

For schema changes on live databases, ask more than "does this SQL work?"

Ask what the exact operation does on the actual engine and version, how much existing data it must touch, what locks it needs and for how long, and what production traffic does while those locks are held or awaited. A migration that is invisible on a small staging dataset can become a production incident when scale turns a tiny lock window into a long one.
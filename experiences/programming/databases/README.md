# Databases

Databases turn application intent into durable shared state, but their behavior depends heavily on data volume, concurrency, storage engine behavior, query patterns, and the workload running at the same time.

A change that looks harmless against a small local dataset can behave very differently when it must scan or rewrite millions of rows while production traffic is reading and writing the same tables. Transactions, locks, schema evolution, query execution, and data integrity all interact with operational constraints that are easy to miss outside production-like conditions.

The useful skill is not memorizing one database vendor's commands. It is learning to ask what work an operation actually performs, what resources it holds while doing that work, which other queries can proceed, and whether application versions can safely coexist while the data shape changes.

## Topics

- [Unsafe Database Migration](unsafe-database-migration/) — recognizing schema changes that become risky through locks, long-running work, production-scale data, rollout incompatibility, or unsafe rollback assumptions.

The topics listed here are only those currently available in the repository.
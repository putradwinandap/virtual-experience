# Initial Taxonomy

Status: **MVP baseline**

The taxonomy should evolve from real content rather than attempting to model all of software engineering up front.

## Canonical metadata vocabulary

Scenario metadata uses canonical kebab-case identifiers.

For the MVP:

```text
domain: programming
```

Initial canonical `area` values are:

```text
concurrency
databases
api-and-integration
distributed-systems
production-and-reliability
security
git-and-collaboration
testing
performance
architecture-and-design
```

Topic and concept identifiers also use kebab-case, for example `race-condition`, `database-transaction`, and `broken-authorization`.

Do not create spelling/casing variants such as `race_condition`, `Race Condition`, or `racecondition` when a canonical term already exists. New canonical terms may be introduced when a real contribution needs them; the taxonomy should not be pre-populated merely for completeness.

## Initial domain: Programming / Software Engineering

```text
programming/
├── concurrency/
├── databases/
├── api-and-integration/
├── distributed-systems/
├── production-and-reliability/
├── security/
├── git-and-collaboration/
├── testing/
├── performance/
└── architecture-and-design/
```

These areas are intentionally broad. We should add or split them when actual contributed experiences make the need clear.

## Example topics

### Concurrency

- race-condition
- deadlock
- lost-update

### Databases

- n-plus-one-query
- unsafe-production-migration
- transaction-boundary-mistake
- missing-index

### API and integration

- retry
- idempotency
- third-party-timeout
- webhook-duplication

### Distributed systems

- partial-failure
- eventual-consistency
- duplicate-message-processing

### Production and reliability

- memory-leak
- cascading-failure
- configuration-drift
- bad-deployment

### Security

- broken-authorization
- leaked-secret
- insecure-direct-object-reference

### Git and collaboration

- accidental-force-push
- merge-conflict
- reverted-production-fix

### Testing

- flaky-test
- environment-dependent-test
- over-mocked-test

### Performance

- cache-stampede
- unbounded-query
- unexpected-hot-path

### Architecture and design

- premature-abstraction
- hidden-coupling
- backward-incompatible-contract-change

## Taxonomy rules

1. Prefer understandable names over academically perfect classification.
2. A scenario has one primary `domain`, `area`, and `topic` home even if it relates to several concepts.
3. `concepts` represents secondary or cross-cutting concepts without duplicating scenario files.
4. Canonical identifiers use lowercase kebab-case.
5. Do not duplicate the same scenario into several directories.
6. Do not create taxonomy entries with no real content need merely for completeness.
7. New topic/concept vocabulary may be introduced with a contribution when needed, but should reuse existing canonical terms whenever possible.
8. Taxonomy changes that affect many existing experiences should be documented as durable project decisions.

## Future domains

Virtual Experience may eventually support domains outside programming, but those taxonomies are explicitly out of MVP scope.

Possible future examples include product management, design, entrepreneurship, finance, operations, or other fields where practical scenarios can accelerate exposure.

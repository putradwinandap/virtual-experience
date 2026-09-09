# Initial Taxonomy

Status: **Draft for MVP**

The taxonomy should evolve from real content rather than attempting to model all of software engineering up front.

## Initial domain: Programming / Software Engineering

Proposed starting categories:

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

These categories are intentionally broad. We should add or split categories when actual contributed experiences make the need clear.

## Example topics

### Concurrency

- race condition
- deadlock
- lost update

### Databases

- N+1 queries
- unsafe production migration
- transaction boundary mistakes
- missing indexes

### API and integration

- retries
- idempotency
- third-party timeout
- webhook duplication

### Distributed systems

- partial failure
- eventual consistency surprises
- duplicate message processing

### Production and reliability

- memory leak
- cascading failure
- configuration drift
- bad deployment

### Security

- broken authorization
- leaked secrets
- insecure direct object reference

### Git and collaboration

- accidental force push
- difficult merge conflict
- reverted production fix

### Testing

- flaky test
- environment-dependent test
- test that mocks away the actual bug

### Performance

- cache stampede
- unbounded query
- unexpected hot path

### Architecture and design

- premature abstraction
- hidden coupling
- backward-incompatible contract change

## Taxonomy rules

1. Prefer understandable names over academically perfect classification.
2. A scenario should have one primary home even if it relates to several concepts.
3. Cross-links or metadata can represent secondary concepts later.
4. Do not duplicate the same scenario into several directories.
5. Do not create categories with no content merely for completeness.
6. Taxonomy changes that affect many existing experiences should be documented as durable project decisions.

## Future domains

Virtual Experience may eventually support domains outside programming, but those taxonomies are explicitly out of MVP scope.

Possible future examples include product management, design, entrepreneurship, finance, operations, or other fields where practical scenarios can accelerate exposure.

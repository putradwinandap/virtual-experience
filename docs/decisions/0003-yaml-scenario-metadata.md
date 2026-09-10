# ADR 0003: Use minimal YAML front matter for scenario metadata

- Status: Accepted
- Date: 2026-09-10

## Context

Virtual Experience scenarios need metadata that humans can understand while also supporting deterministic validation, indexing, search, and potential future presentation layers.

The MVP is repository-first and Markdown-based. Metadata therefore needs to work without introducing a database or application-specific storage format.

Attribution also needs special care because the project distinguishes between who contributes content and whether a scenario represents real, adapted, or illustrative experience. AI-assisted content must never gain fabricated first-hand provenance.

## Decision

Scenario files will use YAML front matter.

The required MVP fields are:

```yaml
---
title: "Oversold Inventory During Flash Sale"
domain: "programming"
area: "concurrency"
topic: "race-condition"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "race-condition"
  - "database-transaction"
---
```

`contributor.github` is optional:

```yaml
contributor:
  github: "username"
```

Allowed difficulty values are:

- `beginner`
- `intermediate`
- `advanced`

Allowed provenance values are:

- `real`
- `adapted`
- `illustrative`

`domain`, `area`, `topic`, and `concepts` use canonical lowercase kebab-case taxonomy identifiers.

## Attribution semantics

Contributor identity and provenance are separate concepts.

- `contributor` identifies who submitted or authored the scenario when explicit attribution is useful.
- `provenance.type` describes the scenario's relationship to real experience.

A contributor field does not prove first-hand experience.

Git history remains the baseline authorship record, so contributor metadata is not mandatory in the MVP.

AI-generated or AI-originated scenarios default to `illustrative`. AI must not invent a human contributor, real incident, company, or first-hand provenance.

## Difficulty semantics

Difficulty measures prerequisite reasoning required to understand the scenario rather than incident severity.

- `beginner`: domain fundamentals are sufficient.
- `intermediate`: understanding requires combining multiple concepts or components.
- `advanced`: understanding requires significant system reasoning, trade-off analysis, concurrency/distribution/scale reasoning, or comparable complexity.

## Intentionally excluded metadata

The MVP does not require:

- stable scenario IDs
- version numbers
- created/updated timestamps
- company names
- technology lists
- severity
- estimated completion time
- publication status
- solution fields
- an `ai_generated` flag

Git already provides history and timestamps. Other fields should only be added after real usage demonstrates a need.

## Consequences

### Positive

- Metadata can be parsed deterministically by Content CI.
- Markdown remains the primary human-readable content format.
- Future indexing or website generation does not need to infer basic classification from prose.
- Provenance becomes explicit and machine-checkable.
- The schema stays small enough for community contributors.

### Negative

- Contributors must learn a small amount of YAML syntax.
- Canonical taxonomy vocabulary requires maintenance.
- Schema changes later may require migrations across existing scenarios.

## Follow-up

Issue #3 should implement repository-owned validation and GitHub Actions checks against this accepted schema.

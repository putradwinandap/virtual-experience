# ADR 0002: Topic and scenario content model

- Status: Accepted
- Date: 2026-09-10

## Context

Virtual Experience needs to represent both reusable concepts and the fact that the same concept can appear in many different real-world situations.

If every contribution becomes a standalone article, the library will fragment concept explanations. If experiences are merged only by concept, important differences in context, symptoms, investigation, decisions, and consequences may disappear.

## Decision

Use a **topic → scenarios** model.

A topic represents the broader concept or problem family. A scenario represents one concrete manifestation of that topic.

Multiple scenarios may coexist under one topic when they provide materially different exposure.

Example:

```text
Race Condition
├── Oversold inventory
├── Duplicate processing
└── Lost update
```

## Consequences

- learners can understand a concept through multiple contexts
- contributor experiences do not need to be artificially merged
- common concept information can live at topic level
- scenario-level provenance and attribution remain possible
- maintainers need criteria for determining whether a submission is a new scenario, a new topic, or a duplicate

Those criteria should evolve from actual contributions and are described initially in `docs/project/experience-model.md`.

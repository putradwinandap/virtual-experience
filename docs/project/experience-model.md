# Experience Model

## Goal

The content model should help a learner feel exposed to a practical situation rather than merely read a definition of a concept.

The core hierarchy is:

```text
Domain
└── Area
    └── Topic
        ├── Topic overview
        └── Scenarios
            ├── Scenario A
            ├── Scenario B
            └── Scenario C
```

Example:

```text
Programming
└── Concurrency
    └── Race Condition
        ├── Overview
        └── Scenarios
            ├── Oversold inventory
            ├── Duplicate processing
            └── Lost update
```

## Topic vs scenario

A **topic** represents a reusable concept, failure class, problem family, or practical phenomenon.

A **scenario** represents one concrete manifestation of that topic.

This distinction is important. We should not create separate definitions of race condition for every contributor, but we should preserve different race-condition scenarios when their contexts and lessons differ.

## Scenario metadata

Scenario files use YAML front matter so metadata remains readable by humans and deterministic for validators, indexing, and future tooling.

The MVP required fields are:

- `title`
- `domain`
- `area`
- `topic`
- `difficulty`
- `provenance.type`
- `concepts`

Explicit `contributor.github` attribution is optional. Git history remains the baseline authorship record.

The canonical schema and copyable example live in `EXPERIENCE_TEMPLATE.md`. Durable rationale is recorded in ADR 0003.

Metadata intentionally does not include IDs, versions, timestamps, company names, severity, estimated time, or AI-generation flags in the MVP. These should only be added when real product needs justify them.

## Scenario learning journey

A scenario should usually expose the learner to the following journey:

```text
Context
  ↓
Situation
  ↓
Symptoms
  ↓
Your Task / Decision Point
  ↓
Investigation
  ↓
Root Cause
  ↓
Possible Approaches
  ↓
Trade-offs
  ↓
What Could Go Wrong
  ↓
Takeaway
```

This is a learning model, not an immutable Markdown heading list. Some scenarios may need different structure, but changes should preserve the intent: **experience the situation before consuming the explanation**.

## Scenario provenance

Every scenario must clearly communicate provenance through `provenance.type`.

### `real`

A human contributor explicitly states that the scenario is based on something they personally encountered.

It may still be anonymized for privacy, confidentiality, or security.

### `adapted`

The scenario derives from real experience but has been generalized, combined, anonymized, or otherwise modified enough that it should not be presented as a literal incident report.

### `illustrative`

The scenario is intentionally constructed to demonstrate a known problem or edge case.

AI-generated scenarios default to this classification unless a human provides provenance supporting another classification.

## Attribution

Attribution describes who contributed or authored a scenario; it must not imply facts we cannot verify.

`contributor.github` is optional because Git history already records authorship and illustrative AI-assisted scenarios should not invent an identity.

A contributor identity and provenance answer different questions:

- contributor: who submitted or authored this content?
- provenance: what claim are we making about the scenario's relationship to real experience?

A contributor may submit `real`, `adapted`, or `illustrative` content. The contributor field alone never proves first-hand experience.

## Difficulty

Difficulty measures prerequisite reasoning needed to understand a scenario, not incident severity.

- `beginner` — understandable with domain fundamentals.
- `intermediate` — requires combining multiple concepts or components.
- `advanced` — requires significant system reasoning, trade-off analysis, concurrency/distribution/scale reasoning, or comparable domain complexity.

## Canonical taxonomy values

`domain`, `area`, `topic`, and `concepts` use canonical kebab-case vocabulary maintained by the project taxonomy. A scenario has one primary domain/area/topic home while `concepts` can represent relevant cross-cutting concepts without duplicating the scenario into multiple directories.

## Duplicate scenarios

Two scenarios should remain separate when they differ materially in one or more of:

- context or domain
- observable symptoms
- constraints
- investigation path
- decisions
- solution trade-offs
- consequences
- lessons

Near-identical submissions can be merged or linked when a second copy provides no meaningful new exposure.

## Quality bar

A useful Virtual Experience scenario should make a learner more likely to recognize a similar class of situation later.

A scenario is weak when it is merely:

- a textbook definition
- a generic tutorial
- an unexplained code snippet
- a solution with no problem context
- an AI-generated story presented as real experience

A scenario is strong when the learner can answer questions such as:

- What did the situation look like before the root cause was known?
- What signals could have led me toward the problem?
- What decisions were available?
- Why might an obvious solution be insufficient?
- What trade-offs would I need to consider?
- What pattern should I recognize next time?

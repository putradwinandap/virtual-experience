# Experience Model

## Goal

The content model should help a learner feel exposed to a practical situation rather than merely read a definition of a concept.

The core hierarchy is:

```text
Domain
└── Category
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

Every scenario must clearly communicate provenance.

### Real experience

The contributor states that the scenario is based on something they actually encountered.

It may still be anonymized for privacy, confidentiality, or security.

### Adapted experience

The scenario derives from real experience but has been generalized, combined, anonymized, or otherwise modified enough that it should not be presented as a literal incident report.

### Illustrative scenario

The scenario is intentionally constructed to demonstrate a known problem or edge case.

AI-generated scenarios default to this classification.

## Attribution

Attribution should describe who contributed a scenario, not imply facts we cannot verify.

A topic can contain scenarios from multiple contributors.

Example conceptual presentation:

```text
Race Condition

- Scenario: Oversold inventory — contributed by Alice
- Scenario: Duplicate payment processing — contributed by Bob
- Scenario: Lost update — illustrative
```

The exact metadata format remains an MVP implementation decision.

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

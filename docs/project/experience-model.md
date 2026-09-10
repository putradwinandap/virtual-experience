# Experience Model

## Goal

The content model should help a learner feel exposed to a practical situation rather than merely read a definition of a concept.

The core hierarchy is:

```text
Domain
├── README.md                 # Domain overview
└── Area
    ├── README.md             # Area overview
    └── Topic
        ├── README.md         # Topic overview
        └── scenarios
            ├── Scenario A
            ├── Scenario B
            └── Scenario C
```

Example:

```text
Programming
├── Overview
└── Concurrency
    ├── Overview
    └── Race Condition
        ├── Overview
        └── Scenarios
            ├── Oversold inventory
            └── Lost update
```

Every instantiated Domain, Area, and Topic must have a `README.md` overview. A node is instantiated when repository content exists at or beneath it. The rationale and structural rule are recorded in ADR 0004.

## Progressive context

Each layer has a different job. The hierarchy should become more concrete as the learner moves downward.

### Domain — orientation

A Domain answers: **Where am I?**

Its overview should orient the learner to the broad world represented by the Domain, describe the kinds of practical experience that belong there, and surface Areas that actually exist in the repository.

A Domain overview should not become an encyclopedia or explain individual problem solutions.

### Area — problem-space map

An Area answers: **What class of concerns am I exploring?**

Its overview should explain the concern or problem space, why it produces meaningful practical problems, and surface Topics that actually exist beneath it.

An Area overview should provide enough context to understand why its Topics belong together without duplicating their detailed explanations.

### Topic — recognition model

A Topic answers: **What problem pattern am I learning to recognize?**

A topic represents a reusable concept, failure class, problem family, or practical phenomenon. Its overview should explain the shared mental model, useful recognition questions or patterns, and surface Scenarios that actually exist beneath it.

The overview may teach enough concept to orient the learner, but should avoid unnecessarily spoiling the investigation or answer of individual scenarios.

### Scenario — concrete experience

A Scenario answers: **What does encountering this problem actually feel like?**

A scenario represents one concrete manifestation of a Topic. It should expose the learner to a situation, observable signals, decisions, investigation, root cause, approaches, trade-offs, consequences, and takeaways as appropriate.

This distinction is important. We should not create separate definitions of race condition for every contributor, but we should preserve different race-condition scenarios when their contexts and lessons differ.

## Overview navigation

Overview pages should list or clearly surface children that **actually exist** in the repository. They should not present aspirational or supposedly exhaustive catalogs as if those experiences are already available.

For the Markdown MVP, child navigation is maintained manually. Exact headings are not mandated: the responsibility of each layer is the contract, not a rigid document template.

Avoid duplication by keeping explanation at the layer where it belongs and linking downward for detail. Domain pages orient, Area pages map the concern space, Topic pages build recognition, and Scenarios provide concrete experience.

Content CI enforces the deterministic structural invariant that a Scenario has its Domain, Area, and Topic overview chain. Pedagogical completeness, prose quality, useful child navigation, and unnecessary duplication remain review responsibilities.

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

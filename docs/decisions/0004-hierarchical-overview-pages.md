# ADR 0004: Hierarchical overview pages

## Status

Accepted

## Context

Virtual Experience organizes scenario content as:

`Domain → Area → Topic → Scenario`

The original model explicitly included a topic overview, but did not define equivalent orientation at Domain and Area levels or whether overview pages were required. While preparing the first race-condition scenarios, this became a structural dependency: a learner should be able to enter the library at any hierarchy level and understand where they are, what the level represents, and what content is actually available below it.

We want progressive context without turning Virtual Experience into a textbook or duplicating scenario explanations across parent pages.

## Decision

Every **instantiated** Domain, Area, and Topic in `experiences/` must contain a `README.md` overview.

A hierarchy node is instantiated when repository content exists at or beneath that node. Therefore a scenario at:

```text
experiences/<domain>/<area>/<topic>/scenarios/<scenario>.md
```

requires this complete overview chain:

```text
experiences/<domain>/README.md
experiences/<domain>/<area>/README.md
experiences/<domain>/<area>/<topic>/README.md
```

We standardize on `README.md` because GitHub renders it naturally when browsing directories and it keeps the repository useful without a dedicated application.

### Responsibilities by level

**Domain — orientation.** Explain what broad world the learner is entering in the context of Virtual Experience, what kinds of practical experience belong there, and which Areas are currently available.

**Area — problem-space map.** Explain the class of concerns represented by the Area, why those concerns create meaningful practical problems, and which Topics are currently available.

**Topic — recognition model.** Explain the shared concept/problem family, useful recognition questions or patterns, and which Scenarios are currently available. It may teach enough concept to orient the learner but should avoid unnecessarily spoiling the investigation of individual scenarios.

**Scenario — concrete experience.** Put the learner into a specific situation with symptoms, decisions, investigation, root cause, approaches, trade-offs, consequences, and takeaways as appropriate. Scenario learning remains flexible rather than a rigid heading contract.

### Progressive-context principle

The hierarchy should answer progressively more concrete questions:

- Domain: **Where am I?**
- Area: **What class of concerns am I exploring?**
- Topic: **What problem pattern am I learning to recognize?**
- Scenario: **What does encountering this problem actually feel like?**

### Child lists

Overview pages should list or clearly surface **children that actually exist in the repository**. They should not present aspirational or supposedly exhaustive catalogs as if those experiences are already available.

For the Markdown MVP, child navigation is maintained manually. Human review is responsible for useful wording and navigation completeness. We may generate navigation later if manual maintenance becomes a demonstrated burden.

### Flexible prose, stable responsibility

The project does not mandate exact Markdown headings for overview pages. The responsibility of each layer is the contract, not a fixed document template.

### Avoiding duplication

Each layer should add context appropriate to its scope rather than repeat its children:

- Domain does not explain individual problem solutions.
- Area does not duplicate detailed Topic definitions or Scenario investigations.
- Topic does not retell Scenario narratives or reveal their answers prematurely.
- Scenario does not need to re-teach the entire parent hierarchy.

Links and concise summaries are preferred over copied explanations.

### Content CI

Content CI must enforce the deterministic structural invariant: every scenario under `experiences/` has the required Domain, Area, and Topic `README.md` chain.

Content CI does **not** attempt to judge whether an overview is pedagogically complete, whether prose is duplicated, or whether its child list is semantically excellent. Those remain review responsibilities.

The validator may enforce basic file presence and basic Markdown sanity. More semantic validation should only be added when real repository usage demonstrates a concrete need.

## Consequences

### Positive

- GitHub directory browsing becomes a usable learning/navigation experience.
- Learners receive context before entering increasingly specific content.
- The hierarchy becomes explicit and testable rather than implied by folders.
- The first scenario vertical slice can validate Domain → Area → Topic → Scenario end to end.

### Costs

- Adding the first scenario in a new branch of the taxonomy may require up to three overview files.
- Manual child navigation can become stale and requires review discipline.
- Contributors must understand the distinction between orientation, problem-space mapping, recognition models, and concrete scenarios.

These costs are acceptable for the repository-first MVP. Automation can evolve from observed pain rather than speculation.

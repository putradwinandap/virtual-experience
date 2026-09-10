# Experience Scenario Template

> This template defines the MVP scenario format for Virtual Experience. The metadata block is machine-readable and is intended to be validated automatically.

## Required YAML front matter

Every scenario must begin with YAML front matter using this minimal schema:

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
  - "locking"
---
```

### Required fields

- `title` — human-readable scenario title.
- `domain` — canonical top-level domain. MVP value: `programming`.
- `area` — canonical area/category under the domain, such as `concurrency`.
- `topic` — canonical primary topic, such as `race-condition`.
- `difficulty` — one of `beginner`, `intermediate`, or `advanced`.
- `provenance.type` — one of `real`, `adapted`, or `illustrative`.
- `concepts` — one or more canonical related concepts/tags.

### Optional contributor metadata

Contributor metadata is optional because Git history already records authorship and AI-generated seed scenarios should not need a fake identity.

When explicit attribution is useful:

```yaml
contributor:
  github: "username"
```

`contributor` means the person who submitted or authored the scenario. It does **not** by itself prove that the contributor personally experienced the incident.

### Provenance rules

- `real` — a human contributor explicitly states that the scenario is based on something they personally encountered.
- `adapted` — derived from real experience but generalized, anonymized, combined, or materially modified.
- `illustrative` — intentionally constructed to teach a known class of problem or edge case.

AI-generated scenarios must use `illustrative` unless a human contributor provides provenance supporting another classification.

Never invent first-hand attribution, company names, incident details, or contributor identities.

### Difficulty rules

Difficulty measures the prerequisite reasoning needed to understand the scenario, not the severity of the incident.

- `beginner` — understandable with domain fundamentals.
- `intermediate` — requires combining multiple concepts or components.
- `advanced` — requires significant system reasoning, trade-off analysis, concurrency/distribution/scale reasoning, or comparable domain complexity.

### Canonical values

Metadata values such as `domain`, `area`, `topic`, and `concepts` should use canonical kebab-case vocabulary defined by the project taxonomy. Avoid free-form variants such as `race_condition`, `Race Condition`, or `racecondition` when `race-condition` is the canonical term.

---

# Scenario title

## Context

Give the learner enough context to understand the environment without revealing the answer.

Consider including:

- what system or workflow they are dealing with
- their role
- relevant constraints
- what normal behavior looks like

Avoid unnecessary fictional detail that does not affect the problem.

## Situation

Describe what is happening now.

Place the learner inside the situation rather than explaining the underlying concept immediately.

## Symptoms

What can actually be observed before the root cause is known?

Examples include logs, user reports, unexpected data, latency, failed requests, inconsistent state, alerts, or surprising behavior.

## Your Task

What decision, investigation, or response should the learner consider?

Good prompts create a meaningful pause before the explanation.

Examples:

- What would you check first?
- Is the obvious fix sufficient?
- What would you do while production is still affected?
- What risks should you consider before changing the system?

## Investigation

Walk through useful reasoning and evidence.

Do not turn this into an artificial detective story. Focus on signals and checks that help someone recognize the pattern later.

## Root Cause

Explain the underlying mechanism accurately and connect it back to the observed symptoms.

When useful, include a timeline, small diagram, query, log excerpt, or code fragment.

## Possible Approaches

Describe relevant ways the situation could be handled.

There does not always need to be one universally correct solution.

## Trade-offs

Explain what each meaningful approach costs or risks.

Consider complexity, correctness, performance, contention, operability, maintainability, compatibility, cost, or user impact when relevant.

## What Could Go Wrong

Highlight traps, incomplete fixes, or second-order consequences.

This section is especially valuable for Virtual Experience because many practical lessons live in edge cases rather than happy paths.

## Takeaway

End with the recognition pattern the learner should carry into future situations.

Prefer something actionable over a generic summary.

Ask:

> If the learner encounters something similar six months from now, what should make them think, “I have seen this pattern before”?

## Related Concepts

Optional links to relevant topics or scenarios.

---

## Author checklist

Before submitting, check that:

- [ ] YAML front matter follows the required schema.
- [ ] Metadata uses canonical taxonomy values.
- [ ] The scenario teaches through a situation, not only a definition.
- [ ] The root cause is not unnecessarily spoiled at the beginning.
- [ ] Observable symptoms are separated from hindsight when possible.
- [ ] Technical claims are accurate to the best of your knowledge.
- [ ] Trade-offs are included when there is more than one reasonable approach.
- [ ] Provenance is honest.
- [ ] Confidential, private, or identifying information has been removed.
- [ ] AI-generated content is not presented as first-hand experience.
- [ ] The scenario provides meaningfully different exposure if the topic already has scenarios.

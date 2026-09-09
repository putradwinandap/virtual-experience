# Experience Scenario Template

> This template is intentionally explicit while the project validates its content model. Sections may evolve as real contributions reveal what works best.

## Suggested file header

```markdown
# Scenario title

- Topic: <topic>
- Domain: Programming / Software Engineering
- Category: <category>
- Provenance: Real experience | Adapted experience | Illustrative scenario
- Contributor: <name or GitHub handle, when applicable>
- Difficulty: <optional for now>
```

Do not claim `Real experience` unless a human contributor explicitly states that the scenario is based on something they encountered.

AI-generated scenarios must use `Illustrative scenario` by default.

---

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

- [ ] The scenario teaches through a situation, not only a definition.
- [ ] The root cause is not unnecessarily spoiled at the beginning.
- [ ] Observable symptoms are separated from hindsight when possible.
- [ ] Technical claims are accurate to the best of your knowledge.
- [ ] Trade-offs are included when there is more than one reasonable approach.
- [ ] Provenance is honest.
- [ ] Confidential, private, or identifying information has been removed.
- [ ] AI-generated content is not presented as first-hand experience.
- [ ] The scenario provides meaningfully different exposure if the topic already has scenarios.

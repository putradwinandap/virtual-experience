# Contributing to Virtual Experience

Thanks for helping build a shared library of practical exposure.

Virtual Experience is not only a collection of technical explanations. Contributions should help someone recognize, reason about, or prepare for situations they may later encounter in practice.

## Ways to contribute

You can contribute by:

- sharing a scenario you encountered
- submitting an anonymized/adapted version of an experience
- creating an illustrative scenario for an important edge case
- improving the technical accuracy of an existing scenario
- improving clarity or accessibility
- proposing taxonomy improvements
- helping review scenarios
- improving project documentation

## Before contributing a scenario

1. Search the repository for the topic.
2. Check whether a similar scenario already exists.
3. If the same concept exists but your situation has materially different context, symptoms, decisions, trade-offs, or consequences, it can still be valuable as a separate scenario.
4. Use [`EXPERIENCE_TEMPLATE.md`](EXPERIENCE_TEMPLATE.md) as the starting point.

## Provenance

Every scenario must be honest about its origin.

Choose one:

- **Real experience** — based on something you actually encountered.
- **Adapted experience** — based on real experience but anonymized, generalized, combined, or materially modified.
- **Illustrative scenario** — constructed to teach a real class of problem without claiming the incident actually happened.

AI-generated scenarios are **Illustrative scenario** by default.

Do not use AI to manufacture personal history, contributor attribution, production incidents, metrics, company details, or claims of first-hand experience.

## Privacy and confidentiality

Do not submit secrets, credentials, private customer information, personal data, proprietary source code, confidential company information, internal hostnames, sensitive logs, or anything you are not authorized to publish.

When sharing a real experience, anonymize details that are not necessary for the learning value.

If anonymization substantially changes the scenario, classify it as an adapted experience.

## Writing a useful scenario

Try to preserve what the problem looked like **before the answer was known**.

Useful scenarios commonly include:

- context
- observable situation and symptoms
- a decision point for the learner
- investigation/reasoning
- root cause
- possible approaches
- trade-offs
- traps or second-order effects
- a recognition-oriented takeaway

Avoid turning every contribution into a textbook article.

## Technical accuracy

Prefer precise claims over absolute claims.

If a solution depends on a database, framework, runtime, architecture, traffic pattern, or other constraint, state the relevant context.

A practical scenario can have multiple reasonable solutions. Explain trade-offs instead of forcing a universal answer when one does not exist.

## Contribution workflow

For now, use the normal GitHub workflow:

1. Create or identify an Issue when the contribution is substantial or needs discussion.
2. Make one coherent change.
3. Keep unrelated cleanup separate.
4. Open a pull request explaining what experience or project problem the change adds or improves.
5. Respond to technical/content review.

This workflow may evolve as the community grows.

## AI-assisted contributions

AI assistance is welcome for drafting, editing, research support, organization, or review.

The contributor remains responsible for:

- provenance
- technical accuracy
- privacy/confidentiality
- whether they have the right to publish the material
- reviewing generated claims before submission

AI should amplify experience, not fabricate it.

## Project-level contributions

If you are changing the content model, taxonomy, contribution rules, or project philosophy, read [`AGENTS.md`](AGENTS.md) and the relevant documents under `docs/` first.

Durable project decisions should be documented rather than existing only in a pull-request conversation.

## Current status

Virtual Experience is early-stage. Constructive proposals are welcome, and some conventions are intentionally still being validated through real contributions.

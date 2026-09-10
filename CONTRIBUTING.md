# Contributing to Virtual Experience

Thanks for helping build a shared library of practical exposure.

Virtual Experience is not only a collection of technical explanations. Contributions should help someone recognize, reason about, or prepare for situations they may later encounter in practice.

## Start here

Choose the smallest path that fits your contribution:

- **Small correction** — typo, broken link, precise technical correction, or small clarity improvement: a direct pull request is fine.
- **New experience/scenario** — search existing Topics and scenarios first. Open an Experience proposal Issue when placement, duplication, provenance, or scope would benefit from discussion; otherwise a well-scoped PR may proceed directly.
- **Tooling/documentation change** — a small fix can go directly to a PR. Open an Issue first when behavior or scope is not obvious.
- **Project-level change** — changes to philosophy, content architecture, taxonomy rules, licensing, contribution/governance rules, or repository-wide behavior must start with a Project-level proposal Issue before implementation.

The goal is not to require an Issue for every edit. Issues are for coordination and decisions; pull requests are for reviewable changes.

## Ways to contribute

You can contribute by:

- sharing a scenario you encountered
- submitting an anonymized/adapted version of an experience
- creating an illustrative scenario for an important edge case
- improving the technical accuracy of an existing scenario
- improving clarity or accessibility
- proposing taxonomy improvements
- helping review scenarios
- improving project documentation or tooling

## Before contributing a scenario

1. Search the repository for the topic.
2. Check whether a similar scenario already exists.
3. If the same concept exists but your situation has materially different context, symptoms, decisions, trade-offs, or consequences, it can still be valuable as a separate scenario.
4. Use [`EXPERIENCE_TEMPLATE.md`](EXPERIENCE_TEMPLATE.md) as the starting point.
5. If you are unsure where the scenario belongs, use the Experience proposal Issue form before writing the full contribution.

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

## Licensing your contribution

Virtual Experience uses different standard licenses for written content and software/tooling. See [`LICENSE.md`](LICENSE.md) for the canonical scope map.

By intentionally submitting a contribution for inclusion in the repository, you agree to license the submitted material under the license that applies to the material/path you are changing:

- written educational content and documentation: **CC BY 4.0**;
- software, validation tooling, tests, and repository automation: **Apache-2.0**.

A pull request that changes both kinds of material can therefore contain material under both licenses.

Only submit material that you have the right to license on these terms. Publicly visible material is not automatically free to copy. Be especially careful with third-party text, screenshots, images, proprietary code, datasets, trademarks, and incident reports.

No Contributor License Agreement (CLA) or Developer Certificate of Origin (DCO) sign-off is required at this stage.

License attribution and scenario provenance are separate. Being named as an author or contributor does not by itself mean you personally experienced the scenario, and choosing `real`, `adapted`, or `illustrative` does not establish copyright ownership.

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

## Validate relevant changes locally

Scenario structure and metadata are checked by the repository-owned validator. Run the same checks locally before opening a pull request that changes experiences, the schema/taxonomy, validator, or related tooling.

Requires Python 3.12+.

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_experiences.py
```

You can also validate one or more specific scenario files:

```bash
python scripts/validate_experiences.py experiences/programming/concurrency/race-condition/scenarios/oversold-inventory.md
```

The validator checks the accepted YAML metadata contract, canonical domain/area values, kebab-case taxonomy identifiers, provenance and difficulty vocabularies, scenario path consistency, and basic Markdown presence. It intentionally does not judge whether a personal experience is true or whether the content is pedagogically excellent; those remain review responsibilities.

Documentation-only changes outside the Content CI path filters may correctly have no Content CI run.

## Pull request contract

Contributions should go through pull requests so review happens before content becomes canonical:

1. Create or identify an Issue when the contribution needs coordination or prior project-level discussion.
2. Create a task-scoped branch in your fork or working repository.
3. Make one coherent change and keep unrelated cleanup separate.
4. Run relevant local validation.
5. Open a pull request into `main`, link the Issue when applicable, and explain the outcome being added or improved.
6. Complete the repository pull-request checklist honestly.
7. Wait for automated checks when the changed paths trigger them and respond to technical/content review.
8. Merge only after required review/checks are satisfied.

Do not treat direct changes to `main` as the normal contribution path.

Automated checks establish deterministic repository constraints only. Reviewers and contributors remain responsible for technical accuracy, provenance honesty, privacy/confidentiality, learning value, and whether submitted material can legally be published.

## AI-assisted contributions

AI assistance is welcome for drafting, editing, research support, organization, implementation, or review.

The contributor remains responsible for:

- provenance
- technical accuracy
- privacy/confidentiality
- whether they have the right to publish and license the material
- reviewing generated claims before submission

AI should amplify experience, not fabricate it. Accepted durable decisions must be written into repository source-of-truth artifacts rather than left only in AI/chat context.

## Project-level contributions

If you are changing the content model, taxonomy rules, contribution/governance rules, licensing model, project philosophy, or repository-wide behavior, read [`AGENTS.md`](AGENTS.md), [`GOVERNANCE.md`](GOVERNANCE.md), and the relevant documents under `docs/` first.

Open a Project-level proposal Issue before implementation. Durable project decisions should be documented rather than existing only in an Issue or pull-request conversation. Existing ADRs are historical; a changed decision should supersede the previous record rather than silently rewriting it.

## Governance and conduct

[`GOVERNANCE.md`](GOVERNANCE.md) defines the current lightweight decision model, maintainer responsibilities, `main` branch collaboration contract, and how governance should evolve from evidence.

The project expects respectful, constructive, professional collaboration. A formal Code of Conduct is deferred until the project can pair a recognized standard with a real reporting path and enforcement owner; see `GOVERNANCE.md` for the rationale.

## Current status

Virtual Experience is early-stage. The repository is preparing for a small external-contribution pilot. Constructive proposals are welcome, and additional process should be added only when real contributor evidence shows a recurring need.

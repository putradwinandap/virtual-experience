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

## Validate your scenario locally

Scenario structure and metadata are checked by the repository-owned validator. Run the same checks locally before opening a pull request.

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

## Contribution workflow

Contributions should go through pull requests so automated checks and review happen before content becomes canonical:

1. Create or identify an Issue when the contribution is substantial or needs discussion.
2. Create a task-scoped branch in your fork or working repository.
3. Make one coherent change and keep unrelated cleanup separate.
4. Run the local validation commands above.
5. Open a pull request into `main` explaining what experience or project problem the change adds or improves.
6. Wait for Content CI when the changed paths trigger it, and respond to technical/content review.
7. Merge only after required review/checks are satisfied.

Do not treat direct changes to `main` as the normal contribution path.

## AI-assisted contributions

AI assistance is welcome for drafting, editing, research support, organization, or review.

The contributor remains responsible for:

- provenance
- technical accuracy
- privacy/confidentiality
- whether they have the right to publish and license the material
- reviewing generated claims before submission

AI should amplify experience, not fabricate it.

## Project-level contributions

If you are changing the content model, taxonomy, contribution rules, licensing model, or project philosophy, read [`AGENTS.md`](AGENTS.md) and the relevant documents under `docs/` first.

Durable project decisions should be documented rather than existing only in a pull-request conversation.

## Current status

Virtual Experience is early-stage. Constructive proposals are welcome, and some conventions are intentionally still being validated through real contributions.

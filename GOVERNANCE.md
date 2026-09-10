# Governance

Virtual Experience uses lightweight maintainer governance while the project is early-stage.

The purpose of this document is to make participation and decision-making predictable without adding process before real contributor experience justifies it.

## Principles

1. **Repository is the source of truth.** Accepted project knowledge must live in repository artifacts, not only in chat, Issues, or pull-request discussion.
2. **Pull requests are the normal path into `main`.** Review happens before a contribution becomes canonical.
3. **Existing architecture is the default.** Normal content contributions use the accepted model rather than reopening settled project decisions.
4. **Durable changes require durable records.** Material changes to project philosophy, content architecture, taxonomy rules, licensing, contribution rules, or repository-wide behavior require explicit discussion and an appropriate source-of-truth update. Changes with meaningful long-term trade-offs should use an ADR.
5. **Process follows evidence.** New roles, approval layers, automation, or contributor requirements should solve observed recurring friction rather than hypothetical future problems.

## Maintainer responsibility

Maintainers are responsible for deciding what is accepted into the canonical repository.

Review should consider the kind of contribution being proposed. For experience content this includes structural validity, technical accuracy, provenance honesty, privacy/confidentiality, and learning value. Automated validation helps with deterministic repository rules but does not establish that an experience is true, technically excellent, or pedagogically useful.

Maintainers may ask for revisions, decline a proposal that conflicts with accepted project direction, or request that a project-level proposal be discussed before implementation.

At the current project stage there is no committee or voting system. If the maintainer model changes materially as participation grows, that should be documented as a new governance decision rather than assumed implicitly.

## Contribution decision boundaries

### Normal contributions

Normal contributions can proceed through the contribution workflow without reopening project architecture when they fit accepted rules. Examples include:

- a new scenario under an existing Topic;
- a materially distinct scenario for an existing concept;
- technical or editorial corrections;
- documentation improvements that do not change policy;
- tooling fixes that preserve accepted repository behavior.

Small, well-scoped corrections may go directly to a pull request. New scenarios and changes that benefit from classification or scope discussion should use an Issue first.

### Project-level proposals

Open an Issue before implementation when a proposal would materially change any of the following:

- project philosophy or MVP boundaries;
- Domain → Area → Topic → Scenario architecture;
- required scenario metadata or provenance semantics;
- canonical taxonomy rules;
- repository licensing;
- contribution or governance policy;
- repository-wide validation/CI behavior;
- source-of-truth responsibilities.

Accepted durable changes must update the canonical project documentation. When the change represents a long-lived decision with meaningful alternatives or trade-offs, add a new ADR. Existing ADRs are historical records: supersede them rather than silently rewriting their accepted rationale.

## Disagreement and ambiguity

Prefer evidence and repository principles over preference alone.

If a proposal is ambiguous, keep the existing accepted behavior until the discussion produces a reason to change it. Record unresolved questions as assumptions, review findings, or follow-up Issues when useful.

A pull request discussion is not itself a durable architecture decision. If review changes accepted project knowledge, move that result into the appropriate repository document before considering the work complete.

## `main` branch collaboration contract

The desired repository protection model is:

- pull requests are the normal path into `main`;
- prevent force pushes to `main`;
- prevent deletion of `main`;
- allow required review/check settings to remain proportional to the active maintainer count;
- do not globally require the current `Content CI` status while it remains path-filtered, because documentation-only pull requests may correctly have no Content CI run;
- if an always-required status check becomes desirable, first introduce a check that runs on every pull request or redesign the CI trigger so required-check behavior cannot leave valid PRs permanently waiting.

Repository rulesets are operational configuration. This document defines the intended collaboration contract even when account permissions or repository settings require the protection itself to be configured separately.

## AI-assisted work

AI assistance is welcome, but it does not transfer contributor responsibility.

Contributors remain responsible for the rights to submitted material, provenance, privacy/confidentiality, technical claims, and reviewing generated output. AI-generated experience content defaults to `illustrative` unless a human provides supported provenance for another classification.

AI agents working on the project follow `AGENTS.md`, including the principle:

> **Chat is temporary. Repository is memory.**

## Licensing

Incoming contributions follow the repository licensing model documented in `LICENSE.md` and ADR 0005. Written educational content/documentation uses CC BY 4.0; software/tooling uses Apache-2.0.

No CLA or DCO is required at the current stage. Additional contributor agreements should be introduced only if a concrete future need justifies them.

## Community conduct

The project expects respectful, constructive, professional collaboration.

A formal Code of Conduct is intentionally deferred for this baseline because the project does not yet have a dedicated private reporting channel or an established moderation/enforcement structure. Adopting a standard code while leaving its reporting and enforcement placeholders unresolved would create an incomplete promise to contributors.

Before broader public recruitment or when the external-contribution pilot demonstrates the need, evaluate adoption of a recognized standard such as Contributor Covenant together with a real reporting path and enforcement owner.

## Evolution

This governance baseline is deliberately small. The next test is a limited external-contribution pilot.

Capture real friction from that pilot. Add process only when repeated evidence shows that the current model is insufficient.

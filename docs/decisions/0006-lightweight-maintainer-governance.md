# ADR 0006 — Lightweight maintainer governance for community readiness

- Status: Accepted
- Date: 2026-09-10

## Context

Virtual Experience has validated its initial content architecture across four seed vertical slices and established explicit licensing. The next useful evidence should come from external contribution rather than more internally generated architecture.

External contributors need predictable entry points and decision boundaries, but the project is still small. Introducing committees, voting systems, mandatory Issue ceremony, contributor agreements, or complex automation before observing contributor friction would conflict with the project's evidence-driven approach.

The repository also has a path-filtered `Content CI` workflow. Some valid pull requests, especially documentation/governance changes, intentionally do not receive that check. This matters when describing future branch protection: a status check that does not run on every pull request must not be configured as an unconditional globally required check.

## Decision

Adopt a lightweight maintainer governance baseline for the current stage.

### Contribution entry points

- Pull requests are the normal path into `main`.
- Small, well-scoped corrections may go directly to a pull request without a pre-existing Issue.
- New experiences should use Issue-first discussion when Topic placement, duplication, provenance, or scope is uncertain.
- Project-level changes must start with an Issue before implementation.

Project-level changes include material changes to project philosophy, content architecture, taxonomy rules, licensing, contribution/governance rules, source-of-truth responsibilities, or repository-wide validation behavior.

### Decision authority

Maintainers decide what is accepted into the canonical repository.

Normal contributions follow accepted architecture by default. A pull request is not a mechanism for silently reopening settled project decisions.

When a project-level proposal is accepted, durable knowledge must be moved into the appropriate repository source of truth. Decisions with meaningful long-term alternatives/trade-offs use a new ADR. Historical ADRs are superseded rather than silently rewritten.

### Review responsibility

Automated checks establish deterministic repository constraints only. They do not prove provenance truthfulness, technical excellence, privacy safety, rights to submitted material, or learning value. Contributors and maintainers remain responsible for those review dimensions.

### Repository protection contract

The intended `main` branch contract is PR-first collaboration with force pushes and branch deletion prevented where practical. Review requirements should remain proportional to the active maintainer count.

The current path-filtered `Content CI` must not be globally required for every pull request. If the project later wants an always-required status check, it should first introduce an always-running check or redesign workflow triggers so valid pull requests cannot be blocked by an absent check.

### AI-assisted contributions

AI assistance is allowed for drafting, research support, implementation, editing, and review. Human contributors remain responsible for rights, provenance, privacy/confidentiality, and submitted claims. AI-generated experience content defaults to `illustrative` unless supported human provenance establishes otherwise.

Accepted project knowledge must live in repository artifacts; chat/agent context is not a durable decision record.

### Code of Conduct

Do not add a formal Code of Conduct in this baseline yet.

The project expects respectful and constructive collaboration, but a formal conduct policy should be paired with a real reporting channel and enforcement owner. Publishing a standard document with unresolved enforcement/reporting placeholders would create an incomplete governance promise.

When public participation expands or the external pilot demonstrates a need, prefer evaluating a recognized standard such as Contributor Covenant rather than inventing a custom code.

## Alternatives considered

### Require an Issue for every pull request

Rejected. This adds ceremony to small corrections without improving decision quality.

### Add committees or voting now

Rejected. The project does not yet have enough maintainers or governance conflicts to justify those mechanisms.

### Require CLA or DCO

Rejected. ADR 0005 already selected a lightweight inbound=outbound licensing model, and no new evidence justifies additional contributor agreements.

### Require Content CI globally

Rejected while the workflow is path-filtered. Pull requests outside its paths can correctly receive no run, which would make an unconditional required check operationally unsafe.

### Add a formal Code of Conduct immediately

Deferred rather than rejected permanently. A recognized standard is preferable once the project can provide an actual reporting and enforcement path.

## Consequences

### Positive

- New contributors have explicit entry paths without excessive ceremony.
- Maintainer authority and project-level decision boundaries are visible.
- Small fixes remain low-friction.
- Durable decisions stay repository-resident and AI-operable.
- Branch-protection guidance accounts for actual CI trigger behavior.
- Governance can evolve from external-contributor evidence.

### Costs and risks

- Maintainer decision authority is centralized at the current stage.
- Some judgment remains human, especially scenario classification and learning quality.
- A formal conduct/reporting framework is not yet present and must be revisited before broader community growth makes it necessary.
- Operational GitHub branch protection still requires repository settings to match the documented contract.

## Follow-up

Run a small external-contribution pilot. Record concrete friction in contributor discovery, Topic/Scenario placement, provenance/privacy, metadata, validation, review, licensing, and GitHub workflow. Use that evidence to decide which community-readiness improvements are actually needed next.

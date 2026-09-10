# Current State

Last updated: 2026-09-10

## Status

Virtual Experience has completed its initial repository/content foundation and is entering **Phase 2 — Community readiness**.

The accepted content model has been exercised across four materially different vertical slices, passed its first evidence-based architecture review without requiring expansion, has an explicit dual-license model, and now has a lightweight contribution/governance baseline for public participation.

The next evidence source should be a small external-contribution pilot rather than more speculative process or architecture work.

## Accepted direction

- Project name: **Virtual Experience**
- Tagline: **Experience problems before they become your problems.**
- Core principle: **Virtual Experience does not replace real experience. It prepares you for it.**
- Initial domain: programming/software engineering
- Initial product: open-source GitHub repository using Markdown
- Content hierarchy: Domain → Area → Topic → Scenario
- Every instantiated Domain, Area, and Topic requires a `README.md` overview
- Hierarchy responsibilities are progressive: Domain orients, Area maps a concern space, Topic builds problem-pattern recognition, Scenario provides concrete experience
- Overview pages surface children that actually exist rather than presenting aspirational catalogs as available content
- Overview prose remains flexible; exact Markdown headings are not a schema
- Primary content unit: concrete scenario under a broader topic
- Same topic may contain multiple materially different scenarios from different contributors
- Scenario metadata uses minimal YAML front matter
- Required metadata: `title`, `domain`, `area`, `topic`, `difficulty`, `provenance.type`, and `concepts`
- Provenance vocabulary: `real`, `adapted`, `illustrative`
- AI-generated scenarios default to `illustrative` and must not be presented as real first-hand experiences
- Explicit `contributor.github` metadata is optional; Git history remains the baseline authorship record
- Difficulty vocabulary: `beginner`, `intermediate`, `advanced`, measuring prerequisite reasoning rather than incident severity
- Canonical taxonomy identifiers use lowercase kebab-case
- Experience metadata, path rules, and required overview chain are enforced by a repository-owned Python validator
- GitHub Actions runs validator tests and experience validation on relevant pull requests
- Content CI remains deterministic and path-filtered; semantic truth, provenance truthfulness, overview/navigation quality, and pedagogical quality remain review responsibilities
- Written educational content and documentation are licensed under **CC BY 4.0**
- Software, validation tooling, tests, and repository automation are licensed under **Apache-2.0**
- Incoming contributions use the applicable repository license without an additional CLA/DCO at this stage
- License attribution and scenario provenance remain distinct concepts
- Pull requests are the normal path into `main`; small corrections do not require a pre-existing Issue
- New experiences use Issue-first discussion when placement, duplication, provenance, or scope is uncertain
- Durable project-level changes require Issue-first discussion and source-of-truth updates; meaningful long-lived trade-offs use ADRs
- Maintainers decide what enters the canonical repository under the lightweight governance model
- A formal Code of Conduct is deferred until it can be paired with a real reporting path and enforcement owner
- Dedicated web platform remains deferred until repository/content limitations justify it
- Repository documentation is the durable project memory for human and AI contributors

## Repository source-of-truth model

Important locations:

- `AGENTS.md` — AI operating contract
- `README.md` — public project overview
- `GOVERNANCE.md` — maintainer responsibility, decision boundaries, and repository collaboration contract
- `LICENSE.md` — canonical licensing scope map
- `LICENSE-CONTENT` — CC BY 4.0 content-license notice/reference
- `LICENSE-CODE` — Apache-2.0 software license text
- `EXPERIENCE_TEMPLATE.md` — canonical scenario authoring/schema reference
- `CONTRIBUTING.md` — contributor entry points, licensing, review, and local validation guidance
- `.github/PULL_REQUEST_TEMPLATE.md` — lightweight PR contract/checklist
- `.github/ISSUE_TEMPLATE/` — focused experience and project-level proposal entry points
- `scripts/validate_experiences.py` — executable scenario and hierarchy validation rules
- `.github/workflows/content-ci.yml` — path-filtered automated pull-request quality gate
- `docs/project/` — stable project concepts and taxonomy
- `docs/planning/` — MVP and roadmap
- `docs/decisions/` — durable decisions and rationale
- `docs/reviews/` — evidence-based project/model reviews
- `docs/context/` — current state, assumptions, and unresolved context
- GitHub Issues — executable units of work and pre-implementation discussion when needed
- Git history — implementation/change history

## Completed seed vertical slices

1. Programming → Concurrency → Race Condition
2. Programming → API & Integration → Idempotency
3. Programming → Databases → Unsafe Database Migration
4. Programming → Security → Broken Authorization

Together, these slices exercised the same architecture across concurrency, distributed/API behavior, database operations, and application security without requiring domain-specific schema expansion.

## First content-model review

The first review is recorded in `docs/reviews/mvp-content-model-review.md`.

Key conclusion: **keep the MVP content architecture as-is.**

Validated decisions include the four-level hierarchy, required overview chain, flexible overview prose, scenario learning journey, multiple scenarios per Topic, minimal metadata, manual navigation at current scale, deterministic Content CI, the AI operating contract, and repository-first delivery.

Observed friction that needs external evidence rather than immediate architecture changes includes `concepts` vocabulary drift, Topic-versus-Scenario classification for newcomers, and the human contribution workflow.

## Licensing decision

ADR 0005 establishes a dual-license repository model:

- CC BY 4.0 for written educational content and documentation;
- Apache-2.0 for software/tooling and repository automation.

`LICENSE.md` defines the path/material scope. Contributors intentionally submitting material for inclusion use the applicable license. No CLA or DCO is required at the current stage.

Third-party material is not automatically relicensed, and copyright/license attribution must not be confused with `real`, `adapted`, or `illustrative` scenario provenance.

## Contribution and governance baseline

`GOVERNANCE.md` defines the current lightweight decision model. It intentionally avoids committees, voting systems, and additional contributor agreements while the project has no evidence that they are needed.

The contributor journey distinguishes small direct-PR corrections, new experience proposals, normal tooling/documentation work, and project-level proposals. Focused GitHub Issue forms and a PR checklist support those paths without requiring an Issue for every edit.

The desired `main` protection contract is documented: PR-first collaboration, no force pushes/deletion, and review/check requirements proportional to the maintainer model. The current Content CI must not be globally required while it remains path-filtered because valid documentation-only PRs can have no run. No repository ruleset was present when this baseline was reviewed; branch-protection details could not be read through the connected GitHub integration, so operational protection remains a separate repository-setting task.

A formal Code of Conduct is deferred for now. The project should prefer a recognized standard such as Contributor Covenant when it can also provide a real reporting path and enforcement owner rather than publishing unresolved placeholders.

## Current priorities

1. Run a small external-contribution pilot using the new contribution/governance entry points.
2. Capture concrete contributor friction: discovery, Topic-versus-Scenario placement, provenance/privacy, `concepts`, validation, review, licensing, and GitHub workflow.
3. Refine taxonomy, validator, navigation, licensing guidance, governance, or authoring guidance only when pilot evidence demonstrates a recurring need.
4. Configure/verify operational `main` branch protection separately against the documented collaboration contract.
5. Revisit the content model only after meaningful new evidence accumulates.

## Known open questions

- How should real experiences be anonymized without removing useful context?
- When does a scenario deserve its own Topic versus belonging under an existing Topic, especially for independent contributors?
- Will `concepts` remain coherent as multiple contributors introduce vocabulary?
- What contribution, review, repository-governance, or licensing friction becomes visible during the external-contribution pilot?
- When should a recognized Code of Conduct be adopted, and what reporting/enforcement path should support it?
- When does repository content volume create enough navigation/discovery pressure to justify generated tooling or a dedicated interface?

## Recent durable decisions

- ADR 0001 — repository-first MVP
- ADR 0002 — topic/scenario content model
- ADR 0003 — minimal YAML front matter for scenario metadata
- ADR 0004 — hierarchical overview pages for instantiated Domain, Area, and Topic nodes
- MVP content-model review — no architecture change justified after the first four vertical slices
- ADR 0005 — dual-license written content under CC BY 4.0 and software/tooling under Apache-2.0
- Lightweight governance baseline — maintainers accept canonical changes; normal contributions follow accepted architecture; project-level changes require explicit discussion and durable repository updates; process grows from contributor evidence

## Maintenance rule

Update this document whenever project state, accepted direction, or immediate priorities materially change.

Do not use this file as a detailed changelog. Commits and pull requests already serve that purpose.

# Current State

Last updated: 2026-09-10

## Status

Virtual Experience is in **Phase 0 — Foundation**. The accepted content model has now been exercised across four materially different repository vertical slices and completed its first evidence-based architecture review.

The review found no evidence that justifies changing the Domain → Area → Topic → Scenario hierarchy, required scenario metadata, overview-page model, deterministic Content CI boundary, or repository-first MVP architecture.

The project is ready to shift its next evidence source from internally produced seed content toward broader sharing and external contribution.

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
- Content CI remains deterministic; semantic truth, provenance truthfulness, overview/navigation quality, and pedagogical quality remain review responsibilities
- Dedicated web platform remains deferred until repository/content limitations justify it
- Repository documentation is the durable project memory for human and AI contributors

## Repository source-of-truth model

Important locations:

- `AGENTS.md` — AI operating contract
- `README.md` — public project overview
- `EXPERIENCE_TEMPLATE.md` — canonical scenario authoring/schema reference
- `CONTRIBUTING.md` — contribution and local validation guidance
- `scripts/validate_experiences.py` — executable scenario and hierarchy validation rules
- `.github/workflows/content-ci.yml` — automated pull-request quality gate
- `docs/project/` — stable project concepts and taxonomy
- `docs/planning/` — MVP and roadmap
- `docs/decisions/` — durable decisions and rationale
- `docs/reviews/` — evidence-based project/model reviews
- `docs/context/` — current state, assumptions, and unresolved context
- GitHub Issues — executable units of work
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

## Current priorities

1. Resolve the repository licensing model before actively encouraging broader reuse and contribution.
2. Prepare the repository contribution/governance baseline for public participation without adding unnecessary process.
3. Run a small external-contribution pilot and capture concrete contributor friction as the next evidence source.
4. Refine taxonomy, validator, navigation, or authoring guidance only when that evidence demonstrates a recurring need.
5. Revisit the content model only after meaningful new evidence accumulates rather than after an arbitrary number of additional Topics.

## Known open questions

- Which license model best fits contributed written content and future supporting software/tooling?
- How should real experiences be anonymized without removing useful context?
- When does a scenario deserve its own Topic versus belonging under an existing Topic, especially for independent contributors?
- Will `concepts` remain coherent as multiple contributors introduce vocabulary?
- What contribution, review, or repository-governance friction becomes visible once people outside the initial maintainer workflow begin contributing?
- When does repository content volume create enough navigation/discovery pressure to justify generated tooling or a dedicated interface?

## Recent durable decisions

- ADR 0001 — repository-first MVP
- ADR 0002 — topic/scenario content model
- ADR 0003 — minimal YAML front matter for scenario metadata
- ADR 0004 — hierarchical overview pages for instantiated Domain, Area, and Topic nodes
- MVP content-model review — no architecture change justified after the first four vertical slices

## Maintenance rule

Update this document whenever project state, accepted direction, or immediate priorities materially change.

Do not use this file as a detailed changelog. Commits and pull requests already serve that purpose.

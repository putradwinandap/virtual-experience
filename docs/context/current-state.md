# Current State

Last updated: 2026-09-10

## Status

Virtual Experience is in **Phase 0 — Foundation**, with the content model now being exercised through real repository vertical slices.

The repository has a defined Domain → Area → Topic → Scenario content model, accepted MVP scenario metadata, hierarchical overview rules, deterministic Content CI enforcement, and a completed Race Condition seed topic with two materially different illustrative scenarios. The current content expansion is Idempotency under API & Integration.

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
- Content CI is deterministic; semantic truth, provenance truthfulness, overview quality/navigation quality, and pedagogical quality remain review responsibilities
- Dedicated web platform is intentionally deferred until repository/content limitations justify it
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
- `docs/context/` — current state, assumptions, and unresolved context
- GitHub Issues — executable units of work
- Git history — implementation/change history

## Current priorities

1. Exercise the accepted content model with additional materially different vertical slices rather than expanding the schema speculatively.
2. Complete Issue #9: add API & Integration and Idempotency overviews plus two materially distinct illustrative idempotency scenarios.
3. Continue with the planned Unsafe Database Migration and Broken Authorization seed topics to test the model across different engineering areas.
4. Review the content model after several topics expose enough concrete authoring and navigation friction to justify changes.
5. Refine validator strictness only when real content exposes a concrete need.
6. Choose a license appropriate for a repository centered on contributed written content plus supporting code/tooling.

## Known open questions

- Which license model best fits contributed written content and future supporting software/tooling?
- How should real experiences be anonymized without removing useful context?
- When does a scenario deserve its own topic versus belonging under an existing topic?
- Which metadata additions, if any, become justified after real contributions exist?
- How strict should Markdown section validation become after more seed scenarios exercise the learning model?
- When, if ever, should manually maintained overview child navigation become generated navigation?

## Recent durable decisions

- ADR 0001 — repository-first MVP
- ADR 0002 — topic/scenario content model
- ADR 0003 — minimal YAML front matter for scenario metadata
- ADR 0004 — hierarchical overview pages for instantiated Domain, Area, and Topic nodes

## Maintenance rule

Update this document whenever project state, accepted direction, or immediate priorities materially change.

Do not use this file as a detailed changelog. Commits and pull requests already serve that purpose.

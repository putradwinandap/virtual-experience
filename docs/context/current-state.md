# Current State

Last updated: 2026-09-10

## Status

Virtual Experience is in **Phase 0 — Foundation**.

The repository now has a defined Domain → Area → Topic → Scenario content model, accepted MVP scenario metadata, hierarchical overview rules, and deterministic Content CI enforcement. The next vertical slice is to exercise that foundation with the first race-condition topic and seed scenarios.

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

1. Complete Issue #6 and establish hierarchical overview pages as an enforced content invariant.
2. Resume Issue #2: add Programming, Concurrency, and Race Condition overviews plus at least two materially distinct illustrative race-condition scenarios.
3. Use that vertical slice to validate the full Domain → Area → Topic → Scenario learning/navigation model and Content CI against real repository content.
4. Refine validator strictness only when real content exposes a concrete need.
5. Choose a license appropriate for a repository centered on contributed written content plus supporting code/tooling.

## Known open questions

- Which license model best fits contributed written content and future supporting software/tooling?
- How should real experiences be anonymized without removing useful context?
- When does a scenario deserve its own topic versus belonging under an existing topic?
- Which metadata additions, if any, become justified after real contributions exist?
- How strict should Markdown section validation become after the first seed scenarios exercise the learning model?
- When, if ever, should manually maintained overview child navigation become generated navigation?

## Recent durable decisions

- ADR 0001 — repository-first MVP
- ADR 0002 — topic/scenario content model
- ADR 0003 — minimal YAML front matter for scenario metadata
- ADR 0004 — hierarchical overview pages for instantiated Domain, Area, and Topic nodes

## Maintenance rule

Update this document whenever project state, accepted direction, or immediate priorities materially change.

Do not use this file as a detailed changelog. Commits and pull requests already serve that purpose.

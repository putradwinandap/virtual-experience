# Current State

Last updated: 2026-09-10

## Status

Virtual Experience is in **Phase 0 — Foundation**.

The repository has just been initialized as the durable source of truth for the project.

## Accepted direction

- Project name: **Virtual Experience**
- Tagline: **Experience problems before they become your problems.**
- Core principle: **Virtual Experience does not replace real experience. It prepares you for it.**
- Initial domain: programming/software engineering
- Initial product: open-source GitHub repository using Markdown
- Primary content unit: concrete scenario under a broader topic
- Same topic may contain multiple materially different scenarios from different contributors
- AI-generated scenarios must not be presented as real first-hand experiences
- Dedicated web platform is intentionally deferred until repository/content limitations justify it
- Repository documentation is the durable project memory for human and AI contributors

## Repository source-of-truth model

The repository should contain durable knowledge rather than depending on individual chat sessions.

Important locations:

- `AGENTS.md` — AI operating contract
- `README.md` — public project overview
- `docs/project/` — stable project concepts
- `docs/planning/` — MVP and roadmap
- `docs/decisions/` — durable decisions and rationale
- `docs/context/` — current state, assumptions, and unresolved context
- GitHub Issues — executable units of work
- Git history — implementation/change history

## Current priorities

1. Finalize `EXPERIENCE_TEMPLATE.md`.
2. Finalize `CONTRIBUTING.md`.
3. Choose an open-source license.
4. Create the first project Issues.
5. Add seed scenarios, starting with programming/software engineering.
6. Validate whether the proposed scenario structure feels useful rather than tutorial-like.

## Known open questions

- Which open-source license best fits the repository, especially because it primarily contains contributed written content rather than only software?
- What minimum metadata should every scenario carry?
- Should contributor attribution live in front matter, a visible section, Git history, or a combination?
- What difficulty model, if any, should be used?
- How should real experiences be anonymized without removing the context that makes them useful?
- When does a scenario deserve its own topic versus belonging under an existing topic?
- What initial seed scenarios provide the best demonstration of the project's value?

## Maintenance rule

Update this document whenever project state, accepted direction, or immediate priorities materially change.

Do not use this file as a detailed changelog. Commits and pull requests already serve that purpose.

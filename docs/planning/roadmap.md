# Roadmap

Status: **Living document**

The roadmap describes direction, not a promise of dates.

## Phase 0 — Foundation

Goal: make the repository understandable and operable by both humans and AI agents.

- [x] Define project vision, mission, and principles
- [x] Define AI agent operating rules
- [x] Define initial experience model
- [x] Define initial taxonomy
- [x] Define MVP boundaries
- [x] Establish an experience template and executable metadata contract
- [x] Establish initial contribution guidance
- [x] Choose repository licensing model
- [x] Establish an initial GitHub Issue-driven workflow/backlog

## Phase 1 — Seed experiences

Goal: prove the content format with actual scenarios.

Completed seed Topics:

- race condition
- payment retry / idempotency
- unsafe database migration
- broken authorization

The seed set includes multiple materially different scenarios under Topics and exercises the accepted model across concurrency, API/integration behavior, databases, and security.

The first evidence-based content-model review concluded that no architecture change is currently justified.

## Phase 2 — Community readiness

Goal: make contributing understandable and low-friction.

Current direction:

- establish a lightweight contribution/governance baseline
- provide focused Issue and pull-request entry points without requiring an Issue for every edit
- keep Content CI deterministic and distinguish automated validation from human review responsibility
- run a small external-contribution pilot
- capture real contributor friction before adding more process
- refine anonymization/privacy guidance, taxonomy guidance, review checklists, or navigation only when pilot evidence demonstrates a recurring need

Do not add contributor bureaucracy merely to look mature. Community process should grow from observed participation.

## Phase 3 — Validate demand

Goal: learn how people actually consume and contribute to the library.

Observe:

- which scenarios are most useful
- how people discover topics
- where Markdown navigation becomes painful
- which content structures confuse contributors
- what learners want to do that GitHub cannot support well

Do not build a platform merely because one is possible.

## Phase 4 — Experience platform exploration

Only after a clear need emerges, evaluate a dedicated interface.

Possible capabilities:

- searchable scenario catalog
- filters by topic, difficulty, role, or provenance
- progressive reveal of scenario solutions
- decision-based learning flows
- contributor profiles
- scenario relationships
- interactive simulations
- optional AI-guided discussion

These are hypotheses, not committed features.

## Phase 5 — Beyond programming

If the content model proves transferable, experiment with other fields where scenario exposure is valuable.

Any new domain should have contributors with relevant knowledge and should preserve the project's honesty about the limits of simulated experience.

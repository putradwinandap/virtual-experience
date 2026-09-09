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
- [ ] Finalize experience template
- [ ] Finalize contribution guide
- [ ] Choose open-source license
- [ ] Establish initial GitHub Issue backlog

## Phase 1 — Seed experiences

Goal: prove the content format with actual scenarios.

Candidate seed topics:

- race condition
- payment retry / idempotency
- unsafe database migration
- broken authorization
- accidental force push
- N+1 query
- flaky tests
- cache stampede

Important validation target: at least one topic should contain multiple materially different scenarios.

## Phase 2 — Community readiness

Goal: make contributing understandable and low-friction.

Potential work:

- refine contribution workflow from real contributor feedback
- add issue/PR templates if useful
- define scenario metadata only after learning what is needed
- add content review checklist
- improve navigation/indexing
- document anonymization and privacy guidance for real experiences

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

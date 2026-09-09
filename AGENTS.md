# AGENTS.md

## Purpose

This file defines the default operating rules for AI agents working on Virtual Experience.

Treat the repository as the durable source of truth. Do not rely on chat memory for accepted project decisions.

## Project

Virtual Experience is an open-source library of real-world scenarios, edge cases, failures, decisions, and lessons designed to give people earlier exposure to situations they may encounter in practice.

The project starts with programming/software engineering and may expand into other fields over time.

### Core principle

**Virtual Experience does not replace real experience. It prepares you for it.**

Virtual Experience helps people build recognition and mental models before they encounter similar situations in the real world.

### Tagline

**Experience problems before they become your problems.**

## AI-native principle

**Chat is temporary. Repository is memory.**

When a discussion produces durable knowledge, convert it into the appropriate repository artifact before considering the work complete.

This repository is intended to be highly AI-operable. Any capable AI agent should be able to understand the project direction, current state, accepted decisions, and contribution rules by reading the repository.

## Source of truth map

- Project introduction: `README.md`
- Vision, mission, and principles: `docs/project/vision.md`
- Experience model and schema: `docs/project/experience-model.md`
- Taxonomy: `docs/project/taxonomy.md`
- Current project state: `docs/context/current-state.md`
- Assumptions and unresolved questions: `docs/context/assumptions.md`
- Roadmap: `docs/planning/roadmap.md`
- MVP boundaries: `docs/planning/mvp.md`
- Durable decisions: `docs/decisions/`
- Contributor guide: `CONTRIBUTING.md`
- Experience template: `EXPERIENCE_TEMPLATE.md`
- Executable work: GitHub Issues
- Change history: commits and pull requests

## Required agent workflow

Before starting work:

1. Read this file.
2. Read `docs/context/current-state.md`.
3. Read the GitHub Issue for the task, if one exists.
4. Read only the project documents relevant to the task.
5. Inspect existing repository content before proposing changes.

During work:

1. Do not invent accepted requirements when the repository is ambiguous.
2. Prefer the smallest coherent change that advances the project.
3. Preserve the distinction between facts, contributor experiences, illustrative scenarios, assumptions, and editorial interpretation.
4. Do not silently change project philosophy, taxonomy, or experience format.
5. Avoid unnecessary duplication of knowledge across documents.
6. Keep content clear enough for newcomers while retaining technical accuracy.
7. Never fabricate attribution, contributor identity, production incidents, metrics, company names, or claims of first-hand experience.

Before finishing work:

1. Verify the task against its acceptance criteria when available.
2. Update documentation when accepted project knowledge changes.
3. Update `docs/context/current-state.md` when project state materially changes.
4. Add a decision record when making a durable project/content architecture decision with meaningful trade-offs.
5. Keep commits scoped and descriptive.
6. Summarize what changed and any unresolved questions.

## Experience content rules

Virtual Experience is not a conventional tutorial collection.

An experience should prioritize **situational exposure and reasoning** over merely explaining a concept.

A strong scenario should usually communicate:

1. Context
2. Situation
3. Symptoms or observable signals
4. The learner's task or decision point
5. Investigation or reasoning path
6. Root cause or underlying mechanism
7. Possible approaches
8. Trade-offs and consequences
9. What could go wrong
10. Takeaway / recognition pattern

Not every scenario must rigidly use every heading, but the learning journey should preserve this intent.

## Provenance and honesty rules

Content may come from different provenance types. They must not be conflated.

- **Real experience** — contributed from something a person actually encountered.
- **Adapted experience** — based on one or more real experiences but anonymized or generalized.
- **Illustrative scenario** — constructed to teach a known class of problem and not claimed as a real incident.

AI-generated scenarios must default to **illustrative scenario** unless a human contributor explicitly provides provenance supporting another classification.

AI must never present generated content as something a named contributor personally experienced.

## Duplicate-topic rule

Do not collapse distinct experiences merely because they share the same underlying concept.

For example, `race-condition` may contain multiple scenarios involving inventory, payments, counters, job workers, or distributed systems.

The topic represents the concept. Scenarios represent concrete manifestations of that concept.

## Documentation rules

- Do not copy raw chat transcripts into the repository.
- Distill discussions into accepted decisions, principles, assumptions, issues, or project-state updates.
- Avoid duplicating the same source of truth across multiple documents.
- If documents conflict, surface the conflict rather than choosing silently.
- Date project-state documents when materially updating them.
- Decision records are historical. If a durable decision changes, supersede it rather than silently rewriting the old rationale.

## Git and task rules

- One Issue should describe one coherent outcome whenever practical.
- Branches should be task-scoped when branches are used.
- Pull requests should reference their Issue when applicable.
- Do not mix unrelated cleanup with feature/content work.
- Do not consider generated content complete until it has been checked against the repository's content and provenance rules.

# Virtual Experience

> **Experience problems before they become your problems.**

Virtual Experience is an open-source library of real-world scenarios, edge cases, failures, decisions, and lessons designed to help people gain exposure to situations they may encounter in practice.

The project starts with programming and software engineering. In the future, the same model may expand into other fields where practical experience, uncertainty, edge cases, and decision-making matter.

## Why

Learning a concept and recognizing it in a real situation are different skills.

A developer may understand the definition of a race condition without ever having seen two customers purchase the last item at nearly the same time. A newcomer may know what an API timeout is without having considered what happens when a payment succeeds but its response never reaches the application.

Virtual Experience exists to reduce that exposure gap.

It does **not** claim to replace real experience. Real environments contain complexity, pressure, incomplete information, people, legacy systems, organizational constraints, and consequences that cannot be fully reproduced in Markdown.

Instead, Virtual Experience helps learners build mental models and recognition patterns earlier.

> **Virtual Experience does not replace real experience. It prepares you for it.**

## How it works

Knowledge is organized around topics and concrete scenarios.

For example:

```text
Race Condition
├── Scenario 1: Oversold inventory
├── Scenario 2: Duplicate processing
└── Scenario 3: Lost update
```

Two contributors may encounter the same underlying concept in very different circumstances. Those experiences should remain distinct scenarios when their context, symptoms, decisions, or consequences provide different learning value.

A scenario is intended to place the learner inside a situation rather than merely define a concept. It can walk through context, symptoms, investigation, decision points, root cause, possible approaches, trade-offs, consequences, and takeaways.

## Initial scope

The MVP is intentionally simple:

- GitHub repository
- Markdown-first experiences
- Programming/software engineering as the initial domain
- Community contributions through GitHub
- Multiple scenarios per topic
- A shared experience format and taxonomy

A dedicated web application may come later. The repository and content model come first.

## Example structure

```text
experiences/
└── programming/
    └── concurrency/
        └── race-condition/
            ├── README.md
            └── scenarios/
                ├── oversold-inventory.md
                └── lost-update.md
```

## Content provenance

Virtual Experience values honesty about where scenarios come from. A scenario can be classified as:

- **Real experience** — based on something a contributor actually encountered.
- **Adapted experience** — derived from real experience but anonymized or generalized.
- **Illustrative scenario** — intentionally constructed to teach a real class of problem without claiming that the incident actually happened to the author.

AI-generated scenarios are illustrative by default unless a human contributor provides real provenance.

## Contributing

Contributions are welcome. You can contribute a new scenario, improve an existing experience, clarify technical reasoning, or help evolve the project itself.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`EXPERIENCE_TEMPLATE.md`](EXPERIENCE_TEMPLATE.md).

## Project documentation

Project direction and durable context live in the repository so humans and AI agents can work from the same source of truth.

Start with:

- [`AGENTS.md`](AGENTS.md) — rules for AI agents
- [`docs/project/vision.md`](docs/project/vision.md) — vision, mission, and principles
- [`docs/project/experience-model.md`](docs/project/experience-model.md) — how experiences are modeled
- [`docs/project/taxonomy.md`](docs/project/taxonomy.md) — initial content taxonomy
- [`docs/planning/mvp.md`](docs/planning/mvp.md) — MVP boundaries
- [`docs/planning/roadmap.md`](docs/planning/roadmap.md) — project roadmap
- [`docs/context/current-state.md`](docs/context/current-state.md) — current state and next priorities
- [`docs/decisions/`](docs/decisions/) — durable project decisions

## License

A license has not been selected yet. See the current project state for this unresolved decision.

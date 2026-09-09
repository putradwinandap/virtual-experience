# Assumptions and Open Questions

Last updated: 2026-09-10

This document stores project assumptions that are useful for planning but are **not yet durable decisions**.

When an assumption becomes accepted project policy, move the durable result into the appropriate project document or decision record.

## Current assumptions

### Markdown is sufficient for the first validation cycle

We currently assume that GitHub + Markdown is enough to validate the experience model before investing in a web application.

### Programming is a good first domain

The project begins with programming/software engineering because it contains many recurring edge cases, production failures, design decisions, and practical situations that are difficult to learn from definitions alone.

This does not imply that Virtual Experience is permanently a programming-only project.

### Contributors will benefit from a shared scenario structure

We assume a reusable template will improve consistency and learning quality, but the template should not become so rigid that contributors must distort real experiences to fit it.

### Multiple scenarios per topic are valuable

We assume different manifestations of the same underlying concept can teach different recognition patterns and trade-offs.

### AI can help scale the project, but provenance must remain explicit

AI can assist with editing, organization, review, scenario construction, and repository maintenance. It must not manufacture first-hand experience or attribution.

## Open design questions

- What scenario metadata is mandatory?
- Do we use YAML front matter or human-readable Markdown metadata?
- Should scenarios reveal the solution immediately or support a progressive learning format later?
- How should we identify related concepts without creating taxonomy duplication?
- How much code should scenarios include?
- How do we distinguish beginner-friendly simplification from misleading oversimplification?
- What evidence or review standard should apply to technical claims?
- What license structure best supports both repository tooling and contributed written experiences?

## Rule for AI agents

Do not silently treat an assumption in this file as an accepted requirement.

If work depends on an unresolved assumption, either keep the implementation reversible or surface the decision explicitly.

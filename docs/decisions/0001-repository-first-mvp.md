# ADR 0001: Repository-first Markdown MVP

- Status: Accepted
- Date: 2026-09-10

## Context

Virtual Experience may eventually benefit from a dedicated web application, interactive learning flows, search, personalization, or other platform capabilities.

However, the project's central hypothesis is not yet whether a particular UI works. The first hypothesis is whether structured scenario-based exposure is useful and whether people can contribute and consume those scenarios coherently.

Building an application immediately would introduce product, infrastructure, design, and maintenance work before validating the content model.

## Decision

Virtual Experience will begin as a public GitHub repository with Markdown as the primary content format.

The repository itself is the MVP product and the durable source of truth for project context.

A dedicated application is deferred until actual usage demonstrates limitations that a platform can materially solve.

## Consequences

### Positive

- very low implementation overhead
- contribution workflow uses familiar open-source primitives
- content remains portable
- project history is naturally versioned
- humans and AI agents can operate from the same artifacts
- attention remains focused on content quality and information architecture

### Negative

- GitHub is less approachable for some non-technical contributors
- discovery and navigation may degrade as content grows
- progressive/interactive learning experiences are limited
- analytics and personalization are limited

These limitations are acceptable during MVP validation and may become evidence for a future platform.

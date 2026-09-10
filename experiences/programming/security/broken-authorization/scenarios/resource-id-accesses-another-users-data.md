---
title: "Resource ID Accesses Another User's Data"
domain: "programming"
area: "security"
topic: "broken-authorization"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "authorization"
  - "object-level-authorization"
  - "access-control"
---

# Resource ID Accesses Another User's Data

## Context

A team is testing a small document application in an isolated development environment populated with synthetic accounts and test documents. Every signed-in user can view and edit documents they own.

The API identifies each document with a resource ID. The normal interface only links a user to documents returned by their own dashboard.

## Situation

While writing authorization tests, the team creates two synthetic users, each with a separate document. A request for the first user's own document works as expected.

The test then asks the same authenticated endpoint for the second synthetic user's document. The server returns it instead of rejecting the request.

## Symptoms

- Requests without a valid session are rejected.
- Requests with a valid session can retrieve a document when given its resource ID.
- The dashboard itself only displays resources belonging to the current user.
- The returned document includes an owner different from the authenticated test identity.
- The behavior is reproducible across synthetic test resources regardless of whether their identifiers are easy or difficult to predict.

## Learner Task / Decision Point

You need to determine which security property is missing. The endpoint clearly authenticates requests, so investigate what additional relationship must be verified before a resource is returned.

Consider whether identifier secrecy should affect the correctness of the authorization decision.

## Investigation

Follow the server-side data-access path in the controlled application.

Questions worth answering:

1. Which identity is authenticated for the request?
2. How does the server load the requested document?
3. Does the query constrain the resource by both its identifier and the current user's permitted ownership or tenant boundary?
4. If the resource is loaded first, where is its ownership or access relationship checked before data is returned?
5. Are read, update, delete, export, and other operations applying the same object-level policy?
6. What should happen if a valid resource identifier becomes known through logs, links, references, or another legitimate workflow?
7. Do tests create resources owned by different synthetic users and verify cross-user access is denied?

The purpose is to verify isolation inside a system the team controls. Real third-party accounts or resources are not needed to reproduce or understand the failure.

## Root Cause

The endpoint required authentication but loaded a document using only the client-provided resource ID. It never verified that the authenticated identity was authorized to access that particular object.

The UI's user-specific dashboard reduced which identifiers normal users encountered, but the backend did not encode or check the ownership boundary. Authentication established who made the request; it did not establish permission to every document in the system.

## Possible Approaches

Depending on the application's data and policy model, the team could:

- constrain data-access queries to resources the authenticated identity is allowed to access;
- evaluate an object-level authorization policy after loading a resource but before exposing or mutating it;
- make tenant or ownership context an explicit input to repository/service APIs so unconstrained lookups are harder to use accidentally;
- apply the same object-level policy across read and write operations;
- add cross-user and cross-tenant denial tests using synthetic fixtures;
- treat opaque identifiers as an implementation property rather than an access-control mechanism.

A system with sharing, teams, delegated access, or administrators may need a richer relationship policy than simple `owner == current_user` logic.

## Trade-offs

Scoping database queries by authorized ownership can reduce the chance that unauthorized objects enter application logic and may combine access control efficiently with retrieval. Complex permission models, however, can make query construction and policy reuse harder.

A centralized object-level policy can express richer relationships and improve consistency, but loading the object before authorization may require care to avoid unintended information disclosure, side effects, or inconsistent not-found/forbidden behavior.

Opaque identifiers are still useful for reasons such as avoiding enumeration-friendly URLs or decoupling public identifiers from database keys, but they cannot replace authorization. Correct access control should continue to hold even when a valid identifier is known.

## What Could Go Wrong

- Read endpoints enforce ownership while update, delete, download, or export paths do not.
- A tenant-aware service calls a lower-level repository method that performs an unconstrained lookup.
- Caching returns a resource without including authorization-relevant identity or tenant context in the cache design.
- Shared-resource features are added later and ad hoc ownership checks become inconsistent.
- Tests cover valid owners but never construct a second identity to exercise the denial boundary.
- The team changes sequential IDs to random IDs and mistakenly considers the authorization defect fixed.

## Takeaway

Being authenticated does not grant access to every object an application can identify. Resource-level operations need server-side authorization tied to the requested object and the authenticated identity's relationship to it, and that boundary should remain correct even when identifiers are known.
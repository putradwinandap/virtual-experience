---
title: "The Harmless Field Rename"
domain: "programming"
area: "architecture-and-design"
topic: "hidden-coupling"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "hidden-coupling"
  - "api-contract"
  - "backward-compatibility"
  - "schema-evolution"
---

# The Harmless Field Rename

## Context

An order service returns order data to the web application through an internal API. The documented response includes an order ID, status, total, and line items. The service team wants to rename an internal database-derived field from `customer_name` to `display_name` to support a broader set of profiles.

The web application has its own API adapter, and several background jobs consume the same response library.

## Situation

The rename is released as a small refactor. The order service tests pass, and the web application appears healthy in a basic smoke test. Shortly afterward, customer-support emails show blank names in the order dashboard, while the fulfillment export begins rejecting rows.

The order service team says the renamed field was never part of the documented contract.

## Symptoms

- One dashboard screen renders an empty customer name.
- A fulfillment export fails schema validation.
- Other order screens continue to work.
- The service's unit and contract tests are green.
- Repository-wide search finds no direct reference in the order service, but a shared response helper transforms fields dynamically.

## Your Task

How would you identify the consumers affected by this change? What should be restored or changed before attempting the rename again?

## Investigation

Map the response from the order service to every boundary: HTTP clients, shared libraries, exports, event publishers, and scheduled jobs. Search for the old field in consumer repositories, generated schemas, fixtures, and transformation code—not only in the producer.

Compare the actual serialized response before and after the release. Inspect the shared helper and its tests for dynamic field selection, fallback behavior, or object spreading. Identify which consumers were relying on the field despite the absence of explicit documentation.

Add a request or consumer-level reproduction for each affected path. The key evidence is not merely that the producer changed a name; it is that multiple consumers had formed an implicit contract around the old shape.

## Root Cause

The shared response helper exposed `customer_name` to consumers even though the public documentation did not promise it. Some consumers read the field directly, while others depended on a generated export schema containing it. The producer's tests verified its own implementation, not the behavior of all downstream consumers.

The undocumented response shape became a real contract through repeated use. The coupling was hidden because ownership and compatibility expectations were defined only by documentation, not by the observable interface and consumer tests.

## Possible Approaches

- Restore the old field temporarily and introduce `display_name` alongside it.
- Version the API or response schema when the old shape cannot be preserved.
- Publish an explicit contract and add consumer-driven contract tests for important clients.
- Replace the shared dynamic helper with a typed, reviewed adapter at each boundary.
- Inventory and communicate the deprecation period before removing the old field.

## Trade-offs

Keeping both fields makes migration safer but increases schema complexity and maintenance. Versioning creates a clearer boundary but requires clients and operational tooling to support multiple versions. Consumer-driven tests improve confidence but add coordination and CI cost. Typed adapters make dependencies visible but may duplicate some mapping code.

## What Could Go Wrong

Do not assume a field is safe to remove because it is undocumented. Do not rely only on repository-wide search when consumers live in separate repositories or receive generated artifacts. Avoid silently changing the meaning of a field while preserving its name. Also, do not deprecate the old field without measuring or observing remaining usage.

## Takeaway

When a “private” response field is widely observable, it can become a contract regardless of what the documentation says. Before changing a shared shape, map actual consumers, make the dependency explicit, and provide a migration path when compatibility matters.

## Related Concepts

- [Idempotency](../../../api-and-integration/idempotency/)

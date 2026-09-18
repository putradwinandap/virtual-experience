---
title: "The Query That Became the Hot Path"
domain: "programming"
area: "performance"
topic: "unbounded-query"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "unbounded-query"
  - "pagination"
  - "query-plan"
---

# The Query That Became the Hot Path

## Context

An admin endpoint lists recent events for a customer. It originally served a small dataset and returns a JSON array directly from a database query.

## Situation

Months later, the endpoint becomes slow and causes database CPU spikes during support operations. The application code has not changed.

## Symptoms

- Response time grows with older customers' event counts.
- Database reads and response payload sizes are much larger for a few accounts.
- Application CPU is moderate, but database CPU and network usage are high.
- Adding more application instances provides little improvement.

## Your Task

How would you establish whether the endpoint is scanning, sorting, or returning too much data? What change would bound the work without hiding records users still need to inspect?

## Investigation

Measure query duration, rows examined, rows returned, sort behavior, and payload size by account. Inspect the query plan and indexes. Check whether the endpoint has a limit, stable ordering, and a pagination strategy that remains efficient on later pages.

## Root Cause

The endpoint performed unbounded work: it selected every matching event and sorted the full result for each request. Data growth converted a once-small operation into a hot path.

## Possible Approaches

- Add a selective index matching the filter and stable ordering.
- Introduce a bounded page size with cursor-based pagination.
- Select only fields needed by the view.
- Move historical data to a separate retrieval path or archive.

## Trade-offs

Indexes consume storage and write capacity. Cursor pagination is efficient but more complex for clients than a simple page number. Field selection and archiving improve cost but may require API and product changes.

## What Could Go Wrong

Do not add a limit without a deterministic order; users may see duplicates or skipped records. Do not rely on application-side slicing after fetching the full result. Do not assume an index helps without checking the actual query plan and data distribution.

## Takeaway

When performance worsens as data grows, look for work with no explicit bound. Measure rows scanned, rows returned, sorting, and payload size before choosing an optimization.

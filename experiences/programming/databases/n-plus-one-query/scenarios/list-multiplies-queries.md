---
title: "The List Endpoint That Multiplied Queries"
domain: "programming"
area: "databases"
topic: "n-plus-one-query"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "n-plus-one-query"
  - "query-plan"
  - "batching"
---

# The List Endpoint That Multiplied Queries

## Context

An endpoint loads 100 orders, then renders each customer's name through a lazy relationship.

## Situation

The endpoint is fast in development but slow in production, especially for accounts with many orders.

## Symptoms

- Query count grows with result count.
- Database latency dominates request time.
- Increasing application replicas does not remove the database pressure.

## Your Task

Measure how many queries one request performs and choose a fix that preserves the response contract.

## Investigation

Use query logging or tracing to compare a one-item and 100-item request. Identify repeated lookups and check whether the relationship is needed for every row.

## Root Cause

The initial list query was followed by one related-record query per item.

## Possible Approaches

Join or eager-load required data, batch related IDs in one query, or change the response to omit data that is not needed.

## Trade-offs

Joins can duplicate rows; eager loading uses memory; batching adds application logic. The right choice depends on cardinality and payload needs.

## What Could Go Wrong

Do not fix the symptom by caching every lookup without checking freshness and memory growth.

## Takeaway

When query count grows with rows returned, inspect hidden relationship loading before tuning individual queries.

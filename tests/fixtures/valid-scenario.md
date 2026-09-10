---
title: "Oversold Inventory During Flash Sale"
domain: "programming"
area: "concurrency"
topic: "race-condition"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts:
  - "race-condition"
  - "database-transaction"
---

# Oversold Inventory During Flash Sale

## Context

A store processes concurrent purchases for limited inventory.

## Situation

Two requests observe the same remaining stock before either update completes.

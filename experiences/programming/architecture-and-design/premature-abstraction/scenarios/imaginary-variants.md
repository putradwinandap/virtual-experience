---
title: "The Abstraction Designed for Imaginary Variants"
domain: "programming"
area: "architecture-and-design"
topic: "premature-abstraction"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["premature-abstraction", "duplication", "cohesion"]
---

# The Abstraction Designed for Imaginary Variants

## Context

Two similar handlers are combined into a generic framework before their behavior is well understood.

## Situation

The third use case requires flags and hooks that make the abstraction harder to understand than the original code.

## Symptoms

- Callers pass combinations of options that are difficult to explain.
- Small changes require touching the shared framework.

## Your Task

Decide whether to generalize, split, or wait for stronger evidence.

## Investigation

Compare real invariants and variation points. Identify whether duplication is accidental or whether the flows merely look similar.

## Root Cause

The design optimized for predicted reuse rather than observed shared behavior.

## Possible Approaches

Keep local code until patterns stabilize, extract a narrow shared primitive, or accept intentional duplication.

## Trade-offs

Duplication costs synchronized fixes; premature abstraction costs coupling and comprehension.

## What Could Go Wrong

Do not judge duplication only by line count; duplicated concepts can have different reasons to change.

## Takeaway

Abstract stable knowledge, not superficial similarity.

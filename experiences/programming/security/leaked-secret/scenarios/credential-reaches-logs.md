---
title: "The Credential That Reached Logs"
domain: "programming"
area: "security"
topic: "leaked-secret"
difficulty: "intermediate"
provenance:
  type: "illustrative"
concepts: ["leaked-secret", "credential-rotation", "redaction"]
---

# The Credential That Reached Logs

## Context

An integration logs failed request details for debugging. A token is included in a serialized request object.

## Situation

The log is shipped to a shared system and retained by several teams.

## Symptoms

- A credential appears in structured logs or an exception trace.
- Access logs show the token may have been used after the event.

## Your Task

Contain exposure without assuming deletion from one log index removes every copy.

## Investigation

Identify the credential scope, retention destinations, readers, and first possible use. Preserve incident evidence while limiting access.

## Root Cause

Sensitive request material crossed a logging boundary without field-level redaction.

## Possible Approaches

Revoke and replace the credential, remove or restrict exposed records where possible, and add centralized redaction tests.

## Trade-offs

Rotation may interrupt clients. Redaction reduces debugging detail but prevents a larger class of incidents.

## What Could Go Wrong

Do not paste the secret into a ticket while discussing the leak, and do not rely only on deleting the visible log entry.

## Takeaway

Treat logs as durable, widely replicated data; secrets must be excluded before emission.

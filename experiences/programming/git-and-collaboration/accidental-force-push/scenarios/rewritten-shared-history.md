---
title: "The Force Push That Rewrote Shared History"
domain: "programming"
area: "git-and-collaboration"
topic: "accidental-force-push"
difficulty: "beginner"
provenance:
  type: "illustrative"
concepts:
  - "accidental-force-push"
  - "shared-branch"
  - "reflog"
---

# The Force Push That Rewrote Shared History

## Context

Several contributors push to a shared repository. A developer rebases a local branch, sees that the remote branch has diverged, and uses a force push to make the branch match the rebased history.

## Situation

Another contributor's commits disappear from the remote branch. An open pull request changes unexpectedly, and a release workflow can no longer find the commit it was configured to build.

## Symptoms

- The remote branch no longer contains commits visible earlier that day.
- A pull request diff changes or becomes smaller.
- Teammates report that their local branches have commits absent from the remote.
- CI references an old commit that is no longer reachable from the branch.

## Your Task

How would you preserve evidence and recover the missing commits without overwriting more work?

## Investigation

Stop additional pushes to the branch. Record the current remote tip, inspect local reflogs and other clones, and identify the old branch tip. Verify which commits are missing before creating a recovery branch. Prefer `--force-with-lease` for intentional history replacement because it refuses to overwrite an unexpected remote update.

## Root Cause

The force push replaced the remote reference rather than merging the remote history. The command protected the pusher's local intent, not the other contributors' commits.

## Possible Approaches

- Restore the old tip on a recovery branch and review the lost commits.
- Reapply missing commits with a carefully reviewed cherry-pick.
- Revert an already-published change when preserving linear history is less important than a visible corrective commit.
- Protect important branches and require pull requests.

## Trade-offs

Reference restoration is fast but may reintroduce unwanted commits. Cherry-picking preserves selected work but can create conflicts and duplicate history. Branch protection reduces accidental damage while adding review friction.

## What Could Go Wrong

Do not run another force push before recording the current state. Do not assume unreachable commits are immediately gone; reflogs and clones may still preserve them. Avoid blaming a contributor before reconstructing the sequence of references.

## Takeaway

A shared branch is a coordination boundary. Before rewriting it, verify that the remote has not moved; after an accident, preserve references first and recover second.

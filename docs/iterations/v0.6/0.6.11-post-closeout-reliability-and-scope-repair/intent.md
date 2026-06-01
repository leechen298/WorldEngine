# Intent

Status: review complete

## Problem

The v0.6 reliability validation initially reported `partial pass`, not clean
pass. The executable command matrix passed, but the scope authorization and
backend/API reliability findings blocked final clean-pass evidence.

The root issue is governance plus two narrow behavior gaps:

- `0.6.10` is documentation-only and cannot authorize current backend/frontend
  dirty files.
- failed generation fallback digests drop valid seed material when an unrelated
  non-JSON value makes canonical digesting fail.
- public preview API coverage does not directly exercise sensitive imported-plan
  provenance failure.

## Why Now

The current worktree already contains post-closeout review-fix changes. Leaving
them only as a parent review addendum keeps the repo in an ambiguous state where
some documents say clean and the reliability result says partial pass.

## Relationship To Roadmap

This is a v0.6 repair package. It does not start v0.7 external validation
readiness or v0.8 projection readiness.

## Non-Goals

- no new generation capability.
- no new public API route or schema.
- no migrations, persistence, live provider behavior, or concrete world content.
- no new live Agent smoke or autonomous runner execution.

## Expected Handoff

After this package passes, v0.6 remains final/closed with an additional
post-closeout reliability repair record. If a future rerun fails, the durable
reliability result must be downgraded with explicit blockers.

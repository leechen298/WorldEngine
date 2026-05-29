# 03 Codex Autonomous Validation Plan

Status: not started / planned
Type: autonomous-validation-planning package

## Goal

Define the independent Codex autonomous validation plan for v0.3
post-closeout. This package tells a future reviewer what to read, what claims
to check, what commands to run or block, and what not to modify.

This package does not execute autonomous validation.

## Deliverables

- `README.md`
- `intent.md`
- `contract.md`
- `test-plan.md`
- `plan.md`
- `review.md`

Each file has a `.zh.md` mirror.

## Required Reviewer Behavior

The reviewer must:

- not rely on implementer summaries.
- read docs and code directly.
- run available validation commands or record blockers.
- avoid code modifications.
- avoid unverified pass claims.
- output an independent review.
- check WorldSpec loader claims.
- check runtime context bridge claims.
- check RuntimeEngine compatibility.
- check Event.refs response compatibility.
- check that no concrete demo-world regression appears.

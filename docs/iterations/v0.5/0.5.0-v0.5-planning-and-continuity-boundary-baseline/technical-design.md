# Technical Design

Status: planned / ready for review

## Current State

v0.4 is final / closeout complete. It delivers a minimal request-driven
Agent-in-World loop with bounded perception, action intent/result contracts,
validated `noop` and `params.patch`, and `POST /world/agent/loop/step`.

v0.4 deliberately did not implement memory, episodic memory, relationship
state, self-summary, reflection, or personality drift. v0.4 post-closeout
validation recorded a clean pass after a scoped frontend build type repair.
That evidence is baseline and handoff context only.

No `docs/iterations/v0.5/` package existed before this work.

## Contract Alignment and Invariants

This package is documentation-only. It must preserve these invariants:

- implementation authorization stays `no`.
- all changes remain under `docs/iterations/v0.5/**`.
- no runtime, schema, API, frontend, backend test, fixture, migration,
  generated result, external repository, or `backend/worldengine/`
  implementation file changes occur.
- all six v0.5 capabilities enter as reviewed contracts before behavior.
- working memory and episodic memory are the only first implementation
  candidates.
- historical v0.4 evidence is not promoted to v0.5 pass evidence.

## Documentation Structure

Parent campaign docs:

- `README.md`: version root, goal entry, scope, deliverables, package index,
  current state, and handoff baseline.
- `v0.5-plan.md`: detailed version plan and quasi-package specs for all
  planned children.
- `GOAL_RUNNER.md`: route selection, implementation authorization,
  subagent/evaluator gates, reporting rules, and stop conditions.
- `CURRENT_STATE.md`: current campaign status, active child, route, next action,
  and evidence snapshot.
- `CAMPAIGN_PLAN.md`: campaign sequence, cross-child handoff, exit criteria,
  and stop conditions.
- `review.md`: parent-level documentation evidence and subagent/evaluator
  findings.

Child package docs:

- `README.md`: package status, goal, scope, deliverables, and document list.
- `intent.md`: problem, goal, non-goals, why now, north-star alignment, and
  handoff.
- `contract.md`: public concepts, capability split, compatibility constraints,
  allowed changes, forbidden changes, and follow-ups.
- `technical-design.md`: this documentation design and invariants.
- `test-plan.md`: exact documentation verification commands and not-run
  implementation checks.
- `plan.md`: ordered execution steps and stop conditions.
- `review.md`: changed files, commands, test results, compatibility review,
  scope review, subagent evidence, findings, and final assessment.

Every active doc has a `.zh.md` mirror.

## Planned Future Implementation Interfaces

This package may name future implementation paths but must not create them:

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py` or an equivalent approved path
- `backend/app/tests/test_agent_memory_*.py`

Any future implementation package must define exact schemas, services,
interfaces, data flow, tests, and compatibility checks before implementation.

## Compatibility Strategy

`0.5.0` changes no product behavior. Future implementation packages must treat
these v0.4 surfaces as compatibility-sensitive:

- `PerceptionFrame`
- `ActionIntent`
- `ActionResult`
- request-scoped `LoopStep`
- `POST /world/agent/loop/step`
- `/world/agent/params/propose-and-apply`
- runtime tick and world time
- API envelope and error shape
- event routes and optional `Event.refs`
- params behavior
- archive behavior

## Anti-Drift Rules

- Keep parent `README.md`, `CURRENT_STATE.md`, `v0.5-plan.md`,
  `CAMPAIGN_PLAN.md`, and `review.md` status values aligned.
- Keep English and Chinese mirrors semantically equivalent.
- Record command evidence exactly.
- Record implementation checks as not run for this docs-only package.
- Stop if any implementation file class appears in the changed-file set.

## Risks

- Risk: documentation implies implementation authorization.
  Mitigation: record `implementation_authorized: no` in package docs and
  review.
- Risk: v0.4 evidence is misread as v0.5 validation.
  Mitigation: label all v0.4 evidence as handoff only.
- Risk: v0.5 expands into application-specific behavior.
  Mitigation: repeat concrete-world, external-validation, projection, and
  `backend/worldengine/` prohibitions in parent and child contracts.
- Risk: mirror drift.
  Mitigation: create English and Chinese files in the same pass and include
  mirror checks in review.


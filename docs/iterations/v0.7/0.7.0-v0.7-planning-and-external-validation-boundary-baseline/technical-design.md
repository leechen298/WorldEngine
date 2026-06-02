# Technical Design

## Current State

The v0.7 parent package exists at `docs/iterations/v0.7/` and has passed
read-only parent review. Before this package, the parent state recorded no
active child and no implementation authorization. The planned `0.7.x` entries
in `v0.7-plan.md` were roadmap-level package specs only.

Root guidance files such as `AGENTS.md` and `AGENTS.zh.md` are outside this
child package's allowed changes. If they are dirty in a future run, they must
be treated as separate user work unless the user explicitly authorizes that
scope.

## Documentation Structure

This child creates a concrete package directory:

```text
docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/
```

The directory contains the full package set and Chinese mirrors:

```text
README.md
intent.md
contract.md
technical-design.md
test-plan.md
plan.md
review.md
README.zh.md
intent.zh.md
contract.zh.md
technical-design.zh.md
test-plan.zh.md
plan.zh.md
review.zh.md
```

## Affected Files

Allowed child files:

- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/**`

Allowed parent status surfaces:

- `docs/iterations/v0.7/README.md`
- `docs/iterations/v0.7/README.zh.md`
- `docs/iterations/v0.7/v0.7-plan.md`
- `docs/iterations/v0.7/v0.7-plan.zh.md`
- `docs/iterations/v0.7/GOAL_RUNNER.md`
- `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.7/CURRENT_STATE.md`
- `docs/iterations/v0.7/CURRENT_STATE.zh.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.7/review.md`
- `docs/iterations/v0.7/review.zh.md`

## Control Flow

1. `GOAL_RUNNER.md` routes `完成 v0.7` to `CURRENT_STATE.md`.
2. `CURRENT_STATE.md` points to the active `0.7.0` child.
3. The agent reads the child package in required order.
4. Because this package is documentation-only, the agent runs documentation
   verification and read-only evaluator review.
5. If no P1/P2 remains, the package may hand off to `0.7.1`; otherwise it
   remains in review or records a blocker.

## Data Model / Schema Changes

None. This package must not change runtime data models, API schemas, report
schemas, checker schemas, database schemas, persistence, migrations, frontend
models, or external runner result schemas.

## Runtime / Service Design

None. No runtime service, API route, checker implementation, frontend behavior,
or test implementation changes are authorized.

## Compatibility Strategy

- Treat v0.6 evidence as historical handoff context only.
- Keep all current implementation behavior unchanged.
- Keep planned child package specs non-authoritative until each child package
  is created or confirmed and reviewed.
- Keep implementation authorization closed.

## Anti-Drift Rules

- Status surfaces must agree on active child, route, and implementation
  authorization.
- Review evidence must distinguish current-session checks from historical
  evidence.
- Chinese mirrors must preserve status, type, goal, scope, forbidden changes,
  compatibility constraints, findings, and final assessment semantics.
- Any out-of-scope file change must be classified as pre-existing user work or
  removed from package scope.

## Risks

- Parent status could drift from child package status.
- Documentation could imply implementation authorization.
- Historical v0.6 evidence could be promoted to current v0.7 pass evidence.
- Dirty root guidance files could be accidentally included in the package.
- Chinese mirrors could lose a blocking restriction or final-assessment
  nuance.

The test plan detects these risks with status checks, required-file checks,
scope guards, mirror checks, and subagent/evaluator review.

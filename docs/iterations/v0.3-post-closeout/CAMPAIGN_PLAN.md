# Campaign Plan

Status: campaign executed / passed with P3
Type: Codex `/goal` campaign plan

## Purpose

This plan defines the ordered campaign sequence for:

```text
完成 v0.3-post-closeout
```

It is campaign guidance, not WorldEngine runtime behavior and not an
automation-controller implementation.

Execution result: the approved 2026-05-29 campaign run completed the sequence
through final bundle synthesis with final assessment `passed with P3`.

## Sequence

### 0. Master validation planning

Purpose: establish the parent campaign, status taxonomy, stop conditions,
evidence vocabulary, and report templates.

Inputs: v0.3 release docs, v0.3 evidence index, compatibility audit, final
closeout review, `docs/iterations/AGENTS.md`, scope boundary docs, and the
loader / bridge / event compatibility code and tests listed in
`validation-master-plan.md`.

Allowed changes: create parent `v0.3-post-closeout` docs and child package
scaffolding.

Forbidden changes: runtime, schema, API, frontend, backend tests, fixtures,
migrations, E2E artifacts, external repositories, release status, or v0.4
implementation.

Expected deliverables: parent README, current state, goal runner, campaign
plan, master validation plan, report template, review, and child package docs.

Verification expectation: documentation checks only.

Exit criteria: all required docs exist, do not claim validation execution, and
are ready for human / ChatGPT review.

Handoff: `01-e2e-validation-plan` becomes the first active child.

### 1. E2E / integration / API smoke validation plan

Purpose: define what future E2E, integration, API smoke, loader, bridge,
Event.refs, release-claim, and concrete demo-world regression validation must
check.

Inputs: parent campaign docs, v0.3 closeout docs, loader/bridge/event code,
and current repository test files.

Allowed changes: update `01-e2e-validation-plan/**` planning docs.

Forbidden changes: validation execution, runtime implementation, schema, API,
frontend, tests, fixtures, external repositories, and private oracle details.

Expected deliverables: README, intent, contract, test plan, execution plan,
and review evidence for planning quality.

Verification expectation: documentation checks and scope wording checks only.

Exit criteria: plan is specific enough for `02` to execute without inventing
scope or success criteria.

Handoff: `02-e2e-validation-execution` may execute only after this plan is
reviewed.

### 2. E2E / integration / API smoke execution

Purpose: run or explicitly block the future validation commands and fill the
E2E / integration validation report.

Inputs: `01` plan, `02` execution plan, current branch/commit, v0.3 docs,
loader/bridge/event code and tests, API route files, and available E2E config.

Allowed changes: update `02-e2e-validation-execution/**` report and review
files with execution evidence or blockers.

Forbidden changes: implementation repair, runtime/schema/API/frontend/test
edits, fixture data, migrations, release status changes, and external repo
creation.

Expected deliverables: filled `e2e-validation-report.md`, commands run,
P1/P2/P3 classification, and review update.

Verification expectation: future execution should run documentation checks,
backend deterministic checks, focused loader/bridge tests, event compatibility
tests, API smoke, and E2E if configured. If E2E is unavailable, record it as
not configured or blocked and use API smoke plus backend integration tests as
fallback.

Exit criteria: final assessment is one of `passed`, `passed with P3`,
`blocked`, `failed`, or `not executed`.

Handoff: `03-codex-autonomous-validation-plan` starts only after `02` has
execution evidence or a recorded blocker.

### 3. Codex autonomous validation plan

Purpose: define independent Codex reviewer inputs, constraints, commands, and
claim checks without executing the review.

Inputs: parent campaign docs, v0.3 release and evidence docs, loader/bridge
code, RuntimeEngine, WorldCell/Event schemas, and focused tests.

Allowed changes: update `03-codex-autonomous-validation-plan/**` planning docs.

Forbidden changes: autonomous review execution, code changes, test changes,
runtime/schema/API/frontend edits, fixtures, external repositories, and
demo-world details.

Expected deliverables: reviewer contract, test plan, plan, and review record.

Verification expectation: documentation checks only.

Exit criteria: `04` can run an independent review without relying on the
implementer's summary.

Handoff: `04-codex-autonomous-validation-execution` owns the actual
independent Codex review.

### 4. Codex autonomous validation execution and review

Purpose: conduct or explicitly block a future independent Codex review of v0.3
loader, bridge, API/schema/runtime compatibility, Event.refs compatibility,
and demo-world regression boundaries.

Inputs: `03` plan, `04` review template, v0.3 source docs, loader/bridge/event
code and tests, and `02` validation evidence when available.

Allowed changes: update `04-codex-autonomous-validation-execution/**` review
documents with independent findings, commands, blockers, and recommendation.

Forbidden changes: implementation repair, runtime/schema/API/frontend/test
edits, fixtures, external repositories, release status changes, and private
oracle details.

Expected deliverables: filled Codex autonomous review, unsupported-claim
classification, P1/P2/P3 list, and package review update.

Verification expectation: reviewer runs available validation commands or
records blockers, reads docs and code directly, and does not rely on
implementer summaries.

Exit criteria: final recommendation is one of `passed`, `passed with P3`,
`blocked`, `failed`, or `not executed`.

Handoff: `05-final-validation-bundle` synthesizes current evidence only.

### 5. Final validation bundle

Purpose: summarize the current campaign's E2E/integration, API smoke, backend,
loader, bridge, Event.refs, autonomous review, release-claim, compatibility,
demo-world regression, P1/P2/P3, blocker, and v0.4 proceed status.

Inputs: reports from `02` and `04`, parent campaign state, v0.3 evidence docs,
and unresolved findings from all child package reviews.

Allowed changes: update `05-final-validation-bundle/**` summary and review
files.

Forbidden changes: new implementation work, fresh execution not needed to
resolve evidence conflicts, release status changes, external repository
creation, or hidden pass claims.

Expected deliverables: `validation-summary.md`,
`final-validation-bundle.md`, and `review.md`.

Verification expectation: synthesize only current evidence or recorded
blockers; rerun commands only if the active execution contract requires it.

Exit criteria: final assessment is one of `passed`, `passed with P3`,
`blocked`, `failed`, or `not executed`; v0.4 proceed status is explicit.

Handoff: if not executed, blocked, or failed, a future reviewed package decides
next action. If passed or passed with P3, v0.4 may proceed only through its own
reviewed iteration package.

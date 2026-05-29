# v0.2 Post-Closeout Validation

Status: ready for execution
Type: post-closeout validation planning

## Goal

Maintain the document chain for independent v0.2 post-closeout validation and
route the remaining validation packages safely.

v0.2 feature and documentation closeout is complete. v0.2 independent
E2E / integration validation has now passed. v0.2 Codex autonomous validation
is not yet performed.

This package does not reopen v0.2 implementation. It does not change v0.2
release status.

## Current Routing Note

This package was originally created as a documentation-only post-closeout
validation chain. Since then, `02-e2e-validation-execution` has been executed
and currently records `passed` with 2026-05-29 evidence.

The remaining active work is:

1. review-closeout `03-codex-autonomous-validation-plan`;
2. execute `04-codex-autonomous-validation-execution`;
3. fill `05-final-validation-bundle`.

This validation chain does not reopen v0.2 implementation or change v0.2
release status. Use `CURRENT_STATE.md` and `GOAL_RUNNER.md` as the short routing
entrypoints for Codex App `/goal`.

## Governance

This validation documentation follows the evidence, review, and post-closeout
validation rules defined in `docs/iterations/AGENTS.md` as files under
`docs/iterations/v0.2-post-closeout/`.

## Validation Chain

0. Master validation planning.
1. E2E / integration / API smoke validation plan.
2. E2E / integration / API smoke execution report.
3. Codex autonomous validation plan.
4. Codex autonomous validation execution and review template.
5. Final validation bundle template.

## Package Index

| Package | Type | Status | Purpose |
|---|---|---|---|
| `01-e2e-validation-plan` | validation-planning | review complete | Define v0.2 post-closeout E2E, integration, and API smoke validation scope. |
| `02-e2e-validation-execution` | validation-execution | passed | Execute v0.2 post-closeout E2E, integration, and API smoke validation. |
| `03-codex-autonomous-validation-plan` | validation-planning | planned / ready for review | Define independent Codex autonomous validation scope. |
| `04-codex-autonomous-validation-execution` | validation-execution | not executed | Execute independent Codex autonomous validation. |
| `05-final-validation-bundle` | validation-bundle | not executed | Summarize final v0.2 post-closeout validation result. |

## Result States

Validation documents may use these states:

- `planned`
- `ready for execution`
- `executed`
- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`

Execution reports start as `not executed` until a validation run fills them
with current-session evidence. `02-e2e-validation-execution` previously reached
`blocked` because browser E2E could not bind the configured backend port in the
2026-05-28 execution context. The package was reopened on 2026-05-29 after
`agent-iter` validation stages were updated to run with host-capable localhost
binding. The 2026-05-29 host-capable rerun passed backend deterministic checks,
API smoke, and configured browser E2E.

## Scope

Allowed:

- Define post-closeout validation workflow.
- Define report templates and evidence requirements.
- Define E2E / integration / API smoke execution expectations.
- Define Codex autonomous validation expectations.
- Define final validation bundle requirements.

Forbidden:

- Do not run backend, frontend, E2E, API smoke, runtime, schema execution,
  fixture, migration, or autonomous validation commands while updating planning
  or routing documents.
- Do not run validation commands outside the package that explicitly owns that
  validation execution.
- Do not modify runtime, schema, API, frontend, backend tests, fixtures, or
  external repositories.
- Do not add concrete demo-world names, locations, characters, resources,
  story rules, seed data, UI selectors, or private oracle details.
- Do not declare a completed v0.2 final validation result before `04` and `05`
  are closed with evidence.
- Do not change v0.2 final / complete status.

## Deliverables

- `CURRENT_STATE.md`
- `CURRENT_STATE.zh.md`
- `GOAL_RUNNER.md`
- `GOAL_RUNNER.zh.md`
- `validation-master-plan.md`
- `validation-master-plan.zh.md`
- `validation-report-template.md`
- `validation-report-template.zh.md`
- `review.md`
- `review.zh.md`
- `01-e2e-validation-plan/`
- `02-e2e-validation-execution/`
- `03-codex-autonomous-validation-plan/`
- `04-codex-autonomous-validation-execution/`
- `05-final-validation-bundle/`

## Final Assessment State

This documentation package is ready for human / ChatGPT review after the
documentation checks in the package reviews pass.

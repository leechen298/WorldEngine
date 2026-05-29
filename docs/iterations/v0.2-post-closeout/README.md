# v0.2 Post-Closeout Validation

Status: planned / ready for review
Type: post-closeout validation planning

## Goal

Create the document chain for independent v0.2 post-closeout validation.

v0.2 feature and documentation closeout is complete. v0.2 independent
E2E / integration validation is not yet performed. v0.2 Codex autonomous
validation is not yet performed.

This package does not reopen v0.2 implementation. It does not change v0.2
release status. This pass only creates validation documents.

## Governance

This validation documentation follows the evidence, review, and post-closeout
validation rules defined in `docs/iterations/AGENTS.md` as files under
`docs/iterations/v0.2-post-closeout/`.

## Validation Chain

0. Master validation planning.
1. E2E / integration / API smoke validation plan.
2. E2E / integration / API smoke execution template.
3. Codex autonomous validation plan.
4. Codex autonomous validation execution and review template.
5. Final validation bundle template.

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

No execution report in this package records a successful result. Execution
reports start as `not executed` until a later validation run fills them with
current-session evidence.

## Scope

Allowed:

- Define post-closeout validation workflow.
- Define report templates and evidence requirements.
- Define E2E / integration / API smoke execution expectations.
- Define Codex autonomous validation expectations.
- Define final validation bundle requirements.

Forbidden:

- Do not run backend, frontend, E2E, API smoke, runtime, schema execution,
  fixture, migration, or autonomous validation commands in this documentation
  pass.
- Do not modify runtime, schema, API, frontend, backend tests, fixtures, or
  external repositories.
- Do not add concrete demo-world names, locations, characters, resources,
  story rules, seed data, UI selectors, or private oracle details.
- Do not declare a completed v0.2 validation result.
- Do not change v0.2 final / complete status.

## Deliverables

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

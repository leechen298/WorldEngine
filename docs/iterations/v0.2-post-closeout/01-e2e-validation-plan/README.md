# E2E / Integration / API Smoke Validation Plan

Status: restart ready
Type: validation planning

## Goal

Define the v0.2 post-closeout E2E / integration / API smoke validation scope
without executing any validation commands.

## Current Campaign Note

This package previously reached review complete. For the current
`v0.2-post-closeout` goal campaign, that review is archived and must be rerun
or explicitly re-accepted before the campaign advances to
`02-e2e-validation-execution`.

## Scope

This package plans:

- repository and documentation checks.
- backend deterministic checks.
- schema smoke checks.
- event compatibility checks.
- runtime step checks.
- world events checks.
- event steps checks.
- params checks when available.
- archive checks when available.
- API smoke checks.
- E2E framework availability checks.
- release claim validation.
- concrete demo-world regression checks.

## E2E Definition

WorldEngine v0.2 does not claim a product UI. For this post-closeout package,
E2E means:

- browser E2E if a runnable framework is available.
- backend integration plus API smoke plus release claim validation as fallback.

If no E2E framework exists or the suite cannot run, record E2E as not
configured or blocked. Do not convert that into a successful result.

## Deliverables

- `intent.md`
- `intent.zh.md`
- `contract.md`
- `contract.zh.md`
- `test-plan.md`
- `test-plan.zh.md`
- `plan.md`
- `plan.zh.md`
- `review.md`
- `review.zh.md`

## Final Assessment State

Restart ready. No current-campaign validation execution has happened in this
package.

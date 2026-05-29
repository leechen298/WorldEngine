# Contract

Status: blocked

## Public Concepts

- Reviewed branch: the branch recorded during execution.
- Reviewed commit: the exact commit recorded during execution.
- Command evidence: command, purpose, exit code, and output summary.
- Blocker: a reason validation could not run or complete.
- Final assessment: one of `passed`, `passed with P3`, `blocked`, `failed`,
  or `not executed`.

## Allowed Changes

During a later execution pass, update only this package's report and review
unless a separate approved plan allows broader documentation updates.

During validation-fix passes, update only this package's validation evidence,
status fields, and milestone finding rows needed to record the blocker or
rerun result.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend tests, fixtures, or
  migrations from this execution package.
- Do not hardcode branch or commit before execution.
- Do not use Playwright config presence as proof that browser E2E can run.
- Do not declare success for checks that were not run.
- Do not hide blockers.

## Compatibility Requirements

Execution must compare observed behavior to v0.2 release claims without
changing v0.2 status. Claim conflicts become findings, not silent edits to the
release docs.

## Out-of-Scope Follow-Ups

- Fixing failed checks.
- Adding E2E infrastructure.
- Changing v0.2 implementation or release status.

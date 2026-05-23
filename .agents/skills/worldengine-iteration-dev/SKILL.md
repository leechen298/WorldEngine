---
name: worldengine-iteration-dev
description: Use when implementing a reviewed WorldEngine code or mixed iteration package after its contract, technical design, test plan, and plan have been approved.
---

# WorldEngine Iteration Dev

Use this skill only inside the WorldEngine repository.

This is the implementation-stage workflow. It executes an already reviewed
code or mixed iteration package.

## Required Reading

Before editing implementation files, read the active package in this order:

1. `README.md`
2. `intent.md`
3. `contract.md`
4. `technical-design.md`
5. `test-plan.md`
6. `plan.md`
7. `review.md`

Also read `AGENTS.md` and the project direction docs referenced there when the
package touches project direction.

## Gate Check

Start implementation only when the package clearly shows the documentation
review gate is complete, such as `Status: ready for implementation`, reviewed
contract/design/test-plan checklist items, or equivalent package wording.

Stop and report a blocker if:

- required package documents are missing.
- the package is still proposed, planned, or awaiting review.
- contract, design, test plan, and execution plan conflict.
- the requested work is outside the current package.
- implementation reveals a design gap.

Do not repair iteration documents and continue coding in the same flow after a
gate or design blocker.

## Implementation Rules

- Implement only the approved package scope.
- Keep iteration and planning documents read-only during implementation, except
  for `review.md` closeout evidence when the active contract or user explicitly
  requires it.
- Do not silently reinterpret the contract.
- Do not change `backend/worldengine/` unless the active contract explicitly
  allows it.
- Preserve compatibility unless the active contract allows a breaking change.

## Verification

Run the commands listed in the active `test-plan.md`. Report exact commands,
exit codes, relevant pass/fail counts, and skipped checks.

Do not claim tests, builds, E2E, UI smoke, Agent smoke, runtime behavior, or
autonomous test coverage passed without current-session evidence.

## Review Evidence

When closeout is in scope, update `review.md` with:

- changed files.
- commands run.
- test results.
- compatibility review.
- scope review.
- unresolved P1/P2/P3 findings.
- final assessment.

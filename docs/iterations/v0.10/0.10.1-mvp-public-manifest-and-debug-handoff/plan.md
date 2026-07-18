# Plan

## Ordered Execution Steps

1. Read governing docs and current v0.10 route.
2. Read existing `/manifest` schema, route, and focused tests.
3. Draft this package document set and mirrors.
4. Run a read-only documentation / contract evaluator.
5. If no P1/blocking P2 remains, update `review.md` to record
   `implementation_authorized: yes`.
6. Implement additive schema changes in `backend/app/schemas/world.py`.
7. Update `/manifest` construction in `backend/app/api/routes/world.py`.
8. Update focused manifest tests in
   `backend/app/tests/test_public_handoff_contract_api.py`.
9. Run the exact commands in `test-plan.md`.
10. Run implementation-scope and code/evidence evaluator checkpoints.
11. Fix in-scope findings or record blockers.
12. Update package and parent reviews with changed files, commands, results,
    compatibility review, scope review, unresolved findings, and handoff.
13. If closeout passes, advance the parent route to
    `0.10.2-world-session-contract-and-state-store-documentation-package-needed`.

## Phase Boundaries

Documentation phase:

- Create and review package documents.
- Do not edit implementation files until `review.md` records
  `implementation_authorized: yes`.

Implementation phase:

- Edit only the allowed schema, route, and focused test files.
- Keep changes additive and redacted.

Verification phase:

- Run focused tests and documentation checks.
- Use evaluator checkpoints before final route closeout.

## Stop Conditions

Stop if:

- required package docs or mirrors are missing.
- documentation / contract evaluator reports unresolved P1 or blocking P2.
- implementation requires files outside the approved scope.
- manifest work requires session state, runtime execution, provider live calls,
  checker fixtures, frontend, Validation Client, generated results, migrations,
  or external repository changes.
- secret/raw/private data would appear in public manifest output.
- planned/future session surfaces would be reported as `pass` or `available`
  before implementation.

## Review Update Step

Before implementation, record the documentation review gate and authorization
decision. Before closeout, update `review.md` and parent v0.10 review with:

- changed files.
- commands run.
- test results.
- subagent/evaluator evidence.
- compatibility review.
- scope review.
- unresolved findings.
- final assessment and handoff route.

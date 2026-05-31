# Plan

Status: review complete

## Files

Create:

- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/README.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/README.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/intent.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/intent.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/contract.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/contract.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/technical-design.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/technical-design.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/test-plan.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/test-plan.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/plan.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/plan.zh.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/review.md`
- `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/review.zh.md`

After review evidence supports completion, update:

- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `docs/iterations/v0.6/v0.6-plan.zh.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/CURRENT_STATE.zh.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/review.zh.md`

Do not touch:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- migrations or alembic files
- fixtures or generated results
- external repositories
- release documents outside the active v0.6 package

## Ordered Execution Steps

1. Read repository guidance, project direction docs, iteration standards, v0.6
   parent docs, `0.6.0` review evidence, and current WorldSpec / loader /
   runtime-context / API envelope code.
2. Draft the complete `0.6.1` package docs and Chinese mirrors with status
   `planned / ready for review` and `implementation_authorized: no`.
3. Run documentation checks, mirror checks, required-term checks, and scope
   guard from `test-plan.md`.
4. Dispatch or record a read-only documentation evaluator for the drafted
   package.
5. Fix P1/P2 findings inside documentation scope, or record blockers if they
   cannot be fixed.
6. When checks and evaluator evidence show no unresolved P1/P2, update this
   package `review.md` and `review.zh.md` with exact evidence.
7. Update parent v0.6 status surfaces and mirrors to mark `0.6.1` review
   complete and set active child to
   `0.6.2-template-catalog-and-deterministic-generator-core`.
8. Rerun status and scope checks after parent status updates.

## Phase Boundaries

- Documentation drafting may create only this package's docs and mirrors.
- Review synchronization may update parent v0.6 status surfaces only after
  checks and evaluator evidence support completion.
- Implementation remains closed. No schema, service, API, frontend, fixture,
  migration, generated result, or test implementation can start in `0.6.1`.

## Stop Conditions

Stop and record a blocker if:

- any required package file or mirror is missing.
- the contract requires concrete world content, private validation internals,
  application-specific backend behavior, live AI-provider behavior, external
  validation readiness, or projection readiness.
- a documentation command fails and cannot be fixed inside documentation scope.
- a subagent/evaluator reports a blocking P1/P2 that cannot be fixed inside
  documentation scope.
- implementation files would need to change during this package.
- status surfaces drift between package and parent docs.

## Review Update Step

After verification, update `review.md` and `review.zh.md` with:

- changed files.
- exact commands run.
- exact results.
- compatibility review.
- scope review.
- subagent/evaluator status.
- unresolved P1/P2/P3 findings.
- final assessment.

## Verification

Use the exact documentation checks, mirror checks, status checks, and scope
guards in `test-plan.md`.

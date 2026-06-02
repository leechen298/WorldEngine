# Plan

## Files

Create:

- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/README.md`
- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/intent.md`
- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/contract.md`
- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/technical-design.md`
- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/test-plan.md`
- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/plan.md`
- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/review.md`
- Chinese mirrors for each package document。

Modify:

- `docs/iterations/v0.7/` 下的 v0.7 parent status and route surfaces。

Do not touch:

- runtime、schema、API、frontend、backend test、checker implementation、fixture、migration、
  external repository、generated result 和 `backend/worldengine/` implementation files。
- `AGENTS.md` 和 `AGENTS.zh.md` 等 root guidance files，除非读取其 rules。

## Steps

1. Read the parent v0.7 docs, project direction docs, and iteration rules.
2. Confirm parent review can route to `0.7.0`.
3. Create the full `0.7.0` child package and Chinese mirrors.
4. Synchronize parent status surfaces to point to the active child.
5. Run the documentation checks listed in `test-plan.md`.
6. Dispatch read-only subagent/evaluator review for package completeness, mirror consistency, scope, and status semantics.
7. Fix any P1/P2 or stop with a blocker.
8. Update `review.md` and `review.zh.md` with actual command evidence and evaluator findings.
9. If no blocker remains, mark `0.7.0` review complete and hand off to `0.7.1`.

## Stop Conditions

- Required child package documents or mirrors are missing.
- Any implementation file changes appear inside this package scope.
- Parent and child status surfaces disagree.
- A positive pass/final/release/readiness claim lacks current-session evidence.
- A subagent/evaluator reports P1 or unresolved P2.
- Historical v0.6 evidence is treated as current v0.7 pass evidence.

## Verification

Use documentation checks and subagent/evaluator review only. Do not run code tests unless a scope violation introduces
implementation changes, in which case stop and record the violation instead of widening the package.

# Plan

Chinese mirror: `plan.zh.md`.

Status: documentation drafted / review pending

## Ordered Execution Steps

1. Read v0.11 route, parent plan, iteration rules, existing rule/session/
   direction/evolution APIs, and current evolution tests.
2. Draft this complete package document set and Chinese mirrors.
3. Run documentation gate commands.
4. Request a read-only documentation / contract evaluator.
5. Fix any P1/P2 findings inside package scope.
6. If evaluator passes, update `review.md` with
   `implementation_authorized: yes`; provider live and external validation stay
   `no`.
7. Implement only the approved additive session evolution scope.
8. Run focused backend verification from `test-plan.md`.
9. Request implementation-scope and code-review/evidence evaluator checkpoints.
10. Fix any P1/P2 findings inside package scope.
11. Update package review, parent v0.11 route/status docs, and handoff to
    `0.11.5`.

## Phase Boundaries

- Documentation phase ends only after evaluator approval.
- Implementation phase begins only after `review.md` records
  `implementation_authorized: yes`.
- Closeout begins only after focused verification and evaluator checkpoints.

## Stop Conditions

Stop before implementation or closeout if work would:

- implement without active package authorization.
- bypass public legality evaluation.
- apply rejected/blocked candidates.
- mutate Agent private state or direct final facts.
- introduce provider calls, frontend changes, persistence, migrations,
  Validation Client code, concrete demo fixtures, or `backend/worldengine`.
- claim unrun tests or validation passed.

## Review Update Step

`review.md` must record changed files, exact commands run, test results,
compatibility review, scope review, evaluator checkpoints, unresolved findings,
and final assessment.

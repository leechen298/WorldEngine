# Plan

Chinese mirror: `plan.zh.md`.

Status: documentation drafted / review pending

## Ordered Execution Steps

1. Read v0.11 route, parent plan, all prior v0.11 child reviews, fidelity
   helpers, and fidelity tests.
2. Draft this complete package document set and Chinese mirrors.
3. Run documentation gate commands.
4. Request a read-only documentation / contract evaluator.
5. Fix any P1/P2 findings inside package scope.
6. If evaluator passes, update `review.md` with
   `implementation_authorized: yes`; provider live and external validation stay
   `no`.
7. Run focused fidelity and v0.11 regression verification.
8. Record scorecard evidence and v0.11 closeout result.
9. Request implementation/evidence evaluator checkpoint.
10. Fix any P1/P2 findings inside package scope.
11. Update package review, parent v0.11 closeout docs, and handoff to v0.12.

## Phase Boundaries

- Documentation phase ends only after evaluator approval.
- Evidence execution begins only after `review.md` records
  `implementation_authorized: yes`.
- v0.11 closeout begins only after focused verification and evaluator
  checkpoint.

## Stop Conditions

Stop before evidence execution or closeout if work would:

- use private/raw evaluator/provider/prompt data.
- claim provider live, external Validation Client, Agent autonomy, or complete
  MVP PASS.
- implement new runtime feature scope not authorized by this package.
- modify frontend, persistence, migrations, concrete fixtures, or
  `backend/worldengine`.
- claim unrun tests or validation passed.

## Review Update Step

`review.md` must record changed files, exact commands run, test results,
scorecard evidence, compatibility review, scope review, evaluator checkpoints,
unresolved findings, final v0.11 assessment, and v0.12 handoff.

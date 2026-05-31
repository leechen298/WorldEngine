# Campaign Plan

Status: final / closeout complete

## Objective

Run v0.5 as a review-gated `/goal` campaign that defines and implements the
Memory and Self-Continuity Substrate without widening WorldEngine into
application-specific backend behavior.

## Authoritative Inputs Read For 0.5.0

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.4/README.md`
- `docs/iterations/v0.4/CURRENT_STATE.md`
- `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/final-closeout.md`
- `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/review.md`
- `docs/iterations/v0.4/review.md`
- `docs/iterations/v0.4-post-closeout/README.md`
- `docs/iterations/v0.4-post-closeout/CURRENT_STATE.md`
- `docs/iterations/v0.4-post-closeout/review.md`
- `docs/testing/results/2026-05-31-v0.4-overall-product-capability-validation.md`
- `docs/testing/results/2026-05-31-v0.4-e2e-agent-test-expansion.md`

## Campaign Rules

- The active child package is the only implementation scope.
- `0.5.0` is documentation-only and must not modify implementation files.
- Implementation authorization starts as no for every child.
- Mixed/code packages must complete documentation review before implementation.
- Historical v0.4 evidence is handoff context only.
- Current-session command evidence is required before v0.5 runtime, API, E2E,
  build, Agent smoke, autonomous validation, or release claims.
- Chinese mirrors must preserve status, type, goal, scope, forbidden changes,
  compatibility requirements, findings, and final assessment semantics.

## Planned Child Sequence

1. `0.5.0-v0.5-planning-and-continuity-boundary-baseline`
2. `0.5.1-memory-self-continuity-contracts`
3. `0.5.2-working-and-episodic-memory-substrate`
4. `0.5.3-memory-context-loop-integration`
5. `0.5.4-reflection-relationship-and-drift-contract-followup`
6. `0.5.5-v0.5-evidence-and-compatibility-audit`
7. `0.5.6-v0.5-release-candidate-bundle`
8. `0.5.7-v0.5-final-closeout`

## Cross-Child Handoff Rules

- `0.5.0` hands off reviewed campaign structure and capability boundaries to
  `0.5.1`.
- `0.5.1` hands off public concept and schema semantics to `0.5.2`.
- `0.5.2` hands off only working and episodic memory substrate evidence to
  `0.5.3`.
- `0.5.3` hands off bounded read-only memory context evidence to `0.5.4`.
- `0.5.4` hands off relationship, self-summary, reflection, and drift contract
  status to audit.
- `0.5.5` hands off evidence and compatibility review to release candidate.
- `0.5.6` hands off release-candidate findings to final closeout.
- `0.5.7` may mark final status only after evidence consistency and review
  gates pass.

## Campaign Exit Criteria

v0.5 may be marked `final / closeout complete` only when:

- all active child packages are review complete or explicitly deferred by
  contract.
- implementation-bearing children record current-session command evidence.
- compatibility review confirms v0.4 loop/API surfaces remain compatible or
  only additively changed by reviewed contracts.
- scope review confirms no concrete demo-world, external validation internal,
  frontend product behavior, migration, projection app, generation, or
  `backend/worldengine/` work slipped in.
- unresolved findings are classified and no P1/P2 remains without explicit
  accepted rationale.

## Stop Conditions

Stop before implementation or closeout if:

- active package docs are missing required files or mirrors.
- a required subagent/evaluator checkpoint is unavailable or reports blocking
  P1/P2.
- implementation touches files outside the active package contract.
- verification commands fail and the package cannot honestly record pass
  evidence.
- status surfaces drift between README, current state, plan, review, and
  closeout docs.

# Campaign Plan

Status: planned / ready for review

## Objective

Run v0.8 as a review-gated `/goal` campaign that prepares WorldEngine to reach
a minimum normally working state and exposes enough public, generic core-side
surfaces for a separate external validation function to judge whether the
engine works.

This campaign must not turn the core repository into the external validator,
an external projection application, a product-specific backend, or a storage
place for concrete validation worlds.

## Authoritative Inputs Read For Parent Drafting

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.7/README.md`
- `docs/iterations/v0.7/CURRENT_STATE.md`
- `docs/iterations/v0.7/GOAL_RUNNER.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.7/v0.7-plan.md`
- `docs/testing/results/2026-06-02-v0.7-code-review.md`
- `docs/current-implementation.md`
- `docs/glossary.md`

## Campaign Rules

- The parent v0.8 package remains the authoritative campaign entrypoint.
- No v0.8 child package is active.
- The planned `0.8.x` entries in `v0.8-plan.md` are roadmap-level planned
  package specs. They do not authorize implementation and are not immutable
  execution scripts.
- Implementation authorization starts as no for every child.
- Mixed/code packages must complete documentation review before implementation.
- Historical v0.7 and v0.6 evidence is handoff context only.
- v0.7 post-closeout P1/P2 blockers must be repaired, routed to a narrow
  repair, or recorded as blockers before any affected v0.8 readiness claim.
- Current-session command evidence is required before v0.8 runtime, API,
  frontend, E2E, build, Agent smoke, autonomous validation, minimum
  working-state PASS, external validation readiness, product readiness,
  generation-quality, or release claims.
- Chinese mirrors must preserve status, type, goal, scope, forbidden changes,
  compatibility requirements, findings, and final assessment semantics.
- Readiness claims must distinguish core contract readiness, core observable
  surface readiness, minimum working-state evidence, external validation
  handoff readiness, external validation PASS, blocked, skipped, and out of
  scope.

## Planned Child Sequence

1. `0.8.0-v0.8-planning-and-v0.7-handoff-baseline`
2. `0.8.1-minimum-working-state-contract`
3. `0.8.2-core-observable-surface-boundary`
4. `0.8.3-generation-runtime-agent-loop-readiness`
5. `0.8.4-external-validation-handoff-contract`
6. `0.8.5-core-working-state-smoke-evidence`
7. `0.8.6-v0.8-evidence-and-boundary-audit`
8. `0.8.7-v0.8-release-candidate-bundle`
9. `0.8.8-v0.8-final-closeout`

This sequence is a route proposal. It may be revised by reviewed child package
documents. It must not be used to skip the active child package review, and it
must not be followed mechanically if implementation or evidence uncovers a
design problem.

## Cross-Child Handoff Rules

- `0.8.0` should hand off reviewed campaign structure, v0.7 handoff-risk
  handling, minimum working-state boundaries, and external-validation
  boundaries to `0.8.1`.
- `0.8.1` should hand off readiness claim taxonomy and authorization criteria
  to `0.8.2`.
- `0.8.2` should hand off generic core observable surface semantics to
  `0.8.3`.
- `0.8.3` should hand off core generation/runtime/Agent-loop readiness
  boundaries and evidence needs to `0.8.4`.
- `0.8.4` should hand off external-validation handoff semantics without
  defining external validator implementation.
- `0.8.5` should hand off core-side smoke and compatibility evidence to audit.
- `0.8.6` should hand off evidence and boundary review to release candidate.
- `0.8.7` should hand off release-candidate findings to final closeout.
- `0.8.8` may mark final status only after evidence consistency and review
  gates pass.

## Campaign Exit Criteria

v0.8 may be marked `final / closeout complete` only when:

- all active child packages are review complete or explicitly deferred by
  contract.
- implementation-bearing children record current-session command evidence.
- compatibility review confirms v0.7 projection contracts, v0.6 generation,
  v0.5 memory, v0.4 Agent loop, and v0.3 loader/runtime-context bridge remain
  compatible or only additively changed by reviewed contracts.
- v0.7 post-closeout P1/P2 blockers are repaired with current-session evidence
  or recorded as blockers in the active v0.8 evidence.
- scope review confirms no external validation implementation, external
  application implementation, product UI, concrete app data, private external
  repo path, UI selector, hidden reset API, private transcript, validation
  oracle internal, app-specific backend behavior, migration, or
  `backend/worldengine/` work slipped in.
- minimum working-state and external-validation handoff claims are backed by
  current-session schema/checker/API/test evidence where those claims are in
  scope.
- unresolved findings are classified and no P1/P2 remains without explicit
  accepted rationale.

## Stop Conditions

Stop before implementation or closeout if:

- active package docs are missing required files or mirrors.
- a planned package has not yet been converted into current child package docs.
- a required evaluator checkpoint is unavailable or reports blocking P1/P2.
- implementation touches files outside the active package contract.
- implementation discovers a design gap and the active child contract, design,
  test plan, plan, and review have not been updated and re-reviewed.
- verification commands fail and the package cannot honestly record pass
  evidence.
- minimum working-state readiness text turns into product readiness.
- external validation boundary text turns into external validator
  implementation or external app implementation.
- concrete application data, private app internals, UI selectors, hidden reset
  APIs, external validator connection details, oracle internals, or external
  repository details become required.
- v0.7 post-closeout blockers are ignored while making affected readiness
  claims.
- status surfaces drift between README, current state, plan, review, and
  closeout docs.

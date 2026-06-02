# Campaign Plan

Status: final / closeout complete

## Objective

Run v0.7 as a review-gated `/goal` campaign that prepares WorldEngine for
external validation suites and projection consumers through public contracts,
redacted reports, readiness manifests, and compatibility evidence without
turning the core repository into an external validation app, projection
product, or application-specific backend.

## Authoritative Inputs Read For 0.7.0

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/external-fixture-boundary.md`
- `docs/contracts/external-fixture-runner-contract.md`
- `docs/validation-report-template.md`
- `docs/testing/product-capability-validation-playbook.md`
- `docs/testing/test-documentation-playbook.md`
- `docs/testing/code-review-playbook.md`
- `docs/current-implementation.md`
- `docs/glossary.md`
- `docs/releases/v0.6.md`
- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/GOAL_RUNNER.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.6/v0.6-plan.md`

## Campaign Rules

- The parent v0.7 package remains the authoritative campaign entrypoint.
- `0.7.0-v0.7-planning-and-external-validation-boundary-baseline` is review
  complete.
- `0.7.1-public-validation-and-projection-contracts` is review complete.
- `0.7.2-validation-report-schema-and-redaction-checker` is review complete.
- `0.7.3-contract-bundle-and-readiness-manifest` is review complete.
- `0.7.4-projection-consumer-read-model-contracts` is review complete.
- `0.7.5-quality-regression-and-compatibility-evidence` is review complete.
- `0.7.6-v0.7-evidence-and-compatibility-audit` is review complete.
- `0.7.7-v0.7-release-candidate-bundle` is review complete.
- `0.7.8-v0.7-final-closeout` is review complete and final closeout complete.
- No v0.7 child package remains active.
- The planned `0.7.x` entries in `v0.7-plan.md` are roadmap-level planned
  package specs. They do not authorize implementation and are not immutable
  execution scripts.
- Any post-closeout work requires a new reviewed package or the next version's
  reviewed iteration package.
- Implementation authorization starts as no for every child.
- Mixed/code packages must complete documentation review before
  implementation.
- Historical v0.6 evidence is handoff context only.
- Current-session command evidence is required before v0.7 runtime, API,
  frontend, E2E, build, Agent smoke, autonomous validation, external
  validation, projection readiness, product readiness, generation-quality, or
  release claims.
- Chinese mirrors must preserve status, type, goal, scope, forbidden changes,
  compatibility requirements, findings, and final assessment semantics.
- Readiness claims must distinguish contract readiness, report format
  readiness, core-side compatibility readiness, actual external suite PASS,
  and out-of-scope checks.

## Planned Child Sequence

1. `0.7.0-v0.7-planning-and-external-validation-boundary-baseline`
2. `0.7.1-public-validation-and-projection-contracts`
3. `0.7.2-validation-report-schema-and-redaction-checker`
4. `0.7.3-contract-bundle-and-readiness-manifest`
5. `0.7.4-projection-consumer-read-model-contracts`
6. `0.7.5-quality-regression-and-compatibility-evidence`
7. `0.7.6-v0.7-evidence-and-compatibility-audit`
8. `0.7.7-v0.7-release-candidate-bundle`
9. `0.7.8-v0.7-final-closeout`

This sequence is a route proposal. It may be revised by reviewed child package
documents. It must not be used to skip the active child package review, and it
must not be followed mechanically if implementation or evidence uncovers a
design problem.

## Cross-Child Handoff Rules

- `0.7.0` handed off reviewed campaign structure, v0.6 handoff, and
  external-consumer boundaries to `0.7.1`.
- `0.7.1` handed off public readiness concepts, report semantics, projection
  consumer boundaries, and authorization criteria to `0.7.2`.
- `0.7.2` handed off report schema/checker and redaction evidence to `0.7.3`.
- `0.7.3` handed off public contract bundle and readiness manifest semantics to
  `0.7.4`.
- `0.7.4` handed off projection consumer read-model contracts and approved
  implementation evidence to `0.7.5`.
- `0.7.5` handed off regression and compatibility evidence to audit.
- `0.7.6` handed off evidence and compatibility review to release candidate.
- `0.7.7` handed off release-candidate findings to final closeout.
- `0.7.8` marked final status after evidence consistency and review gates
  passed.

## Campaign Exit Criteria

v0.7 may be marked `final / closeout complete` only when:

- all active child packages are review complete or explicitly deferred by
  contract.
- implementation-bearing children record current-session command evidence.
- compatibility review confirms v0.6 generation, v0.5 memory, v0.4 Agent loop,
  and v0.3 `WorldSpec` loader/runtime-context bridge remain compatible or only
  additively changed by reviewed contracts.
- scope review confirms no concrete validation world, external oracle
  internal, UI selector, hidden reset API, application-specific backend
  behavior, migration, first projection app, live provider dependency, or
  `backend/worldengine/` work slipped in.
- redacted report and projection consumer claims are backed by current-session
  schema/checker/API/test evidence where those claims are in scope.
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
- external validation examples require concrete external world content inside
  this repo.
- projection readiness text turns into v0.8 external projection application
  implementation.
- status surfaces drift between README, current state, plan, review, and
  closeout docs.

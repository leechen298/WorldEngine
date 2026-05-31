# Contract

Status: review complete

implementation_authorized: no

## Scope

This package is documentation-only. It may create a v0.6 release-candidate
bundle and update v0.6 parent status surfaces for release-candidate routing.
It must not modify implementation files or expand v0.6 product claims.

## Release Candidate Claims Allowed

The bundle may state that v0.6 has reviewed current-session evidence for:

- generation concept, template, and schema semantics;
- deterministic template catalog generation;
- structured generation plan compilation;
- AI-assisted plan import boundaries without provider/runtime AI integration;
- validation metadata and preview API behavior;
- bounded regeneration and loader/runtime-context readiness checks;
- dashboard generation preview and focused E2E smoke;
- compatibility audit with no unresolved P1/P2 finding through `0.6.8`.

## Claims Not Allowed

The bundle must not state or imply:

- final release or closeout completion;
- product readiness across all WorldEngine surfaces;
- external validation-world readiness;
- projection application readiness;
- Agent smoke or full autonomous runner coverage;
- generation-quality approval;
- live provider integration, prompt quality, or network-backed AI behavior;
- concrete world, story, map, character, seed, fixture, or demo application
  readiness.

## Allowed Files

- Files under
  `docs/iterations/v0.6/0.6.9-v0.6-release-candidate-bundle/`
- Parent v0.6 docs:
  - `docs/iterations/v0.6/README.md`
  - `docs/iterations/v0.6/README.zh.md`
  - `docs/iterations/v0.6/CURRENT_STATE.md`
  - `docs/iterations/v0.6/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.6/GOAL_RUNNER.md`
  - `docs/iterations/v0.6/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.6/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.6/v0.6-plan.md`
  - `docs/iterations/v0.6/v0.6-plan.zh.md`
  - `docs/iterations/v0.6/review.md`
  - `docs/iterations/v0.6/review.zh.md`

## Forbidden Files

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- fixture, migration, generated output, external repository, and product demo
  files.

## Review Gate

This package may be marked review complete only if:

- required English docs and Chinese mirrors exist;
- `0.6.8` is review complete and has no unresolved P1/P2 finding;
- release-candidate claims and exclusions are explicit;
- documentation and status consistency checks pass;
- a read-only release-candidate evaluator reports no P1/P2 finding.

## Handoff

If review completes, hand off to `0.6.10-v0.6-final-closeout` with
implementation authorization still closed.

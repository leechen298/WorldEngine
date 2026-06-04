# Plan

Chinese mirror: `plan.zh.md`.

## Objective

Create a documentation-only package that prepares WorldEngine for external
Validation-Client Agent autonomous validation by defining provider boundaries
and a handoff manifest plan.

## Tasks

### 1. Package Documents

Create:

```text
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/README.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/intent.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/technical-design.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/test-plan.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/plan.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/validation-client-contract-handoff.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-task-plan.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/external-validation-gate-matrix.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/planning-readiness-checklist.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-handoff-prompt.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/review.md
```

Create Chinese mirrors for every file.

### 2. Provider Boundary Plan

Define:

- WorldEngine owns provider configuration.
- validation clients do not manage keys.
- Kimi Code subscription is a coding-agent candidate, not automatically a
  runtime provider.
- Kimi Platform / Moonshot API and DeepSeek API are runtime provider candidates
  that need budget and rate-limit controls.

### 3. Handoff Manifest Plan

Define future manifest fields:

- provider class.
- provider readiness.
- credential source class.
- public surface ids.
- evidence references.
- redaction flags.
- blockers and warnings.

### 3.5 Validation Client Contract Handoff

Document the exact public surfaces required by the external Validation Client:

- `GET /manifest`.
- OpenAPI-discoverable world creation endpoint, preferably `POST /worlds`.
- public world creation response fields.
- optional public director guidance endpoint for full autonomous validation.
- verification commands proving Validation Client `/health/worldengine`
  reports world creation available and `POST /sessions/worldengine` succeeds.

### 3.6 Implementation Handoff Prompt

Create a future-chat prompt that:

- lists required reading.
- defines the exact allowed WorldEngine implementation goal.
- repeats the no-Validation-Client-code boundary.
- repeats the no-secret/no-private-prompt/no-provider-raw-trace boundary.
- names verification commands and completion wording.

### 3.7 Detailed Implementation Task Plan

Create a task-by-task implementation plan that:

- lists required reading for future implementation.
- splits public schemas, `GET /manifest`, `POST /worlds`, director guidance,
  provider readiness redaction, Validation Client compatibility probe, and
  closeout.
- records candidate files, test focus, verification commands, and stop rules for
  each task.
- states that this package still does not authorize implementation.

### 3.8 Contract Readiness Checklist

Create a post-implementation checklist template that:

- restricts conclusions to `WORLDENGINE_CONTRACT_READY`, `PARTIAL`, `BLOCKED`,
  or `FAIL`.
- checks `/health`, `/manifest`, `/openapi.json`, `POST /worlds`, and director
  guidance.
- checks provider readiness redaction.
- checks Validation Client `/health/worldengine` and `POST /sessions/worldengine`
  compatibility probes.
- states that contract ready still does not mean external validation PASS or
  human validation PASS.

### 3.9 External Validation Gate Matrix

Create the WorldEngine-side external validation gate matrix:

- state that WorldEngine owns only Gate 1: public contract readiness.
- state that Validation Client, Codex, second Agent, and human validators own
  later gates.
- state that `WORLDENGINE_CONTRACT_READY` only means the contract can be handed
  to Validation Client for Codex autonomous validation.
- state that WorldEngine does not implement Validation Client operation logs,
  E2E, browser autonomous validation, second-Agent review, or human experience
  judgment.
- state that the current Gate 1 blockers are missing `/manifest` and a
  Validation Client-discoverable world creation endpoint.

### 3.10 Planning Readiness Checklist

Create the planning readiness checklist:

- conclusion is `PLAN_READY_FOR_REVIEW`.
- state that this package still does not authorize implementation.
- state that the only next allowed step is user review followed by Gate 1
  implementation.
- state that current blockers remain missing `/manifest` and discoverable world
  creation endpoint.
- state that this checklist does not prove `WORLDENGINE_CONTRACT_READY`.

### 4. Review

Run:

```bash
git diff --check
```

Record docs-only scope review and note that implementation tests were not run.

## Out Of Scope

- runtime provider implementation.
- API endpoints.
- schemas.
- checkers.
- validation client code.
- external validation scenarios.
- human validation execution.

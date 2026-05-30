# Campaign Plan

Status: ready for review
Type: Codex `/goal` development campaign plan

## Purpose

This plan defines the ordered campaign sequence for:

```text
完成 v0.4
```

It is campaign guidance, not WorldEngine runtime behavior and not an automation-controller implementation.

## Campaign Exit Criteria

v0.4 may be marked final / closeout complete only after all implementation-bearing child packages have reviewed package docs, required subagent/evaluator checkpoints have no blocking findings, focused and compatibility verification commands are recorded with current evidence, release-candidate review approves final closeout, and `0.4.7-v0.4-final-closeout` records no unresolved P1/P2 findings.

## Sequence

### 0. v0.4 Planning And Compatibility Baseline

Package: `0.4.0-v0.4-planning-and-compatibility-baseline`

Purpose: Create the v0.4 documentation root, goal-campaign controls, version plan, compatibility baseline, and v0.3 handoff mapping without changing implementation files.

Allowed changes:

- Create `docs/iterations/v0.4/**` parent and child documentation.
- Define goal entry `完成 v0.4`.
- Define subagent/evaluator checkpoints and package sequence.
- Record v0.3 post-closeout evidence as handoff context only.

Forbidden changes:

- Do not modify runtime, schema, API, frontend, backend test, fixture, migration, or legacy implementation files from this documentation-only package.
- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Documentation-only verification and rationale for not running code tests.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Record backend/frontend/API/E2E/runtime tests as not run because the package is documentation-only.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

### 1. Agent-in-World Loop Contract

Package: `0.4.1-agent-in-world-loop-contract`

Purpose: Define the public v0.4 Agent-in-World loop concepts, event semantics, API boundary, error model, and implementation authorization criteria before code changes.

Allowed changes:

- Define `PerceptionFrame`, `ActionIntent`, `ActionResult`, and `LoopStep` semantics.
- Define event and error model contracts as documentation only.
- Define allowed action vocabulary: `noop` and validated `params.patch`.
- Define API boundary without adding a route in this package.

Forbidden changes:

- Do not modify runtime, schema, API, frontend, backend test, fixture, migration, or legacy implementation files from this documentation-only package.
- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Documentation-only verification and rationale for not running code tests.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Record backend/frontend/API/E2E/runtime tests as not run because the package is documentation-only.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

### 2. Agent Perception And Schemas

Package: `0.4.2-agent-perception-and-schemas`

Purpose: Add generic Agent-in-World schema models and a bounded perception builder that reads runtime state, recent events, world params, and optional runtime-context summary without mutating state.

Allowed changes:

- Add additive schemas under `backend/app/schemas/`.
- Add read-only perception builder under approved `backend/app/` modules.
- Read runtime state, event log, world params, and optional runtime context summary.
- Add focused backend tests for bounded read-only perception.

Forbidden changes:

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Focused test evidence, compatibility evidence, and required subagent/evaluator checkpoints when implemented.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Run focused backend tests from `backend/` with `.venv/bin/python -m pytest ...`.
- Run adjacent compatibility tests for touched surfaces.
- Run FastAPI TestClient API smoke if a route is added.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

### 3. Action Intent Validation And Result Adapter

Package: `0.4.3-action-intent-validation-and-result-adapter`

Purpose: Implement the minimal generic action intent validator and result adapter for noop and validated params.patch, reusing existing param validation and dry-run safeguards.

Allowed changes:

- Add internal action validator/adapter under approved `backend/app/` modules.
- Support `noop` as a valid no-effect action.
- Support `params.patch` only through `ParamPatchItem`, `ParamValidator`, `ParamDryRunValidator`, and existing apply semantics.
- Add focused backend tests for accepted, rejected, dry-run blocked, and no-op intents.

Forbidden changes:

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Focused test evidence, compatibility evidence, and required subagent/evaluator checkpoints when implemented.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Run focused backend tests from `backend/` with `.venv/bin/python -m pytest ...`.
- Run adjacent compatibility tests for touched surfaces.
- Run FastAPI TestClient API smoke if a route is added.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

### 4. Minimal Agent Loop Orchestration And API

Package: `0.4.4-minimal-agent-loop-orchestration-and-api`

Purpose: Wire a request-driven minimal Agent-in-World loop that builds perception, obtains or accepts an intent, validates and applies the intent, emits inspectable result evidence, and returns a stable API response.

Allowed changes:

- Add request-driven loop service under approved `backend/app/` modules.
- Add one reviewed API route only if contract-authorized.
- Use deterministic providers or explicit test intents for tests.
- Add focused service/API tests and adjacent compatibility checks.

Forbidden changes:

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.
- Do not replace or break `/world/agent/params/propose-and-apply`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Focused test evidence, compatibility evidence, and required subagent/evaluator checkpoints when implemented.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Run focused backend tests from `backend/` with `.venv/bin/python -m pytest ...`.
- Run adjacent compatibility tests for touched surfaces.
- Run FastAPI TestClient API smoke if a route is added.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

### 5. Agent Loop Evidence And Compatibility Audit

Package: `0.4.5-agent-loop-evidence-and-compatibility-audit`

Purpose: Audit v0.4 implementation evidence, changed files, compatibility surfaces, unresolved findings, and handoff readiness for release-candidate review.

Allowed changes:

- Create or update v0.4 evidence index and compatibility audit docs if authorized.
- Summarize command evidence from implementation packages.
- Classify runtime, API, event, params, archive, frontend, schema, fixture, migration, and legacy impacts.
- Record v0.5 handoff as planning readiness only.

Forbidden changes:

- Do not modify runtime, schema, API, frontend, backend test, fixture, migration, or legacy implementation files from this documentation-only package.
- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Documentation-only verification and rationale for not running code tests.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Record backend/frontend/API/E2E/runtime tests as not run because the package is documentation-only.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

### 6. v0.4 Release Candidate Bundle

Package: `0.4.6-v0.4-release-candidate-bundle`

Purpose: Prepare a v0.4 release-candidate bundle from reviewed implementation and audit evidence without declaring final release or adding implementation changes.

Allowed changes:

- Create release-candidate bundle docs under `docs/iterations/v0.4/`.
- Summarize package statuses, evidence, commands, findings, and compatibility claims.
- Define final review questions for 0.4.7.
- Use evaluator review for claim support and mirror quality.

Forbidden changes:

- Do not modify runtime, schema, API, frontend, backend test, fixture, migration, or legacy implementation files from this documentation-only package.
- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Documentation-only verification and rationale for not running code tests.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Record backend/frontend/API/E2E/runtime tests as not run because the package is documentation-only.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

### 7. v0.4 Final Closeout

Package: `0.4.7-v0.4-final-closeout`

Purpose: Mark v0.4 final / closeout complete only after release-candidate review approval, evidence consistency checks, and unresolved finding classification.

Allowed changes:

- Update v0.4 status surfaces to final / closeout complete only after approval.
- Update finding records and v0.5 handoff notes.
- Record final evidence summary, commands, compatibility review, and scope review.
- Update release docs only if the active contract explicitly includes them.

Forbidden changes:

- Do not modify runtime, schema, API, frontend, backend test, fixture, migration, or legacy implementation files from this documentation-only package.
- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

Expected deliverables:

- Complete package docs and Chinese mirrors.
- Documentation-only verification and rationale for not running code tests.
- Review recording changed files, commands, compatibility review, scope review, and P1/P2/P3 findings.

Verification expectation:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Record backend/frontend/API/E2E/runtime tests as not run because the package is documentation-only.

Exit criteria: package review records required evidence, required evaluator checkpoints, no unresolved P1/P2, and an explicit handoff status.

Handoff: next package in the sequence receives only reviewed evidence and explicit handoff notes.

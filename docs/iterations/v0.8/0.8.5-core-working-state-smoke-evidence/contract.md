# Contract

## Public Concepts

- `CoreWorkingStateSmokeEvidence`: current-session command evidence for
  public core-side WorldEngine surfaces.
- `CoreSurface`: a bounded surface that can be proven from repository-local
  code, tests, checkers, or API behavior without external validator data.
- `SmokeEvidenceClass`: one of `backend_schema`, `backend_api`,
  `runtime_event`, `agent_loop`, `memory_context`, `archive`, `generation`,
  `handoff_contract`, `frontend`, `e2e`, `agent_smoke`, `autonomous`,
  `external_validation`, or `manual_review`.
- `SmokeEvidenceStatus`: one of `pass`, `fail`, `blocked`, `skipped`, or
  `out_of_scope`.
- `ProofBoundary`: the exact claim a command result supports.
- `EvidenceArtifact`: a repository-local, redacted result file or command log
  reference created or cited by this package.

## Required Core Surfaces

The package must classify these surfaces:

- WorldSpec schema and loader compatibility.
- generation schema, plan compiler, preview, regeneration, runtime-readiness,
  and core-readiness surfaces.
- runtime context bridge and runtime step evidence.
- event schema/API compatibility.
- Agent loop service/API/perception/action evidence.
- memory-context substrate and perception compatibility.
- archive snapshot/summary compatibility.
- v0.7 public contract/checker compatibility for handoff context.
- frontend, E2E, Agent smoke, autonomous, and external validation surfaces as
  in-scope only if the reviewed test plan authorizes commands for them;
  otherwise explicitly classify them as skipped or out of scope.

## Allowed Changes

Documentation stage:

- Create or update files under
  `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/`.
- Create or update Chinese mirrors for this package.
- Update parent v0.8 route/status/review surfaces.

Evidence stage after review:

- Run the exact commands authorized by `test-plan.md`.
- Record redacted command evidence in this package `review.md`.
- Optionally create a result summary under `docs/testing/results/` only if
  `review.md` records that artifact path before creation.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  external validator code, external application code, or `backend/worldengine/`
  files during documentation stage.
- Do not implement new product behavior or alter product functionality to make
  validation pass.
- Do not import, clone, run, or implement an external validator or external app
  repository.
- Do not add concrete validation worlds, product scenarios, UI selectors,
  private screenshots, private transcripts, private paths, oracle internals,
  provider traces, raw prompts, secrets, or non-redacted external event
  payloads.
- Do not treat skipped, blocked, out-of-scope, historical, or documentation
  evidence as PASS.
- Do not claim external validation PASS, product readiness, projection app
  readiness, generation quality PASS, full autonomous PASS, or final v0.8
  readiness.

## Command Authorization Boundary

Before documentation review completes:

- `implementation_authorized: no`
- `evidence_execution_authorized: no`

After documentation/contract review, `review.md` may record:

- `implementation_authorized: no`, unless the evaluator explicitly finds a
  test/checker/artifact implementation change is needed and the contract is
  updated first.
- `evidence_execution_authorized: yes`, limited to the exact commands in
  `test-plan.md`, if no P1 or blocking P2 remains.

## Compatibility Requirements

- v0.3 loader/runtime-context bridge remains compatible.
- v0.4 Agent loop action/perception boundary remains compatible.
- v0.5 memory context remains read-only and process-local.
- v0.6 generation, preview, regeneration, and runtime-readiness surfaces
  remain compatible.
- v0.7 public validation report, readiness manifest, projection read-model,
  and `0.7.9` checker/docs repair evidence remain handoff context only.
- v0.8 `0.8.3` core-readiness evidence remains bounded to its focused route.
- v0.8 `0.8.4` handoff statuses are used for classification and not as PASS
  substitutes.

## Review Gates

Documentation review must verify:

- all required English docs and Chinese mirrors exist.
- command matrix covers required core surfaces or classifies gaps.
- proof boundaries are specific and do not overclaim.
- skipped, blocked, and out-of-scope surfaces have explicit rationale.
- artifact paths are redacted and repository-local.
- no runtime/test/checker implementation files are changed by documentation
  drafting.
- a read-only documentation/contract evaluator reports no P1 and no blocking
  P2.

Closeout after evidence execution requires a later implementation/evidence
stage and must not happen during documentation drafting.

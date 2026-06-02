# Contract

## Public Concepts

- `ProjectionReadModelContract`: a public, read-only contract describing
  payload families external consumers may read in later packages.
- `ReadModelFamily`: one of `runtime_summary`, `event_timeline_summary`,
  `agent_loop_summary`, `memory_context_summary`,
  `generation_readiness_summary`, `readiness_manifest_summary`, or
  `redacted_report_summary`.
- `BoundedSummary`: a redacted summary that avoids raw memory, raw prompts,
  private traces, transcripts, and non-redacted event payloads.
- `NoWriteCapability`: a required marker confirming the read model exposes no
  mutation, reset, persistence, private runner hook, or product-specific write
  behavior.

## Required Read Model Families

The schema/checker must require these read-only families:

- `runtime_summary`
- `event_timeline_summary`
- `agent_loop_summary`
- `memory_context_summary`
- `generation_readiness_summary`
- `readiness_manifest_summary`
- `redacted_report_summary`

Each family must define:

- family id.
- version.
- read-only marker.
- allowed public fields.
- redaction notes.
- no-write guarantee.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/`.
- Create or update Chinese mirrors for this child package.
- Create `docs/contracts/projection-read-model-contract.md`.
- Create `docs/contracts/projection-read-model-schema.json`.
- Create `tools/testing/validate_projection_read_model_contract.py`.
- Create `tools/testing/test_validate_projection_read_model_contract.py`.
- Update parent v0.7 status and route surfaces after review and closeout.

## Forbidden Changes

- Do not add runtime, API route, frontend, persistence, migration, product
  dashboard, projection app, game UI, concrete world viewer, write API, reset
  API, private runner hook, external repository, or `backend/worldengine/`
  implementation changes.
- Do not expose private application state, concrete validation worlds,
  character names, location names, maps, story rules, seed data, UI selectors,
  raw memory records, provider secrets, prompts, private traces, transcripts,
  or non-redacted event payloads.
- Do not claim projection application readiness, product readiness, external
  consumer PASS, runtime/API/frontend PASS, or v0.8 readiness.

## Compatibility Requirements

- Read-model contracts are additive, read-only, and versioned.
- Existing runtime, event, Agent loop, memory, generation, API envelope, and
  dashboard behavior remain unchanged.
- Manifest references from `0.7.3` remain valid.
- Future API-backed projection surfaces must use a later reviewed package if
  runtime/API implementation is needed.

## Review Gates

Implementation may begin only after:

- package docs and Chinese mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- package `review.md` records `implementation_authorized: yes`.

Closeout may happen only after:

- focused projection read-model checker tests pass.
- readiness manifest checker tests pass if manifest references are touched.
- `git diff --check` passes.
- changed-file scope guard passes.
- implementation-scope, code-review, validation-evidence, and closeout
  consistency evaluators report no blocking findings.

## Out-of-Scope Follow-ups

- `0.7.5`: quality regression and compatibility evidence.
- `0.7.6`: evidence and compatibility audit.
- `0.7.7`: release-candidate bundle.
- `0.7.8`: final closeout.

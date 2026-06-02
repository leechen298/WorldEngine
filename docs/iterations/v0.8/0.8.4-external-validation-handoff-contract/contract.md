# Contract

## Public Concepts

- `ExternalValidationHandoff`: a public, core-side contract describing what
  WorldEngine can expose or record for a future external validation function.
- `HandoffSurface`: a stable public identifier for a core-side surface, such
  as `generation_core_readiness`, `runtime_context_summary`,
  `agent_loop_probe`, `readiness_manifest`, or `projection_read_model`.
- `HandoffEvidenceReference`: a repository-relative, redacted reference to
  current-session evidence. It is not evidence by itself unless paired with
  the command or review result that produced it.
- `HandoffStatus`: one of `contract_ready`, `core_evidence_ready`, `blocked`,
  `skipped`, or `out_of_scope`.
- `HandoffEvidenceClass`: one of `documentation`, `schema_checker`,
  `api_backend`, `frontend_e2e`, `agent_smoke`, `autonomous`,
  `external_validation`, or `manual_review`.
- `RedactionConfirmation`: a required statement that public evidence excludes
  forbidden private details.
- `ForbiddenDetailReview`: a required classification showing whether any
  forbidden detail class is present.
- `BlockerSemantics`: rules that prevent `blocked`, `skipped`, and
  `out_of_scope` from being treated as PASS.

## Handoff Semantics

`contract_ready` means a public contract surface is reviewed. It does not mean
runtime behavior, external validation, product readiness, or v0.8 readiness
passed.

`core_evidence_ready` may be used only by a later reviewed evidence package
when current-session commands prove the named core-side surface and the review
records the exact evidence. This package defines the term but does not use it
as a PASS claim.

`blocked`, `skipped`, and `out_of_scope` are not pass equivalents. Each must
include a reason, affected surface id, evidence class, and next-action or
handoff note.

`external_validation` as an evidence class may be named only as a future class.
This package does not authorize running an external validator and does not
accept external validation PASS evidence.

## Allowed Handoff Fields

Future handoff records may include only these public field classes:

- handoff id and version.
- engine version, commit, or package reference.
- public handoff surface id.
- public contract surface path.
- evidence class.
- handoff status.
- repository-relative redacted evidence reference.
- command or review evidence reference when available.
- redaction confirmation.
- forbidden-detail review.
- unresolved P1/P2/P3 findings.
- blocker, skipped, or out-of-scope rationale.
- compatibility notes.
- scope review notes.

## Forbidden Detail Classes

Public handoff records must not contain:

- private external repository paths.
- external validator connection details or commands.
- private runner state.
- private scenarios, oracle internals, or acceptance targets.
- product UI selectors, screenshots, transcripts, or product routes.
- concrete external validation worlds, maps, characters, locations, resources,
  story rules, seed data, or product content.
- hidden reset APIs, write hooks, persistence hooks, or private fixture hooks.
- provider traces, raw prompts, secrets, credentials, or non-redacted external
  event payloads.
- raw memory records or private application state.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.8/0.8.4-external-validation-handoff-contract/`.
- Create or update Chinese mirrors for this package.
- Update parent v0.8 route/status/review surfaces after documentation review.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  external validator code, external application code, or `backend/worldengine/`
  implementation files.
- Do not create `docs/contracts/` schemas, `tools/testing` checkers, report
  templates, generated evidence artifacts, or public API surfaces in this
  package.
- Do not implement external validator connection workflow, automation
  commands, private scenario contracts, oracle behavior, product UI, app
  repository layout, or product-specific acceptance criteria.
- Do not claim external validation PASS, external consumer PASS, product
  readiness, projection application readiness, runtime/API/frontend/E2E PASS,
  Agent smoke PASS, autonomous PASS, generation-quality PASS, minimum
  working-state PASS, or final v0.8 readiness.

## Compatibility Requirements

- v0.7 external validation report semantics remain the redacted report
  baseline.
- v0.7 readiness manifest semantics remain the public evidence-reference
  baseline.
- v0.7 projection read-model semantics remain the read-only/no-write baseline.
- v0.7 `0.7.9` checker/docs clean pass remains handoff context only.
- v0.8 `0.8.1` claim taxonomy, `0.8.2` observable surface boundary, and
  `0.8.3` core-readiness evidence remain compatible and are not expanded by
  this package.

## Review Gates

This package may be marked review complete only after:

- all required English docs and Chinese mirrors exist.
- documentation checks pass.
- parent/child status surfaces are consistent.
- changed-file scope guard confirms documentation-only scope plus already
  reviewed prior v0.8 changes.
- a read-only documentation/contract evaluator reports no P1 and no blocking
  P2.

Implementation remains unauthorized after this documentation-only package
unless a future package creates a reviewed mixed/code contract.

## Handoff

If reviewed, this package hands the handoff contract to
`0.8.5-core-working-state-smoke-evidence`. `0.8.5` must still create or
confirm its own package documents and review gate before running evidence or
changing implementation files.

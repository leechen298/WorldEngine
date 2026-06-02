# Contract

## Public Concepts

- `ReadinessManifest`: a public machine-readable index of WorldEngine
  readiness surfaces and evidence classifications.
- `ContractSurface`: a public document, schema, or template path that an
  external consumer may read.
- `CapabilityArea`: a generic public capability label such as external
  validation readiness, redacted report validation, or projection consumer
  boundary.
- `ReadinessClaim`: a scoped taxonomy value from the reviewed v0.7 contracts.
- `EvidenceReference`: a public, redacted evidence path or checker command
  reference. It is not proof of external suite PASS unless classified as such
  with current-session evidence.

## Manifest Semantics

The manifest must include:

- manifest id.
- manifest version.
- engine version or reference.
- generated source classification.
- public contract surfaces.
- public schema surfaces.
- public template surfaces.
- supported readiness claim values.
- capability areas.
- redacted evidence references.
- compatibility notes.
- redaction rules.

Required public surface paths:

- `docs/contracts/external-fixture-runner-contract.md`
- `docs/contracts/external-validation-readiness-contract.md`
- `docs/contracts/projection-consumer-contract.md`
- `docs/testing/external-validation-report-schema.json`
- `docs/validation-report-template.md`
- `tools/testing/validate_external_validation_report.py`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md`

The manifest may list reviewed taxonomy values, including PASS-like values,
inside a `readiness_claim_values` taxonomy section. That list is not evidence.
`evidence_references[*].status` is stricter: in this package it may use only
`contract ready`, `report format ready`, `blocked`, `skipped`, or
`out of scope`. The checker must reject `external suite pass`,
`external consumer pass`, and `core-side compatibility ready` in evidence
references unless a later reviewed package adds current-session accepted
evidence rules for those statuses.

The manifest must not include private runner state, private paths, concrete
world details, UI selectors, hidden reset details, oracle internals, seed data,
transcripts, or non-redacted event payloads.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/`.
- Create or update Chinese mirrors for this child package.
- Create `docs/contracts/v0.7-readiness-manifest-schema.json`.
- Create `docs/contracts/v0.7-readiness-manifest.json`.
- Create `tools/testing/validate_readiness_manifest.py`.
- Create `tools/testing/test_validate_readiness_manifest.py`.
- Update parent v0.7 status and route surfaces after review and closeout.

## Forbidden Changes

- Do not modify runtime, API routes, frontend, persistence, migrations,
  generated results, external repositories, fixture runners, or
  `backend/worldengine/`.
- Do not add private external suite configuration, private repository paths,
  concrete external world data, concrete world names, character names,
  location names, story rules, seed data, UI selectors, hidden reset API
  details, validation oracle internals, transcripts, or non-redacted event
  payloads.
- Do not create product app behavior, projection read models, write APIs,
  persistence, migrations, release packaging, or external suite automation.
- Do not claim external suite PASS, projection application readiness, product
  readiness, release readiness, runtime PASS, API PASS, frontend PASS, E2E
  PASS, live Agent smoke PASS, or full autonomous PASS.

## Compatibility Requirements

- Existing contract docs remain valid.
- Existing external validation report schema/checker behavior remains
  compatible.
- Manifest fields are additive and versioned.
- Manifest paths must be public repository-relative paths.
- Historical v0.6 evidence may be referenced only as handoff context, not as
  v0.7 PASS evidence.

## Review Gates

Implementation may begin only after:

- package docs and Chinese mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- package `review.md` records `implementation_authorized: yes`.

Closeout may happen only after:

- focused manifest checker tests pass.
- existing external validation report checker tests pass if manifest references
  that schema/checker.
- `git diff --check` passes.
- changed-file scope guard passes.
- implementation-scope, code-review, validation-evidence, and closeout
  consistency evaluators report no blocking findings.

## Out-of-Scope Follow-ups

- `0.7.4`: projection consumer read-model contracts.
- `0.7.5`: quality regression and compatibility evidence.
- `0.7.6`: evidence and compatibility audit.
- `0.7.7`: release-candidate bundle.
- `0.7.8`: final closeout.

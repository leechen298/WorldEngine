# External Validation Readiness Contract

Status: review complete / v0.7.1

## Purpose

This contract defines public, redacted readiness semantics for external
validation suites that consume WorldEngine. It extends the existing external
fixture runner boundary without importing concrete validation worlds, private
oracle behavior, private runner state, or application-specific backend logic
into the core repository.

This document is a public contract surface. It does not implement a report
schema, checker, API route, fixture, runner, or validation suite.

## Public Concepts

- `ExternalValidationSuite`: an external consumer that exercises public
  WorldEngine contracts and may return redacted evidence.
- `ReadinessSurface`: a public API, CLI, schema, exported contract, report
  format, or documented evidence bundle that external validation may consume.
- `ReadinessClaim`: a scoped statement about what has been prepared or
  verified.
- `RedactedValidationReport`: a report that records public behavior,
  compatibility notes, pass/fail/blocked/skipped state, and unresolved
  findings without leaking external-world internals.
- `RedactionConfirmation`: an explicit report field or review statement that
  confirms forbidden consumer details were removed.
- `CompatibilityEvidence`: current-session command or checker evidence tied
  to a public WorldEngine surface.

## Readiness Claim Taxonomy

Allowed claim values:

- `contract ready`: public semantics and boundaries are documented and
  reviewed.
- `report format ready`: a redacted report format or schema is documented or
  implemented and reviewed.
- `core-side compatibility ready`: current-session evidence proves the
  in-scope core surfaces remain compatible with the reviewed contract.
- `external suite pass`: a specific external suite ran against public
  surfaces and returned accepted redacted PASS evidence.
- `blocked`: a required check could not run and the blocker is recorded.
- `skipped`: a check was intentionally not run and the reason is recorded.
- `out of scope`: a check or claim belongs to a future version or external
  repository.

Forbidden claim shortcuts:

- Do not use `ready`, `passed`, `clean pass`, `product ready`, or `projection
  ready` without a scoped taxonomy value and evidence source.
- Do not treat historical v0.6 evidence as current v0.7 PASS evidence.
- Do not treat manual observation as an external suite PASS source.

## Required Redaction Rules

Redacted validation evidence stored in this repository must not include:

- concrete external world names.
- character names.
- location names.
- story rules.
- seed data.
- private transcripts.
- UI selectors.
- hidden reset API details.
- private fixture repository paths.
- validation oracle internals.
- non-redacted external event payloads.

Abstract identifiers such as `external-suite-001`,
`target-redacted-001`, `scenario-001`, and `contract-surface-001` are allowed.

## Required Report Semantics

A future machine-readable report schema or checker must preserve:

- report id.
- engine commit or version reference.
- public contract surface exercised.
- external suite id.
- redacted target id.
- capability area.
- abstract scenario id.
- high-level public goal.
- status: `pass`, `fail`, `blocked`, `skipped`, or `out_of_scope`.
- observed public behavior.
- redacted evidence summary.
- compatibility notes.
- unresolved P1/P2/P3 findings.
- redaction confirmation.

`pass` is allowed only when the report describes public behavior and the
redaction confirmation is true. `blocked`, `skipped`, and `out_of_scope` are
not pass equivalents.

## Compatibility Requirements

- Existing runtime, event, archive, params, Agent loop, memory, generation,
  API envelope, and dashboard behavior remain unchanged by this contract.
- Existing `docs/contracts/external-fixture-runner-contract.md` remains
  compatible. This contract adds readiness taxonomy and report semantics.
- Future schema/checker implementation must be additive and must not require
  private consumer details.
- Future external suite evidence must describe requested core changes as
  generic engine capability gaps, not consumer-specific feature requests.

## Authorization Criteria For 0.7.2

`0.7.2-validation-report-schema-and-redaction-checker` may start only after a
review confirms:

- this contract is review complete.
- report status values and redaction rules are unambiguous.
- forbidden leaked details are testable by a generic checker.
- `blocked`, `skipped`, and `out_of_scope` are distinct from `pass`.
- no concrete validation world or private oracle detail is required.
- implementation authorization remains closed until `0.7.2` records
  `implementation_authorized: yes`.

## Non-Goals

- Do not implement the schema/checker in this contract.
- Do not run an external validation suite.
- Do not add validation fixtures, private runner imports, or product-specific
  backend behavior.
- Do not claim product readiness or v0.8 projection application readiness.

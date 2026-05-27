# Technical Design

## Design Summary

This package is documentation-only. The design output is a public contract
that describes how an external runner may invoke WorldEngine through reviewed
surfaces and how redacted reports may be returned as evidence.

No code design, schema design, API implementation, fixture implementation, or
test implementation is introduced.

## Contract Structure

`docs/contracts/external-fixture-runner-contract.md` contains:

- purpose and consumer boundary.
- public concepts.
- allowed public consumption surfaces.
- v0.3 contract chain.
- redacted validation report shape.
- required redaction rules.
- compatibility constraints.
- forbidden inferences.
- acceptance requirements.
- handoff rules.

## External Runner Flow

The documented flow is:

1. External runner selects a public WorldEngine contract surface.
2. External runner invokes WorldEngine outside this repository.
3. External runner records observed public behavior.
4. External runner redacts consumer-specific internals.
5. External runner produces a report using
   `docs/validation-report-template.md`.
6. WorldEngine stores or reviews only the redacted report and any generic
   engine follow-up.

## Redaction Model

Reports may include abstract identifiers:

- `external-suite-001`
- `target-redacted-001`
- `scenario-001`

Reports must not include concrete external-world names, characters, locations,
story rules, seed data, oracle internals, UI selectors, hidden reset APIs,
private repository paths, or non-redacted payloads.

## Verification Design

Documentation verification is based on:

- file existence checks.
- status synchronization checks.
- contract heading and required-term checks.
- redaction field checks against `docs/validation-report-template.md`.
- sentinel concrete-anchor no-match checks.
- implementation-scope no-change checks.

Backend, frontend, runtime, API, E2E, Agent smoke, and build tests are not
part of this package because it changes documentation only.

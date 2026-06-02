# Technical Design

## Current State

WorldEngine already has:

- `docs/external-fixture-boundary.md`.
- `docs/contracts/external-fixture-runner-contract.md`.
- `docs/validation-report-template.md`.
- v0.6 implementation evidence that is handoff context only.
- parent v0.7 campaign docs and reviewed `0.7.0` routing baseline.

It does not yet have a dedicated external-validation readiness contract or
projection consumer contract.

## Documentation Structure

This package adds:

```text
docs/contracts/external-validation-readiness-contract.md
docs/contracts/projection-consumer-contract.md
docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/
```

The contract docs are documentation-only public surfaces. They do not create
schemas, checkers, APIs, manifests, projection payloads, or tests.

## Contract Content

`external-validation-readiness-contract.md` defines:

- public readiness concepts.
- readiness claim taxonomy.
- redacted report semantics.
- required redaction rules.
- compatibility requirements.
- authorization criteria for `0.7.2`.

`projection-consumer-contract.md` defines:

- projection consumer concepts.
- read-only consumer boundary.
- allowed future consumer surfaces.
- redaction and bounded-exposure rules.
- projection readiness taxonomy.
- authorization criteria for later projection implementation packages.

## Affected Surfaces

Documentation only:

- v0.7 parent and child package docs.
- `docs/contracts/external-validation-readiness-contract.md`.
- `docs/contracts/projection-consumer-contract.md`.

No runtime, schema, API, frontend, test, checker, fixture, migration, external
repository, generated result, or legacy implementation surface is affected.

## Compatibility Strategy

- Keep `external-fixture-runner-contract.md` compatible.
- Add readiness taxonomy and projection boundary docs without changing public
  runtime/API behavior.
- Explicitly distinguish contract readiness from external suite PASS,
  projection app readiness, product readiness, and current-session validation.

## Anti-Drift Rules

- Parent and child status surfaces must agree on active child and route.
- Contract docs must not contain concrete external world or product-specific
  examples.
- Contract docs must not imply implementation authorization.
- Review evidence must record code tests as not run because this is
  documentation-only.

## Risks

- Readiness language could imply a product or external-suite PASS claim.
- Projection consumer wording could drift into v0.8 application readiness.
- Report semantics could allow private details into future evidence.
- A later checker could confuse `blocked`, `skipped`, or `out_of_scope` with
  `pass`.

The test plan uses documentation checks, scope guards, forbidden-content
sentinels, and subagent review to catch these risks.

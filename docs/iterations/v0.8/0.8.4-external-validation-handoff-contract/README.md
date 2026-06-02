# 0.8.4 External Validation Handoff Contract

Status: review complete
Type: documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## Purpose

This package defines the public handoff contract WorldEngine may expose to a
future external validation function. It tells future packages what the core
repository may name, classify, and reference without defining how the external
validator connects, runs, judges private scenarios, or stores private evidence.

The handoff contract bridges:

```text
reviewed v0.8 core readiness surfaces
  -> public handoff surface identifiers
  -> redacted evidence reference rules
  -> blocked/skipped/out-of-scope classification
  -> later core-side smoke evidence
```

## Current State

Current v0.8 has:

- `0.8.1` minimum working-state claim taxonomy.
- `0.8.2` observable public surface boundaries.
- `0.8.3` bounded generation -> runtime -> Agent loop core-readiness evidence.
- v0.7 handoff context for redacted validation reports, readiness manifests,
  projection read-model contracts, and V07-CR checker/docs repair.

The missing slice is a v0.8-specific handoff vocabulary that keeps public
evidence references useful for later validation while preventing private
validator details from entering the core repository.

## Handoff Contract Summary

WorldEngine may expose or record only public, generic handoff facts:

- handoff surface ids.
- public contract surface references.
- redacted evidence reference ids and repository-relative paths.
- evidence class and status values.
- redaction confirmation.
- forbidden-detail review.
- blocker, skipped, and out-of-scope rationale.
- compatibility notes and unresolved finding classification.

WorldEngine must not expose or record:

- external validator connection details.
- external validator commands or private runner state.
- private scenarios, oracle internals, product UI selectors, app repository
  layout, private transcripts, screenshots, paths, world data, product content,
  secrets, provider traces, raw prompts, or non-redacted external event
  payloads.

## Scope

This package is documentation-only. It may create the 0.8.4 package documents,
Chinese mirrors, and parent v0.8 status/review updates. It does not add
schemas, checkers, templates, API routes, backend tests, frontend code,
fixtures, generated artifacts, migrations, external repositories, or
`backend/worldengine/` files.

## Handoff

This package hands `0.8.5-core-working-state-smoke-evidence` a public
classification contract for later core-side evidence. It does not hand off
external validation PASS, product readiness, projection application readiness,
frontend/E2E PASS, Agent smoke PASS, autonomous PASS, generation quality PASS,
or final v0.8 readiness.

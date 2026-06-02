# Projection Read Model Contract

Status: reviewed contract / v0.7.9 checker repair context

## Purpose

This contract defines public, read-only projection read-model families that
future external consumers may use to understand WorldEngine state and evidence
without entering private runtime, fixture, or product-application scope.

This is not an API implementation, projection application, product dashboard,
frontend route, persistence model, migration, reset path, or write contract.

## Source Contract

This contract refines the boundary in
`docs/contracts/projection-consumer-contract.md`.

The machine-checkable schema lives in
`docs/contracts/projection-read-model-schema.json`.

The schema is reviewed as a public contract artifact. It is not projection
readiness PASS, product readiness PASS, external consumer PASS, or v0.8
readiness.

## Required Read Model Families

The schema must expose these read-only families:

- `runtime_summary`
- `event_timeline_summary`
- `agent_loop_summary`
- `memory_context_summary`
- `generation_readiness_summary`
- `readiness_manifest_summary`
- `redacted_report_summary`

Each family is a bounded public summary and must include:

- a family `id`.
- a `version`.
- `read_only: true`.
- non-empty `allowed_fields`.
- non-empty `redaction_notes`.
- `no_write_capability: true`.

## Public Field Boundary

Allowed fields are limited to public identifiers, public references, statuses,
counts, ranges, compatibility claims, finding counts, and bounded summaries.

Allowed fields must not expose or imply:

- write, reset, persistence, migration, or private runner behavior.
- projection app state or product UI state.
- raw memory records.
- prompts, private traces, private transcripts, provider secrets, or UI
  selectors.
- non-redacted external event payloads.
- concrete external validation worlds, maps, locations, character names, story
  rules, seed data, or private fixture paths.

## Forbidden Capabilities

The public schema must mark these capabilities as forbidden:

- `write_api`
- `reset_api`
- `persistence`
- `migration`
- `private_runner_hook`
- `product_ui`
- `projection_app_behavior`
- `consumer_specific_backend_behavior`
- `raw_memory_export`
- `prompt_trace_export`
- `private_transcript_export`
- `event_payload_export`

These entries are exclusion rules, not implemented features.

## Compatibility

- Existing runtime, API, dashboard, Agent loop, memory, generation, and event
  behavior remains unchanged.
- The contract is additive and versioned.
- API-backed projection surfaces require a later reviewed package.
- This contract does not claim projection application readiness, product
  readiness, external consumer PASS, runtime/API/frontend PASS, or v0.8
  readiness.

## Validation

Use:

```bash
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
```

The checker validates required families, read-only markers, no-write
capability, safe allowed fields, public source paths, redaction rules, and
synthetic forbidden-detail markers.

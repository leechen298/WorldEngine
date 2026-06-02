# Technical Design

## Current State

`0.7.1` defines projection consumer boundaries and `0.7.3` exposes public
contract discovery through a readiness manifest. WorldEngine does not yet have
a concrete public contract for projection read-model payload families.

## Implementation Structure

Planned implementation files:

```text
docs/contracts/projection-read-model-contract.md
docs/contracts/projection-read-model-schema.json
tools/testing/validate_projection_read_model_contract.py
tools/testing/test_validate_projection_read_model_contract.py
```

## Schema Shape

The schema should define a contract object with:

- `contract_id`
- `contract_version`
- `source_contract`
- `read_model_families`
- `forbidden_capabilities`
- `redaction_rules`
- `compatibility_notes`

Required `read_model_families` keys:

- `runtime_summary`
- `event_timeline_summary`
- `agent_loop_summary`
- `memory_context_summary`
- `generation_readiness_summary`
- `readiness_manifest_summary`
- `redacted_report_summary`

Each read-model family should include:

- `id`
- `version`
- `read_only`
- `allowed_fields`
- `redaction_notes`
- `no_write_capability`

## Checker Flow

The checker should:

1. Load a JSON projection read-model contract.
2. Validate required top-level fields and read-model families.
3. Validate each family is read-only and has no write capability.
4. Validate allowed fields are public identifiers or bounded summaries only.
5. Reject forbidden capabilities such as write APIs, reset APIs, persistence,
   migrations, private runner hooks, product UI, or projection app behavior.
6. Reject synthetic private-detail markers.
7. Print deterministic `FAIL:` lines or one deterministic `PASS:` line.

## Test Strategy

Focused tests should cover:

- valid contract passes.
- missing required family fails for the required family set:
  `runtime_summary`, `event_timeline_summary`, `agent_loop_summary`,
  `memory_context_summary`, `generation_readiness_summary`,
  `readiness_manifest_summary`, and `redacted_report_summary`.
- family with `read_only: false` fails.
- family with `no_write_capability: false` fails.
- write/reset/persistence/private-runner capability markers fail.
- raw memory/prompt/transcript/event payload markers fail.
- CLI returns `0` for valid contract and `1` for invalid contract.

## Compatibility Strategy

- Keep implementation schema/checker only; do not add API routes.
- Keep all payload families generic and abstract.
- Preserve runtime/API/frontend/dashboard behavior.
- Do not update `0.7.3` manifest unless a reviewed change explicitly requires
  it.

## Anti-Drift Rules

- Parent and child status surfaces must agree before closeout.
- Projection read models must remain read-only.
- `projection consumer contract ready` is not projection application
  readiness.
- Tests must use synthetic sentinel strings for forbidden private details.

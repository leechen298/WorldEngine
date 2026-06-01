# API Reference v0.6

Status: current API reference through v0.6

Base URL in local development: `http://localhost:8000`

Chinese mirror: `api-reference-v0.6.zh.md`.

All successful responses use:

```json
{
  "code": 0,
  "data": {},
  "msg": "ok"
}
```

Errors use:

```json
{
  "code": 30,
  "msg": "Validation error",
  "data": {}
}
```

## Error Code Mapping

| HTTP status | API code |
|---:|---:|
| 400 | 10 |
| 401 | 20 |
| 403 | 21 |
| 404 | 24 |
| 409 | 29 |
| 422 | 30 |
| 500 | 50 |

## Health

### `GET /health`

Returns backend health.

Response data:

```json
{
  "status": "ok",
  "service": "worldengine-backend"
}
```

## Runtime

### `GET /runtime/state`

Returns current runtime state.

Response data:

```json
{
  "tick_id": 0,
  "world_time_seconds": 0,
  "step_seconds": 600,
  "updated_at": "2026-05-23T00:00:00+00:00"
}
```

### `POST /runtime/step`

Advances runtime by one step and returns the new runtime state.

Side effects:

- increments `tick_id`.
- increments `world_time_seconds`.
- appends `tick.advanced`.
- runs world modules and appends module events.
- may trigger archive snapshot/summary creation.

## World Timeline

### `GET /world/events`

Returns newest-first events.

Query params:

| Param | Type | Default | Notes |
|---|---|---:|---|
| `from_tick` | int | null | inclusive lower tick filter |
| `to_tick` | int | null | inclusive upper tick filter |
| `cursor` | string | null | event id cursor |
| `limit` | int | `20` | min `1`, max `200` |

Response data:

```json
{
  "items": [],
  "next_cursor": null,
  "has_more": false,
  "limit": 20
}
```

### `GET /world/event-steps`

Returns newest-first event groups by tick.

Query params:

| Param | Type | Default | Notes |
|---|---|---:|---|
| `from_tick` | int | null | inclusive lower tick filter |
| `to_tick` | int | null | inclusive upper tick filter |
| `cursor` | string | null | tick cursor |
| `limit` | int | `20` | min `1`, max `200` |

## World Params

### `GET /world/params`

Returns current world params as a JSON object.

### `POST /world/params/apply`

Applies world param patches after static validation and dry-run validation.

Request body:

```json
{
  "patches": [
    {
      "op": "set",
      "path": "counter.increment",
      "value": {
        "value": 2,
        "type": "number"
      }
    }
  ]
}
```

Supported ops:

- `add`
- `set`
- `remove`

Writable paths:

| Path | Type |
|---|---|
| `counter.increment` | int |
| `heartbeat.enabled` | bool |
| `scene.weather` | string |

Reserved prefixes:

- `system`
- `runtime`
- `_internal`

Validation errors return HTTP `422` with `data.errors`. Dry-run errors also
include `data.metrics`.

## Params Agent

### `POST /world/agent/params/propose-and-apply`

Asks the params agent to propose patches for a goal and apply them if they pass
validation.

Request body:

```json
{
  "goal": "speed up the counter"
}
```

If proposals are rejected after the max attempts, the route returns HTTP `422`
with errors, metrics, and attempts in `data`.

## Agent Loop

### `POST /world/agent/loop/step`

Runs one request-scoped Agent-in-World loop step.

Request body:

```json
{
  "event_limit": 20,
  "intent": {
    "type": "noop",
    "reason": "inspect only"
  }
}
```

`intent` is optional. When omitted, the service uses a deterministic `noop`
intent. `event_limit` is bounded from `1` to `200`.

Supported action types:

- `noop`
- `params.patch`

`params.patch` uses the same patch object shape and static/dry-run validation
rules as `POST /world/params/apply`.

`perception.memory_context` is an additive v0.5 response field. It contains
bounded read-only working and episodic memory records when the process-local
memory store has matching records for the default agent/world scope. The API
does not expose memory write, seed, search, or persistence endpoints.

## World Generation

v0.6 adds request-scoped World Generation v1 APIs under `/world/generation`.
These APIs validate and preview generic `WorldSpec` payloads. They do not call
live providers, persist generated worlds, execute generated worlds as active
runtime state, or approve subjective generation quality.

Common diagnostic shape:

```json
{
  "code": "duplicate_cell_id",
  "severity": "error",
  "message": "duplicate cell id: root",
  "path": "/root/child_cells/0",
  "source_context": {}
}
```

### `POST /world/generation/preview`

Validates one generation source and returns either a public `worldspec_preview`
or diagnostics.

`source_kind` must be one of:

- `template`
- `plan`
- `imported_plan`

Exactly one matching source payload must be provided:

| `source_kind` | Required payload |
|---|---|
| `template` | `template_request` |
| `plan` | `plan_request` |
| `imported_plan` | `import_request` |

Template request example:

```json
{
  "request_id": "preview-template",
  "source_kind": "template",
  "template_request": {
    "request_id": "preview-template",
    "template": {
      "id": "template.basic",
      "version": "1",
      "root": {
        "id": "root",
        "label": "Root",
        "entity_refs": [
          { "id": "entity.root", "kind": "agent" }
        ],
        "child_cells": [],
        "metadata": { "visibility": "public" }
      },
      "metadata": { "category": "generic" },
      "constraints": {}
    },
    "seed_material": { "seed": "template-seed" },
    "constraints": {}
  }
}
```

Plan request uses the same recursive cell shape under `plan_request.plan`.
Imported-plan preview uses `import_request` with:

- `import_id`
- `plan`
- `source`
- `metadata`

`source.redacted` must be true for AI-assisted plan provenance, and sensitive
keys such as prompts, provider traces, secrets, credentials, tokens, validation
oracles, `access_token`, `apiKey`, and `providerTrace` are rejected. Redacted
usage metrics such as `prompt_tokens`, `completion_tokens`, `total_tokens`,
`token_count`, `token_usage`, and `cached_tokens` are allowed.

Passed response data:

```json
{
  "request_id": "preview-template",
  "source_kind": "template",
  "validation_status": "passed",
  "metadata": {
    "generation_id": "generation-123",
    "request_id": "preview-template",
    "source_kind": "template",
    "template_id": "template.basic",
    "template_version": "1",
    "plan_id": null,
    "plan_version": null,
    "seed_digest": "abc123",
    "validation_status": "passed",
    "diagnostics_count": 0,
    "preview_summary": {
      "root_world_id": "world-generated",
      "root_label": "Root",
      "total_cell_count": 1,
      "max_child_depth": 1,
      "entity_ref_count": 1
    },
    "import_source": null
  },
  "diagnostics": [],
  "worldspec_preview": {
    "schema_version": "0.2",
    "id": "world-generated",
    "label": "Root",
    "root": {
      "id": "root",
      "label": "Root",
      "kind": "world",
      "entity_refs": [],
      "child_cells": [],
      "metadata": {}
    },
    "metadata": {}
  }
}
```

Failed preview responses keep `worldspec_preview` as `null` and return
diagnostics.

### `POST /world/generation/runtime-readiness`

Checks whether a candidate `WorldSpec` can pass the loader and runtime-context
bridge without mutating runtime state.

Request body:

```json
{
  "request_id": "readiness-template",
  "source_label": "generation-123",
  "worldspec": {
    "schema_version": "0.2",
    "id": "worldspec-runtime-ready",
    "root": {
      "id": "cell-root",
      "kind": "world",
      "entity_refs": [],
      "child_cells": [],
      "metadata": {}
    },
    "metadata": {}
  }
}
```

Response data:

```json
{
  "request_id": "readiness-template",
  "validation_status": "passed",
  "loader_passed": true,
  "runtime_context_passed": true,
  "does_not_mutate_runtime": true,
  "runtime_context_summary": {},
  "diagnostics": []
}
```

### `POST /world/generation/regenerate`

Derives a new preview request from a base preview request, applies optional
seed/constraint overrides, records lineage, and runs runtime-readiness checks
when the regenerated preview passes.

Request body:

```json
{
  "request_id": "regen-success",
  "base_preview_request": {
    "request_id": "regen-preview-base",
    "source_kind": "template",
    "template_request": {
      "request_id": "regen-template-base",
      "template": {
        "id": "template.regen",
        "version": "1",
        "root": {
          "id": "root",
          "label": "Root",
          "entity_refs": [],
          "child_cells": [],
          "metadata": {}
        },
        "metadata": {},
        "constraints": {}
      },
      "seed_material": { "seed": "base-seed" },
      "constraints": {}
    }
  },
  "parent_generation_id": "generation-parent",
  "reason": "operator requested a new seed",
  "seed_material": { "seed": "regen-seed" },
  "constraints": { "max_child_cells": 3 }
}
```

Response data contains:

- `validation_status`
- `lineage`
- `preview`
- `runtime_readiness`
- `diagnostics`

`lineage.changed_fields` records whether `seed_material` or `constraints`
changed from the base preview request.

## Archive

### `GET /world/snapshots`

Returns saved snapshots.

Query params:

| Param | Type | Default |
|---|---|---:|
| `from_tick` | int | null |
| `to_tick` | int | null |
| `limit` | int | `200` |
| `order` | `asc` or `desc` | `asc` |

### `GET /world/snapshots/{snapshot_id}`

Returns a snapshot by id, or HTTP `404` if not found.

### `GET /world/summaries`

Returns archive summaries.

Query params:

| Param | Type | Default |
|---|---|---:|
| `limit` | int | `200` |
| `order` | `asc` or `desc` | `asc` |

### `GET /world/summaries/{summary_id}`

Returns a summary by id, or HTTP `404` if not found.

## Current API Limits

- All runtime/archive/event/memory state is process-local and in-memory.
- No authentication or tenant boundary exists.
- No public memory read/write/search API exists.
- No durable persistence exists for generated worlds, memory, runtime, archive,
  or event state.
- Loaded or generated `WorldSpec` data is not executed as active recursive
  runtime state.
- World generation APIs are generic preview/readiness surfaces only; they do
  not call live providers or expose generation-quality approval.

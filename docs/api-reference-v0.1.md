# API Reference v0.1

Status: current API reference

Base URL in local development: `http://localhost:8000`

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

Response data:

```json
{
  "items": [
    {
      "tick_id": 1,
      "world_time_seconds": 600,
      "event_count": 3,
      "created_at": "2026-05-23T00:00:00+00:00",
      "items": []
    }
  ],
  "next_cursor": null,
  "has_more": false,
  "limit": 20
}
```

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

Response data on success:

```json
{
  "applied": true,
  "patches": [],
  "attempts": 1
}
```

If proposals are rejected after the max attempts, the route returns HTTP `422`
with errors and metrics.

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

- All runtime/archive/event state is process-local and in-memory.
- No authentication or tenant boundary exists.
- No stable external recursive-world contract exists.
- Event schema is minimal.
- API docs describe current v0.1 behavior only.

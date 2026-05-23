# API Reference v0.1

Status: current API reference

英文版本：`api-reference-v0.1.md`。

Local development base URL: `http://localhost:8000`

所有 successful responses 使用：

```json
{
  "code": 0,
  "data": {},
  "msg": "ok"
}
```

Errors 使用：

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

返回 backend health。

Response data：

```json
{
  "status": "ok",
  "service": "worldengine-backend"
}
```

## Runtime

### `GET /runtime/state`

返回 current runtime state。

Response data：

```json
{
  "tick_id": 0,
  "world_time_seconds": 0,
  "step_seconds": 600,
  "updated_at": "2026-05-23T00:00:00+00:00"
}
```

### `POST /runtime/step`

推进 runtime 一个 step，并返回新的 runtime state。

Side effects：

- increment `tick_id`。
- increment `world_time_seconds`。
- append `tick.advanced`。
- 运行 world modules 并 append module events。
- 可能触发 archive snapshot/summary creation。

## World Timeline

### `GET /world/events`

返回 newest-first events。

Query params：

| Param | Type | Default | Notes |
|---|---|---:|---|
| `from_tick` | int | null | inclusive lower tick filter |
| `to_tick` | int | null | inclusive upper tick filter |
| `cursor` | string | null | event id cursor |
| `limit` | int | `20` | min `1`, max `200` |

Response data：

```json
{
  "items": [],
  "next_cursor": null,
  "has_more": false,
  "limit": 20
}
```

### `GET /world/event-steps`

返回按 tick 分组的 newest-first event groups。

Query params：

| Param | Type | Default | Notes |
|---|---|---:|---|
| `from_tick` | int | null | inclusive lower tick filter |
| `to_tick` | int | null | inclusive upper tick filter |
| `cursor` | string | null | tick cursor |
| `limit` | int | `20` | min `1`, max `200` |

Response data：

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

返回 current world params，格式为 JSON object。

### `POST /world/params/apply`

在 static validation 和 dry-run validation 后应用 world param patches。

Request body：

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

Supported ops：

- `add`
- `set`
- `remove`

Writable paths：

| Path | Type |
|---|---|
| `counter.increment` | int |
| `heartbeat.enabled` | bool |
| `scene.weather` | string |

Reserved prefixes：

- `system`
- `runtime`
- `_internal`

Validation errors 返回 HTTP `422`，并包含 `data.errors`。Dry-run errors 还包含 `data.metrics`。

## Params Agent

### `POST /world/agent/params/propose-and-apply`

请求 params agent 根据 goal 提出 patches，并在通过 validation 后应用。

Request body：

```json
{
  "goal": "speed up the counter"
}
```

成功时 response data：

```json
{
  "applied": true,
  "patches": [],
  "attempts": 1
}
```

如果 proposals 在 max attempts 后仍被 rejected，route 返回 HTTP `422`，并带 errors 和 metrics。

## Archive

### `GET /world/snapshots`

返回 saved snapshots。

Query params：

| Param | Type | Default |
|---|---|---:|
| `from_tick` | int | null |
| `to_tick` | int | null |
| `limit` | int | `200` |
| `order` | `asc` or `desc` | `asc` |

### `GET /world/snapshots/{snapshot_id}`

按 id 返回 snapshot；找不到时返回 HTTP `404`。

### `GET /world/summaries`

返回 archive summaries。

Query params：

| Param | Type | Default |
|---|---|---:|
| `limit` | int | `200` |
| `order` | `asc` or `desc` | `asc` |

### `GET /world/summaries/{summary_id}`

按 id 返回 summary；找不到时返回 HTTP `404`。

## Current API Limits

- 所有 runtime/archive/event state 都是 process-local 和 in-memory。
- 没有 authentication 或 tenant boundary。
- 没有 stable external recursive-world contract。
- Event schema 是 minimal。
- API docs 只描述当前 v0.1 behavior。

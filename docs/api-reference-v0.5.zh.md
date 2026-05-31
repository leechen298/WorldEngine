# API Reference v0.5

状态：当前 API reference，覆盖到 v0.5

英文版本：`api-reference-v0.5.md`。

Local development base URL：`http://localhost:8000`

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

Validation errors 返回 HTTP `422`，并包含 `data.errors`。Dry-run errors 还包含
`data.metrics`。

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

如果 proposals 在 max attempts 后仍被 rejected，route 返回 HTTP `422`，并在 `data`
中带 errors、metrics 和 attempts。

## Agent Loop

### `POST /world/agent/loop/step`

执行一次 request-scoped Agent-in-World loop step。

Request body：

```json
{
  "event_limit": 20,
  "intent": {
    "type": "noop",
    "reason": "inspect only"
  }
}
```

`intent` 可省略。省略时 service 使用 deterministic `noop` intent。`event_limit`
被限制在 `1` 到 `200`。

Supported action types：

- `noop`
- `params.patch`

`noop` 不接受 patches，也不会修改 world params。

`params.patch` 使用与 `POST /world/params/apply` 相同的 patch object shape 和
static/dry-run validation rules。

Response data：

```json
{
  "perception": {
    "runtime": {
      "tick_id": 0,
      "world_time_seconds": 0,
      "step_seconds": 600,
      "is_running": false,
      "updated_at": null
    },
    "params": {},
    "recent_events": [],
    "runtime_context_summary": null,
    "memory_context": {
      "working_memory": [],
      "episodic_memory": []
    }
  },
  "intent": {
    "type": "noop",
    "patches": [],
    "reason": "default deterministic noop",
    "metadata": {}
  },
  "result": {
    "status": "noop",
    "applied": false,
    "action_type": "noop",
    "patches": [],
    "errors": [],
    "metrics": {},
    "params": {},
    "event_id": null,
    "message": "No action applied."
  }
}
```

`perception.memory_context` 是 v0.5 additive response field。当 process-local
memory store 中存在匹配 default agent/world scope 的记录时，它会包含 bounded
read-only working 和 episodic memory records。API 不暴露 memory write、seed、
search 或 persistence endpoints。

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

## 当前 API 限制

- 所有 runtime/archive/event/memory state 都是 process-local 和 in-memory。
- 没有 authentication 或 tenant boundary。
- 没有 public memory read/write/search API。
- Memory、runtime、archive 或 event state 都没有 durable persistence。
- Loaded `WorldSpec` data 不通过 public loader API 暴露，也不会作为 active
  recursive runtime state 执行。
- 当前没有 world generation API；该未来范围属于 v0.6。

# API Reference v0.6

状态：当前 API reference，覆盖到 v0.6

英文版本：`api-reference-v0.6.md`。

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

### `GET /world/event-steps`

返回按 tick 分组的 newest-first event groups。

Query params：

| Param | Type | Default | Notes |
|---|---|---:|---|
| `from_tick` | int | null | inclusive lower tick filter |
| `to_tick` | int | null | inclusive upper tick filter |
| `cursor` | string | null | tick cursor |
| `limit` | int | `20` | min `1`, max `200` |

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

`params.patch` 使用与 `POST /world/params/apply` 相同的 patch object shape 和
static/dry-run validation rules。

`perception.memory_context` 是 v0.5 additive response field。当 process-local
memory store 中存在匹配 default agent/world scope 的记录时，它会包含 bounded
read-only working 和 episodic memory records。API 不暴露 memory write、seed、
search 或 persistence endpoints。

## World Generation

v0.6 在 `/world/generation` 下新增 request-scoped World Generation v1 APIs。这些
API 校验并 preview generic `WorldSpec` payloads。它们不调用 live providers，不持久化
generated worlds，不把 generated worlds 作为 active runtime state 执行，也不批准
subjective generation quality。

Common diagnostic shape：

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

校验一个 generation source，并返回 public `worldspec_preview` 或 diagnostics。

`source_kind` 必须是：

- `template`
- `plan`
- `imported_plan`

必须提供一个匹配的 source payload：

| `source_kind` | Required payload |
|---|---|
| `template` | `template_request` |
| `plan` | `plan_request` |
| `imported_plan` | `import_request` |

Template request example：

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

Plan request 在 `plan_request.plan` 下使用相同 recursive cell shape。
Imported-plan preview 使用包含 `import_id`、`plan`、`source` 和 `metadata` 的
`import_request`。

AI-assisted plan provenance 要求 `source.redacted` 为 true。Prompts、provider
traces、secrets、credentials、tokens、validation oracles、`access_token`、
`apiKey` 和 `providerTrace` 等 sensitive keys 会被拒绝。Redacted usage metrics，
例如 `prompt_tokens`、`completion_tokens`、`total_tokens`、`token_count`、
`token_usage` 和 `cached_tokens` 允许保留。

Passed response data 包含：

- `request_id`
- `source_kind`
- `validation_status`
- `metadata`
- `diagnostics`
- `worldspec_preview`

Failed preview responses 会把 `worldspec_preview` 保持为 `null` 并返回 diagnostics。

### `POST /world/generation/runtime-readiness`

检查候选 `WorldSpec` 是否能通过 loader 和 runtime-context bridge，并且不修改 runtime
state。

Request body：

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

Response data 包含：

- `validation_status`
- `loader_passed`
- `runtime_context_passed`
- `does_not_mutate_runtime`
- `runtime_context_summary`
- `diagnostics`

### `POST /world/generation/regenerate`

从 base preview request 派生新的 preview request，应用可选 seed/constraint
overrides，记录 lineage，并在 regenerated preview 通过时运行 runtime-readiness
checks。

Request body：

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

Response data 包含：

- `validation_status`
- `lineage`
- `preview`
- `runtime_readiness`
- `diagnostics`

`lineage.changed_fields` 会记录 `seed_material` 或 `constraints` 是否相对 base
preview request 发生变化。

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
- Generated worlds、memory、runtime、archive 或 event state 都没有 durable
  persistence。
- Loaded 或 generated `WorldSpec` data 不会作为 active recursive runtime state
  执行。
- World generation APIs 只是 generic preview/readiness surfaces；它们不调用 live
  providers，也不暴露 generation-quality approval。

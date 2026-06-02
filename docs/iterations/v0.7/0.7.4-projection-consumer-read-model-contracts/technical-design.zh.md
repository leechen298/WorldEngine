# Technical Design

## Current State

`0.7.1` 定义了 projection consumer boundaries，`0.7.3` 通过 readiness manifest 暴露
public contract discovery。WorldEngine 还没有 projection read-model payload families 的
concrete public contract。

## Implementation Structure

Planned implementation files：

```text
docs/contracts/projection-read-model-contract.md
docs/contracts/projection-read-model-schema.json
tools/testing/validate_projection_read_model_contract.py
tools/testing/test_validate_projection_read_model_contract.py
```

## Schema Shape

Schema 应定义 contract object，包含：

- `contract_id`
- `contract_version`
- `source_contract`
- `read_model_families`
- `forbidden_capabilities`
- `redaction_rules`
- `compatibility_notes`

Required `read_model_families` keys：

- `runtime_summary`
- `event_timeline_summary`
- `agent_loop_summary`
- `memory_context_summary`
- `generation_readiness_summary`
- `readiness_manifest_summary`
- `redacted_report_summary`

每个 read-model family 应包含：

- `id`
- `version`
- `read_only`
- `allowed_fields`
- `redaction_notes`
- `no_write_capability`

## Checker Flow

Checker 应：

1. Load a JSON projection read-model contract。
2. Validate required top-level fields and read-model families。
3. Validate each family is read-only and has no write capability。
4. Validate allowed fields are public identifiers or bounded summaries only。
5. Reject forbidden capabilities，例如 write APIs、reset APIs、persistence、
   migrations、private runner hooks、product UI 或 projection app behavior。
6. Reject synthetic private-detail markers。
7. 对每个 error 打印 deterministic `FAIL:` line，成功时打印一个 deterministic `PASS:` line。

## Test Strategy

Focused tests 覆盖：

- valid contract passes。
- missing required family fails for the required family set：
  `runtime_summary`、`event_timeline_summary`、`agent_loop_summary`、
  `memory_context_summary`、`generation_readiness_summary`、
  `readiness_manifest_summary` 和 `redacted_report_summary`。
- family with `read_only: false` fails。
- family with `no_write_capability: false` fails。
- write/reset/persistence/private-runner capability markers fail。
- raw memory/prompt/transcript/event payload markers fail。
- CLI returns `0` for valid contract and `1` for invalid contract。

## Compatibility Strategy

- 保持 implementation schema/checker only；不添加 API routes。
- 所有 payload families 保持 generic and abstract。
- Preserve runtime/API/frontend/dashboard behavior。
- 不更新 `0.7.3` manifest，除非 reviewed change 明确要求。

## Anti-Drift Rules

- Parent and child status surfaces closeout 前必须一致。
- Projection read models 必须保持 read-only。
- `projection consumer contract ready` 不是 projection application readiness。
- Tests 必须使用 synthetic sentinel strings 检查 forbidden private details。

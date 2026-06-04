# Technical Design

英文版本：`technical-design.md`。

## Implementation Structure

预期 runtime repair 是以下文件中的窄 wording change：

```text
backend/app/api/routes/world.py
```

当前 `submit_director_guidance` response 使用了包含 private/internal marker terms
的 public-facing text。修复应替换为 public-safe wording，例如：

```text
Public director guidance was accepted as external world-environment direction.
No direct internal state mutation was performed.
```

最终 wording 必须避开所有 known public evidence markers，也不应命名受保护的 private
Agent concepts。

## Test Structure

focused tests 应位于：

```text
backend/app/tests/test_public_handoff_contract_api.py
```

当前 test 断言 `"private memory"` 出现在 `public_explanation` 中；implementation
必须先把它改成 redaction-boundary assertion，并确认该 assertion 会在当前实现上失败。

test 应检查：

- response status 仍是 `200`。
- response status 仍是 `accepted`。
- `applied_event_id` 存在。
- `public_explanation` 不包含 forbidden evidence markers。
- event payload 仍省略 raw `instruction_text`。
- event payload 仍省略 private state markers。

如果 autonomous checker 对 full lifecycle operation logs 中 direct API operation
records 缺少 regression coverage，则按本仓库现有 testing convention 在
`tools/testing/tests/` 或对应位置补充 focused checker coverage。不得削弱现有 checker
rules。

## Data And Control Flow

```text
Validation Client UI
  -> Validation Client public API
  -> WorldEngine POST /worlds/{world_id}/director-guidance
  -> WorldEngine appends director.guidance.accepted event
  -> WorldEngine returns DirectorGuidanceResponse.public_explanation
  -> Validation Client evidence exporter scans public evidence
  -> WorldEngine saved-result checker validates exported evidence
```

本 package 只改变 public explanation text，并在必要时补 checker regression coverage。
它不添加新的 private mutation path。

## Compatibility Strategy

- response schema fields 不变。
- operation id 不变。
- event type 和 event payload shape 不变；不得加入 raw instruction text。
- public manifest 和 world creation behavior 不变。

## Anti-Drift Rules

- 不要通过在 public API output 中拼出 private marker terms 来描述 private boundary
  guarantees。
- 不要把 evidence redaction responsibility 从 public output 转嫁给 Validation Client。
- 不要把旧 failed result 在 code changes 后改称 passing；它仍是 historical FAIL evidence。
- 没有新的 result directory 通过 documented checker 时，不声明 full lifecycle PASS。

# Technical Design

## Implementation Structure

implementation 应保持 additive，并围绕现有 public handoff manifest path 展开。

`backend/app/schemas/world.py` 中的 schema changes：

- 添加 status taxonomy 和 checker-handoff model types。
- 扩展 `PublicSurface`，加入 optional/defaulted MVP/debug metadata：maturity、validation
  status、required-for-MVP flag 和 notes。
- 扩展 `HandoffManifest`，加入 optional/defaulted v0.10 fields，例如
  `mvp_contract_version`、`manifest_status`、`status_taxonomy`、`checker_handoff`、
  `validation_client_role`、`provider_owner`、`evaluator_role` 和
  `worldline_branch_semantics`。

`backend/app/api/routes/world.py` 中的 route changes：

- 保持 `/manifest` path 和 operation id 不变。
- 保持现有 public surface list entries。
- 为现有 surfaces 添加 v0.10 MVP/debug metadata。
- 将计划中的 session/debug surfaces 标为 `unavailable` 或 `not_run`，而不是伪装成已实现。
- 增加 warnings/blockers，清楚区分 provider readiness 和 live proof、planned session surfaces
  和 available functionality。

`backend/app/tests/test_public_handoff_contract_api.py` 中的 test changes：

- 断言 legacy fields 仍存在。
- 断言 `worldengine_version` 和 `mvp_contract_version` 描述 v0.10。
- 断言 `status_taxonomy` 包含 `pass`、`fail`、`blocked` 和 `not_run`。
- 断言 planned session surfaces 在 implementation 前没有被标记为 available/pass。
- 断言 redaction flags 仍为 false，且 serialized manifest output 不包含已知 secret/raw markers。
- 断言 branch terminology 避免 parent/source-world semantics。

## Affected Files

Implementation files：

- `backend/app/schemas/world.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_public_handoff_contract_api.py`

Documentation files：

- `docs/iterations/v0.10/0.10.1-mvp-public-manifest-and-debug-handoff/` 下的文件。
- 根据需要更新 v0.10 parent route/review files。

## Data / Control Flow

本包唯一改变的 runtime-facing flow 是：

```text
GET /manifest
-> provider_readiness_from_env()
-> HandoffManifest with additive v0.10 debug metadata
-> redacted public JSON response
```

不创建 world session state。不执行 runtime tick。不进行 provider live call。不生成 checker result。

## Compatibility Strategy

- 保持现有 field names 和 response path。
- 新增字段带 default values，保持 schema construction 简单。
- 保留现有 `public_surfaces` list，同时扩展其 entries。
- 对 unavailable future surfaces 诚实标记，不省略所有 future handoff expectations，也不报告为
  pass。
- 保持 redaction booleans 默认 false，并用测试覆盖已知 leak markers。

## Anti-Drift Rules

- 如果 implementation 需要 allowed list 以外的文件，停止并更新本 package 供 review 后再编辑。
- 如果需要 session state 或 runtime behavior，停止并交接到 `0.10.2` 或后续。
- 如果需要 checker/fixture work，停止并记录 blocker 或修订 package。
- 如果 future surface 不可用，标记为 `unavailable`、`blocked` 或 `not_run`，绝不标记为 `pass`。
- worldline 或 replay branch semantics 不使用 parent/source-world wording。

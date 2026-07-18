# Contract

## Public Concepts

本包可以引入或细化以下 public manifest concepts：

- `mvp_contract_version`：public MVP debug contract version，预期标识 v0.10，同时不破坏现有
  legacy fields。
- `worldengine_version`：必须把 public discovery 推进到 `v0.10`，同时保持 additive
  compatibility。
- `manifest_status`：`pass`、`fail`、`blocked` 或 `not_run` 之一；当前 manifest 可以诚实地把
  future session surfaces 标为 `blocked` 或 `not_run`。
- `status_taxonomy`：`pass`、`fail`、`blocked` 和 `not_run` 的 public definitions，避免
  client 自行发明 UI-only meanings。
- `mvp_debug_surface`：discoverable public API surface，包含 path、method、operation id、
  availability、maturity、validation status，以及是否为 v0.10 MVP path 所必需。
- `checker_handoff`：redacted public skeleton，命名 checker-compatible artifacts、expected
  result values、evaluator authority 和 unsupported items。
- `validation_client_role`：`display_export_only`。
- `provider_owner`：`worldengine`。
- `evaluator_role`：`worldengine_checker_or_second_agent_review`。
- `worldline_branch_semantics`：branches 是用于 replay/debugging 的可比较时间线分支，不是
  parent/child worlds、source worlds 或 origin trees。

## Compatibility Requirements

- 现有 manifest fields 保持可用且 additive-compatible：`schema_version`、
  `worldengine_version`、`provider`、`public_surfaces`、`redaction`、`blockers` 和
  `warnings`。
- 现有 public surface entries 对当前 consumers 仍有效。
- 现有 provider readiness behavior 继续是 redacted readiness summary，不是 live-call proof。
- 新字段必须在 schema 层面 optional/defaulted，使旧 tests 和 clients 可忽略。
- Status values 必须保留 `pass`、`fail`、`blocked` 和 `not_run`；不得映射为 UI-only labels。
- Public payloads 不得包含 provider secrets、raw model labels、raw prompts、raw responses、
  raw traces、private memory、hidden context、raw thought 或 private evaluator data。

## Allowed Changes

- 在 `backend/app/schemas/world.py` 扩展 additive manifest/debug handoff models 和 fields。
- 更新 `backend/app/api/routes/world.py` 的 `/manifest` 构造和 public surface metadata。
- 更新 `backend/app/tests/test_public_handoff_contract_api.py`，加入 v0.10 manifest fields、
  compatibility、status taxonomy、redaction、blocked/not_run honesty 和 branch terminology
  的 focused tests。
- 更新 package 和 parent v0.10 docs/reviews。

## Forbidden Changes

- 不实现 Validation Client repository behavior。
- 不实现 session storage、session APIs、session runtime、snapshot evidence、dashboard flow、
  persistence、migrations、generated-result writing、provider live calls、checker fixtures 或
  external validation。
- 除非 documentation review 先记录并批准 scope change，否则不修改 allowed file list 以外的文件。
- 不加入 concrete demo worlds、maps、characters、locations、resources、story rules、seed
  data、UI selectors 或 application-specific backend logic。
- 不修改 `backend/worldengine/`。
- 不声明 v0.10 runnable session PASS、dashboard PASS、external validation PASS、provider live
  PASS、Agent autonomy PASS 或 full MVP PASS。

## North Star Check

本包通过明确 public discovery 和 evidence handoff 来强化 WorldEngine 作为 generic engine 的定位。
它保持 external clients 是 public evidence 的 consumers/exporters，而不是 provider behavior、
world generation、runtime mutation 或 evaluation authority 的 owners。

## Out-of-Scope Follow-ups

- `0.10.2`：actual world session contract and state store。
- `0.10.3`：worldview input to runnable session creation。
- `0.10.4`：bounded session runtime and snapshot evidence。
- `0.10.5`：dashboard MVP session flow。
- `0.10.6`：v0.10 validation and handoff。

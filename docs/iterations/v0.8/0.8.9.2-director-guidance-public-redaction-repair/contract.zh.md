# Contract

英文版本：`contract.md`。

## Public Concepts

- `Public director guidance explanation`：public-facing status sentence，用来说明
  director guidance 已作为 external/world-environment guidance 被接受，但不命名
  private 或 internal WorldEngine markers。
- `Public evidence marker`：autonomous checker 或 external evidence redaction
  pipeline 会拒绝的 marker，包括 `api_key`、`apikey`、`authorization`、
  `credential`、`hidden_context`、`private_prompt`、`provider_secret`、
  `raw_request`、`raw_response`、`self_state` 以及等价 private Agent internals。
- `Direct API operation-log rejection`：full lifecycle operation log 不得把 direct
  API calls 记录成 Agent operations。Public API evidence 应进入
  `api-summary.json`。

## Allowed Changes

implementation 只能修改以下 WorldEngine 文件和 surface：

```text
backend/app/api/routes/world.py
backend/app/tests/test_public_handoff_contract_api.py
tools/testing/validate_agent_autonomous_result.py
tools/testing/test_validate_agent_autonomous_result.py
docs/iterations/v0.8/0.8.9.2-director-guidance-public-redaction-repair/
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
docs/testing/results/2026-06-04-worldengine-full-lifecycle-validation.md
docs/testing/results/2026-06-04-worldengine-full-lifecycle-validation.zh.md
```

只有当当前 tests 或 checker behavior 不能证明 full lifecycle scenario 的 direct API
operation-log rejection 时，才可修改 testing tool files。

## Forbidden Changes

- 不修改 `backend/worldengine/`。
- 不修改 Validation Client repository。
- 不修改 frontend code。
- 不修改 provider credential storage，不增加 live provider calls。
- 不添加 concrete demo-world content、validation-world seed data、private
  validation oracle logic、app-specific backend behavior、maps、characters、
  locations、resources 或 story rules。
- 不放松 redaction、evidence integrity 或 operation-log rules 来让失败 run 通过。
- 不修改无关 WorldEngine API response shapes。
- 不声明 external validation PASS、Codex autonomous validation PASS、human
  validation PASS、product readiness 或 v0.8 final closeout changes。

## Compatibility Requirements

- `POST /worlds/{world_id}/director-guidance` 必须保持 OpenAPI-discoverable，
  operation id 仍为 `submit_director_guidance`。
- endpoint 必须继续接受 public direction，并 append public
  `director.guidance.accepted` event。
- event payload 必须继续省略 raw `instruction_text`。
- public response 必须保持对 `DirectorGuidanceResponse` 的 additive-compatible。
- 既有 `/world/*`、`/worlds`、`/manifest`、runtime、generation 和 Agent loop
  endpoints 必须保持既有行为。

## North Star Check

本 package 保持 WorldEngine generic。它只修复 external validation consumers 使用的
public contract，不向 core repository 添加 external application logic 或 concrete
validation-world content。

## Exit Criteria

- documentation/contract evaluator 没有 P0/P1 和 blocking P2。
- code changes 前明确记录 implementation authorization。
- focused test 在 public wording repair 前失败，修复后通过。
- focused backend tests 通过。
- 用 exact commands 验证 full lifecycle evidence integrity 的 saved-result checker
  behavior。
- 如果没有 `evidence_execution_authorized: yes`，focused repair closeout 可以不运行
  live full lifecycle rerun，但 `review.md` 必须把 rerun 记录为 not authorized，并将
  package verdict 限定为 focused repair evidence。
- full lifecycle PASS closeout 必须先由 review 记录
  `evidence_execution_authorized: yes`，并运行 fresh full lifecycle rerun；该 rerun
  要么 checker PASS，要么以 exact unavailable dependencies 记录 blocked。

## Out-of-Scope Follow-ups

- Validation Client evidence exporter changes。
- Human validation。
- Live provider validation。
- future direct Agent memory/self-continuity implementation。
- product readiness 或 release recertification。

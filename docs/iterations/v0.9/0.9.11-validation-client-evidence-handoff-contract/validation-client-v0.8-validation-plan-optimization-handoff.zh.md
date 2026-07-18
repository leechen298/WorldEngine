# Validation Client v0.8 测试计划优化交接文档

英文镜像：
`validation-client-v0.8-validation-plan-optimization-handoff.md`。

状态：交接文档已准备 / 外部优化迭代未开始

## 目的

本文把 WorldEngine v0.9 的验证要求交接给独立的
`WorldEngine-Validation-Client` 仓库。本文不在 WorldEngine 仓库里授权或实现
客户端代码。

目标 Validation Client 里程碑应定位为一次优化迭代，建议命名为：

```text
v0.8-worldengine-v0.9-validation-plan-optimization
```

这个迭代的目标是更新 Validation Client 的完整 WorldEngine 测试计划和证据能力，让
客户端之后可以随着 WorldEngine 的变化持续迭代。产出的客户端应成为严格的
WorldEngine v0.9 外部验证承载面：

- 只通过公开接口操作 WorldEngine。
- 展示公开生命周期证据。
- 记录人类或 Agent 可见的操作过程。
- 导出可被 WorldEngine checker 消费的 evidence bundle。
- 原样保留 `pass`、`fail`、`blocked`、`not_run`，不做美化改写。
- 不接管 provider key、provider call、LLM 生成、世界演化、Agent 自主性、
  scorecard 权威性或 PASS 判定。

## 当前权威状态

WorldEngine v0.9 是引擎行为和验证合同的权威来源。

当前 WorldEngine 事实：

- basic lifecycle validation 已经有历史 checker-level PASS 证据。
- v0.9 LLM-backed lifecycle validation 不是 PASS。
- `0.9.11-validation-client-evidence-handoff-contract` 定义了外部客户端使用的
  公开 evidence bundle 合同。
- `0.9.12-llm-backed-full-lifecycle-validation-execution` 产出了 checker-valid
  `BLOCKED` 结果，不是 live provider PASS。
- 2026-06-06 saved result 在 live LLM-backed lifecycle 执行前被阻塞，原因是
  provider 环境变量不存在，且没有完整的一键式 staged runner command。
- 尚未声明 Validation Client export PASS，也尚未声明 external validation PASS。

因此 Validation Client v0.8 必须同时能承载成功证据和阻塞证据。checker-valid
`BLOCKED` 是有效证据结果，但不是产品 PASS。

## 仓库职责拆分

WorldEngine 仓库负责：

- provider 配置和 provider 调用。
- LLM-backed 世界创建和结构化公开生成输出。
- 世界规则、参数演化、事件、快照、diff 和合法性。
- Agent 连续性、沉淀、自主性证据和公开摘要。
- checker、scorecard、scenario 合同和 PASS 权威。
- 引擎侧证据的脱敏边界。

Validation Client 仓库负责：

- 人类或 Codex 类 Agent 使用的 Web/client 工作流。
- WorldEngine 连接 preflight 和公开 surface discovery。
- operation log、UI 可见状态、API summary、截图和下载文件。
- evidence bundle 展示和导出。
- 基于公开 event、diff、snapshot、commit point 证据的 replay/fork/branch 视图。
- 第二 Agent 复核和人工交接模板。

Validation Client 不得：

- 管理或展示 provider key。
- 直接调用 DeepSeek 或任何 LLM provider。
- 生成权威世界内容。
- 计算权威参数变化或最终世界状态。
- 编写客户端脚本动作后标记成 WorldEngine Agent 自主性。
- 脱离 WorldEngine checker、scorecard 或第二 Agent 复核自行判定 PASS。
- 暴露 raw prompt、raw provider request/response、provider trace、
  authorization header、API key、Agent private memory、Agent private goal、
  raw thought、hidden context、private evaluator data、seed 或 oracle data。
- 把 narrative projection 或 diagnostic conversation 写成 canonical world event
  或 Agent memory。

## 必读文档

Validation Client v0.8 开工前应先读取这些 WorldEngine 文件：

```text
/Users/leechen/projects/WorldEnginProjects/WorldEngine/AGENTS.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/project-north-star.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/product-model.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/scope-boundaries.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/roadmap.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/README.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/llm-backed-lifecycle-validation-plan.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/README.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-suite-execution.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-artifact-contract.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-scorecard.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/second-agent-review-protocol.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/provider-live-smoke-deepseek.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-world-creation.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/world-rule-parameter-evolution.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/agent-persistent-autonomy-evidence.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-full-lifecycle-autonomous.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution/review.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md
```

同时也应读取当前 Validation Client 文档和代码：

```text
/Users/leechen/projects/WorldEngine-Validation-Client/AGENTS.md
/Users/leechen/projects/WorldEngine-Validation-Client/docs/specs/validation-client-design.md
/Users/leechen/projects/WorldEngine-Validation-Client/docs/specs/validation-client-design.zh.md
/Users/leechen/projects/WorldEngine-Validation-Client/docs/milestones/v0.7-agent-autonomous-validation/
/Users/leechen/projects/WorldEngine-Validation-Client/apps/api/app/worldengine_client.py
/Users/leechen/projects/WorldEngine-Validation-Client/apps/api/app/routes/evidence.py
/Users/leechen/projects/WorldEngine-Validation-Client/apps/api/app/routes/validation_runs.py
/Users/leechen/projects/WorldEngine-Validation-Client/apps/web/src/pages/RuntimeConsole.tsx
/Users/leechen/projects/WorldEngine-Validation-Client/apps/web/e2e/v0.7-ui-smoke.spec.ts
```

v0.7 里程碑已经提供了 operation log 和 evidence 基础，但部分 v0.7 文档仍指向
WorldEngine 0.8.9 门禁。v0.8 应把这些视为历史资料，新目标必须对齐
WorldEngine v0.9。

## 客户端能力目标

Validation Client v0.8 应在 v0.7 基础上扩展，而不是重做基础客户端。

最低能力目标：

1. 连接 WorldEngine 并记录 preflight 证据。
2. 从 `/manifest` 和 `/openapi.json` 发现公开 surfaces。
3. 创建或检查 WorldEngine-backed validation session。
4. 通过公开 runtime controls 执行 bounded lifecycle。
5. 以外部环境引导的形式提交自然语言 world direction。
6. 展示和导出 rule-linked evolution 与 event legality 证据。
7. 展示和导出 Agent continuity/autonomy 证据。
8. 把 narrative projection 与 diagnostic dialogue 展示为世界外检查面。
9. 按 v0.9 命名 artifact 和 manifest 导出 evidence bundle。
10. 在 active scenario 支持 checker 时，产出可被 WorldEngine 检查的
    saved-result directory。
11. 当 WorldEngine 缺 provider、runner、schema 或 full lifecycle 支持时，原样保留
    `BLOCKED` 和 `not_run`。

## 公开接口矩阵

Validation Client v0.8 应在可用时使用以下 WorldEngine 公开接口。如果接口不可用，
客户端必须记录 `blocked` 或 `not_run`，不能伪造操作。

| 能力 | WorldEngine 公开接口 | 客户端职责 |
| --- | --- | --- |
| Preflight | `GET /health` | 记录可达性和延迟摘要。 |
| 公开合同发现 | `GET /manifest` | 展示 provider readiness warning 和公开 surface list。不得把 readiness 当成 live-call proof。 |
| API 发现 | `GET /openapi.json` | 发现 operation id 和 URL。 |
| 基础世界创建 | `POST /worlds` | 只用于 basic lifecycle；记录是否是 generic deterministic output。 |
| 世界观生成 | `POST /world/generation/worldview` | 提交 premise，并展示公开生成世界和规则 readiness 证据。 |
| Provider live smoke | `POST /provider/live-smoke` | 只调用 WorldEngine endpoint；不得直接调用 provider 或处理 key。 |
| Runtime state | `GET /runtime/state` | 展示 tick、world time、step seconds。 |
| 单 tick | `POST /runtime/step` | 推进一个 tick，并记录 operation/API 证据。 |
| Bounded run | `POST /runtime/run` | 运行用户指定 tick 数或世界时间长度；不得默认无限运行。 |
| Pause | `POST /runtime/pause` | 暂停后续 bounded run。 |
| Resume | `POST /runtime/resume` | 恢复后续 bounded run。 |
| Events | `GET /world/events` | 展示事件时间线并导出 event evidence。 |
| Event steps | `GET /world/event-steps` | 展示按 tick 聚合的证据。 |
| Snapshots | `GET /archive/snapshots` | 在可用时展示 replay anchor 证据。 |
| World params | `GET /world/params` | 展示公开参数状态。 |
| 自然语言方向 | `POST /worlds/{world_id}/direction` | 队列化外部环境方向，并记录时间窗口证据。 |
| 旧导演引导 | `POST /worlds/{world_id}/director-guidance` | 保持 basic lifecycle 兼容；v0.9 优先使用 direction contract。 |
| 事件合法性 | `POST /worlds/{world_id}/evolution/evaluate-event` | 只把 candidate/rule set 作为公开评估输入；记录 accepted/rejected 结果。 |
| Agent 连续性 | `POST /worlds/{world_id}/agents/{agent_id}/continuity/evaluate` | 展示公开 continuity/consolidation/action evidence；不得创建 private state。 |
| 小说投影 | `POST /worlds/{world_id}/narrative/project` | 只作为外部故事/投影输出展示。 |
| 诊断对话 | `POST /worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate` | 只作为世界外检查；不得写入世界记忆。 |

## 运行控制要求

客户端 UI 应提供 bounded controls：

- 单步推进一次。
- 运行 `N` ticks。
- 在支持时运行 `N` 秒世界时间。
- 暂停。
- 继续。
- 暂停/继续后再运行一段 bounded segment。

UI 不得把世界呈现成没有明确预算的无限循环。operation log 应记录准确的运行预算、
结果摘要、tick 范围，以及运行是否被暂停或阻塞。

## Scenario 矩阵

| Scenario | 必须执行的客户端操作 | 必须导出的客户端 artifacts | 允许结论 |
| --- | --- | --- | --- |
| `worldengine-full-lifecycle-autonomous` | 创建世界、step/run ticks、读取 events/snapshots、观察 Agent action evidence、提交 direction/guidance、导出 bundle、运行 checker。 | `result.json`、`operation-log.jsonl`、`api-summary.json`、`world-lifecycle-summary.json`、截图/transcript、`redaction-scan.json`、`scorecard-summary.json`。 | PASS 只能来自 WorldEngine checker/scorecard。 |
| `provider-live-smoke-deepseek` | 发现 `/provider/live-smoke`，调用 WorldEngine endpoint，记录脱敏状态。 | `provider-live-summary.json`、`operation-log.jsonl`、`redaction-scan.json`。 | PASS/BLOCKED/FAIL 来自 WorldEngine 公开响应和 checker 规则。 |
| `llm-backed-world-creation` | 提交 premise，调用 WorldEngine-owned world generation/creation path，记录 generic fallback detection。 | `world-creation-summary.json`、public state refs、visualization refs。 | 只有 LLM-backed 且不是 deterministic generic fallback 才能 PASS。 |
| `world-rule-parameter-evolution` | 运行 bounded ticks，采集 params/events/diffs，把参数变化映射到规则。 | `world-rule-summary.json`、`rule-parameter-summary.json`、`diff-replay-summary.json`。 | 只有存在 rule-linked changes 证据才能 PASS。 |
| `rule-compliant-event-generation` | 提交 legal/illegal candidate 或 direction-linked event，记录 adjudication 和 state diff。 | `event-legality-summary.json`、event refs、diff refs。 | 只有没有 direct final-state mutation 且存在 legality evidence 才能 PASS。 |
| `agent-persistent-autonomy-evidence` | 观察多轮公开 Agent continuity evidence，包括 intent/no-intent states 和 event reactions。 | `agent-autonomy-summary.json`、public memory/thought summaries、event refs。 | 只有证据来自 WorldEngine 且不是 client-scripted action 才能 PASS。 |
| `llm-backed-full-lifecycle-autonomous` | 执行完整链路：provider smoke、world creation、rule evolution、event legality、Agent autonomy、evidence export、checker/scorecard、第二 Agent 复核。 | 完整 v0.9 evidence bundle。 | PASS 只能来自 checker/scorecard 加第二 Agent clean review。 |

用于构造 artifacts 的 direct API harvest 必须单独记录为 API evidence，不得伪装成
`operation-log.jsonl` 里的用户可见 Agent 操作。

## Evidence Bundle 合同

导出的 bundle 应支持以下结构：

```text
evidence-bundle/
  manifest.json
  result.json
  operation-log.jsonl
  api-log.jsonl
  api-summary.json
  provider-live-summary.json
  world-creation-summary.json
  world-rule-summary.json
  rule-parameter-summary.json
  event-legality-summary.json
  agent-autonomy-summary.json
  diff-replay-summary.json
  world-lifecycle-summary.json
  narrative-projection-summary.json
  diagnostic-conversation-summary.json
  redaction-scan.json
  scorecard-summary.json
  second-agent-review.md
  transcript.md
  console.log
  screenshots/
```

只有 scenario 要求的 artifacts 才必须存在，但缺失 required artifact 必须明确显示为
`blocked`、`not_run` 或 `fail`。

`manifest.json` 必须包含：

- `schema_version`
- `bundle_id`
- `scenario`
- `result_status`
- `client_role`
- `provider_owner`
- `evaluator_role`
- `created_at`
- `artifact_index`
- `redaction_status`
- `checker_contract`
- `unsupported_items`

固定值建议：

```json
{
  "client_role": "display_export_only",
  "provider_owner": "worldengine",
  "evaluator_role": "worldengine_checker_or_second_agent_review"
}
```

每个 `artifact_index` entry 应包含：

- `name`
- `path`
- `required`
- `displayable`
- `exportable`
- `producer`
- `schema_version`
- `redaction_status`

Artifact path 必须是相对路径，并且必须留在 bundle directory 内。

## Artifact 映射

| Artifact | 主要 producer | 客户端职责 |
| --- | --- | --- |
| `result.json` | Validation Client packaging / WorldEngine checker contract | 保留 scenario、final status、result dir metadata 和 unsupported items。 |
| `operation-log.jsonl` | Validation Client | 记录可见用户/Agent 操作：点击、输入、导航、导出、checker command reference。 |
| `api-log.jsonl` | Validation Client | 把 direct public API calls 和 artifact harvest 与可见操作分开记录。 |
| `api-summary.json` | Validation Client | 汇总 endpoints、status codes、latency buckets 和 redaction status。 |
| `provider-live-summary.json` | WorldEngine public endpoint / client packaging | 保留 provider class、model label、call attempted/status、latency、token bucket、failure category。 |
| `world-creation-summary.json` | WorldEngine public evidence / client packaging | 记录 premise summary、world id、creation mode、LLM-backed status、generic fallback detection。 |
| `world-rule-summary.json` | WorldEngine public evidence / client packaging | 记录公开参数、rule count、boundary conditions、legality rules、real-world rule categories。 |
| `rule-parameter-summary.json` | WorldEngine public evidence / client packaging | 记录 tick range、changed parameters、rule links、unexplained changes、fixed-counter detection。 |
| `event-legality-summary.json` | WorldEngine public evidence / client packaging | 记录 checked events、random/user-guided directions、adjudications、direct mutation detection。 |
| `agent-autonomy-summary.json` | WorldEngine public evidence / client packaging | 记录多轮公开 autonomy evidence，以及是否检测到 client scripting。 |
| `diff-replay-summary.json` | Validation Client over WorldEngine public evidence | 记录 event/snapshot/diff refs、replay support、jump targets、missing links。 |
| `world-lifecycle-summary.json` | Validation Client packaging | 汇总 creation、runtime、events、snapshots、direction、Agent evidence、export status。 |
| `narrative-projection-summary.json` | WorldEngine public projection / client packaging | 把 projection status 记录为非 canonical 外部检查。 |
| `diagnostic-conversation-summary.json` | WorldEngine public projection / client packaging | 把 diagnostic dialogue status 记录为 out-of-world inspection。 |
| `redaction-scan.json` | Validation Client and/or checker | 记录所有 artifacts 的 clean/leak 状态。 |
| `scorecard-summary.json` | WorldEngine checker/scorecard 或客户端打包 checker output | 保留 checker verdict source 和 score items。 |
| `second-agent-review.md` | 第二 Agent | 保存只读复核输出，或记录 `not_run`/`blocked` 状态。 |

## Redaction 要求

每个可展示或可导出的 artifact 都必须声明 redaction status。PASS 要求所有 blocking
flags 都是 false：

- `api_keys_included`
- `authorization_headers_included`
- `raw_prompts_included`
- `raw_provider_requests_included`
- `raw_provider_responses_included`
- `provider_traces_included`
- `private_agent_memory_included`
- `private_agent_goals_included`
- `raw_thought_included`
- `hidden_context_included`
- `private_evaluator_data_included`
- `seed_or_oracle_data_included`

如果 forbidden marker 只出现在 redaction 字段名中，scanner 应把它分类为 metadata，
而不是泄露。如果 forbidden value 出现在内容中，bundle 必须是 `fail`。

## 状态保真

Validation Client UI 可以为了可读性翻译标签，但导出的数据必须保留机器状态：

- `pass`
- `fail`
- `blocked`
- `not_run`
- `out_of_scope`，仅在 scenario contract 明确允许时使用。

不得把 `blocked`、`not_run` 或 `unsupported` 映射成 PASS。不得把绿色 UI smoke
当作 WorldEngine validation PASS。

## Validation Client 内需要创建的 v0.8 里程碑文档

Validation Client 仓库应创建新的里程碑目录：

```text
docs/milestones/v0.8-worldengine-v0.9-validation-plan-optimization/
```

建议文件：

```text
README.md
README.zh.md
intent.md
intent.zh.md
contract.md
contract.zh.md
technical-design.md
technical-design.zh.md
test-plan.md
test-plan.zh.md
plan.md
plan.zh.md
review.md
review.zh.md
scenario-operation-matrix.md
scenario-operation-matrix.zh.md
artifact-contract.md
artifact-contract.zh.md
redaction-matrix.md
redaction-matrix.zh.md
autonomous-validation-runbook.md
autonomous-validation-runbook.zh.md
second-agent-review-template.md
second-agent-review-template.zh.md
```

该里程碑应明确 supersede v0.7 中仍指向 WorldEngine 0.8.9 的过期引用，同时保留
v0.7 作为历史基础。

该里程碑应被描述为可重复执行的测试计划优化迭代，而不是一次性的兼容补丁。之后
WorldEngine 如果调整公开验证接口、scenario 合同、artifact 合同或 checker 规则，
Validation Client 可以按同样模式继续开后续优化迭代。

## Validation Client 内部建议拆分

Validation Client 可以在 v0.8 文档完成审核后，拆成以下小任务实现：

1. 文档和路由刷新。
2. WorldEngine v0.9 public surface discovery 和 capability model。
3. Evidence manifest 与 artifact-index schema。
4. provider/world/rule/event/Agent/replay summary 的命名 artifact builders。
5. Redaction scan 和 status preservation。
6. bounded run、pause、resume、additional run 的 runtime UI controls。
7. 当前规划 validation 的 scenario runner/export flow。
8. checker-compatible saved-result export。
9. scorecard、blocked/not-run items、第二 Agent review 的前端展示。
10. API/web/E2E 测试，以及 WorldEngine checker handoff validation。

## v0.8 验证要求

Validation Client v0.8 实现应运行该仓库适用的 focused 和 broad checks。至少包括：

```bash
cd /Users/leechen/projects/WorldEngine-Validation-Client
cd apps/api && uv run pytest -q
pnpm --dir apps/web test
pnpm --dir apps/web build
pnpm run test
pnpm run build
git diff --check
```

如果存在 Playwright 或等价 E2E，应运行 v0.8 flow 的 E2E。

如果 scenario 支持 checker validation，应从 Validation Client 导出 result
directory，并在 WorldEngine 仓库里验证：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
make validate-agent-autonomous-result RESULT_DIR=<result-dir>
```

如果结果是 `BLOCKED`，只有 artifacts 诚实说明阻塞原因时，checker 才应该接受这个
saved result。

## 预期第一轮验证结果

第一版 v0.8 验证仍然可能是 `BLOCKED`。

以下情况可以接受：

- WorldEngine provider 环境没有配置。
- live provider smoke 不能通过 WorldEngine 尝试。
- WorldEngine 缺少某个 scenario 需要的 LLM-backed evidence。
- checker/schema support 不完整。
- required artifact 尚未生成。
- 第二 Agent 复核尚未运行。

客户端必须让 blocker 可见、可导出。不能把 blocker 藏在 UI 成功状态后面。

## 后续路由

v0.8 开发或验证后按以下规则路由：

| 缺口 | 路由 |
| --- | --- |
| 缺 provider live endpoint、provider abstraction、LLM-backed generation、world rules、event legality、Agent continuity/autonomy evidence | WorldEngine 实现迭代。 |
| 缺 scenario artifact 的 checker/schema/fixtures/result validation | WorldEngine `docs/testing` + `tools/testing` package。 |
| 缺 UI display、operation log、API summary、evidence bundle fields、saved-result export、replay/diff/snapshot display | Validation Client milestone。 |
| DeepSeek/provider call 失败，但 WorldEngine API 和证据齐全 | provider/environment validation failure，默认不改客户端代码。 |
| raw prompt/response/key/private memory/raw thought 泄露 | 立即 redaction failure，先修边界再继续。 |

## 成功定义

本文的成功标准是：Validation Client 能用这份材料启动自己的 v0.8 milestone，不需要
猜 WorldEngine v0.9 的职责边界。

Validation Client v0.8 自身完成的标准是：它自己的仓库记录已审核的 milestone
文档、实现证据、测试结果，以及一个诚实报告 `PASS`、`PARTIAL`、`BLOCKED` 或
`FAIL` 的 checker-handoff result。

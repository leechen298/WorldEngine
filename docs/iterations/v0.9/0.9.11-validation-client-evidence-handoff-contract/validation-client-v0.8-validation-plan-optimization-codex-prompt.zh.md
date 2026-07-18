# Codex 提示词：实现 Validation Client v0.8 测试计划优化

英文镜像：
`validation-client-v0.8-validation-plan-optimization-codex-prompt.md`。

在新的 Codex 聊天中使用本文提示词，工作目录应为：

```text
/Users/leechen/projects/WorldEngine-Validation-Client
```

## 提示词

```text
PLEASE IMPLEMENT THIS PLAN:

目标：
把 Validation Client v0.8 创建并实现为一次优化迭代：
`v0.8-worldengine-v0.9-validation-plan-optimization`。

目标是更新 Validation Client 的完整 WorldEngine 测试计划、scenario matrix、
evidence bundle contract、runbook 和对 WorldEngine v0.9 验证的实现支撑。这应是一种
可重复的优化模式：之后 WorldEngine 如果更新公开验证接口、scenario 合同、artifact
合同或 checker 规则，Validation Client 可以按同样模式继续开后续优化迭代。

Validation Client 必须保持外部客户端和 evidence 承载面定位。它不得成为 LLM
provider owner、world generator、event legality authority、Agent autonomy
authority、evaluator 或 PASS source。

仓库：
- Validation Client:
  /Users/leechen/projects/WorldEngine-Validation-Client
- WorldEngine reference repository:
  /Users/leechen/projects/WorldEnginProjects/WorldEngine

必须读取的 WorldEngine 文档：
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/AGENTS.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/project-north-star.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/product-model.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/scope-boundaries.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/roadmap.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/README.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/llm-backed-lifecycle-validation-plan.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-suite-execution.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-artifact-contract.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-scorecard.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/second-agent-review-protocol.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/provider-live-smoke-deepseek.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-world-creation.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/world-rule-parameter-evolution.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/agent-persistent-autonomy-evidence.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-full-lifecycle-autonomous.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution/review.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/validation-client-v0.8-validation-plan-optimization-handoff.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/validation-client-v0.8-validation-plan-optimization-handoff.zh.md

必须读取的 Validation Client 文档和代码：
- AGENTS.md
- AGENTS.zh.md，如果存在
- docs/specs/validation-client-design.md
- docs/specs/validation-client-design.zh.md
- docs/milestones/v0.7-agent-autonomous-validation/
- apps/api/app/worldengine_client.py
- apps/api/app/routes/evidence.py
- apps/api/app/routes/validation_runs.py
- apps/api/app/routes/sessions.py
- apps/api/app/routes/timelines.py
- apps/web/src/pages/RuntimeConsole.tsx
- apps/web/src/api/client.ts
- apps/web/src/api/types.ts
- apps/web/e2e/v0.7-ui-smoke.spec.ts

需要保留的当前事实：
- v0.7 已经有可用的 WorldEngine discovery、session creation、operation log、
  validation run、evidence bundle export、Runtime Console UI、replay、branch、
  director guidance 和 Playwright smoke。
- 一些 v0.7 文档仍指向 WorldEngine 0.8.9 gate。把这些当作历史资料。v0.8
  必须对齐 WorldEngine v0.9。
- WorldEngine v0.9 LLM-backed validation 当前是 checker-valid BLOCKED，不是
  PASS。除非有新的 checker/scorecard/second-Agent 证据，否则不得声称 provider
  live PASS、LLM-backed full lifecycle PASS、Validation Client export PASS 或
  external validation PASS。

必须执行的工作流：
1. 先创建 v0.8 optimization milestone documentation package:
   docs/milestones/v0.8-worldengine-v0.9-validation-plan-optimization/
2. 至少包含：
   - README.md 和 README.zh.md
   - intent.md 和 intent.zh.md
   - contract.md 和 contract.zh.md
   - technical-design.md 和 technical-design.zh.md
   - test-plan.md 和 test-plan.zh.md
   - plan.md 和 plan.zh.md
   - review.md 和 review.zh.md
   - scenario-operation-matrix.md 和 scenario-operation-matrix.zh.md
   - artifact-contract.md 和 artifact-contract.zh.md
   - redaction-matrix.md 和 redaction-matrix.zh.md
   - autonomous-validation-runbook.md 和 autonomous-validation-runbook.zh.md
   - second-agent-review-template.md 和 second-agent-review-template.zh.md
3. 文档创建后，先做 documentation-stage review，并记录 implementation 是否已授权。
   如果当前用户提示词明确授权文档后继续实现，则继续实现。否则停在文档阶段，并
   报告 implementation 等待 review。

如果已授权实现，实现范围如下：
1. 刷新 v0.8 routing 和过期 v0.7 引用，使 v0.8 指向 WorldEngine v0.9，而不是
   WorldEngine 0.8.9。
2. 扩展 WorldEngine discovery，建模 v0.9 public surfaces:
   - GET /health
   - GET /manifest
   - GET /openapi.json
   - POST /provider/live-smoke
   - POST /world/generation/worldview
   - POST /worlds
   - GET /runtime/state
   - POST /runtime/step
   - POST /runtime/run
   - POST /runtime/pause
   - POST /runtime/resume
   - GET /world/events
   - GET /world/event-steps
   - GET /archive/snapshots
   - GET /world/params
   - POST /worlds/{world_id}/direction
   - POST /worlds/{world_id}/director-guidance
   - POST /worlds/{world_id}/evolution/evaluate-event
   - POST /worlds/{world_id}/agents/{agent_id}/continuity/evaluate
   - POST /worlds/{world_id}/narrative/project
   - POST /worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate
3. 增加 bounded runtime controls 到 UI 和 logs：
   - 单步一次
   - 运行 N ticks
   - 在支持时运行 N 秒世界时间
   - 暂停
   - 继续
   - 再运行一段 bounded segment
4. 增加 scenario-aware evidence export:
   - worldengine-full-lifecycle-autonomous
   - provider-live-smoke-deepseek
   - llm-backed-world-creation
   - world-rule-parameter-evolution
   - rule-compliant-event-generation
   - agent-persistent-autonomy-evidence
   - llm-backed-full-lifecycle-autonomous
5. 增加或升级 v0.9-compatible evidence bundle manifest:
   - schema_version
   - bundle_id
   - scenario
   - result_status
   - client_role=display_export_only
   - provider_owner=worldengine
   - evaluator_role=worldengine_checker_or_second_agent_review
   - created_at
   - artifact_index
   - redaction_status
   - checker_contract
   - unsupported_items
6. 支持 scenario 需要的 named artifacts：
   - result.json
   - operation-log.jsonl
   - api-log.jsonl
   - api-summary.json
   - provider-live-summary.json
   - world-creation-summary.json
   - world-rule-summary.json
   - rule-parameter-summary.json
   - event-legality-summary.json
   - agent-autonomy-summary.json
   - diff-replay-summary.json
   - world-lifecycle-summary.json
   - narrative-projection-summary.json
   - diagnostic-conversation-summary.json
   - redaction-scan.json
   - scorecard-summary.json
   - second-agent-review.md
   - transcript.md
   - console.log
   - screenshots/
7. 区分用户可见 operation logs 和 direct API harvest logs。不得把 direct API calls
   伪装成用户或 Agent 操作。
8. 精确保留状态：
   - pass
   - fail
   - blocked
   - not_run
   - out_of_scope 只能在 scenario contract 允许时使用
9. 对所有 displayable/exportable artifacts 增加 redaction scanning。如果 bundle
   包含 API keys、authorization headers、raw prompts、raw provider
   requests/responses、provider traces、private Agent memory/goals、raw thought、
   hidden context、private evaluator data、seed 或 oracle data，必须 fail。
10. 展示 scorecard/checker/second-Agent review 结果，但客户端不得自行判定 PASS。

禁止实现：
- 不得从 Validation Client 直接调用 DeepSeek 或任何 provider。
- 不得保存、展示或转发 provider keys。
- 不得在客户端生成 LLM-backed world content。
- 不得在客户端计算权威 world rules、parameter changes、event legality 或
  Agent autonomy。
- 不得把 blocked/not_run/unsupported 映射成 PASS。
- 不得把 Validation Client UI smoke 当成 WorldEngine validation PASS。
- 不得把 narrative projection 或 diagnostic dialogue 写入 canonical world state
  或 Agent memory。
- 不得泄露 raw prompts、raw responses、provider traces、private memory、
  private goals、raw thought、hidden context、private evaluator data、seed 或
  oracle data。

必须补充的测试和检查：
- API tests 覆盖 manifest schema、artifact_index relative paths、path traversal
  rejection、status enum preservation、unsupported_items、redaction flags、以及
  missing required artifacts 不能变成 PASS。
- API tests 覆盖 provider-blocked saved-result export。
- 前端 tests 覆盖 v0.9 artifact display、scorecard/second-Agent review display、
  redaction warning display，以及 UI 不声明 evaluator/human PASS。
- 增加 E2E 或 integration 覆盖 v0.9 evidence bundle 导出。
- 可以时，从 WorldEngine 验证导出的 result directory：
  cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
  make validate-agent-autonomous-result RESULT_DIR=<result-dir>

运行适用的仓库检查：
cd /Users/leechen/projects/WorldEngine-Validation-Client
cd apps/api && uv run pytest -q
pnpm --dir apps/web test
pnpm --dir apps/web build
pnpm run test
pnpm run build
git diff --check

可用 subagents，尤其用于只读复核、evidence-contract review 或 redaction review。

最终用中文报告：
- 总结论。
- 创建/更新的文档。
- 修改的代码文件。
- 已运行测试/checker 和结果。
- 如果生成了 exported result directory，给出路径。
- 是否真实调用 provider。
- 是否发现 raw prompt/response/key/private memory/raw thought 泄露。
- 剩余 PASS/PARTIAL/BLOCKED/FAIL 状态。
- 是否 commit/push。
```

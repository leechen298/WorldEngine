# 契约

## 公开概念

- `PerceptionFrame`：从 runtime state、recent events、world params 和可选 runtime context summary 组装的有界 agent-facing input。它不得持久化记忆或推断自我连续性。
- `ActionIntent`：来自 agent loop step 的可审查请求动作。v0.4 只允许已评审的最小动作词汇。
- `ActionResult`：action intent 经过校验和应用后的 accepted、rejected 或 no-op 结果。
- `LoopStep`：一次 request-scoped perceive -> intent -> validate/apply -> result 循环。它不是后台自治。

## 允许修改

- 在获授权时创建或更新 v0.4 evidence index 和 compatibility audit docs。
- 汇总实现包的命令证据。
- 分类 runtime、API、event、params、archive、frontend、schema、fixture、migration 和 legacy impacts。
- 仅把 v0.5 handoff 记录为 planning readiness。

## 禁止修改

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

## 兼容性要求

- 除非 active child 明确改变，否则 `RuntimeEngine` tick 和 `world_time_seconds` 行为必须兼容。
- API envelope 和 error shape 必须兼容。
- `/runtime/state`、`/runtime/step`、`/world/events` 和 `/world/event-steps` 是兼容性敏感 surface。
- world params、params apply behavior、既有 ParamsAgent endpoint、archive behavior 和 Event.refs 可选序列化都是兼容性敏感 surface。
- 除非 active contract 明确允许 breaking change，否则 schema changes 必须 additive。

## 实现授权

在本包记录 `GOAL_RUNNER.md` 要求的全部 review gates 前，implementation authorization 保持关闭。对 docs-only package，授权仅限文档变更。对 mixed 或 code package，只有必需 documentation/contract evaluator 报告无阻塞 finding 后，`review.md` 才能记录 `implementation_authorized: yes`。

## 范围外后续

- v0.5 memory 和 self-continuity substrate。
- v0.6 world generation。
- v0.7 external validation readiness。
- v0.8 projection application readiness。
- 具体 product、game 或 validation-world behavior。

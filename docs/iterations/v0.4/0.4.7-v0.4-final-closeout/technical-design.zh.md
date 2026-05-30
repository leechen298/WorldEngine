# 技术设计

## 文档或实现结构

仅最终文档收口，不做实现变更。

对 code 或 mixed package，除非本包契约明确扩大范围，否则实现必须停留在 `backend/app/`。不得在 `backend/worldengine/` 下新增 runtime feature。

## 受影响文件

本包允许的文件类别：

- 只有 approval 后才把 v0.4 status surfaces 更新为 final / closeout complete。
- 更新 finding records 和 v0.5 handoff notes。
- 记录 final evidence summary、commands、compatibility review 和 scope review。
- 只有 active contract 明确包含时才更新 release docs。

明确范围外：

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

## 数据 / 控制流

v0.4 loop 方向：

1. 从 runtime state、recent events、current params 和可选 runtime context summary 构建有界 `PerceptionFrame`。
2. 在 request-scoped loop step 内产生或接受 `ActionIntent`。
3. 按最小动作词汇校验 intent。
4. 对 `noop`，返回无 effect 的 `ActionResult`。
5. 对 `params.patch`，转换为 `ParamPatchItem`，运行静态校验，运行 dry-run 校验，并且只在校验成功后 apply。
6. 仅按 active package contract 授权发出或返回可审查 result evidence。

本包只能实现契约明确允许的子集。sequence 中后续步骤在各自 package 评审前保持 planned。

## 兼容性策略

- 除非 active child 明确改变，否则 `RuntimeEngine` tick 和 `world_time_seconds` 行为必须兼容。
- API envelope 和 error shape 必须兼容。
- `/runtime/state`、`/runtime/step`、`/world/events` 和 `/world/event-steps` 是兼容性敏感 surface。
- world params、params apply behavior、既有 ParamsAgent endpoint、archive behavior 和 Event.refs 可选序列化都是兼容性敏感 surface。
- 除非 active contract 明确允许 breaking change，否则 schema changes 必须 additive。

## 防漂移规则

- 未完成必需 evaluator checkpoint 时停止。
- 发现 P1 或未解决 P2 时停止。
- 如果需要 active contract 未授权的文件类别，停止并记录 blocker。
- 不得用历史证据冒充当前会话通过证据。

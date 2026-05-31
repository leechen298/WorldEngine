# Campaign Plan

状态：final / closeout complete
类型：Codex `/goal` 开发 campaign plan

## 用途

本计划定义以下 goal 的有序 campaign sequence：

```text
完成 v0.4
```

它是 campaign guidance，不是 WorldEngine runtime behavior，也不是 automation-controller 实现。

## Campaign 退出条件

v0.4 只有在所有带实现 child package 都有已评审 package docs、必需 subagent/evaluator checkpoints 无阻塞 findings、聚焦和兼容性验证命令有当前证据记录、release-candidate review 批准 final closeout，并且 `0.4.7-v0.4-final-closeout` 记录无未解决 P1/P2 findings 后，才能标记为 final / closeout complete。

## 顺序

### 0. v0.4 规划与兼容性基线

包：`0.4.0-v0.4-planning-and-compatibility-baseline`

目的：创建 v0.4 文档根目录、goal campaign 控制文件、版本计划、兼容性基线和 v0.3 交接映射，不修改实现文件。

允许修改：

- 创建 `docs/iterations/v0.4/**` 父级和 child 文档。
- 定义 goal 入口 `完成 v0.4`。
- 定义 subagent/evaluator checkpoints 和 package sequence。
- 仅把 v0.3 收口后证据记录为 handoff context。

禁止修改：

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

预期交付物：

- 完整 package docs 和中文镜像。
- documentation-only verification 和未运行代码测试的理由。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 记录 backend/frontend/API/E2E/runtime tests not run because the package is documentation-only。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

### 1. 世界内 Agent 闭环契约

包：`0.4.1-agent-in-world-loop-contract`

目的：在代码变更前定义 v0.4 世界内 Agent 闭环的公开概念、事件语义、API 边界、错误模型和实现授权条件。

允许修改：

- 定义 `PerceptionFrame`、`ActionIntent`、`ActionResult` 和 `LoopStep` 语义。
- 仅以文档定义 event 和 error model contracts。
- 定义允许动作词汇：`noop` 和经过校验的 `params.patch`。
- 定义 API boundary，但本包不新增 route。

禁止修改：

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

预期交付物：

- 完整 package docs 和中文镜像。
- documentation-only verification 和未运行代码测试的理由。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 记录 backend/frontend/API/E2E/runtime tests not run because the package is documentation-only。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

### 2. Agent 感知与 Schema

包：`0.4.2-agent-perception-and-schemas`

目的：新增通用世界内 Agent schema model 和有界 perception builder，读取 runtime state、recent events、world params 和可选 runtime-context summary，不产生状态变更。

允许修改：

- 在 `backend/app/schemas/` 下添加 additive schemas。
- 在获批 `backend/app/` 模块下添加只读 perception builder。
- 读取 runtime state、event log、world params 和可选 runtime context summary。
- 添加覆盖有界只读 perception 的聚焦后端测试。

禁止修改：

- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

预期交付物：

- 完整 package docs 和中文镜像。
- 实现后记录聚焦测试、兼容性测试和必需 subagent/evaluator checkpoints。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 在 `backend/` 下用 `.venv/bin/python -m pytest ...` 运行聚焦后端测试。
- 按 touched surface 运行相邻兼容性测试。
- 如新增 API route，通过 FastAPI TestClient 做 API smoke。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

### 3. Action Intent 校验与 Result Adapter

包：`0.4.3-action-intent-validation-and-result-adapter`

目的：实现最小通用 action intent validator 和 result adapter，支持 noop 与经过校验的 params.patch，复用既有参数校验和 dry-run 防护。

允许修改：

- 在获批 `backend/app/` 模块下添加内部 action validator/adapter。
- 支持 `noop` 作为合法无 effect action。
- 仅通过 `ParamPatchItem`、`ParamValidator`、`ParamDryRunValidator` 和既有 apply semantics 支持 `params.patch`。
- 添加覆盖 accepted、rejected、dry-run blocked 和 no-op intents 的聚焦后端测试。

禁止修改：

- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

预期交付物：

- 完整 package docs 和中文镜像。
- 实现后记录聚焦测试、兼容性测试和必需 subagent/evaluator checkpoints。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 在 `backend/` 下用 `.venv/bin/python -m pytest ...` 运行聚焦后端测试。
- 按 touched surface 运行相邻兼容性测试。
- 如新增 API route，通过 FastAPI TestClient 做 API smoke。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

### 4. 最小 Agent 闭环编排与 API

包：`0.4.4-minimal-agent-loop-orchestration-and-api`

目的：接入 request-driven 最小世界内 Agent 闭环：构建 perception，获得或接受 intent，校验并应用 intent，发出可审查 result evidence，并返回稳定 API response。

允许修改：

- 在获批 `backend/app/` 模块下添加 request-driven loop service。
- 只有 contract 授权时才新增一个已评审 API route。
- 测试中使用确定性 provider 或显式 test intent。
- 添加聚焦 service/API 测试和相邻兼容性检查。

禁止修改：

- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。
- 不得替换或破坏 `/world/agent/params/propose-and-apply`。

预期交付物：

- 完整 package docs 和中文镜像。
- 实现后记录聚焦测试、兼容性测试和必需 subagent/evaluator checkpoints。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 在 `backend/` 下用 `.venv/bin/python -m pytest ...` 运行聚焦后端测试。
- 按 touched surface 运行相邻兼容性测试。
- 如新增 API route，通过 FastAPI TestClient 做 API smoke。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

### 5. Agent 闭环证据与兼容性审计

包：`0.4.5-agent-loop-evidence-and-compatibility-audit`

目的：审计 v0.4 实现证据、变更文件、兼容性 surface、未解决 findings 和 release-candidate review 交接就绪度。

允许修改：

- 在获授权时创建或更新 v0.4 evidence index 和 compatibility audit docs。
- 汇总实现包的命令证据。
- 分类 runtime、API、event、params、archive、frontend、schema、fixture、migration 和 legacy impacts。
- 仅把 v0.5 handoff 记录为 planning readiness。

禁止修改：

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

预期交付物：

- 完整 package docs 和中文镜像。
- documentation-only verification 和未运行代码测试的理由。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 记录 backend/frontend/API/E2E/runtime tests not run because the package is documentation-only。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

### 6. v0.4 发布候选包

包：`0.4.6-v0.4-release-candidate-bundle`

目的：从已评审实现和审计证据准备 v0.4 release-candidate bundle，不声明最终发布，也不添加实现变更。

允许修改：

- 在 `docs/iterations/v0.4/` 下创建 release-candidate bundle docs。
- 汇总 package statuses、evidence、commands、findings 和 compatibility claims。
- 定义 0.4.7 的 final review questions。
- 使用 evaluator review 检查 claim support 和 mirror quality。

禁止修改：

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

预期交付物：

- 完整 package docs 和中文镜像。
- documentation-only verification 和未运行代码测试的理由。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 记录 backend/frontend/API/E2E/runtime tests not run because the package is documentation-only。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

### 7. v0.4 最终收口

包：`0.4.7-v0.4-final-closeout`

目的：仅在 release-candidate review approval、证据一致性检查和未解决 finding 分类完成后，才把 v0.4 标记为 final / closeout complete。

允许修改：

- 只有 approval 后才把 v0.4 status surfaces 更新为 final / closeout complete。
- 更新 finding records 和 v0.5 handoff notes。
- 记录 final evidence summary、commands、compatibility review 和 scope review。
- 只有 active contract 明确包含时才更新 release docs。

禁止修改：

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

预期交付物：

- 完整 package docs 和中文镜像。
- documentation-only verification 和未运行代码测试的理由。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 记录 backend/frontend/API/E2E/runtime tests not run because the package is documentation-only。

退出条件：package review 记录必需证据、必需 evaluator checkpoints、无未解决 P1/P2，并有明确 handoff status。

交接：sequence 中的下一包只接收已评审证据和明确 handoff notes。

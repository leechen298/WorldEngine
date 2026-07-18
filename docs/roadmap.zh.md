# Roadmap

状态：`planning guide`

英文版本：`roadmap.md`

本 roadmap 定义交付方向。每个 version 在实现前仍需要 scoped iteration packages。

## v0.1 - Runtime Scaffold

状态：`current baseline`

目标：建立 monorepo、FastAPI backend、Vue dashboard、runtime tick、event log、
params、archive 和 basic API envelope。

## v0.2 - Recursive World Foundation

状态：`final / closeout complete`

目标：建立 documentation governance、north star、recursive world schema/spec
language、additive event contract、generic schema smoke validation、external
fixture boundary、legacy boundary、iterative development workflow，以及可 review
的 release-candidate evidence。

非目标：不把 RuntimeEngine 迁移到 WorldCell，不构建 demo-specific runtime。

Concrete external worlds 不得作为 core repository 内的 fixtures、loader inputs、
projection targets 或 acceptance targets 出现。它们只能通过 public APIs、CLI
contracts、schemas、exported contracts 和 redacted validation reports 消费
WorldEngine。

### v0.2.5 - Core Boundary Cleanup and Roadmap Reset

目标：从 active core docs、fixtures 和 tests 中移除 concrete external-world anchors，
并围绕 generic engine consumers 重置后续 roadmap。

### v0.2.6 - Iteration Workflow and Plan Reset

目标：重排 v0.2 剩余 package sequence，增加 ChatGPT / Codex A / Codex B
自动迭代 workflow，并抽象化 v0.2 iteration documentation 中的 residual concrete
demo anchors。

### v0.2.7 - Recursive Schema Contract Hardening

目标：加固 EntityRef、WorldCell、WorldSpec schema contracts 和 generic schema
tests，不实现 runtime loading。

### v0.2.8 - Event Reference Contract Hardening

目标：加固 EventRef 和 Event.refs additive event reference contracts，不实现
resolver 或 causality engine。

### v0.2.9 - Generic Schema Evidence and Boundary Audit

目标：在 compatibility review 前审计 v0.2 schema、event、external boundary 和
legacy boundary evidence。

### v0.2.10 - Legacy Boundary and Compatibility Review

目标：在 v0.3 bridge work 前明确 v0.1 runtime scaffold compatibility 和 legacy
boundaries。

### v0.2.11 - v0.2 Release Candidate Bundle

目标：准备 release-candidate evidence，供 human / ChatGPT review，不声明 final release。

### v0.2.12 - v0.2 Final Closeout

目标：仅在 release-candidate bundle 通过 human / ChatGPT review 后执行 final closeout。

## v0.3 - WorldSpec Loader and Runtime Bridge

状态：`final / closeout complete`

目标：在不破坏 v0.1 runtime compatibility 的前提下，把 validated generic WorldSpec
data 加载进 runtime context。

交接：v0.4 只能通过自己的已评审 iteration package 启动。

## v0.3.5 - External Fixture Contract Readiness

目标：定义 external fixture runners 如何通过 public contracts 调用 core repository，
同时不在 WorldEngine 内创建这些 repositories。

## v0.4 - Agent-in-World Minimal Loop

状态：`final / closeout complete`

目标：让 Agent 感知世界事件、产生 action intent、接收 action result，并通过一个最小、
经过校验的闭环影响 world state。

交接：v0.5 可以基于已评审的 request-driven minimal loop 启动，但 memory 和
self-continuity 仍是明确的 future scope。

## v0.5 - Memory and Self-Continuity Substrate

状态：`final / closeout complete`

目标：引入 working memory、episodic memory、relationship state、self-summary、
reflection records，以及会影响 future action 的 personality drift signals。

关闭范围：v0.5 已实现 additive generic working-memory 和 episodic-memory backend
schemas、process-local in-memory substrate，以及 Agent Loop perception 中的 bounded
read-only memory context。Relationship state、self-summary、reflection records 和
personality drift signals 只作为 deferred contracts 完成细化。

Final evidence：focused backend memory/loop/action compatibility `33 passed`；
full backend regression `145 passed`；required docs/mirrors `missing=0`；
changed-file scope guard `out_of_scope=0`；closeout consistency evaluator PASS。
不声明 frontend、E2E、Agent smoke、autonomous、external validation、projection
readiness 或 product readiness 已通过。

交接：v0.6 world generation v1 只能从自己的 reviewed iteration package 启动。

## v0.6 - World Generation v1

状态：`final / closeout complete`

目标：从 templates 和 structured AI-assisted generation 生成 runnable WorldSpec data，
并包含 validation、metadata、preview 和 regeneration support。

关闭范围：v0.6 已实现 generic world-generation contracts、template semantics、
deterministic template catalog generation、structured generation plan compilation、
不含 live provider integration 的 AI-assisted plan import boundaries、validation
metadata、preview/regeneration/runtime-readiness APIs，以及带 focused E2E smoke 的
dashboard generation preview。

Final evidence：full backend regression `220 passed`；frontend unit `36 passed`；
frontend build 通过且仅有 Vite large-chunk warning；E2E `16 passed`；required
docs/mirrors `missing=0`；changed-file scope guard `out_of_scope=0`；closeout
consistency evaluator PASS。不声明 external validation readiness、projection
readiness、product readiness、Agent smoke、autonomous runner、live provider 或
generation-quality pass。

交接：v0.7 external validation readiness 只能从自己的 reviewed iteration package 开始。

## v0.7 - External Validation Readiness / Projection Consumer Readiness

目标：通过 public contracts、redacted reports 和 compatibility evidence，让 WorldEngine
为 external validation suites 和 projection consumers 做好准备。

## v0.8 - Minimum Proved Working WorldEngine / External Validation Readiness

目标：准备 WorldEngine core runtime、generation、Agent loop、memory context 和
projection/read-model surfaces，让 external validation function 可以验证 engine 达到最小
正常工作状态，同时不把 validation logic、external application code、app-specific behavior
或 concrete world content 移入 core repository。

v0.8 不是 external validation implementation，也不是第一个 external product application。
它定义 core-side readiness boundary、observable public surfaces、evidence expectations 和
stop rules。

## v0.9 - LLM-backed World Lifecycle Foundation

状态：`reviewed / planning-ready`

目标：把 WorldEngine 从 basic lifecycle 推进到第一版 LLM-backed lifecycle foundation：
WorldEngine 自己拥有 live provider calls，把用户基础 world view 转成 runnable public world
model，评估 generation fidelity，控制 bounded world execution，把用户自然语言 direction
处理成受规则约束的 environment guidance，通过 explicit legality evidence 演化 parameters 和
events，暴露类脑 Agent continuity/consolidation public evidence，并通过 checker-backed
artifacts 验证整条 flow。

v0.9 不是 product client、game release、concrete demo world 或 external validator
implementation。它不能把 provider ownership、evaluation authority、concrete world content
或 application-specific backend behavior 移出 generic WorldEngine core boundary。

## v0.10 - MVP Debug Contract And Runnable World Session

状态：`PARTIAL / WorldEngine-side MVP slice complete; external Validation Client export blocked`

目标：启动 MVP 交付线。先对齐 WorldEngine-Validation-Client 需要的 public
manifest/debug handoff contract，然后建立第一条 runnable world session slice：
worldview input、session identity、bounded runtime、events、snapshots、dashboard
inspection、public client discovery，以及避免父子/源语义的 replay/worldline branch
terminology。

v0.10 不声明完整 LLM quality、Agent autonomy 或 product readiness。它应产出可调试的
session baseline，并能诚实报告 `pass`、`fail`、`blocked` 或 `not_run` evidence。

交接：v0.11 只能在 runnable session 和 debug handoff 有证据，或缺失项被明确记录为 blocker
后启动。

## v0.11 - MVP Rule-Bound World Evolution

状态：`PARTIAL / closeout complete; external Validation Client export blocked`

目标：让 runnable MVP world 通过 public rules、parameters、user direction boundaries、
legal event candidates、applied public diffs 和 worldview fidelity evidence 演化。

用户 direction 保持为外部 world-level pressure：它可以引入“可能面临雷击风险”这类风险，但
WorldEngine 必须通过 rules、state、probability 和 legality evidence 决定实际结果，而不是把用户
指令直接复制成最终事实。

v0.11 不是 Agent pseudo-self 或完整 validation automation 版本。它要先让世界变化能被解释，
再叠加 Agent continuity。

交接：v0.12 只能在 rule-linked event/diff evidence 存在，或缺失 handoff 被明确记录为 blocker
后启动。

## v0.12 - MVP Agent Continuity And Validation Automation

状态：`PARTIAL / closeout complete; external Validation Client export blocked`

目标：通过 minimal public Agent continuity loop、memory/rest consolidation evidence、
read-only 小说式 narrative 和 diagnostic inspection surfaces、明确区分世界内 Agent 与外部验证
Agent 的术语，以及基于 WorldEngine-Validation-Client evidence 的 checker-backed full lifecycle
validation，完成 MVP。

v0.12 是第一个可以声明 complete MVP PASS 的版本，但只能基于 checker、scorecard 和
read-only review evidence。如果 provider、client 或 checker capability 缺失，closeout 应诚实
分类为 PARTIAL、BLOCKED 或 FAIL。

Closeout result：PARTIAL。WorldEngine-side Agent continuity、memory、inspection、handoff 和 deterministic checker evidence 已存在。Complete MVP PASS 仍被缺失的 current v0.12 external Validation Client export/result directory 阻断。

## v0.13 - 最小可运行 MVP 锚点

状态：`planning / documentation package ready for user review`

目标：围绕一条确定性、单 Session、单 Agent、lockstep 纵向切片重新锚定实现。这条切片需要把
世界生成、正典 runtime、Agent action 和 experience、accepted/rejected 用户干预、通用投影、
管理控制台操作、Godot 消费和独立外部分类证明为同一场因果运行。

v0.13 把 v0.10-v0.12 的代码和证据视为历史背景，不把它们当作目标设计或当前证明。只有通过
新 contract 的既有工作才允许复用。本版本不删除历史工作，不把具体验证世界放进 WorldEngine，
也不让 Godot 成为 core dependency。

交付顺序：

1. `0.13.0-worldengine-runnable-anchor`：WorldEngine 侧通用协议、确定性
   package/session/runtime/Agent/intervention loop、evidence 和管理控制台。
2. `0.13.1-godot-validation-client-anchor`：在 `WorldEngine-Validation-Client` 中实现外部
   Godot executor 和隔离 checker。
3. `0.13.2-anchor-run-validation-and-closeout`：干净 cross-client 运行，以及有证据支持的
   `PASS`、`PARTIAL`、`BLOCKED` 或 `FAIL`。

完整 v0.13 PASS 必须包含外部 Godot/checker 运行。仅通过 `0.13.0` 只证明 WorldEngine 侧
锚点。

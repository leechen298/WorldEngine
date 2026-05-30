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

目标：让 Agent perceive world events、produce action intents、receive action results，
并通过一个 minimal validated loop 影响 world state。

## v0.5 - Memory and Self-Continuity Substrate

目标：引入 working memory、episodic memory、relationship state、self-summary、
reflection records，以及会影响 future action 的 personality drift signals。

## v0.6 - World Generation v1

目标：从 templates 和 structured AI-assisted generation 生成 runnable WorldSpec data，
并包含 validation、metadata、preview 和 regeneration support。

## v0.7 - External Validation Readiness / Projection Consumer Readiness

目标：通过 public contracts、redacted reports 和 compatibility evidence，让 WorldEngine
为 external validation suites 和 projection consumers 做好准备。

## v0.8 - First External Projection Application Readiness

目标：准备 engine interfaces、evidence 和 projection contracts，让第一个 external
product application 能消费 WorldEngine，而不把 application-specific behavior 移入
core repository。

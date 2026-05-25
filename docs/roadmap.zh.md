# Roadmap

Status: planning guide

英文版本：`roadmap.md`。

本 roadmap 定义 delivery direction。每个 version 在实现前仍然需要 scoped iteration packages。

## v0.1 - Runtime Scaffold

Status: current baseline

Goal: 建立 monorepo、FastAPI backend、Vue dashboard、runtime tick、event log、params、archive
和 basic API envelope。

## v0.2 - Recursive World Foundation

Goal: 建立 documentation governance、north star、recursive world schema/spec language、additive
event contract、generic schema smoke validation、external fixture boundary 和 legacy
boundary。

Non-goal: 不迁移 RuntimeEngine 到 WorldCell，不构建 demo-specific runtime。

Concrete external worlds 不能作为 core repository 内的 fixtures、loader inputs、projection
targets 或 acceptance targets 出现。它们只能通过 public APIs、CLI contracts、schemas、exported
contracts 和 redacted validation reports 消费 WorldEngine。

### v0.2.5 - Core Boundary Cleanup and Roadmap Reset

Goal: 从 active core docs、fixtures 和 tests 中移除 concrete external-world anchors，并围绕
generic engine consumers 重置后续 roadmap。

### v0.2.6 - Generic Recursive World Foundation Closeout

Goal: 围绕 generic WorldCell、WorldSpec、EntityRef、EventRef、schema smoke validation 和
external consumer boundaries 关闭 v0.2。

## v0.3 - WorldSpec Loader and Runtime Bridge

Goal: 在不破坏 v0.1 runtime compatibility 的前提下，把 validated generic WorldSpec data
加载进 runtime context。

## v0.3.5 - External Fixture Contract Readiness

Goal: 定义 external fixture runners 如何通过 public contracts 调用 core repository，同时不在
WorldEngine 内创建这些 repositories。

## v0.4 - Agent-in-World Minimal Loop

Goal: 让 Agent perceive world events、produce action intents、receive action results，并通过一个
minimal validated loop 影响 world state。

## v0.5 - Memory and Self-Continuity Substrate

Goal: 引入 working memory、episodic memory、relationship state、self-summary、reflection records
和会影响 future action 的 personality drift signals。

## v0.6 - World Generation v1

Goal: 从 templates 和 structured AI-assisted generation 生成 runnable WorldSpec data，并包含
validation、metadata、preview 和 regeneration support。

## v0.7 - External Validation Readiness / Projection Consumer Readiness

Goal: 通过 public contracts、redacted reports 和 compatibility evidence，让 WorldEngine 为
external validation suites 和 projection consumers 做好准备。

## v0.8 - First External Projection Application Readiness

Goal: 准备 engine interfaces、evidence 和 projection contracts，让第一个 external product
application 能消费 WorldEngine，而不把 application-specific behavior 移入 core repository。

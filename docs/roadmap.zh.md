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
event contract、reference WorldSpec fixture 和 legacy boundary。

Non-goal: 不迁移 RuntimeEngine 到 WorldCell，不构建 village runtime。

Tiny Village 可以在 v0.7 之前作为 reference fixture、schema validation target、loader test input
或 projection acceptance target 出现。它不能在 roadmap 明确允许之前，变成 WorldEngine 内部的
game-specific runtime logic。

## v0.3 - WorldSpec Loader and Runtime Bridge

Goal: 在不破坏 v0.1 runtime compatibility 的前提下，把 validated WorldSpec data 加载进
runtime context。

## v0.4 - Agent-in-World Minimal Loop

Goal: 让 Agent perceive world events、produce action intents、receive action results，并通过一个
minimal validated loop 影响 world state。

## v0.5 - Memory and Self Continuity

Goal: 引入 working memory、episodic memory、relationship state、self-summary、reflection records
和会影响 future action 的 personality drift signals。

## v0.6 - World Generation v1

Goal: 从 templates 和 structured AI-assisted generation 生成 runnable WorldSpec data，并包含
validation、metadata、preview 和 regeneration support。

## v0.7 - Reference Village World

Goal: 构建第一个完整 reference world，用于验证 world generation、world runtime、recursive
structure、Agent continuity 和 player projection，同时不把 engine 改成 game-specific backend code。

## v0.8 - First Game Surface

Goal: 启动 user-facing game surface，让它 consume WorldEngine APIs 和 projections，同时把 world
runtime 与 Agent self-continuity 留在 engine 内。

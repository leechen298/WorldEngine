# Product Model

Status: authoritative product model

英文版本：`product-model.md`。

## WorldEngine Is

- A recursive world generation engine。
- A world runtime engine。
- An event timeline and memory substrate。
- An agent-in-world cognition substrate。
- 面向 dashboards、games、APIs、tools 和 external clients 的 projection provider。
- 用于 inspect 和 replay world history、Agent experience 与 state change 的 system。

## WorldEngine Is Not

- 不只是 village game backend。
- 不只是 NPC chat system。
- 不只是 story generator。
- 不只是 game client。
- 不宣称 real consciousness。
- 不是存放 game-specific UI、art、sound、animation、packaging 或 distribution logic 的仓库。

## Core Domains

### World Generation

World generation 会把 user direction、templates、structured configuration 或 AI-assisted plans
转换成 valid world specs。Generated worlds 必须 structured、validated、saved、run、inspected
并可扩展。

### World Runtime

World runtime 推进 time、evaluate rules、apply consequences、record events、update state、
produce snapshots，并支持 recovery。

### Agent Domain

Agents 不是 generic NPC chat wrappers。它们拥有 identity、state、needs、goals、memory、
relationships、action intent、feedback、reflection 和随时间发展的 self-narrative。

### Persistence

Persistence 存储 world specs、runtime state、events、snapshots、generation metadata、Agent
state、memory records 和 reviewable evidence。

### Projection

Projection 把 running world 暴露给不同 consumers。Dashboard、game、API client 或 external
system 都看到同一个 underlying world model 的 projection。

## First Product Surface

第一款 product surface 可以是 village-like electronic-pet world。它应该 consume WorldEngine
capabilities，而不是拥有 world runtime 或 Agent self-continuity logic。

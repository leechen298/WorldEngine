# Product Model

Status: authoritative product model

英文版本：`product-model.md`。

## WorldEngine Is

- A recursive world generation engine。
- A world runtime engine。
- An event timeline and memory substrate。
- An agent-in-world cognition substrate。
- WorldEngine-owned LLM-backed generation and reasoning substrate。
- 面向 dashboards、games、APIs、tools 和 external clients 的 projection provider。
- 用于 inspect 和 replay world history、Agent experience 与 state change 的 system。

## WorldEngine Is Not

- 不是 demo-specific 或 application-specific backend。
- 不只是 NPC chat system。
- 不只是 story generator。
- 不只是 provider proxy 或 prompt runner。
- 不只是 game client。
- 不宣称 real consciousness。
- 不是存放 game-specific UI、art、sound、animation、packaging 或 distribution logic 的仓库。

## Core Domains

### World Generation

World generation 会把 user direction、templates、structured configuration 或 AI-assisted plans
转换成 valid world specs。Generated worlds 必须 structured、validated、saved、run、inspected
并可扩展。

当 generation 使用 LLM 时，WorldEngine 拥有 provider call，并且必须把 model output 转换成
public、structured、validated world data。Raw prompts 和 raw responses 不是 product surfaces
或 validation evidence。

### World Runtime

World runtime 推进 time、evaluate rules、apply consequences、record events、update state、
produce snapshots，并支持 recovery。

Runtime execution 应该 bounded 且 inspectable。Consumers 可以要求 engine run one tick、run
multiple ticks、run for a world-time duration、pause、resume 或 continue，但 engine 仍负责
state、rules、event legality、snapshots 和 run evidence。

### Agent Domain

Agents 不是 generic NPC chat wrappers。它们拥有 identity、state、needs、goals、memory、
relationships、action intent、feedback、reflection 和随时间发展的 self-narrative。

Agent cognition 不是 mandatory per-tick mutation loop。Short-term memory、long-term memory、
personality、skills、intent 和 self-narrative 应有 explicit public summaries，并且可以通过
sleep、rest 或 low-activity phases consolidation，这些 phase 可以跨多个 ticks。

### Persistence

Persistence 存储 world specs、runtime state、events、snapshots、generation metadata、Agent
state、memory records 和 reviewable evidence。

Persistence 可以存储 public summaries、consolidation records、projections 和 redacted evidence。
除非 reviewed contract 明确允许 redacted public form，否则它不得把 raw provider traces、raw
thought、private memory payloads 或 diagnostic conversations 变成 canonical evidence。

### Projection

Projection 把 running world 暴露给不同 consumers。Dashboard、game、API client 或 external
system 都看到同一个 underlying world model 的 projection。

Narrative output、replay views 和 out-of-world diagnostic Agent conversations 默认是 projection
或 inspection surfaces。它们可以帮助人类或 validator 理解运行情况，但不会修改 canonical
world timeline 或 Agent memory，除非未来 reviewed bridge 明确改变该边界。

## External Product Surfaces

Product surfaces 应该作为 public WorldEngine consumers 存在。它们 consume schemas、APIs、
events、projections 和 exported contracts，而不是在 core repository 内拥有 world runtime
或 Agent self-continuity logic。

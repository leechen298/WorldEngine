# 契约

状态：planned / ready for review

## 公共概念

- `v0.5 Memory and Self-Continuity Substrate`：用于 inspectable agent memory 与
  engineered pseudo-self continuity 的版本边界。
- `Working memory`：带 provenance 和 explicit lifetime semantics 的 bounded
  current-context memory。
- `Episodic memory`：连接 agent experience、action outcomes、world time 和 evidence
  的 event-linked records。
- `Relationship state`：agents、entities 或 world references 之间的 structured
  relationship semantics，在初始 implementation slice 中只做 contract-only。
- `Self-summary`：Agent continuity state 的 inspectable summary；在 summarization
  behavior 评审前只做 contract-only。
- `Reflection record`：Agent self-assessment 或 feedback processing 的可评审记录；
  在 automatic reflection 评审前只做 contract-only。
- `Personality drift signal`：未来可影响 action 的 inspectable signal；在
  action-modifier behavior 评审前只做 contract-only。

## 能力拆分

| Capability | This package | First implementation candidate |
| --- | --- | --- |
| Working memory | 定义边界 | 是，在 `0.5.2` |
| Episodic memory | 定义边界 | 是，在 `0.5.2` |
| Relationship state | 定义边界 | 暂无 behavior |
| Self-summary | 定义边界 | 暂无 summarization |
| Reflection records | 定义边界 | 暂无 automatic reflection |
| Personality drift signals | 定义边界 | 暂无 action modifier |

## 兼容性约束

- Existing v0.4 Agent Loop schemas 和 APIs 在 `0.5.0` 中保持不变。
- `PerceptionFrame`、`ActionIntent`、`ActionResult`、request-scoped `LoopStep` 和
  `POST /world/agent/loop/step` 是 compatibility-sensitive。
- `/world/agent/params/propose-and-apply` 继续可用且不变。
- Runtime tick/time behavior、API envelope/error shape、event routes、params
  behavior、archive behavior 和 optional `Event.refs` serialization 仍是
  compatibility-sensitive。
- Future schema changes 必须是 additive，除非后续已评审 child 明确允许 breaking change。
- v0.4 与 post-closeout command evidence 只作为 handoff evidence，不是当前 v0.5
  pass evidence。

## 允许修改

- 创建 `docs/iterations/v0.5/**` documentation。
- 创建 parent campaign files、child package files、中文镜像、review evidence 和
  package sequencing。
- 只命名 planned future implementation paths，不创建它们：
  - `backend/app/schemas/agent_memory.py`
  - `backend/app/agent/memory.py` 或等价已批准路径
  - `backend/app/tests/test_agent_memory_*.py`
- 记录 read-only review 中的 subagent/evaluator findings。

## 禁止修改

- 不修改 runtime、schema、API、frontend、backend test、fixture、migration、
  generated result、external repository 或 `backend/worldengine/` implementation
  files。
- 本 package 不创建 planned future implementation paths。
- 不添加 memory store behavior、loop integration、action modifiers、public runtime
  APIs、durable persistence、migrations、frontend behavior 或 tests。
- 不添加 concrete world names、maps、characters、locations、resources、story rules、
  seed data、UI-specific app behavior、private validation oracle details、world
  generation、external validation readiness 或 projection app readiness。

## North Star 检查

本 package 通过把 memory、relationship history、self-narrative 和 personality drift
准备成可检查的 engineered contracts 来符合 north star。它不声明 real consciousness，
也不把 WorldEngine 收窄成 demo-specific 或 application-specific backend。

## 范围外后续

- `0.5.1`：public memory/self-continuity concept contracts 与 schema semantics。
- `0.5.2`：首个 working/episodic memory schema 和 in-memory substrate
  implementation。
- `0.5.3`：loop perception 中的 bounded read-only memory context。
- 后续 packages：relationship behavior、self-summary generation、automatic
  reflection 和 personality drift action modifiers。
- v0.6 world generation、v0.7 external validation readiness 和 v0.8 projection
  application readiness。


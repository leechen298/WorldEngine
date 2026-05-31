# 契约

状态：review complete

## 公开概念

### Working Memory

Working memory 是 agent 在 world 内的 bounded current-context memory record。
它用于短期事实、观察、意图或 operator-provided notes，供近期 loop perception 使用。

必须满足的语义：

- 每条记录具备 `agent_id`、`world_id`、稳定的 `memory_id`、`content`、`source`、
  `created_at` 和 `updated_at` 语义。
- 记录必须携带 provenance，说明 memory 来自 observed event、action result、
  operator input、system import 或 derived process。
- 记录必须有明确的 bounded-lifetime 语义，例如 priority、ttl/tick window、
  expiration 或 max-context selection。第一个实现可以使用简单的 in-memory
  bounded selection，但不得暗示 durable persistence。
- 记录必须保持 generic，不编码具体 world name、character、map、resource、
  story rule 或 validation-oracle detail。

### Episodic Memory

Episodic memory 是 agent experience 的 event-linked record。它记录发生了什么、何时发生、
与哪些 world/event/action evidence 相关，以及为什么该 episode 可供后续检查。

必须满足的语义：

- 每条记录具备 `agent_id`、`world_id`、稳定的 `memory_id`、`summary`、
  `event_refs`、`tick`、`world_time`、`source`、`created_at`，并可选包含
  outcome 或 action-result references。
- event 与 action references 必须使用 generic identifiers；可用时应兼容可选的
  `Event.refs` references。
- episodes 是可检查的 evidence records，不是隐藏 behavior modifiers。
- 第一个实现只能用 in-memory 存储。Durable persistence、indexing、vector retrieval、
  summarization 和 external validation automation 都不在范围内。

### Relationship State

Relationship state 是 agent 与另一个 agent、entity 或 world reference 之间关系的结构化、可检查表示。

必须满足的语义：

- 计划中的记录应识别 subject agent、target reference、relationship dimensions、
  provenance 和 updated time。
- 在 v0.5 中，relationship state 只保留 contract/schema semantics，直到后续已评审 package 明确授权 behavior。
- 本包和 `0.5.2` 都不得让 relationship state 改变 action semantics。

### Self-Summary

Self-summary 是 agent continuity state 的可检查摘要，例如稳定 identity notes、current goals、
memory-derived themes 或 operator review notes。

必须满足的语义：

- 计划中的记录应识别 agent、world、summary text 或 structured facets、provenance、
  created/updated time 和 evidence references。
- 本包不实现 self-summary generation。
- 不授权 automatic summarization、LLM call 或 action modifier。

### Reflection Record

Reflection record 是 agent self-assessment、feedback processing 或 decision review 的可审查记录。

必须满足的语义：

- 计划中的记录应识别 agent、world、trigger、reflection content、evidence references、
  created time 和 source。
- 本包不实现 automatic reflection behavior。
- reflection records 必须可审计，不得静默重写 memory 或 action behavior。

### Personality Drift Signal

Personality drift signal 是可检查信号，后续可能描述 behavioral tendency、preference 或 decision pattern 的变化。

必须满足的语义：

- 计划中的记录应识别 agent、world、signal dimension、direction、strength、
  evidence references、source 和 created time。
- drift signal 在本包中不改变 action selection。
- 任何未来 action-modifier behavior 都需要后续已评审 package。

## `0.5.2` 授权条件

`0.5.2-working-and-episodic-memory-substrate` 只有在以下条件全部成立后才可以实现：

- package 包含 README、intent、contract、technical-design、test-plan、plan、review 和中文镜像。
- contract 将实现限制为 additive generic working-memory / episodic-memory schemas、
  generic in-memory substrate 和 focused backend tests。
- documentation/contract evaluator 报告无 P0/P1，且无 blocking P2。
- `0.5.2/review.md` 记录 `implementation_authorized: yes`。
- planned tests 覆盖 focused memory tests、相邻 v0.4 loop/API compatibility tests、
  docs/mirror checks 和 changed-file scope guard。

## 兼容性要求

- 保持 v0.4 `PerceptionFrame`、`ActionIntent`、`ActionResult`、
  request-scoped `LoopStep` 和 `POST /world/agent/loop/step` behavior。
- 保持 `/world/agent/params/propose-and-apply`、runtime tick/time、event routes、
  params behavior、archive behavior、API envelope/error shape 和可选 `Event.refs`
  serialization。
- 计划中的 schema changes 必须是 additive。
- 历史 v0.4 evidence 只作为 handoff context，不是当前 v0.5 pass evidence。

## 允许修改

- 创建并更新
  `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/` 下的文档。
- 仅为准确交接更新父级 v0.5 status surfaces。
- 定义 public concept contracts、planned schema semantics、compatibility requirements
  和 implementation authorization criteria。
- 记录只读 evaluator findings 和 documentation verification evidence。

## 禁止修改

- 不修改 `backend/app/**`、`backend/worldengine/**`、`frontend/**`、migrations、
  fixtures、generated results、external repositories 或 backend tests。
- 不创建 `backend/app/schemas/agent_memory.py`、`backend/app/agent/memory.py`
  或任何 `test_agent_memory_*.py` 文件。
- 不添加 runtime APIs、persistence、vector search、LLM summarization、
  reflection automation、relationship behavior、personality drift action modifiers、
  frontend behavior 或 world generation。
- 不添加 concrete world content 或 private validation oracle details。

## North Star 检查

本包通过把 memory、relationship、reflection、self-summary 和 drift 变成可检查工程契约，
推进 North Star 中 pseudo-self 的方向。它保持 engine generic，不把仓库收窄成 game、demo 或 projection application backend。

## 范围外后续工作

- `0.5.2`：实现 working/episodic memory schemas 和 in-memory substrate。
- `0.5.3`：把 bounded read-only memory context 接入 loop perception。
- `0.5.4`：细化 relationship/self-summary/reflection/drift contracts，并决定 schema-only implementation 是否继续推迟。
- v0.6：world generation。
- v0.7：external validation readiness 和 report automation。
- v0.8：projection application readiness。

# 契约

状态：review complete

## Package 决策

`0.5.4` 是 documentation-only。它细化 schema semantics 和 authorization criteria，
但不添加 schema files 或 backend behavior。

Implementation authorization 保持 `no`。

## Relationship State

Relationship state 是 agent 与另一个 generic target reference 之间关系的可检查描述。

任何未来 schema 必须满足：

- 识别 `agent_id`、`world_id`、稳定 relationship record id 和 generic `target_ref`。
- 使用 generic relationship dimensions，例如 familiarity、trust、obligation、
  alignment、conflict 或 affinity，但不得编码具体 characters、locations、factions、
  resources 或 story rules。
- 包含 observed events、operator review、imported state 或 derived analysis 的
  provenance 和 evidence references。
- 包含 `created_at`、`updated_at`、source、可选 confidence 和可选 observation window。
- 在后续已评审 behavior package 明确授权用于 action selection 前，只能作为 inspectable
  data。

v0.5.4 禁止：

- Relationship state 不得修改 action choice、params patches、runtime events、memory
  selection 或 API behavior。

## Self-Summary

Self-summary 是 agent continuity state 的可检查摘要。

任何未来 schema 必须满足：

- 识别 `agent_id`、`world_id`、稳定 summary id、summary text 或 generic facets、
  source、created/updated time 和 evidence references。
- 区分 operator-authored、imported 和 derived summaries。
- 包含 version 或 supersession semantics，使 summaries 可审计，而不是被静默覆盖。
- 避免声称 consciousness、sentience 或 true selfhood。该记录只是 continuity state
  的 engineering summary。

v0.5.4 禁止：

- 不授权 self-summary generation、LLM summarization、automatic compression、
  automatic memory rewrite 或 action modifier。

## Reflection Record

Reflection record 是 self-assessment、feedback processing 或 decision review 的可审计记录。

任何未来 schema 必须满足：

- 识别 `agent_id`、`world_id`、稳定 reflection id、trigger、source、created time、
  content 和 evidence references。
- 如果使用 structured facets，应区分 observation、critique、hypothesis 和 proposed
  follow-up sections。
- 将 proposed updates 与 applied changes 分开。
- 保留导致 reflection 的 evidence trail。

v0.5.4 禁止：

- 不授权 automatic reflection loop、memory rewrite、relationship update、self-summary
  update 或 action behavior change。

## Personality Drift Signal

Personality drift signal 是关于 behavioral tendency、preference 或 decision pattern
可能变化的可检查信号。

任何未来 schema 必须满足：

- 识别 `agent_id`、`world_id`、稳定 signal id、dimension、direction、strength、
  source、created time 和 evidence references。
- 尽可能包含 baseline reference 或 observation window。
- 通过 confidence 或 review status 显式表达 uncertainty。
- 保持为 signal，而不是 direct behavior rule。

v0.5.4 禁止：

- Drift signals 不得改变 action choice、action validation、params patches、memory
  ranking 或 loop output。

## 未来授权条件

后续 package 只有在满足以下条件后，才可以实现 schema-only support：

- package 在 implementation 前明确标记为 mixed 或 code。
- 所有 required package docs 和 mirrors 存在。
- documentation/contract evaluator 报告无 P1 且无 blocking P2。
- `review.md` 记录 `implementation_authorized: yes`。
- 第一个 production change 前已有并运行 focused failing test。
- contract 保持 changes additive 且 generic。
- validation 包含 focused schema tests、touched loop/API surfaces 的 compatibility
  checks、docs/mirror checks 和 changed-file scope guard。

任何会影响 action selection、memory ranking、summaries、relationships、reflection 或
drift 的 behavior，都需要后续 behavior-specific package，不能伪装成 schema-only work。

## 兼容性要求

- `PerceptionFrame.memory_context` 保持 read-only perception data。
- `LoopStepRequest`、`ActionIntent`、`ActionResult`、action adapter semantics、
  params behavior、event routes、runtime tick/time、archive behavior 和 API
  envelope/error shape 保持不变。
- 现有 v0.5 memory substrate 和 memory context tests 只作为其所属 package 的当前证据，
  不授权在本 package 扩大 behavior。

## 允许修改

- 本目录下的 package docs 和 mirrors。
- 仅为准确交接更新 parent v0.5 status/review surfaces。

## 禁止修改

- 不修改 backend code、backend tests、frontend files、migrations、generated results、
  fixtures、external repositories 或 `backend/worldengine/**`。
- 不添加 public memory APIs、loop request selectors、persistence、vector retrieval、
  LLM summarization、automatic reflection、relationship behavior、self-summary
  generation、drift action modifiers、concrete world content、private validation
  oracle details 或 application-specific backend logic。

## North Star 检查

本 package 通过让剩余 continuity concepts 在 behavior 前变得可检查且有边界，推进
North Star 中 pseudo-self 的方向。它不声称 agent consciousness，也不把 WorldEngine
变成 world-specific application backend。

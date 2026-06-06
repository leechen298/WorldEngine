# 合同

英文原文：`contract.md`。

## 公开概念

`WorldEventCandidate`

- 规则关联世界演化的公开候选事件。
- 包含 candidate id、world id、可选 branch id、event type、source、proposed tick/time window、公开 cause refs、公开 location refs、公开 rule refs、公开 parameter patches、direction refs、probability evidence、causality evidence 和 public summary。
- Extra fields 必须被拒绝。
- 在合法性评估接受之前，它不是 canonical event。
- 不得包含 raw prompts、raw provider responses、provider traces、hidden context、private Agent memory、private goals、private evaluator data、raw thought、chain-of-thought、authorization headers、API keys、secrets 或 concrete demo-world oracle data。

`WorldEventLegalityResult`

- 事件候选的公开确定性结果。
- Status values：
  - `accepted`
  - `rejected`
  - `blocked`
- 包含公开 legality classification、diagnostics、matched rule ids、checked constraint ids、referenced parameter ids、timing evidence、probability evidence、causality evidence、redaction status，以及 accepted 时的 state-diff summary。
- Rejected results 不得 enqueue 或 append accepted world-evolution event。

`WorldStateDiff`

- 被接受候选导致的参数变化公开摘要。
- 包含 changed parameter ids、paths、old public values、new public values、operation、rule id、constraint ids 和 public explanation。
- 如果检测到 private marker，diff values 必须 redacted。
- Diff 只限于公开 rule/parameter state，不得修改 Agent private state。
- 如果实现应用 accepted patches，diff 就是必需的公开 replay artifact，用来证明哪些公开 in-memory parameter state 发生了变化。

`WorldEvolutionEvidence`

- 附加到 accepted event 或由 API helper 返回的公开 evidence artifact。
- 包含 rule linkage、state snapshot references、direction refs、legality status、diagnostics count、state-diff summary 和 redaction status。
- 它的形状应当可供 checker 消费，但本包不实现 checker fixtures，也不执行 checker validation。

`WorldEvolutionSummary`

- 某个 world 的 accepted/rejected event candidates 公开摘要。
- 如果 implementation 需要 public inspection surface，可以实现为 in-memory helper 或 route。

## 必需合法性检查

Legality evaluation 必须以确定性方式 reject 或 diagnose：

- candidate rule refs 不能解析到公开 rule ids。
- parameter patches 指向 unknown parameter ids。
- patch operations 不在 matched rule 允许的操作列表中。
- parameter values 超出公开 constraints。
- candidate timing 超出当前 bounded runtime tick/time window。
- 绕过 rule effects 的 direct final facts。
- direct Agent private-state、goal、inventory、relationship、life/death 或 private location mutation。
- candidate evidence 或 refs 包含 private markers。
- event candidate 缺少 public cause、rule、timing 或 state evidence。

只有满足以下条件时，legality evaluation 才可以接受 candidate：

- 至少匹配一个 public rule。
- 每个 proposed patch 都 target matched rule 覆盖的 public parameter。
- 每个 operation 都被 matched rule 允许。
- patch 后 public constraints 仍满足。
- timing evidence 与 current runtime state 兼容。
- causality evidence 和 probability evidence 以公开形式存在。
- 关联的 direction guidance 保持 bounded，不直接强制 final fact。

Accepted candidates 只有在 legality evaluation 接受后，才可以将公开 parameter patches 应用到 active in-memory `WorldState`。实现必须在同一个 request flow 中记录 accepted event 和公开 replay/diff evidence。本包不授权 durable storage、persistent rule installation、background evolution 或 hidden state mutation。

## 允许修改

Documentation review 授权后，本包可以修改：

- `backend/app/schemas/` 中的 additive schemas，用于 event candidates、legality results、state diffs 和 evolution evidence。
- `backend/app/core/` 下的窄 deterministic helpers，用于 legality evaluation 和公开 state-diff construction。
- 仅针对 accepted legal candidates 的 active-backend in-memory public parameter updates；这些更新必须使用 public rule-linked patches，并记录 diff/replay evidence。
- `backend/app/api/routes/world.py`、`backend/app/api/routes/runtime.py` 或窄 active-backend route module，仅用于 additive public route behavior，或必要的 manifest/OpenAPI exposure。
- event payload construction，仅用于给 accepted events 增加公开 legality/evolution evidence。
- `backend/app/tests/` 下的 focused backend tests。
- package `review.md` 和 `review.zh.md`。
- review 或 implementation closeout 后，仅用于 route/status handoff 的 v0.9 parent status/review docs。

## 禁止修改

本包不得：

- 修改 `backend/worldengine/`。
- 修改 frontend code。
- 修改 Validation Client 或 external repositories。
- 执行 live provider calls 或 LLM interpretation。
- 创建 generated worlds、generated rules 或 generated-result artifacts。
- 执行 checkers 或修改 checker fixtures。
- 运行 external validation 或 autonomous validation。
- 实现 durable scheduling、background workers、cron、queue services 或 deployment infrastructure。
- 实现 Agent continuity、memory consolidation、narrative projection 或 diagnostic dialogue。
- 修改 Agent private memory、goals、personality、skills、relationships、inventory、life/death 或 private location state。
- 添加 concrete demo-world names、maps、characters、locations、resources、story rules、validation oracle data 或 application-specific backend behavior。
- 存储或导出 API keys、authorization headers、raw prompts、raw provider requests、raw provider responses、provider traces、hidden context、private Agent memory、raw thought、chain-of-thought 或 private evaluator data。
- 声明 provider live-call PASS、checker PASS、external validation PASS、product readiness 或 full v0.9 closeout。

## 兼容性要求

- Existing event schemas 和 `/world/events` behavior 必须保持 additive-compatible。
- Existing `/world/event-steps`、`/world/snapshots` 和 archive behavior 必须保持 additive-compatible。
- Existing runtime bounded-run 和 `/runtime/step` behavior 必须保持 compatible。
- Existing `/world/params` 和 `/world/params/apply` behavior 必须保持 compatible。
- `0.9.3` 的 existing generated rule/parameter validation behavior 必须保持 compatible。
- Existing `/worlds/{world_id}/direction` 和 `/worlds/{world_id}/director-guidance` behavior 必须保持 compatible。
- Existing public handoff manifest behavior 必须保持 compatible。
- New request schemas 必须 reject extra fields 和 private markers。
- Accepted event evidence 不应依赖 checker support 才有用。
- Rejected candidates 不得 append canonical accepted events 或 mutate public state。
- Accepted candidates 的 public state changes 必须能通过 recorded diff、rule refs 和 event evidence 复现。

## North Star 检查

本包通过把 events 连接到 public rules 和 state，而不是插入 arbitrary story outcomes，保持 WorldEngine 的通用性。它强化后续 Agent continuity 所需的 event spine，同时保留 Agent pseudo-self work 属于后续 packages 的边界。

## 后续包范围

- `0.9.8`：brain-inspired Agent continuity and consolidation evidence。
- `0.9.9`：narrative projection and diagnostic dialogue boundaries。
- `0.9.10`：LLM-backed checker fixtures、schema 和 scorecard support。
- `0.9.12`：live or blocked full lifecycle validation execution。

## 退出条件

本包只有在以下条件满足后才可 close：

- required package docs 和 mirrors 存在。
- documentation/contract evaluator 报告无 P0/P1，且无 blocking P2。
- code changes 前已记录 implementation authorization。
- focused tests 证明合法事件接受、非法事件拒绝、受方向引导但仍符合规则的候选接受、timing/rule/constraint diagnostics、redaction、state-diff consistency、extra-field rejection，以及与既有 direction/runtime/event/rule surfaces 的兼容性。
- relevant backend regressions 在当前 session 通过。
- `review.md` 记录 exact commands、changed files、subagent findings、compatibility review、scope review、unresolved findings 和 final route。

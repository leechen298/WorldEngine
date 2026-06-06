# Contract

英文原文：`contract.md`。

## Public Concepts

`WorldDirectionRequest`

- 提交 natural-language world guidance 的 public request。
- 包含 `instruction_text`、optional `branch_id`、optional `apply_after_tick`、
  optional `expires_after_tick` 和 optional `public_context`。
- Extra fields 必须 rejected。
- 当 raw instruction 包含 private markers 时，不得 echo 到 event payloads 或 public
  summaries。

`WorldDirectionClassification`

- Submitted direction 的 public classification。
- Allowed categories：
  - `environment_trend`
  - `external_pressure`
  - `event_candidate_bias`
  - `probability_shift`
  - `rule_constraint`
  - `future_evaluation_hint`
- Forbidden categories：
  - `direct_final_fact`
  - `agent_private_state_mutation`
  - `agent_goal_mutation`
  - `inventory_injection`
  - `relationship_override`
  - `rule_bypass`
  - `private_marker_detected`

`WorldDirectionQueueItem`

- 用于 future world-level consideration 的 public queued guidance item。
- 包含 public id、world id、classification、status、timing window、public summary、
  public context keys、redaction status，以及 optional future rule/adjudication references。
- 它不代表 event outcome、Agent action 或 Agent memory。

`WorldDirectionResponse`

- Public response，status 为 `queued`、`rejected`、`blocked` 或 `unavailable`。
- 包含 classification、accepted 时的 queue item、rejected 时的 public rejection reason，
  并且不包含 direct state mutation evidence。

`WorldDirectionSummary`

- 当前 queued 或 rejected direction items 的 public summary。
- 如果 implementation 选择在本包暴露 queue inspection，可以由 helper 或 endpoint 返回。

## 允许变更

- Active backend schema files 中 additive direction schemas。
- Active backend helper code，用于 deterministic direction classification、redaction 和
  in-memory queue storage。
- Canonical direction submission 的 additive world API route behavior。
- `/worlds/{world_id}/director-guidance` 的 compatibility wrapper 或 compatibility behavior。
- 仅在 public API contract 需要时更新 Manifest/OpenAPI surface。
- Focused backend/API tests。
- Closeout 后的 package-local review documentation 和 parent v0.9 status updates。

## 禁止变更

- 不进行 live provider calls 或 LLM interpretation。
- 不创建 generated-result。
- 不执行 checker，也不修改 checker fixtures。
- 不进行 external validation 或 autonomous validation。
- 不修改 frontend UI 或 Validation Client。
- 不引入 durable scheduler、background worker、queue service、deployment infrastructure 或
  cron-like behavior。
- 不实现 event legality 或 final event adjudication。
- 除存储 future public references 外，不实现 rule-linked parameter evolution。
- 不 mutate Agent continuity、private memory、goal、relationship、inventory、personality、
  skill、life/death 或 location。
- 不让 “Agent X is dead” 这类 direct final facts 成为 canonical state。
- 不加入 concrete demo-world fixtures 或 application-specific logic。
- 不修改 `backend/worldengine/`。

## 兼容性要求

- 既有 `/worlds/{world_id}/director-guidance` 对 benign environmental guidance 的 accepted
  behavior 必须保持兼容。
- 既有 public handoff、world creation、event listing、runtime、generation、
  rule-parameter 和 fidelity tests 必须继续通过。
- 既有 director guidance event payload redaction requirements 必须保留。
- Existing `DirectorGuidanceRequest` / `DirectorGuidanceResponse` 只能 additive 扩展，
  除非本包明确记录一个能保留 old response surface 的 wrapper。
- Direction classification 必须 deterministic，并且无需 provider calls 即可测试。
- Rejected direction 不得 mutate state、enqueue accepted item 或记录 final outcome。

## 范围外后续

- `0.9.7`：rule-linked evolution and event legality。
- `0.9.8`：brain-inspired Agent continuity and consolidation evidence。
- `0.9.10`：checker fixtures and scorecard support。
- `0.9.12`：live or blocked full lifecycle validation execution。

## Exit Criteria

本包只有满足以下条件才可 close：

- required package docs and mirrors exist。
- documentation/contract evaluator reports no P0/P1 and no blocking P2。
- implementation authorization 在代码变更前记录。
- focused tests 证明 allowed environmental direction 会被 queued、direct final outcomes 会被
  rejected、private Agent mutation requests 会被 rejected、timing windows bounded、public
  summaries redacted、extra fields rejected，并且 existing director-guidance compatibility
  preserved。
- relevant backend regressions 在当前 session 通过。
- `review.md` 记录 exact commands、changed files、subagent findings、compatibility review、
  scope review、unresolved findings 和 final route。

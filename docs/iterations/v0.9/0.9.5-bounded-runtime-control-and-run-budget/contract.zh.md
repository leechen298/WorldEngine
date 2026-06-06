# Contract

英文原文：`contract.md`。

## 公开概念

`RuntimeRunRequest`

- Bounded runtime advancement 的 public request。
- 支持以下两者之一：
  - `ticks`：运行有限 tick 数。
  - `duration_seconds`：运行直到至少推进指定 world time。
- 包含 `max_ticks`、`max_duration_seconds`、`max_provider_calls` 和
  `max_estimated_cost_units` guards。

`RuntimeControlState`

- Public runtime-control state，`status` 可为 `running`、`paused` 和 `idle`。
- 不创建 durable scheduling。

`RuntimeRunSummary`

- Bounded run 的 public summary。
- 包含 start/end tick、start/end world time、ticks requested、ticks executed、stop
  reason、guard summary、provider/cost counters 和 redaction status。

## 允许修改

- 在 active backend schema files 中添加 additive runtime-control schemas。
- 在 RuntimeEngine methods 或 adjacent active-backend helper code 中添加 bounded run、
  pause、resume 和 control state。
- 在 `backend/app/api/routes/runtime.py` 中添加 Runtime API endpoints。
- 仅当 existing app route registration 需要时，更新 manifest/OpenAPI exposure。
- Focused backend/API tests。
- Closeout 后更新 package-local review documentation 和 parent v0.9 status。

## 禁止修改

- 不进行 live provider calls。
- 不创建 generated-result。
- 不运行 checker execution 或修改 checker fixtures。
- 不进行 external validation 或 autonomous validation。
- 不修改 frontend UI 或 Validation Client。
- 不实现 durable scheduler、background worker、queue、deployment infrastructure 或 cron-like behavior。
- 不实现 event legality 或 rule-linked parameter evolution。
- 不实现 Agent continuity、memory consolidation、narrative projection 或 diagnostic dialogue behavior。
- 不加入 concrete demo-world fixtures 或 application-specific logic。
- 不修改 `backend/worldengine/`。

## 兼容性要求

- 既有 `/runtime/step` 必须继续只推进一个 tick。
- 既有 `/runtime/state` response fields 必须保持 compatible。
- 既有 event、snapshot、archive、world params、Agent loop 和 world generation tests 必须继续通过。
- New request schemas 必须拒绝 unbounded requests 和 extra fields。
- Pause 必须阻止 multi-tick bounded runs，但不得让既有 `/runtime/step` incompatible，除非 implementation
  contract 明确记录并测试该行为。
- 本包中的 provider-call 和 cost counters 必须保持为零。

## 后续范围

- `0.9.6`：natural-language world direction boundary。
- `0.9.7`：rule-linked evolution and event legality。
- `0.9.8`：brain-inspired Agent continuity and consolidation evidence。
- `0.9.10`：checker fixtures and scorecard support。
- `0.9.12`：live 或 blocked full lifecycle validation execution。

## 退出条件

本包只有在以下条件满足后才能 close：

- required package docs 和 mirrors 存在。
- documentation/contract evaluator 报告无 P0/P1 且无 blocking P2。
- code changes 之前已记录 implementation authorization。
- focused tests 证明 bounded tick runs、bounded duration runs、pause/resume、max guard
  rejection、zero provider/cost counters、public run summary 和 single-step compatibility。
- 当前会话 relevant backend regressions 通过。
- `review.md` 记录 exact commands、changed files、subagent findings、compatibility
  review、scope review、unresolved findings 和 final route。


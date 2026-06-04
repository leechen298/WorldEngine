# Technical Design

英文版本：`technical-design.md`。

## Current State

`tools/testing/validate_agent_autonomous_result.py` 当前接受一组固定 dashboard
saved-result scenarios。它校验 required artifacts、operation log shape、UI target
coverage、score items、unresolved P1 findings 和 scorecard summary status。

它不会校验 lifecycle-specific evidence，例如 world creation、runtime tick
progression、Agent autonomy、external direction boundaries 或 redaction scans。

## Contract Alignment and Invariants

- Agent operation logs 继续只允许 UI/CLI。
- WorldEngine API evidence 存在 redacted artifacts 中。
- 现有 scenarios 保持当前 required UI target 行为。
- 新场景保持 generic，不包含 concrete world content。

## Proposed Implementation

把 `worldengine-full-lifecycle-autonomous` 加入：

- autonomous scenario index。
- `result-schema.json`。
- checker supported scenario set。
- required UI target coverage。

为新场景增加 lifecycle-specific artifact validation：

- `artifacts.api_summary` 必须存在。
- `artifacts.world_lifecycle_summary` 必须存在。
- `world-lifecycle-summary.json` 必须包含以下 pass sections：
  - `world_creation`。
  - `runtime_progression`。
  - `agent_autonomy`。
  - `external_direction`。
  - `evidence_integrity`。

checker 应拒绝：

- lifecycle summary 缺失。
- tick 没有推进。
- 未观察到 events。
- 未观察到 Agent actions。
- client-scripted Agent actions。
- direct Agent private-state mutation。
- redaction scan failed。

## Affected Surfaces

- autonomous validation docs。
- autonomous result schema。
- autonomous checker。
- checker tests and fixtures。
- Makefile fixture target。

## Data Model / Schema Changes

result schema 新增一个 scenario enum value。`additionalProperties` 保持 true，因此是
additive。

`world-lifecycle-summary.json` 是 checker artifact，不是 public API schema。

## Runtime / Service Design

不改变 runtime 或 service behavior。

## Compatibility

现有 saved-result fixtures 和 scenarios 必须继续通过。invalid fixtures 必须继续失败。

## Risks

- checker 只能验证已记录 evidence，不能执行 live run。scenario 和 review 必须说明这个区别。
- Agent autonomy evidence 是 bounded：checker 可以拒绝 client scripting 和缺失
  WorldEngine evidence，但不能证明哲学意义上的意识。
- lifecycle summary 必须避免 private provider traces 和 private Agent state。

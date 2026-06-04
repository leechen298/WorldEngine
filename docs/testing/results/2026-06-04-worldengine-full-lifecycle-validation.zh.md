# WorldEngine 完整生命周期自主验证

Status: FAIL
Mode: live full lifecycle validation plus saved-result checker
Date: 2026-06-04

英文版本：`2026-06-04-worldengine-full-lifecycle-validation.md`。

## Scope

本文记录 `worldengine-full-lifecycle-autonomous` 场景、checker support 和 generic
fixture 作为 testing assets 加入后，第一次正式 full lifecycle validation run。

这是 testing result，不是 iteration package。它不占用 WorldEngine product iteration
编号。

## Scenario

权威场景：

- `docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md`

Checker：

- `tools/testing/validate_agent_autonomous_result.py`

Result directory：

- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/`

## Command

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle
```

Result：failed。

Checker failure：

```text
FAIL: world-lifecycle-summary.json evidence_integrity.redaction_scan_passed must be true
```

## Covered Evidence

本次 run 在 redaction 失败前覆盖了要求的 lifecycle surfaces：

- 通过 Validation Client 创建 WorldEngine-backed world。
- Public world id：`world-16df0fbcaa35`。
- Runtime progression：tick `0` 到 tick `10`。
- Events observed：`42`。
- Snapshots observed：`1`。
- WorldEngine-backed Agent action event observed：`1`。
- Director guidance 通过 public surface accepted。
- Validation Client 导出 evidence bundle。

Supporting artifacts：

- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/result.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/world-lifecycle-summary.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/scorecard-summary.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/validation-client-evidence-bundle.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/raw/`

## Failure Analysis

这不是 UI smoke failure，也不是 tick/event/snapshot 缺失。直接 checker failure 是
evidence integrity。

Validation Client 导出：

```json
"private_worldengine_internals_included": true
```

并记录 warning：

```text
sensitive content redacted from evidence records
```

redaction trigger 与 WorldEngine public director guidance response 在 public
explanation 中包含 private/internal marker terms 一致。当前 public response 文本直接点名
private Agent memory、goal、identity、relationship、`self_state` 和 hidden context
等 protected concepts。Validation Client 保守地将这些 marker 视为敏感内容，并在 evidence
bundle 中 redacts explanation。

## Boundary

不要通过放宽 checker 或忽略 redaction flag 把本结果改成 PASS。

正确 follow-up 是创建新的 product repair iteration，调整 WorldEngine public output，
让它能表达边界，但不输出 private/internal marker terms。

## Recommended Follow-up

创建新的 reviewed implementation package，例如：

```text
0.8.9.2-director-guidance-public-redaction-repair
```

建议 repair scope：

- WorldEngine public director guidance response 必须使用 public-safe wording。
- Public output 不得包含 private memory、private goals、relationship internals、
  `self_state`、hidden context、raw provider traces 或 private prompts 等 private
  marker terms。
- Autonomous checker 也应拒绝把 direct public API calls 伪装成 CLI operations 的
  operation-log entries。Direct API evidence 应进入 `api-summary.json`，不是 Agent
  operation log。

修复后，重新运行同一个 full lifecycle validation 和 checker command。

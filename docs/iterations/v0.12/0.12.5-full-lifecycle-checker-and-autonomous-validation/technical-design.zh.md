# Technical Design

英文原文：`technical-design.md`。

## Existing Checker Entry Points

仓库已定义 deterministic autonomous checker entry points：

```bash
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=<dir>
```

这些命令使用 `tools/testing/validate_agent_autonomous_result.py`。

## Supported Evidence Modes

1. `fixture_checker_validation`：验证内置 fixtures 和 checker behavior。这只能作为 checker evidence PASS。
2. `saved_result_validation`：验证现有 result directory。如果 result 早于 v0.12，必须标为 historical，且只能对该 saved result PASS。
3. `fresh_external_validation`：验证当前 external Validation Client export。只有 result directory 为本 package/session 新产出并通过 checker/review 时，才能支持 v0.12 PASS。

## Expected Result Docs

Evidence execution 后创建：

- `full-lifecycle-validation-result.md`：exact commands、result dirs、statuses、blocker/partial/fail rationale 和 final package classification。
- `scorecard-summary.md`：scorecard/checker items、verdict sources、redaction status 和 unverified items。
- `read-only-evaluator-review.md`：second-agent read-only review findings。

## Blocker Handling

如果 fresh external result directory 不可用，记录：

```text
fresh_external_validation_status: BLOCKED
blocker_owner: WorldEngine-Validation-Client or environment/provider/checker
v0.12_mvp_pass_supported: false
```

不得创建 synthetic evidence 来让 checker pass。

## Redaction Boundary

所有 result docs 必须避免 raw prompts、raw provider responses、raw thought、private Agent memory、private goals、provider traces、secrets、tokens 和 private evaluator data。

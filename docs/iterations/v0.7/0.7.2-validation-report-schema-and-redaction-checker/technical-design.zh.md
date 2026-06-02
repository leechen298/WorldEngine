# Technical Design

## Current State

WorldEngine 当前已有：

- `docs/contracts/external-fixture-runner-contract.md`。
- `docs/contracts/external-validation-readiness-contract.md`。
- `docs/contracts/projection-consumer-contract.md`。
- `docs/validation-report-template.md`。
- `tools/testing/` 下的 Agent smoke 和 Agent autonomous saved-result checkers。

当前还没有 machine-readable external validation report schema 或 checker。
Template 也需要 additive alignment，以匹配 `0.7.1` readiness status taxonomy。

## Implementation Structure

Planned implementation files：

```text
docs/testing/external-validation-report-schema.json
tools/testing/validate_external_validation_report.py
tools/testing/test_validate_external_validation_report.py
```

Planned documentation/template update：

```text
docs/validation-report-template.md
```

Package evidence files：

```text
docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/
```

## Schema Shape

Schema 应定义一个 generic report object，并包含 required fields：

```text
report_id
engine_reference
public_contract_surface
external_suite_id
redacted_target_id
capability_area
scenario_id
high_level_goal
status
observed_public_behavior
redacted_evidence_summary
compatibility_notes
unresolved_findings
redaction_confirmed
forbidden_detail_review
scope_review
```

`status` 必须枚举 `pass`、`fail`、`blocked`、`skipped` 和 `out_of_scope`。
Schema 是 public documentation；checker 负责 JSON Schema 不便表达且不应引入新
dependencies 的 semantic validation。

## Checker Flow

Checker 应：

1. Load a JSON report file。
2. Validate top-level value is an object。
3. Validate required fields and simple field types。
4. Validate `status` is one of the allowed values。
5. Validate `redaction_confirmed` is true。
6. Validate every `forbidden_detail_review` flag is false。
7. Validate `pass` reports include public behavior and evidence summary and
   have no unresolved P1/P2 findings。
8. Validate `blocked`、`skipped`、`out_of_scope` reports include explicit reason，
   且不被当成 pass。
9. Scan report strings for generic redaction-risk markers，例如 absolute
   private paths、UI-selector markers、hidden reset markers、oracle-internal
   markers、seed-data markers、transcript markers 和 external event payload markers。
10. 对每个 error 打印 deterministic `FAIL:` line，或成功时打印一个 deterministic
    `PASS:` line。

Checker 不得 import private fixture data，也不评估 external suite truth。它只检查
report shape 和 redaction safety。

## Test Strategy

Focused tests 应在 memory 中构建 report dictionaries，并写入 temporary JSON files。
它们只能使用 abstract identifiers。

Required cases：

- valid `pass` report passes。
- missing required field fails。
- unsupported status fails。
- `pass` with `redaction_confirmed: false` fails。
- `pass` with unresolved P1/P2 fails。
- `blocked` without reason fails。
- valid `blocked`、`skipped`、`out_of_scope` reports pass as non-pass statuses。
- report containing forbidden detail review flag set to true fails。
- report containing private path、UI selector、hidden reset、oracle internal、
  seed-data、transcript 或 event payload marker fails。
- CLI returns `0` on valid input and `1` on invalid input。

## Compatibility Strategy

- Implementation isolated to new checker and schema。
- 不修改 Agent smoke/autonomous checkers 或其 schemas。
- 只使用 Python standard library。
- Additively update `docs/validation-report-template.md`，让 existing human
  report structure 保持可识别。
- 所有 examples 保持 abstract and redacted。

## Anti-Drift Rules

- Parent and child status surfaces closeout 前必须一致。
- `implementation_authorized: yes` 只能在 evaluator approval 后出现。
- Checker 不得使用 private consumer knowledge。
- `blocked`、`skipped`、`out_of_scope` 绝不能被 accepted as pass。
- Tests 不得包含 concrete external validation world details。
- Review evidence 必须区分 focused checker tests 与未运行的 broader
  runtime/API/frontend/E2E/Agent/autonomous checks。

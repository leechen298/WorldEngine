# Test Plan

英文原文：`test-plan.md`。

## 文档门禁

```bash
git diff --check
python3 required-file completeness check
rg -n "^implementation_authorized: yes|^evidence_execution_authorized: yes|^provider_live_call_authorized: yes|^external_validation_authorized: yes" docs/iterations/v0.12/0.12.5-full-lifecycle-checker-and-autonomous-validation docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
python3 package whitespace check
```

预期结果：

- `git diff --check` exit `0` 且无输出。
- package completeness 返回 `{'missing': [], 'empty': []}`。
- active yes authorization scan 在 review authorization 前 exit `1`。
- package whitespace check 返回空 `problems` list。

## 授权后的 Checker Verification

只有 documentation review 通过并记录 `evidence_execution_authorized: yes` 后运行：

```bash
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=tools/testing/fixtures/agent-autonomous/valid-worldengine-full-lifecycle
git diff --check
```

预期结果：

- fixture checker command exit `0`。
- full lifecycle fixture checker command exit `0`。
- fixture command 中 invalid fixtures 按预期失败。
- `git diff --check` exit `0`。

## Fresh External Validation Decision

如果当前 v0.12 external Validation Client result directory 存在，运行：

```bash
make validate-agent-autonomous-result RESULT_DIR=<current-v0.12-result-dir>
```

如果当前 result directory 不存在，记录 `fresh_external_validation_status: BLOCKED`，并且不声明 v0.12 MVP PASS。

## 未授权则不运行

- Provider live calls：未授权。
- External Validation Client implementation：本仓库禁止。
- Frontend/E2E：不属于本包。
- Complete MVP closeout：属于 `0.12.6`。

## No-Unverified-Claims Rule

除非当前 session 已检查 current result directory 并记录结果，否则不得声明 fresh autonomous validation、provider live PASS、external Validation Client PASS 或 complete MVP PASS。

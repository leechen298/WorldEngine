# Review

Status: review complete
implementation_authorized: yes

## 变更文件

预期 package 文件：

- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/README.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/intent.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/contract.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/technical-design.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/test-plan.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/plan.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/review.md`
- 每个 package document 对应的中文镜像。

已实现文件：

- `docs/contracts/projection-read-model-contract.md`
- `docs/contracts/projection-read-model-schema.json`
- `tools/testing/validate_projection_read_model_contract.py`
- `tools/testing/test_validate_projection_read_model_contract.py`

## 已运行命令

- `git diff --check` -> pass。
- `python3 -c 'from pathlib import Path ... missing_0_7_4_docs=0 ...'` -> pass，
  `missing_0_7_4_docs=0`。
- `rg -n "... child docs not created ..."` 检查 parent v0.7 status surfaces -> 无匹配，
  预期 exit `1`。
- `python3 -c 'import subprocess ... changed-file scope guard ...'` -> pass，
  `changed_or_untracked=92`，`out_of_scope_changed_or_untracked=0`。
- `backend/.venv/bin/python -m pytest tools/testing/test_validate_projection_read_model_contract.py`
  -> code-review P2 修复前 16 passed；新增 unsupported top-level key 和 extra family 拒绝测试后
  18 passed。
- `backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json`
  -> `PASS: validated projection read model contract at docs/contracts/projection-read-model-schema.json`。
- `backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py`
  -> 13 passed。
- `backend/.venv/bin/python -m json.tool docs/contracts/projection-read-model-schema.json`
  -> pass。
- `git diff --check` -> implementation 后 pass。
- `python3 -c 'import subprocess ... changed-file scope guard ...'` -> implementation 后 pass，
  `changed_or_untracked=96`，`out_of_scope_changed_or_untracked=0`。

## 测试结果

Implementation tests passed：

- Projection read-model checker tests：code-review P2 修复后 18 passed。
- Projection read-model CLI validation：PASS。
- Readiness manifest adjacent regression：13 passed。
- Projection read-model schema JSON parse：pass。

Backend runtime tests、frontend tests、API smoke、E2E、Agent smoke live run、full
autonomous runner、external validation suite、projection application validation 和 release
checks 未运行，因为本 package 只改变 contract/schema/checker/test files，且不声明这些 surfaces。

## Subagent / Evaluator Evidence

- Parfit documentation/contract evaluator：
  `PASS: authorize implementation`。
- Aquinas mirror/scope evaluator：
  `PASS: mirrors/scope OK for implementation authorization`。
- Parfit implementation-scope/code-review evaluator 曾报告 P2：unsupported top-level capability
  keys 和 extra families 未被拒绝。Checker 已改为拒绝 unsupported top-level keys 和 unsupported
  families，并补充回归测试。最终结果：`PASS: implementation/code review OK`。
- Aquinas validation-evidence/scope evaluator：
  `PASS: validation evidence OK for 0.7.4 closeout after review update`。
- Parfit closeout consistency evaluator：
  `PASS: closeout consistency OK for 0.7.4 review complete`。
- Aquinas mirror/closeout consistency evaluator：
  `PASS: mirrors/closeout consistency OK for 0.7.4 review complete`。

## 兼容性评审

Documentation gate 与 implementation evidence 已通过。实现只落在 projection read-model
contract、schema、checker 和 test files。Runtime、API、frontend、persistence、
migrations、generated results、external repositories 和 `backend/worldengine/` 都不在本包范围内。

## 范围评审

Changed-file scope guard 在 implementation authorization 前通过：
`changed_or_untracked=92`，`out_of_scope_changed_or_untracked=0`。Implementation 后再次通过：
`changed_or_untracked=96`，`out_of_scope_changed_or_untracked=0`。

## 未解决发现

- P1：none。
- P2：none。
- P3：none。

## 已解决发现

- P2：checker 曾允许 unsafe extra top-level capability keys 和 unsupported read-model
  family keys。已通过拒绝 unsupported top-level keys 与 unsupported families，并补 focused
  regression tests 修复。

## 最终评估

Review complete。Parent v0.7 route/status 已 handoff 到
`0.7.5-quality-regression-and-compatibility-evidence`。本 package 不声明
runtime/API/frontend/E2E/Agent smoke/autonomous/external suite/projection application/product/v0.8
readiness。

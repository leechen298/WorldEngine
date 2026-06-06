# Plan

英文镜像：`plan.md`。

Status：implementation complete / verification passed

## Objective

把 LLM-backed autonomous validation suite 从 `checker-extension-required` 文档转换为
checker-supported saved-result contracts、fixtures 和 regression tests。

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/AGENTS.md`
- `docs/project-north-star.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/llm-backed-suite-execution.md`
- `docs/testing/agent-autonomous/scenarios/` 下的 LLM-backed scenario docs
- `tools/testing/` 下当前 saved-result checker 和 fixtures

## Files

Create：

- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/README.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/README.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/intent.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/intent.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/contract.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/contract.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/technical-design.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/technical-design.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/test-plan.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/test-plan.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/plan.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/plan.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/review.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/review.zh.md`

Documentation review 后才可 modify：

- Evaluator 报告无 P0/P1/P2 findings 后，parent v0.9 route/status docs 已从
  documentation-review-needed 推进到 implementation-authorized。

Authorization 后的 implementation files：

- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/**`
- `docs/testing/agent-autonomous/result-schema.json`
- `docs/testing/agent-autonomous/**` 下的 LLM-backed testing docs

Do not touch：

- `backend/worldengine/**`
- `backend/app/**` 下的 product runtime behavior
- `frontend/**`
- external repositories 或 Validation Client code
- generated result directories used as evidence，除非它们是本 package 明确的 checker fixtures。

## Steps

1. Draft 完整 0.9.10 package document set。
2. 运行 documentation checks。
3. 将 package docs 交给 read-only documentation/contract evaluator。
4. Documentation/contract evaluator 已报告 PASS 且无 P0/P1/P2 findings；child 和 parent docs
   已更新为 implementation-authorized。
5. 只实现授权的 checker/fixture/test/documentation scope。
6. 运行 `test-plan.md` 中的 commands。
7. closeout 前交给 implementation-scope evaluator。
8. 只有 verification 和 evaluator review 都通过后，更新 `review.md` 并把 parent route 推进到
   `0.9.11`。

## Verification

Documentation-stage verification：

- `git diff --check`
- package completeness scan。
- status/authorization scan，防止 accidental implementation authorization。

Implementation-stage verification：

- `make validate-agent-autonomous-fixtures`
- `backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q`
- `backend/.venv/bin/python -m pytest tools/testing -q`
- `git diff --check`
- forbidden runtime/frontend/Validation Client changes scope scan。

## Stop Conditions

- Required package documents 或 mirrors 缺失。
- Documentation review 报告 P0/P1/blocking P2。
- Implementation 需要 product runtime、provider call、frontend 或 Validation Client changes。
- Checker PASS 依赖 subjective judgment 或 missing public artifacts。
- Redaction requirements 无法用 saved-result artifacts 执行。

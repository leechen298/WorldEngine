# Contract

英文镜像：`contract.md`。

## Public Concepts

- `LLM_BACKED_SCENARIOS`：六个 LLM-backed autonomous scenario names：
  `provider-live-smoke-deepseek`、`llm-backed-world-creation`、
  `world-rule-parameter-evolution`、`rule-compliant-event-generation`、
  `agent-persistent-autonomy-evidence` 和
  `llm-backed-full-lifecycle-autonomous`。
- `llm_backed_result_status`：scenario status values `pass`、`fail`、`blocked` 和
  `not_run`。
- `llm_backed_artifact_summary`：
  `docs/testing/agent-autonomous/llm-backed-artifact-contract.md` 定义的 required public JSON
  artifacts。
- `llm_backed_scorecard_item`：
  `docs/testing/agent-autonomous/llm-backed-scorecard.md` 中的 deterministic critical items。
- `redaction_scan`：证明 forbidden markers 不存在的 public evidence。
- `second_agent_review_status`：用于 full lifecycle PASS gating 的 read-only review result。

## Compatibility Constraints

- 现有 dashboard scenarios 和 `worldengine-full-lifecycle-autonomous` saved-result checker
  behavior 必须保持 compatible。
- 现有 fixture commands 必须继续可用：
  `make validate-agent-autonomous-result RESULT_DIR=<dir>` 和
  `make validate-agent-autonomous-fixtures`。
- Result schema extensions 必须 additive。Existing valid basic fixtures 不得被要求补充
  LLM-backed artifacts。
- 当 required public artifacts 诚实分类 missing provider/evidence prerequisites 时，
  LLM-backed scenarios 可接受 `blocked` 或 `not_run`。
- `pass` result 必须比 `blocked` 或 `not_run` 更严格；missing critical artifacts、redaction
  leaks、failed critical items 或 missing second-Agent review 必须阻止 PASS。

## Allowed Changes

- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/**`
- `docs/testing/agent-autonomous/result-schema.json`
- `docs/testing/agent-autonomous/**` 下的 LLM-backed autonomous testing docs
- 本 package directory 和 parent v0.9 routing/review docs。

## Forbidden Changes

- 不修改 WorldEngine product runtime behavior。
- 不运行 provider live calls，也不处理 provider credentials。
- 不实现 frontend UI。
- 不实现 Validation Client repository。
- 不重写 generated-result 来强行 PASS。
- 不把 concrete external validation world seed data 放进本仓库。
- 不在 `backend/worldengine/` 新增 runtime features。
- 不修改 `backend/app/**`。预期 implementation scope 是 `tools/testing` 加 docs 和 fixtures。

## Required Checker Semantics

- 将 supported scenarios 扩展到六个 LLM-backed scenario names。
- LLM-backed scenarios 允许 `status` values `pass`、`fail`、`blocked` 和 `not_run`，
  同时保留 older scenarios 的 successful-result behavior。
- 要求每个 declared `required_artifacts` entry 存在，且路径 stay inside result directory。
- 根据 artifact contract 验证 scenario-specific required artifact names。
- 当 `redaction` 或 `redaction-scan.json` 包含 API keys、authorization headers、raw prompts、
  raw provider requests、raw provider responses、provider traces、private Agent memory、
  private Agent goals、raw thought、raw chain-of-thought、hidden context、private evaluator data
  或 concrete external-world seed/oracle content 时，拒绝 PASS。
- 当 scorecard critical items 缺失、非 pass、unsupported 或缺少 public evidence 时，拒绝 PASS。
- 对 `llm-backed-full-lifecycle-autonomous`，PASS 前必须有所有 component summaries、
  `scorecard-summary.json` 和无 blocking P1/P2 的 `second-agent-review.md`。
- Missing checker support 或 missing required evidence 必须按 `checker_gap`、`client_evidence`
  或 scenario-specific taxonomy 分类，不得 PASS。

## North Star Check

本 package 让 public evidence 可被机器检查。它不添加 application-specific backend behavior、
concrete worlds、product UI 或 hidden LLM truth。

## Out-of-Scope Follow-ups

- `0.9.11` 拥有 Validation Client evidence handoff contracts。
- `0.9.12` 拥有 live 或 blocked LLM-backed full lifecycle execution evidence。
- 未来 packages 可在真实 result artifacts 暴露更多 public structure 后添加更严格 semantic checks。

# Technical Design

英文镜像：`technical-design.md`。

## Current State

`tools/testing/validate_agent_autonomous_result.py` 当前验证 dashboard scenarios 和 basic
`worldengine-full-lifecycle-autonomous` 的 saved autonomous result directories。它检查 result
metadata、relative artifact paths、operation-log structure、score item PASS status、
scorecard summary、basic public evidence redaction markers，以及 basic full lifecycle scenario
的 `world-lifecycle-summary.json` shape。

`docs/testing/agent-autonomous/result-schema.json` 只枚举当前 basic autonomous scenarios。
LLM-backed scenario docs 和 artifact contract 仍是 `planned / checker-extension-required`。

## Contract Alignment and Invariants

- Checker 保持 saved-result checker。它不得启动服务、mutate product state、call providers 或
  rewrite result artifacts。
- Existing scenarios 保持当前 PASS-only success semantics。
- LLM-backed scenarios 获得 explicit status classification 和更严格的 PASS checks。
- Redaction checks 必须扫描 artifact payloads 和 artifact names/field names，仅允许 documented
  safe exceptions。
- Full lifecycle PASS 必须同时要求 deterministic checker/scorecard PASS 和 clean second-Agent
  review status。

## Proposed Implementation

1. 添加 LLM-backed scenario constants、scenario-specific required artifact maps、allowed
   statuses 和 taxonomy maps。
2. 拆分 status validation：existing scenarios 仍要求 `status=pass`，LLM-backed scenarios 可为
   `pass`、`fail`、`blocked` 或 `not_run`。
3. 为 LLM-backed summary artifacts 添加 JSON loaders：
   - `provider-live-summary.json`
   - `world-creation-summary.json`
   - `world-rule-summary.json`
   - `rule-parameter-summary.json`
   - `event-legality-summary.json`
   - `agent-autonomy-summary.json`
   - `diff-replay-summary.json`
   - `world-lifecycle-summary.json`
   - `redaction-scan.json`
   - `scorecard-summary.json`
4. 添加 scenario-specific validators，用于 PASS-critical fields。Required public signals
   缺失或与 artifact contract 矛盾时，必须拒绝 PASS。
5. 添加 blocked/not-run classification checks：`blocked` 和 `not_run` 需要 non-empty
   `failures` 或 `unverified_items` 并带 scenario taxonomy，且不得被描述为 PASS。
6. 添加 fixture directories，至少覆盖：
   - valid 或 blocked provider live smoke result。
   - valid LLM-backed world creation result。
   - valid rule parameter evolution result。
   - valid rule-compliant event generation result。
   - valid Agent persistent autonomy result。
   - valid full lifecycle result。
   - invalid redaction leak。
   - invalid missing critical artifact。
   - invalid full lifecycle missing second-Agent review。
   - invalid PASS with blocked scorecard item。
7. Implementation evidence 存在后，更新 `result-schema.json` 和 documentation statuses 以反映
   checker support。

## Affected Surfaces

- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/**`
- `docs/testing/agent-autonomous/result-schema.json`
- LLM-backed testing docs 和本 package docs。

## Data Model / Schema Changes

`result.json` 保持 additive。Existing fields 仍为 required。LLM-backed scenarios 增加
non-PASS status values 和 scenario-specific artifact requirements。

Summary artifacts 使用 `llm-backed-artifact-contract.md` 中定义的 fields。PASS 要求 redaction
booleans 和 critical evidence fields 与 scorecard 一致。

## Runtime / Service Design

不修改 runtime 或 service code。Checker 只从 saved result directory 读取文件并输出 validation
errors，刻意与 live provider execution 解耦。

## Compatibility

Existing fixtures 和 `make validate-agent-autonomous-fixtures` 必须继续通过。Existing failures
必须继续失败。New LLM-backed fixtures 不得让 older dashboard result directories 变成 invalid。

## Risks

- Checker rules 过弱会 rubber-stamp 缺失的 LLM-backed evidence。通过 scenario-specific
  PASS-critical checks 和 negative fixtures 覆盖。
- Redaction scanning 过宽可能拒绝安全字段名。Safe exceptions 必须 explicit and tested。
- 允许 `blocked` 和 `not_run` 可能模糊 PASS。Checker 必须保持清晰区分：只有所有 critical
  items 都 pass 的 `pass` 才是 PASS。

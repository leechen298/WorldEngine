# Contract

英文版本：`contract.md`。

## Public Concepts

- `worldengine-full-lifecycle-autonomous`：通过外部客户端表面验证完整
  WorldEngine 生命周期的 autonomous saved-result scenario。
- `world_lifecycle_summary`：redacted artifact，用来证明 world creation、runtime
  progression、Agent autonomy evidence、external direction boundaries 和 evidence
  integrity。
- `api_summary`：与 Agent operation log 分离的 redacted public API evidence。
- `agent_autonomy_evidence`：证明 Agent actions 来自 WorldEngine state/event
  surfaces、不是客户端直接脚本控制的 public evidence。

## Compatibility Constraints

- 现有 autonomous saved-result scenarios 必须继续有效。
- result schema extensions 必须 additive。
- dashboard scenarios 的 checker 行为必须保持兼容。
- direct API calls 必须继续禁止作为 Agent operation-log entries。
- 本场景 API evidence 必须保留在 artifacts 中，而不是 hidden logs。

## Allowed Changes

- `docs/testing/agent-autonomous/README.md`
- `docs/testing/agent-autonomous/scorecard.md`
- `docs/testing/agent-autonomous/result-schema.json`
- `docs/testing/agent-autonomous/scenarios/`
- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/`
- `Makefile`
- `docs/iterations/v0.8/README.md`
- `docs/iterations/v0.8/README.zh.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/CURRENT_STATE.zh.md`
- 本 package 的 review evidence。

## Forbidden Changes

- 不修改 WorldEngine runtime、schemas、API routes、provider code、frontend、
  migrations 或 `backend/worldengine/`。
- 不修改 Validation Client repository。
- 不新增 concrete validation world content、named characters、maps、location seed
  data、story rules 或 app-specific backend logic。
- 不暴露 provider keys、authorization headers、raw requests、raw responses、
  private prompts、private Agent memory、private goals、relationship internals、
  `self_state`、hidden context、private file paths 或 validation oracle internals。
- 不从 fixtures 声称 live WorldEngine PASS、Codex autonomous PASS、human
  validation PASS 或 product readiness。

## North Star Check

本 package 提升 generated worlds、runtime progression 和 Agent-in-world behavior
的 evidence，同时把 application 和 validation 细节留在 core engine 之外。

## Out-of-Scope Follow-ups

- 通过 Validation Client 执行 live autonomous run。
- 第二 Agent evidence review。
- human validation。
- live validation 发现的 runtime repairs。
- 除 scenario stop rules 之外的 provider heartbeat 或 provider-cost governance。

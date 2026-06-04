# Test Plan

英文版本：`test-plan.md`。

## Mode

本 package 使用 focused backend regression 加 saved-result checker verification。
只有在外部 Validation Client 环境可用并实际重跑后，才能声明 full lifecycle
autonomous validation full PASS。

## RED Test

修改 runtime code 前，先更新或新增 focused public handoff API test，使其在当前实现上失败：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_public_handoff_contract_api.py -q
```

预期 RED failure：director guidance `public_explanation` 包含 forbidden public
evidence markers 或 protected private/internal wording。

## Focused Backend Tests

implementation 后运行：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_public_handoff_contract_api.py -q
```

预期：pass。

然后运行相关 0.8.9.1 regression set：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_world_generation_schema.py backend/app/tests/test_public_handoff_contract_api.py backend/app/tests/test_generation_core_readiness_api.py -q
```

预期：pass。

## Full Backend Regression

运行：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests -q
```

预期：pass；如果有无关失败，必须记录 exact evidence 和 scope rationale。

## Saved-Result Checker

先保持 historical failed result 诚实：

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle
```

在新 rerun 前，预期结果：仍以已知 redaction failure 失败。不得改写旧 artifacts 让它通过。

package review 明确记录 `implementation_authorized: yes` 和
`evidence_execution_authorized: yes` 后，并且新的 full lifecycle run 创建 fresh
result directory 后，运行：

```bash
make validate-agent-autonomous-result RESULT_DIR=<new-result-dir>
```

full closeout 预期：pass。

如果没有记录 `evidence_execution_authorized: yes`，不得启动 live full lifecycle
rerun。review 应将 rerun 记录为 not authorized，并把 closeout 限定到 focused repair
evidence。

## Optional Runtime Probe

如果 implementation 已完成且本地服务可启动，运行：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project uvicorn app.main:app --host 127.0.0.1 --port 8000
curl -s -o /tmp/we-director-0.8.9.2.json -w '%{http_code}' -H 'Content-Type: application/json' -d '{"instruction_text":"public world guidance"}' http://127.0.0.1:8000/worlds/world-public/director-guidance
rg -n "api_key|apikey|authorization|credential|hidden_context|private_prompt|provider_secret|raw_request|raw_response|self_state|private memory|private goal|relationship internals|hidden context" /tmp/we-director-0.8.9.2.json
```

预期：HTTP `200`；forbidden-marker scan 无匹配。

## Documentation Checks

运行：

```bash
git diff --check
rg -n "implementation_authorized: yes|Status: implementation complete|Status: review complete|PASS_READY_FOR_HUMAN_VALIDATION|Codex autonomous validation PASS|human validation PASS|external validation PASS" docs/iterations/v0.8/0.8.9.2-director-guidance-public-redaction-repair docs/iterations/v0.8/README.md docs/iterations/v0.8/README.zh.md docs/iterations/v0.8/CURRENT_STATE.md docs/iterations/v0.8/CURRENT_STATE.zh.md
```

documentation stage 预期：除了 `test-plan.md` 或 `review.md` 中引用的 forbidden
search terms，不出现 implementation 或 PASS claims。

## Not Run

documentation-stage package creation 期间，不运行 backend 或 autonomous validation
作为 PASS evidence。runtime implementation 尚未授权。

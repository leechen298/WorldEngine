# Test Plan

状态：documentation-stage evidence plan

## Documentation Gate

```bash
git diff --check
```

预期结果：passed with no output。

```bash
python3 -c '<0.8.0 through 0.8.5 required child docs and mirrors check>'
```

预期结果：`missing_child_docs=0`。

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Evidence execution 前预期结果：parent status `in progress / 0.8.5 ready for review`，
active child `0.8.5-core-working-state-smoke-evidence`，route
`documentation-review-needed`，implementation/evidence execution authorization 均为 `no`。

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

预期结果：documentation drafting 阶段，changed files 限制在 `docs/iterations/v0.8/**` 加
already reviewed `0.8.3` backend/app schema/helper/route/test files。

```bash
python3 -c '<v0.8 markdown whitespace check>'
```

预期结果：无 trailing whitespace，无 tab characters。

## Evidence Execution Authorization

`review.md` 记录 `evidence_execution_authorized: yes` 前，不得运行 evidence matrix。

Documentation review 后，可授权下面的 matrix。每个 command 都必须记录 exact result、
pass/fail count 和 proof boundary。

## Core Backend Focused Matrix

Generation and loader：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_worldspec_schema_smoke.py backend/app/tests/test_worldspec_loader.py backend/app/tests/test_world_cell_schema.py backend/app/tests/test_deterministic_world_generation.py backend/app/tests/test_generation_plan_schema.py backend/app/tests/test_plan_import_schema.py backend/app/tests/test_plan_import_boundary.py backend/app/tests/test_structured_generation_plan_compiler.py backend/app/tests/test_template_catalog.py backend/app/tests/test_world_generation_schema.py backend/app/tests/test_generation_preview_api.py backend/app/tests/test_generation_regeneration_api.py backend/app/tests/test_runtime_context_bridge.py backend/app/tests/test_generation_core_readiness.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Proof boundary：generation、WorldSpec、import、preview、regeneration、runtime-readiness、
runtime-context 和 core-readiness backend/API surfaces。

Runtime, event, archive：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_runtime_step.py backend/app/tests/test_event_schema_compat.py backend/app/tests/test_event_api_compat.py backend/app/tests/test_archive_snapshot_summary.py -q
```

Proof boundary：runtime step、event compatibility 和 process-local archive snapshot/summary
behavior。

Agent, memory, params：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_agent_action_adapter.py backend/app/tests/test_agent_loop_service.py backend/app/tests/test_agent_loop_api.py backend/app/tests/test_agent_perception.py backend/app/tests/test_agent_memory_substrate.py backend/app/tests/test_params_agent.py backend/app/tests/test_dry_run_policy.py backend/app/tests/test_dry_run_validation.py backend/app/tests/test_param_validator.py backend/app/tests/test_world_params.py -q
```

Proof boundary：Agent loop、perception、action adapter、memory context、params-agent、
dry-run 和 params validation behavior。

## v0.7 Handoff Compatibility Matrix

这些 commands 只可用于确认 repository-local public contract 和 checker compatibility。它们不是
external validation PASS。

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py tools/testing/test_validate_readiness_manifest.py tools/testing/test_validate_projection_read_model_contract.py -q
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
```

如果 `backend/.venv/bin/python` 不可用，记录 blocker；不要在未更新 `review.md` 的情况下替换
环境。

## Redaction / Overclaim Guard

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

允许的命中只能位于 forbidden、non-claim、redaction 或 historical handoff contexts。

## Explicit Non-Run Classifications

除非后续 reviewed update 授权 exact commands，本 package 将这些分类为 out of scope：

- external validation suite。
- external app 或 projection app validation。
- product-readiness validation。
- generation-quality validation。

除非 evidence review 明确决定运行 broader product profile，否则这些分类为 skipped with
rationale：

- frontend unit/build。
- browser E2E。
- Agent smoke。
- autonomous saved-result 或 full autonomous runner。

## Artifact Scope

如果创建 result artifact，它必须位于 `docs/testing/results/`，使用 v0.8-specific name，
保持 redacted，并在 final assessment 前列入 `review.md`。Artifact 不得包含 private paths、
screenshots、transcripts、UI selectors、external validator commands、oracle internals、provider
traces、raw prompts、secrets、concrete validation worlds 或 non-redacted external event payloads。

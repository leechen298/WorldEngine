# Review

状态：review complete
implementation_authorized: no
evidence_execution_authorized: yes, limited to exact commands in `test-plan.md`

## Changed Files

预期 documentation files：

- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/README.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/README.zh.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/intent.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/intent.zh.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/contract.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/contract.zh.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/technical-design.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/technical-design.zh.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/test-plan.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/test-plan.zh.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/plan.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/plan.zh.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/review.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/review.zh.md`

Parent route/status files 预期更新为 ready for review。

## Commands Run

```bash
git status --short --branch
```

Result：branch `v0.7...origin/v0.7`；changed/untracked files 限制在 v0.8 iteration
docs，以及已 review 的 `0.8.3` backend/app schema/helper/route/test scope。

```bash
git diff --check
```

Result：passed with no output。

```bash
python3 -c '<0.8.0 through 0.8.5 required child docs and mirrors check>'
```

Result：`missing_child_docs=0`。

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Result：`status_check_failures=0`。

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

Result：`changed_or_untracked=23`，`out_of_scope_changed_or_untracked=0`。

```bash
python3 -c '<v0.8 Markdown whitespace check>'
```

Result：`markdown_files=96`，`trailing_whitespace=0`，`tab_lines=0`。

```bash
rg -n '<old 0.8.5 selected/not-created route/status patterns>' docs/iterations/v0.8/*.md
```

Result：passed with no output。

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_worldspec_schema_smoke.py backend/app/tests/test_worldspec_loader.py backend/app/tests/test_world_cell_schema.py backend/app/tests/test_deterministic_world_generation.py backend/app/tests/test_generation_plan_schema.py backend/app/tests/test_plan_import_schema.py backend/app/tests/test_plan_import_boundary.py backend/app/tests/test_structured_generation_plan_compiler.py backend/app/tests/test_template_catalog.py backend/app/tests/test_world_generation_schema.py backend/app/tests/test_generation_preview_api.py backend/app/tests/test_generation_regeneration_api.py backend/app/tests/test_runtime_context_bridge.py backend/app/tests/test_generation_core_readiness.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Initial sandboxed attempt 在 tests 开始前失败，因为 `uv` 无法访问
`/Users/leechen/.cache/uv`。同一命令随后用已批准的 `uv run` elevated permissions 重跑。

Result：`130 passed, 1 warning in 0.41s`。

Proof boundary：WorldSpec schema/loader、generation plan/import/compiler、template catalog、
deterministic generation、generation schema、preview、regeneration、runtime-context bridge 和
core-readiness backend/API surfaces。

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_runtime_step.py backend/app/tests/test_event_schema_compat.py backend/app/tests/test_event_api_compat.py backend/app/tests/test_archive_snapshot_summary.py -q
```

Initial sandboxed attempt 在 tests 开始前失败，因为 `uv` 无法访问
`/Users/leechen/.cache/uv`。同一命令随后用已批准的 `uv run` elevated permissions 重跑。

Result：`42 passed, 1 warning in 0.43s`。

Proof boundary：runtime step、event schema/API compatibility 和 process-local archive
snapshot/summary behavior。

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_agent_action_adapter.py backend/app/tests/test_agent_loop_service.py backend/app/tests/test_agent_loop_api.py backend/app/tests/test_agent_perception.py backend/app/tests/test_agent_memory_substrate.py backend/app/tests/test_params_agent.py backend/app/tests/test_dry_run_policy.py backend/app/tests/test_dry_run_validation.py backend/app/tests/test_param_validator.py backend/app/tests/test_world_params.py -q
```

Initial sandboxed attempt 在 tests 开始前失败，因为 `uv` 无法访问
`/Users/leechen/.cache/uv`。同一命令随后用已批准的 `uv run` elevated permissions 重跑。

Result：`60 passed, 1 warning in 0.50s`。

Proof boundary：Agent loop/action/perception、memory substrate、params-agent、dry-run、
param validation 和 world params behavior。

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py tools/testing/test_validate_readiness_manifest.py tools/testing/test_validate_projection_read_model_contract.py -q
```

Result：`84 passed in 0.23s`。

Proof boundary：v0.7 public validation report、readiness manifest 和 projection read-model
checker compatibility，仅作为 handoff context。

```bash
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
```

Result：`PASS: validated readiness manifest at docs/contracts/v0.7-readiness-manifest.json`。

Proof boundary：repository-local v0.7 readiness manifest contract 仍是有效 handoff context。

```bash
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
```

Result：`PASS: validated projection read model contract at docs/contracts/projection-read-model-schema.json`。

Proof boundary：repository-local projection read-model contract 仍是有效 handoff context。

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

Result：command returned matches。已 review 的 matches 均位于 forbidden、non-claim、
redaction-check 或 historical handoff contexts，包括 v0.7 historical redaction probes。没有
match 被接受为 current v0.8 PASS、external validation PASS、product-readiness、
private-detail 或 final-readiness claim。

## Test Results

Documentation checks passed。当前 session 中，已授权 backend/core 和 v0.7 handoff
compatibility evidence commands 均 passed。

Skipped 或 out-of-scope classifications：

- frontend unit/build：skipped；本 package 未授权 exact command。
- browser E2E：skipped；本 package 未授权 exact command。
- Agent smoke：skipped；本 package 未授权 exact command。
- autonomous saved-result/full runner：skipped；本 package 未授权 exact command。
- external validation suite：out of scope。
- external app 或 projection app validation：out of scope。
- product-readiness validation：out of scope。
- generation-quality validation：out of scope。

未运行或声明 checker、fixture、migration、generated-artifact、external repository、external
validator/app 或 `backend/worldengine/` implementation tests。

## Subagent / Evaluator Evidence

Read-only documentation/contract evaluator
`019e8892-9805-7870-9f64-1be1ffcff613` 报告 PASS。

Findings：

- P1：none。
- P2：none。
- P3：none。

Authorization recommendation：记录 `evidence_execution_authorized: yes`，仅限
`test-plan.md` 中的 exact commands；保持 `implementation_authorized: no`。

Validation-evidence evaluator
`019e889b-6555-7dc2-b871-e6d5f6bfa63b` 报告 PASS。

Findings：

- P1：none。
- P2：none。
- P3：parent `review.md` 和 `review.zh.md` 中 parent-review wording 陈旧，仍写 review
  complete "through 0.8.3"。Closeout 时已修正该 wording。

Closeout recommendation：将 `0.8.5-core-working-state-smoke-evidence` 标为 review
complete，将 parent route 推进到 `0.8.6-documentation-package-needed`，并保持
`implementation_authorized: no`。

## Compatibility Review

Evaluator review passed。Draft package 只授权后续 evidence execution commands，不授权
implementation changes，并保持 v0.3 到 v0.7 surfaces 以及 reviewed v0.8 packages 的
compatibility。

Evidence commands 已为 in-scope core/backend surfaces 通过。v0.7 contract/checker commands
仅作为 handoff compatibility 通过，不是 external validation PASS。

## Scope Review

当前 scope guard passed。Drafting scope 限制在本 package 和 parent v0.8 status/review
documents，加上 already reviewed earlier v0.8 worktree changes。

Evidence execution 未修改 product/runtime files、`backend/worldengine/`、frontend、
migration、fixture、checker implementation、external repositories 或 external validator/app
code。

## Unresolved Findings

- P1：none。
- P2：none。
- P3：none。

## Final Assessment

Authorized evidence matrix execution 和 validation-evidence review 均已完成。本 package
review complete，可 hand off 到 `0.8.6-v0.8-evidence-and-boundary-audit` document-package
creation。Implementation 仍未授权。

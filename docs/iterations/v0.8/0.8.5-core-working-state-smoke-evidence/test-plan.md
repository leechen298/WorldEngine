# Test Plan

Status: documentation-stage evidence plan

## Documentation Gate

```bash
git diff --check
```

Expected result: passed with no output.

```bash
python3 -c '<0.8.0 through 0.8.5 required child docs and mirrors check>'
```

Expected result: `missing_child_docs=0`.

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Expected result before evidence execution: parent status
`in progress / 0.8.5 ready for review`, active child
`0.8.5-core-working-state-smoke-evidence`, route
`documentation-review-needed`, and implementation/evidence execution
authorization `no`.

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

Expected result: changed files are limited to `docs/iterations/v0.8/**` plus
already reviewed `0.8.3` backend/app schema/helper/route/test files during
documentation drafting.

```bash
python3 -c '<v0.8 markdown whitespace check>'
```

Expected result: no trailing whitespace and no tab characters.

## Evidence Execution Authorization

Do not run the evidence matrix until `review.md` records
`evidence_execution_authorized: yes`.

After documentation review, the authorized matrix may include the commands
below. Each command must be recorded with exact result, pass/fail count, and
proof boundary.

## Core Backend Focused Matrix

Generation and loader:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_worldspec_schema_smoke.py backend/app/tests/test_worldspec_loader.py backend/app/tests/test_world_cell_schema.py backend/app/tests/test_deterministic_world_generation.py backend/app/tests/test_generation_plan_schema.py backend/app/tests/test_plan_import_schema.py backend/app/tests/test_plan_import_boundary.py backend/app/tests/test_structured_generation_plan_compiler.py backend/app/tests/test_template_catalog.py backend/app/tests/test_world_generation_schema.py backend/app/tests/test_generation_preview_api.py backend/app/tests/test_generation_regeneration_api.py backend/app/tests/test_runtime_context_bridge.py backend/app/tests/test_generation_core_readiness.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Proof boundary: generation, WorldSpec, import, preview, regeneration,
runtime-readiness, runtime-context, and core-readiness backend/API surfaces.

Runtime, event, archive:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_runtime_step.py backend/app/tests/test_event_schema_compat.py backend/app/tests/test_event_api_compat.py backend/app/tests/test_archive_snapshot_summary.py -q
```

Proof boundary: runtime step, event compatibility, and process-local archive
snapshot/summary behavior.

Agent, memory, params:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_agent_action_adapter.py backend/app/tests/test_agent_loop_service.py backend/app/tests/test_agent_loop_api.py backend/app/tests/test_agent_perception.py backend/app/tests/test_agent_memory_substrate.py backend/app/tests/test_params_agent.py backend/app/tests/test_dry_run_policy.py backend/app/tests/test_dry_run_validation.py backend/app/tests/test_param_validator.py backend/app/tests/test_world_params.py -q
```

Proof boundary: Agent loop, perception, action adapter, memory context,
params-agent, dry-run, and params validation behavior.

## v0.7 Handoff Compatibility Matrix

These commands may be run only to confirm repository-local public contract and
checker compatibility. They are not external validation PASS.

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py tools/testing/test_validate_readiness_manifest.py tools/testing/test_validate_projection_read_model_contract.py -q
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
```

If `backend/.venv/bin/python` is unavailable, record the blocker and do not
substitute a different environment without updating `review.md`.

## Redaction / Overclaim Guard

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

Allowed matches must be in forbidden, non-claim, redaction, or historical
handoff contexts.

## Explicit Non-Run Classifications

Unless a later reviewed update authorizes exact commands, classify these as
out of scope for this package:

- external validation suite.
- external app or projection app validation.
- product-readiness validation.
- generation-quality validation.

Unless the evidence review explicitly decides to run the broader product
profile, classify these as skipped with rationale:

- frontend unit/build.
- browser E2E.
- Agent smoke.
- autonomous saved-result or full autonomous runner.

## Artifact Scope

If a result artifact is created, it must be under `docs/testing/results/`, use
a v0.8-specific name, be redacted, and be listed in `review.md` before final
assessment. No artifact may include private paths, screenshots, transcripts,
UI selectors, external validator commands, oracle internals, provider traces,
raw prompts, secrets, concrete validation worlds, or non-redacted external
event payloads.

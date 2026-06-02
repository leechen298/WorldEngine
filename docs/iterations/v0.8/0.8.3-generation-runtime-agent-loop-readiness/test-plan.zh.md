# Test Plan

## Documentation Gate

```bash
git diff --check
```

预期结果：无输出。

```bash
python3 -c '<0.8.3 required child docs and mirrors check>'
```

预期结果：`0.8.3-generation-runtime-agent-loop-readiness missing_child_docs=0`。

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

预期结果：`status_check_failures=0`。

```bash
python3 -c '<docs-only changed-file scope guard before implementation>'
```

预期结果：implementation 未授权时，changed files 限制在 `docs/iterations/v0.8/**`。

## Implementation 前的 Red Tests

`implementation_authorized: yes` 后，先添加 failing tests：

- schema test：`worldspec` 和 `preview_request` 必须二选一。
- successful candidate `WorldSpec` probe 的 core test：
  - runtime readiness passed。
  - isolated runtime exactly once advance。
  - default Agent loop intent 是 `noop`。
  - result not applied。
  - app runtime 不被 mutate。
- `POST /world/generation/core-readiness` 的 API test。
- forbidden extra fields 使用既有 422 envelope 的 API validation test。
- invalid preview 或 invalid `WorldSpec` 返回 diagnostics，且不返回 runtime/Agent success
  evidence 的 failure-path test。
- redaction test：返回 evidence 不包含 prompts/provider traces/secrets/private fields。

## Focused Implementation Verification

运行 implementation 命名的 focused tests。预期候选：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_generation_core_readiness.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Adjacent compatibility：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_generation_preview_api.py backend/app/tests/test_generation_regeneration_api.py backend/app/tests/test_runtime_context_bridge.py backend/app/tests/test_agent_loop_service.py backend/app/tests/test_agent_loop_api.py backend/app/tests/test_runtime_step.py -q
```

## Scope and Claim Guards

```bash
python3 -c '<changed-file scope guard for approved code paths>'
```

Implementation 后 allowed paths：

- `docs/iterations/v0.8/**`
- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/tests/test_generation_core_readiness.py`
- `backend/app/tests/test_generation_core_readiness_api.py`

```bash
rg -n 'backend/worldengine|frontend|migrations|provider SDK|api_key|secret|raw_prompt|provider_trace|external validator|UI selector' <changed code files>
```

预期结果：除 explicit rejection tests 或 documentation non-claim text 外，没有 forbidden
implementation hits。

## Broad Regression Trigger

只有当 implementation 修改 named route/helper/schema path 之外的 shared behavior，或 adjacent
focused tests 失败并指向 shared API envelope/runtime behavior risk 时，才运行 broader backend
regression。

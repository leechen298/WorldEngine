# Test Plan

英文原文：`test-plan.md`。

## Documentation Checks

implementation authorization 前运行：

```bash
git status --short --branch
git diff --check
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary')
names = ['README', 'intent', 'contract', 'technical-design', 'test-plan', 'plan', 'review']
missing = [str(root / f'{name}{suffix}') for name in names for suffix in ['.md', '.zh.md'] if not (root / f'{name}{suffix}').exists()]
print('missing_child_docs', len(missing))
if missing:
    print('\n'.join(missing))
    raise SystemExit(1)
PY
```

预期结果：child docs and mirrors 存在；authorization 前没有 runtime files changed。

## Focused Backend Tests

implementation 后运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py -q
```

预期覆盖：

- unconfigured provider 返回 `call_status=not_configured`。
- unsupported provider 返回 public blocked/failure category。
- safe mock provider path 可以不依赖 network access 返回 public success。
- live smoke response 只包含 public/redacted fields。
- 注入的 secret-like env values 不出现在 serialized responses。
- `/manifest` 保持 additive-compatible。
- 如果选择 API implementation，OpenAPI 暴露 provider smoke path。

## Checker / Redaction Tests

如果实现 checker support，运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
```

预期覆盖：

- redacted public fields 的 provider live summary 通过。
- 含 forbidden markers 的 provider live summary 失败。
- provider-live-smoke scenario 不被当成 basic full-lifecycle PASS。

## Regression Tests

code changed 后 implementation closeout 前运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

## Optional Live Provider Smoke

仅当 provider environment 已配置且本 package review 授权 bounded live calls 时运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
WORLDENGINE_LLM_PROVIDER=deepseek .venv/bin/python -m pytest app/tests/test_provider_live_smoke_live.py -q
```

或等价 documented API probe：

```bash
curl -i -X POST http://127.0.0.1:8000/provider/live-smoke
```

如果环境未配置，记录 `not_configured` 或 `blocked`。不要标记 provider live PASS。

## 未运行命令及原因

除非未来 reviewed update 扩大 scope，否则本包不运行 E2E、Agent smoke、autonomous full
lifecycle validation、Validation Client flows、generated-result rewrites 或 LLM-backed world
creation tests。它们不能证明本 provider boundary，并可能过度声明 v0.9 readiness。

## Pass Criteria

Implementation closeout 只有在以下条件满足时才可通过：

- documentation/contract evaluator 报告没有 P0/P1/blocking P2。
- focused backend tests pass。
- `/manifest` compatibility preserved。
- public provider summary redaction tests pass。
- optional live smoke 要么有 current-session evidence 证明通过，要么诚实分类为 not
  configured/blocked。
- review evidence 记录 exact commands、exit status、compatibility review、scope
  review、unresolved findings 和 final handoff。

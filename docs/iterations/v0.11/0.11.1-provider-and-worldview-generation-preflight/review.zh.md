# Review

英文版本：`review.md`。

状态：`implementation complete / focused verification passed`

implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Documentation Stage Review

日期：2026-06-13

本包准备 provider/worldview generation preflight implementation contract。
Evaluator review 通过前，implementation 不授权。

## Changed Files

创建 package docs 和 mirrors：

```text
docs/iterations/v0.11/0.11.1-provider-and-worldview-generation-preflight/
```

Implemented：

```text
backend/app/schemas/provider_preflight.py
backend/app/api/routes/provider.py
backend/app/api/routes/world.py
backend/app/tests/test_provider_worldview_preflight_api.py
```

## Commands Run

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.1-provider-and-worldview-generation-preflight')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.11/0.11.1-provider-and-worldview-generation-preflight docs/iterations/v0.11/CURRENT_STATE.md docs/iterations/v0.11/README.md docs/iterations/v0.11/review.md
```

结果：

- `git diff --check` 通过，无输出。
- package completeness check 返回 `{'missing': [], 'empty': []}`。
- authorization scan 未发现 active yes authorization fields。命中仅为 future
  plan/checklist text。

Implementation verification：

```bash
python3 -m pytest app/tests/test_provider_worldview_preflight_api.py app/tests/test_llm_worldview_generation_api.py app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

首次 focused test run 发现一个 request-validation bug：

- P2 fixed：private-marker worldview preflight input 在构造 nested
  `WorldviewGenerationRequest` 时抛出内部 Pydantic `ValidationError`。现在 preflight
  request schema 会直接拒绝 private markers，使 FastAPI 返回仓库统一的 sanitized 422 response。

最终结果：focused backend tests `37 passed`；`git diff --check` 通过，无输出。

Manual preflight redaction inspection：

```bash
python3 - <<'PY'
from fastapi.testclient import TestClient
from app.api.app_factory import create_app
import os

os.environ['WORLDENGINE_LLM_PROVIDER'] = 'deepseek'
os.environ['WORLDENGINE_LLM_MODEL'] = 'sk-live-secret-model'
os.environ['DEEPSEEK_API_KEY'] = 'sk-live-secret-key'
payload = TestClient(create_app()).post('/provider/worldview-preflight', json={
    'request_id': 'manual-check',
    'worldview_premise': 'A public coastal world'
}).json()
print(payload['preflight_status'])
print(payload['provider'])
print(payload['live_call_authorized'], payload['call_attempted'])
print(payload['worldview']['generation_status'], payload['worldview']['generation_mode'])
print('secret_present', 'sk-live-secret' in str(payload).lower())
PY
```

结果：configured provider 报告为
`provider_ready_blocked_without_live_authorization`；provider model label 为
`redacted`；`live_call_authorized False`；`call_attempted False`；worldview
status/mode 为 `blocked blocked`；`secret_present False`。

## Compatibility Review

计划变更是 additive，并保持现有 provider/live-smoke、worldview generation、session 和
manifest behavior 兼容。

## Scope Review

Live provider calls、provider quality PASS、external Validation Client、world rules、
direction queue、events/diffs、fidelity scoring、durable persistence 和
`backend/worldengine/` 均不在范围内。

## Unresolved Findings

- P1: none recorded yet。
- P2: none recorded yet。
- P3: none recorded yet。

## Final Assessment

PASS。Reviewed scope 内 implementation complete。

## Implementation Closeout Evaluator

只读 evaluator `019ebd64-e8b2-78e3-a7ae-648c96ef17f8`：PASS。

Evidence：

- 无 P1/P2 findings。
- Scope 符合 package contract：additive preflight schema、additive provider route、
  manifest entry 和 focused tests。
- 未发现 live provider call path。Preflight 读取 provider readiness，并调用本地 non-live
  helper；configured providers 在没有 live authorization 时保持 blocked。
- Configured provider 返回
  `provider_ready_blocked_without_live_authorization`、
  `live_call_authorized=False`、`call_attempted=False`、redacted model label，
  且没有 secret leak。
- Manifest 保持 `/provider/live-smoke` 和 `/world/generation/worldview` 为 blocked，
  只把 non-live preflight surface 标记为 pass。
- Private marker request 返回 sanitized `422`；未暴露 raw input key、
  `hidden_context`、`raw_prompt` 或 secret marker。
- Evaluator 重跑 focused backend verification，结果 `37 passed`；`git diff --check`
  通过；`git diff --name-only -- backend/worldengine` 无输出。

Residual note：当前 worktree 有 0.11.1 范围外的 broader campaign dirty/untracked files。
本 PASS 仅适用于 named 0.11.1 files，不得用于关闭 unrelated v0.9/v0.10/v0.12/frontend
changes。

## Documentation / Contract Evaluator

只读 evaluator `019ebd5e-8695-7341-bc9c-a93da93843d7`：PASS。

Evidence：

- 无 P1/P2 findings。
- Package 满足 mixed implementation package gate，英文和中文 docs 均完整。
- Scope 限定为 additive provider/worldview preflight schema/API、manifest discovery、
  redaction-safe summaries、focused backend tests 和 parent route/evidence sync。
- 禁区保持关闭：live provider calls、provider quality PASS、raw prompt/response/
  provider trace/secrets/private data、Validation Client implementation/PASS、world rules、
  direction queue、events/diffs、fidelity scoring、persistence/migrations 和
  `backend/worldengine/`。
- Affected files 和 focused backend test plan coherent。
- `implementation_authorized` 仅可在本 package scope 内设为 `yes`。
  `provider_live_call_authorized` 和 `external_validation_authorized` 必须保持 `no`。

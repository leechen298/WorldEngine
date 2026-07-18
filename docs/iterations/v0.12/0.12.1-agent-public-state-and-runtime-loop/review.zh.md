# Review

英文源文件：`review.md`。

状态：review complete

implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Documentation Stage Review

日期：2026-06-13

本 package 准备 minimal session-scoped public Agent runtime loop 的 reviewed contract。
Documentation evaluator review 通过前，不授权 implementation。

## 变更文件

创建：

```text
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/README.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/README.zh.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/intent.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/intent.zh.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/contract.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/contract.zh.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/technical-design.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/technical-design.zh.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/test-plan.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/test-plan.zh.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/plan.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/plan.zh.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/review.md
docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop/review.zh.md
```

Implementation changed：

```text
backend/app/schemas/session.py
backend/app/core/world_session.py
backend/app/api/routes/session.py
backend/app/api/routes/world.py
backend/app/tests/test_session_agent_runtime_loop_api.py
```

## 已运行命令

Documentation gate：

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop')
files = sorted(pkg.glob('*.md'))
problems = []
for file in files:
    text = file.read_text()
    if text and not text.endswith('\n'):
        problems.append(f'{file}: missing final newline')
    for index, line in enumerate(text.splitlines(), start=1):
        if line.rstrip() != line:
            problems.append(f'{file}:{index}: trailing whitespace')
print({'checked_files': len(files), 'problems': problems})
PY
```

结果：

- `git diff --check` 无输出，通过。
- package completeness check 返回 `{'missing': [], 'empty': []}`。
- authorization scan 未发现 active yes authorization fields。命中项为 future
  review/contract/test-plan text 或 parent historical command examples。
- package whitespace check 返回 `{'checked_files': 14, 'problems': []}`。

Implementation verification：

```bash
python3 -m pytest app/tests/test_session_agent_runtime_loop_api.py -q
python3 -m pytest app/tests/test_session_agent_runtime_loop_api.py app/tests/test_agent_loop_service.py app/tests/test_public_handoff_contract_api.py
git diff --check
python3 active-package whitespace check
python3 session Agent step public evidence probe
```

结果：

- 新 session Agent runtime loop API tests `4 passed`。
- Focused backend verification `16 passed`。
- `git diff --check` 无输出，通过。
- active-package whitespace check 返回 `{'checked_files': 19, 'problems': []}`。
- public evidence probe 返回 `{'state': 'acting', 'public_intent':
  'acknowledge_public_event', 'client_scripted_action': False,
  'event_delta_count': 3, 'redaction_status': 'passed'}`。

## 兼容性审查

Implementation 对现有 session 和 Agent loop surfaces 是 additive。Existing request-driven
`/world/agent/loop/step` 保持兼容，且不作为 session Agent autonomy evidence。Session Agent
step 通过 request schema reject unknown client action payload fields。

## 范围审查

Implementation 保持在 `0.12.1` scope 内。Provider live-call 和 external validation
authorization 仍保持关闭。没有进行 frontend、persistence/migration、Validation Client、
checker automation、narrative/diagnostic、complete MVP closeout 或 `backend/worldengine/`
changes。

## 未解决问题

- P1：暂无。
- P2：暂无。
- P3：暂无。

## 最终评估

PASS。Focused implementation evidence 和 implementation-scope evaluator review 支持
`0.12.1` package closeout。

## Documentation / Contract Evaluator

只读 documentation evaluator `019ebdc7-1c25-7690-842c-727eaad36ce4`：PASS。

Evidence：

- Required package files 和 zh mirrors 均存在且非空。
- Contract、design 和 test plan 足够具体，可以进入 implementation。
- Scope 阻止 client-scripted autonomy、raw/private/provider leakage、frontend、
  persistence/migration、Validation Client、provider live calls 和 `backend/worldengine/`。
- Test plan 覆盖 public Agent state、WorldEngine-owned step selection、
  client-scripted-action rejection、event evidence、redaction 和 manifest compatibility。
- Parent route 与 active `0.12.1` documentation package 一致。

Authorization：implementation 只可在本 package scope 内设置为 `yes`。Provider live-call
和 external validation 仍未授权。

## Implementation-Scope Evaluator

只读 implementation evaluator `019ebdcc-7c07-7ae2-9469-edac4d704613`：PASS。

Evidence：

- Session Agent step request 只接受 `event_limit` 和 `mode_hint`；`intent` 或 `patches`
  等 extra client action fields 会被 reject。
- Session Agent step selection 是 WorldEngine-owned，并从 mode hint 和 public events 推导
  public `resting`、`acting` 或 `waiting` outcomes。
- Public Agent evidence payloads 只包含 public fields，并设置
  `client_scripted_action: False`。
- Default public Agent state 是 session-scoped 且 redaction-safe。
- Existing request-driven `/world/agent/loop/step` 保持兼容，但不作为 session autonomy
  evidence。
- Manifest additions 是 additive，并匹配 focused tests。

Evaluator 重跑 focused backend verification，结果 `16 passed`，并重跑 `git diff --check`
和 public evidence probe；全部通过。

# Review

英文源文件：`review.md`。

状态：review complete

implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 文档阶段评审

日期：2026-06-13

本包准备自然语言方向队列与边界的实现 contract。只有 evaluator review 通过后，才允许实现。

## 变更文件

创建 package 文档和镜像：

```text
docs/iterations/v0.11/0.11.3-natural-language-direction-queue-and-boundary/
```

已实现：

```text
backend/app/schemas/session.py
backend/app/core/world_session.py
backend/app/api/routes/session.py
backend/app/api/routes/world.py
backend/app/tests/test_session_direction_queue_api.py
```

## 已运行命令

文档门禁：

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.3-natural-language-direction-queue-and-boundary')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.11/0.11.3-natural-language-direction-queue-and-boundary docs/iterations/v0.11/CURRENT_STATE.md docs/iterations/v0.11/README.md docs/iterations/v0.11/review.md
```

实现验证：

```bash
python3 -m pytest app/tests/test_session_direction_queue_api.py app/tests/test_world_direction_boundary.py app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

## 测试结果

- `git diff --check` 无输出，通过。
- package 完整性检查返回 `{'missing': [], 'empty': []}`。
- 授权扫描未发现 active yes authorization fields。命中项仅为未来 plan/test/readiness 文本。
- 聚焦后端验证 `48 passed`。
- 实现后 `git diff --check` 无输出，通过。

## 兼容性审查

计划变更是 session API 的 additive 变更，必须保持现有 `/worlds/{world_id}/direction`、session create/run/status、session rule attach/read、event log、snapshot 和 manifest 行为兼容。

## 范围审查

规则合规事件生成、direction 消费、diff 应用、worldview fidelity scoring、live provider 调用、外部 Validation Client、持久化 / 迁移、具体 demo fixture、frontend 变更和 `backend/worldengine/` 仍在范围外。

## Scoped Changed-File Audit

当前 worktree 是累计 MVP campaign worktree，不是隔离的 0.11.3-only worktree。
`git status --short` 包含先前 v0.10 work、v0.11.1 provider/preflight work、
v0.11.2 rules work、parent planning docs、v0.9 handoff docs、v0.12 planning docs、
v0.10 frontend/dashboard work 和 global project docs。

`0.11.3` implementation review evidence 只覆盖：

```text
backend/app/schemas/session.py
backend/app/core/world_session.py
backend/app/api/routes/session.py
backend/app/api/routes/world.py
backend/app/tests/test_session_direction_queue_api.py
docs/iterations/v0.11/0.11.3-natural-language-direction-queue-and-boundary/
docs/iterations/v0.11/CURRENT_STATE.md
docs/iterations/v0.11/CURRENT_STATE.zh.md
docs/iterations/v0.11/README.md
docs/iterations/v0.11/README.zh.md
docs/iterations/v0.11/review.md
docs/iterations/v0.11/review.zh.md
```

Frontend files、provider preflight files、v0.9/v0.10/v0.12 docs、global project
docs 和其他 prior-package files 不作为 `0.11.3` closeout evidence。未执行 staging、
commit 或 push。

## 文档 / Contract Evaluator

只读 evaluator `019ebd82-4017-74a1-8f94-56e2a47d7410`：初次 FAIL。

Finding：

- P2 已修复：package docs 漏掉父计划要求的 accepted/rejected replayable operation evidence 和 client status classification。README、contract、technical design 和 test plan 现在都要求脱敏安全、可 replay 的 session-direction operation records，以及 client-readable queued/rejected classification fields，之后才可授权实现。

复审：PASS。

Evidence：

- 无剩余 P1/P2 findings。
- Package 现在要求 accepted 和 rejected session directions 的可 replay public operation records。
- Package 现在要求 client-readable queued/rejected status 和 classification fields。
- 范围仍限制在 additive session direction queue/read surfaces、public operation evidence、manifest discovery 和 focused backend tests。
- Event generation / diffs 仍属于 `0.11.4`。
- Provider live calls 和外部 Validation Client 仍未授权。

授权：implementation 仅可在本 package scope 内设置为 `yes`。

## Implementation-Scope Evaluator

只读 evaluator `019ebd8b-08f2-79c2-8051-5e1007ecffe1`：初始 closeout readiness
FAIL。

Findings：

- P2 已修复：parent v0.11 route/status 与 0.11.3 implementation state 冲突。Parent
  `CURRENT_STATE`、`README` 和 `review` 现在记录 implementation review pending、
  active-child implementation authorization yes，以及 active-child focused evidence
  execution authorization yes。
- P2 已修复：当前 worktree 并非 0.11.3 scope 隔离状态。本 review 现在记录 scoped
  changed-file audit，并将 frontend、provider、v0.9/v0.10/v0.12、global docs 和
  prior-package files 排除在 0.11.3 closeout evidence 之外。

Evaluator behavior review 没有发现 implemented session-direction path 中的 P1/P2 defect。
它也重跑了 focused verification，结果 `48 passed`，并且 `git diff --check` 无输出。

复审：PASS。

Evidence：

- 无剩余 P1/P2 findings。
- Parent v0.11 routing 现在匹配 implementation-review 和 active-child authorization state。
- Scoped changed-file audit 已足够明确，可作为 0.11.3 closeout evidence。
- Accepted directions 会入队并记录 `world.session_direction.queued`。
- Rejected directions 不入队并记录 `world.session_direction.rejected`。
- 两条路径都保持 `direct_state_mutation_applied: false`。
- Evaluator 重跑 focused verification，结果 `48 passed`；`git diff --check` 无输出。

## 未解决问题

- P1：暂无。
- P2：暂无。
- P3：暂无。

## 最终评估

PASS。已在 reviewed scope 内完成实现。

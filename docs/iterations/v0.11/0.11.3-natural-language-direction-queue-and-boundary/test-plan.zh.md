# 测试计划

英文源文件：`test-plan.md`。

状态：文档已起草 / 等待评审

## 要运行的精确命令

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
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" \
  docs/iterations/v0.11/0.11.3-natural-language-direction-queue-and-boundary \
  docs/iterations/v0.11/CURRENT_STATE.md \
  docs/iterations/v0.11/README.md \
  docs/iterations/v0.11/review.md
```

授权后的实现验证：

```bash
python3 -m pytest app/tests/test_session_direction_queue_api.py app/tests/test_world_direction_boundary.py app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

## 预期结果

- 文档完整性检查不返回 missing 或 empty package files。
- 授权扫描在 review gate 前不发现提前的 implementation/live/external yes。
- 聚焦后端测试通过。
- 被接受的 lightning-risk guidance 返回 queued external pressure 或其他允许的公开类别，且不改变状态。
- “kill this Agent now” 这类直接最终事实 guidance 被拒绝，且不创建 queued item。
- 私有标记被拒绝或脱敏，不公开回显。
- 现有 world-direction endpoint 测试继续通过。
- Manifest / discovery 暴露 session direction endpoints。
- 被接受和被拒绝的 session directions 会创建可 replay 的公开 operation evidence，例如 event-log records，且不回显原始指令。
- Client-readable status/classification fields 能区分 queued、rejected、allowed category、forbidden category 和 `direct_state_mutation_applied: false`。

## 不运行的命令及原因

- 本包未授权 provider live smoke。
- 本包未授权外部 Validation Client 自动化。
- 除非实现改动 dashboard code，否则不计划 frontend E2E。
- Autonomous Agent validation 不属于 v0.11.3 范围。

## 阻塞记录规则

若命令失败，先在本包 contract 范围内修复。只有外部环境、provider 授权、Validation Client/checker 能力或属于其他 package 的范围问题，才记录为 `BLOCKED`。

## 禁止未验证声明

`review.md` 只能记录当前 session 实际运行过的命令。不得从本包声明 provider live、外部验证、E2E、自主 Agent 或完整 MVP PASS。

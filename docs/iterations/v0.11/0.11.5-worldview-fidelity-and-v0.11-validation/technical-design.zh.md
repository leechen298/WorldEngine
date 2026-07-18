# 技术设计

英文源文件：`technical-design.md`。

状态：文档已起草 / 等待评审

## 实现结构

如可用，使用 deterministic public fidelity helpers：

```text
evaluate_immediate_worldview_fidelity(...)
evaluate_bounded_run_worldview_fidelity(...)
build_worldview_fidelity_scorecard(...)
```

Closeout path 以 evidence 优先：

```text
public generation summary + rule summary
  -> immediate fidelity artifact
public runtime/event/diff/snapshot summary
  -> bounded-run fidelity artifact
immediate + bounded-run
  -> v0.11 scorecard
scorecard + child package reviews
  -> v0.11 closeout and v0.12 handoff
```

## 影响文件

允许的实现 / evidence 文件：

- `backend/app/core/worldview_fidelity.py`
- `backend/app/schemas/world_generation.py`
- `backend/app/tests/test_worldview_fidelity_evaluation.py`
- 必要时修改聚焦现有 regression tests

允许的文档 / 状态文件：

- 当前 package 目录。
- `docs/iterations/v0.11/CURRENT_STATE.md`
- `docs/iterations/v0.11/CURRENT_STATE.zh.md`
- `docs/iterations/v0.11/README.md`
- `docs/iterations/v0.11/README.zh.md`
- `docs/iterations/v0.11/v0.11-plan.md`
- `docs/iterations/v0.11/v0.11-plan.zh.md`
- `docs/iterations/v0.11/review.md`
- `docs/iterations/v0.11/review.zh.md`
- closeout 需要时的 v0.12 route handoff docs。

## 兼容策略

- Fidelity helpers 保持 deterministic 和 public。
- Deterministic generic fallback 不足以支持 final fidelity PASS。
- Missing bounded-run evidence 记为 blocked，不记为 pass。
- Redaction failures 记为 fail。
- Provider live、external Validation Client 和 Agent autonomy claims 不进入 v0.11 closeout。

## 防漂移规则

- 不使用 hidden evaluator oracle。
- 不使用 raw provider/prompt evidence。
- 不实现 external validation。
- 不扩大到 v0.12 Agent continuity。

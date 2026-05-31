# 技术设计

状态：final / closeout complete

## 收口模型

Final closeout 有三个阶段：

1. 准备 closeout records，同时 status 保持 `ready for review`；
2. 运行 final verification 和 evaluator review；
3. 只有 gate 通过后，才把 parent 与 roadmap status 同步为
   `final / closeout complete`。

## 最终证据矩阵

| Surface | Required Final Evidence | Claim Boundary |
| --- | --- | --- |
| Documentation and mirrors | required-docs check `missing=0` | v0.6 docs complete |
| Changed-file scope | cumulative scope guard `out_of_scope=0` | only reviewed v0.6 surfaces |
| Backend | full backend regression | reviewed generation/runtime/API backend surfaces |
| Frontend | frontend unit test and build | dashboard generation preview only |
| E2E | `make test-e2e` | focused dashboard/runtime smoke including generation preview |
| Status | status consistency checks | all current surfaces agree |

## 延后范围矩阵

| Surface | Final Closeout Position |
| --- | --- |
| External validation readiness | 延后到 v0.7 |
| Projection readiness | 延后到 v0.8 |
| Product readiness | v0.6 closeout 不声明 |
| Agent smoke/autonomous | 未显式运行则不声明，预期 out of scope |
| Generation quality | 不声明；validity 与 quality 继续分开 |
| Concrete content | core repository 中禁止 |

## 状态同步

如果 final gate 通过，更新：

- v0.6 parent status files 为 `final / closeout complete`；
- `0.6.10` package docs 和 final-closeout record 为 final status；
- 只在不暗示 v0.7/v0.8 完成时，更新 v0.6 roadmap status entries。

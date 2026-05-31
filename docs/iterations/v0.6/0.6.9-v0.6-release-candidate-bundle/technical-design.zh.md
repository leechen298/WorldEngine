# 技术设计

状态：review complete

## 设计

Release-candidate bundle 是 documentation index，不是新的 runtime artifact。它把已评审
evidence 汇总为四个部分：

1. package readiness table；
2. release-candidate claim boundary；
3. unresolved finding classification；
4. final-closeout handoff checklist。

## 包就绪表

| Package | RC 使用的状态 | 包含证据 |
| --- | --- | --- |
| `0.6.0` | review complete | campaign boundary 和 generation scope baseline |
| `0.6.1` | review complete | public generation contracts 和 template semantics |
| `0.6.2` | review complete | deterministic template catalog generator 和 backend tests |
| `0.6.3` | review complete | structured generation plan compiler 和 backend tests |
| `0.6.4` | review complete | AI-assisted boundary 和 plan import tests |
| `0.6.5` | review complete | validation metadata 和 preview API tests |
| `0.6.6` | review complete | regeneration 和 runtime-readiness API tests |
| `0.6.7` | review complete | dashboard preview、frontend unit/build、E2E、browser smoke |
| `0.6.8` | review complete | evidence 和 compatibility audit，含 evaluator PASS |

## 声明边界

| Surface | Release Candidate Position |
| --- | --- |
| Backend generation schemas/core | 作为 reviewed v0.6 implementation evidence 包含。 |
| Preview/regeneration/readiness API | 作为 reviewed API evidence 包含。 |
| Dashboard generation preview | 作为 focused UI/E2E smoke evidence 包含。 |
| Loader/runtime-context readiness | 仅包含 `0.6.6` 已检查的边界。 |
| External validation worlds | 排除；不声明 readiness。 |
| Projection application | 排除；不声明 readiness。 |
| Agent smoke/autonomous runner | 排除；不声明 pass。 |
| Generation quality | 排除；validity 与 quality 仍分开。 |
| Product readiness | 排除；release candidate 不是 whole-product PASS。 |
| Final release | 排除，直到 `0.6.10` 完成。 |

## 交接清单

交接给 `0.6.10` 时应包含：

- release-candidate status 和 checklist result；
- 确认没有 unresolved P1/P2 finding；
- 从已评审 child packages 继承的 exact current-session evidence counts；
- 明确的 not-run/out-of-scope surfaces；
- 在标记 v0.6 final 前，必须运行 `0.6.10` 定义的 final closeout checks。

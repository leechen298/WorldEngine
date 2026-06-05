# Technical Design

英文镜像：`technical-design.md`。

## 设计原则

Repair 必须由 evidence 驱动。Implementation agent 必须先复现或检查失败，再识别哪个
layer 出错。修复必须针对该 layer，且不能削弱 scenario 对用户可见行为的证明。

## 现有 Scenario

已实现的 E2E scenario：

```text
frontend/e2e/dashboard.spec.ts
dashboard-archive-summary creates and renders a newer archive summary
```

期望流程：

1. stepping 前记录 latest summary。
2. 打开 dashboard，并确认 MemoryPanel 可见。
3. runtime step 四次。
4. 通过 API 等待 newer summary。
5. 断言 tick range 和 event stats。
6. 断言 MemoryPanel 渲染 newer summary stats 和 text。

Scenario 文档位于：

```text
docs/testing/e2e-scenarios/dashboard-archive-summary.md
```

## 诊断矩阵

| Bucket | 需要收集的 Evidence | 可能修复 |
| --- | --- | --- |
| `archive_generation_gap` | enough steps 后 API 查不到 newer summary | 修 backend archive interval、event capture 或 summary generation |
| `summary_api_visibility_gap` | summary 内部存在但 latest/list API 不暴露或排序错误 | 修 backend summary list/latest ordering 或 filtering |
| `memory_panel_refresh_gap` | API 有 newer summary，但 MemoryPanel 渲染 old/empty state | 修 frontend refresh 或 state update |
| `e2e_environment_gap` | Playwright server 没有应用 low summary/snapshot intervals | 修 test server environment 或 setup |
| `e2e_wait_or_state_isolation_gap` | app 行为正确，但 predicate 比较了错误 baseline 或 serial state race | 修 focused Playwright helper，并保持断言强度 |
| `other_blocked` | root cause 需要更大 archive redesign 或不可用依赖 | 停止并记录 blocker |

## 必需调查流程

1. 运行 focused failing scenario。
2. 捕获 stepping 前 latest summary。
3. runtime step 四次。
4. stepping 后查询 summaries 和 runtime state。
5. 对比：
   - `beforeSummary` identity 和 tick range。
   - latest API summary identity 和 tick range。
   - total events 和 `tick.advanced` count。
   - MemoryPanel rendered text 和 stats。
6. 在 `review.md` 中记录一个 root-cause bucket。

## 修复策略

除非 evidence 证明多个 layer 都坏了，否则只选择一个 primary repair path：

### Backend Archive Path

只有当 API 在 expected steps 后没有生成 newer valid summary 时使用。

可能工作：

- 确保 E2E environment honor summary interval configuration。
- 确保 runtime steps 产生 summary-eligible archived events。
- 确保新 events 后 summary tick ranges 会推进。
- 为 repaired archive behavior 添加或更新 focused backend tests。

### Frontend MemoryPanel Path

只有当 API evidence 正确但 UI 没有渲染 newer summary 时使用。

可能工作：

- runtime steps 后刷新 latest archive summary。
- 更新 state handling，使 latest summary 替换 stale data。
- 保持稳定 `data-testid` selectors，除非 selector bug 是已证明 root cause。

### E2E Harness Path

只有当 backend 和 UI behavior 正确，但 test predicate 错误、时间不足或没有隔离时使用。

可能工作：

- 使用稳定 summary identity 和 tick coverage 做 baseline comparison。
- poll 正确 API endpoint。
- 如果 prior test 创建的 summary 干扰 ordering，则隔离 serial state。
- 只有 evidence 证明 application behavior 正确且 original timeout 不足时，才可调整 timeout。

## 声明边界

本 package 只可声明：

- focused archive summary E2E repair。
- 如果当前 session 运行并通过，声明 current `make test-e2e` clean pass。
- 如果当前 session 运行并通过，声明 latest basic full lifecycle saved-result checker
  仍可验证。

本 package 不可声明：

- LLM-backed lifecycle capability。
- live provider capability。
- product readiness。
- external validation PASS。
- 超出 repaired scenario 的 archive persistence 或 summary quality。

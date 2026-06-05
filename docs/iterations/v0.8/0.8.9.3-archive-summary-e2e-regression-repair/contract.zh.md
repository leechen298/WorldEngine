# Contract

英文镜像：`contract.md`。

## 公开概念

- `Archive summary`：由 archived runtime events 生成，并由 dashboard MemoryPanel
  渲染的公开 world-history summary。
- `Newer summary`：其 identity 或 tick coverage 晚于 E2E stepping phase 前观察到
  的 summary。
- `MemoryPanel evidence`：稳定的 dashboard text 和 stats，证明 latest archive
  summary 对用户可见。
- `Focused E2E repair`：恢复失败 archive summary scenario 的最小修复，且不削弱
  user-visible assertion。

## 批准后允许变更

Implementation 只能修改以下文件或 surfaces 中最小必要子集：

```text
frontend/e2e/agent-loop.spec.ts
frontend/e2e/dashboard.spec.ts
frontend/playwright.config.ts
frontend/src/**
backend/app/**
backend/app/tests/**
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

`frontend/src/**`、`backend/app/**` 和 `backend/app/tests/**` 是条件授权。只有当
focused diagnosis 证明根因在 frontend behavior、backend archive behavior 或缺少
focused regression coverage 时才可使用。

## 禁止变更

- 不得修改 `backend/worldengine/`。
- 不得修改 Validation Client repository。
- 不得 skip 或删除失败 Playwright test。
- 不得把 scenario 弱化成只检查 dashboard 是否加载。
- 不得移除 runtime steps 后必须创建 newer summary 的要求。
- 不得仅靠延长 timeout 作为修复，除非 diagnostic evidence 证明 application behavior
  正确而 wait condition 过短。
- 不得重写、删除或编辑 saved validation result directories 来让历史 evidence pass。
- 不得加入 live provider calls、DeepSeek smoke、provider abstractions 或 LLM-backed
  world creation/evolution behavior。
- 不得加入 concrete validation-world content 或 app-specific backend logic。
- 不得声明 external validation PASS、product readiness 或 LLM-backed lifecycle readiness。

## 必需诊断分类

选择 implementation changes 前，`review.md` 必须把 root cause 归类到以下之一：

```text
archive_generation_gap
summary_api_visibility_gap
memory_panel_refresh_gap
e2e_environment_gap
e2e_wait_or_state_isolation_gap
other_blocked
```

分类必须引用 focused evidence，例如当前 session 中的 API responses、UI state、
Playwright trace observations 或 backend logs。

## 兼容性要求

- Existing archive summary response shape 必须保持 additive-compatible。
- Existing dashboard MemoryPanel selectors 必须保持稳定，除非 package 记录
  selector-specific reason 并更新 E2E docs。
- Existing runtime step、event、snapshot、params、generation、Agent loop 和 public
  handoff endpoints 必须保持现有行为，除非 root cause 已证明位于直接相邻的 archive
  summary path。
- E2E web server configuration 不得改变 test environment 之外的 backend runtime defaults。
- Repair 不得把 concrete world fixtures 或 external validation scenario data 引入
  WorldEngine core。

## 退出标准

- Documentation/contract review 记录无 P0/P1 且无 blocking P2。
- 代码变更前必须记录 `implementation_authorized: yes`。
- Focused diagnosis 记录一个 root-cause bucket。
- 当前 session focused archive summary E2E scenario 通过。
- 当前 session `make test-e2e` 通过。
- 当前 session 必要 adjacent backend/frontend tests 通过。
- 当前 session latest basic full lifecycle saved-result checker 通过，或记录 exact blocker。
- `git diff --check` 通过。
- `review.md` 和 `review.zh.md` 记录 changed files、commands、results、
  compatibility review、scope review、unresolved findings 和 final assessment。

## 后续但不在本范围

- LLM-backed lifecycle validation execution。
- Provider live smoke endpoint 或 checker support。
- Agent persistent autonomy quality improvements。
- Archive summary quality、retention、compression 或 durable persistence work，除非
  直接属于失败 E2E contract。
- Validation Client evidence exporter 或 UI work。

# 0.8.9.3 Archive Summary E2E Regression Repair

英文镜像：`README.md`。

Status：implementation complete / PASS
implementation_authorized：yes
evidence_execution_authorized：yes，仅限 `test-plan.md` commands
Type：mixed repair package

## 目标

诊断并修复当前 `dashboard-archive-summary` E2E 回归，让 WorldEngine 在进入
LLM-backed lifecycle validation 可执行证据之前，先恢复干净的基础 dashboard E2E
基线。

本 package 的触发原因是：最新一次 current-product validation 证明 basic full
lifecycle saved-result validation 已通过，但 WorldEngine E2E suite 没有 clean pass：

```text
make test-e2e
16 passed / 1 failed
frontend/e2e/dashboard.spec.ts:292
dashboard-archive-summary creates and renders a newer archive summary
```

失败点是在 runtime step 之后等待 newer archive summary 超时。本 package 必须判断
问题到底在 archive summary 生成、summary API 排序/可见性、frontend MemoryPanel
刷新、E2E environment setup，还是 Playwright wait condition。

## 范围

批准后允许：

- 复现 focused failing E2E scenario。
- 检查 runtime steps 前后的 archive summary API state。
- 按证据在 backend archive behavior、frontend MemoryPanel behavior 或 E2E harness
  logic 中修复最小根因。
- 保留“newer archive summary 被创建并渲染”的强断言。
- 重跑 focused 和 broad E2E verification。
- 重跑最新 basic full lifecycle saved-result checker，确认之前 autonomous PASS
  evidence 仍可验证。

禁止：

- 不得 skip、删除或把失败 E2E 弱化成 smoke-only check。
- 不得重写 generated validation result directories。
- 不得修改 Validation Client repository。
- 不得加入 DeepSeek、provider live smoke 或 LLM-backed world generation behavior。
- 不得加入具体 validation-world names、characters、locations、story rules、seed
  data、private oracle logic 或 app-specific backend behavior。
- 不得在 `backend/worldengine/` 下实现新的 runtime features。

## 交付物

- focused diagnosis evidence，明确失败层级。
- review approval 后的窄范围 implementation repair。
- focused E2E 和 `make test-e2e` 的 current-session verification evidence。
- 根据 touched files 需要补充的 backend 或 frontend regression commands evidence。
- 最新 basic full lifecycle autonomous result 的 current-session saved-result checker evidence。
- 完成 `review.md` 和 `review.zh.md`，记录 changed files、commands、findings、
  scope review、compatibility review 和 final assessment。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

已包含中文镜像。

## 当前门禁

2026-06-05 已在 explicit user approval 后完成 documentation/contract review。
本 package scope 内的 implementation 和 verification 已完成。本 package 不再授权
除 `review.md` 已记录的 completed `test-plan.md` commands 之外的 evidence execution。

```text
implementation_authorized: yes
```

## 交接

本 package 已以 clean current-session evidence 关闭。WorldEngine 可以在本 package
scope 内认为基础 dashboard E2E baseline 已修复。LLM-backed lifecycle validation 仍是
独立测试计划，不得由本 package 声明。

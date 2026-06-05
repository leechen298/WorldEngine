# Test Plan

英文镜像：`test-plan.md`。

## 验证顺序

Implementation closeout 时按以下顺序运行 commands，并在 `review.md` 中记录 exact
commands、results 和关键输出。

## 1. Baseline Reproduction

目标：修改 implementation files 前，先证明当前失败或证明它是 intermittent。

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

如果 focused test 意外通过，必须再重跑一次并检查 API/UI state，再决定 package 是否
已经不需要。不得只因为一次 retry 通过就 close package。

## 2. Diagnostic Probe

目标：归类 root cause bucket。

必需 evidence：

- stepping 前的 summary。
- stepping 后的 summary list。
- stepping 后的 runtime state。
- 如果涉及 UI，记录 MemoryPanel rendered summary stats/text。
- 如果 focused test 失败，记录 Playwright artifact path。

具体 command 或 script 可在 implementation 时决定，但不得写 product code，也不得重写
saved validation results。

## 3. Focused Repair Verification

Repair 后运行 focused scenario：

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

PASS 要求 focused scenario 通过，且没有 skip 或削弱 newer-summary assertions。

## 4. Broad E2E Verification

运行 full E2E suite：

```bash
make test-e2e
```

PASS 要求 full suite 在当前 session 通过。

## 5. Adjacent Regression Commands

只运行 touched files 所需的 commands：

- 如果 backend archive/API code 变化：

```bash
uv run pytest backend/app/tests
```

- 如果 frontend source code 变化：

```bash
cd frontend
pnpm test
pnpm build
```

- 如果只有 Playwright test harness 变化：

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts
```

Implementation agent 可以先添加更窄的 focused backend tests，但 closeout 前必须运行
合适的 broader adjacent command。

## 6. Basic Full Lifecycle Saved-Result Checker

确认 latest basic autonomous lifecycle result 仍可验证：

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

这不是新的 live autonomous run。它只用 checker 验证 latest saved result。

## 7. Documentation and Diff Checks

```bash
git diff --check
```

Staging 或 closeout 前还必须检查 `git status --short --branch`。

## PASS 来源

本 package 只有在以下条件满足时才可报告 PASS：

- focused E2E repair verification 通过。
- `make test-e2e` 通过。
- required adjacent regressions 通过，或明确 not applicable。
- saved-result checker 通过，或因 local artifacts 不可用而被记录为 blocked 并说明 exact reason。
- review 记录无 unresolved P1 或 blocking P2。

## FAIL 或 BLOCKED 来源

出现以下情况必须报告 FAIL 或 BLOCKED：

- focused E2E 在 attempted repair 后仍失败。
- `make test-e2e` 仍失败。
- root cause 需要 broader archive redesign。
- repair 需要 Validation Client changes。
- verification 需要重写 saved results。
- 发现 redaction 或 private-evidence leak。

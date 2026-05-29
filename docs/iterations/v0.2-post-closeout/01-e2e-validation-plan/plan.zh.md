# Plan

状态：`planned / ready for review`

## 执行步骤

1. 读取 v0.2 release、evidence、boundary 和 compatibility docs。
2. 确认 v0.2 closeout 仍为 final / complete，且本 validation 不重新打开 implementation。
3. 定义 repository 和 documentation checks。
4. 定义 backend deterministic checks。
5. 定义 schema smoke 和 event compatibility checks。
6. 定义 runtime step、world events、event steps、params 和 archive checks。
7. 定义使用 TestClient 或 curl 的 API smoke strategy。
8. 定义 E2E framework availability discovery。
9. 定义 browser E2E 不可用时的 fallback。
10. 定义 release claim validation。
11. 定义 concrete demo-world regression check。
12. 用 documentation-only evidence 更新 review。

## 阶段边界

- 本 package 在 planning 后停止。
- `02-e2e-validation-execution/` 负责 command execution 和 results。

## 停止条件

如果 plan 出现以下问题，停止并在 review 中记录 P2：

- 硬编码 current branch。
- 把 Playwright config 当成 E2E runnable 的证据。
- 声明 validation results。
- 改变 implementation scope。

## Review 更新步骤

review 必须列出 changed files、commands run、commands not run、scope review、
compatibility review、unresolved P1/P2/P3 和 final assessment。

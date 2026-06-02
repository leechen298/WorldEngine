# Contract

## Final Closeout Inputs

- `0.7.0` 到 `0.7.7` 的所有 v0.7 child package reviews。
- `0.7.5` evidence matrix。
- `0.7.6` audit report。
- `0.7.7` release-candidate summary。
- current final verification commands。
- current changed-file scope。

## 允许变更

- 创建或更新
  `docs/iterations/v0.7/0.7.8-v0.7-final-closeout/` 下的文件。
- Final evaluator approval 后更新 parent v0.7 README、current state、campaign plan、goal runner、
  version plan 和 review status。

## 禁止变更

- 不修改 implementation files。
- 不把未运行 surfaces 标记为 passed。
- 不启动 v0.8 或创建 v0.8 package docs。
- 不移除 explicit exclusions。

## Required Final Claims

Final closeout 可以声明：

- v0.7 public contract/readiness documentation、schemas、checkers、manifest、projection read-model
  contract、evidence matrix、audit 和 release-candidate package 已 review complete。
- in-scope checker/schema verification 在 current session passed。
- changed-file scope 留在 approved v0.7 surfaces 内。

Final closeout 不得声明：

- external suite PASS。
- projection application readiness。
- product readiness。
- runtime/API/frontend/E2E/live Agent/full autonomous/generation-quality PASS。
- v0.8 readiness。

## Closeout Gate

只有 final commands pass、final evaluator checks pass 且无 unresolved P1/P2 时，才允许 closeout。

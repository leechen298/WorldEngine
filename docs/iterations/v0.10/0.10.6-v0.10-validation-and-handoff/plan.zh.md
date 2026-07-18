# Plan

英文版本：`plan.md`。

1. 创建完整 package docs 和中文镜像。
2. 运行文档完整性检查和 whitespace checks。
3. 请求只读 evaluator review。
4. 如果 PASS，仅为 validation commands 记录 `implementation_authorized: yes` 和
   `evidence_execution_authorized: yes`。
5. 运行后端、前端、E2E、manifest 和 whitespace validation commands。
6. 记录 `PASS`、`PARTIAL`、`BLOCKED` 或 `FAIL` evidence。
7. 请求 closeout evaluator review。
8. 同步 v0.10 parent closeout 和 v0.11 handoff route。

如果 validation 暴露 in-scope P1/P2 defect，则停止。不要在本包实现 v0.11 或 v0.12 work。

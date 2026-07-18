# 计划

英文源文件：`plan.md`。

状态：文档已起草 / 等待评审

## 顺序执行步骤

1. 读取 v0.11 route、父计划、所有先前 v0.11 child reviews、fidelity helpers 和 fidelity tests。
2. 起草完整 package 文档集和中文镜像。
3. 运行文档门禁命令。
4. 请求只读文档 / contract evaluator。
5. 在 package scope 内修复任何 P1/P2 findings。
6. 若 evaluator 通过，在 `review.md` 写入 `implementation_authorized: yes`；provider live 和 external validation 保持 `no`。
7. 运行聚焦 fidelity 和 v0.11 regression verification。
8. 记录 scorecard evidence 和 v0.11 closeout result。
9. 请求 implementation/evidence evaluator checkpoint。
10. 在 package scope 内修复任何 P1/P2 findings。
11. 更新 package review、父级 v0.11 closeout docs，并交接到 v0.12。

## 阶段边界

- 文档阶段只有在 evaluator 批准后结束。
- Evidence execution 只有在 `review.md` 记录 `implementation_authorized: yes` 后开始。
- v0.11 closeout 只有在聚焦验证和 evaluator checkpoint 后开始。

## 停止条件

如果工作会导致以下情况，必须在 evidence execution 或 closeout 前停止：

- 使用 private/raw evaluator/provider/prompt data。
- 声明 provider live、外部 Validation Client、Agent autonomy 或 complete MVP PASS。
- 实现本包未授权的新 runtime feature scope。
- 修改 frontend、persistence、migrations、concrete fixtures 或 `backend/worldengine`。
- 声称未运行的测试或验证已经通过。

## Review 更新步骤

`review.md` 必须记录 changed files、精确命令、测试结果、scorecard evidence、兼容性审查、范围审查、evaluator checkpoints、未解决 findings、最终 v0.11 assessment 和 v0.12 handoff。

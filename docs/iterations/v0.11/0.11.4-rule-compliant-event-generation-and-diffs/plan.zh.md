# 计划

英文源文件：`plan.md`。

状态：文档已起草 / 等待评审

## 顺序执行步骤

1. 读取 v0.11 route、父计划、迭代规则、现有 rule/session/direction/evolution APIs 和当前 evolution tests。
2. 起草完整 package 文档集和中文镜像。
3. 运行文档门禁命令。
4. 请求只读文档 / contract evaluator。
5. 在 package scope 内修复任何 P1/P2 findings。
6. 若 evaluator 通过，在 `review.md` 写入 `implementation_authorized: yes`；provider live 和 external validation 保持 `no`。
7. 只实现已批准的 additive session evolution scope。
8. 运行 `test-plan.md` 中的聚焦后端验证。
9. 请求 implementation-scope 和 code-review/evidence evaluator checkpoints。
10. 在 package scope 内修复任何 P1/P2 findings。
11. 更新 package review、父级 v0.11 route/status 文档，并交接给 `0.11.5`。

## 阶段边界

- 文档阶段只有在 evaluator 批准后结束。
- 实现阶段只有在 `review.md` 记录 `implementation_authorized: yes` 后开始。
- Closeout 只有在聚焦验证和 evaluator checkpoints 后开始。

## 停止条件

如果工作会导致以下情况，必须在实现或 closeout 前停止：

- 未经 active package 授权就实现。
- 绕过 public legality evaluation。
- 应用 rejected/blocked candidates。
- 修改 Agent private state 或直接最终事实。
- 引入 provider calls、frontend changes、persistence、migrations、Validation Client code、具体 demo fixtures 或 `backend/worldengine`。
- 声称未运行的测试或验证已经通过。

## Review 更新步骤

`review.md` 必须记录 changed files、精确命令、测试结果、兼容性审查、范围审查、evaluator checkpoints、未解决 findings 和最终评估。

# 计划

英文源文件：`plan.md`。

状态：文档已起草 / 等待评审

## 顺序执行步骤

1. 读取 v0.11 route、父计划、迭代规则、现有 session API、现有 world-direction 分类器和测试。
2. 起草完整 package 文档集和中文镜像。
3. 运行文档门禁命令。
4. 请求只读文档 / contract evaluator。
5. 在 package 范围内修复任何 P1/P2 问题。
6. 若 evaluator 通过，在 `review.md` 写入 `implementation_authorized: yes`；provider live 和 external validation 保持 `no`。
7. 只实现已批准的 additive session direction queue 范围。
8. 运行 `test-plan.md` 中的聚焦后端验证。
9. 请求 implementation-scope 和 code-review/evidence evaluator checkpoint。
10. 在 package 范围内修复任何 P1/P2 问题。
11. 更新 package review、父级 v0.11 route/status 文档，并交接到 `0.11.4`。

## 阶段边界

- 文档阶段只有在 evaluator 批准后结束。
- 实现阶段只有在 `review.md` 记录 `implementation_authorized: yes` 后开始。
- Closeout 只有在聚焦验证和必需 evaluator checkpoint 后开始。

## 停止条件

如果工作会导致以下情况，必须在实现或 closeout 前停止：

- 未经 active package 授权就实现。
- 修改事件生成、diff 应用、provider 调用、Validation Client、持久化、迁移、frontend 或 `backend/worldengine/`。
- 让自然语言直接施加最终事实。
- 暴露原始指令文本、私有标记、secret、隐藏上下文、原始 prompt、原始 response 或 provider trace。
- 声称未运行的测试或验证已经通过。

## Review 更新步骤

`review.md` 必须记录 changed files、精确命令、测试结果、兼容性审查、范围审查、evaluator checkpoint、未解决 findings 和最终评估。

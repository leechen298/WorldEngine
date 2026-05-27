# Plan

## 文件

- 新建：
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/intent.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/intent.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/contract.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/contract.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/technical-design.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/technical-design.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/test-plan.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/test-plan.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/plan.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/plan.zh.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.md`
  - `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.zh.md`
- 文档阶段修改：
  - `docs/iterations/v0.3/README.md`
  - `docs/iterations/v0.3/README.zh.md`
  - `docs/iterations/v0.3/v0.3-plan.md`
  - `docs/iterations/v0.3/v0.3-plan.zh.md`
- 仅在收口评审批准后修改：
  - `docs/releases/v0.3.md`
  - `docs/releases/v0.3.zh.md`
  - `docs/iterations/v0.3/findings.md`，仅在问题状态变化时。
- 不触碰：
  - 运行时、schema、API、前端、fixture、migration 或测试实现文件。
  - `backend/worldengine/`。
  - 外部仓库内容。

## 步骤

1. 阅读仓库指南、v0.3 里程碑文档、0.3.7 发布候选证据、问题清单、模板和之前
   的收口示例。
2. 创建 0.3.8 镜像包文档。
3. 在包 README 和 v0.3 里程碑索引中将 0.3.8 标记为 `ready for review`；
   同步 v0.3 计划文档，避免状态漂移。
4. 运行 `test-plan.md` 中的文档阶段验证。
5. 在 `review.md` 和 `review.zh.md` 中记录当前会话证据。
6. 等待人工 / ChatGPT 评审批准，再应用最终收口发布措辞或 review-complete
   状态。

## 验证

文档阶段验证仅限文档检查：

- `git diff --check`
- 镜像包文件存在性检查。
- 针对包 README、里程碑索引和计划文档的状态一致性 grep。
- 收口门禁措辞 grep。
- 未解决 P1/P2 阻塞项检查。
- 具体演示锚点扫描。
- 变更文件范围检查。
- 行尾空白 grep。

运行时、后端、前端、schema 执行、fixture、migration 和测试实现检查不属于
文档阶段，除非最终评审者后续要求新的证据。

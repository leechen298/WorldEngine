# v0.2 开发工作流

英文版本：`development-workflow.md`

## 角色模型

- Human + ChatGPT：定义 version 和 package intent，批准各阶段闸口，并执行
  holistic review。
- Codex A：准备 package docs，自审和补强文档，审核 implementation diff，
  并检查 evidence。
- Codex B：实现已批准的 package，并修复 review findings。

## 产物流转

0. Human + ChatGPT 讨论 version / package plan。
1. 将计划保存为 `docs/iterations/<version>/00-chatgpt-plan.md`。
2. Codex A 生成 package docs。
3. Codex A 自审并补强 package docs。
4. Human approval 或 script gate 允许实现。
5. Codex B 基于 approved package 实现。
6. 运行 local tests。
7. Codex A 审核 Codex B diff。
8. Codex B 修复。
9. 默认最多重复第 6 到第 8 步 `N = 3` 轮。
10. 生成 `final-review-bundle.md`。
11. ChatGPT 执行 holistic review。

## 状态机

```text
planned
  -> docs drafted
  -> ready for human / ChatGPT review
  -> approved for implementation
  -> implementation in progress
  -> tests/evidence complete
  -> diff review
  -> fix loop if needed
  -> final review bundle ready
  -> holistic review approved
```

documentation-only package 可以停在 `ready for human / ChatGPT review`，也可以按
contract 要求进入更后面的文档 review 状态。它们不得静默变成 code package。

## 闸口

- 批准闸：package docs 必须先 review，再进入 implementation。
- 实现闸：implementation 必须只遵循已批准的 package。
- 测试闸：必须运行 `test-plan.md` 中的命令；documentation-only package 跳过测试时必须说明原因。
- Diff 审核闸：changed files 和 behavior 必须符合 package contract。
- 最终审核闸：release-candidate 或 closeout work 必须等待 holistic review。

## 严重级别

- P1：阻塞 correctness、compatibility、scope 或 evidence 的问题。
- P2：package 可以视为 ready 前必须修复的问题。
- P3：不阻塞的 polish、clarity 或 follow-up。

## 证据规则

- 除非当前 session 已验证，不得声称 tests、builds、runtime behavior、E2E、
  UI smoke 或 backend behavior 通过。
- 每个 code 或 mixed package 都必须在 `review.md` 中记录 changed files、
  commands run、test results、compatibility review、scope review、
  unresolved findings 和 final assessment。
- documentation-only package 只有在明确说明原因时，才可以跳过 code tests。

## 范围规则

- 不得超出 active package scope。
- core repository 中不得加入 concrete demo worlds。
- External fixture 和 validation worlds 只能作为 consumers。
- Future-version work 不得在当前 package 内实现。
- `backend/app/` 是 active backend code path。
- `frontend/` 是 active dashboard code path。
- `backend/worldengine/` 仍是 legacy，除非 later approved iteration contract
  另有说明。

## 默认修复循环

默认最大循环次数：`N = 3`。

如果三轮 review/fix 后仍有 P1/P2 findings，停止并请求 human / ChatGPT review，
不要扩大 scope。

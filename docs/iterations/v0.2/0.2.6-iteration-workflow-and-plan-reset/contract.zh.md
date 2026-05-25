# 契约

英文版本：`contract.md`

## 公共概念

- 迭代工作流与计划重排：在 final release work 前，明确规划 v0.2 从 0.2.6
  到 0.2.12 的 package sequence。
- 准迭代包规格：0.2.7 到 0.2.12 的每个 planned package 都必须写到足够详细，
  让后续 agent 能生成完整 package docs，而不需要发明 scope。
- 自动迭代工作流：ChatGPT / Codex A / Codex B 流程，包含 approval、
  implementation、test、review 和 fix gates。
- final-review-bundle template：holistic human / ChatGPT review 前需要生成的
  review artifact。
- 历史抽象化：抽象化 historical concrete fixture details，同时保留 superseded
  concrete fixture work 曾经发生过的历史事实。

## 兼容性约束

- Existing runtime behavior 必须保持不变。
- Existing API response shapes 必须保持不变。
- Existing schema behavior 必须保持不变。
- Existing frontend behavior 必须保持不变。
- Existing tests 和 fixtures 必须保持不变。
- 完成本 package 后，v0.2 仍保持 `planned / in progress`。

## 允许变更

- 更新 `docs/iterations/v0.2/README.md` 和 `README.zh.md`。
- 更新 `docs/iterations/v0.2/v0.2-plan.md` 和 `v0.2-plan.zh.md`。
- 仅围绕 v0.2 和 0.2.6 到 0.2.12 planning 更新 `docs/roadmap.md` 和
  `docs/roadmap.zh.md`。
- 将 `docs/releases/v0.2.md` 和 `docs/releases/v0.2.zh.md` 保持为 draft /
  planned / not released documents。
- 增加本 package directory 及其英文 / 中文文档。
- 增加 `docs/iterations/v0.2/00-chatgpt-plan.md` 和
  `docs/iterations/v0.2/00-chatgpt-plan.zh.md`。
- 增加 `docs/iterations/v0.2/development-workflow.md` 和
  `docs/iterations/v0.2/development-workflow.zh.md`。
- 增加 `docs/iterations/v0.2/final-review-bundle-template.md` 和
  `docs/iterations/v0.2/final-review-bundle-template.zh.md`。
- 抽象化 `docs/iterations/v0.2/**` 和 v0.2 release docs 中的 historical
  concrete demo details。

## 禁止变更

- 不修改 runtime code。
- 不修改 schema code。
- 不修改 API code。
- 不修改 frontend code。
- 不修改 backend tests。
- 不修改 fixtures。
- 不创建 0.2.7 到 0.2.12 的 package directories。
- 不创建 external repositories。
- 不实现 loader、runtime bridge、agent loop、memory、self-continuity、
  generation、projection API、product UI 或 application-specific backend behavior。
- 不把 concrete demo names、fixture filenames、locations、roles、resources、
  buildings、plot anchors 或 concrete grep term list 写入 tracked docs。
- 不把 v0.2 标记为 final release。

## 详细计划验收闸

最终输出前，必须确认 `docs/iterations/v0.2/v0.2-plan.md` 和
`docs/iterations/v0.2/v0.2-plan.zh.md` 对 0.2.7 到 0.2.12 的每个 package
都包含完整的准迭代包规格。

如果任一 package 缺少以下字段之一，必须记录为 P2 finding，并且不能声称
plan is ready：

- Package name / 包名
- Status / 状态
- Type / 类型
- Goal / 目标
- Why this exists / 存在原因
- Inputs / required reading / 输入与必读文件
- Allowed changes / 允许变更
- Forbidden changes / 禁止变更
- Expected deliverables / 预期交付
- Expected tests / verification / 预期测试与验证
- Compatibility constraints / 兼容性约束
- Scope guardrails / 范围护栏
- Exit criteria / 退出条件
- Handoff to next package / 交接给下一包

`README.md` 和 `README.zh.md` 可以只保持 summary-level，但 `v0.2-plan.md` 和
`v0.2-plan.zh.md` 必须足够详细，让后续 Codex planning pass 能生成 next package，
而不需要发明 scope。

## 北极星检查

本 package 不会把 WorldEngine 缩窄成 demo-specific backend。它会消除 ambiguity，
避免 future automation 把 historical concrete fixture direction 当成 active scope。

## 范围外 follow-ups

- 0.2.7：recursive schema contract hardening。
- 0.2.8：event reference contract hardening。
- 0.2.9：evidence and boundary audit。
- 0.2.10：legacy compatibility review。
- 0.2.11：release candidate bundle。
- 0.2.12：approval 后执行 final closeout。

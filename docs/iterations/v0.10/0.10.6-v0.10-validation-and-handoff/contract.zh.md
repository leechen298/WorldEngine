# 契约

英文版本：`contract.md`。

## 公开概念

- **可运行会话 MVP 切片**：v0.10 已评审范围内的公开能力，用户可以从 worldview input
  创建 public session，运行 bounded ticks，检查 timeline/snapshot evidence，并使用 dashboard
  controls。
- **关闭结论**：只能是 `PASS`、`PARTIAL`、`BLOCKED` 或 `FAIL`，并且必须由当前会话证据支撑。
- **交接给 v0.11**：通过文档状态让 v0.11 从 runnable session slice 开始 rule-bound world
  evolution；这不是 v0.11 implementation。

## 允许变更

- 运行并记录 `test-plan.md` 中列出的 validation commands。
- 检查 public manifest/discovery output。
- 更新本 package 的 review，以及 v0.10 parent closeout/handoff docs。
- 只通过 status/handoff docs 将 v0.11 标记为下一个 campaign route。
- 仅当 validation 暴露 in-scope P1/P2 defect，且修复仍位于 reviewed v0.10 contract 内时，
  才记录 narrowly scoped defect repair。

## 禁止变更

- 不新增 runtime、API、schema、frontend、provider、checker、fixture、Validation Client、
  persistence、migration 或 `backend/worldengine/` implementation，除非先记录 reviewed P1/P2
  defect repair。
- 不发起 live provider calls。
- 不执行 external Validation Client，也不声明 automated PASS。
- 不实现 v0.11 或 v0.12 features。
- 不声明 Agent autonomy。

## 兼容性要求

- 现有 v0.10 public API 和 dashboard behavior 必须与 0.10.1 到 0.10.5 记录的证据保持兼容。
- 现有 backend 和 frontend tests 是各自 reviewed scope 的权威证据。
- v0.10 closeout 不得把 replay/worldline branches 改写成 parent/source world semantics。

## 后续范围外事项

- Rule-bound world evolution 属于 v0.11。
- Agent continuity 和 pseudo-self formation 属于 v0.12。
- External Validation Client automation 仍在 WorldEngine 之外。
- Provider-backed quality validation 需要后续 provider/live evidence gate。

## 验证契约

运行并记录 current-session evidence：

- focused backend session/public handoff/bounded runtime tests。
- frontend unit tests。
- frontend build。
- targeted dashboard E2E。
- public manifest/discovery inspection。
- `git diff --check`。

如果命令因 environment/sandbox/server limitations 无法运行，记录精确失败；除非 approved rerun
解决，否则分类为 PARTIAL 或 BLOCKED。

## 关闭契约

本包必须产出以下之一：

- `PASS`：v0.10 runnable session MVP slice 在 reviewed scope 内有证据支持。
- `PARTIAL`：core slice works，但缺少 non-core 或 environment-limited evidence item。
- `BLOCKED`：external environment/permission/tool/provider limitation 阻止 required evidence。
- `FAIL`：in-scope evidence 已运行并发现 unresolved defect。

## 交接契约

如果 v0.10 以 PASS 或 acceptable PARTIAL 关闭，v0.11 可以从 runnable session 开始增加
rule-bound world evolution。Agent continuity 仍属于 v0.12 scope。

## 禁止声明

不得声明：

- live provider quality PASS。
- external Validation Client automated PASS。
- Agent autonomy。
- durable persistence。
- v0.11 rule evolution implemented。
- v0.12 Agent continuity implemented。

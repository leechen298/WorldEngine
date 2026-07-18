# 0.12.3 叙事与诊断检查界面

英文原文：`README.md`。

状态：review complete
类型：混合实现包
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

为 session/world 行为和公开 Agent 证据增加轻量、只读的叙事与诊断检查界面。

这个包要让人类或验证器能用可读投影理解发生了什么，同时不改变 canonical world state、timeline events 或 Agent memory。它基于早期 world-level projection boundary，并把它扩展到 v0.12 所需的 session、tick range、branch 和 Agent-focused inspection。

## 范围

评审通过后允许：

- 增加 session-scoped narrative projection 和 diagnostic inspection schema。
- 增加 session ID、tick range、branch ID、Agent focus 和 bounded public source refs 请求字段。
- 在现有 WorldEngine 路由边界下增加只读 API surface 或 artifact。
- 复用或扩展现有 `external_projection` boundary helper。
- 为新 inspection surface 增加 manifest/public-surface discovery。
- 增加聚焦后端测试，覆盖 session/tick-range/branch/Agent-focused query、public evidence provenance、redaction、read-only behavior 和 compatibility。

禁止：

- 不允许叙事投影改变 canonical world state。
- 不允许 diagnostic conversation 写入 world timeline 或 Agent memory。
- 不允许 raw thought、chain-of-thought、private memory、private goals、hidden context、provider traces、raw prompts、raw provider responses、secrets 或 private evaluator data 出现在请求、响应、事件、测试或证据里。
- 不做 gameplay dialogue、具体 demo content、player records、frontend、persistence/migration、provider live call、外部 Validation Client、checker automation 或完整 MVP closeout。
- 不在 `backend/worldengine/` 下实现。

## 交付物

- 支持 session/tick-range/branch/Agent-focused 的 narrative projection API/artifact。
- out-of-world diagnostic inspection summary API/artifact。
- 标识 public evidence 输入的 provenance 和 redaction 字段。
- 聚焦后端测试和 review evidence。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## 状态清单

- [x] 文档已起草
- [x] Contract 已评审
- [x] Technical design 已评审
- [x] Test plan 已评审
- [x] Implementation 已授权
- [x] Implementation 已完成
- [x] Tests 已完成
- [x] Review 已完成

## 当前判断

Implementation-scope evaluator review 在 P2 修复后通过。本包在 scoped read-only session narrative 和 diagnostic inspection surfaces 范围内已完成。

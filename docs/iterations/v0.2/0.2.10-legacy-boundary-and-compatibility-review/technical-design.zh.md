# Technical Design

英文版本：`technical-design.md`

## 当前状态

Active implementation map 将 v0.1 描述为 runtime scaffold，包含：

- `backend/app/` 下的 active FastAPI backend。
- `frontend/` 下的 active Vue dashboard。
- in-memory runtime state、event log、snapshots 和 summaries。
- params validation、dry-run validation 和 params-agent proposal flow。
- 未接入 active app 的 legacy `backend/worldengine/` code。

v0.2 通过已完成的 packages 增加了 recursive schema 和 event reference
foundations，但这些 contracts 不是 runtime loading behavior。v0.3 是第一个计划
把 generic WorldSpec data bridge 到 runtime context 的 milestone。

## Contract 对齐和不变量

- 将 `docs/current-implementation.md`、`docs/backend-implementation.md`、
  `docs/architecture.md`、package reviews 和当前 route/schema docs 视为
  documentation evidence，而不是修改 implementation 的许可。
- 将 `backend/app/` app wiring 视为 active，将 `backend/worldengine/` 视为
  legacy，除非后续 reviewed contract 另有说明。
- 将 v0.2 schema/event contracts 视为 additive foundations。
- 区分 documented baseline 和 current-session verified behavior。
- 所有 examples 保持 domain-neutral。
- 不编辑 code、tests、schemas、fixtures、migrations、API routes 或 frontend
  files。

## 拟议实现

文档评审通过后：

1. 阅读 current implementation、backend implementation、architecture、API、
   scope、roadmap、evidence、boundary 和已完成的 v0.2 package review docs。
2. 用只读命令检查 active 和 legacy path names，确认文档引用。
3. 创建 `docs/legacy-boundary.md` / `.zh.md`，覆盖 active path、legacy path、
   placeholder infrastructure、documentation 和 future migration rules。
4. 创建 `docs/iterations/v0.2/compatibility-review.md` / `.zh.md`，包含 runtime、
   API、frontend、schema/event contracts、legacy paths 和 v0.3 handoff
   constraints 的 compatibility matrix。
5. 更新 `findings.md`，记录 unresolved compatibility evidence gaps、ambiguous
   boundaries 或 status drift。
6. 运行 `test-plan.md` 中的 documentation checks。
7. 更新本 package 的 review files，记录 exact commands、results、compatibility
   review、scope review、assumptions 和 unresolved findings。

## 受影响表面

Documentation:

- `docs/legacy-boundary.md`
- `docs/legacy-boundary.zh.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/compatibility-review.zh.md`
- `docs/iterations/v0.2/findings.md`
- `docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/**`
- v0.2 milestone index 和 plan status fields。

不影响 runtime、schema、API、frontend、fixture、migration 或 test implementation
surface。

## Data Model / Schema Changes

无。

## Runtime / Service Design

无。

## 兼容性

Runtime behavior、schema validation、event behavior、API response shapes、
frontend behavior、fixture behavior、migration behavior 和 legacy
`backend/worldengine/` behavior 均保持不变。

Compatibility review 可以识别 missing evidence 或 future bridge risks，但不能
通过改变 implementation behavior 来关闭这些缺口。

## 假设

- Current implementation documentation 是 v0.1 behavior 的正确 baseline，除非
  current-session verification 证明存在 drift。
- Compatibility review 可以使用 documentation evidence，但必须准确标记证据来源；
  不需要重新运行 backend/frontend tests。
- 当前 repository 环境中可用的 shell 命令足以执行 link/path checks。
- 除非 implementation files 发生变化，否则不需要 backend/frontend tests；本
  package 明确禁止此类变化。

## 风险

- 风险：compatibility language 暗示 v0.2 schemas 已经被 runtime 加载。缓解：
  所有 runtime 相关表述必须区分当前 v0.1 behavior 与未来 v0.3 bridge work。
- 风险：legacy code inspection 变成 refactor work。缓解：只记录 boundaries 和
  findings。
- 风险：documentation evidence 已过期。缓解：分开记录 evidence source 和
  verification status。
- 风险：英文和中文 status mirrors 漂移。缓解：status checks 必须覆盖两个镜像。

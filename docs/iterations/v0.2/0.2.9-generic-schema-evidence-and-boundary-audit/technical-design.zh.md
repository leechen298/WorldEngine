# Technical Design

英文版本：`technical-design.md`

## 当前状态

v0.2 milestone index 和 plan 将 0.2.9 列为 evidence 与 boundary audit package。
此前 package 已创建或更新：

- authoritative direction 和 boundary docs。
- EntityRef、WorldCell、WorldSpec、EventRef 与 Event.refs contracts。
- focused schema 和 event compatibility tests。
- 带有 command 和 test evidence 的 package reviews。
- `docs/iterations/v0.2/findings.md`，当前包含一个 deferred 0.2.7 status
  synchronization finding。

Active implementation map 仍描述 v0.1 runtime behavior。v0.2 schema 与 event
contracts 是 additive foundations，并未加载进 runtime behavior。

## Contract 对齐与不变量

- 将 completed package reviews 视为 evidence，而不是 implementation targets。
- 将 active direction、scope 和 boundary docs 视为 source-of-truth boundary
  inputs。
- 区分 historical artifact evidence 与 active direction。
- 所有 examples 和 findings 保持 domain-neutral。
- 不编辑 code、tests、schemas、fixtures、migrations、API routes 或 frontend
  files。

## 计划实现

Documentation review approval 后：

1. 阅读 completed v0.2 package reviews、contract docs、boundary docs、
   implementation maps 和 findings register。
2. 创建 `evidence-index.md` / `.zh.md`，包含 active claims、evidence source、
   verification source、status 和 notes。
3. 创建 `boundary-audit.md` / `.zh.md`，包含 boundary checks、repository path
   checks、anchor sweep summary、status drift review 和 unresolved findings。
4. 如果确认 deferred 0.2.7 status mismatch 是 documentation status drift，
   则解决它；否则保留 open 并更新 rationale。
5. 为新增、关闭或 retargeted audit findings 更新 `findings.md`。
6. 运行 `test-plan.md` 中的 documentation checks。
7. 用 exact commands、results、compatibility review、scope review 和 unresolved
   findings 更新本 package review files。

## 影响面

Documentation：

- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/evidence-index.zh.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/boundary-audit.zh.md`
- `docs/iterations/v0.2/findings.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/**`
- v0.2 milestone index 和 plan status fields。

不影响 runtime、schema、API、frontend、fixture、migration 或 test implementation
surfaces。

## Data Model / Schema Changes

无。

## Runtime / Service Design

无。

## 兼容性

Runtime behavior、schema validation、event behavior、API response shapes、
frontend behavior、fixture behavior、migration behavior 和 legacy
`backend/worldengine/` behavior 均保持不变。

Audit 可以识别 missing evidence 或 status drift，但不得通过改变 implementation
behavior 来关闭这些 gaps。

## 假设

- Package review files 包含 completed v0.2 work 最权威的 command 和 test
  evidence。
- Documentation-only audit outputs 在本 documentation gate review 后，可作为
  0.2.9 implementation deliverables。
- Link/path checks 可用 repository environment 中的 shell commands 完成。
- 除非 implementation files changed，否则 backend/frontend tests 不需要运行；
  而本 package 禁止这类变更。

## 风险

- 风险：audit language 夸大当前 runtime behavior。缓解：每个
  implemented/tested claim 必须引用 review evidence，否则标为 planned。
- 风险：anchor sweep 在 old review evidence 中发现 historical concrete-fixture
  text。缓解：将 historical artifacts 与 active direction 分开分类。
- 风险：status drift 同时影响 English 和 Chinese mirrors。缓解：status checks
  必须覆盖双方。
- 风险：missing evidence 诱发 code changes。缓解：记录 findings，并交给 later
  packages。

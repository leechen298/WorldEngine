# Contract

英文版本：`contract.md`

## 公共概念

- Release-candidate bundle：汇总 v0.2 evidence 和 limitations 的 review packet，
  不声明 final release。
- Final review bundle：从 release-candidate evidence 生成的 ChatGPT / human
  review handoff document。
- Release-candidate claim：v0.2 capability 或 boundary statement，必须映射到
  existing documentation、tests、package review evidence 或 visible limitation。
- Evidence source：completed package review、contract、audit、compatibility
  review、boundary document、release draft，或 0.2.11 当前运行的 command。
- Blocking finding：会阻止 final closeout 的 unresolved P1/P2 issue，除非已
  resolved 或被 review explicitly accepted。

## 兼容性约束

- Runtime behavior 不得改变。
- Schema behavior 和 validation behavior 不得改变。
- Event storage、event pagination 和 API response behavior 不得改变。
- Frontend behavior 不得改变。
- Fixture、migration 和 test implementation files 不得改变。
- Release-candidate docs 不得声明 final release status。
- Release-candidate claims 必须区分 implemented、documented、tested、
  reviewed、planned、not implemented、historical 和 finding states。
- Unresolved P1/P2 findings 必须保持 visible，并且在 resolved 或 explicitly
  accepted 前阻塞 0.2.12 final closeout。

## 允许变更

- 新增 `docs/iterations/v0.2/v0.2-release-candidate-bundle.md`。
- 新增 `docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md`。
- 新增 `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md`。
- 新增 `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md`。
- 用 release-candidate evidence 和 limitations 更新 `docs/releases/v0.2.md`。
- 同步更新 `docs/releases/v0.2.zh.md`。
- 如果 release-candidate assembly 发现、关闭或 retarget findings，则更新
  `docs/iterations/v0.2/findings.md`。
- 用 evidence 更新本包的 `review.md` 和 `review.zh.md`。
- 更新 v0.2 milestone index 和 plan 中 0.2.11 的 status fields。
- 运行 read-only repository searches、path checks、release-status wording checks
  和 documentation sanity checks。

## 禁止变更

- 不修改 runtime services、modules、event log behavior、archive behavior、
  agent behavior、persistence、API routes、app assembly 或 frontend behavior。
- 不修改 schema implementation files。
- 不修改 tests 或 fixtures。
- 不新增 migrations。
- 不修改 `backend/worldengine/`。
- 不实现 WorldSpec loading、RuntimeEngine-to-WorldCell migration、runtime bridge、
  generation、projection、agent loop、memory、self-continuity、resolver 或
  causality behavior。
- 不创建 external repositories，也不加入 external validation internals。
- 不增加 concrete external-world names、characters、locations、roles、resources、
  story rules、seed data、UI selectors、private runner state 或 application-specific
  backend logic。
- 除非本 session 运行了对应 command 或 flow，不声明 tests、builds、runtime behavior、
  API behavior 或 frontend behavior passed。
- 没有 human / ChatGPT approval 时，不标记 v0.2 final 或 0.2.12 ready。

## 验收要求

- `docs/iterations/v0.2/v0.2-release-candidate-bundle.md` 和 `.zh.md` 存在，并
  汇总 v0.2 scope、completed packages、evidence、limitations、unresolved
  findings、compatibility status 和 final-closeout prerequisites。
- 本包目录中的 `final-review-bundle.md` 和 `.zh.md` 存在，并遵循 final review
  bundle template structure。
- `docs/releases/v0.2.md` 和 `.zh.md` 从 draft/planned wording 更新为
  release-candidate wording，但不声明 final release。
- 每个 release-candidate claim 都映射到 concrete evidence source，或标记为
  planned、not implemented、historical 或 finding。
- P1/P2/P3 findings 显式列出，并说明是否 block final closeout。
- Release-status wording checks 确认没有声明 final release。
- Concrete demo anchor sweep 通过，或所有 residuals 被归类为 historical/review-only。
- Changed files 限于 approved documentation paths。
- Package docs、bundle docs、final-review docs 和 release docs 的英文/中文镜像同步。

## North Star 检查

本包通过让 v0.2 evidence 可 review 来保护 WorldEngine 作为 generic recursive
world engine 的方向，同时保留 future scope boundaries。它不引入 concrete worlds、
product-specific backend logic、application-specific fixtures 或 runtime behavior。

## 范围外后续

- 0.2.12 只能在 0.2.11 release-candidate bundle 通过 review 后执行 final closeout。
- v0.3 只能在 v0.2 closeout 和单独 reviewed package contract 后设计并实现
  WorldSpec loader 与 runtime bridge work。
- Future runtime、API、frontend、E2E 或 compatibility regression evidence 属于
  后续相关 code/mixed package；除非作为 read-only verification 明确运行，否则不属于
  本 documentation-only release-candidate bundle。

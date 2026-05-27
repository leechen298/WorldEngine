# v0.3 WorldSpec Loader and Runtime Bridge

状态：`planned / in progress`

## 目标

v0.3 把 v0.2 的 recursive schema foundation 推进到 validated generic
WorldSpec loader 与 minimal runtime context bridge，同时保持 v0.1 runtime
compatibility。

## 版本边界

v0.3 可以定义并在后续包中实现：

- WorldSpec loader contract。
- minimal generic WorldSpec loader。
- runtime context bridge contract。
- minimal optional runtime context bridge。
- runtime、API、event、archive、params、frontend-facing 和 legacy-path
  compatibility evidence。
- external fixture runner contract readiness。
- evidence and compatibility audit。
- release-candidate 和 final closeout documentation。

v0.3 不可以实现：

- Agent-in-World loop。
- memory 或 self-continuity substrate。
- world generation。
- 面向 external product surface 的 projection API。
- product UI 或 game UI。
- concrete demo world fixture。
- concrete external validation world。
- external fixture repository。
- external validation repository。
- story generation。
- NPC chat system。
- self-awareness claims。

## 计划来源

- 规划种子：`docs/iterations/v0.3/00-chatgpt-plan.md`
- 详细 package plan：`docs/iterations/v0.3/v0.3-plan.md`

## External Automation Consumption

WorldEngine 提供 iteration docs、package specs、verification expectations 和
review bundle templates，供 external automation controllers 消费。
WorldEngine 不实现 controller。Agent roles、retry loops、scheduling 和
orchestration 属于外部自动化。

## Package Index

### `0.3.0-v0.3-planning-and-compatibility-baseline`

类型：documentation-only
状态：`ready for review`
目的：建立 v0.3 planning docs 和 compatibility baseline，不实现 loader 或 bridge。

### `0.3.1-worldspec-loader-contract`

类型：documentation-only
状态：`planned`
目的：在实现前定义 WorldSpec loader contract。

### `0.3.2-worldspec-loader-implementation`

类型：mixed or code
状态：`planned`
目的：在 contract review 后实现 minimal generic WorldSpec loader。

### `0.3.3-runtime-context-bridge-contract`

类型：documentation-only
状态：`planned`
目的：定义 validated WorldSpec-derived context 如何接近 runtime，但暂不改变 runtime behavior。

### `0.3.4-runtime-context-bridge-implementation`

类型：mixed or code
状态：`planned`
目的：在保持现有 runtime 和 API behavior 的前提下实现 minimal optional runtime context bridge。

### `0.3.5-external-fixture-contract-readiness`

类型：documentation-only or mixed
状态：`planned`
目的：定义 external fixture runners 如何通过 public WorldEngine contracts 消费 core，不在 core 内创建 external repositories。

### `0.3.6-runtime-bridge-evidence-and-compatibility-audit`

类型：documentation-only or mixed
状态：`planned`
目的：审计 loader 和 bridge evidence、compatibility，以及 v0.4 handoff readiness。

### `0.3.7-v0.3-release-candidate-bundle`

类型：documentation-only
状态：`planned`
目的：准备 release-candidate bundle 供 human / ChatGPT review，不声明 release status。

### `0.3.8-v0.3-final-closeout`

类型：documentation-only
状态：`planned / gated`
目的：仅在 release-candidate review approval 后执行 final closeout。

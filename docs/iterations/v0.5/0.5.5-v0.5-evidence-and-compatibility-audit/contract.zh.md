# 契约

状态：review complete

## Package 决策

`0.5.5` 是 documentation-only。它审计 evidence 和 compatibility；不添加
implementation、release-candidate status 或 final release status。

Implementation authorization 保持 `no`。

## Evidence Index

### `0.5.1-memory-self-continuity-contracts`

- 类型：documentation-only。
- Final status：review complete。
- 当前证据：docs/mirror checks、scope guard、forbidden implementation sentinel、
  documentation/contract evaluator PASS。
- Implementation authorization：no。
- Result：为 working memory、episodic memory、relationship state、self-summary、
  reflection record 和 personality drift signal 定义 public concepts 和 schema semantics。

### `0.5.2-working-and-episodic-memory-substrate`

- 类型：mixed/code。
- Final status：review complete。
- Implementation authorization：documentation/contract evaluator PASS 后为 yes。
- 当前 implementation evidence：TDD red、intermediate Python 3.9 syntax failure、
  focused memory substrate green（`7 passed`）、adjacent perception/loop/API/action
  compatibility（`24 passed`）、implementation-scope evaluator PASS、P2/P3 fix 后
  code-review evaluator PASS、validation-evidence evaluator PASS、closeout
  consistency PASS。
- Result：additive generic working-memory 和 episodic-memory schemas、process-local
  in-memory substrate、focused backend tests。

### `0.5.3-memory-context-loop-integration`

- 类型：mixed/code。
- Final status：review complete。
- Implementation authorization：documentation/contract evaluator PASS 后为 yes。
- 当前 implementation evidence：TDD red（`2 failed, 14 passed`）、focused
  perception/API green（`16 passed`）、memory/loop/action adjacent matrix
  （`33 passed`）、runtime/world/event compatibility matrix（`33 passed`）、full
  backend regression（`145 passed`）、implementation-scope evaluator PASS、
  code-review evaluator PASS、validation-evidence evaluator PASS、closeout
  consistency PASS。
- Result：loop perception 中的 optional bounded read-only memory context，以及不改变
  action semantics 的 internal app-state memory store wiring。

### `0.5.4-reflection-relationship-and-drift-contract-followup`

- 类型：documentation-only。
- Final status：review complete。
- 当前证据：docs/mirror checks、scope guard、forbidden implementation sentinel、
  documentation/contract evaluator PASS。
- Implementation authorization：no。
- Result：relationship state、self-summary、reflection record 和 personality drift
  signal semantics 已细化；schema-only 和 behavior work 继续 deferred。

## Compatibility Audit

Compatibility-sensitive surfaces：

- `PerceptionFrame`：只增加 additive `memory_context`；existing fields 保持。
- `LoopStepRequest`：未改变；无 memory selectors。
- `ActionIntent`：未改变。
- `ActionResult`：未改变。
- `POST /world/agent/loop/step`：existing callers 不需要新 request fields；strict
  request validation 保持。
- `/world/agent/params/propose-and-apply`：由 adjacent loop/API tests 覆盖。
- runtime tick/world time、event routes、params behavior、API envelope/error
  shape：由 adjacent compatibility 和 full backend regression 覆盖。

无证据表明以下 surface 被改变：

- `backend/worldengine/**`。
- frontend behavior。
- migrations 或 durable persistence。
- public memory APIs。
- relationship behavior、self-summary generation、automatic reflection 或 personality
  drift action modifiers。
- concrete world content、private validation oracle details 或 application-specific
  backend logic。

## 未解决 Findings 分类

- P1：none。
- P2：none。
- P3：v0.5 audit 无 open P3。

`0.5.2` 和 `0.5.3` 中曾经 blocking 的 findings 已修复，并在 child closeout 前通过
re-evaluation。

## Release-Candidate 交接准备度

如果本地 audit checks 和 evidence/compatibility evaluator 通过，campaign 可以进入
`0.5.6` 准备 release-candidate bundle。

这不是 release-candidate declaration，也不是 final closeout。

## 允许修改

- 本目录下的 package docs 和 mirrors。
- 仅为准确交接更新 parent v0.5 status/review surfaces。

## 禁止修改

- 不修改 runtime、schema、API、frontend、test、fixture、migration、external
  repository、generated result 或 `backend/worldengine/**`。
- 本 package 不改变 release-candidate 或 final release status。
- 不把 v0.4 historical evidence 提升为当前 v0.5 pass evidence。

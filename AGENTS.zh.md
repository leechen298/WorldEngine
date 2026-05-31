# AGENTS.md

本文件为 Codex 和其他 AI coding agent 在本仓库工作时的规则说明。

英文入口：`AGENTS.md`。

## Project Overview

WorldEngine 是 recursive world generation 与 runtime engine。它的长期目标是
generate worlds、run worlds over time、support recursive world structures，并让
Agent 在这些 world 中通过 memory、continuity、feedback、action 和 pseudo-self
formation 形成持续变化的主体表现。

在提出或实现会影响项目方向的工作前，先阅读：

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`

External fixture、validation 和 projection applications 是 WorldEngine 的 consumers。
它们不是 engine core 的一部分，也不能把本仓库变成 application-specific backend code。

## Active Code Path

- `backend/app/` 是 active backend code path。
- `frontend/` 是 active dashboard code path。
- `backend/worldengine/` 是 pre-v0.1 legacy code，除非后续 iteration contract
  明确允许，否则不要视为 active path。

不要在 `backend/worldengine/` 下新增 runtime feature。

## Iteration Documentation Gate

以 `docs/iterations/README.md` 作为每个 iteration 的文档标准。
创建或修改 `docs/iterations/` 下文件时，还必须读取
`docs/iterations/AGENTS.zh.md`。该文件定义 version plan、planned package、
iteration package、validation plan、evidence 和 review documentation 的详细程度要求。

对范围较大的 documentation generation 请求，尤其是 `/plan` 风格 prompt 或需要创建多个
iteration files 的请求，起草文档前先遵循 `docs/iterations/AGENTS.zh.md` 中的 Codex
Plan-Mode Document Generation Standard。

只有当用户明确要求 subagents / parallel agent work，或 active package 的
`GOAL_RUNNER.md`、contract 或 plan 明确授权时，Codex 才可以使用 subagents。
Subagent work 必须保持在 active package scope 内，遵守同样的 git safety 和 evidence
rules，并服从 main agent；main agent 负责 synthesis、verification 和 final status。
对于 `/goal` development campaigns，iteration rules 要求 implementation-bearing child
packages close out 前必须经过 subagent / evaluator checkpoints。Iteration work 的详细
subagent 和 learning-report 规则见 `docs/iterations/AGENTS.zh.md`。

当用户说 `完成 <iteration-package>` 或 `complete <iteration-package>` 时，先在
`docs/iterations/**/<iteration-package>/` 下定位匹配 package。如果该 package 包含
`README.md`、`GOAL_RUNNER.md`、`CURRENT_STATE.md` 或 `CAMPAIGN_PLAN.md`，必须先读取
这些文件再 planning 或 execution。不要根据 memory 或相邻 package 推断 workflow。

代码或混合型 iteration 在实现前必须先有 iteration package：

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`

Documentation-only iteration 只有在不准备 runtime、schema、API、UI 或 test
实现时，才可以省略 `technical-design.md` 和 `test-plan.md`。如果它改变 process
rules、version semantics、product boundaries、concepts、evidence rules 或
templates，仍然必须包含 `contract.md`。

Iteration work 必须分成两个 gate：

1. Documentation stage：先起草或更新当前 iteration package 所需文档。除非当前请求
   明确是 documentation-only 且文件属于文档 scope，否则不要改 runtime、schema、
   API、UI、test 或 fixture 文件。
2. Implementation stage：只有 iteration package 通过 review 并批准后才能开始。把已
   批准的文档视为 work contract。

不要一边起草或修订 iteration 文档，一边实现对应的 runtime/code changes。文档必须先
单独可 review，之后才能进入代码实现。如果实现过程中发现 design gap，先停止实现，
更新相关文档；只有更新后的 contract、design、test plan 或 execution plan 通过 review
后，才能继续。

实现代码时，先按顺序阅读当前 iteration 文档并遵循它们：

1. `intent.md`
2. `contract.md`
3. `technical-design.md`
4. `test-plan.md`
5. `plan.md`
6. `review.md`

如果实现过程中发现 design problem，先停止，更新相关 iteration 文档；只有在
contract/design 更新并通过 review 后，才能继续。

## Hard Rules

1. North Star first.
   任何 feature proposal 都必须先对照 `docs/project-north-star.md`。

2. No implementation without iteration docs.
   代码或混合型 iteration 必须有 intent、contract、technical design、test plan、
   execution plan 和 review evidence。这些文档是实现前必须通过 review 的 gate，
   不是边写代码边补的 paperwork。

3. Current package only.
   只实现当前 active iteration package。不要顺手实现 adjacent future versions 或
   convenient follow-on capabilities。

4. Preserve compatibility.
   Schema extension 必须 additive，除非当前 iteration contract 明确允许 breaking
   changes。

5. Event is the system spine.
   World、Agent、memory、runtime 和 external projection 应该通过 Event contract
   与 evidence 收敛，而不是通过 hidden side effects。

6. Application surfaces are not the engine goal.
   不要把 WorldEngine 收窄成 demo-specific 或 application-specific backend logic。

7. Agent pseudo-self is core, but not automatic current scope.
   roadmap 或 iteration contract 可以只定义边界，把 Agent self-continuity 的实现放到
   后续版本。

8. Keep WorldEngine core generic.
   不要在本仓库加入 concrete demo-world names、maps、characters、locations、
   resources、story rules、seed data、UI code 或 game/application-specific backend
   logic。

9. External validation worlds are consumers.
   不要用 external validation world 反向驱动 internal engine abstractions。External
   fixture 和 validation applications 只能通过 public APIs、CLI contracts、schemas、
   exported contracts 或 redacted reports 消费 WorldEngine。

10. Review must include evidence.
   每个 code iteration 都必须在 `review.md` 记录 changed files、commands run、
   test results、compatibility review、scope review 和 unresolved findings。

## Verification and Reporting

- 只有在当前 work session 运行过相关命令或流程后，才可以声称 tests、builds、
  E2E、UI smoke 或 runtime behavior 通过。
- Docs-only iteration 可以不运行 code tests，但 `review.md` 必须说明没有运行测试及原因。
- 优先运行与 iteration contract 对应的 focused verification；当 blast radius 需要时，再运行
  broader regression commands。

## Natural-Language Validation Triggers

当用户说出 `测试 <version>`、`验证 <version>`、`<version> 是否通过`、
`测试 <iteration-package>`、`验证当前产品`，或要求 `clean pass` 这类短 validation
request 时，把它视为启动 `docs/testing/product-capability-validation-playbook.zh.md`
中可复用产品能力验证流程的请求。

这句话只是 trigger，本身不是 PASS verdict。

报告结果前必须：

- 读取 active version 或 package state，确定 in-scope validation surface。
- 如果 validation 会修改 tests、checkers、fixtures、result schemas、runtime/API/frontend
  behavior 或 durable evidence rules，先创建或使用所需 iteration package。
- 对每个 in-scope command/checker，实际运行或明确分类为 passed、failed、blocked、
  skipped 或 out of scope。
- 区分 E2E、Agent smoke、minimal autonomous saved-result validation、full autonomous
  runner/full suite 和人工观察。
- 在相关 `review.md` 或 `docs/testing/results/` summary 中记录 command results、
  artifact paths、unresolved P1/P2/P3 findings 和 final verdict。

如果当前 evidence 没有覆盖 frontend、E2E、Agent smoke、autonomous、external
validation、projection readiness 或 product readiness，必须点名这些 exclusions，不得暗示
更宽范围已经 PASS。

## Natural-Language Test Documentation Triggers

当用户说出 `编写 <version> 测试方案`、`补充 <iteration-package> 测试文档`、
`设计 <feature> 测试用例`、`写 E2E 测试场景` 或 `生成测试矩阵` 这类短
test-documentation request 时，把它视为启动
`docs/testing/test-documentation-playbook.zh.md` 中可复用测试文档流程的请求。

这个 trigger 与 validation 分开。它产出或更新测试文档、测试方案、测试场景和测试用例；
不声明 tests 已运行或通过。

如果请求同时要求编写测试文档和执行验证，先编写或更新测试文档，再使用
`docs/testing/product-capability-validation-playbook.zh.md` 进入执行和 verdict 阶段。

## Git Safety

- 不要 revert 或覆盖 working tree 中已经存在的用户修改。
- staging 或 commit 前先检查 changed-file set，并保持范围限定在当前 iteration
  package，除非用户明确扩大 scope。

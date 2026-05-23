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

第一款 village-like game 或 electronic-pet surface 只是 WorldEngine 第一个
user-facing projection。它不是 engine goal，也不能把仓库变成 game-specific
backend。

## Active Code Path

- `backend/app/` 是 active backend code path。
- `frontend/` 是 active dashboard code path。
- `backend/worldengine/` 是 pre-v0.1 legacy code，除非后续 iteration contract
  明确允许，否则不要视为 active path。

不要在 `backend/worldengine/` 下新增 runtime feature。

## Iteration Documentation Gate

以 `docs/iterations/README.md` 作为每个 iteration 的文档标准。

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

6. Game surface is not engine goal.
   不要把 WorldEngine 收窄成 village game backend。

7. Agent pseudo-self is core, but not automatic current scope.
   roadmap 或 iteration contract 可以只定义边界，把 Agent self-continuity 的实现放到
   后续版本。

8. Review must include evidence.
   每个 code iteration 都必须在 `review.md` 记录 changed files、commands run、
   test results、compatibility review、scope review 和 unresolved findings。

## Verification and Reporting

- 只有在当前 work session 运行过相关命令或流程后，才可以声称 tests、builds、
  E2E、UI smoke 或 runtime behavior 通过。
- Docs-only iteration 可以不运行 code tests，但 `review.md` 必须说明没有运行测试及原因。
- 优先运行与 iteration contract 对应的 focused verification；当 blast radius 需要时，再运行
  broader regression commands。

## Git Safety

- 不要 revert 或覆盖 working tree 中已经存在的用户修改。
- staging 或 commit 前先检查 changed-file set，并保持范围限定在当前 iteration
  package，除非用户明确扩大 scope。

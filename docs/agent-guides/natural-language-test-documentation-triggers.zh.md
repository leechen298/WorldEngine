# Natural-Language Test Documentation Triggers

Status: reusable agent routing guide

英文版本：`natural-language-test-documentation-triggers.md`。

当用户说出这类短 test-documentation request 时使用本指南：

```text
编写 <version> 测试方案
补充 <iteration-package> 测试文档
设计 <feature> 测试用例
写 E2E 测试场景
生成测试矩阵
```

## Primary Workflow

执行 `docs/testing/test-documentation-playbook.zh.md`。

这个 trigger 与 validation 分开。它产出或更新 test documentation、plans、scenarios 和
cases；不声明 tests 已运行或通过。

## Broad Version-Level Output

对于 `编写 v0.7 测试方案` 这类宽范围 version-level 请求，不要停在一个简短 plan、
checklist 或 capability matrix。必须产出或更新可 review 的测试文档套件，细节要足够让
另一个 agent 不用自行发明断言就能实现或执行。

完整 version 测试文档套件必须包含以下内容，除非 active request 或 package 明确把某一层排除在
scope 外，并把该排除记录为 unresolved gap：

- overall test strategy 和 evidence boundary。
- 具体 unit / backend integration / API test cases。
- 具体 E2E cases。
- `docs/testing/e2e-scenarios/` 下的 E2E scenario contracts。
- Agent smoke cases 和 evidence requirements。
- Codex/test-runner Agent autonomous cases。
- `docs/testing/agent-autonomous/scenarios/` 下的 Agent autonomous scenario contracts。
- 从 requirements、contracts、known risks 和 review findings 到 test cases 的 traceability。
- 每个重要层级的 command、artifact、fixture、pass/fail owner、current automation
  status 和 unresolved gap 字段。
- 让测试文档套件可发现的 README 或 index updates。

## Existing Document Handling

如果相关 test plan 或 scenario set 已经存在：

1. 先按照 `docs/testing/test-documentation-playbook.zh.md` 审核它，再扩展。
2. 缺少 concrete test cases、缺少 E2E scenario contracts、缺少 Agent autonomous
   scenario contracts、command matrix 前后不一致、PASS claim 过宽、evidence owner
   不清，都视为 documentation findings。
3. 在声称测试方案完成前，必须修复 P1/P2 documentation gaps。
4. 更新 indexes，确保后续 agent 不依赖 chat history 也能找到测试文档套件。

## Recommended Version-Level File Pattern

Version-level test suites 优先使用以下可发现的拆分结构，除非 active package 定义了更窄结构：

```text
docs/testing/<version>-overall-test-plan.zh.md
docs/testing/<version>-unit-api-test-cases.zh.md
docs/testing/<version>-e2e-test-cases.zh.md
docs/testing/<version>-agent-test-cases.zh.md
docs/testing/e2e-scenarios/<scenario>.md
docs/testing/agent-smoke/scenarios/<scenario>.md
docs/testing/agent-autonomous/scenarios/<scenario>.md
```

overall plan 只作为 strategy 和 index。具体 cases 和 scenario details 放进分册或 scenario
contracts。

## E2E Documentation Requirements

E2E 文档必须：

- 区分 implemented Playwright coverage 和 planned coverage。
- 除非 spec 真的执行 request-level API assertions，否则不要声称 UI-only spec 覆盖这些断言。
- 记录 local-server assumptions。
- 记录 serial state 和 reset boundaries。
- 包含 UI assertions、API assertions 和 event/log cross-checks。
- 包含 failure-path assertions。
- 包含 artifact/report paths。
- 将 planned gaps 与 implemented coverage 分开写。

## Agent Autonomous Documentation Requirements

这里的 "Agent" 指 Codex 或 test-runner agent 作为普通测试用户，不是未来 WorldEngine
世界里的 in-world Agent。

完整用户式 autonomous tests 分为 user-action layer 和 evidence layer。user-action layer
必须至少包含一种普通用户操作，例如操作 dashboard 或调用公开 product APIs。checker CLI
commands 和 raw artifacts 属于 verdict/evidence layer；它们不能单独替代 user-action layer。

autonomous user-action layer 可以：

- 操作 dashboard。
- 调用公开 product APIs。

verdict/evidence layer 可以：

- 运行公开 checker CLI commands。
- 记录 raw artifacts。

PASS 必须来自 deterministic checker、scorecard checker 或未来 full autonomous suite
checker。必须区分 full user-style autonomous tests、Agent smoke 和当前 minimal
saved-result checker，尤其当当前 checker 把 direct API operations 作为 Agent operations
拒绝时。

## Authorization Boundary

编写测试文档不授权新增或修改 test code、checker code、fixtures、schemas、
runtime/API/frontend behavior 或 durable result artifacts。

如果用户要求实现 tests 或执行 validation，必须先使用所需 iteration package gate，再进入对应
validation flow。

如果请求同时包含 test documentation 和 validation，先编写或更新 test documentation，再切换到
`docs/testing/product-capability-validation-playbook.zh.md` 进入执行和 verdict 阶段。

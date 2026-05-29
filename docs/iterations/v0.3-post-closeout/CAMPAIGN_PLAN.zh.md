# Campaign 计划

状态：`campaign executed / passed with P3`
类型：Codex `/goal` campaign plan

## 用途

本计划定义以下目标的执行顺序：

```text
完成 v0.3-post-closeout
```

它是 campaign 指引，不是 WorldEngine 运行时行为，也不是自动化控制器实现。

执行结果：2026-05-29 批准后的 campaign run 已完成到最终汇总，最终评估为
`passed with P3`。

## 执行顺序

### 0. 主验证规划

目的：建立父级 campaign、状态分类、停止条件、证据词汇和报告模板。

输入：v0.3 发布文档、v0.3 证据索引、兼容性审计、最终收口 review、
`docs/iterations/AGENTS.md`、范围边界文档，以及 `validation-master-plan.md`
中列出的 loader / bridge / event compatibility 代码和测试。

允许修改：创建父级 `v0.3-post-closeout` 文档和子包脚手架。

禁止修改：runtime、schema、API、frontend、backend tests、fixtures、migrations、
E2E artifacts、外部仓库、发布状态或 v0.4 实现。

预期交付：父级 README、当前状态、goal runner、campaign 计划、主验证计划、报告模板、
review，以及子包文档。

验证预期：只做文档检查。

退出条件：所有必需文档存在，不声称已经执行验证，并且可以交给人工 / ChatGPT review。

交接：`01-e2e-validation-plan` 成为第一个当前子包。

### 1. E2E / 集成 / API smoke 验证计划

目的：定义后续 E2E、集成、API smoke、loader、bridge、Event.refs、release claim
和 concrete demo-world regression 验证应该检查什么。

输入：父级 campaign 文档、v0.3 收口文档、loader / bridge / event 代码，以及当前仓库测试文件。

允许修改：更新 `01-e2e-validation-plan/**` 规划文档。

禁止修改：执行验证、实现 runtime、修改 schema、API、frontend、tests、fixtures、
外部仓库或 private oracle details。

预期交付：README、intent、contract、test plan、执行计划和规划质量 review。

验证预期：只运行文档检查和范围措辞检查。

退出条件：计划足够具体，`02` 后续执行时不需要临时发明范围或成功标准。

交接：`02-e2e-validation-execution` 只有在本计划通过 review 后才能执行。

### 2. E2E / 集成 / API smoke 执行

目的：后续运行验证命令，或明确记录阻塞，并填写 E2E / 集成验证报告。

输入：`01` 计划、`02` 执行计划、当前 branch / commit、v0.3 文档、loader / bridge /
event 代码和测试、API route 文件，以及可用的 E2E 配置。

允许修改：用执行证据或 blocker 更新 `02-e2e-validation-execution/**` 报告和 review 文件。

禁止修改：实现修复、runtime / schema / API / frontend / test 编辑、fixture data、
migrations、发布状态变更和外部仓库创建。

预期交付：填好的 `e2e-validation-report.md`、实际运行命令、P1/P2/P3 分类和 review 更新。

验证预期：后续执行应运行文档检查、后端确定性检查、聚焦 loader / bridge 测试、
event compatibility 测试、API smoke，以及在已配置时运行 E2E。如果 E2E 不可用，
记录为 not configured 或 blocked，并以 API smoke 加后端集成测试作为 fallback。

退出条件：最终评估只能是 `passed`、`passed with P3`、`blocked`、`failed` 或
`not executed`。

交接：只有 `02` 已有执行证据或已记录 blocker 后，才进入
`03-codex-autonomous-validation-plan`。

### 3. Codex 自主验证计划

目的：定义独立 Codex reviewer 的输入、约束、命令和 claim 检查，但不执行评审。

输入：父级 campaign 文档、v0.3 发布和证据文档、loader / bridge 代码、
`RuntimeEngine`、`WorldCell` / `Event` schema，以及聚焦测试。

允许修改：更新 `03-codex-autonomous-validation-plan/**` 规划文档。

禁止修改：执行自主评审、修改代码、修改测试、编辑 runtime / schema / API / frontend、
fixtures、外部仓库或 demo-world details。

预期交付：reviewer 契约、测试计划、执行计划和 review 记录。

验证预期：只做文档检查。

退出条件：`04` 可以在不依赖实现者总结的情况下运行独立评审。

交接：`04-codex-autonomous-validation-execution` 负责真正的独立 Codex review。

### 4. Codex 自主验证执行与评审

目的：后续执行或明确阻塞一次独立 Codex review，检查 v0.3 loader、bridge、
API / schema / runtime compatibility、Event.refs 兼容性和 demo-world regression 边界。

输入：`03` 计划、`04` 评审模板、v0.3 source docs、loader / bridge / event 代码和测试，
以及可用时的 `02` 验证证据。

允许修改：用独立 findings、命令、blockers 和 recommendation 更新
`04-codex-autonomous-validation-execution/**` 评审文档。

禁止修改：实现修复、runtime / schema / API / frontend / test 编辑、fixtures、
外部仓库、发布状态变更和 private oracle details。

预期交付：填好的 Codex autonomous review、unsupported claim 分类、P1/P2/P3 列表和
包 review 更新。

验证预期：reviewer 自己运行可用验证命令或记录 blocker，直接读 docs 和 code，
不依赖实现者总结。

退出条件：最终建议只能是 `passed`、`passed with P3`、`blocked`、`failed` 或
`not executed`。

交接：`05-final-validation-bundle` 只综合当前证据。

### 5. 最终验证汇总

目的：汇总当前 campaign 的 E2E / 集成、API smoke、后端、loader、bridge、
Event.refs、自主评审、release claim、compatibility、demo-world regression、P1/P2/P3、
blocker 和 v0.4 是否可继续。

输入：`02` 和 `04` 的报告、父级 campaign 状态、v0.3 证据文档，以及所有子包 review
中的未解决 findings。

允许修改：更新 `05-final-validation-bundle/**` summary 和 review 文件。

禁止修改：新实现工作、非必要的 fresh execution、发布状态变更、外部仓库创建或隐藏成功结论。

预期交付：`validation-summary.md`、`final-validation-bundle.md` 和 `review.md`。

验证预期：只综合当前证据或已记录 blocker；只有 active execution contract 要求时才重新运行命令。

退出条件：最终评估只能是 `passed`、`passed with P3`、`blocked`、`failed` 或
`not executed`；v0.4 是否可继续必须明确。

交接：如果结果为 not executed、blocked 或 failed，由后续已评审包决定下一步。
如果结果为 passed 或 passed with P3，v0.4 仍只能通过自己的已评审迭代包继续。

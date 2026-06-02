# Agent Guide Index

Status: agent guidance index

英文版本：`README.md`。

本目录存放 `AGENTS.zh.md` 引用的详细规则。`AGENTS.zh.md` 只保留简短路由和边界提醒；
trigger examples、required outputs、review gates 和执行细节写在这些 guide documents 中。

## Natural-Language Request Routing

| Request class | Guide | Primary workflow |
| --- | --- | --- |
| Iteration documentation | `natural-language-iteration-documentation-triggers.zh.md` | `docs/iterations/AGENTS.zh.md` |
| Iteration implementation | `natural-language-implementation-triggers.zh.md` | `docs/iterations/AGENTS.zh.md` |
| Product validation | `natural-language-validation-triggers.zh.md` | `docs/testing/product-capability-validation-playbook.zh.md` |
| Test documentation | `natural-language-test-documentation-triggers.zh.md` | `docs/testing/test-documentation-playbook.zh.md` |
| Code review | `natural-language-code-review-triggers.zh.md` | `docs/testing/code-review-playbook.zh.md` |

## Rules

- Natural-language triggers 只负责分类用户意图；trigger phrase 本身不授权 runtime、schema、
  API、frontend、test、fixture、migration 或 external repository implementation。
- 如果一个请求同时包含 documentation、implementation、validation 或 review，按 guide
  documents 定义的顺序执行相关 workflow。
- 所有结论必须有 evidence boundary。不要仅凭 trigger phrase 报告 PASS、closeout 或
  implementation completion。

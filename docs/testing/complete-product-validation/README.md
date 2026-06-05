# Complete Product Validation Documentation Suite

Status: planned complete testing documentation suite, documentation-only

Chinese mirror: `README.zh.md`.

## Purpose

This directory is the entry point for complete WorldEngine product validation.
It organizes the documents needed to test all current and roadmap-relevant
WorldEngine functionality without turning one oversized test plan into an
unreviewable document.

The suite is designed for future validation runs that need to answer:

```text
Can WorldEngine generate worlds, run worlds over time, expose events,
snapshots, replay evidence, support Agents with memory and continuity, project
public state to external consumers, and prove the lifecycle through redacted
evidence and checkers?
```

This is not a PASS record. It is not a product iteration. It does not authorize
runtime, API, checker, fixture, frontend, provider, or Validation Client code
changes.

## Current Baseline

- `0.8.9` basic full lifecycle autonomous validation has passed through the
  saved-result checker.
- That PASS proves a minimum external-client lifecycle: create world, advance
  ticks, observe events and snapshots, capture one WorldEngine-backed Agent
  action, submit director guidance, export evidence, and pass redaction.
- That PASS does not prove LLM-backed provider calls, LLM-backed world
  creation, generated world rules, event legality under rules, or sustained
  Agent pseudo-self behavior.
- The LLM-backed validation contract is defined in
  `docs/testing/llm-backed-lifecycle-validation-plan.md` and is referenced by
  this suite instead of duplicated as a standalone island.

## Document Map

| Document | Role |
| --- | --- |
| `README.md` / `README.zh.md` | Suite index, status, and usage model. |
| `coverage-map.md` / `coverage-map.zh.md` | Complete product capability taxonomy and traceability from North Star to test surfaces. |
| `validation-spec.md` / `validation-spec.zh.md` | PASS/FAIL authority, validation layers, roles, verdict rules, and non-negotiable boundaries. |
| `scenario-matrix.md` / `scenario-matrix.zh.md` | Scenario catalog for all major capability areas, including existing E2E, Agent smoke, autonomous, and LLM-backed lifecycle scenarios. |
| `runbook.md` / `runbook.zh.md` | Future execution sequence for full validation, including preflight, staged checks, second-Agent review, and result recording. |
| `evidence-contract.md` / `evidence-contract.zh.md` | Artifact layout, required summaries, operation logs, redaction rules, and evidence bundle expectations. |
| `result-template.md` / `result-template.zh.md` | Durable result summary template for `docs/testing/results/`. |
| `gap-routing.md` / `gap-routing.zh.md` | How to classify failures and decide whether to open testing-asset work, a WorldEngine implementation iteration, a Validation Client milestone, or an environment repair. |

## Relationship To Existing Testing Docs

This suite does not replace the existing testing docs. It composes them:

- `docs/testing/product-capability-validation-playbook.md` defines the generic
  product validation process.
- `docs/testing/test-documentation-playbook.md` defines how test
  documentation should be written.
- `docs/testing/e2e-scenarios/` defines browser E2E scenario contracts.
- `docs/testing/agent-smoke/` defines Agent-assisted smoke contracts.
- `docs/testing/agent-autonomous/` defines Codex/test-runner autonomous
  saved-result contracts and checker expectations.
- `docs/testing/llm-backed-lifecycle-validation-plan.md` defines the
  LLM-backed lifecycle validation contract.
- `docs/testing/results/` records durable evidence after actual validation
  runs.

## Usage Model

Use this suite when the user asks for:

```text
/goal 对当前产品能力做完整验证
/goal 完整测试 WorldEngine 全部功能
/goal 运行完整 LLM-backed lifecycle 验证
/goal 生成完整测试文档
```

If the request is documentation-only, generate or update docs in this suite
and do not claim PASS.

If the request is validation execution, use `runbook.md`, produce a result
directory, run the documented commands/checkers, perform second-Agent review
when required, and write a durable result under `docs/testing/results/`.

If validation discovers missing implementation, use `gap-routing.md` before
opening any WorldEngine iteration or Validation Client milestone.

## Completion Standard

Complete product validation is only complete when every in-scope capability in
`coverage-map.md` has one of these statuses with evidence:

- `pass`.
- `fail`.
- `blocked`.
- `skipped`.
- `out_of_scope`.

`pass` requires checker output, command output, scorecard evidence, or
second-Agent read-only review as defined in `validation-spec.md`. Plans,
manual impressions, UI smoke alone, provider readiness alone, and deterministic
mock behavior alone are not enough.

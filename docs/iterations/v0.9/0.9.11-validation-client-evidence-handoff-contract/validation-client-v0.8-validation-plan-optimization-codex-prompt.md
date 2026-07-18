# Codex Prompt: Implement Validation Client v0.8 Validation Plan Optimization

Chinese mirror:
`validation-client-v0.8-validation-plan-optimization-codex-prompt.zh.md`.

Use this prompt in a new Codex chat rooted at:

```text
/Users/leechen/projects/WorldEngine-Validation-Client
```

## Prompt

```text
PLEASE IMPLEMENT THIS PLAN:

Goal:
Create and implement Validation Client v0.8 as an optimization iteration:
`v0.8-worldengine-v0.9-validation-plan-optimization`.

The goal is to update the Validation Client's complete WorldEngine test plan,
scenario matrix, evidence bundle contract, runbook, and implementation support
for WorldEngine v0.9 validation. This should be a repeatable optimization
pattern: future Validation Client versions may repeat it whenever WorldEngine
updates public validation surfaces, scenario contracts, artifact contracts, or
checker rules.

The Validation Client must remain an external client and evidence carrier. It
must not become the LLM provider owner, world generator, event legality
authority, Agent autonomy authority, evaluator, or PASS source.

Repositories:
- Validation Client:
  /Users/leechen/projects/WorldEngine-Validation-Client
- WorldEngine reference repository:
  /Users/leechen/projects/WorldEnginProjects/WorldEngine

Required WorldEngine reading:
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/AGENTS.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/project-north-star.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/product-model.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/scope-boundaries.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/roadmap.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/README.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/llm-backed-lifecycle-validation-plan.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-suite-execution.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-artifact-contract.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-scorecard.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/second-agent-review-protocol.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/provider-live-smoke-deepseek.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-world-creation.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/world-rule-parameter-evolution.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/agent-persistent-autonomy-evidence.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-full-lifecycle-autonomous.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution/review.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/validation-client-v0.8-validation-plan-optimization-handoff.md
- /Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/validation-client-v0.8-validation-plan-optimization-handoff.zh.md

Required Validation Client reading:
- AGENTS.md
- AGENTS.zh.md, if present
- docs/specs/validation-client-design.md
- docs/specs/validation-client-design.zh.md
- docs/milestones/v0.7-agent-autonomous-validation/
- apps/api/app/worldengine_client.py
- apps/api/app/routes/evidence.py
- apps/api/app/routes/validation_runs.py
- apps/api/app/routes/sessions.py
- apps/api/app/routes/timelines.py
- apps/web/src/pages/RuntimeConsole.tsx
- apps/web/src/api/client.ts
- apps/web/src/api/types.ts
- apps/web/e2e/v0.7-ui-smoke.spec.ts

Current state to preserve:
- v0.7 already has useful WorldEngine discovery, session creation, operation
  logs, validation runs, evidence bundle export, Runtime Console UI, replay,
  branch, director guidance, and Playwright smoke.
- Some v0.7 docs still point at WorldEngine 0.8.9 gates. Treat those as
  historical references. v0.8 must target WorldEngine v0.9.
- WorldEngine v0.9 LLM-backed validation is currently checker-valid BLOCKED,
  not PASS. Do not claim provider live PASS, LLM-backed full lifecycle PASS,
  Validation Client export PASS, or external validation PASS unless fresh
  checker/scorecard/second-Agent evidence proves it.

Required workflow:
1. First create the v0.8 optimization milestone documentation package:
   docs/milestones/v0.8-worldengine-v0.9-validation-plan-optimization/
2. Include at least:
   - README.md and README.zh.md
   - intent.md and intent.zh.md
   - contract.md and contract.zh.md
   - technical-design.md and technical-design.zh.md
   - test-plan.md and test-plan.zh.md
   - plan.md and plan.zh.md
   - review.md and review.zh.md
   - scenario-operation-matrix.md and scenario-operation-matrix.zh.md
   - artifact-contract.md and artifact-contract.zh.md
   - redaction-matrix.md and redaction-matrix.zh.md
   - autonomous-validation-runbook.md and autonomous-validation-runbook.zh.md
   - second-agent-review-template.md and second-agent-review-template.zh.md
3. After the docs are created, perform a documentation-stage review and record
   whether implementation is authorized. If the current user prompt explicitly
   authorizes implementation after docs, continue to implementation. Otherwise
   stop after the docs package and report that implementation is waiting for
   review.

Implementation scope, if authorized:
1. Refresh v0.8 routing and stale v0.7 references so v0.8 targets WorldEngine
   v0.9, not WorldEngine 0.8.9.
2. Extend WorldEngine discovery to model v0.9 public surfaces:
   - GET /health
   - GET /manifest
   - GET /openapi.json
   - POST /provider/live-smoke
   - POST /world/generation/worldview
   - POST /worlds
   - GET /runtime/state
   - POST /runtime/step
   - POST /runtime/run
   - POST /runtime/pause
   - POST /runtime/resume
   - GET /world/events
   - GET /world/event-steps
   - GET /archive/snapshots
   - GET /world/params
   - POST /worlds/{world_id}/direction
   - POST /worlds/{world_id}/director-guidance
   - POST /worlds/{world_id}/evolution/evaluate-event
   - POST /worlds/{world_id}/agents/{agent_id}/continuity/evaluate
   - POST /worlds/{world_id}/narrative/project
   - POST /worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate
3. Add bounded runtime controls to UI and logs:
   - step once
   - run N ticks
   - run N world-time seconds when supported
   - pause
   - resume
   - run another bounded segment
4. Add scenario-aware evidence export for:
   - worldengine-full-lifecycle-autonomous
   - provider-live-smoke-deepseek
   - llm-backed-world-creation
   - world-rule-parameter-evolution
   - rule-compliant-event-generation
   - agent-persistent-autonomy-evidence
   - llm-backed-full-lifecycle-autonomous
5. Add or upgrade v0.9-compatible evidence bundle manifest:
   - schema_version
   - bundle_id
   - scenario
   - result_status
   - client_role=display_export_only
   - provider_owner=worldengine
   - evaluator_role=worldengine_checker_or_second_agent_review
   - created_at
   - artifact_index
   - redaction_status
   - checker_contract
   - unsupported_items
6. Support named artifacts where scenario-required:
   - result.json
   - operation-log.jsonl
   - api-log.jsonl
   - api-summary.json
   - provider-live-summary.json
   - world-creation-summary.json
   - world-rule-summary.json
   - rule-parameter-summary.json
   - event-legality-summary.json
   - agent-autonomy-summary.json
   - diff-replay-summary.json
   - world-lifecycle-summary.json
   - narrative-projection-summary.json
   - diagnostic-conversation-summary.json
   - redaction-scan.json
   - scorecard-summary.json
   - second-agent-review.md
   - transcript.md
   - console.log
   - screenshots/
7. Separate user-visible operation logs from direct API harvest logs. Do not
   disguise direct API calls as user or Agent operations.
8. Preserve statuses exactly:
   - pass
   - fail
   - blocked
   - not_run
   - out_of_scope only when a scenario contract allows it
9. Add redaction scanning for all displayable/exportable artifacts. The bundle
   must fail if it includes API keys, authorization headers, raw prompts, raw
   provider requests/responses, provider traces, private Agent memory/goals,
   raw thought, hidden context, private evaluator data, seed, or oracle data.
10. Display scorecard/checker/second-Agent review results, but do not let the
    client decide PASS.

Forbidden implementation:
- Do not directly call DeepSeek or any provider from Validation Client.
- Do not store, show, or forward provider keys.
- Do not generate LLM-backed world content in the client.
- Do not compute authoritative world rules, parameter changes, event legality,
  or Agent autonomy in the client.
- Do not map blocked/not_run/unsupported into PASS.
- Do not treat Validation Client UI smoke as WorldEngine validation PASS.
- Do not write narrative projection or diagnostic dialogue into canonical
  world state or Agent memory.
- Do not leak raw prompts, raw responses, provider traces, private memory,
  private goals, raw thought, hidden context, private evaluator data, seed, or
  oracle data.

Required tests and checks:
- Add API tests for manifest schema, artifact_index relative paths, path
  traversal rejection, status enum preservation, unsupported_items,
  redaction flags, and missing required artifacts not becoming PASS.
- Add API tests for provider-blocked saved-result export.
- Add frontend tests for v0.9 artifact display, scorecard/second-Agent review
  display, redaction warning display, and UI not claiming evaluator/human PASS.
- Add E2E or integration coverage for exporting a v0.9 evidence bundle.
- When possible, validate an exported result directory from WorldEngine:
  cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
  make validate-agent-autonomous-result RESULT_DIR=<result-dir>

Run the repository checks that apply:
cd /Users/leechen/projects/WorldEngine-Validation-Client
cd apps/api && uv run pytest -q
pnpm --dir apps/web test
pnpm --dir apps/web build
pnpm run test
pnpm run build
git diff --check

Use subagents if useful for read-only review, evidence-contract review, or
redaction review.

Final report in Chinese:
- Summary verdict.
- Docs created/updated.
- Code files changed.
- Tests/checkers run and results.
- Exported result directory path, if generated.
- Whether a real provider call happened.
- Whether any raw prompt/response/key/private memory/raw thought leak was found.
- Remaining PASS/PARTIAL/BLOCKED/FAIL state.
- Whether the work is committed/pushed or not.
```

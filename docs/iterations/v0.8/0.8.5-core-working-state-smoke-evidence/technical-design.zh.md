# Technical Design

状态：documentation-stage validation design

## Evidence Matrix Design

本 package 使用 command matrix，每个 core surface 一行：

```text
surface_id
evidence_class
command
proof_boundary
expected_status
artifact_or_log_reference
non_claims
```

任何 command 运行前，matrix 必须先记录在 `test-plan.md`。Evidence execution 只有在 review
authorization 后才可运行列出的 commands。

## Required Command Groups

Documentation-stage candidate matrix 定义这些 command groups：

1. Formatting and documentation guards：
   - `git diff --check`
   - required package docs and mirrors check。
   - status consistency check。
   - changed-file scope guard。
   - v0.8 Markdown whitespace check。
2. Generation and loader backend focused tests：
   - WorldSpec schema and loader tests。
   - deterministic generation、plan schema/import/compile、template catalog、generation
     schema、preview、regeneration、runtime-readiness 和 core-readiness tests。
3. Runtime/event/backend focused tests：
   - runtime context bridge。
   - runtime step。
   - event schema/API compatibility。
   - archive snapshot/summary。
4. Agent/memory backend focused tests：
   - Agent loop service/API/perception/action adapter。
   - memory substrate。
   - params agent 和当前 core behavior 使用的 dry-run validation boundaries。
5. v0.7 handoff compatibility：
   - 如需确认 report/manifest/projection handoff compatibility，可运行 repository-local public
     contract/checker commands。
6. Explicit non-run classifications：
   - frontend build/unit、E2E、Agent smoke、autonomous、external validation、product readiness
     和 generation-quality checks，除非 reviewed package 授权并命名 commands。

## Proof Boundary Design

每个 command result 必须窄解释：

- backend/API focused tests 只证明其命名的 backend/API surfaces。
- checker tests 只证明 checker/schema compatibility。
- documentation guards 只证明 documentation shape、status 和 scope。
- historical v0.7/v0.6 results 只证明 handoff context。
- skipped/out-of-scope entries 不证明任何 PASS，且不得计为 PASS。

## Artifact Design

本 package 可在 `review.md` 中记录 command output summaries。`docs/testing/results/` 下的独立
result artifact 是 optional，且必须在创建前获得授权，保持 repository-local 和 redacted。

Artifact references 不得包含 private external repository paths、external validator details、
private scenario names、UI selectors、screenshots、transcripts、raw prompts、provider
traces、secrets、concrete validation worlds 或 non-redacted external event payloads。

## Authorization Design

Documentation review 可以授权 evidence execution，但默认不应授权 implementation changes。如果
evidence 暴露 bug 或 missing test implementation，应停止并创建或更新相关 package contract，
之后才可修改 code。

# Complete Product Validation Result Template

Status: template

Chinese mirror: `result-template.zh.md`.

Use this template for:

```text
docs/testing/results/YYYY-MM-DD-complete-product-validation.md
```

## Header

```markdown
# Complete Product Validation Result

Status: clean_pass | partial_pass | failed | blocked
Mode: documentation audit | command validation | autonomous validation | LLM-backed lifecycle | mixed
Date: YYYY-MM-DD
Branch:
Commit:
Result directory:
Chinese mirror: `YYYY-MM-DD-complete-product-validation.zh.md`
```

## Scope

```markdown
## Scope

In scope:

- ...

Out of scope:

- ...

This result does not claim:

- ...
```

## Current Baseline

Record the current state relied on by the run:

- active version or package state.
- relevant prior durable result files.
- whether LLM-backed lifecycle is in scope.
- whether Validation Client is in scope.

## Command Matrix

| Layer | Command or checker | Working directory | Result | PASS authority | Artifact |
| --- | --- | --- | --- | --- | --- |
| L0 | ... | ... | ... | yes/no | ... |

## Coverage Matrix

| CPV ID | Capability | Scope status | Validation status | Evidence | Findings |
| --- | --- | --- | --- | --- | --- |
| CPV-01 | Governance and scope boundary | in_scope | pass/fail/blocked/skipped/out_of_scope | ... | ... |

Every CPV row from `coverage-map.md` must be present.

## Scenario Results

| Scenario | Status | PASS/FAIL source | Artifact | Notes |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

## Artifact Summary

List required artifacts and whether they exist:

- `result.json`:
- `coverage-matrix.json`:
- `command-matrix.md`:
- `operation-log.jsonl`:
- `api-summary.json`:
- `redaction-scan.json`:
- `second-agent-review.md`:

## Redaction Review

```markdown
Redaction verdict: pass | fail | not_run

Forbidden content scan:

- API keys:
- authorization headers:
- raw prompts:
- raw provider responses:
- private Agent memory/goals/thought:
- hidden context:
- private evaluator/oracle data:
- concrete external validation world seed data:
```

## Second-Agent Review

```markdown
Second-Agent review: pass | failed | not_run
Reviewer:
Blocking P1/P2: yes | no
Report:
```

## Failures And Findings

| ID | Severity | Taxonomy | Evidence | Required follow-up |
| --- | --- | --- | --- | --- |
| ... | P1/P2/P3 | provider/world_creation/world_evolution/event_legality/agent_autonomy/redaction/client_evidence/checker_gap/runtime/frontend/docs/environment | ... | ... |

## Verdict

```markdown
Verdict: clean_pass | partial_pass | failed | blocked

Reason:

Evidence source:

Unresolved blockers:
```

## Handoff

Route follow-up using `gap-routing.md`:

- testing assets:
- WorldEngine iteration:
- Validation Client milestone:
- provider/environment:
- redaction repair:

# Second-Agent Evidence Review Protocol

Status: planned review protocol

## Purpose

Second-Agent review is a read-only evidence review. It prevents the operating
Agent from self-declaring PASS after producing artifacts.

## Inputs

- result directory path.
- scenario contract.
- scorecard contract.
- artifact contract.
- checker output.
- operation logs.
- API summaries.
- evidence bundle.

## Forbidden Actions

The second Agent must not:

- modify result artifacts.
- rerun product flows and overwrite evidence.
- repair code.
- infer PASS from UI screenshots alone.
- inspect private provider keys or private WorldEngine internals.
- use hidden reset APIs, database internals, private oracles, or external world
  seed data.

## Review Checklist

The second Agent must check:

- required artifacts exist.
- scenario name matches the result.
- checker or scorecard output is present.
- every critical score item has a supported PASS source.
- no operation-log direct API call is disguised as an Agent UI/CLI operation.
- API evidence is in API summary/log artifacts.
- redaction scan is clean.
- no raw prompt, raw response, API key, private Agent memory, raw thought,
  hidden context, or oracle data appears.
- unsupported PASS claims are absent.
- failures are classified using the scenario taxonomy.

## Output

Write or report:

```text
second-agent-review.md
```

Minimum sections:

- Scope.
- Inputs reviewed.
- Artifact completeness.
- Checker/scorecard review.
- Operation boundary review.
- Redaction review.
- PASS overclaim review.
- Findings table.
- Final review verdict.

Any P1 or P2 finding blocks full lifecycle PASS.

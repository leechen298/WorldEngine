# Scenario: dashboard-params-flow

Status: planned follow-up

This scenario is intentionally not part of the first Agent smoke run. It is
reserved for a later package after `dashboard-basic-runtime` proves the evidence
protocol.

Expected future coverage:

- record world params before a UI patch.
- set `counter.increment`.
- record world params after the patch.
- step runtime.
- prove the counter event reflects the new increment.

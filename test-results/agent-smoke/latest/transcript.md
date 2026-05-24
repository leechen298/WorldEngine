# Agent Smoke Transcript: dashboard-params-flow

## Scenario

`dashboard-params-flow`

## Actions

1. Ran the approved evidence helper baseline command before the successful dashboard UI flow.
2. Opened the WorldEngine dashboard at `http://127.0.0.1:5173/`.
3. Filled `counter.increment` in the params path input.
4. Selected params type `number`.
5. Filled params value `2`.
6. Clicked `Apply`.
7. Observed the dashboard params JSON update to `counter.increment.value = 2`.
8. Clicked `Step`.
9. Observed the runtime tick advance from `0` to `1`.
10. Captured `screenshots/dashboard-params-flow.png`.
11. Ran the approved evidence helper collect command to generate `api-summary.json`.
12. Ran `make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest`.

## Notes

No direct API operation was recorded as an Agent operation. Backend API reads
used to produce `api-baseline.json` and `api-summary.json` were performed by
the approved helper commands.

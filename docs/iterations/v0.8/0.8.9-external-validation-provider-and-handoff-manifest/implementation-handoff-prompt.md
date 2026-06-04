# Implementation Handoff Prompt

Chinese mirror: `implementation-handoff-prompt.zh.md`.

Use this prompt in a future implementation chat. This package currently
remains documentation-only.

```text
/goal Implement 0.8.9-external-validation-provider-and-handoff-manifest public handoff manifest and world creation contract.

Required reading:
- AGENTS.md
- docs/project-north-star.md
- docs/product-model.md
- docs/scope-boundaries.md
- docs/roadmap.md
- docs/iterations/README.md
- docs/iterations/AGENTS.md
- docs/iterations/v0.8/README.md
- docs/iterations/v0.8/CURRENT_STATE.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/README.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/technical-design.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/validation-client-contract-handoff.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-task-plan.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/external-validation-gate-matrix.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/planning-readiness-checklist.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/handoff-status.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-handoff-prompt.md

Goal:
- Add or implement GET /manifest returning a redacted public readiness document.
- Add an OpenAPI-discoverable public world creation endpoint, preferably POST /worlds.
- Ensure the world creation response includes public world_id, status, public state, and visualization.
- If feasible, add POST /worlds/{world_id}/director-guidance.
- Expose provider readiness only as provider class, readiness, credential source class, and public model label.

Boundaries:
- Do not implement Validation Client code.
- Do not add concrete demo-world content.
- Do not move external validator behavior into WorldEngine.
- Do not expose API keys, private prompts, provider raw traces, private Agent memory, private goals, self_state, hidden_context, or private file paths.
- Do not reopen v0.8 final closeout. 0.8.9 is a post-closeout addendum.

Verification:
- cd backend && .venv/bin/python -m pytest app/tests -q
- git diff --check
- Start WorldEngine and verify /health, /manifest, /openapi.json, and POST /worlds.
- Start Validation Client API and verify /health/worldengine reports world_creation: available.
- Verify Validation Client POST /sessions/worldengine succeeds.

Completion:
- Update this package review.md and review.zh.md.
- If contract ready, record evidence using contract-readiness-checklist.md.
- Conclude only that WorldEngine contract is ready for Validation Client autonomous validation.
- Do not claim external validation PASS or human validation PASS.
```

## Stop Rules

- Stop if the implementation requires concrete demo-world content.
- Stop if provider credentials would be exposed in public output.
- Stop if Validation Client code changes are needed; record that as a
  downstream Validation Client task instead.
- Stop if the implementation would change the meaning of v0.8 final closeout.

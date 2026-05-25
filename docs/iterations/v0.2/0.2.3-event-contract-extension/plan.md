# Plan

## Files

Create during documentation stage:

- `docs/iterations/v0.2/0.2.3-event-contract-extension/README.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/README.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/intent.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/intent.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/contract.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/contract.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/technical-design.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/test-plan.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/plan.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/plan.zh.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/review.md`
- `docs/iterations/v0.2/0.2.3-event-contract-extension/review.zh.md`

Modify during documentation stage:

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Allowed implementation files after review approval:

- `backend/app/schemas/event.py`
- `backend/app/tests/test_event_schema_compat.py`
- this package's `review.md` and `review.zh.md` during closeout

Do not touch during documentation stage:

- `backend/`
- `frontend/`
- `backend/worldengine/`
- `docs/iterations/v0.2/0.2.1-project-north-star/`
- `docs/iterations/v0.2/0.2.2-recursive-world-contract/`
- 0.2.4 package files.

## Steps

1. Create the complete 0.2.3 English package documents.
2. Create synchronized `.zh.md` mirrors.
3. Update v0.2 README and plan documents so 0.2.3 is `ready for implementation`.
4. Run documentation-stage verification commands from `test-plan.md`.
5. Update `review.md` and `review.zh.md` with actual documentation-stage
   evidence.
6. Stop before implementation. Use `worldengine-iteration-dev` only when
   implementation is explicitly requested.

## Verification

Focused documentation-stage verification:

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.3-event-contract-extension -maxdepth 1 -type f | sort
rg -n "0.2.3-event-contract-extension|ready for implementation|EventRef|refs|Event Contract|backward compatible|payload|EventPage|EventStep|EventStepPage" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|concrete demo|migration|agent memory|pseudo-self|referential integrity|resolve refs|frontend|API route" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'
```

Implementation verification is defined in `test-plan.md` but must not run
until code is added after review approval.

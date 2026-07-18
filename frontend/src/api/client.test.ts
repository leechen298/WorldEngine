import { afterEach, describe, expect, it, vi } from "vitest";

import {
  applyWorldParams,
  ApiClientError,
  checkGenerationRuntimeReadiness,
  createSessionFromWorldview,
  fetchHealth,
  getSessionStatus,
  previewGeneration,
  pauseSession,
  regenerateWorld,
  getWorldEventSteps,
  getWorldParams,
  getWorldEvents,
  getRuntimeState,
  listSessionSnapshots,
  resumeSession,
  runSession,
  stepRuntime,
} from "./client";

const fetchMock = vi.fn();

vi.stubGlobal("fetch", fetchMock);

describe("api client", () => {
  afterEach(() => {
    fetchMock.mockReset();
  });

  it("unwraps successful response data", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            tick_id: 3,
            world_time_seconds: 1800,
            step_seconds: 600,
            updated_at: "2026-03-09T00:00:00+00:00",
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(getRuntimeState()).resolves.toEqual({
      tick_id: 3,
      world_time_seconds: 1800,
      step_seconds: 600,
      updated_at: "2026-03-09T00:00:00+00:00",
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/runtime/state", undefined);
  });

  it("throws ApiClientError for http errors with api payload", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 20,
          msg: "Unauthenticated",
        }),
        {
          status: 401,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(fetchHealth()).rejects.toMatchObject({
      name: "ApiClientError",
      message: "Unauthenticated",
      status: 401,
      code: 20,
    });
  });

  it("throws ApiClientError when success status has non-zero business code", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 29,
          msg: "Conflict",
          data: null,
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(stepRuntime()).rejects.toMatchObject({
      name: "ApiClientError",
      message: "Conflict",
      status: 200,
      code: 29,
    });
  });

  it("creates sessions from public worldview input", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            session_id: "session-1",
            world_id: "world-1",
            public_label: "generated-world",
            status: "created",
            runtime_ref: { tick_id: 0, world_time_seconds: 0, step_seconds: 600 },
            evidence_refs: {
              event_count_at_create: 0,
              snapshot_count_at_create: 0,
              current_event_count: 0,
              current_snapshot_count: 0,
            },
            generation_summary: {
              request_id: "request-1",
              generation_id: "generation-1",
              generation_status: "fallback",
              generation_mode: "deterministic_fallback",
              creation_mode: "deterministic_generic_fallback",
              provider_class: "unconfigured",
              provider_backed: false,
              llm_backed: false,
              deterministic_generic_fallback_detected: true,
              premise_digest: "abc123",
              runtime_ready: "true",
              blockers: [],
              warnings: [],
              public_world_model_refs: {},
            },
            created_at: "2026-03-09T00:00:00+00:00",
            updated_at: "2026-03-09T00:00:00+00:00",
            persistence: "in_memory",
          },
        }),
        { status: 200, headers: { "Content-Type": "application/json" } },
      ),
    );

    await expect(
      createSessionFromWorldview({
        request_id: "request-1",
        worldview_premise: "public workshop world",
      }),
    ).resolves.toMatchObject({
      session_id: "session-1",
      generation_summary: {
        generation_mode: "deterministic_fallback",
      },
    });
    expect(fetchMock).toHaveBeenCalledWith(
      "http://localhost:8000/sessions/from-worldview",
      expect.objectContaining({ method: "POST" }),
    );
  });

  it("calls session run and control endpoints", async () => {
    fetchMock
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            code: 0,
            msg: "ok",
            data: {
              session_id: "session-1",
              world_id: "world-1",
              run_summary: {
                schema_version: "0.9.5",
                status: "completed",
                stop_reason: "requested_ticks_reached",
                start_tick: 0,
                end_tick: 2,
                start_world_time_seconds: 0,
                end_world_time_seconds: 1200,
                step_seconds: 600,
                ticks_requested: 2,
                duration_requested_seconds: null,
                ticks_executed: 2,
                guard_summary: { max_ticks: 5 },
                provider_calls_used: 0,
                estimated_cost_units_used: 0,
                redaction_status: "passed",
                control_status: "idle",
              },
              runtime_delta: {
                start_tick: 0,
                end_tick: 2,
                start_world_time_seconds: 0,
                end_world_time_seconds: 1200,
              },
              event_evidence: {
                event_count_before: 0,
                event_count_after: 2,
                event_delta_count: 2,
              },
              snapshot_evidence: {
                snapshot_count_before: 0,
                snapshot_count_after: 2,
                snapshot_delta_count: 2,
                snapshot_ids: ["snap-1", "snap-2"],
              },
              timeline_label: "timeline branch for session session-1",
              redaction_status: "passed",
            },
          }),
          { status: 200, headers: { "Content-Type": "application/json" } },
        ),
      )
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({ code: 0, msg: "ok", data: { status: "paused" } }),
          { status: 200, headers: { "Content-Type": "application/json" } },
        ),
      )
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            code: 0,
            msg: "ok",
            data: {
              session_id: "session-1",
              world_id: "world-1",
              public_label: "WorldEngine MVP session",
              status: "ready",
              runtime_ref: { tick_id: 2, world_time_seconds: 1200, step_seconds: 600 },
              evidence_refs: {
                event_count_at_create: 0,
                snapshot_count_at_create: 0,
                current_event_count: 2,
                current_snapshot_count: 2,
              },
              created_at: "2026-03-09T00:00:00+00:00",
              updated_at: "2026-03-09T00:20:00+00:00",
              persistence: "in_memory",
            },
          }),
          { status: 200, headers: { "Content-Type": "application/json" } },
        ),
      );

    await expect(runSession("session-1", { ticks: 2, max_ticks: 5 })).resolves.toMatchObject({
      snapshot_evidence: { snapshot_delta_count: 2 },
    });
    await expect(pauseSession("session-1")).resolves.toEqual({ status: "paused" });
    await expect(resumeSession("session-1")).resolves.toMatchObject({ status: "ready" });

    expect(fetchMock).toHaveBeenNthCalledWith(
      1,
      "http://localhost:8000/sessions/session-1/run",
      expect.objectContaining({ method: "POST" }),
    );
    expect(fetchMock).toHaveBeenNthCalledWith(
      2,
      "http://localhost:8000/sessions/session-1/pause",
      expect.objectContaining({ method: "POST" }),
    );
    expect(fetchMock).toHaveBeenNthCalledWith(
      3,
      "http://localhost:8000/sessions/session-1/resume",
      expect.objectContaining({ method: "POST" }),
    );
  });

  it("reads session status and bounded session snapshots", async () => {
    fetchMock
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            code: 0,
            msg: "ok",
            data: {
              session_id: "session-1",
              status: "ready",
              runtime_ref: { tick_id: 2, world_time_seconds: 1200, step_seconds: 600 },
              evidence_refs: {
                event_count_at_create: 0,
                snapshot_count_at_create: 0,
                current_event_count: 2,
                current_snapshot_count: 2,
              },
              updated_at: "2026-03-09T00:20:00+00:00",
            },
          }),
          { status: 200, headers: { "Content-Type": "application/json" } },
        ),
      )
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            code: 0,
            msg: "ok",
            data: {
              session_id: "session-1",
              world_id: "world-1",
              items: [
                {
                  id: "snap-2",
                  tick_id: 2,
                  world_time_seconds: 1200,
                  created_at: "2026-03-09T00:20:00+00:00",
                  runtime_state: { tick_id: 2, world_time_seconds: 1200, step_seconds: 600 },
                  params: {},
                },
              ],
              total: 2,
              limit: 1,
              timeline_label: "timeline branch for session session-1",
              redaction_status: "passed",
            },
          }),
          { status: 200, headers: { "Content-Type": "application/json" } },
        ),
      );

    await expect(getSessionStatus("session-1")).resolves.toMatchObject({ status: "ready" });
    await expect(listSessionSnapshots("session-1", { limit: 1, order: "desc" })).resolves.toMatchObject({
      total: 2,
      items: [{ id: "snap-2" }],
    });
    expect(fetchMock).toHaveBeenNthCalledWith(
      2,
      "http://localhost:8000/sessions/session-1/snapshots?limit=1&order=desc",
      undefined,
    );
  });

  it("builds query strings for world events", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            items: [],
            next_cursor: "evt-2",
            has_more: true,
            limit: 10,
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(
      getWorldEvents({ from_tick: 2, to_tick: 4, cursor: "evt-9", limit: 10 }),
    ).resolves.toEqual({
      items: [],
      next_cursor: "evt-2",
      has_more: true,
      limit: 10,
    });
    expect(fetchMock).toHaveBeenCalledWith(
      "http://localhost:8000/world/events?from_tick=2&to_tick=4&cursor=evt-9&limit=10",
      undefined,
    );
  });

  it("builds query strings for world event steps", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            items: [],
            next_cursor: "3",
            has_more: true,
            limit: 10,
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(
      getWorldEventSteps({ from_tick: 2, to_tick: 4, cursor: "6", limit: 10 }),
    ).resolves.toEqual({
      items: [],
      next_cursor: "3",
      has_more: true,
      limit: 10,
    });
    expect(fetchMock).toHaveBeenCalledWith(
      "http://localhost:8000/world/event-steps?from_tick=2&to_tick=4&cursor=6&limit=10",
      undefined,
    );
  });

  it("loads world params", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            counter: {
              increment: 2,
            },
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(getWorldParams()).resolves.toEqual({
      counter: {
        increment: 2,
      },
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/world/params", undefined);
  });

  it("posts params patches", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            heartbeat: {
              enabled: false,
            },
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(
      applyWorldParams({
        patches: [
          {
            op: "set",
            path: "heartbeat.enabled",
            value: false,
          },
        ],
      }),
    ).resolves.toEqual({
      heartbeat: {
        enabled: false,
      },
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/world/params/apply", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        patches: [
          {
            op: "set",
            path: "heartbeat.enabled",
            value: false,
          },
        ],
      }),
    });
  });

  it("posts generation preview requests", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            request_id: "dashboard-preview",
            source_kind: "template",
            validation_status: "passed",
            metadata: {
              generation_id: "generation-123",
              request_id: "dashboard-preview",
              source_kind: "template",
              seed_digest: "abc",
              validation_status: "passed",
              diagnostics_count: 0,
              preview_summary: { total_cell_count: 2 },
            },
            diagnostics: [],
            worldspec_preview: { id: "worldspec-1", root: { id: "root", child_cells: [] } },
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    const body = {
      request_id: "dashboard-preview",
      source_kind: "template" as const,
      template_request: {
        request_id: "dashboard-preview",
        template: {
          id: "template.dashboard",
          version: "1",
          root: {
            id: "root",
            label: "Root",
            entity_refs: [],
            child_cells: [],
            metadata: {},
          },
          metadata: {},
          constraints: {},
        },
        seed_material: { seed: "dashboard" },
        constraints: {},
      },
    };

    await expect(previewGeneration(body)).resolves.toMatchObject({
      request_id: "dashboard-preview",
      validation_status: "passed",
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/world/generation/preview", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
  });

  it("posts runtime-readiness requests", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            request_id: "readiness",
            validation_status: "passed",
            loader_passed: true,
            runtime_context_passed: true,
            does_not_mutate_runtime: true,
            runtime_context_summary: { root_cell_id: "root" },
            diagnostics: [],
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    const body = {
      request_id: "readiness",
      worldspec: { id: "worldspec-1", root: { id: "root", child_cells: [] } },
      source_label: "generation-123",
    };

    await expect(checkGenerationRuntimeReadiness(body)).resolves.toMatchObject({
      validation_status: "passed",
      loader_passed: true,
    });
    expect(fetchMock).toHaveBeenCalledWith(
      "http://localhost:8000/world/generation/runtime-readiness",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      },
    );
  });

  it("posts generation regeneration requests", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            request_id: "regen",
            validation_status: "passed",
            lineage: {
              lineage_id: "lineage-1",
              source_request_id: "dashboard-preview",
              regenerated_generation_id: "generation-regen",
              changed_fields: ["seed_material"],
            },
            preview: {
              request_id: "regen",
              source_kind: "template",
              validation_status: "passed",
              metadata: {
                generation_id: "generation-regen",
                request_id: "regen",
                source_kind: "template",
                seed_digest: "def",
                validation_status: "passed",
                diagnostics_count: 0,
                preview_summary: {},
              },
              diagnostics: [],
              worldspec_preview: { id: "worldspec-regen", root: { id: "root" } },
            },
            runtime_readiness: {
              request_id: "regen",
              validation_status: "passed",
              loader_passed: true,
              runtime_context_passed: true,
              does_not_mutate_runtime: true,
              runtime_context_summary: {},
              diagnostics: [],
            },
            diagnostics: [],
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    const body = {
      request_id: "regen",
      base_preview_request: {
        request_id: "dashboard-preview",
        source_kind: "template" as const,
        template_request: {
          request_id: "dashboard-preview",
          template: {
            id: "template.dashboard",
            version: "1",
            root: { id: "root", entity_refs: [], child_cells: [], metadata: {} },
            metadata: {},
            constraints: {},
          },
        },
      },
      seed_material: { seed: "next" },
    };

    await expect(regenerateWorld(body)).resolves.toMatchObject({
      request_id: "regen",
      validation_status: "passed",
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/world/generation/regenerate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
  });

  it("throws fallback error for non-json responses", async () => {
    fetchMock.mockResolvedValue(
      new Response("server unavailable", {
        status: 503,
        headers: { "Content-Type": "text/plain" },
      }),
    );

    await expect(fetchHealth()).rejects.toMatchObject({
      name: "ApiClientError",
      message: "Request failed: 503",
      status: 503,
      code: 503,
    });
  });
});

import { afterEach, describe, expect, it, vi } from "vitest";

import {
  applyWorldParams,
  ApiClientError,
  checkGenerationRuntimeReadiness,
  fetchHealth,
  previewGeneration,
  regenerateWorld,
  getWorldEventSteps,
  getWorldParams,
  getWorldEvents,
  getRuntimeState,
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

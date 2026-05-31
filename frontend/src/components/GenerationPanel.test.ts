import { flushPromises, mount } from "@vue/test-utils";
import { describe, expect, it, vi } from "vitest";

import { ApiClientError } from "../api/client";
import GenerationPanel from "./GenerationPanel.vue";

const { previewGenerationMock, readinessMock } = vi.hoisted(() => ({
  previewGenerationMock: vi.fn(),
  readinessMock: vi.fn(),
}));

vi.mock("../api/client", async (importOriginal) => {
  const actual = await importOriginal<typeof import("../api/client")>();
  return {
    ...actual,
    previewGeneration: previewGenerationMock,
    checkGenerationRuntimeReadiness: readinessMock,
  };
});

function previewResponse() {
  return {
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
      preview_summary: {
        root_world_id: "worldspec-123",
        root_label: "Root",
        total_cell_count: 2,
        max_child_depth: 2,
        entity_ref_count: 0,
      },
    },
    diagnostics: [],
    worldspec_preview: {
      schema_version: "0.2",
      id: "worldspec-123",
      label: "Root",
      root: {
        id: "root",
        label: "Root",
        kind: "world",
        entity_refs: [],
        child_cells: [],
        metadata: {},
      },
      metadata: {},
    },
  };
}

describe("GenerationPanel", () => {
  it("submits a generic preview and renders readiness metadata", async () => {
    previewGenerationMock.mockResolvedValue(previewResponse());
    readinessMock.mockResolvedValue({
      request_id: "dashboard-preview",
      validation_status: "passed",
      loader_passed: true,
      runtime_context_passed: true,
      does_not_mutate_runtime: true,
      runtime_context_summary: { root_cell_id: "root" },
      diagnostics: [],
    });

    const wrapper = mount(GenerationPanel);
    await wrapper.get("[data-test='generation-root-label-input']").setValue("Operator Root");
    await wrapper.get("[data-test='generation-preview-submit']").trigger("click");
    await flushPromises();

    expect(previewGenerationMock).toHaveBeenCalledWith(
      expect.objectContaining({
        request_id: "dashboard-preview",
        source_kind: "template",
      }),
    );
    expect(readinessMock).toHaveBeenCalledWith({
      request_id: "dashboard-preview",
      worldspec: previewResponse().worldspec_preview,
      source_label: "generation-123",
    });
    expect(wrapper.get("[data-test='generation-validation-status']").text()).toContain("passed");
    expect(wrapper.get("[data-test='generation-id']").text()).toContain("generation-123");
    expect(wrapper.get("[data-test='generation-summary']").text()).toContain("total_cell_count");
    expect(wrapper.get("[data-test='generation-readiness-status']").text()).toContain("passed");
  });

  it("renders generation diagnostics without running readiness", async () => {
    previewGenerationMock.mockResolvedValue({
      ...previewResponse(),
      validation_status: "failed",
      worldspec_preview: null,
      metadata: {
        ...previewResponse().metadata,
        validation_status: "failed",
        diagnostics_count: 1,
      },
      diagnostics: [
        {
          code: "duplicate_cell_id",
          severity: "error",
          message: "duplicate cell id",
          path: "/root/id",
          source_context: {},
        },
      ],
    });

    const wrapper = mount(GenerationPanel);
    await wrapper.get("[data-test='generation-preview-submit']").trigger("click");
    await flushPromises();

    expect(readinessMock).not.toHaveBeenCalled();
    expect(wrapper.get("[data-test='generation-validation-status']").text()).toContain("failed");
    expect(wrapper.get("[data-test='generation-diagnostics']").text()).toContain("duplicate_cell_id");
    expect(wrapper.find("[data-test='generation-readiness-status']").exists()).toBe(false);
  });

  it("renders readiness diagnostics after a passed preview", async () => {
    previewGenerationMock.mockResolvedValue(previewResponse());
    readinessMock.mockResolvedValue({
      request_id: "dashboard-preview",
      validation_status: "failed",
      loader_passed: true,
      runtime_context_passed: false,
      does_not_mutate_runtime: true,
      runtime_context_summary: null,
      diagnostics: [
        {
          code: "runtime_context_failed",
          severity: "error",
          message: "runtime context build failed",
          path: "/root",
          source_context: {},
        },
      ],
    });

    const wrapper = mount(GenerationPanel);
    await wrapper.get("[data-test='generation-preview-submit']").trigger("click");
    await flushPromises();

    expect(wrapper.get("[data-test='generation-readiness-status']").text()).toContain("failed");
    expect(wrapper.get("[data-test='generation-readiness-diagnostics']").text()).toContain(
      "runtime_context_failed",
    );
  });

  it("renders API errors", async () => {
    previewGenerationMock.mockRejectedValue(
      new ApiClientError("Validation failed", {
        status: 422,
        code: 30,
        data: { errors: [{ type: "extra_forbidden" }] },
      }),
    );

    const wrapper = mount(GenerationPanel);
    await wrapper.get("[data-test='generation-preview-submit']").trigger("click");
    await flushPromises();

    expect(wrapper.get("[data-test='generation-error']").text()).toContain("Validation failed");
  });
});

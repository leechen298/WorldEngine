import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import TimelinePanel from "./TimelinePanel.vue";

describe("TimelinePanel", () => {
  it("renders table details for module events", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        events: [
          {
            id: "evt-1",
            tick_id: 1,
            world_time_seconds: 600,
            type: "module.counter",
            source: "root.counter",
            payload: {
              module_path: "root.counter",
              counter: 1,
            },
            created_at: "2026-03-09T00:10:00+00:00",
          },
        ],
      },
    });

    expect(wrapper.text()).toContain("module.counter");
    expect(wrapper.text()).toContain("[root.counter]");
    expect(wrapper.text()).toContain("Page size");
  });

  it("renders counter values and current page state", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        events: [
          {
            id: "evt-counter",
            tick_id: 3,
            world_time_seconds: 1800,
            type: "module.counter",
            source: "root.counter",
            payload: {
              module_path: "root.counter",
              counter: 3,
            },
            created_at: "2026-03-09T00:30:00+00:00",
          },
        ],
        currentPage: 3,
      },
    });

    expect(wrapper.text()).toContain("counter=3");
    expect(wrapper.text()).toContain("Page 3");
    expect(wrapper.text()).toContain("Newest first");
  });

  it("keeps long timeline rows in the table markup", () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        events: [
          {
            id: "evt-2",
            tick_id: 2,
            world_time_seconds: 1200,
            type: "module.aggregate",
            source: "root",
            payload: {
              module_path: "root.really.long.module.path.that.should.wrap.cleanly",
            },
            created_at: "2026-03-09T00:20:00+00:00",
          },
        ],
      },
    });

    expect(wrapper.find(".timeline-table").exists()).toBe(true);
    expect(wrapper.text()).toContain("root.really.long.module.path.that.should.wrap.cleanly");
  });

  it("emits pagination and page-size change events", async () => {
    const wrapper = mount(TimelinePanel, {
      props: {
        events: [
          {
            id: "evt-4",
            tick_id: 4,
            world_time_seconds: 2400,
            type: "tick.advanced",
            source: "system",
            payload: {},
            created_at: "2026-03-09T00:40:00+00:00",
          },
        ],
        canPrevious: true,
        hasMore: true,
        pageSize: 20,
      },
    });

    await wrapper.get("[data-test='timeline-prev-page']").trigger("click");
    await wrapper.get("[data-test='timeline-next-page']").trigger("click");
    await wrapper.get("[data-test='timeline-page-size']").setValue("50");

    expect(wrapper.emitted("previous-page")).toHaveLength(1);
    expect(wrapper.emitted("next-page")).toHaveLength(1);
    expect(wrapper.emitted("page-size-change")).toEqual([[50]]);
  });
});

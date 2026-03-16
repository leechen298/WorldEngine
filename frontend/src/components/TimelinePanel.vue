<template>
  <a-card title="Timeline Panel">
    <template #extra>
      <label class="timeline-page-size-control">
        <span>Page size</span>
        <select
          data-test="timeline-page-size"
          class="timeline-page-size-select"
          :value="pageSize"
          @change="handlePageSizeChange"
        >
          <option v-for="option in pageSizeOptions" :key="option" :value="option">
            {{ option }} / page
          </option>
        </select>
      </label>
    </template>
    <a-spin :spinning="loading">
      <a-alert v-if="error" type="error" show-icon :message="error" />
      <a-empty v-else-if="steps.length === 0" description="No events yet." />
      <div v-else class="timeline-table-shell">
        <a-table
          class="timeline-table"
          :data-source="steps"
          :columns="columns"
          :pagination="false"
          :row-key="(record) => record.tick_id"
          size="small"
          :scroll="{ x: 960 }"
          :expanded-row-render="renderExpandedRow"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'tick_id'">
              <a-tag color="blue">#{{ record.tick_id }}</a-tag>
            </template>
            <template v-else-if="column.key === 'event_count'">
              <a-tag color="geekblue">{{ record.event_count }} events</a-tag>
            </template>
            <template v-else-if="column.key === 'summary'">
              <a-typography-text class="timeline-cell-text">
                {{ summarizeStep(record as WorldEventStep) }}
              </a-typography-text>
            </template>
            <template v-else-if="column.key === 'created_at'">
              <a-typography-text type="secondary">
                {{ record.created_at }}
              </a-typography-text>
            </template>
          </template>
        </a-table>

        <div class="timeline-pagination">
          <a-space wrap :size="[8, 8]">
            <a-button
              data-test="timeline-prev-page"
              :disabled="!canPrevious"
              @click="emit('previous-page')"
            >
              Previous
            </a-button>
            <a-button
              data-test="timeline-next-page"
              type="primary"
              ghost
              :disabled="!hasMore"
              @click="emit('next-page')"
            >
              Next
            </a-button>
            <a-typography-text type="secondary">
              Page {{ currentPage }}
            </a-typography-text>
            <a-typography-text type="secondary">
              Newest first
            </a-typography-text>
          </a-space>
        </div>
      </div>
    </a-spin>
  </a-card>
</template>

<script setup lang="ts">
import { h, toRefs } from "vue";
import {
  Alert as AAlert,
  Button as AButton,
  Card as ACard,
  Descriptions as ADescriptions,
  DescriptionsItem as ADescriptionsItem,
  Divider as ADivider,
  Empty as AEmpty,
  Space as ASpace,
  Spin as ASpin,
  Table as ATable,
  Tag as ATag,
  TypographyText as ATypographyText,
} from "ant-design-vue";
import type { WorldEvent, WorldEventStep } from "../api/client";

const props = withDefaults(
  defineProps<{
    steps: WorldEventStep[];
    loading?: boolean;
    error?: string;
    pageSize?: number;
    currentPage?: number;
    hasMore?: boolean;
    canPrevious?: boolean;
    pageSizeOptions?: number[];
  }>(),
  {
    loading: false,
    error: "",
    pageSize: 20,
    currentPage: 1,
    hasMore: false,
    canPrevious: false,
    pageSizeOptions: () => [20, 50, 100],
  },
);
const { canPrevious, currentPage, error, hasMore, loading, pageSize, pageSizeOptions, steps } =
  toRefs(props);

const emit = defineEmits<{
  (event: "next-page"): void;
  (event: "previous-page"): void;
  (event: "page-size-change", value: number): void;
}>();

const columns = [
  {
    title: "Tick",
    dataIndex: "tick_id",
    key: "tick_id",
    width: 96,
  },
  {
    title: "Events",
    dataIndex: "event_count",
    key: "event_count",
    width: 120,
  },
  {
    title: "Summary",
    key: "summary",
  },
  {
    title: "Updated At",
    dataIndex: "created_at",
    key: "created_at",
    width: 240,
  },
];

function formatDetails(event: WorldEvent): string {
  const detailParts: string[] = [];
  const modulePath = event.payload?.module_path;
  const summary = event.payload?.summary;
  const counter = event.payload?.counter;
  const patches = event.payload?.patches;
  const params = event.payload?.params;

  if (typeof modulePath === "string" && modulePath.length > 0) {
    detailParts.push(`[${modulePath}]`);
  }
  if (event.type === "module.counter" && counter !== undefined) {
    detailParts.push(`counter=${counter}`);
  }
  if (typeof summary === "string" && summary.length > 0) {
    detailParts.push(summary);
  }
  if (Array.isArray(patches) && patches.length > 0) {
    detailParts.push(`${patches.length} patch${patches.length > 1 ? "es" : ""}`);
  }
  if (params && typeof params === "object" && Object.keys(params).length > 0) {
    detailParts.push(`params=${JSON.stringify(params)}`);
  }
  if (detailParts.length > 0) {
    return detailParts.join(" | ");
  }

  const payloadKeys = Object.keys(event.payload ?? {});
  if (payloadKeys.length === 0) {
    return "-";
  }
  return JSON.stringify(event.payload);
}

function summarizeStep(step: WorldEventStep): string {
  const typeCounts = new Map<string, number>();

  for (const item of step.items) {
    typeCounts.set(item.type, (typeCounts.get(item.type) ?? 0) + 1);
  }

  return (
    Array.from(typeCounts.entries())
      .map(([type, count]) => `${type} x${count}`)
      .join(" | ") || "-"
  );
}

function renderExpandedRow({ record }: { record: WorldEventStep }) {
  const step = record;
  return h("div", { class: "timeline-step-details" }, [
    h(
      ADescriptions,
      {
        size: "small",
        column: 3,
        bordered: true,
      },
      {
        default: () => [
          h(ADescriptionsItem, { label: "Tick" }, () => `#${step.tick_id}`),
          h(ADescriptionsItem, { label: "World Time" }, () => String(step.world_time_seconds)),
          h(ADescriptionsItem, { label: "Events" }, () => String(step.event_count)),
        ],
      },
    ),
    h(ADivider, { style: "margin: 12px 0" }),
    ...step.items.map((item) =>
      h("div", { class: "timeline-step-event", key: item.id }, [
        h("div", { class: "timeline-step-event-header" }, [
          h(ATag, { color: item.type === "tick.advanced" ? "blue" : "default" }, () => item.type),
          h(ATypographyText, { code: true }, () => item.source),
          h(ATypographyText, { type: "secondary" }, () => item.created_at),
        ]),
        h(ATypographyText, { class: "timeline-cell-text" }, () => formatDetails(item)),
      ]),
    ),
  ]);
}

function handlePageSizeChange(rawEvent: Event): void {
  const target = rawEvent.target as HTMLSelectElement | null;
  const nextValue = Number(target?.value);
  if (Number.isFinite(nextValue) && nextValue > 0) {
    emit("page-size-change", nextValue);
  }
}

defineExpose({
  formatDetails,
  summarizeStep,
});
</script>

<style scoped>
.timeline-page-size-control {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: #526072;
}

.timeline-page-size-select {
  min-width: 108px;
  padding: 4px 8px;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  background: #fff;
}

.timeline-table-shell {
  display: grid;
  gap: 12px;
}

.timeline-pagination {
  display: flex;
  justify-content: flex-end;
}

.timeline-cell-text {
  white-space: normal;
}

.timeline-step-details {
  display: grid;
  gap: 8px;
}

.timeline-step-event {
  display: grid;
  gap: 6px;
  padding: 8px 0;
}

.timeline-step-event + .timeline-step-event {
  border-top: 1px solid #f0f0f0;
}

.timeline-step-event-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}

.timeline-table :deep(.ant-table-cell) {
  vertical-align: top;
  overflow-wrap: anywhere;
  word-break: break-word;
}
</style>

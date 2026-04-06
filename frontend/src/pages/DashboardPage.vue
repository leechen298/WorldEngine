<template>
  <main class="dashboard-shell">
    <section class="dashboard">
      <header class="dashboard-header">
        <div>
          <a-typography-title :level="1">WorldEngine Dashboard</a-typography-title>
          <a-typography-paragraph class="dashboard-subtitle">
            Runtime overview, event timeline, and world parameter controls.
          </a-typography-paragraph>
        </div>
      </header>

      <a-row :gutter="[16, 16]" class="dashboard-status-row">
        <a-col :xs="24" :lg="12">
          <a-card title="Backend Health" class="status-card">
            <a-spin :spinning="loading">
              <a-alert v-if="error" type="error" show-icon :message="error" />
              <a-descriptions v-else :column="1" size="small" bordered>
                <a-descriptions-item label="Status">
                  {{ health?.status ?? "-" }}
                </a-descriptions-item>
                <a-descriptions-item label="Service">
                  {{ health?.service ?? "-" }}
                </a-descriptions-item>
              </a-descriptions>
            </a-spin>
          </a-card>
        </a-col>

        <a-col :xs="24" :lg="12">
          <a-card title="Runtime State" class="status-card">
            <a-spin :spinning="runtimeLoading">
              <a-alert v-if="runtimeError" type="error" show-icon :message="runtimeError" />
              <a-descriptions v-else :column="1" size="small" bordered>
                <a-descriptions-item label="tick_id">
                  {{ runtime?.tick_id ?? "-" }}
                </a-descriptions-item>
                <a-descriptions-item label="world_time_seconds">
                  {{ runtime?.world_time_seconds ?? "-" }}
                </a-descriptions-item>
                <a-descriptions-item label="step_seconds">
                  {{ runtime?.step_seconds ?? "-" }}
                </a-descriptions-item>
                <a-descriptions-item label="updated_at">
                  {{ runtime?.updated_at ?? "-" }}
                </a-descriptions-item>
              </a-descriptions>
            </a-spin>
          </a-card>
        </a-col>
      </a-row>

      <section class="panel-grid">
        <RuntimeControls class="panel-grid-full" @stepped="handleRuntimeStepped" />
        <TimelinePanel
          class="panel-grid-full"
          :steps="eventSteps"
          :loading="eventsLoading"
          :error="eventsError"
          :page-size="eventsPageSize"
          :current-page="eventsCurrentPage"
          :has-more="eventsHasMore"
          :can-previous="canLoadPreviousEvents"
          @next-page="handleNextEventsPage"
          @previous-page="handlePreviousEventsPage"
          @page-size-change="handleEventsPageSizeChange"
        />
        <WorldPanel
          class="panel-grid-full"
          :params="worldParams"
          :loading="worldParamsLoading"
          :error="worldParamsError"
          @applied="handleParamsApplied"
        />
        <AgentPanel />
        <MemoryPanel
          :summary="latestSummary"
          :loading="summaryLoading"
          :error="summaryError"
        />
      </section>
    </section>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import {
  Alert as AAlert,
  Card as ACard,
  Col as ACol,
  Descriptions as ADescriptions,
  DescriptionsItem as ADescriptionsItem,
  Row as ARow,
  Spin as ASpin,
  TypographyParagraph as ATypographyParagraph,
  TypographyTitle as ATypographyTitle,
} from "ant-design-vue";
import {
  getWorldParams,
  getWorldSummaries,
  fetchHealth,
  getWorldEventSteps,
  getRuntimeState,
  type HealthResponse,
  type RuntimeState,
  type WorldEventStep,
  type WorldParams,
  type WorldSummary,
} from "../api/client";
import RuntimeControls from "../components/RuntimeControls.vue";
import TimelinePanel from "../components/TimelinePanel.vue";
import WorldPanel from "../components/WorldPanel.vue";
import AgentPanel from "../components/AgentPanel.vue";
import MemoryPanel from "../components/MemoryPanel.vue";

const DEFAULT_EVENTS_PAGE_SIZE = 20;

const health = ref<HealthResponse | null>(null);
const loading = ref<boolean>(true);
const error = ref<string>("");
const runtime = ref<RuntimeState | null>(null);
const runtimeLoading = ref<boolean>(true);
const runtimeError = ref<string>("");
const eventSteps = ref<WorldEventStep[]>([]);
const eventsLoading = ref<boolean>(true);
const eventsError = ref<string>("");
const eventsPageSize = ref<number>(DEFAULT_EVENTS_PAGE_SIZE);
const eventsCurrentCursor = ref<string | null>(null);
const eventsCursorHistory = ref<Array<string | null>>([]);
const eventsNextCursor = ref<string | null>(null);
const eventsHasMore = ref<boolean>(false);
const worldParams = ref<WorldParams>({});
const worldParamsLoading = ref<boolean>(true);
const worldParamsError = ref<string>("");
const latestSummary = ref<WorldSummary | null>(null);
const summaryLoading = ref<boolean>(true);
const summaryError = ref<string>("");

const eventsCurrentPage = computed(() => eventsCursorHistory.value.length + 1);
const canLoadPreviousEvents = computed(() => eventsCursorHistory.value.length > 0);

async function loadRuntimeState(): Promise<void> {
  try {
    runtime.value = await getRuntimeState();
    runtimeError.value = "";
  } catch (err) {
    runtimeError.value = err instanceof Error ? err.message : "Unknown error";
  } finally {
    runtimeLoading.value = false;
  }
}

async function loadEvents(cursor: string | null = eventsCurrentCursor.value): Promise<boolean> {
  try {
    const page = await getWorldEventSteps({
      cursor: cursor ?? undefined,
      limit: eventsPageSize.value,
    });
    eventSteps.value = page.items;
    eventsNextCursor.value = page.next_cursor ?? null;
    eventsHasMore.value = page.has_more;
    eventsCurrentCursor.value = cursor;
    eventsError.value = "";
    return true;
  } catch (err) {
    eventsError.value = err instanceof Error ? err.message : "Unknown error";
    return false;
  } finally {
    eventsLoading.value = false;
  }
}

async function loadWorldParams(): Promise<void> {
  try {
    worldParams.value = await getWorldParams();
    worldParamsError.value = "";
  } catch (err) {
    worldParamsError.value = err instanceof Error ? err.message : "Unknown error";
  } finally {
    worldParamsLoading.value = false;
  }
}

async function loadLatestSummary(): Promise<void> {
  try {
    const result = await getWorldSummaries({ limit: 1, order: "desc" });
    latestSummary.value = result.items.length > 0 ? result.items[0] : null;
    summaryError.value = "";
  } catch (err) {
    summaryError.value = err instanceof Error ? err.message : "Unknown error";
  } finally {
    summaryLoading.value = false;
  }
}

function handleParamsApplied(nextParams: WorldParams): void {
  worldParams.value = nextParams;
  worldParamsError.value = "";
}

async function handleRuntimeStepped(): Promise<void> {
  runtimeLoading.value = true;
  eventsLoading.value = true;
  eventsCursorHistory.value = [];
  eventsCurrentCursor.value = null;
  eventsNextCursor.value = null;
  eventsHasMore.value = false;
  await Promise.all([loadRuntimeState(), loadEvents(null), loadLatestSummary()]);
}

async function handleNextEventsPage(): Promise<void> {
  if (!eventsHasMore.value || !eventsNextCursor.value) {
    return;
  }

  eventsLoading.value = true;
  const nextCursor = eventsNextCursor.value;
  const nextHistory = [...eventsCursorHistory.value, eventsCurrentCursor.value];
  const loaded = await loadEvents(nextCursor);
  if (loaded) {
    eventsCursorHistory.value = nextHistory;
  }
}

async function handlePreviousEventsPage(): Promise<void> {
  if (eventsCursorHistory.value.length === 0) {
    return;
  }

  eventsLoading.value = true;
  const nextHistory = eventsCursorHistory.value.slice(0, -1);
  const previousCursor = eventsCursorHistory.value[eventsCursorHistory.value.length - 1] ?? null;
  const loaded = await loadEvents(previousCursor);
  if (loaded) {
    eventsCursorHistory.value = nextHistory;
  }
}

async function handleEventsPageSizeChange(nextPageSize: number): Promise<void> {
  if (!Number.isFinite(nextPageSize) || nextPageSize <= 0 || nextPageSize === eventsPageSize.value) {
    return;
  }

  eventsPageSize.value = nextPageSize;
  eventsLoading.value = true;
  eventsCursorHistory.value = [];
  eventsCurrentCursor.value = null;
  eventsNextCursor.value = null;
  eventsHasMore.value = false;
  await loadEvents(null);
}

onMounted(async () => {
  try {
    health.value = await fetchHealth();
  } catch (err) {
    error.value = err instanceof Error ? err.message : "Unknown error";
  } finally {
    loading.value = false;
  }

  await loadRuntimeState();
  await loadEvents(null);
  await loadWorldParams();
  await loadLatestSummary();
});
</script>

<style scoped>
.dashboard-shell {
  min-height: 100vh;
  padding: 32px 20px 48px;
}

.dashboard-header {
  margin-bottom: 20px;
}

.dashboard-subtitle {
  max-width: 680px;
  margin-bottom: 0;
  color: #526072;
}

.dashboard-status-row {
  margin-bottom: 16px;
}

.status-card {
  height: 100%;
}

.panel-grid-full {
  grid-column: 1 / -1;
}
</style>

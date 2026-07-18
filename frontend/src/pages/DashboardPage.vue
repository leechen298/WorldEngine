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
                  <span data-test="backend-health-status">{{ health?.status ?? "-" }}</span>
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
                  <span data-test="runtime-tick-id">{{ runtime?.tick_id ?? "-" }}</span>
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

      <a-card title="MVP Session Flow" class="session-card">
        <a-space direction="vertical" :size="12" class="session-stack">
          <div class="session-create-row">
            <input
              v-model="sessionPremise"
              class="session-premise-input"
              data-test="session-premise-input"
              placeholder="Public worldview premise"
            />
            <a-button
              data-test="session-create-button"
              type="primary"
              :loading="sessionCreating"
              @click="handleCreateSession"
            >
              Create Session
            </a-button>
          </div>
          <a-alert v-if="sessionError" data-test="session-error" type="error" show-icon :message="sessionError" />

          <a-descriptions
            v-if="currentSession"
            data-test="session-summary"
            :column="1"
            size="small"
            bordered
          >
            <a-descriptions-item label="session_id">
              <span data-test="session-id">{{ currentSession.session_id }}</span>
            </a-descriptions-item>
            <a-descriptions-item label="world_id">
              {{ currentSession.world_id }}
            </a-descriptions-item>
            <a-descriptions-item label="status">
              <span data-test="session-status">{{ currentSession.status }}</span>
            </a-descriptions-item>
            <a-descriptions-item label="generation">
              <span data-test="session-generation-mode">
                {{ currentSession.generation_summary?.generation_mode ?? "-" }}
              </span>
            </a-descriptions-item>
            <a-descriptions-item label="runtime_tick">
              {{ currentSession.runtime_ref.tick_id }}
            </a-descriptions-item>
          </a-descriptions>

          <div v-if="currentSession" class="session-run-row">
            <input
              v-model.number="sessionRunTicks"
              class="session-run-input"
              data-test="session-run-ticks-input"
              min="1"
              max="100"
              type="number"
            />
            <a-button
              data-test="session-run-button"
              type="primary"
              :loading="sessionRunning"
              @click="handleRunSession"
            >
              Run
            </a-button>
            <a-button data-test="session-pause-button" :loading="sessionPausing" @click="handlePauseSession">
              Pause
            </a-button>
            <a-button data-test="session-resume-button" :loading="sessionResuming" @click="handleResumeSession">
              Resume
            </a-button>
          </div>

          <a-descriptions
            v-if="latestRunEvidence"
            data-test="session-run-evidence"
            :column="1"
            size="small"
            bordered
          >
            <a-descriptions-item label="ticks_executed">
              {{ latestRunEvidence.run_summary.ticks_executed }}
            </a-descriptions-item>
            <a-descriptions-item label="event_delta_count">
              {{ latestRunEvidence.event_evidence.event_delta_count }}
            </a-descriptions-item>
            <a-descriptions-item label="snapshot_delta_count">
              <span data-test="session-snapshot-delta">
                {{ latestRunEvidence.snapshot_evidence.snapshot_delta_count }}
              </span>
            </a-descriptions-item>
            <a-descriptions-item label="timeline">
              {{ latestRunEvidence.timeline_label }}
            </a-descriptions-item>
          </a-descriptions>

          <div v-if="sessionSnapshots" data-test="session-snapshot-list" class="session-snapshots">
            <div class="session-snapshot-heading">
              Snapshots: {{ sessionSnapshots.total }}
            </div>
            <ul>
              <li v-for="snapshot in sessionSnapshots.items" :key="snapshot.id">
                tick {{ snapshot.tick_id }} · {{ snapshot.id }}
              </li>
            </ul>
          </div>
        </a-space>
      </a-card>

      <section class="panel-grid">
        <RuntimeControls class="panel-grid-full" @stepped="handleRuntimeStepped" />
        <GenerationPanel class="panel-grid-full" />
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
  Button as AButton,
  Card as ACard,
  Col as ACol,
  Descriptions as ADescriptions,
  DescriptionsItem as ADescriptionsItem,
  Row as ARow,
  Spin as ASpin,
  Space as ASpace,
  TypographyParagraph as ATypographyParagraph,
  TypographyTitle as ATypographyTitle,
} from "ant-design-vue";
import {
  createSessionFromWorldview,
  getWorldParams,
  getWorldSummaries,
  fetchHealth,
  getWorldEventSteps,
  getRuntimeState,
  listSessionSnapshots,
  pauseSession,
  resumeSession,
  runSession,
  type SessionRunEvidenceResponse,
  type SessionSnapshotListResponse,
  type HealthResponse,
  type RuntimeState,
  type WorldSession,
  type WorldEventStep,
  type WorldParams,
  type WorldSummary,
} from "../api/client";
import RuntimeControls from "../components/RuntimeControls.vue";
import GenerationPanel from "../components/GenerationPanel.vue";
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
const sessionPremise = ref<string>("");
const sessionRunTicks = ref<number>(1);
const sessionCreating = ref<boolean>(false);
const sessionRunning = ref<boolean>(false);
const sessionPausing = ref<boolean>(false);
const sessionResuming = ref<boolean>(false);
const sessionError = ref<string>("");
const currentSession = ref<WorldSession | null>(null);
const latestRunEvidence = ref<SessionRunEvidenceResponse | null>(null);
const sessionSnapshots = ref<SessionSnapshotListResponse | null>(null);

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

async function refreshSessionSnapshots(): Promise<void> {
  if (!currentSession.value) {
    sessionSnapshots.value = null;
    return;
  }
  sessionSnapshots.value = await listSessionSnapshots(currentSession.value.session_id, {
    limit: 5,
    order: "desc",
  });
}

async function refreshDashboardEvidence(): Promise<void> {
  runtimeLoading.value = true;
  eventsLoading.value = true;
  eventsCursorHistory.value = [];
  eventsCurrentCursor.value = null;
  eventsNextCursor.value = null;
  eventsHasMore.value = false;
  await Promise.all([
    loadRuntimeState(),
    loadEvents(null),
    loadLatestSummary(),
    refreshSessionSnapshots(),
  ]);
}

async function handleCreateSession(): Promise<void> {
  const premise = sessionPremise.value.trim();
  if (!premise) {
    sessionError.value = "Worldview premise is required";
    return;
  }

  sessionCreating.value = true;
  sessionError.value = "";
  try {
    currentSession.value = await createSessionFromWorldview({
      request_id: `dashboard-session-${Date.now()}`,
      worldview_premise: premise,
      allow_deterministic_fallback: true,
    });
    latestRunEvidence.value = null;
    await refreshDashboardEvidence();
  } catch (err) {
    sessionError.value = err instanceof Error ? err.message : "Create session failed";
  } finally {
    sessionCreating.value = false;
  }
}

async function handleRunSession(): Promise<void> {
  if (!currentSession.value) {
    return;
  }

  sessionRunning.value = true;
  sessionError.value = "";
  try {
    const ticks = Math.max(1, Math.min(100, Number(sessionRunTicks.value) || 1));
    latestRunEvidence.value = await runSession(currentSession.value.session_id, {
      ticks,
      max_ticks: Math.max(ticks, 100),
    });
    currentSession.value = {
      ...currentSession.value,
      status: latestRunEvidence.value.run_summary.status === "completed" ? "ready" : currentSession.value.status,
      runtime_ref: {
        ...currentSession.value.runtime_ref,
        tick_id: latestRunEvidence.value.runtime_delta.end_tick,
        world_time_seconds: latestRunEvidence.value.runtime_delta.end_world_time_seconds,
      },
      evidence_refs: {
        ...currentSession.value.evidence_refs,
        current_event_count: latestRunEvidence.value.event_evidence.event_count_after,
        current_snapshot_count: latestRunEvidence.value.snapshot_evidence.snapshot_count_after,
      },
    };
    await refreshDashboardEvidence();
  } catch (err) {
    sessionError.value = err instanceof Error ? err.message : "Run session failed";
  } finally {
    sessionRunning.value = false;
  }
}

async function handlePauseSession(): Promise<void> {
  if (!currentSession.value) {
    return;
  }

  sessionPausing.value = true;
  sessionError.value = "";
  try {
    await pauseSession(currentSession.value.session_id);
    currentSession.value = { ...currentSession.value, status: "paused" };
  } catch (err) {
    sessionError.value = err instanceof Error ? err.message : "Pause session failed";
  } finally {
    sessionPausing.value = false;
  }
}

async function handleResumeSession(): Promise<void> {
  if (!currentSession.value) {
    return;
  }

  sessionResuming.value = true;
  sessionError.value = "";
  try {
    currentSession.value = await resumeSession(currentSession.value.session_id);
  } catch (err) {
    sessionError.value = err instanceof Error ? err.message : "Resume session failed";
  } finally {
    sessionResuming.value = false;
  }
}

async function handleRuntimeStepped(): Promise<void> {
  await refreshDashboardEvidence();
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

.session-card {
  margin-bottom: 16px;
}

.session-stack {
  width: 100%;
}

.session-create-row,
.session-run-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
}

.session-premise-input {
  min-width: 260px;
  flex: 1;
}

.session-run-input {
  width: 92px;
}

.session-premise-input,
.session-run-input {
  height: 32px;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  padding: 4px 11px;
  color: #102032;
}

.session-snapshots ul {
  margin: 6px 0 0;
  padding-left: 20px;
}

.session-snapshot-heading {
  font-weight: 600;
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

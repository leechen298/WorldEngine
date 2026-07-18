<template>
  <main class="runnable-anchor-shell">
    <div class="workbench">
      <header class="workbench-header">
        <div>
          <span class="product-label">WorldEngine · API V1</span>
          <h1>可运行锚点工作台</h1>
        </div>
        <div class="header-actions">
          <a-tag v-if="capabilities" data-test="capabilities-ready" color="green">
            {{ capabilities.contract_version }} · anchor
          </a-tag>
          <a-tag v-else color="default">能力清单未加载</a-tag>
          <a-button
            data-test="refresh-capabilities"
            :loading="capabilitiesLoading"
            @click="loadCapabilities"
          >
            刷新能力
          </a-button>
        </div>
      </header>

      <a-alert
        v-if="operationError"
        data-test="operation-error"
        class="operation-alert"
        type="error"
        show-icon
        :message="operationError"
      />
      <a-alert
        v-else-if="operationMessage"
        data-test="operation-message"
        class="operation-alert"
        type="success"
        show-icon
        :message="operationMessage"
      />

      <section v-if="capabilities" class="capability-surface" data-test="capability-manifest">
        <div class="capability-metrics">
          <div><span>Engine Build</span><strong data-test="engine-build">{{ capabilities.engine_build }}</strong></div>
          <div><span>Instance</span><strong>{{ capabilities.instance_id }}</strong></div>
          <div><span>Schema</span><strong>{{ capabilities.schema_version }}</strong></div>
          <div><span>State Hash</span><strong>{{ capabilities.state_hash_algorithm }}</strong></div>
          <div><span>公共操作</span><strong data-test="operation-count">{{ capabilities.operations.length }}</strong></div>
        </div>
        <details class="operation-manifest" data-test="capability-operations">
          <summary>公共操作清单</summary>
          <div class="operation-grid">
            <div v-for="operation in capabilities.operations" :key="operation.operation_id">
              <a-tag :color="operation.method === 'POST' ? 'gold' : 'blue'">{{ operation.method }}</a-tag>
              <code>{{ operation.operation_id }}</code>
              <span>{{ operation.path }}</span>
            </div>
          </div>
        </details>
      </section>

      <div class="workbench-grid">
        <aside class="control-rail">
          <section class="control-section" data-test="package-controls">
            <div class="section-heading">
              <span>01</span>
              <div><h2>确定性世界包</h2><small>WorldBrief → RunnableWorldPackage</small></div>
            </div>

            <label class="field-label" for="anchor-seed">Seed</label>
            <a-input id="anchor-seed" v-model:value="briefForm.seed" data-test="brief-seed" />

            <label class="field-label" for="anchor-premise">公开前提</label>
            <a-textarea
              id="anchor-premise"
              v-model:value="briefForm.premise"
              data-test="brief-premise"
              :auto-size="{ minRows: 2, maxRows: 4 }"
            />

            <div class="two-column-fields">
              <div>
                <label class="field-label" for="anchor-state-key">状态变量</label>
                <a-input id="anchor-state-key" v-model:value="briefForm.stateKey" data-test="state-key" />
              </div>
              <div>
                <label class="field-label" for="anchor-initial">初始值</label>
                <a-input-number
                  id="anchor-initial"
                  v-model:value="briefForm.initial"
                  data-test="state-initial"
                  :min="-1000"
                  :max="1000"
                />
              </div>
            </div>

            <div class="three-column-fields">
              <div>
                <label class="field-label" for="anchor-minimum">最小</label>
                <a-input-number id="anchor-minimum" v-model:value="briefForm.minimum" :min="-1000" :max="1000" />
              </div>
              <div>
                <label class="field-label" for="anchor-maximum">最大</label>
                <a-input-number id="anchor-maximum" v-model:value="briefForm.maximum" :min="-1000" :max="1000" />
              </div>
              <div>
                <label class="field-label" for="anchor-variable-step">步幅</label>
                <a-input-number id="anchor-variable-step" v-model:value="briefForm.variableStep" :min="1" :max="100" />
              </div>
            </div>

            <div class="two-column-fields">
              <div>
                <label class="field-label" for="anchor-step-seconds">Tick 秒数</label>
                <a-input-number
                  id="anchor-step-seconds"
                  v-model:value="briefForm.stepSeconds"
                  :min="0.1"
                  :max="3600"
                  :step="0.1"
                />
              </div>
              <div>
                <label class="field-label" for="anchor-constraints">约束 JSON</label>
                <a-input id="anchor-constraints" v-model:value="briefForm.constraintsText" />
              </div>
            </div>

            <a-button
              block
              data-test="generate-package"
              type="primary"
              :loading="busyOperation === 'package'"
              :disabled="isBusy"
              @click="handleGeneratePackage"
            >
              生成并校验哈希
            </a-button>

            <dl v-if="worldPackage" class="result-block" data-test="package-result">
              <div><dt>readiness</dt><dd data-test="package-readiness">{{ worldPackage.readiness.status }}</dd></div>
              <div><dt>package_id</dt><dd>{{ worldPackage.package_id }}</dd></div>
              <div class="result-wide"><dt>package_hash</dt><dd data-test="package-hash">{{ worldPackage.package_hash }}</dd></div>
              <div class="result-wide"><dt>确定性复算</dt><dd data-test="determinism-status">{{ determinismStatus }}</dd></div>
            </dl>
          </section>

          <section class="control-section" data-test="session-controls">
            <div class="section-heading">
              <span>02</span>
              <div><h2>会话与精确步进</h2><small>Session Boot · Lockstep</small></div>
            </div>

            <a-button
              block
              data-test="boot-session"
              :loading="busyOperation === 'boot'"
              :disabled="isBusy || worldPackage?.readiness.status !== 'ready'"
              @click="handleBootSession"
            >
              从当前 Hash 启动会话
            </a-button>

            <div class="inline-command">
              <div>
                <label class="field-label" for="anchor-step-count">精确步数</label>
                <a-input-number
                  id="anchor-step-count"
                  v-model:value="stepCount"
                  data-test="step-count"
                  :min="1"
                  :max="100"
                />
              </div>
              <a-button
                data-test="step-session"
                type="primary"
                :loading="busyOperation === 'step'"
                :disabled="isBusy || !session"
                @click="handleStepSession"
              >
                执行 Step N
              </a-button>
            </div>

            <dl v-if="session" class="result-block" data-test="session-result">
              <div class="result-wide"><dt>session_id</dt><dd data-test="session-id">{{ session.session_id }}</dd></div>
              <div><dt>initial_snapshot</dt><dd>{{ session.initial_snapshot_id }}</dd></div>
              <div><dt>source hash</dt><dd>{{ session.source_package_hash.slice(0, 16) }}…</dd></div>
            </dl>
            <dl v-if="latestStep" class="result-block" data-test="step-result">
              <div><dt>ticks</dt><dd data-test="step-range">{{ latestStep.start_tick }} → {{ latestStep.end_tick }}</dd></div>
              <div><dt>revisions</dt><dd>{{ latestStep.start_revision }} → {{ latestStep.end_revision }}</dd></div>
              <div><dt>events</dt><dd>{{ latestStep.event_refs.length }}</dd></div>
              <div><dt>snapshots</dt><dd>{{ latestStep.snapshot_refs.length }}</dd></div>
            </dl>
          </section>

          <section class="control-section" data-test="direction-controls">
            <div class="section-heading">
              <span>03</span>
              <div><h2>同窗口方向判定</h2><small>Accepted + Semantic Rejected</small></div>
            </div>

            <div class="two-column-fields">
              <div>
                <label class="field-label" for="anchor-direction-magnitude">有界压力</label>
                <a-input-number
                  id="anchor-direction-magnitude"
                  v-model:value="directionMagnitude"
                  data-test="direction-magnitude"
                  :min="-100"
                  :max="100"
                />
              </div>
              <div>
                <label class="field-label" for="anchor-final-value">直接最终值</label>
                <a-input-number
                  id="anchor-final-value"
                  v-model:value="directionFinalValue"
                  data-test="direction-final-value"
                  :min="-1000"
                  :max="1000"
                />
              </div>
            </div>

            <a-button
              block
              data-test="submit-direction-pair"
              :loading="busyOperation === 'directions'"
              :disabled="isBusy || !projection"
              @click="handleDirectionPair"
            >
              提交同窗口双判定
            </a-button>

            <div v-if="acceptedDirection || rejectedDirection" class="decision-grid">
              <div v-if="acceptedDirection" data-test="accepted-direction-result">
                <span>有界方向</span>
                <a-tag color="green">{{ acceptedDirection.status }}</a-tag>
                <code>{{ acceptedDirection.reason_code }}</code>
                <small>{{ acceptedDirection.window_id }}</small>
              </div>
              <div v-if="rejectedDirection" data-test="rejected-direction-result">
                <span>最终事实</span>
                <a-tag color="red">{{ rejectedDirection.status }}</a-tag>
                <code>{{ rejectedDirection.reason_code }}</code>
                <small>{{ rejectedDirection.window_id }}</small>
              </div>
            </div>
          </section>

          <section class="control-section" data-test="client-mutation-controls">
            <div class="section-heading">
              <span>04</span>
              <div><h2>客户端请求边界</h2><small>Generic Action · Typed Feedback</small></div>
            </div>

            <label class="field-label" for="anchor-action">Action</label>
            <a-select
              id="anchor-action"
              v-model:value="selectedActionId"
              data-test="action-select"
              :options="actionOptions"
              :disabled="!projection"
            />
            <div class="inline-command compact">
              <div>
                <label class="field-label" for="anchor-action-amount">Amount</label>
                <a-input-number
                  id="anchor-action-amount"
                  v-model:value="actionAmount"
                  data-test="action-amount"
                  :min="-100"
                  :max="100"
                />
              </div>
              <a-button
                data-test="submit-action"
                :loading="busyOperation === 'action'"
                :disabled="isBusy || !projection || !selectedActionId"
                @click="handleSubmitAction"
              >
                提交 Action
              </a-button>
            </div>

            <div v-if="latestAction" class="mutation-receipt" data-test="action-result">
              <a-tag :color="latestAction.status === 'accepted' ? 'green' : 'red'">{{ latestAction.status }}</a-tag>
              <code>{{ latestAction.reason_code }}</code>
              <span>{{ latestAction.applied_diff_refs.length }} diff</span>
            </div>

            <label class="field-label feedback-label" for="anchor-feedback-type">Feedback Type</label>
            <a-select
              id="anchor-feedback-type"
              v-model:value="selectedFeedbackType"
              data-test="feedback-type"
              :options="feedbackTypeOptions"
              :disabled="!worldPackage"
            />
            <label class="field-label" for="anchor-feedback-summary">公开摘要</label>
            <a-input
              id="anchor-feedback-summary"
              v-model:value="feedbackSummary"
              data-test="feedback-summary"
            />
            <a-button
              block
              data-test="submit-feedback"
              :loading="busyOperation === 'feedback'"
              :disabled="isBusy || !projection || !selectedFeedbackType"
              @click="handleSubmitFeedback"
            >
              提交 Typed Feedback
            </a-button>

            <div v-if="latestFeedback" class="mutation-receipt" data-test="feedback-result">
              <a-tag :color="latestFeedback.status === 'accepted' ? 'green' : 'red'">{{ latestFeedback.status }}</a-tag>
              <code>{{ latestFeedback.reason_code }}</code>
              <span>{{ latestFeedback.applied_diff_refs.length }} diff</span>
            </div>
          </section>
        </aside>

        <section class="inspection-column">
          <ProjectionPanel :projection="projection" />
          <EvidencePanel
            :event-page="eventPage"
            :evidence="evidence"
            :loading="refreshingCanonical"
            @refresh="handleRefreshCanonical"
            @download="handleDownloadEvidence"
          />
        </section>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, reactive, ref } from "vue";
import {
  Alert as AAlert,
  Button as AButton,
  Input as AInput,
  InputNumber as AInputNumber,
  Select as ASelect,
  Tag as ATag,
  Textarea as ATextarea,
} from "ant-design-vue";
import {
  EngineV1ApiError,
  createWorldPackage,
  createWorldSession,
  exportSessionEvidence,
  getEngineCapabilities,
  getPublicProjection,
  getWorldPackage,
  getWorldSession,
  pollWorldEvents,
  stepWorldSession,
  submitWorldAction,
  submitWorldDirection,
  submitWorldFeedback,
  type ActionResult,
  type CapabilityManifest,
  type DirectionDecision,
  type EventPage,
  type EvidenceBundle,
  type FeedbackResult,
  type PublicProjection,
  type RunnableWorldPackage,
  type SessionStepResult,
  type WorldBrief,
  type WorldSessionView,
} from "../api/engineV1";
import EvidencePanel from "../components/runnable-anchor/EvidencePanel.vue";
import ProjectionPanel from "../components/runnable-anchor/ProjectionPanel.vue";

type BusyOperation = "package" | "boot" | "step" | "directions" | "action" | "feedback";

const capabilities = ref<CapabilityManifest | null>(null);
const capabilitiesLoading = ref(false);
const worldPackage = ref<RunnableWorldPackage | null>(null);
const determinismStatus = ref("");
const session = ref<WorldSessionView | null>(null);
const projection = ref<PublicProjection | null>(null);
const eventPage = ref<EventPage | null>(null);
const evidence = ref<EvidenceBundle | null>(null);
const latestStep = ref<SessionStepResult | null>(null);
const acceptedDirection = ref<DirectionDecision | null>(null);
const rejectedDirection = ref<DirectionDecision | null>(null);
const latestAction = ref<ActionResult | null>(null);
const latestFeedback = ref<FeedbackResult | null>(null);
const operationError = ref("");
const operationMessage = ref("");
const busyOperation = ref<BusyOperation | null>(null);
const refreshingCanonical = ref(false);

const briefForm = reactive({
  seed: "anchor-seed-0130",
  premise: "一个由公开规则驱动、可按固定 tick 推进的通用世界。",
  constraintsText: "{}",
  stateKey: "world_signal",
  initial: 0,
  minimum: -100,
  maximum: 100,
  variableStep: 1,
  stepSeconds: 1,
});

const stepCount = ref(2);
const directionMagnitude = ref(1);
const directionFinalValue = ref(10);
const selectedActionId = ref("");
const actionAmount = ref(1);
const selectedFeedbackType = ref("");
const feedbackSummary = ref("客户端已观察到公开动作结果。" );

let requestSequence = 0;
const canonicalRefreshAttempts = 3;

const isBusy = computed(() => busyOperation.value !== null);

const actionOptions = computed(() => {
  const ids = projection.value?.allowed_actions ?? packageActionIds(worldPackage.value);
  return ids.map((actionId) => ({ label: actionId, value: actionId }));
});

const feedbackTypeOptions = computed(() =>
  packageFeedbackTypes(worldPackage.value).map((feedbackType) => ({
    label: feedbackType,
    value: feedbackType,
  })),
);

function nextRequestId(operation: string): string {
  requestSequence += 1;
  return `${operation}-${Date.now().toString(36)}-${requestSequence}`;
}

function buildBrief(): WorldBrief {
  const constraints = JSON.parse(briefForm.constraintsText) as unknown;
  if (!constraints || typeof constraints !== "object" || Array.isArray(constraints)) {
    throw new Error("约束 JSON 必须是对象。" );
  }
  if (!briefForm.stateKey.trim()) {
    throw new Error("状态变量不能为空。" );
  }
  return {
    seed: briefForm.seed.trim(),
    premise: briefForm.premise.trim(),
    constraints: constraints as Record<string, unknown>,
    state_variables: [
      {
        key: briefForm.stateKey.trim(),
        initial: briefForm.initial,
        minimum: briefForm.minimum,
        maximum: briefForm.maximum,
        step: briefForm.variableStep,
      },
    ],
    agent_count: 1,
    step_seconds: briefForm.stepSeconds,
  };
}

function packageActionIds(value: RunnableWorldPackage | null): string[] {
  if (!value) {
    return [];
  }
  return value.action_catalog.flatMap((item) =>
    typeof item.action_id === "string" ? [item.action_id] : [],
  );
}

function packageFeedbackTypes(value: RunnableWorldPackage | null): string[] {
  const raw = value?.projection_manifest.allowed_feedback_types;
  return Array.isArray(raw) ? raw.filter((item): item is string => typeof item === "string") : [];
}

function actionTarget(actionId: string): string {
  const catalogItem = worldPackage.value?.action_catalog.find(
    (item) => item.action_id === actionId,
  );
  if (typeof catalogItem?.target_ref === "string") {
    return catalogItem.target_ref;
  }
  return worldPackage.value?.brief.state_variables[0]?.key ?? briefForm.stateKey;
}

function syncPackageInputs(value: RunnableWorldPackage): void {
  const actions = packageActionIds(value);
  const feedbackTypes = packageFeedbackTypes(value);
  if (!actions.includes(selectedActionId.value)) {
    selectedActionId.value = actions[0] ?? "";
  }
  if (!feedbackTypes.includes(selectedFeedbackType.value)) {
    selectedFeedbackType.value = feedbackTypes[0] ?? "";
  }
}

function clearNotice(): void {
  operationError.value = "";
  operationMessage.value = "";
}

function readReasonCode(data: unknown): string | null {
  if (!data || typeof data !== "object" || Array.isArray(data)) {
    return null;
  }
  const reasonCode = (data as Record<string, unknown>).reason_code;
  return typeof reasonCode === "string" ? reasonCode : null;
}

function errorText(error: unknown): string {
  if (error instanceof EngineV1ApiError) {
    const reasonCode = readReasonCode(error.data);
    return reasonCode ? `${error.message} (${reasonCode})` : error.message;
  }
  if (error instanceof Error) {
    return error.message;
  }
  return "未知错误";
}

function sameCanonicalHead(left: PublicProjection, right: PublicProjection): boolean {
  return (
    left.session_id === right.session_id &&
    left.tick === right.tick &&
    left.revision === right.revision &&
    left.state_hash === right.state_hash &&
    left.event_cursor === right.event_cursor
  );
}

async function pollAllEvents(sessionId: string): Promise<EventPage> {
  const items: EventPage["items"] = [];
  let cursor = 0;
  for (let pageIndex = 0; pageIndex < 1000; pageIndex += 1) {
    const page = await pollWorldEvents(sessionId, {
      afterSequence: cursor,
      limit: 200,
    });
    items.push(...page.items);
    if (!page.has_more) {
      return {
        session_id: page.session_id,
        after_sequence: 0,
        items,
        next_sequence: page.next_sequence,
        has_more: false,
      };
    }
    if (page.next_sequence <= cursor) {
      throw new Error("事件游标没有继续推进。" );
    }
    cursor = page.next_sequence;
  }
  throw new Error("事件轮询超过管理端安全页数。" );
}

function canonicalViewsMatch(
  headBefore: PublicProjection,
  headAfter: PublicProjection,
  serverSession: WorldSessionView,
  serverEvents: EventPage,
  serverEvidence: EvidenceBundle,
): boolean {
  return (
    sameCanonicalHead(headBefore, headAfter) &&
    sameCanonicalHead(serverSession.projection, headAfter) &&
    sameCanonicalHead(serverEvidence.projection, headAfter) &&
    serverSession.session_id === headAfter.session_id &&
    serverEvents.session_id === headAfter.session_id &&
    serverEvents.next_sequence === headAfter.event_cursor &&
    serverSession.source_package_hash === headAfter.source_package_hash &&
    serverEvidence.package.package_hash === headAfter.source_package_hash
  );
}

async function loadCapabilities(): Promise<void> {
  capabilitiesLoading.value = true;
  try {
    capabilities.value = await getEngineCapabilities();
    operationError.value = "";
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    capabilitiesLoading.value = false;
  }
}

async function refreshCanonicalData(sessionId = session.value?.session_id): Promise<void> {
  if (!sessionId) {
    return;
  }
  refreshingCanonical.value = true;
  try {
    for (let attempt = 0; attempt < canonicalRefreshAttempts; attempt += 1) {
      const headBefore = await getPublicProjection(sessionId);
      const [serverSession, serverEvents, serverEvidence] = await Promise.all([
        getWorldSession(sessionId),
        pollAllEvents(sessionId),
        exportSessionEvidence(sessionId),
      ]);
      const headAfter = await getPublicProjection(sessionId);
      if (
        !canonicalViewsMatch(
          headBefore,
          headAfter,
          serverSession,
          serverEvents,
          serverEvidence,
        )
      ) {
        continue;
      }
      session.value = serverSession;
      projection.value = headAfter;
      eventPage.value = serverEvents;
      evidence.value = serverEvidence;
      if (!headAfter.allowed_actions.includes(selectedActionId.value)) {
        selectedActionId.value = headAfter.allowed_actions[0] ?? "";
      }
      return;
    }
    throw new Error("并发更新期间未取得一致的服务端 revision，请重试。" );
  } finally {
    refreshingCanonical.value = false;
  }
}

async function handleGeneratePackage(): Promise<void> {
  clearNotice();
  busyOperation.value = "package";
  try {
    const brief = buildBrief();
    const [first, second] = await Promise.all([
      createWorldPackage({ request_id: nextRequestId("package-primary"), brief }),
      createWorldPackage({ request_id: nextRequestId("package-repeat"), brief }),
    ]);
    const fetched = await getWorldPackage(first.package_id);
    if (first.package_hash !== second.package_hash || first.package_hash !== fetched.package_hash) {
      throw new Error("相同 WorldBrief 的 package_hash 不一致。" );
    }
    worldPackage.value = fetched;
    determinismStatus.value = `通过 · ${first.package_hash === second.package_hash ? "2/2 hash 一致" : "不一致"}`;
    syncPackageInputs(fetched);
    session.value = null;
    projection.value = null;
    eventPage.value = null;
    evidence.value = null;
    latestStep.value = null;
    acceptedDirection.value = null;
    rejectedDirection.value = null;
    latestAction.value = null;
    latestFeedback.value = null;
    operationMessage.value = "世界包已生成，并由服务端读取结果完成确定性校验。";
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleBootSession(): Promise<void> {
  if (!worldPackage.value) {
    return;
  }
  clearNotice();
  busyOperation.value = "boot";
  try {
    const created = await createWorldSession({
      request_id: nextRequestId("session-boot"),
      package_id: worldPackage.value.package_id,
      package_hash: worldPackage.value.package_hash,
    });
    session.value = created;
    await refreshCanonicalData(created.session_id);
    operationMessage.value = "会话已从当前 package_hash 启动，权威投影与证据已刷新。";
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleStepSession(): Promise<void> {
  if (!session.value || !projection.value) {
    return;
  }
  clearNotice();
  busyOperation.value = "step";
  try {
    latestStep.value = await stepWorldSession(session.value.session_id, {
      request_id: nextRequestId("session-step"),
      step_count: stepCount.value,
      expected_revision: projection.value.revision,
    });
    await refreshCanonicalData(session.value.session_id);
    operationMessage.value = `精确推进 ${latestStep.value.step_count} 个 tick，服务端投影与证据已刷新。`;
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleDirectionPair(): Promise<void> {
  if (!session.value || !projection.value) {
    return;
  }
  clearNotice();
  busyOperation.value = "directions";
  try {
    const sessionId = session.value.session_id;
    const windowId = projection.value.active_intervention_window.window_id;
    const targetRef = worldPackage.value?.brief.state_variables[0]?.key ?? briefForm.stateKey;
    acceptedDirection.value = await submitWorldDirection(sessionId, {
      request_id: nextRequestId("direction-bounded"),
      window_id: windowId,
      expected_revision: projection.value.revision,
      kind: "bounded_pressure",
      target_ref: targetRef,
      summary: "对公开状态变量施加有界压力。",
      magnitude: directionMagnitude.value,
    });
    await refreshCanonicalData(sessionId);
    if (projection.value?.active_intervention_window.window_id !== windowId) {
      throw new Error("服务端在同窗口双判定之间切换了干预窗口。" );
    }
    rejectedDirection.value = await submitWorldDirection(sessionId, {
      request_id: nextRequestId("direction-final-fact"),
      window_id: windowId,
      expected_revision: projection.value.revision,
      kind: "direct_final_fact",
      target_ref: targetRef,
      summary: "直接指定最终世界事实。",
      final_value: directionFinalValue.value,
    });
    await refreshCanonicalData(sessionId);
    if (
      acceptedDirection.value.window_id !== rejectedDirection.value.window_id ||
      acceptedDirection.value.status !== "accepted" ||
      rejectedDirection.value.status !== "rejected"
    ) {
      throw new Error("同窗口 accepted/rejected 判定不完整。" );
    }
    operationMessage.value = "同一干预窗口已记录有界方向接受与最终事实语义拒绝。";
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleSubmitAction(): Promise<void> {
  if (!session.value || !projection.value || !selectedActionId.value) {
    return;
  }
  clearNotice();
  busyOperation.value = "action";
  try {
    latestAction.value = await submitWorldAction(session.value.session_id, {
      request_id: nextRequestId("client-action"),
      expected_revision: projection.value.revision,
      action_id: selectedActionId.value,
      target_ref: actionTarget(selectedActionId.value),
      amount: actionAmount.value,
    });
    await refreshCanonicalData(session.value.session_id);
    operationMessage.value = "Action 已由 WorldEngine 规则判定，权威投影与证据已刷新。";
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleSubmitFeedback(): Promise<void> {
  if (!session.value || !projection.value || !selectedFeedbackType.value) {
    return;
  }
  clearNotice();
  busyOperation.value = "feedback";
  try {
    const evidenceEvents = evidence.value?.events ?? [];
    const relatedEventRef =
      latestAction.value?.event_ref ??
      (evidenceEvents.length > 0 ? evidenceEvents[evidenceEvents.length - 1].event_id : undefined);
    latestFeedback.value = await submitWorldFeedback(session.value.session_id, {
      request_id: nextRequestId("client-feedback"),
      expected_revision: projection.value.revision,
      feedback_type: selectedFeedbackType.value,
      summary: feedbackSummary.value,
      ...(relatedEventRef ? { related_event_ref: relatedEventRef } : {}),
    });
    await refreshCanonicalData(session.value.session_id);
    operationMessage.value = "Typed Feedback 已由 WorldEngine 接受或拒绝，权威证据已刷新。";
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleRefreshCanonical(): Promise<void> {
  clearNotice();
  try {
    await refreshCanonicalData();
    operationMessage.value = "投影、事件与证据已从服务端刷新。";
  } catch (error) {
    operationError.value = errorText(error);
  }
}

async function handleDownloadEvidence(): Promise<void> {
  if (!session.value) {
    return;
  }
  clearNotice();
  refreshingCanonical.value = true;
  try {
    const latestEvidence = await exportSessionEvidence(session.value.session_id);
    evidence.value = latestEvidence;
    const blob = new Blob([JSON.stringify(latestEvidence, null, 2)], {
      type: "application/json;charset=utf-8",
    });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = `${session.value.session_id}-evidence.json`;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    URL.revokeObjectURL(url);
    operationMessage.value = `证据已导出，完整性为 ${latestEvidence.completeness.status}。`;
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    refreshingCanonical.value = false;
  }
}

onMounted(() => {
  void loadCapabilities();
});
</script>

<style scoped>
.runnable-anchor-shell {
  min-height: 100vh;
  color: #17202a;
  background: #f2f4f7;
}

.workbench {
  width: min(1600px, 100%);
  margin: 0 auto;
  padding: 20px 24px 40px;
}

.workbench-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  min-height: 58px;
  padding-bottom: 14px;
  border-bottom: 1px solid #d0d5dd;
}

.product-label {
  display: block;
  margin-bottom: 2px;
  color: #667085;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0;
}

h1,
h2,
dl,
dd {
  margin: 0;
}

h1 {
  color: #101828;
  font-size: 24px;
  line-height: 1.3;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.operation-alert {
  margin-top: 12px;
}

.capability-surface {
  margin-top: 14px;
  border: 1px solid #d9dee5;
  border-radius: 6px;
  background: #ffffff;
}

.capability-metrics {
  display: grid;
  grid-template-columns: 1fr 1fr 1.2fr 1.2fr 0.55fr;
}

.capability-metrics div {
  min-width: 0;
  padding: 11px 14px;
  border-right: 1px solid #eaecf0;
}

.capability-metrics div:last-child {
  border-right: 0;
}

.capability-metrics span,
.capability-metrics strong {
  display: block;
}

.capability-metrics span {
  color: #667085;
  font-size: 10px;
}

.capability-metrics strong {
  overflow: hidden;
  margin-top: 2px;
  color: #344054;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 11px;
  font-weight: 600;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.operation-manifest {
  border-top: 1px solid #eaecf0;
}

.operation-manifest summary {
  padding: 9px 14px;
  color: #475467;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
}

.operation-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1px;
  padding: 1px;
  background: #eaecf0;
}

.operation-grid div {
  display: grid;
  grid-template-columns: 50px minmax(120px, 0.75fr) minmax(180px, 1.25fr);
  align-items: center;
  gap: 8px;
  min-width: 0;
  padding: 8px 10px;
  background: #ffffff;
}

.operation-grid code,
.operation-grid span {
  overflow: hidden;
  font-size: 10px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.operation-grid code {
  color: #344054;
}

.operation-grid span {
  color: #667085;
}

.workbench-grid {
  display: grid;
  grid-template-columns: minmax(340px, 390px) minmax(0, 1fr);
  align-items: start;
  gap: 16px;
  margin-top: 16px;
}

.control-rail {
  display: grid;
  gap: 12px;
}

.control-section {
  min-width: 0;
  padding: 16px;
  border: 1px solid #d9dee5;
  border-radius: 6px;
  background: #ffffff;
}

.section-heading {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 14px;
}

.section-heading > span {
  display: grid;
  width: 26px;
  height: 26px;
  place-items: center;
  border: 1px solid #98a2b3;
  border-radius: 3px;
  color: #475467;
  font-size: 11px;
  font-weight: 700;
}

.section-heading h2 {
  color: #1d2939;
  font-size: 15px;
  line-height: 1.3;
}

.section-heading small {
  display: block;
  margin-top: 2px;
  color: #667085;
  font-size: 10px;
}

.field-label {
  display: block;
  margin: 10px 0 5px;
  color: #475467;
  font-size: 11px;
  font-weight: 600;
}

.two-column-fields,
.three-column-fields {
  display: grid;
  gap: 8px;
}

.two-column-fields {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.three-column-fields {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.control-section :deep(.ant-input-number),
.control-section :deep(.ant-select) {
  width: 100%;
}

.control-section > :deep(.ant-btn-block) {
  margin-top: 14px;
}

.inline-command {
  display: grid;
  grid-template-columns: minmax(90px, 0.65fr) minmax(150px, 1.35fr);
  align-items: end;
  gap: 8px;
  margin-top: 10px;
}

.inline-command.compact {
  margin-top: 0;
}

.result-block {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 8px 12px;
  margin-top: 12px;
  padding: 10px;
  border-left: 3px solid #2f855a;
  background: #f4faf6;
}

.result-block div {
  min-width: 0;
}

.result-wide {
  grid-column: 1 / -1;
}

.result-block dt {
  color: #667085;
  font-size: 10px;
}

.result-block dd {
  overflow: hidden;
  margin-top: 2px;
  color: #344054;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 10px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.decision-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 8px;
  margin-top: 12px;
}

.decision-grid > div {
  min-width: 0;
  padding: 9px;
  border: 1px solid #e4e7ec;
  border-radius: 4px;
  background: #f8fafb;
}

.decision-grid span,
.decision-grid code,
.decision-grid small {
  display: block;
}

.decision-grid span {
  margin-bottom: 5px;
  color: #475467;
  font-size: 11px;
  font-weight: 600;
}

.decision-grid code {
  overflow: hidden;
  margin-top: 6px;
  color: #344054;
  font-size: 9px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.decision-grid small {
  overflow: hidden;
  margin-top: 3px;
  color: #98a2b3;
  font-size: 8px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.feedback-label {
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px solid #eaecf0;
}

.mutation-receipt {
  display: flex;
  align-items: center;
  gap: 6px;
  min-width: 0;
  margin-top: 10px;
  color: #667085;
  font-size: 10px;
}

.mutation-receipt code {
  overflow: hidden;
  color: #344054;
  font-size: 10px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.mutation-receipt span {
  flex: 0 0 auto;
}

.inspection-column {
  display: grid;
  min-width: 0;
  gap: 16px;
}

@media (max-width: 1260px) {
  .operation-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 1040px) {
  .workbench-grid {
    grid-template-columns: 1fr;
  }

  .control-rail {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 760px) {
  .workbench {
    padding: 14px 12px 28px;
  }

  .workbench-header {
    align-items: flex-start;
    flex-direction: column;
  }

  .capability-metrics,
  .control-rail,
  .operation-grid {
    grid-template-columns: 1fr;
  }

  .capability-metrics div,
  .capability-metrics div:last-child {
    border-right: 0;
    border-bottom: 1px solid #eaecf0;
  }

  .capability-metrics div:last-child {
    border-bottom: 0;
  }

  .operation-grid div {
    grid-template-columns: 50px minmax(100px, 0.8fr) minmax(150px, 1.2fr);
  }
}

@media (max-width: 440px) {
  .two-column-fields,
  .three-column-fields,
  .decision-grid {
    grid-template-columns: 1fr;
  }

  .result-wide {
    grid-column: auto;
  }
}
</style>

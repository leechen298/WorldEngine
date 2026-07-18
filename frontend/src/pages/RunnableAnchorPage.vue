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
        v-else-if="operationWarning"
        data-test="operation-warning"
        class="operation-alert"
        type="warning"
        show-icon
        :message="operationWarning"
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
            <a-input
              id="anchor-seed"
              v-model:value="briefForm.seed"
              data-test="brief-seed"
              :disabled="isBusy"
              :maxlength="128"
              :status="briefFieldErrors.seed ? 'error' : undefined"
            />
            <span v-if="briefFieldErrors.seed" class="field-error" data-test="brief-seed-error">
              {{ briefFieldErrors.seed }}
            </span>

            <label class="field-label" for="anchor-premise">公开前提</label>
            <a-textarea
              id="anchor-premise"
              v-model:value="briefForm.premise"
              data-test="brief-premise"
              :auto-size="{ minRows: 2, maxRows: 4 }"
              :disabled="isBusy"
              :maxlength="1000"
              :status="briefFieldErrors.premise ? 'error' : undefined"
            />
            <span
              v-if="briefFieldErrors.premise"
              class="field-error"
              data-test="brief-premise-error"
            >
              {{ briefFieldErrors.premise }}
            </span>

            <div class="two-column-fields">
              <div>
                <label class="field-label" for="anchor-state-key">状态变量</label>
                <a-input
                  id="anchor-state-key"
                  v-model:value="briefForm.stateKey"
                  data-test="state-key"
                  :disabled="isBusy"
                  :maxlength="64"
                  :status="briefFieldErrors.stateKey ? 'error' : undefined"
                />
                <span
                  v-if="briefFieldErrors.stateKey"
                  class="field-error"
                  data-test="state-key-error"
                >
                  {{ briefFieldErrors.stateKey }}
                </span>
              </div>
              <div>
                <label class="field-label" for="anchor-initial">初始值</label>
                <a-input-number
                  id="anchor-initial"
                  v-model:value="briefForm.initial"
                  data-test="state-initial"
                  :disabled="isBusy"
                  :precision="0"
                  :status="briefFieldErrors.initial ? 'error' : undefined"
                />
                <span
                  v-if="briefFieldErrors.initial"
                  class="field-error"
                  data-test="state-initial-error"
                >
                  {{ briefFieldErrors.initial }}
                </span>
              </div>
            </div>

            <div class="three-column-fields">
              <div>
                <label class="field-label" for="anchor-minimum">最小</label>
                <a-input-number
                  id="anchor-minimum"
                  v-model:value="briefForm.minimum"
                  data-test="state-minimum"
                  :disabled="isBusy"
                  :precision="0"
                  :status="briefFieldErrors.minimum ? 'error' : undefined"
                />
                <span
                  v-if="briefFieldErrors.minimum"
                  class="field-error"
                  data-test="state-minimum-error"
                >
                  {{ briefFieldErrors.minimum }}
                </span>
              </div>
              <div>
                <label class="field-label" for="anchor-maximum">最大</label>
                <a-input-number
                  id="anchor-maximum"
                  v-model:value="briefForm.maximum"
                  data-test="state-maximum"
                  :disabled="isBusy"
                  :precision="0"
                  :status="briefFieldErrors.maximum ? 'error' : undefined"
                />
                <span
                  v-if="briefFieldErrors.maximum"
                  class="field-error"
                  data-test="state-maximum-error"
                >
                  {{ briefFieldErrors.maximum }}
                </span>
              </div>
              <div>
                <label class="field-label" for="anchor-variable-step">步幅</label>
                <a-input-number
                  id="anchor-variable-step"
                  v-model:value="briefForm.variableStep"
                  data-test="state-step"
                  :disabled="isBusy"
                  :min="1"
                  :max="100"
                  :precision="0"
                  :status="briefFieldErrors.variableStep ? 'error' : undefined"
                />
                <span
                  v-if="briefFieldErrors.variableStep"
                  class="field-error"
                  data-test="state-step-error"
                >
                  {{ briefFieldErrors.variableStep }}
                </span>
              </div>
            </div>

            <div class="two-column-fields">
              <div>
                <label class="field-label" for="anchor-step-seconds">Tick 秒数</label>
                <a-input-number
                  id="anchor-step-seconds"
                  v-model:value="briefForm.stepSeconds"
                  data-test="step-seconds"
                  :disabled="isBusy"
                  :max="3600"
                  :step="0.1"
                  :status="briefFieldErrors.stepSeconds ? 'error' : undefined"
                />
                <span
                  v-if="briefFieldErrors.stepSeconds"
                  class="field-error"
                  data-test="step-seconds-error"
                >
                  {{ briefFieldErrors.stepSeconds }}
                </span>
              </div>
              <div>
                <label class="field-label" for="anchor-constraints">约束 JSON</label>
                <a-input
                  id="anchor-constraints"
                  v-model:value="briefForm.constraintsText"
                  data-test="brief-constraints"
                  :disabled="isBusy"
                  :status="briefFieldErrors.constraintsText ? 'error' : undefined"
                />
                <span
                  v-if="briefFieldErrors.constraintsText"
                  class="field-error"
                  data-test="brief-constraints-error"
                >
                  {{ briefFieldErrors.constraintsText }}
                </span>
              </div>
            </div>

            <a-button
              block
              data-test="generate-package"
              type="primary"
              :loading="busyOperation === 'package'"
              :disabled="isBusy || hasBriefErrors"
              @click="handleGeneratePackage"
            >
              生成并校验哈希
            </a-button>

            <dl v-if="worldPackage" class="result-block" data-test="package-result">
              <div><dt>readiness</dt><dd data-test="package-readiness">{{ worldPackage.readiness.status }}</dd></div>
              <div><dt>package_id</dt><dd>{{ worldPackage.package_id }}</dd></div>
              <div class="result-wide"><dt>package_hash</dt><dd data-test="package-hash">{{ worldPackage.package_hash }}</dd></div>
              <div class="result-wide"><dt>brief fingerprint</dt><dd data-test="brief-fingerprint">{{ generatedBriefFingerprintLabel }}</dd></div>
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
              :disabled="isBusy || !hasCurrentPackage"
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
                  :precision="0"
                />
              </div>
              <a-button
                data-test="step-session"
                type="primary"
                :loading="busyOperation === 'step'"
                :disabled="isBusy || !hasCurrentProjection"
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
              <div><h2>独立方向命令</h2><small>Bounded Pressure · Direct Final Fact</small></div>
            </div>

            <div class="direction-command">
              <div>
                <label class="field-label" for="anchor-direction-magnitude">有界压力</label>
                <a-input-number
                  id="anchor-direction-magnitude"
                  v-model:value="directionMagnitude"
                  data-test="direction-magnitude"
                  :min="-300"
                  :max="300"
                  :precision="0"
                />
              </div>
              <a-button
                block
                data-test="submit-bounded-direction"
                :loading="busyOperation === 'bounded-direction'"
                :disabled="isBusy || !hasCurrentProjection"
                @click="handleSubmitBoundedDirection"
              >
                提交有界压力命令
              </a-button>
              <div class="direction-receipt" data-test="accepted-direction-result">
                <span>有界压力状态</span>
                <a-tag :color="acceptedDirection?.status === 'accepted' ? 'green' : 'default'">
                  {{ acceptedDirection?.status ?? "未提交" }}
                </a-tag>
                <a-tag v-if="acceptedDirection" color="blue">
                  {{ acceptedDirection.application_status }}
                </a-tag>
                <code v-if="acceptedDirection">{{ acceptedDirection.reason_code }}</code>
                <code v-if="acceptedDirection?.application_reason_code">
                  {{ acceptedDirection.application_reason_code }}
                </code>
                <small v-if="acceptedDirection">{{ acceptedDirection.window_id }}</small>
              </div>
              <span
                v-if="boundedDirectionError"
                class="command-error"
                data-test="bounded-direction-error"
              >
                {{ boundedDirectionError }}
              </span>
            </div>

            <div class="direction-command">
              <div>
                <label class="field-label" for="anchor-final-value">直接最终值</label>
                <a-input-number
                  id="anchor-final-value"
                  v-model:value="directionFinalValue"
                  data-test="direction-final-value"
                  :precision="0"
                />
              </div>
              <a-button
                block
                data-test="submit-final-fact-direction"
                :loading="busyOperation === 'final-fact-direction'"
                :disabled="isBusy || !hasCurrentProjection"
                @click="handleSubmitFinalFactDirection"
              >
                提交最终事实命令
              </a-button>
              <div class="direction-receipt" data-test="rejected-direction-result">
                <span>最终事实状态</span>
                <a-tag :color="rejectedDirection?.status === 'rejected' ? 'red' : 'default'">
                  {{ rejectedDirection?.status ?? "未提交" }}
                </a-tag>
                <a-tag v-if="rejectedDirection" color="blue">
                  {{ rejectedDirection.application_status }}
                </a-tag>
                <code v-if="rejectedDirection">{{ rejectedDirection.reason_code }}</code>
                <code v-if="rejectedDirection?.application_reason_code">
                  {{ rejectedDirection.application_reason_code }}
                </code>
                <small v-if="rejectedDirection">{{ rejectedDirection.window_id }}</small>
              </div>
              <span
                v-if="finalFactDirectionError"
                class="command-error"
                data-test="final-fact-direction-error"
              >
                {{ finalFactDirectionError }}
              </span>
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
              :disabled="!hasCurrentProjection"
            />
            <div class="inline-command compact">
              <div>
                <label class="field-label" for="anchor-action-amount">Amount</label>
                <a-input-number
                  id="anchor-action-amount"
                  v-model:value="actionAmount"
                  data-test="action-amount"
                  :min="-300"
                  :max="300"
                  :precision="0"
                />
              </div>
              <a-button
                data-test="submit-action"
                :loading="busyOperation === 'action'"
                :disabled="isBusy || !hasCurrentProjection || !selectedActionId"
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
              :disabled="!hasCurrentProjection"
            />
            <label class="field-label" for="anchor-feedback-summary">公开摘要</label>
            <a-input
              id="anchor-feedback-summary"
              v-model:value="feedbackSummary"
              data-test="feedback-summary"
              :maxlength="500"
            />
            <a-button
              block
              data-test="submit-feedback"
              :loading="busyOperation === 'feedback'"
              :disabled="isBusy || !hasCurrentProjection || !selectedFeedbackType"
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
            :can-refresh="hasCurrentSession"
            @refresh="handleRefreshCanonical"
            @download="handleDownloadEvidence"
          />
        </section>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { computed, onMounted, reactive, ref, watch } from "vue";
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

type BusyOperation =
  | "package"
  | "boot"
  | "step"
  | "bounded-direction"
  | "final-fact-direction"
  | "action"
  | "feedback";

interface BriefFormState {
  seed: string;
  premise: string;
  constraintsText: string;
  stateKey: string;
  initial: number | undefined;
  minimum: number | undefined;
  maximum: number | undefined;
  variableStep: number | undefined;
  stepSeconds: number | undefined;
}

type BriefFieldErrors = Partial<Record<keyof BriefFormState, string>>;

const capabilities = ref<CapabilityManifest | null>(null);
const capabilitiesLoading = ref(false);
const worldPackage = ref<RunnableWorldPackage | null>(null);
const generatedBriefFingerprint = ref<string | null>(null);
const determinismStatus = ref("");
const session = ref<WorldSessionView | null>(null);
const sessionBriefFingerprint = ref<string | null>(null);
const projection = ref<PublicProjection | null>(null);
const eventPage = ref<EventPage | null>(null);
const evidence = ref<EvidenceBundle | null>(null);
const latestStep = ref<SessionStepResult | null>(null);
const acceptedDirection = ref<DirectionDecision | null>(null);
const rejectedDirection = ref<DirectionDecision | null>(null);
const latestAction = ref<ActionResult | null>(null);
const latestFeedback = ref<FeedbackResult | null>(null);
const operationError = ref("");
const operationWarning = ref("");
const operationMessage = ref("");
const boundedDirectionError = ref("");
const finalFactDirectionError = ref("");
const busyOperation = ref<BusyOperation | null>(null);
const refreshingCanonical = ref(false);

const briefForm = reactive<BriefFormState>({
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
const briefFieldErrors = computed(validateBriefForm);
const hasBriefErrors = computed(() => Object.keys(briefFieldErrors.value).length > 0);
const currentBriefFingerprint = computed(() =>
  hasBriefErrors.value ? null : fingerprintBrief(buildBrief()),
);
const hasCurrentPackage = computed(
  () =>
    worldPackage.value?.readiness.status === "ready" &&
    generatedBriefFingerprint.value !== null &&
    generatedBriefFingerprint.value === currentBriefFingerprint.value,
);
const hasCurrentSession = computed(
  () =>
    session.value !== null &&
    sessionBriefFingerprint.value !== null &&
    sessionBriefFingerprint.value === currentBriefFingerprint.value,
);
const hasCurrentProjection = computed(
  () =>
    hasCurrentSession.value &&
    projection.value !== null &&
    projection.value.session_id === session.value?.session_id,
);
const generatedBriefFingerprintLabel = computed(() =>
  generatedBriefFingerprint.value ? shortFingerprint(generatedBriefFingerprint.value) : "",
);

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

function validateInteger(
  value: number | null | undefined,
  label: string,
): string | undefined {
  if (typeof value !== "number" || !Number.isSafeInteger(value)) {
    return `${label}必须是整数。`;
  }
  return undefined;
}

function validateBriefForm(): BriefFieldErrors {
  const errors: BriefFieldErrors = {};
  const seed = briefForm.seed.trim();
  const premise = briefForm.premise.trim();
  const stateKey = briefForm.stateKey.trim();

  if (!seed) {
    errors.seed = "Seed 不能为空。";
  } else if (seed.length > 128) {
    errors.seed = "Seed 不能超过 128 个字符。";
  }
  if (!premise) {
    errors.premise = "公开前提不能为空。";
  } else if (premise.length > 1000) {
    errors.premise = "公开前提不能超过 1000 个字符。";
  }
  if (!stateKey) {
    errors.stateKey = "状态变量不能为空。";
  } else if (!/^[a-z][a-z0-9_]{0,63}$/.test(stateKey)) {
    errors.stateKey = "须以小写字母开头，且只能包含小写字母、数字和下划线（最多 64 位）。";
  }

  try {
    const constraints = JSON.parse(briefForm.constraintsText) as unknown;
    if (!constraints || typeof constraints !== "object" || Array.isArray(constraints)) {
      errors.constraintsText = "约束 JSON 必须是对象。";
    }
  } catch {
    errors.constraintsText = "约束 JSON 格式无效。";
  }

  errors.initial = validateInteger(briefForm.initial, "初始值");
  errors.minimum = validateInteger(briefForm.minimum, "最小值");
  errors.maximum = validateInteger(briefForm.maximum, "最大值");
  errors.variableStep = validateInteger(briefForm.variableStep, "步幅");

  if (!errors.variableStep && (briefForm.variableStep! < 1 || briefForm.variableStep! > 100)) {
    errors.variableStep = "步幅必须在 1 到 100 之间。";
  }
  if (!errors.minimum && !errors.maximum && briefForm.minimum! >= briefForm.maximum!) {
    errors.minimum = "最小值必须小于最大值。";
    errors.maximum = "最大值必须大于最小值。";
  }
  if (
    !errors.initial &&
    !errors.minimum &&
    !errors.maximum &&
    (briefForm.initial! < briefForm.minimum! || briefForm.initial! > briefForm.maximum!)
  ) {
    errors.initial = "初始值必须位于最小值与最大值之间。";
  }
  if (
    !errors.initial &&
    !errors.minimum &&
    !errors.maximum &&
    !errors.variableStep &&
    briefForm.initial! + briefForm.variableStep! > briefForm.maximum! &&
    briefForm.initial! - briefForm.variableStep! < briefForm.minimum!
  ) {
    errors.variableStep = "当前初始值至少要能向上或向下执行一次该步幅。";
  }

  if (
    typeof briefForm.stepSeconds !== "number" ||
    !Number.isFinite(briefForm.stepSeconds) ||
    briefForm.stepSeconds <= 0 ||
    briefForm.stepSeconds > 3600
  ) {
    errors.stepSeconds = "Tick 秒数必须大于 0 且不超过 3600。";
  }

  for (const key of Object.keys(errors) as Array<keyof BriefFieldErrors>) {
    if (!errors[key]) {
      delete errors[key];
    }
  }
  return errors;
}

function buildBrief(): WorldBrief {
  const firstError = Object.values(briefFieldErrors.value)[0];
  if (firstError) {
    throw new Error(firstError);
  }
  const constraints = JSON.parse(briefForm.constraintsText) as Record<string, unknown>;
  return {
    seed: briefForm.seed.trim(),
    premise: briefForm.premise.trim(),
    constraints,
    scale_bounds: {
      minimum_locations: 1,
      maximum_locations: 1,
      minimum_agents: 1,
      maximum_agents: 1,
      minimum_state_variables: 1,
      maximum_state_variables: 16,
    },
    state_variables: [
      {
        key: briefForm.stateKey.trim(),
        initial: briefForm.initial!,
        minimum: briefForm.minimum!,
        maximum: briefForm.maximum!,
        step: briefForm.variableStep!,
      },
    ],
    agent_count: 1,
    step_seconds: briefForm.stepSeconds!,
  };
}

function stableSerialize(value: unknown): string {
  if (Array.isArray(value)) {
    return `[${value.map(stableSerialize).join(",")}]`;
  }
  if (value && typeof value === "object") {
    return `{${Object.keys(value as Record<string, unknown>)
      .sort()
      .map(
        (key) =>
          `${JSON.stringify(key)}:${stableSerialize((value as Record<string, unknown>)[key])}`,
      )
      .join(",")}}`;
  }
  return JSON.stringify(value) ?? "null";
}

function fingerprintBrief(brief: WorldBrief): string {
  return stableSerialize(brief);
}

function shortFingerprint(fingerprint: string): string {
  let hash = 0x811c9dc5;
  for (let index = 0; index < fingerprint.length; index += 1) {
    hash = Math.imul(hash ^ fingerprint.charCodeAt(index), 0x01000193);
  }
  return `brief-${(hash >>> 0).toString(16).padStart(8, "0")}-${fingerprint.length}`;
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

function resetSessionArtifacts(): void {
  session.value = null;
  sessionBriefFingerprint.value = null;
  projection.value = null;
  eventPage.value = null;
  evidence.value = null;
  latestStep.value = null;
  acceptedDirection.value = null;
  rejectedDirection.value = null;
  boundedDirectionError.value = "";
  finalFactDirectionError.value = "";
  latestAction.value = null;
  latestFeedback.value = null;
}

function resetGeneratedArtifacts(): void {
  worldPackage.value = null;
  generatedBriefFingerprint.value = null;
  determinismStatus.value = "";
  selectedActionId.value = "";
  selectedFeedbackType.value = "";
  resetSessionArtifacts();
}

function clearNotice(): void {
  operationError.value = "";
  operationWarning.value = "";
  operationMessage.value = "";
}

watch(
  currentBriefFingerprint,
  (fingerprint) => {
    if (
      generatedBriefFingerprint.value !== null &&
      fingerprint !== generatedBriefFingerprint.value
    ) {
      resetGeneratedArtifacts();
      operationError.value = "";
      operationMessage.value = "";
      operationWarning.value = "WorldBrief 已变更，旧生成包和会话已失效，请重新生成。";
    }
  },
  { flush: "sync" },
);

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

function syncDirectionReceipts(serverEvidence: EvidenceBundle): void {
  if (acceptedDirection.value) {
    acceptedDirection.value =
      serverEvidence.direction_decisions.find(
        (decision) => decision.request_id === acceptedDirection.value?.request_id,
      ) ?? acceptedDirection.value;
  }
  if (rejectedDirection.value) {
    rejectedDirection.value =
      serverEvidence.direction_decisions.find(
        (decision) => decision.request_id === rejectedDirection.value?.request_id,
      ) ?? rejectedDirection.value;
  }
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

function sessionContextMatches(sessionId: string, fingerprint: string): boolean {
  return (
    session.value?.session_id === sessionId &&
    sessionBriefFingerprint.value === fingerprint &&
    currentBriefFingerprint.value === fingerprint
  );
}

async function refreshCanonicalData(sessionId: string, fingerprint: string): Promise<void> {
  if (!sessionContextMatches(sessionId, fingerprint)) {
    throw new Error("当前会话已失效，请重新生成世界包并启动会话。" );
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
      if (!sessionContextMatches(sessionId, fingerprint)) {
        throw new Error("刷新期间 WorldBrief 已变更，旧会话结果未写入页面。" );
      }
      session.value = serverSession;
      projection.value = headAfter;
      eventPage.value = serverEvents;
      evidence.value = serverEvidence;
      syncDirectionReceipts(serverEvidence);
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
    const fingerprint = fingerprintBrief(brief);
    const [first, second] = await Promise.all([
      createWorldPackage({ request_id: nextRequestId("package-primary"), brief }),
      createWorldPackage({ request_id: nextRequestId("package-repeat"), brief }),
    ]);
    const fetched = await getWorldPackage(first.package_id);
    if (first.package_hash !== second.package_hash || first.package_hash !== fetched.package_hash) {
      throw new Error("相同 WorldBrief 的 package_hash 不一致。" );
    }
    if (currentBriefFingerprint.value !== fingerprint) {
      resetGeneratedArtifacts();
      operationWarning.value = "生成期间 WorldBrief 已变更，本次返回包未采用，请重新生成。";
      return;
    }
    resetSessionArtifacts();
    generatedBriefFingerprint.value = fingerprint;
    worldPackage.value = fetched;
    determinismStatus.value = `通过 · ${first.package_hash === second.package_hash ? "2/2 hash 一致" : "不一致"}`;
    syncPackageInputs(fetched);
    operationMessage.value = "世界包已生成，并由服务端读取结果完成确定性校验。";
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleBootSession(): Promise<void> {
  const packageToBoot = worldPackage.value;
  const fingerprint = generatedBriefFingerprint.value;
  if (!packageToBoot || !fingerprint || !hasCurrentPackage.value) {
    clearNotice();
    operationWarning.value = "当前没有与 WorldBrief 匹配的可启动包，请重新生成。";
    return;
  }
  clearNotice();
  busyOperation.value = "boot";
  try {
    const created = await createWorldSession({
      request_id: nextRequestId("session-boot"),
      package_id: packageToBoot.package_id,
      package_hash: packageToBoot.package_hash,
    });
    if (
      currentBriefFingerprint.value !== fingerprint ||
      worldPackage.value?.package_id !== packageToBoot.package_id
    ) {
      operationWarning.value = "会话启动期间 WorldBrief 已变更，旧会话未采用，请重新生成。";
      return;
    }
    if (created.source_package_hash !== packageToBoot.package_hash) {
      throw new Error("服务端会话 source_package_hash 与当前生成包不一致。" );
    }
    resetSessionArtifacts();
    session.value = created;
    sessionBriefFingerprint.value = fingerprint;
    try {
      await refreshCanonicalData(created.session_id, fingerprint);
      operationMessage.value = "会话已从当前 package_hash 启动，权威投影与证据已刷新。";
    } catch (error) {
      operationWarning.value = `会话 ${created.session_id} 已启动，但权威证据刷新失败：${errorText(error)}`;
    }
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleStepSession(): Promise<void> {
  if (!session.value || !projection.value || !sessionBriefFingerprint.value || !hasCurrentProjection.value) {
    return;
  }
  if (!Number.isInteger(stepCount.value) || stepCount.value < 1 || stepCount.value > 100) {
    clearNotice();
    operationError.value = "精确步数必须是 1 到 100 之间的整数。";
    return;
  }
  const sessionId = session.value.session_id;
  const fingerprint = sessionBriefFingerprint.value;
  const expectedRevision = projection.value.revision;
  clearNotice();
  busyOperation.value = "step";
  try {
    const result = await stepWorldSession(sessionId, {
      request_id: nextRequestId("session-step"),
      step_count: stepCount.value,
      expected_revision: expectedRevision,
    });
    if (!sessionContextMatches(sessionId, fingerprint)) {
      operationWarning.value = "旧会话的 Step 已返回，但 WorldBrief 已变更，结果未写入页面。";
      return;
    }
    latestStep.value = result;
    try {
      await refreshCanonicalData(sessionId, fingerprint);
      operationMessage.value = `精确推进 ${result.step_count} 个 tick，服务端投影与证据已刷新。`;
    } catch (error) {
      operationWarning.value = `Step 已完成，但权威证据刷新失败：${errorText(error)}`;
    }
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleSubmitBoundedDirection(): Promise<void> {
  if (!session.value || !projection.value || !sessionBriefFingerprint.value || !hasCurrentProjection.value) {
    return;
  }
  if (!Number.isInteger(directionMagnitude.value) || directionMagnitude.value < -300 || directionMagnitude.value > 300) {
    boundedDirectionError.value = "有界压力必须是 -300 到 300 之间的整数。";
    return;
  }
  const sessionId = session.value.session_id;
  const fingerprint = sessionBriefFingerprint.value;
  const windowId = projection.value.active_intervention_window.window_id;
  const expectedRevision = projection.value.revision;
  const targetRef = worldPackage.value?.brief.state_variables[0]?.key ?? briefForm.stateKey;
  clearNotice();
  boundedDirectionError.value = "";
  busyOperation.value = "bounded-direction";
  try {
    const decision = await submitWorldDirection(sessionId, {
      request_id: nextRequestId("direction-bounded"),
      window_id: windowId,
      expected_revision: expectedRevision,
      kind: "bounded_pressure",
      target_ref: targetRef,
      summary: "对公开状态变量施加有界压力。",
      magnitude: directionMagnitude.value,
    });
    if (!sessionContextMatches(sessionId, fingerprint)) {
      operationWarning.value = `旧会话的有界压力命令已返回 ${decision.status}，但 WorldBrief 已变更。`;
      return;
    }
    acceptedDirection.value = decision;
    try {
      await refreshCanonicalData(sessionId, fingerprint);
      operationMessage.value = `有界压力命令已独立提交，服务端状态：${decision.status}。`;
    } catch (error) {
      boundedDirectionError.value = `命令已返回 ${decision.status}，但证据刷新失败：${errorText(error)}`;
      operationWarning.value = boundedDirectionError.value;
    }
  } catch (error) {
    boundedDirectionError.value = errorText(error);
    operationError.value = `有界压力命令提交失败：${boundedDirectionError.value}`;
  } finally {
    busyOperation.value = null;
  }
}

async function handleSubmitFinalFactDirection(): Promise<void> {
  if (!session.value || !projection.value || !sessionBriefFingerprint.value || !hasCurrentProjection.value) {
    return;
  }
  if (!Number.isInteger(directionFinalValue.value)) {
    finalFactDirectionError.value = "最终值必须是整数。";
    return;
  }
  const sessionId = session.value.session_id;
  const fingerprint = sessionBriefFingerprint.value;
  const windowId = projection.value.active_intervention_window.window_id;
  const expectedRevision = projection.value.revision;
  const targetRef = worldPackage.value?.brief.state_variables[0]?.key ?? briefForm.stateKey;
  clearNotice();
  finalFactDirectionError.value = "";
  busyOperation.value = "final-fact-direction";
  try {
    const decision = await submitWorldDirection(sessionId, {
      request_id: nextRequestId("direction-final-fact"),
      window_id: windowId,
      expected_revision: expectedRevision,
      kind: "direct_final_fact",
      target_ref: targetRef,
      summary: "直接指定最终世界事实。",
      final_value: directionFinalValue.value,
    });
    if (!sessionContextMatches(sessionId, fingerprint)) {
      operationWarning.value = `旧会话的最终事实命令已返回 ${decision.status}，但 WorldBrief 已变更。`;
      return;
    }
    rejectedDirection.value = decision;
    try {
      await refreshCanonicalData(sessionId, fingerprint);
      operationMessage.value = `最终事实命令已独立提交，服务端状态：${decision.status}。`;
    } catch (error) {
      finalFactDirectionError.value = `命令已返回 ${decision.status}，但证据刷新失败：${errorText(error)}`;
      operationWarning.value = finalFactDirectionError.value;
    }
  } catch (error) {
    finalFactDirectionError.value = errorText(error);
    operationError.value = `最终事实命令提交失败：${finalFactDirectionError.value}`;
  } finally {
    busyOperation.value = null;
  }
}

async function handleSubmitAction(): Promise<void> {
  if (
    !session.value ||
    !projection.value ||
    !sessionBriefFingerprint.value ||
    !selectedActionId.value ||
    !hasCurrentProjection.value
  ) {
    return;
  }
  if (!Number.isInteger(actionAmount.value) || actionAmount.value < -300 || actionAmount.value > 300) {
    clearNotice();
    operationError.value = "Action amount 必须是 -300 到 300 之间的整数。";
    return;
  }
  const sessionId = session.value.session_id;
  const fingerprint = sessionBriefFingerprint.value;
  const expectedRevision = projection.value.revision;
  const actionId = selectedActionId.value;
  clearNotice();
  busyOperation.value = "action";
  try {
    const result = await submitWorldAction(sessionId, {
      request_id: nextRequestId("client-action"),
      expected_revision: expectedRevision,
      action_id: actionId,
      target_ref: actionTarget(actionId),
      amount: actionAmount.value,
    });
    if (!sessionContextMatches(sessionId, fingerprint)) {
      operationWarning.value = `旧会话的 Action 已返回 ${result.status}，但 WorldBrief 已变更。`;
      return;
    }
    latestAction.value = result;
    try {
      await refreshCanonicalData(sessionId, fingerprint);
      operationMessage.value = "Action 已由 WorldEngine 规则判定，权威投影与证据已刷新。";
    } catch (error) {
      operationWarning.value = `Action 已返回 ${result.status}，但权威证据刷新失败：${errorText(error)}`;
    }
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleSubmitFeedback(): Promise<void> {
  if (
    !session.value ||
    !projection.value ||
    !sessionBriefFingerprint.value ||
    !selectedFeedbackType.value ||
    !hasCurrentProjection.value
  ) {
    return;
  }
  const summary = feedbackSummary.value.trim();
  if (!summary || summary.length > 500) {
    clearNotice();
    operationError.value = "公开摘要不能为空且不能超过 500 个字符。";
    return;
  }
  const sessionId = session.value.session_id;
  const fingerprint = sessionBriefFingerprint.value;
  const expectedRevision = projection.value.revision;
  const feedbackType = selectedFeedbackType.value;
  clearNotice();
  busyOperation.value = "feedback";
  try {
    const evidenceEvents = evidence.value?.events ?? [];
    const relatedEventRef =
      latestAction.value?.event_ref ??
      (evidenceEvents.length > 0 ? evidenceEvents[evidenceEvents.length - 1].event_id : undefined);
    const result = await submitWorldFeedback(sessionId, {
      request_id: nextRequestId("client-feedback"),
      expected_revision: expectedRevision,
      feedback_type: feedbackType,
      summary,
      ...(relatedEventRef ? { related_event_ref: relatedEventRef } : {}),
    });
    if (!sessionContextMatches(sessionId, fingerprint)) {
      operationWarning.value = `旧会话的 Typed Feedback 已返回 ${result.status}，但 WorldBrief 已变更。`;
      return;
    }
    latestFeedback.value = result;
    try {
      await refreshCanonicalData(sessionId, fingerprint);
      operationMessage.value = "Typed Feedback 已由 WorldEngine 接受或拒绝，权威证据已刷新。";
    } catch (error) {
      operationWarning.value = `Typed Feedback 已返回 ${result.status}，但权威证据刷新失败：${errorText(error)}`;
    }
  } catch (error) {
    operationError.value = errorText(error);
  } finally {
    busyOperation.value = null;
  }
}

async function handleRefreshCanonical(): Promise<void> {
  const sessionId = session.value?.session_id;
  const fingerprint = sessionBriefFingerprint.value;
  clearNotice();
  if (!sessionId || !fingerprint || !hasCurrentSession.value) {
    operationWarning.value = "尚未启动与当前 WorldBrief 匹配的会话，无法刷新证据。";
    return;
  }
  try {
    await refreshCanonicalData(sessionId, fingerprint);
    operationMessage.value = "投影、事件与证据已从服务端刷新。";
  } catch (error) {
    operationError.value = errorText(error);
  }
}

async function handleDownloadEvidence(): Promise<void> {
  const sessionId = session.value?.session_id;
  const fingerprint = sessionBriefFingerprint.value;
  if (!sessionId || !fingerprint || !hasCurrentSession.value) {
    clearNotice();
    operationWarning.value = "尚未启动与当前 WorldBrief 匹配的会话，无法导出证据。";
    return;
  }
  clearNotice();
  refreshingCanonical.value = true;
  try {
    const latestEvidence = await exportSessionEvidence(sessionId);
    if (!sessionContextMatches(sessionId, fingerprint)) {
      operationWarning.value = "证据导出期间 WorldBrief 已变更，旧会话证据未下载。";
      return;
    }
    evidence.value = latestEvidence;
    const blob = new Blob([JSON.stringify(latestEvidence, null, 2)], {
      type: "application/json;charset=utf-8",
    });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = `${sessionId}-evidence.json`;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    URL.revokeObjectURL(url);
    operationMessage.value = `证据已导出：完整性 ${latestEvidence.completeness.integrity.status}，场景覆盖 ${latestEvidence.completeness.scenario_coverage.status}。`;
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
  overflow-x: hidden;
  color: #17202a;
  background: #f2f4f7;
}

.workbench {
  box-sizing: border-box;
  width: min(1600px, 100%);
  max-width: 100%;
  min-width: 0;
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
  flex-wrap: wrap;
  gap: 8px;
  min-width: 0;
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
  min-width: 0;
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

.field-error,
.command-error {
  display: block;
  margin-top: 4px;
  color: #b42318;
  font-size: 10px;
  line-height: 1.4;
  overflow-wrap: anywhere;
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

.direction-command {
  display: grid;
  gap: 8px;
  min-width: 0;
}

.direction-command + .direction-command {
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px solid #eaecf0;
}

.direction-command > :deep(.ant-btn-block) {
  margin-top: 2px;
}

.direction-receipt {
  display: grid;
  grid-template-columns: auto auto minmax(0, 1fr);
  align-items: center;
  gap: 6px;
  min-width: 0;
  margin-top: 2px;
  color: #667085;
  font-size: 10px;
}

.direction-receipt > span {
  color: #475467;
  font-weight: 600;
}

.direction-receipt code,
.direction-receipt small {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.direction-receipt code {
  grid-column: 1 / -1;
  color: #344054;
  font-size: 9px;
}

.direction-receipt small {
  grid-column: 1 / -1;
  color: #98a2b3;
  font-size: 8px;
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

  .header-actions {
    justify-content: flex-start;
    width: 100%;
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
    grid-template-columns: 46px minmax(0, 1fr);
  }

  .operation-grid span {
    grid-column: 1 / -1;
  }
}

@media (max-width: 440px) {
  .two-column-fields,
  .three-column-fields,
  .inline-command {
    grid-template-columns: 1fr;
  }

  .result-wide {
    grid-column: auto;
  }
}
</style>

<template>
  <a-card data-test="world-panel" title="World Panel">
    <a-space direction="vertical" :size="16" class="world-stack">
      <a-typography-paragraph class="world-help">
        The JSON above shows the current world parameters. Use a dot path below to update a
        single parameter. For example, set path to
        <a-typography-text code>counter.increment</a-typography-text>, choose type
        <a-typography-text code>number</a-typography-text>, and enter
        <a-typography-text code>2</a-typography-text> as the value to produce
        <a-typography-text code>{{ stringExample }}</a-typography-text>. If you need a unit,
        for example for <a-typography-text code>river.width</a-typography-text>, fill in
        <a-typography-text code>unit</a-typography-text> as well to produce
        <a-typography-text code>{{ unitExample }}</a-typography-text>.
      </a-typography-paragraph>

      <a-spin :spinning="loading">
        <a-alert v-if="error" type="error" show-icon :message="error" />
        <pre v-else data-test="world-params-json" class="world-params">{{ formattedParams }}</pre>
      </a-spin>

      <a-form layout="vertical" class="world-param-form">
        <a-form-item label="Path">
          <a-input data-test="world-params-path-input" v-model:value="path" :placeholder="pathPlaceholder" />
        </a-form-item>
        <a-form-item label="Type">
          <a-select data-test="world-params-type-select" v-model:value="valueType" :options="typeOptions" />
        </a-form-item>
        <a-form-item label="Value">
          <a-select
            v-if="valueType === 'boolean'"
            v-model:value="booleanValue"
            :options="booleanOptions"
          />
          <a-input
            v-else
            data-test="world-params-value-input"
            v-model:value="rawValue"
            :placeholder="valuePlaceholder"
          />
        </a-form-item>
        <a-form-item label="Unit (optional)">
          <a-input v-model:value="unit" :placeholder="unitPlaceholder" />
        </a-form-item>
        <a-space direction="vertical" :size="12">
          <a-button
            type="primary"
            data-test="world-params-apply-button"
            :loading="applying"
            :disabled="!path.trim()"
            @click="handleApply"
          >
            {{ applying ? "Applying..." : "Apply" }}
          </a-button>
          <a-alert v-if="applyError" data-test="world-params-error" type="error" show-icon :message="applyError">
            <template v-if="applyErrorDetails.length" #description>
              <ul class="apply-error-list">
                <li v-for="(detail, i) in applyErrorDetails" :key="i">{{ detail }}</li>
              </ul>
            </template>
          </a-alert>
        </a-space>
      </a-form>

      <a-divider />

      <a-form layout="vertical" class="world-param-form">
        <a-form-item label="Goal (optional)">
          <a-input
            data-test="world-agent-goal-input"
            v-model:value="agentGoal"
            placeholder="e.g. speed up counter / disable heartbeat"
          />
        </a-form-item>
        <a-space direction="vertical" :size="12">
          <a-button
            type="primary"
            data-test="world-agent-autotune-button"
            :loading="agentRunning"
            @click="handleAgentApply"
            class="agent-btn"
          >
            {{ agentRunning ? "Running..." : "LLM Auto-Tune" }}
          </a-button>
          <a-alert
            v-if="agentSuccess"
            data-test="world-agent-success"
            type="success"
            show-icon
            :message="agentSuccess"
          >
            <template v-if="agentPatches.length" #description>
              <details class="agent-patches-details">
                <summary>Show {{ agentPatches.length }} patch(es)</summary>
                <pre data-test="world-agent-patches" class="agent-patches-pre">{{ JSON.stringify(agentPatches, null, 2) }}</pre>
              </details>
            </template>
          </a-alert>
          <a-alert
            v-if="agentError"
            data-test="world-agent-error"
            type="error"
            show-icon
            :message="agentError"
          >
            <template v-if="agentErrorDetails.length" #description>
              <ul class="apply-error-list">
                <li v-for="(detail, i) in agentErrorDetails" :key="i">{{ detail }}</li>
              </ul>
            </template>
          </a-alert>
        </a-space>
      </a-form>
    </a-space>
  </a-card>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import {
  Alert as AAlert,
  Button as AButton,
  Card as ACard,
  Divider as ADivider,
  Form as AForm,
  FormItem as AFormItem,
  Input as AInput,
  Select as ASelect,
  Space as ASpace,
  Spin as ASpin,
  TypographyParagraph as ATypographyParagraph,
  TypographyText as ATypographyText,
} from "ant-design-vue";

import { ApiClientError, applyWorldParams, getWorldParams, proposeAndApplyWorldParams, type WorldParams } from "../api/client";

type ParamValueType = "string" | "number" | "boolean" | "json";

const props = withDefaults(
  defineProps<{
    params?: WorldParams | null;
    loading?: boolean;
    error?: string;
  }>(),
  {
    params: null,
    loading: false,
    error: "",
  },
);

const emit = defineEmits<{
  (event: "applied", params: WorldParams): void;
}>();

const path = ref<string>("");
const rawValue = ref<string>("");
const valueType = ref<ParamValueType>("string");
const booleanValue = ref<"true" | "false">("false");
const unit = ref<string>("");
const applying = ref<boolean>(false);
const applyError = ref<string>("");
const applyErrorDetails = ref<string[]>([]);

const agentGoal = ref<string>("");
const agentRunning = ref<boolean>(false);
const agentSuccess = ref<string>("");
const agentPatches = ref<unknown[]>([]);
const agentError = ref<string>("");
const agentErrorDetails = ref<string[]>([]);

const stringExample = '{"value":2,"type":"number"}';
const unitExample = '{"value":1,"type":"number","unit":"meter"}';
const pathPlaceholder = "Example: counter.increment";
const unitPlaceholder = "Example: meter";
const formattedParams = computed(() => JSON.stringify(props.params ?? {}, null, 2));
const typeOptions = [
  { label: "string", value: "string" },
  { label: "number", value: "number" },
  { label: "boolean", value: "boolean" },
  { label: "json", value: "json" },
] ;
const booleanOptions = [
  { label: "true", value: "true" },
  { label: "false", value: "false" },
];
const valuePlaceholder = computed(() => {
  if (valueType.value === "number") {
    return "Example: 2";
  }
  if (valueType.value === "json") {
    return 'Example: {"min":1,"max":3}';
  }
  return "Example: hello";
});

function parseInputValue(input: string, type: ParamValueType, boolValue: "true" | "false"): unknown {
  if (type === "boolean") {
    return boolValue === "true";
  }

  const trimmed = input.trim();

  if (type === "string") {
    return input;
  }

  if (!trimmed) {
    return "";
  }

  if (type === "number") {
    const parsed = Number(trimmed);
    if (Number.isNaN(parsed)) {
      throw new Error("Value must be a valid number");
    }
    return parsed;
  }

  try {
    return JSON.parse(trimmed);
  } catch {
    throw new Error("Value must be valid JSON");
  }
}

function buildPatchValue(): unknown {
  const parsedValue = parseInputValue(rawValue.value, valueType.value, booleanValue.value);
  const structuredValue: Record<string, unknown> = {
    value: parsedValue,
    type: valueType.value,
  };

  if (unit.value.trim()) {
    structuredValue.unit = unit.value.trim();
  }

  return structuredValue;
}

function extractErrorDetails(err: unknown): { msg: string; details: string[] } {
  if (!(err instanceof ApiClientError)) {
    return { msg: err instanceof Error ? err.message : "Apply failed", details: [] };
  }

  const data = err.data as Record<string, unknown> | undefined;
  const errors = Array.isArray(data?.errors) ? (data.errors as Record<string, unknown>[]) : [];

  const details = errors.map((e) => {
    const path = typeof e.path === "string" && e.path ? `${e.path}: ` : "";
    const detail = typeof e.detail === "string" ? e.detail : `${e.reason}`;
    return `${path}${detail}`;
  });

  return { msg: err.message, details };
}

async function handleApply(): Promise<void> {
  applying.value = true;
  applyError.value = "";
  applyErrorDetails.value = [];

  try {
    const nextParams = await applyWorldParams({
      patches: [
        {
          op: "set",
          path: path.value.trim(),
          value: buildPatchValue(),
        },
      ],
    });
    path.value = "";
    rawValue.value = "";
    valueType.value = "string";
    booleanValue.value = "false";
    unit.value = "";
    emit("applied", nextParams);
  } catch (err) {
    const { msg, details } = extractErrorDetails(err);
    applyError.value = msg;
    applyErrorDetails.value = details;
  } finally {
    applying.value = false;
  }
}

async function handleAgentApply(): Promise<void> {
  agentRunning.value = true;
  agentSuccess.value = "";
  agentPatches.value = [];
  agentError.value = "";
  agentErrorDetails.value = [];

  try {
    const result = await proposeAndApplyWorldParams(agentGoal.value.trim() || undefined);
    const nextParams = await getWorldParams();
    agentSuccess.value = `Applied ${result.patches.length} patch(es) in ${result.attempts} attempt(s)`;
    agentPatches.value = result.patches;
    agentGoal.value = "";
    emit("applied", nextParams);
  } catch (err) {
    const { msg, details } = extractErrorDetails(err);
    agentError.value = msg;
    agentErrorDetails.value = details;
  } finally {
    agentRunning.value = false;
  }
}
</script>

<style scoped>
.world-stack {
  width: 100%;
}

.world-params {
  max-height: 240px;
  overflow: auto;
  margin: 0;
  padding: 12px;
  background: rgba(15, 23, 42, 0.06);
  border-radius: 8px;
  font-size: 12px;
}

.world-help {
  margin-top: 0;
  font-size: 13px;
  line-height: 1.5;
}

.world-param-form {
  width: 100%;
}

.world-error {
  color: #b42318;
}

.apply-error-list {
  margin: 4px 0 0;
  padding-left: 18px;
}

.agent-patches-pre {
  max-height: 160px;
  overflow: auto;
  margin: 4px 0 0;
  font-size: 12px;
}
</style>

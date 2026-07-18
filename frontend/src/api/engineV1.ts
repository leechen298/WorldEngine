export const ENGINE_V1_CONTRACT_VERSION = "engine-v1-mvp";
export const ENGINE_V1_SCHEMA_VERSION = "worldengine.engine.v1";

interface ApiSuccessResponse<T> {
  code: number;
  data: T;
  msg: string;
}

interface ApiErrorResponse {
  code: number;
  msg: string;
  data?: unknown;
}

export interface StateVariableSpec {
  key: string;
  initial: number;
  minimum: number;
  maximum: number;
  step: number;
}

export interface WorldScaleBounds {
  minimum_locations: 1;
  maximum_locations: 1;
  minimum_agents: 1;
  maximum_agents: 1;
  minimum_state_variables: number;
  maximum_state_variables: number;
}

export interface WorldBrief {
  seed: string;
  premise: string;
  constraints: Record<string, unknown>;
  scale_bounds?: WorldScaleBounds;
  state_variables: StateVariableSpec[];
  agent_count: 1;
  step_seconds: number;
}

export interface WorldPackageCreateRequest {
  request_id: string;
  brief: WorldBrief;
}

export interface PackageReadiness {
  status: "ready" | "invalid";
  diagnostics: Array<Record<string, unknown>>;
}

export interface RunnableWorldPackage {
  schema_version: typeof ENGINE_V1_SCHEMA_VERSION;
  package_id: string;
  package_hash: string;
  brief: WorldBrief;
  world_spec: Record<string, unknown>;
  rule_catalog: Array<Record<string, unknown>>;
  action_catalog: Array<Record<string, unknown>>;
  agent_seed_set: Array<Record<string, unknown>>;
  projection_manifest: Record<string, unknown>;
  evidence_policy: Record<string, unknown>;
  readiness: PackageReadiness;
}

export interface SessionCreateRequest {
  request_id: string;
  package_id: string;
  package_hash: string;
}

export interface InterventionWindow {
  window_id: string;
  open_tick: number;
  status: "open" | "closed";
}

export interface AgentExperienceRef {
  ref_id: string;
  ref_type: "event" | "action_result";
  source_tick: number;
  public_effect: string;
}

export interface AgentPublicState {
  agent_id: string;
  location_id: string;
  cycle_count: number;
  last_intent: string;
  decision_mode: string;
  experience_refs: AgentExperienceRef[];
}

export interface PublicProjection {
  schema_version: typeof ENGINE_V1_SCHEMA_VERSION;
  session_id: string;
  world_id: string;
  source_package_hash: string;
  status: "ready" | "paused" | "closed";
  tick: number;
  world_time_seconds: number;
  revision: number;
  state_hash: string;
  variables: Record<string, number>;
  feedback_count: number;
  locations: Array<Record<string, unknown>>;
  entities: Array<Record<string, unknown>>;
  agents: AgentPublicState[];
  allowed_actions: string[];
  active_intervention_window: InterventionWindow;
  event_cursor: number;
}

export interface WorldSessionView {
  schema_version: typeof ENGINE_V1_SCHEMA_VERSION;
  session_id: string;
  package_id: string;
  source_package_hash: string;
  initial_snapshot_id: string;
  projection: PublicProjection;
}

export interface SessionStepRequest {
  request_id: string;
  step_count: number;
  expected_revision?: number;
}

export interface SessionStepResult {
  request_id: string;
  status: "completed";
  step_count: number;
  start_tick: number;
  end_tick: number;
  start_revision: number;
  end_revision: number;
  start_state_hash: string;
  end_state_hash: string;
  event_refs: string[];
  snapshot_refs: string[];
  projection: PublicProjection;
}

export interface DirectionRequest {
  request_id: string;
  window_id: string;
  expected_revision?: number;
  kind: "bounded_pressure" | "direct_final_fact";
  target_ref: string;
  summary: string;
  magnitude?: number;
  final_value?: number;
}

export interface DirectionDecision {
  request_id: string;
  window_id: string;
  status: "accepted" | "rejected" | "conflict";
  reason_code: string;
  public_reason: string;
  queued: boolean;
  rule_refs: string[];
  event_ref: string;
  application_event_refs: string[];
  applied_diff_refs: string[];
  tick: number;
  revision: number;
  state_hash_before: string;
  state_hash_after: string;
}

export interface ActionRequest {
  request_id: string;
  expected_revision?: number;
  action_id: string;
  target_ref: string;
  amount: number;
}

export interface ActionResult {
  request_id: string;
  status: "accepted" | "rejected";
  reason_code: string;
  rule_refs: string[];
  event_ref: string;
  applied_diff_refs: string[];
  projection: PublicProjection;
}

export interface FeedbackRequest {
  request_id: string;
  expected_revision?: number;
  feedback_type: string;
  summary: string;
  related_event_ref?: string;
}

export interface FeedbackResult {
  request_id: string;
  status: "accepted" | "rejected";
  reason_code: string;
  rule_refs: string[];
  event_ref: string;
  applied_diff_refs: string[];
  projection: PublicProjection;
}

export interface DiffOperation {
  path: string;
  before: unknown;
  after: unknown;
}

export interface DiffRecord {
  diff_id: string;
  request_id: string;
  event_ref: string;
  tick: number;
  revision: number;
  state_hash_before: string;
  state_hash_after: string;
  operations: DiffOperation[];
}

export interface EventRecord {
  sequence: number;
  event_id: string;
  event_type: string;
  source: string;
  status: "accepted" | "rejected";
  request_id: string;
  tick: number;
  revision: number;
  state_hash_before: string;
  state_hash_after: string;
  rule_refs: string[];
  diff_refs: string[];
  payload: Record<string, unknown>;
}

export interface SnapshotRecord {
  snapshot_id: string;
  tick: number;
  revision: number;
  state_hash: string;
  canonical_state: Record<string, unknown>;
}

export interface AgentCycleEvidence {
  cycle_id: string;
  agent_id: string;
  tick: number;
  perception: Record<string, unknown>;
  decision: Record<string, unknown>;
  action_request: Record<string, unknown>;
  rule_judgment: Record<string, unknown>;
  action_result: Record<string, unknown>;
  experience_refs_used: AgentExperienceRef[];
  event_refs: string[];
  diff_refs: string[];
}

export interface EventPage {
  session_id: string;
  after_sequence: number;
  items: EventRecord[];
  next_sequence: number;
  has_more: boolean;
}

export interface EvidenceCompleteness {
  status: "complete" | "incomplete";
  checks: Record<string, boolean>;
  missing: string[];
}

export interface EvidenceBundle {
  schema_version: typeof ENGINE_V1_SCHEMA_VERSION;
  contract_version: typeof ENGINE_V1_CONTRACT_VERSION;
  state_hash_algorithm: string;
  package: RunnableWorldPackage;
  projection: PublicProjection;
  events: EventRecord[];
  diffs: DiffRecord[];
  snapshots: SnapshotRecord[];
  agent_cycles: AgentCycleEvidence[];
  direction_decisions: DirectionDecision[];
  request_correlations: Array<Record<string, unknown>>;
  completeness: EvidenceCompleteness;
}

export interface CapabilityOperation {
  operation_id: string;
  method: "GET" | "POST";
  path: string;
  maturity: "anchor";
}

export interface CapabilityManifest {
  engine_id: "worldengine";
  engine_build: string;
  instance_id: string;
  contract_version: typeof ENGINE_V1_CONTRACT_VERSION;
  schema_version: typeof ENGINE_V1_SCHEMA_VERSION;
  state_hash_algorithm: string;
  operations: CapabilityOperation[];
}

export interface EventPollOptions {
  afterSequence?: number;
  limit?: number;
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export class EngineV1ApiError extends Error {
  readonly status: number;
  readonly code: number;
  readonly data?: unknown;

  constructor(message: string, options: { status: number; code: number; data?: unknown }) {
    super(message);
    this.name = "EngineV1ApiError";
    this.status = options.status;
    this.code = options.code;
    this.data = options.data;
  }
}

async function parseJsonResponse<T>(
  response: Response,
): Promise<ApiSuccessResponse<T> | ApiErrorResponse | null> {
  const contentType = response.headers.get("content-type") ?? "";
  if (!contentType.includes("application/json")) {
    return null;
  }
  try {
    return (await response.json()) as ApiSuccessResponse<T> | ApiErrorResponse;
  } catch {
    return null;
  }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, init);
  const payload = await parseJsonResponse<T>(response);

  if (!response.ok) {
    const errorPayload = payload as ApiErrorResponse | null;
    throw new EngineV1ApiError(
      errorPayload?.msg ?? `Engine V1 request failed: ${response.status}`,
      {
        status: response.status,
        code: errorPayload?.code ?? response.status,
        data: errorPayload?.data,
      },
    );
  }

  const successPayload = payload as ApiSuccessResponse<T> | null;
  if (!successPayload || successPayload.code !== 0) {
    throw new EngineV1ApiError(successPayload?.msg ?? "Invalid Engine V1 API response", {
      status: response.status,
      code: successPayload?.code ?? -1,
      data: successPayload,
    });
  }
  return successPayload.data;
}

function postJson<T>(path: string, body: unknown): Promise<T> {
  return request<T>(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function sessionPath(sessionId: string, suffix = ""): string {
  return `/api/v1/sessions/${encodeURIComponent(sessionId)}${suffix}`;
}

export function getEngineCapabilities(): Promise<CapabilityManifest> {
  return request<CapabilityManifest>("/api/v1/capabilities");
}

export function createWorldPackage(
  body: WorldPackageCreateRequest,
): Promise<RunnableWorldPackage> {
  return postJson<RunnableWorldPackage>("/api/v1/world-packages", body);
}

export function getWorldPackage(packageId: string): Promise<RunnableWorldPackage> {
  return request<RunnableWorldPackage>(
    `/api/v1/world-packages/${encodeURIComponent(packageId)}`,
  );
}

export function createWorldSession(body: SessionCreateRequest): Promise<WorldSessionView> {
  return postJson<WorldSessionView>("/api/v1/sessions", body);
}

export function getWorldSession(sessionId: string): Promise<WorldSessionView> {
  return request<WorldSessionView>(sessionPath(sessionId));
}

export function stepWorldSession(
  sessionId: string,
  body: SessionStepRequest,
): Promise<SessionStepResult> {
  return postJson<SessionStepResult>(sessionPath(sessionId, "/steps"), body);
}

export function submitWorldDirection(
  sessionId: string,
  body: DirectionRequest,
): Promise<DirectionDecision> {
  return postJson<DirectionDecision>(sessionPath(sessionId, "/directions"), body);
}

export function submitWorldAction(
  sessionId: string,
  body: ActionRequest,
): Promise<ActionResult> {
  return postJson<ActionResult>(sessionPath(sessionId, "/actions"), body);
}

export function submitWorldFeedback(
  sessionId: string,
  body: FeedbackRequest,
): Promise<FeedbackResult> {
  return postJson<FeedbackResult>(sessionPath(sessionId, "/feedback"), body);
}

export function getPublicProjection(sessionId: string): Promise<PublicProjection> {
  return request<PublicProjection>(sessionPath(sessionId, "/projection"));
}

export function pollWorldEvents(
  sessionId: string,
  options: EventPollOptions = {},
): Promise<EventPage> {
  const params = new URLSearchParams({
    after_sequence: String(options.afterSequence ?? 0),
    limit: String(options.limit ?? 200),
  });
  return request<EventPage>(sessionPath(sessionId, `/events?${params.toString()}`));
}

export function exportSessionEvidence(sessionId: string): Promise<EvidenceBundle> {
  return request<EvidenceBundle>(sessionPath(sessionId, "/evidence"));
}

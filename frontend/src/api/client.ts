export type HealthResponse = {
  status: string;
  service: string;
};

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

export interface RuntimeState {
  tick_id: number;
  world_time_seconds: number;
  step_seconds: number;
  updated_at?: string | null;
}

export interface WorldEvent {
  id: string;
  tick_id: number;
  world_time_seconds: number;
  type: string;
  source: string;
  payload: Record<string, any>;
  created_at: string;
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export class ApiClientError extends Error {
  status: number;
  code: number;
  data?: unknown;

  constructor(message: string, options: { status: number; code: number; data?: unknown }) {
    super(message);
    this.name = "ApiClientError";
    this.status = options.status;
    this.code = options.code;
    this.data = options.data;
  }
}

async function parseResponseBody<T>(
  response: Response,
): Promise<ApiSuccessResponse<T> | ApiErrorResponse | null> {
  const contentType = response.headers.get("content-type") ?? "";
  if (!contentType.includes("application/json")) {
    return null;
  }
  return (await response.json()) as ApiSuccessResponse<T> | ApiErrorResponse;
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, init);
  const payload = await parseResponseBody<T>(response);

  if (!response.ok) {
    const errorPayload = payload as ApiErrorResponse | null;
    throw new ApiClientError(
      errorPayload?.msg ?? `Request failed: ${response.status}`,
      {
        status: response.status,
        code: errorPayload?.code ?? response.status,
        data: errorPayload?.data,
      },
    );
  }

  const successPayload = payload as ApiSuccessResponse<T> | null;
  if (!successPayload || successPayload.code !== 0) {
    throw new ApiClientError(
      successPayload?.msg ?? "Invalid API response",
      {
        status: response.status,
        code: successPayload?.code ?? -1,
        data: successPayload,
      },
    );
  }

  return successPayload.data;
}

export async function fetchHealth(): Promise<HealthResponse> {
  return request<HealthResponse>("/health");
}

export async function getRuntimeState(): Promise<RuntimeState> {
  return request<RuntimeState>("/runtime/state");
}

export async function stepRuntime(): Promise<RuntimeState> {
  return request<RuntimeState>("/runtime/step", {
    method: "POST",
  });
}

export async function getWorldEvents(params?: {
  from_tick?: number;
  to_tick?: number;
  limit?: number;
}): Promise<WorldEvent[]> {
  const searchParams = new URLSearchParams();

  if (params?.from_tick !== undefined) {
    searchParams.set("from_tick", String(params.from_tick));
  }
  if (params?.to_tick !== undefined) {
    searchParams.set("to_tick", String(params.to_tick));
  }
  if (params?.limit !== undefined) {
    searchParams.set("limit", String(params.limit));
  }

  const query = searchParams.toString();
  return request<WorldEvent[]>(`/world/events${query ? `?${query}` : ""}`);
}

// One small HTTP client for every integration (Chapter 8).
import { setTimeout as sleep } from 'node:timers/promises';
import { retry, RetryableError } from './retry.js';

export class HttpError extends Error {
  constructor(method, url, status, body) {
    super(`${method} ${url} -> HTTP ${status}`);
    this.name = 'HttpError';
    this.status = status;
    this.body = body;
  }
}

const JSON_TYPE = { 'Content-Type': 'application/json' };
const MAX_WAIT_MS = 60_000;

export function createClient(opts) {
  const {
    baseUrl,
    headers = {},
    timeoutMs = 10_000,
    attempts = 4,
    log = () => {},
  } = opts;

  async function request(method, path, o = {}) {
    const { body, query } = o;
    const url = new URL(path, baseUrl);
    for (const [k, v] of Object.entries(query ?? {})) {
      if (v !== undefined) url.searchParams.set(k, v);
    }

    return retry(async () => {
      const res = await fetch(url, {
        method,
        headers: {
          Accept: 'application/json',
          'User-Agent': 'kes/0.4',
          ...(body ? JSON_TYPE : {}),
          ...headers,
        },
        body: body ? JSON.stringify(body) : undefined,
        signal: AbortSignal.timeout(timeoutMs),
      });
      log(`${method} ${url.pathname} ${res.status}`);

      if (res.status === 429 || res.status >= 500) {
        await waitForRetryAfter(res);
        throw new RetryableError(`HTTP ${res.status}`);
      }
      const text = await res.text();
      const data = text ? safeJson(text) : null;
      if (!res.ok) {
        throw new HttpError(method, url.pathname,
          res.status, data);
      }
      return {
        data, headers: res.headers, status: res.status,
      };
    }, { attempts });
  }

  return {
    request,
    get: (p, o) => request('GET', p, o),
    post: (p, body, o) =>
      request('POST', p, { ...o, body }),
    put: (p, body, o) => request('PUT', p, { ...o, body }),
    patch: (p, body, o) =>
      request('PATCH', p, { ...o, body }),
    delete: (p, o) => request('DELETE', p, o),
  };
}

function safeJson(text) {
  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

async function waitForRetryAfter(res) {
  const header = res.headers.get('retry-after');
  if (!header) return;
  let ms = Number(header) * 1000;
  if (Number.isNaN(ms)) {
    ms = new Date(header).getTime() - Date.now();
  }
  if (ms > 0) await sleep(Math.min(ms, MAX_WAIT_MS));
}

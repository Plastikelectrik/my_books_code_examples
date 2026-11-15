// Retries with exponential backoff and full jitter (Chapter 3).
import { setTimeout as sleep } from 'node:timers/promises';

export class RetryableError extends Error {}

const NET_CODES = new Set([
  'ECONNRESET', 'ECONNREFUSED', 'ETIMEDOUT',
  'EAI_AGAIN', 'UND_ERR_SOCKET',
]);

export function isRetryable(err) {
  if (err instanceof RetryableError) return true;
  if (err.name === 'TimeoutError') return true;
  // fetch wraps network errors: TypeError + cause.code
  const code = err.code ?? err.cause?.code;
  return NET_CODES.has(code);
}

export async function retry(fn, opts = {}) {
  const {
    attempts = 5,
    baseMs = 500,
    maxMs = 10_000,
    signal,
    onRetry = () => {},
    sleepFn = sleep,
  } = opts;

  for (let i = 1; ; i++) {
    try {
      return await fn(i);
    } catch (err) {
      const last = i >= attempts;
      if (last || !isRetryable(err)) throw err;
      const cap = Math.min(maxMs, baseMs * 2 ** (i - 1));
      const delay = Math.round(Math.random() * cap);
      onRetry(err, i, delay);
      await sleepFn(delay, undefined, { signal });
    }
  }
}

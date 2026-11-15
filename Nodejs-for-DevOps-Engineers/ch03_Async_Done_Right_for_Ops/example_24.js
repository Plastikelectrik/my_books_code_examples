// Book: Node.js for DevOps Engineers — Example 24
// src/lib/http.js
import { retry, RetryableError } from './retry.js';

export async function getJson(url, opts = {}) {
  return retry(async () => {
    const res = await fetch(url, {
      ...opts,
      signal: AbortSignal.timeout(opts.timeoutMs ?? 5000),
    });
    if (res.status === 429 || res.status >= 500) {
      throw new RetryableError(`HTTP ${res.status}`);
    }
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  }, {
    onRetry: (err, n, ms) =>
      console.error(
        `retry ${n} in ${ms}ms: ${err.message}`,
      ),
  });
}

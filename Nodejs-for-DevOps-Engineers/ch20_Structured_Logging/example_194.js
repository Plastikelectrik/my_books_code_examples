// Book: Node.js for DevOps Engineers — Example 194
// src/logs/ship.js
import { createReadStream } from 'node:fs';
import { createInterface } from 'node:readline';
import { retry, RetryableError } from '../lib/retry.js';

function postWithRetry(url, body) {
  return retry(async () => {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-ndjson' },
      body,
      signal: AbortSignal.timeout(10_000),
    });
    if (res.status === 429 || res.status >= 500) {
      throw new RetryableError(`HTTP ${res.status}`);
    }
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
  });
}

export async function ship(file, endpoint, opts = {}) {
  const { batchSize = 500, maxWaitMs = 2000 } = opts;
  const rl = createInterface({
    input: createReadStream(file),
    crlfDelay: Infinity,
  });

  let batch = [];
  let timer = null;
  let sent = 0;

  async function flush() {
    clearTimeout(timer);
    timer = null;
    if (!batch.length) return;
    const body = batch.join('\n') + '\n';
    batch = [];
    await postWithRetry(endpoint, body);
    sent++;
  }

  for await (const line of rl) {
    if (!line.trim()) continue;
    batch.push(line);
    if (batch.length >= batchSize) {
      rl.pause();
      await flush();
      rl.resume();
    } else if (!timer) {
      timer = setTimeout(() => flush(), maxWaitMs);
    }
  }
  await flush();
  return { batches: sent };
}

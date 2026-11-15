// Book: Node.js for DevOps Engineers — Example 81
// src/lib/rate-guard.js
import { setTimeout as sleep } from 'node:timers/promises';

export async function respectBudget(headers, log) {
  const remaining = Number(
    headers.get('x-ratelimit-remaining'));
  const reset = Number(headers.get('x-ratelimit-reset'));
  if (Number.isNaN(remaining) || remaining > 20) return;

  const waitMs = Math.max(0, reset * 1000 - Date.now());
  log?.(`rate budget low (${remaining}), ` +
    `pausing ${Math.ceil(waitMs / 1000)}s`);
  await sleep(Math.min(waitMs, 5 * 60_000));
}

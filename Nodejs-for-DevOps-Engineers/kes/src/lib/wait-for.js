// Poll until a condition is met, with a deadline (Chapter 3).
import { setTimeout as sleep } from 'node:timers/promises';

export async function waitFor(check, opts = {}) {
  const {
    timeoutMs = 300_000,
    intervalMs = 5000,
    label = 'condition',
    onTick = () => {},
    sleepFn = sleep,
  } = opts;
  const deadline = Date.now() + timeoutMs;

  while (true) {
    const result = await check();
    if (result.done) return result.value;
    onTick(result);
    if (Date.now() + intervalMs > deadline) {
      throw new Error(`${label} not met in ${timeoutMs}ms`);
    }
    await sleepFn(intervalMs);
  }
}

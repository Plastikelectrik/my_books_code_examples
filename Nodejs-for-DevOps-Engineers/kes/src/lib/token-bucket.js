// Spread requests evenly: N per second (Chapter 8).
import { setTimeout as sleep } from 'node:timers/promises';

export function tokenBucket(perSecond) {
  let tokens = perSecond;
  let last = Date.now();

  return async function take() {
    for (;;) {
      const now = Date.now();
      tokens = Math.min(perSecond,
        tokens + ((now - last) / 1000) * perSecond);
      last = now;
      if (tokens >= 1) {
        tokens -= 1;
        return;
      }
      await sleep(((1 - tokens) / perSecond) * 1000);
    }
  };
}

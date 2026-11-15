// Book: Node.js for DevOps Engineers — Example 130
// src/canary/controller.js
import { setTimeout as sleep } from 'node:timers/promises';
import { analyse, decide } from './analysis.js';

export async function runCanary(o) {
  const {
    steps = [5, 25, 50, 100],
    bakeMs = 5 * 60_000,
    maxHolds = 3,
    router, snapshot, service, stable, canary,
    log = console.error,
    wait = sleep,
  } = o;

  for (const weight of steps) {
    await router.setCanary(weight);
    if (weight === 100) break;

    let holds = 0;
    for (;;) {
      await wait(bakeMs);
      const win = `${Math.round(bakeMs / 1000)}s`;
      const [c, b] = await Promise.all([
        snapshot(service, canary, win),
        snapshot(service, stable, win),
      ]);
      const findings = analyse(c, b);
      const verdict = decide(findings);
      log(`weight ${weight}%: ${verdict} ` +
        JSON.stringify(c));

      if (verdict === 'promote') break;
      if (verdict === 'rollback' || ++holds > maxHolds) {
        await router.setCanary(0);
        return { result: 'rolled-back', weight, findings };
      }
    }
  }
  return { result: 'promoted' };
}

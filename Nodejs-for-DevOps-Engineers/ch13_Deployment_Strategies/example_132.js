// Book: Node.js for DevOps Engineers — Example 132
// src/deploy/strategies.js
import { runCanary } from '../canary/controller.js';

export async function deployWithStrategy(plan, deps) {
  switch (plan.strategy) {
    case 'rolling':
      return deps.rollingUpdate(plan);
    case 'canary': {
      await deps.startCanaryPods(plan);
      const out = await runCanary({
        ...deps.canaryDeps,
        service: plan.service,
        stable: plan.currentVersion,
        canary: plan.version,
      });
      if (out.result === 'promoted') {
        await deps.finaliseCanary(plan);
      } else {
        await deps.removeCanaryPods(plan);
      }
      return out;
    }
    default:
      throw new Error(`unknown strategy ${plan.strategy}`);
  }
}

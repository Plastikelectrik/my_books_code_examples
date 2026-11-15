// Book: Node.js for DevOps Engineers — Example 128
// src/canary/traffic.js
/**
 * @typedef {object} TrafficRouter
 * @property {(weight: number) => Promise<void>} setCanary
 *   Send `weight` percent of traffic to the canary.
 */

export function loggingRouter(inner, log) {
  return {
    async setCanary(weight) {
      log(`traffic: canary ${weight}%`);
      await inner.setCanary(weight);
    },
  };
}

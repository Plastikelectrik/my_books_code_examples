// Book: Node.js for DevOps Engineers — Example 131
// test/canary-controller.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { runCanary } from '../src/canary/controller.js';
import { memoryRouter } from '../src/canary/traffic.js';

const healthy = { requests: 1000, errorRate: 0.001,
  p95Ms: 120, p99Ms: 300 };

test('promotes a healthy canary', async () => {
  const router = memoryRouter();
  const out = await runCanary({
    router, service: 'tracking', stable: 'v1', canary: 'v2',
    snapshot: async () => healthy,
    wait: async () => {}, log: () => {},
  });
  assert.equal(out.result, 'promoted');
  assert.deepEqual(router.history, [5, 25, 50, 100]);
});

test('rolls back when canary errors spike', async () => {
  const router = memoryRouter();
  const out = await runCanary({
    router, service: 'tracking', stable: 'v1', canary: 'v2',
    snapshot: async (s, v) => v === 'v2'
      ? { ...healthy, errorRate: 0.05 } : healthy,
    wait: async () => {}, log: () => {},
  });
  assert.equal(out.result, 'rolled-back');
  assert.deepEqual(router.history, [5, 0]);
});

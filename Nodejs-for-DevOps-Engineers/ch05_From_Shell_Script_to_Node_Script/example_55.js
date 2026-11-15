// Book: Node.js for DevOps Engineers — Example 55
// test/deploy-plan.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { planDeploy } from '../src/deploy/plan.js';

test('builds an image tag from the sha', () => {
  const p = planDeploy({
    service: 'tracking', env: 'staging', sha: 'abc123',
  });
  assert.match(p.image, /tracking:abc123$/);
  assert.equal(p.steps.length, 4);
});

test('rejects unknown environments', () => {
  assert.throws(
    () => planDeploy({
      service: 'tracking', env: 'prod', sha: 'x',
    }),
    /unknown environment: prod/,
  );
});

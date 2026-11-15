// Book: Node.js for DevOps Engineers — Example 108
// test/manifest.test.js
import { test } from 'node:test';
import { renderDeployment } from
  '../src/kube/render-deployment.js';

test('renders the tracking deployment', (t) => {
  const yaml = renderDeployment({
    name: 'tracking', image: 'kestrel/tracking:abc',
    replicas: 3,
  });
  t.assert.snapshot(yaml);
});

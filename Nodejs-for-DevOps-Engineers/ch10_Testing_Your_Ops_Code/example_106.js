// Book: Node.js for DevOps Engineers — Example 106
// test/kubectl-wrapper.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { fakeBin } from './helpers/fake-bin.js';
import { run } from '../src/lib/run.js';

test('parses kubectl JSON output', async () => {
  const { env } = await fakeBin('kubectl', `
    console.log(JSON.stringify({
      items: [{ metadata: { name: 'tracking-7d9' } }],
    }));
  `);
  const out = await run('kubectl',
    ['get', 'pods', '-o', 'json'], { env });
  const pods = JSON.parse(out).items;
  assert.equal(pods[0].metadata.name, 'tracking-7d9');
});

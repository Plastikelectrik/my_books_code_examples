// Book: Node.js for DevOps Engineers — Example 73
// test/config.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { loadConfig } from '../src/config/load.js';

test('flags override env, env overrides file', async () => {
  const cwd = await mkdtemp(path.join(tmpdir(), 'cfg-'));
  const file = { region: 'eu-west-1', timeoutMs: 1000 };
  await writeFile(path.join(cwd, 'kes.config.json'),
    JSON.stringify(file));

  const config = await loadConfig(
    { timeoutMs: 9000 },
    { cwd, env: { KES_REGION: 'us-east-1' } },
  );
  assert.equal(config.region, 'us-east-1');
  assert.equal(config.timeoutMs, 9000);
});

test('rejects a non-numeric timeout', async () => {
  await assert.rejects(
    loadConfig({}, { env: { KES_TIMEOUT_MS: '5s' } }),
    /timeoutMs/,
  );
});

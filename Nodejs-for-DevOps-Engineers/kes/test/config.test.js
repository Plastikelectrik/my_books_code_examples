import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { loadConfig, redact } from '../src/config/load.js';

async function tempDir(files = {}) {
  const dir = await mkdtemp(path.join(tmpdir(), 'kes-'));
  for (const [name, data] of Object.entries(files)) {
    await writeFile(path.join(dir, name),
      JSON.stringify(data));
  }
  return dir;
}

test('layers: defaults < file < profile < env < flags',
  async () => {
    const cwd = await tempDir({ 'kes.config.json': {
      concurrency: 4,
      profiles: { prod: { env: 'production',
        region: 'us-east-1' } },
    } });
    const userDir = await tempDir();
    const c = await loadConfig(
      { profile: 'prod', timeout: '9000' },
      { cwd, userDir, env: { KES_CONCURRENCY: '16' } });
    assert.equal(c.env, 'production');
    assert.equal(c.region, 'us-east-1');
    assert.equal(c.concurrency, 16);
    assert.equal(c.timeoutMs, 9000);
    assert.ok(Object.isFrozen(c));
  });

test('invalid values fail with exit code 2', async () => {
  const cwd = await tempDir();
  await assert.rejects(
    loadConfig({ env: 'qa' }, { cwd, userDir: cwd, env: {} }),
    (err) => err.exitCode === 2 && /env/.test(err.message));
});

test('unknown profile lists the available ones', async () => {
  const cwd = await tempDir({ 'kes.config.json':
    { profiles: { dev: {} } } });
  await assert.rejects(
    loadConfig({ profile: 'prod' },
      { cwd, userDir: cwd, env: {} }),
    /available: dev/);
});

test('redact hides webhook-like keys', () => {
  const r = redact({ env: 'dev',
    slackWebhook: 'https://hooks.example.com/x' });
  assert.equal(r.slackWebhook, '***');
  assert.equal(r.env, 'dev');
});

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { fileURLToPath } from 'node:url';

const run = promisify(execFile);
const root = fileURLToPath(new URL('..', import.meta.url));

function kes(...args) {
  return run(process.execPath, ['src/cli.js', ...args],
    { cwd: root, env: { ...process.env, KES_ENV: '' } })
    .then((r) => ({ ...r, code: 0 }))
    .catch((e) => ({ stdout: e.stdout, stderr: e.stderr,
      code: e.code }));
}

test('services list --json', async () => {
  const r = await kes('services', 'list', '--json');
  assert.equal(r.code, 0);
  assert.equal(JSON.parse(r.stdout).length, 4);
});

test('unknown command exits 2', async () => {
  const r = await kes('nope');
  assert.equal(r.code, 2);
  assert.match(r.stderr, /unknown command/);
});

test('deploy is a dry run by default', async () => {
  const r = await kes('deploy', 'orders-api', '--env',
    'staging', '--sha', 'abc1234', '--json');
  assert.equal(r.code, 0);
  assert.equal(JSON.parse(r.stdout).steps.length, 4);
});

test('kube audit fails on the bad manifest', async () => {
  const r = await kes('kube', 'audit', 'deploy/orders-api.yaml',
    '--json');
  assert.equal(r.code, 1);
  const rows = JSON.parse(r.stdout);
  assert.deepEqual(rows.map((x) => x.failures.length), [0, 7]);
});

test('canary demo --bad rolls back', async () => {
  const r = await kes('canary', 'demo', '--bad', '--json');
  assert.equal(r.code, 1);
  assert.equal(JSON.parse(r.stdout).result, 'rolled-back');
});

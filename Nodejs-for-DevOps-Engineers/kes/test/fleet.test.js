import { test } from 'node:test';
import assert from 'node:assert/strict';
import { makeInventory } from '../src/fleet/inventory.js';
import { shq } from '../src/fleet/shell-quote.js';
import { groupResults } from '../src/fleet/group-output.js';
import { runOnFleet } from '../src/fleet/run.js';
import { rolling } from '../src/fleet/rolling.js';
import { parseDf } from '../src/fleet/disk.js';

const inv = makeInventory({
  defaults: { user: 'deploy' },
  hosts: [
    { name: 'db1', groups: ['db', 'eu'],
      tags: { role: 'primary' } },
    { name: 'db2', groups: ['db', 'us'],
      tags: { role: 'replica' } },
    { name: 'web1', groups: ['web', 'eu'] },
  ],
});
const names = (hs) => hs.map((h) => h.name);

test('inventory queries', () => {
  assert.deepEqual(names(inv.select('db')), ['db1', 'db2']);
  assert.deepEqual(names(inv.select('db,eu')), ['db1']);
  assert.deepEqual(names(inv.select('web|role=replica')),
    ['db2', 'web1']);
  assert.equal(inv.byName('web1').user, 'deploy');
});

test('shq quotes single quotes safely', () => {
  assert.equal(shq("it's"), `'it'\\''s'`);
});

test('groupResults merges identical output', () => {
  const g = groupResults([
    { host: 'a', code: 0, stdout: 'v1\n', stderr: '' },
    { host: 'b', code: 0, stdout: 'v1', stderr: '' },
    { host: 'c', code: 255, stdout: '', stderr: 'timeout' },
  ]);
  assert.deepEqual(g[0], ['v1', ['a', 'b']]);
  assert.match(g[1][0], /ERROR \(255\)/);
});

test('runOnFleet uses the injected exec', async () => {
  const exec = async (host) => ({ host, code: 0,
    stdout: 'ok', stderr: '' });
  const r = await runOnFleet(inv.all, 'uptime',
    { exec, concurrency: 2 });
  assert.equal(r.length, 3);
  assert.ok(r.every((x) => typeof x.ms === 'number'));
});

test('rolling stops at the failure budget', async () => {
  const hosts = Array.from({ length: 8 },
    (_, i) => ({ name: `h${i}` }));
  const task = async (h) => ({ host: h.name,
    ok: h.name !== 'h3' });
  const r = await rolling(hosts, task,
    { batchSizes: [1, 2, 5], maxFailures: 1, log: () => {} });
  assert.equal(r.completed, false);
  assert.equal(r.results.length, 8);
  const r2 = await rolling(hosts.slice(0, 3), task,
    { log: () => {} });
  assert.equal(r2.completed, true);
});

test('parseDf reads the use percentage', () => {
  const out = 'Filesystem 1024-blocks Used Available ' +
    'Capacity Mounted on\n/dev/sda1 100 87 13 87% /\n';
  assert.equal(parseDf(out), 87);
  assert.equal(parseDf('garbage'), null);
});

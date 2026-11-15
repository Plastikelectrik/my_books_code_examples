import { test } from 'node:test';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { loadCatalog, makeCatalog }
  from '../src/catalog/load.js';
import { ServiceSchema } from '../src/catalog/schema.js';

const file = fileURLToPath(
  new URL('../services.yaml', import.meta.url));

test('the example catalogue is valid', async () => {
  const cat = await loadCatalog(file);
  assert.equal(cat.all().length, 4);
  assert.equal(cat.get('orders-api').tier, 1);
  assert.deepEqual(cat.byTeam('warehouse').map((s) => s.name),
    ['inventory', 'label-printer']);
  assert.deepEqual(cat.dependents('payments')
    .map((s) => s.name), ['orders-api']);
});

test('unknown fields and bad names are rejected', () => {
  const r = ServiceSchema.safeParse({ name: 'Bad Name',
    extra: true });
  assert.equal(r.success, false);
});

test('get() throws a CliError for unknown services', () => {
  assert.throws(() => makeCatalog([]).get('x'),
    (e) => e.exitCode === 2);
});

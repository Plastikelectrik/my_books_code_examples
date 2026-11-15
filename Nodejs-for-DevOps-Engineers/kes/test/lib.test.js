import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mapLimit } from '../src/lib/pool.js';
import { retry, RetryableError } from '../src/lib/retry.js';
import { waitFor } from '../src/lib/wait-for.js';
import { daysUntil } from '../src/lib/days.js';
import { parseNextLink } from '../src/lib/paginate.js';
import { exitCodeFor, CliError } from '../src/lib/errors.js';
import { Secret } from '../src/secrets/secret.js';
import { inspect } from 'node:util';

test('mapLimit keeps order and limits concurrency', async () => {
  let active = 0;
  let peak = 0;
  const out = await mapLimit([1, 2, 3, 4, 5], 2, async (n) => {
    active++;
    peak = Math.max(peak, active);
    await new Promise((r) => setTimeout(r, 5));
    active--;
    return n * 10;
  });
  assert.deepEqual(out, [10, 20, 30, 40, 50]);
  assert.equal(peak, 2);
});

test('retry retries retryable errors only', async () => {
  let calls = 0;
  const value = await retry(async () => {
    calls++;
    if (calls < 3) throw new RetryableError('flaky');
    return 'ok';
  }, { sleepFn: async () => {} });
  assert.equal(value, 'ok');
  assert.equal(calls, 3);

  let n = 0;
  await assert.rejects(retry(async () => {
    n++;
    throw new Error('bad input');
  }, { sleepFn: async () => {} }), /bad input/);
  assert.equal(n, 1);
});

test('waitFor returns the value or times out', async () => {
  let i = 0;
  const v = await waitFor(async () => ({ done: ++i === 3,
    value: i }), { sleepFn: async () => {}, intervalMs: 1 });
  assert.equal(v, 3);
  await assert.rejects(waitFor(async () => ({ done: false }),
    { timeoutMs: 0, intervalMs: 10, label: 'rollout' }),
  /rollout not met/);
});

test('daysUntil counts whole days', () => {
  const now = new Date('2026-01-01T00:00:00Z');
  const later = new Date('2026-01-11T12:00:00Z');
  assert.equal(daysUntil(later, now), 10);
});

test('parseNextLink reads the rel="next" link', () => {
  const h = '<https://api.example.com/x?page=2>; rel="next", ' +
    '<https://api.example.com/x?page=9>; rel="last"';
  assert.equal(parseNextLink(h), '/x?page=2');
  assert.equal(parseNextLink(null), null);
});

test('exit codes', () => {
  assert.equal(exitCodeFor(new CliError('x', { code: 3 })), 3);
  const t = new Error('t');
  t.name = 'TimeoutError';
  assert.equal(exitCodeFor(t), 124);
  assert.equal(exitCodeFor(new Error('x')), 1);
});

test('Secret never prints its value', () => {
  const s = new Secret('hunter2');
  assert.equal(`${s}`, '[secret]');
  assert.equal(JSON.stringify({ s }), '{"s":"[secret]"}');
  assert.equal(inspect(s), '[secret]');
  assert.equal(s.reveal(), 'hunter2');
});

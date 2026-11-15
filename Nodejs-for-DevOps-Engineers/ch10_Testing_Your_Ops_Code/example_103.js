// Book: Node.js for DevOps Engineers — Example 103
// test/wait-for.test.js
import { test, mock } from 'node:test';
import assert from 'node:assert/strict';

test('polls until the condition is true', async (t) => {
  t.mock.timers.enable({
    apis: ['setTimeout', 'Date'],
  });
  const { waitFor } = await import(
    '../src/lib/wait-for.js');

  let calls = 0;
  const done = waitFor(
    async () => ({ done: ++calls === 3 }),
    { intervalMs: 5000, timeoutMs: 60_000 },
  );

  for (let i = 0; i < 2; i++) {
    await Promise.resolve();
    await Promise.resolve();
    t.mock.timers.tick(5000);
  }
  await done;
  assert.equal(calls, 3);
});

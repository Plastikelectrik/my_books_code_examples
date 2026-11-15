// Book: Node.js for DevOps Engineers — Example 104
// test/with-module-mock.test.js
import { test, mock } from 'node:test';
import assert from 'node:assert/strict';

test('uses a fake run()', async () => {
  mock.module('../src/lib/run.js', {
    namedExports: {
      run: async () => 'abc1234',
    },
  });
  const { currentSha } = await import('../src/lib/git.js');
  assert.equal(await currentSha(), 'abc1234');
});

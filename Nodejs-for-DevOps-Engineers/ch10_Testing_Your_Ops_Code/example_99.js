// Book: Node.js for DevOps Engineers — Example 99
// test/tour.test.js
import {
  describe, it, before, after,
} from 'node:test';
import assert from 'node:assert/strict';

describe('feature', () => {
  before(() => { /* once before all tests */ });
  after(() => { /* once after all tests */ });

  it('works synchronously', () => {
    assert.equal(1 + 1, 2);
  });

  it('works with async code', async () => {
    const value = await Promise.resolve(42);
    assert.equal(value, 42);
  });

  it.skip('is skipped for now', () => {});

  it.todo('describes something to write later');
});

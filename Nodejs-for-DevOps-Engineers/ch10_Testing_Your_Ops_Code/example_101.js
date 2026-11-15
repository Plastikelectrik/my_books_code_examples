// Book: Node.js for DevOps Engineers — Example 101
// test/select-old.test.js
import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { selectForDeletion } from
  '../src/registry/select-old.js';

const NOW = Date.parse('2026-06-01');
const daysAgo = (n) => NOW - n * 86_400_000;
const img = (repo, age, tags = []) => ({
  repo, tags,
  pushedAt: daysAgo(age),
  id: `${repo}@${age}`,
});

describe('selectForDeletion', () => {
  it('keeps the newest N per repo even if old', () => {
    const images = [100, 101, 102]
      .map((d) => img('api', d));
    const out = selectForDeletion(images,
      { keepLatest: 3, now: NOW });
    assert.equal(out.length, 0);
  });

  it('deletes old images beyond the newest N', () => {
    const images = [1, 2, 40, 50].map((d) => img('api', d));
    const out = selectForDeletion(images,
      { keepLatest: 2, now: NOW });
    assert.deepEqual(out.map((i) => i.id),
      ['api@40', 'api@50']);
  });

  it('never deletes release tags', () => {
    const images = [
      img('api', 1), img('api', 400, ['v1.2.3']),
    ];
    const out = selectForDeletion(images,
      { keepLatest: 1, now: NOW });
    assert.equal(out.length, 0);
  });

  it('counts each repository separately', () => {
    const images = [
      img('api', 90), img('billing', 90),
    ];
    const out = selectForDeletion(images,
      { keepLatest: 1, now: NOW });
    assert.equal(out.length, 0);
  });
});

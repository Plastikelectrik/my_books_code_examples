// Book: Node.js for DevOps Engineers — Example 11
// test/days.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { daysUntil } from '../src/lib/days.js';

test('counts whole days remaining', () => {
  const now = new Date('2026-01-01T00:00:00Z');
  const later = new Date('2026-01-11T12:00:00Z');
  assert.equal(daysUntil(later, now), 10);
});

test('is negative for past dates', () => {
  const now = new Date('2026-01-10T00:00:00Z');
  const past = new Date('2026-01-08T00:00:00Z');
  assert.equal(daysUntil(past, now), -2);
});

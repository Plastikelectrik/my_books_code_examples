// Book: Node.js for DevOps Engineers — Example 190
// test/tag-creator.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { tagsFromEvent } from
  '../functions/tag-creator/logic.js';

test('extracts instance ids and creator', async () => {
  const event = JSON.parse(await readFile(
    'test/fixtures/run-instances.json', 'utf8'));
  const out = tagsFromEvent(event.detail);
  assert.deepEqual(out.ids, ['i-0abc123']);
  assert.match(out.tags[0].Value, /assumed-role/);
});

test('ignores other events', () => {
  assert.equal(
    tagsFromEvent({ eventName: 'StopInstances' }), null);
});

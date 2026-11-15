// Book: Node.js for DevOps Engineers — Example 102
// test/shell-quote.test.js
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { shq } from '../src/fleet/shell-quote.js';

const cases = [
  ['simple', `'simple'`],
  ['with space', `'with space'`],
  [`it's`, `'it'\\''s'`],
  ['$(rm -rf /)', `'$(rm -rf /)'`],
  ['', `''`],
];

for (const [input, expected] of cases) {
  test(`shq(${JSON.stringify(input)})`, () => {
    assert.equal(shq(input), expected);
  });
}

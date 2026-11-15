// Book: Node.js for DevOps Engineers — Example 90
// src/fleet/host-keys.js
import { createHash } from 'node:crypto';
import { inventory } from './inventory.js';

export function verifyKnown(host, key) {
  const fp = 'SHA256:' + createHash('sha256')
    .update(key)
    .digest('base64')
    .replace(/=+$/, '');
  const expected = inventory.byName(host)?.hostKey;
  return expected !== undefined && fp === expected;
}

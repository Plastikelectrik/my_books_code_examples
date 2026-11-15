// Book: Node.js for DevOps Engineers — Example 134
// src/flags/simple-flags.js
import { createHash } from 'node:crypto';

export function isEnabled(flag, userId, flags) {
  const rule = flags[flag];
  if (!rule) return false;
  if (rule.users?.includes(userId)) return true;
  const hash = createHash('sha256')
    .update(`${flag}:${userId}`).digest();
  const bucket = hash.readUInt32BE(0) % 100;
  return bucket < (rule.percent ?? 0);
}

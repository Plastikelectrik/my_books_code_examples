// Book: Node.js for DevOps Engineers — Example 83
// src/webhooks/verify.js
import { createHmac, timingSafeEqual } from 'node:crypto';

export function verifySignature(rawBody, header, secret) {
  if (!header?.startsWith('sha256=')) return false;
  const expected = createHmac('sha256', secret)
    .update(rawBody)
    .digest();
  const given = Buffer.from(header.slice(7), 'hex');
  return given.length === expected.length
    && timingSafeEqual(given, expected);
}

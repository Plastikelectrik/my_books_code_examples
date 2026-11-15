// Book: Node.js for DevOps Engineers — Example 207
// src/chatops/verify.js
import { createHmac, timingSafeEqual } from 'node:crypto';

const MAX_SKEW_S = 300;

export function verifyChatRequest(raw, headers, secret) {
  const ts = Number(headers['x-request-timestamp']);
  const now = Math.floor(Date.now() / 1000);
  if (!ts || Math.abs(now - ts) > MAX_SKEW_S) return false;

  const base = `v0:${ts}:${raw}`;
  const mac = 'v0=' + createHmac('sha256', secret)
    .update(base).digest('hex');
  const given = String(headers['x-signature'] ?? '');
  return mac.length === given.length
    && timingSafeEqual(Buffer.from(mac),
      Buffer.from(given));
}

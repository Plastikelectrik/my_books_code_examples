// Book: Node.js for DevOps Engineers — Example 209
// src/chatops/approvals.js
const pending = new Map();
const TTL_MS = 10 * 60_000;

export function requestApproval(action) {
  const id = crypto.randomUUID();
  pending.set(id, { ...action, at: Date.now() });
  return id;
}

export function approve(id, approver, perms) {
  const p = pending.get(id);
  if (!p) {
    return { ok: false, reason: 'unknown or expired' };
  }
  if (Date.now() - p.at > TTL_MS) {
    pending.delete(id);
    return { ok: false, reason: 'expired' };
  }
  if (approver === p.actor) {
    return { ok: false, reason: 'own request' };
  }
  if (!perms.deployers.includes(approver)) {
    return { ok: false, reason: 'not authorised' };
  }
  pending.delete(id);
  return { ok: true, action: p };
}

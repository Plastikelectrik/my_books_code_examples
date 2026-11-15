// Book: Node.js for DevOps Engineers — Example 202
// src/alerts/state.js
import { DatabaseSync } from 'node:sqlite';

const db = new DatabaseSync(process.env.ALERT_DB ??
  'alerts.db');
db.exec(`CREATE TABLE IF NOT EXISTS alerts (
  key TEXT PRIMARY KEY, status TEXT, severity TEXT,
  first_seen TEXT, last_seen TEXT, notified_at TEXT,
  message_ref TEXT, count INTEGER)`);

const REMIND_MS = 4 * 3_600_000;

export function decide(alert, now = Date.now()) {
  const row = db
    .prepare('SELECT * FROM alerts WHERE key = ?')
    .get(alert.key);

  if (!row) {
    return alert.status === 'firing'
      ? { action: 'notify' } : { action: 'ignore' };
  }
  if (alert.status === 'resolved') {
    return row.status === 'firing'
      ? { action: 'resolve', ref: row.message_ref }
      : { action: 'ignore' };
  }
  if (row.status === 'resolved') {
    return { action: 'notify', reopened: true };
  }
  if (alert.severity !== row.severity) {
    return { action: 'update', ref: row.message_ref };
  }
  const last = Date.parse(row.notified_at);
  return now - last > REMIND_MS
    ? { action: 'remind', ref: row.message_ref }
    : { action: 'count', ref: row.message_ref };
}

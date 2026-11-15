// Alert deduplication state (Chapter 22).
import { DatabaseSync } from 'node:sqlite';

const REMIND_MS = 4 * 3_600_000;

export function createState(db = new DatabaseSync(':memory:')) {
  db.exec(`CREATE TABLE IF NOT EXISTS alerts (
    key TEXT PRIMARY KEY, status TEXT, severity TEXT,
    first_seen TEXT, last_seen TEXT, notified_at TEXT,
    message_ref TEXT, count INTEGER)`);

  const get = (key) => db
    .prepare('SELECT * FROM alerts WHERE key = ?')
    .get(key);

  function decide(alert, now = Date.now()) {
    const row = get(alert.key);
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

  function record(alert, decision, now = Date.now(),
    ref = null) {
    if (decision.action === 'ignore') return;
    const at = new Date(now).toISOString();
    const row = get(alert.key);
    if (!row) {
      db.prepare(`INSERT INTO alerts VALUES
        (?, ?, ?, ?, ?, ?, ?, 1)`).run(alert.key,
        alert.status, alert.severity, at, at, at, ref);
      return;
    }
    const notified = ['notify', 'remind', 'update']
      .includes(decision.action) ? at : row.notified_at;
    db.prepare(`UPDATE alerts SET status = ?, severity = ?,
      last_seen = ?, notified_at = ?, count = count + 1
      WHERE key = ?`).run(alert.status, alert.severity,
      at, notified, alert.key);
  }

  return { decide, record };
}

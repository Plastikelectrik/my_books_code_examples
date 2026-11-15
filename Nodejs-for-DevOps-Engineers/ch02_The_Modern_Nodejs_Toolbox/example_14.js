// Book: Node.js for DevOps Engineers — Example 14
// scripts/seen-alerts.js
import { DatabaseSync } from 'node:sqlite';

const db = new DatabaseSync('kes-state.db');
db.exec(`CREATE TABLE IF NOT EXISTS alerts (
  id TEXT PRIMARY KEY, sent_at TEXT)`);

export function alreadySent(id) {
  const row = db
    .prepare('SELECT 1 FROM alerts WHERE id = ?')
    .get(id);
  return Boolean(row);
}

export function markSent(id) {
  db.prepare(
    'INSERT OR IGNORE INTO alerts VALUES (?, ?)',
  ).run(id, new Date().toISOString());
}

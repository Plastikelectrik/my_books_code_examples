// Book: Node.js for DevOps Engineers — Example 133
// src/deploy/history.js
import { DatabaseSync } from 'node:sqlite';

const db = new DatabaseSync('deploys.db');
db.exec(`CREATE TABLE IF NOT EXISTS deploys (
  service TEXT, version TEXT, digest TEXT,
  env TEXT, at TEXT, actor TEXT, result TEXT)`);

export function record(d) {
  db.prepare(`INSERT INTO deploys VALUES
    (?, ?, ?, ?, ?, ?, ?)`).run(d.service, d.version,
    d.digest, d.env, new Date().toISOString(),
    d.actor, d.result);
}

export function lastGood(service, env, exceptVersion) {
  return db.prepare(`SELECT * FROM deploys
    WHERE service = ? AND env = ? AND result = 'promoted'
      AND version != ?
    ORDER BY at DESC LIMIT 1`)
    .get(service, env, exceptVersion);
}

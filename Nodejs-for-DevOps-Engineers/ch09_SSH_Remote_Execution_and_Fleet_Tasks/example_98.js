// Book: Node.js for DevOps Engineers — Example 98
// src/fleet/audit-log.js
import { appendFile } from 'node:fs/promises';
import os from 'node:os';

export async function auditFleetRun(entry) {
  const line = JSON.stringify({
    at: new Date().toISOString(),
    user: os.userInfo().username,
    host: os.hostname(),
    ...entry,
  });
  await appendFile('fleet-audit.jsonl', line + '\n');
}

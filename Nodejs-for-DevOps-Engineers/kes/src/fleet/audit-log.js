// Record every fleet change (Chapter 9).
import { appendFile } from 'node:fs/promises';
import os from 'node:os';

export async function auditFleetRun(entry,
  file = 'fleet-audit.jsonl') {
  const line = JSON.stringify({
    at: new Date().toISOString(),
    user: os.userInfo().username,
    host: os.hostname(),
    ...entry,
  });
  await appendFile(file, line + '\n');
}

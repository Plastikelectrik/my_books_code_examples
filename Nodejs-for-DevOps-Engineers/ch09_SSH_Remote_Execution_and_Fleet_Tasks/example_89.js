// Book: Node.js for DevOps Engineers — Example 89
// src/fleet/ssh-lib.js
import { Client } from 'ssh2';
import { readFile } from 'node:fs/promises';
import { verifyKnown } from './host-keys.js';

export async function connect(target) {
  const { host, user, keyPath, port = 22 } = target;
  const privateKey = await readFile(keyPath);
  return new Promise((resolve, reject) => {
    const conn = new Client();
    conn
      .on('ready', () => resolve(conn))
      .on('error', reject)
      .connect({
        host, port, username: user, privateKey,
        readyTimeout: 10_000,
        hostVerifier: (key) => verifyKnown(host, key),
      });
  });
}

export function exec(conn, command) {
  return new Promise((resolve, reject) => {
    conn.exec(command, (err, stream) => {
      if (err) return reject(err);
      let stdout = '';
      let stderr = '';
      stream
        .on('data', (d) => (stdout += d))
        .on('close', (code) =>
          resolve({ code, stdout, stderr }));
      stream.stderr.on('data', (d) => (stderr += d));
    });
  });
}

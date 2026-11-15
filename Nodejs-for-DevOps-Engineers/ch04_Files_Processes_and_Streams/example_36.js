// Book: Node.js for DevOps Engineers — Example 36
// src/lib/stream-run.js
import { spawn } from 'node:child_process';
import { once } from 'node:events';

export async function streamRun(cmd, args, opts = {}) {
  const child = spawn(cmd, args, {
    stdio: ['ignore', 'inherit', 'inherit'],
    ...opts,
  });
  const [code, signal] = await once(child, 'exit');
  if (code !== 0) {
    const why = signal
      ? `signal ${signal}`
      : `code ${code}`;
    throw new Error(`${cmd} exited with ${why}`);
  }
}

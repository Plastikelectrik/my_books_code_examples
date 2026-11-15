// Run one command on one host through the system ssh (Chapter 9).
import { spawn } from 'node:child_process';
import { once } from 'node:events';

export async function sshExec(host, command, opts = {}) {
  const { timeoutMs = 60_000, user } = opts;
  const target = user ? `${user}@${host}` : host;
  const args = [
    '-o', 'BatchMode=yes',
    '-o', 'ConnectTimeout=10',
    '-o', 'StrictHostKeyChecking=yes',
    target,
    '--',
    command,
  ];

  const child = spawn('ssh', args, {
    signal: AbortSignal.timeout(timeoutMs),
  });
  let stdout = '';
  let stderr = '';
  child.stdout.on('data', (d) => (stdout += d));
  child.stderr.on('data', (d) => (stderr += d));

  try {
    const [code] = await once(child, 'close');
    return { host, code, stdout, stderr };
  } catch (err) {
    return { host, code: null, stdout, stderr,
      error: err.name };
  }
}

// Book: Node.js for DevOps Engineers — Example 34
// src/lib/run.js
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const execFileP = promisify(execFile);

export async function run(cmd, args = [], opts = {}) {
  try {
    const { stdout } = await execFileP(cmd, args, {
      maxBuffer: 50 * 1024 * 1024,
      timeout: opts.timeoutMs ?? 60_000,
      ...opts,
    });
    return stdout.trim();
  } catch (err) {
    const detail = err.stderr?.trim() || err.message;
    throw new Error(
      `${cmd} ${args.join(' ')} failed: ${detail}`,
      { cause: err },
    );
  }
}

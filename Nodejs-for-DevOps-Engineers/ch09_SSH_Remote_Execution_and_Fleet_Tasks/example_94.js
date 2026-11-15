// Book: Node.js for DevOps Engineers — Example 94
// src/fleet/run.js
import { mapLimit } from '../lib/pool.js';
import { sshExec } from './ssh-binary.js';

export async function runOnFleet(hosts, command, opts) {
  opts ??= {};
  const { concurrency = 10, onResult = () => {} } = opts;
  return mapLimit(hosts, concurrency, async (h) => {
    const t0 = performance.now();
    const r = await sshExec(h.name, command, {
      user: h.user,
      timeoutMs: opts.timeoutMs,
    });
    r.ms = Math.round(performance.now() - t0);
    onResult(r);
    return r;
  });
}

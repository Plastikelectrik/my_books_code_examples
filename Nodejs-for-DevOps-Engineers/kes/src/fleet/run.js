// Run a command across many hosts, N at a time (Chapter 9).
import { mapLimit } from '../lib/pool.js';
import { sshExec } from './ssh-binary.js';

export async function runOnFleet(hosts, command, opts) {
  opts ??= {};
  const { concurrency = 10, onResult = () => {},
    exec = sshExec } = opts;
  return mapLimit(hosts, concurrency, async (h) => {
    const t0 = performance.now();
    const r = await exec(h.name, command, {
      user: h.user,
      timeoutMs: opts.timeoutMs,
    });
    r.ms = Math.round(performance.now() - t0);
    onResult(r);
    return r;
  });
}

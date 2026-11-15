// Book: Node.js for DevOps Engineers — Example 60
// src/commands/health.js (run function)
import { mapLimit } from '../lib/pool.js';
import { loadServices } from '../lib/services.js';
import { CliError } from '../lib/errors.js';

export async function run({ values, out }) {
  const all = await loadServices();
  const services = values.service
    ? all.filter((s) => s.name === values.service)
    : all;
  if (services.length === 0) {
    throw new CliError(`no service named ${values.service}`,
      { code: 2 });
  }

  const timeout = Number(values.timeout);
  out.info(`checking ${services.length} services...`);
  const results = await mapLimit(services, 8, async (s) => {
    const t0 = performance.now();
    try {
      const res = await fetch(`${s.url}/health`, {
        signal: AbortSignal.timeout(timeout),
      });
      const ms = Math.round(performance.now() - t0);
      return {
        name: s.name, ok: res.ok, status: res.status, ms,
      };
    } catch (err) {
      return { name: s.name, ok: false, error: err.name };
    }
  });

  out.result(results, (rows) => {
    for (const r of rows) {
      const detail = r.ok
        ? `${r.ms}ms`
        : (r.error ?? r.status);
      const line = `${r.name.padEnd(16)} ${detail}`;
      console.log(r.ok ? out.ok(line) : out.bad(line));
    }
  });

  if (results.some((r) => !r.ok)) process.exitCode = 1;
}

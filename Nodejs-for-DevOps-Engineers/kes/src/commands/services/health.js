import { mapLimit } from '../../lib/pool.js';
import { CliError } from '../../lib/errors.js';

export const meta = {
  name: 'health',
  summary: 'Check health endpoints of all services',
  usage: 'kes health [--service NAME] [--json]',
  options: {
    service: { type: 'string', short: 's',
      description: 'Only check this service' },
  },
};

export async function run(ctx, { values }) {
  const all = (await ctx.catalog()).all()
    .filter((s) => s.health);
  const services = values.service
    ? all.filter((s) => s.name === values.service)
    : all;
  if (services.length === 0) {
    throw new CliError('no service with a health URL ' +
      `matches ${values.service ?? '(all)'}`, { code: 2 });
  }

  const timeout = ctx.config.timeoutMs;
  ctx.out.info(`checking ${services.length} services...`);
  const results = await mapLimit(services,
    ctx.config.concurrency, async (s) => {
      const t0 = performance.now();
      try {
        const res = await fetch(s.health.url, {
          signal: AbortSignal.timeout(timeout),
        });
        await res.body?.cancel();
        const ms = Math.round(performance.now() - t0);
        return {
          name: s.name, ok: res.ok, status: res.status, ms,
        };
      } catch (err) {
        return { name: s.name, ok: false,
          error: err.cause?.code ?? err.name };
      }
    });

  ctx.out.result(results, (rows) => {
    for (const r of rows) {
      const detail = r.ok
        ? `${r.ms}ms`
        : (r.error ?? r.status);
      const line = `${r.name.padEnd(16)} ${detail}`;
      console.log(r.ok ? ctx.out.ok(line) : ctx.out.bad(line));
    }
  });
  if (results.some((r) => !r.ok)) process.exitCode = 1;
}

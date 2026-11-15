import { runCanary } from '../../canary/controller.js';
import { memoryRouter, loggingRouter }
  from '../../canary/traffic.js';

export const meta = {
  name: 'canary demo',
  summary: 'Simulate a canary rollout with fake metrics',
  usage: 'kes canary demo [--bad]',
  options: {
    bad: { type: 'boolean', default: false,
      description: 'Make the canary misbehave' },
  },
};

export async function run(ctx, { values }) {
  const router = loggingRouter(memoryRouter(),
    (m) => ctx.out.info(m));
  const healthy = { requests: 900, errorRate: 0.002,
    p95Ms: 120, p99Ms: 250 };
  const broken = { ...healthy, errorRate: 0.04 };
  const result = await runCanary({
    service: 'orders-api', stable: 'v1', canary: 'v2',
    router,
    bakeMs: 1000,
    wait: async () => {},
    log: (m) => ctx.out.info(m),
    snapshot: async (svc, version) =>
      version === 'v2' && values.bad ? broken : healthy,
  });
  ctx.out.result(result, (r) => console.log(
    r.result === 'promoted'
      ? ctx.out.ok('canary promoted to 100%')
      : ctx.out.bad(`rolled back at ${r.weight}%`)));
  if (result.result !== 'promoted') process.exitCode = 1;
}

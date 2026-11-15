// Book: Node.js for DevOps Engineers — Example 230
// src/commands/status.js
export const meta = {
  name: 'status',
  summary: 'Show the state of a service',
  usage: 'kes status SERVICE [--json]',
  options: {},
};

export async function run(ctx, { positionals }) {
  const svc = (await ctx.catalog()).get(positionals[0]);
  const { apps } = await ctx.kube();
  const d = await apps.readNamespacedDeployment({
    name: svc.runtime.deployment,
    namespace: svc.runtime.namespace,
  });
  const st = rolloutState(d);
  ctx.out.result({ service: svc.name, ...st }, (r) => {
    console.log(`${r.service}: ${r.progress}`);
    console.log(`owner: ${svc.owner.team}`);
    console.log(`dashboard: ${svc.links.dashboard ?? '-'}`);
  });
}

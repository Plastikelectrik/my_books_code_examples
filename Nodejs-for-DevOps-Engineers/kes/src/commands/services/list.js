export const meta = {
  name: 'services list',
  summary: 'List services from the catalogue',
  usage: 'kes services list [--team NAME] [--json]',
  options: {
    team: { type: 'string', description: 'Only this team' },
  },
};

export async function run(ctx, { values }) {
  const catalog = await ctx.catalog();
  const list = values.team
    ? catalog.byTeam(values.team)
    : catalog.all();
  const rows = list.map((s) => ({
    name: s.name, team: s.owner.team, tier: s.tier,
    strategy: s.deploy.strategy,
  }));
  ctx.out.result(rows, (r) => {
    for (const s of r) {
      console.log(`${s.name.padEnd(16)} ${s.team.padEnd(10)}` +
        ` tier ${s.tier}  ${s.strategy}`);
    }
  });
}

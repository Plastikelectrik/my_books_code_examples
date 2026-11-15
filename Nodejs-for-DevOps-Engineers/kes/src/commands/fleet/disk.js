import { loadInventory } from '../../fleet/inventory.js';
import { runOnFleet } from '../../fleet/run.js';
import { parseDf } from '../../fleet/disk.js';

export const meta = {
  name: 'fleet disk',
  summary: 'Root disk usage on every host, fullest first',
  usage: 'kes fleet disk [--hosts QUERY] [--warn PCT]',
  options: {
    hosts: { type: 'string', description: 'Host query' },
    inventory: { type: 'string', default: 'inventory.yaml',
      description: 'Inventory file' },
    warn: { type: 'string', default: '85',
      description: 'Warn at this percentage' },
  },
};

export async function run(ctx, { values }) {
  const inv = await loadInventory(values.inventory);
  const results = await runOnFleet(inv.select(values.hosts),
    'df -P /', { concurrency: ctx.config.concurrency });
  const rows = results.map((r) => ({
    host: r.host,
    usedPct: r.code === 0 ? parseDf(r.stdout) : null,
  })).sort((a, b) => (b.usedPct ?? 101)
    - (a.usedPct ?? 101));
  const warn = Number(values.warn);
  ctx.out.result(rows, (list) => {
    for (const r of list) {
      const line = `${r.host.padEnd(20)} ` +
        `${r.usedPct ?? '?'}%`;
      console.log(r.usedPct !== null && r.usedPct < warn
        ? ctx.out.ok(line) : ctx.out.bad(line));
    }
  });
}

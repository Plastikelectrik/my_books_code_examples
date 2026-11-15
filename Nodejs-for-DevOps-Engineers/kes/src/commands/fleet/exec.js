import { loadInventory } from '../../fleet/inventory.js';
import { runOnFleet } from '../../fleet/run.js';
import { printGroups } from '../../fleet/group-output.js';
import { auditFleetRun } from '../../fleet/audit-log.js';
import { CliError } from '../../lib/errors.js';

export const meta = {
  name: 'fleet exec',
  summary: 'Run a command over SSH on matching hosts',
  usage: 'kes fleet exec "COMMAND" --hosts QUERY ' +
    '[--inventory FILE] [--dry-run]',
  options: {
    hosts: { type: 'string', description:
      'Host query: db | db,eu | role=replica' },
    inventory: { type: 'string', default: 'inventory.yaml',
      description: 'Inventory file' },
    'dry-run': { type: 'boolean', default: false,
      description: 'Only list the hosts' },
  },
};

export async function run(ctx, { values, positionals }) {
  const command = positionals.join(' ');
  if (!command) {
    throw new CliError('usage: ' + meta.usage, { code: 2 });
  }
  const inv = await loadInventory(values.inventory);
  const hosts = inv.select(values.hosts);
  if (!hosts.length) {
    throw new CliError(`no hosts match ${values.hosts}`,
      { code: 2 });
  }
  ctx.out.info(`${hosts.length} host(s): ` +
    hosts.map((h) => h.name).join(', '));
  if (values['dry-run']) return;

  const results = await runOnFleet(hosts, command, {
    concurrency: ctx.config.concurrency,
  });
  await auditFleetRun({ command, query: values.hosts,
    hosts: hosts.length,
    failed: results.filter((r) => r.code !== 0).length });
  ctx.out.result(results, printGroups);
  if (results.some((r) => r.code !== 0)) {
    process.exitCode = 1;
  }
}

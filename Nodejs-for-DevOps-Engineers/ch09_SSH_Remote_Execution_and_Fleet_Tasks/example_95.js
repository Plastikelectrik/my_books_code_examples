// Book: Node.js for DevOps Engineers — Example 95
// src/commands/fleet/exec.js
import { loadInventory } from '../../fleet/inventory.js';
import { runOnFleet } from '../../fleet/run.js';

export const meta = {
  name: 'fleet exec',
  summary: 'Run a read-only command on many hosts',
  usage: 'kes fleet exec --hosts QUERY -- COMMAND',
  options: {
    hosts: { type: 'string', description: 'Host query' },
    concurrency: { type: 'string', default: '10',
      description: 'Hosts at a time' },
  },
};

export async function run({ values, positionals, out }) {
  const inv = await loadInventory();
  const hosts = inv.select(values.hosts);
  const command = positionals.join(' ');
  out.info(`running on ${hosts.length} hosts: ${command}`);

  const results = await runOnFleet(hosts, command, {
    concurrency: Number(values.concurrency),
    onResult: (r) => out.info(
      `${r.code === 0 ? '✔' : '✖'} ${r.host} (${r.ms}ms)`),
  });

  out.result(results, (rows) => groupOutput(rows));
  if (results.some((r) => r.code !== 0)) {
    process.exitCode = 1;
  }
}

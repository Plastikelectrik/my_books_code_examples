import { readFile } from 'node:fs/promises';
import { planCleanup } from '../../docker/cleanup-plan.js';
import { run as runCmd } from '../../lib/run.js';
import { confirm } from '../../lib/confirm.js';

export const meta = {
  name: 'docker cleanup',
  summary: 'Remove expired or long-stopped containers ' +
    'and dangling images (dry run unless --apply)',
  usage: 'kes docker cleanup [--from STATE.json] ' +
    '[--hours N] [--apply] [--yes]',
  options: {
    from: { type: 'string',
      description: 'Read host state from a JSON file' },
    hours: { type: 'string', default: '24',
      description: 'Stopped for more than N hours' },
    apply: { type: 'boolean', default: false,
      description: 'Really remove' },
    yes: { type: 'boolean', short: 'y', default: false,
      description: 'Do not ask for confirmation' },
  },
};

async function readDockerState() {
  const ids = (await runCmd('docker', ['ps', '-aq']))
    .split('\n').filter(Boolean);
  const containers = ids.length
    ? JSON.parse(await runCmd('docker',
      ['inspect', ...ids])).map((c) => ({
      Id: c.Id,
      State: c.State.Status,
      Labels: c.Config.Labels ?? {},
      finishedAt: Date.parse(c.State.FinishedAt),
    }))
    : [];
  const dangling = (await runCmd('docker', ['images', '-q',
    '--no-trunc', '--filter', 'dangling=true']))
    .split('\n').filter(Boolean);
  return { containers,
    images: dangling.map((Id) => ({ Id, RepoTags: [] })) };
}

export async function run(ctx, { values }) {
  const state = values.from
    ? JSON.parse(await readFile(values.from, 'utf8'))
    : await readDockerState();
  const actions = planCleanup(state, {
    now: Date.now(),
    maxStoppedHours: Number(values.hours),
  });
  ctx.out.result(actions, (list) => {
    if (!list.length) console.log('nothing to clean');
    for (const a of list) {
      console.log(`${a.kind.padEnd(10)} ` +
        `${a.id.slice(0, 12)}  ${a.reason}`);
    }
  });
  if (!values.apply || !actions.length) return;
  if (values.from) {
    ctx.out.info('--apply ignored with --from');
    return;
  }
  if (!await confirm(`Remove ${actions.length} item(s)?`,
    values)) return;
  for (const a of actions) {
    const args = a.kind === 'image'
      ? ['rmi', a.id]
      : ['rm', ...(a.force ? ['-f'] : []), a.id];
    await runCmd('docker', args);
  }
  ctx.out.info(`removed ${actions.length} item(s)`);
}

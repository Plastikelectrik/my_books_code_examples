// Run a plan, or only print it (Chapter 5).
import { styleText } from 'node:util';
import { streamRun } from '../lib/stream-run.js';

export async function executePlan(plan, opts = {}) {
  const { dryRun = true, runner = streamRun,
    log = console.error } = opts;
  for (const [cmd, args] of plan.steps) {
    const line = `${cmd} ${args.join(' ')}`;
    log(styleText('cyan', `$ ${line}`));
    if (!dryRun) await runner(cmd, args);
  }
}

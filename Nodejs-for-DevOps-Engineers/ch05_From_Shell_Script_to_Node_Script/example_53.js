// Book: Node.js for DevOps Engineers — Example 53
// src/deploy/execute.js
import { styleText } from 'node:util';
import { streamRun } from '../lib/stream-run.js';

export async function executePlan(plan, { dryRun }) {
  for (const [cmd, args] of plan.steps) {
    const line = `${cmd} ${args.join(' ')}`;
    console.log(styleText('cyan', `$ ${line}`));
    if (!dryRun) await streamRun(cmd, args);
  }
}

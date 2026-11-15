// Book: Node.js for DevOps Engineers — Example 54
// scripts/deploy.js
import { parseArgs } from 'node:util';
import { run } from '../src/lib/run.js';
import { planDeploy } from '../src/deploy/plan.js';
import { executePlan } from '../src/deploy/execute.js';

const { values, positionals } = parseArgs({
  allowPositionals: true,
  options: {
    env: { type: 'string', short: 'e', default: 'staging' },
    'dry-run': { type: 'boolean', default: false },
    yes: { type: 'boolean', short: 'y', default: false },
  },
});

const [service] = positionals;
const dirty = await run('git', ['status', '--porcelain']);
if (dirty && !values['dry-run']) {
  console.error('working tree dirty, aborting');
  process.exit(1);
}

const sha = await run('git', [
  'rev-parse', '--short', 'HEAD',
]);
const plan = planDeploy({ service, env: values.env, sha });

if (values.env === 'production' && !values.yes) {
  console.error('production deploys need --yes');
  process.exit(2);
}

await executePlan(plan, { dryRun: values['dry-run'] });
console.log(`deployed ${plan.image} to ${values.env}`);

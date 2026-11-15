import { planDeploy } from '../../deploy/plan.js';
import { executePlan } from '../../deploy/execute.js';
import { confirm } from '../../lib/confirm.js';
import { CliError } from '../../lib/errors.js';
import { run as runCmd } from '../../lib/run.js';

export const meta = {
  name: 'deploy',
  summary: 'Build, push and roll out a service ' +
    '(dry run unless --apply)',
  usage: 'kes deploy SERVICE --env ENV [--sha SHA] ' +
    '[--apply] [--yes]',
  options: {
    sha: { type: 'string',
      description: 'Git commit to deploy (default HEAD)' },
    apply: { type: 'boolean', default: false,
      description: 'Really run the commands' },
    yes: { type: 'boolean', short: 'y', default: false,
      description: 'Do not ask for confirmation' },
  },
};

export async function run(ctx, { values, positionals }) {
  const [name] = positionals;
  if (!name) {
    throw new CliError('usage: ' + meta.usage, { code: 2 });
  }
  const env = values.env ?? ctx.config.env;
  const sha = values.sha
    ?? await runCmd('git', ['rev-parse', '--short', 'HEAD']);
  const svc = (await ctx.catalog()).get(name);

  let plan;
  try {
    plan = planDeploy({ svc, env, sha,
      registry: ctx.config.registry });
  } catch (err) {
    throw new CliError(err.message, { code: 2 });
  }

  if (ctx.out.json && !values.apply) {
    return ctx.out.result(plan, () => {});
  }
  ctx.out.info(`${values.apply ? 'Deploying' : 'Plan for'} ` +
    `${plan.service} -> ${env} (${plan.image})`);
  if (values.apply) {
    const ok = await confirm(
      `Deploy ${plan.service} to ${env}?`, values);
    if (!ok) throw new CliError('cancelled', { code: 130 });
  }
  await executePlan(plan, { dryRun: !values.apply });
  if (!values.apply) {
    ctx.out.info('dry run: add --apply to execute');
  }
}

import { access } from 'node:fs/promises';
import { run as runCmd } from '../../lib/run.js';
import { CliError } from '../../lib/errors.js';

const LEVELS = ['info', 'low', 'moderate', 'high',
  'critical'];

export const meta = {
  name: 'supply audit',
  summary: 'Check the lockfile and summarise npm audit',
  usage: 'kes supply audit [--fail-on LEVEL] [--json]',
  options: {
    'fail-on': { type: 'string', default: 'high',
      description: 'Fail at this severity or above' },
  },
};

export async function run(ctx, { values }) {
  const failOn = LEVELS.indexOf(values['fail-on']);
  if (failOn < 0) {
    throw new CliError(`--fail-on must be one of ${
      LEVELS.join(', ')}`, { code: 2 });
  }
  try {
    await access('package-lock.json');
  } catch {
    throw new CliError('no package-lock.json: commit a ' +
      'lockfile and install with npm ci', { code: 1 });
  }
  let report;
  try {
    report = JSON.parse(await runCmd('npm',
      ['audit', '--json'], { timeoutMs: 120_000 }));
  } catch (err) {
    // npm audit exits 1 when it finds something
    const out = err.cause?.stdout;
    if (!out) throw err;
    report = JSON.parse(out);
  }
  const counts = report.metadata?.vulnerabilities ?? {};
  ctx.out.result(counts, (c) => {
    for (const level of LEVELS.toReversed()) {
      console.log(`${level.padEnd(10)} ${c[level] ?? 0}`);
    }
  });
  const bad = LEVELS.slice(failOn)
    .some((l) => (counts[l] ?? 0) > 0);
  if (bad) process.exitCode = 1;
}

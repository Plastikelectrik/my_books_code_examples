// Book: Node.js for DevOps Engineers — Example 170
// scripts/ci/guard-replacements.js
import { run } from '../../src/lib/run.js';

const STATEFUL = [/rds\/instance/i, /s3\/bucket/i,
  /dynamodb\/table/i, /ebs\/volume/i];

const out = await run('pulumi',
  ['preview', '--json', '--stack', process.argv[2]],
  { timeoutMs: 600_000 });
const steps = JSON.parse(out).steps ?? [];

const risky = steps.filter((s) =>
  ['replace', 'delete', 'create-replacement'].includes(s.op)
  && STATEFUL.some((re) => re.test(s.urn)));

for (const s of risky) {
  console.log(`::error::${s.op} on ${s.urn}`);
}
process.exitCode = risky.length ? 1 : 0;

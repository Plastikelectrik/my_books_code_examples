import { readFile } from 'node:fs/promises';
import { parseAllDocuments } from 'yaml';
import { auditDeployment } from '../../kube/audit.js';
import { CliError } from '../../lib/errors.js';

export const meta = {
  name: 'kube audit',
  summary: 'Check Deployment manifests against the ' +
    'platform policy',
  usage: 'kes kube audit FILE.yaml... [--json]',
  options: {},
};

export async function run(ctx, { positionals }) {
  if (!positionals.length) {
    throw new CliError('usage: ' + meta.usage, { code: 2 });
  }
  const report = [];
  for (const file of positionals) {
    const docs = parseAllDocuments(
      await readFile(file, 'utf8'));
    for (const doc of docs) {
      const obj = doc.toJS();
      if (obj?.kind !== 'Deployment') continue;
      report.push({
        file, name: obj.metadata.name,
        failures: auditDeployment(obj),
      });
    }
  }
  ctx.out.result(report, (rows) => {
    for (const r of rows) {
      if (!r.failures.length) {
        console.log(ctx.out.ok(`${r.name} (${r.file})`));
        continue;
      }
      console.log(ctx.out.bad(`${r.name} (${r.file})`));
      for (const f of r.failures) console.log(`    - ${f}`);
    }
  });
  if (report.some((r) => r.failures.length)) {
    process.exitCode = 1;
  }
}

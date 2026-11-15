// Book: Node.js for DevOps Engineers — Example 218
// scripts/ci/audit.js
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const exec = promisify(execFile);
let out;
try {
  ({ stdout: out } = await exec('npm',
    ['audit', '--json', '--omit=dev'],
    { maxBuffer: 20e6 }));
} catch (err) {
  // npm audit exits 1 when it finds issues
  out = err.stdout;
}
const report = JSON.parse(out);
const vulns = Object.values(report.vulnerabilities ?? {});

const serious = vulns.filter((v) =>
  ['high', 'critical'].includes(v.severity)
  && v.fixAvailable);

for (const v of serious) {
  const fix = typeof v.fixAvailable === 'object'
    ? `upgrade ${v.fixAvailable.name} to ` +
      v.fixAvailable.version
    : 'npm audit fix';
  const sev = v.severity.toUpperCase();
  console.log(`${sev} ${v.name}: ${fix}`);
}
process.exitCode = serious.length ? 1 : 0;

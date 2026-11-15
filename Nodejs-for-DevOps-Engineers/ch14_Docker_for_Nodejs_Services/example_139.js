// Book: Node.js for DevOps Engineers — Example 139
// scripts/ci/scan-image.js
import { run } from '../../src/lib/run.js';

const image = process.argv[2];
const out = await run('trivy', ['image', '--quiet',
  '--format', 'json', '--severity', 'HIGH,CRITICAL',
  '--ignore-unfixed', image], { timeoutMs: 300_000 });

const report = JSON.parse(out);
const vulns = (report.Results ?? [])
  .flatMap((r) => r.Vulnerabilities ?? []);

for (const v of vulns) {
  const sev = v.Severity.padEnd(8);
  const fix = `${v.InstalledVersion} -> ${v.FixedVersion}`;
  console.log(`${sev} ${v.VulnerabilityID} ` +
    `${v.PkgName} ${fix}`);
}
if (vulns.some((v) => v.Severity === 'CRITICAL')) {
  process.exitCode = 1;
}

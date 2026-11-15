// Book: Node.js for DevOps Engineers — Example 115
// scripts/ci/changed-services.js
import { run } from '../../src/lib/run.js';
import { setOutput } from './gha.js';

const base = process.env.GITHUB_BASE_REF
  ? `origin/${process.env.GITHUB_BASE_REF}`
  : 'HEAD~1';
const diff = await run('git',
  ['diff', '--name-only', `${base}...HEAD`]);

const services = [...new Set(
  diff.split('\n')
    .map((f) => f.match(/^services\/([^/]+)\//)?.[1])
    .filter(Boolean),
)];
console.log('changed services:', services);
await setOutput('services', JSON.stringify(services));

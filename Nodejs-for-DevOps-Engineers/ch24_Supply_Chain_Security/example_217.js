// Book: Node.js for DevOps Engineers — Example 217
// scripts/ci/lock-diff.js
import { readFile } from 'node:fs/promises';
import { run } from '../../src/lib/run.js';

const base = process.env.GITHUB_BASE_REF ?? 'main';
const before = JSON.parse(await run('git',
  ['show', `origin/${base}:package-lock.json`]));
const after = JSON.parse(
  await readFile('package-lock.json', 'utf8'));

const versions = (lock) => new Map(
  Object.entries(lock.packages ?? {})
    .filter(([p]) => p.startsWith('node_modules/'))
    .map(([p, v]) => [p.replace(/^.*node_modules\//, ''),
      v.version]));

const a = versions(before);
const b = versions(after);
for (const [name, v] of b) {
  if (!a.has(name)) console.log(`+ ${name}@${v}`);
  else if (a.get(name) !== v) {
    console.log(`~ ${name} ${a.get(name)} -> ${v}`);
  }
}
for (const [name, v] of a) {
  if (!b.has(name)) console.log(`- ${name}@${v}`);
}

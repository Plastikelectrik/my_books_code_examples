// Book: Node.js for DevOps Engineers — Example 216
// scripts/ci/dep-summary.js
import { run } from '../../src/lib/run.js';

const raw = await run('npm',
  ['ls', '--all', '--json', '--omit=dev']);
const tree = JSON.parse(raw);

const seen = new Map();
(function walk(deps = {}) {
  for (const [name, d] of Object.entries(deps)) {
    const key = `${name}@${d.version}`;
    if (!seen.has(key)) seen.set(key, d);
    walk(d.dependencies);
  }
})(tree.dependencies);

const names = new Set([...seen.keys()]
  .map((k) => k.slice(0, k.lastIndexOf('@'))));
console.log(`${names.size} production packages, ` +
  `${seen.size} name@version pairs`);

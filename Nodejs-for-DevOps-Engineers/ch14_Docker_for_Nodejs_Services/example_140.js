// Book: Node.js for DevOps Engineers — Example 140
// scripts/ci/image-size.js
import { run } from '../../src/lib/run.js';

async function sizeMb(image) {
  const out = await run('docker', ['image', 'inspect',
    image, '--format', '{{.Size}}']);
  return Number(out) / 1024 / 1024;
}

const [current, previous] = process.argv.slice(2);
const now = await sizeMb(current);
const before = await sizeMb(previous);
const delta = ((now - before) / before) * 100;
console.log(`${now.toFixed(1)} MB (${delta.toFixed(1)}%)`);
if (delta > 10) process.exitCode = 1;

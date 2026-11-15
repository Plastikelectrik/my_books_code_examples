// Book: Node.js for DevOps Engineers — Example 38
// src/lib/tee-run.js
import { spawn } from 'node:child_process';
import { once } from 'node:events';

export async function teeRun(cmd, args, opts = {}) {
  const child = spawn(cmd, args, { ...opts });
  const tail = [];
  const keep = (chunk, out) => {
    out.write(chunk);
    tail.push(...chunk.toString().split('\n'));
    if (tail.length > 50) tail.splice(0, tail.length - 50);
  };
  child.stdout.on('data', (c) => keep(c, process.stdout));
  child.stderr.on('data', (c) => keep(c, process.stderr));
  const [code] = await once(child, 'exit');
  return { code, tail: tail.join('\n') };
}

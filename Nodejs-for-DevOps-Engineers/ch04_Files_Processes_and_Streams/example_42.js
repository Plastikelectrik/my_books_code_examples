// Book: Node.js for DevOps Engineers — Example 42
// examples/kube-errors.js
import { spawn } from 'node:child_process';
import { createInterface } from 'node:readline';

const pod = process.argv[2];
const child = spawn('kubectl', ['logs', '-f', pod]);

const rl = createInterface({ input: child.stdout });
for await (const line of rl) {
  try {
    const entry = JSON.parse(line);
    if (entry.level === 'error') {
      console.log(`${entry.time} ${entry.msg}`);
    }
  } catch {
    // not JSON: ignore
  }
}

// Book: Node.js for DevOps Engineers — Example 47
// examples/hosts-from-stdin.js
import { readStdin } from '../src/lib/stdin.js';

const input = await readStdin();
const hosts = input.split('\n').map((s) => s.trim())
  .filter(Boolean);
console.log(`${hosts.length} hosts received`);

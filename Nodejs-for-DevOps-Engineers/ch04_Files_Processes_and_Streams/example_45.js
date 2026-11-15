// Book: Node.js for DevOps Engineers — Example 45
// examples/verify.js
import { sha256File } from '../src/lib/sha256.js';

const expected = process.env.AGENT_SHA256;
const actual = await sha256File('agent.tar.gz');
if (actual !== expected) {
  console.error(`checksum mismatch: ${actual}`);
  process.exit(1);
}
console.log('checksum OK');

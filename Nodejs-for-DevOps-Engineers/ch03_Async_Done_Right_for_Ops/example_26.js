// Book: Node.js for DevOps Engineers — Example 26
// examples/wait-rollout.js
import { waitFor } from '../src/lib/wait-for.js';

let ready = 0;
const desired = 6;

await waitFor(
  async () => {
    ready = Math.min(desired, ready + 2); // simulated
    return { done: ready === desired, ready };
  },
  {
    label: 'tracking rollout',
    intervalMs: 1000,
    timeoutMs: 30_000,
    onTick: (r) =>
      console.log(`${r.ready}/${desired} ready`),
  },
);
console.log('rollout complete');

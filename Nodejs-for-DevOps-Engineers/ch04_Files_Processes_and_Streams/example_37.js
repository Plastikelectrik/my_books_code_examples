// Book: Node.js for DevOps Engineers — Example 37
// examples/build-image.js
import { streamRun } from '../src/lib/stream-run.js';

const tag = 'kestrel/tracking:dev';
await streamRun('docker', ['build', '-t', tag, '.'], {
  signal: AbortSignal.timeout(15 * 60_000),
});
console.log(`built ${tag}`);

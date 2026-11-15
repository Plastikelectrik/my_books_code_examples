// Book: Node.js for DevOps Engineers — Example 43
// examples/download.js
import { createWriteStream } from 'node:fs';
import { Readable } from 'node:stream';
import { pipeline } from 'node:stream/promises';

const url = 'https://releases.example.com/agent.tar.gz';
const res = await fetch(url, {
  signal: AbortSignal.timeout(120_000),
});
if (!res.ok) throw new Error(`HTTP ${res.status}`);

await pipeline(
  Readable.fromWeb(res.body),
  createWriteStream('agent.tar.gz'),
);
console.log('downloaded');

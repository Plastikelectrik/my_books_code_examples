// Book: Node.js for DevOps Engineers — Example 41
// examples/filter-errors.js
import {
  createReadStream, createWriteStream,
} from 'node:fs';
import { createGunzip } from 'node:zlib';
import { pipeline } from 'node:stream/promises';
import { createInterface } from 'node:readline';

async function* errorsOnly(source) {
  const rl = createInterface({ input: source });
  for await (const line of rl) {
    if (/"level":"(error|fatal)"/.test(line)) {
      yield line + '\n';
    }
  }
}

await pipeline(
  createReadStream('app.log.gz'),
  createGunzip(),
  errorsOnly,
  createWriteStream('errors.log'),
);

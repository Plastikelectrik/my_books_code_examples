// Book: Node.js for DevOps Engineers — Example 44
// src/lib/sha256.js
import { createReadStream } from 'node:fs';
import { createHash } from 'node:crypto';
import { pipeline } from 'node:stream/promises';

export async function sha256File(file) {
  const hash = createHash('sha256');
  await pipeline(createReadStream(file), hash);
  return hash.digest('hex');
}

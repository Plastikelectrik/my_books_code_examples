// Book: Node.js for DevOps Engineers — Example 39
// examples/gzip-logs.js
import {
  createReadStream, createWriteStream,
} from 'node:fs';
import { createGzip } from 'node:zlib';
import { pipeline } from 'node:stream/promises';

await pipeline(
  createReadStream('access.log'),
  createGzip(),
  createWriteStream('access.log.gz'),
);
console.log('compressed');

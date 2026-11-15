// Book: Node.js for DevOps Engineers — Example 48
// examples/hash-many.js
import { Worker } from 'node:worker_threads';
import os from 'node:os';

const files = process.argv.slice(2);
const workerCode = `
  const { parentPort } = require('node:worker_threads');
  const { createHash } = require('node:crypto');
  const { readFileSync } = require('node:fs');
  parentPort.on('message', (f) => {
    const h = createHash('sha256')
      .update(readFileSync(f)).digest('hex');
    parentPort.postMessage([f, h]);
  });`;

const cpus = os.availableParallelism();
const size = Math.min(cpus, files.length);
const pool = Array.from({ length: size },
  () => new Worker(workerCode, { eval: true }));

let next = 0;
await Promise.all(pool.map((w) => new Promise((done) => {
  const feed = () => {
    if (next >= files.length) {
      w.terminate();
      return done();
    }
    w.postMessage(files[next++]);
  };
  w.on('message', ([f, h]) => {
    console.log(h, f);
    feed();
  });
  feed();
})));

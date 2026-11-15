// Book: Node.js for DevOps Engineers — Example 84
// src/webhooks/server.js
import { createServer } from 'node:http';
import { buffer } from 'node:stream/consumers';
import { verifySignature } from './verify.js';

const SECRET = process.env.WEBHOOK_SECRET;

async function handle(event) {
  console.log('received', event.action ?? 'event');
}

createServer(async (req, res) => {
  if (req.method !== 'POST') {
    res.writeHead(405).end();
    return;
  }
  const raw = await buffer(req);
  const sig = req.headers['x-hub-signature-256'];
  if (!verifySignature(raw, sig, SECRET)) {
    res.writeHead(401).end('bad signature');
    return;
  }
  const event = JSON.parse(raw);
  res.writeHead(202).end('accepted');
  queueMicrotask(() => handle(event));
}).listen(8080);

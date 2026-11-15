// Book: Node.js for DevOps Engineers — Example 222
// src/http/server.js
import { createServer } from 'node:http';

export function hardenedServer(handler) {
  const server = createServer({
    maxHeaderSize: 16 * 1024,
    requestTimeout: 30_000,
    headersTimeout: 10_000,
  }, handler);
  server.keepAliveTimeout = 65_000;
  server.maxRequestsPerSocket = 1000;
  return server;
}

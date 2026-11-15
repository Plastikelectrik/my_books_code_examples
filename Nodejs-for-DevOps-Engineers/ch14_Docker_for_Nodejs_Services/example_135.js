// Book: Node.js for DevOps Engineers — Example 135
// src/health/server.js
import { createServer } from 'node:http';

let ready = false;
let shuttingDown = false;

export const setReady = (v) => { ready = v; };
export const setShuttingDown = () => {
  shuttingDown = true;
};

export function startHealthServer(port = 8081) {
  return createServer((req, res) => {
    if (req.url === '/livez') {
      res.writeHead(200).end('ok');
    } else if (req.url === '/readyz') {
      const ok = ready && !shuttingDown;
      res.writeHead(ok ? 200 : 503)
        .end(ok ? 'ready' : 'not ready');
    } else {
      res.writeHead(404).end();
    }
  }).listen(port);
}

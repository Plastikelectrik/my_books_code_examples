// Book: Node.js for DevOps Engineers — Example 136
// src/server.js (shutdown sequence)
import { setTimeout as sleep } from 'node:timers/promises';
import { onShutdown } from './lib/shutdown.js';
import { setShuttingDown } from './health/server.js';

onShutdown(async () => {
  setShuttingDown();
  // give load balancers time to notice
  await sleep(5000);
  await new Promise((r) => appServer.close(r));
});

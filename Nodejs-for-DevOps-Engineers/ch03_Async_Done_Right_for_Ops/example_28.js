// Book: Node.js for DevOps Engineers — Example 28
// src/lib/shutdown.js
const tasks = [];

export function onShutdown(fn) {
  tasks.push(fn);
}

let closing = false;
async function shutdown(signal) {
  if (closing) return;
  closing = true;
  console.error(`${signal} received, shutting down`);
  const force = setTimeout(() => process.exit(1), 10_000);
  force.unref();
  for (const fn of tasks.reverse()) {
    try {
      await fn();
    } catch (err) {
      console.error('shutdown task failed', err);
    }
  }
  process.exit(0);
}

process.once('SIGTERM', () => shutdown('SIGTERM'));
process.once('SIGINT', () => shutdown('SIGINT'));

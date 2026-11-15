// Book: Node.js for DevOps Engineers — Example 27
// examples/watch-config.js
import { watch } from 'node:fs/promises';

const ac = new AbortController();
process.once('SIGINT', () => ac.abort());

try {
  const watcher = watch('./config', { signal: ac.signal });
  for await (const event of watcher) {
    console.log(`${event.eventType}: ${event.filename}`);
  }
} catch (err) {
  if (err.name !== 'AbortError') throw err;
}
console.log('stopped watching');

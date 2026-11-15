// Book: Node.js for DevOps Engineers — Example 146
// src/docker/events.js
import { createInterface } from 'node:readline';
import { Readable } from 'node:stream';

export async function* dockerEvents(
  docker, filters, signal,
) {
  const res = await docker.call('GET', '/events', null,
    { filters });
  const lines = createInterface({
    input: Readable.fromWeb(res.body, { signal }),
  });
  for await (const line of lines) {
    if (line.trim()) yield JSON.parse(line);
  }
}

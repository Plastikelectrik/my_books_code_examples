// Book: Node.js for DevOps Engineers — Example 215
// src/diagnostics/summarise-report.js
import { readFile } from 'node:fs/promises';

export async function summariseReport(file) {
  const r = JSON.parse(await readFile(file, 'utf8'));
  return {
    node: r.header.nodejsVersion,
    uptimeS: Math.round(r.header.uptime ?? 0),
    heapUsedMb: Math.round(
      r.javascriptHeap.usedMemory / 1048576),
    rssMb: Math.round(r.resourceUsage.rss / 1024),
    handles: Object.entries(
      Map.groupBy(r.libuv, (h) => h.type))
      .map(([type, list]) => `${type}:${list.length}`)
      .join(' '),
    jsStack: r.javascriptStack?.stack?.slice(0, 5),
  };
}

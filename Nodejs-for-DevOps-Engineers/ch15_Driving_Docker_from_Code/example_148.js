// Book: Node.js for DevOps Engineers — Example 148
// examples/top-containers.js
import { dockerClient } from '../src/docker/client.js';
import { mapLimit } from '../src/lib/pool.js';
import { cpuPercent, memoryUsage } from
  '../src/docker/stats.js';

const docker = dockerClient();
const running = await docker.get('/containers/json');
const rows = await mapLimit(running, 6, async (c) => {
  const s = await docker.get(`/containers/${c.Id}/stats`,
    { stream: false });
  const mem = memoryUsage(s);
  return {
    name: c.Names[0].slice(1),
    cpu: cpuPercent(s).toFixed(1) + '%',
    mem: `${mem.usedMb.toFixed(0)} / ` +
      `${mem.limitMb.toFixed(0)} MB`,
  };
});
console.table(rows);

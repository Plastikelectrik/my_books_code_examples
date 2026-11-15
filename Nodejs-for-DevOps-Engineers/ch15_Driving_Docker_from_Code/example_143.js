// Book: Node.js for DevOps Engineers — Example 143
// examples/docker-ps.js
import { dockerClient } from '../src/docker/client.js';

const docker = dockerClient();
const containers = await docker.get('/containers/json', {
  all: true,
  filters: { label: ['com.kestrel.service'] },
});

for (const c of containers) {
  const name = c.Names[0].slice(1);
  const svc = c.Labels['com.kestrel.service'];
  console.log(`${name.padEnd(28)} ${svc.padEnd(14)} ` +
    `${c.State}`);
}

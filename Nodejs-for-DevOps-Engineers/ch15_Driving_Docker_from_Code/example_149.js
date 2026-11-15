// Book: Node.js for DevOps Engineers — Example 149
// test/helpers/postgres.js
import { dockerClient } from '../../src/docker/client.js';
import { waitFor } from '../../src/lib/wait-for.js';
import net from 'node:net';

const docker = dockerClient();

export async function startPostgres() {
  const expires = new Date(Date.now() + 3_600_000)
    .toISOString();
  const { Id } = await docker.post('/containers/create', {
    Image: 'postgres:17',
    Env: ['POSTGRES_PASSWORD=test'],
    Labels: { 'com.kestrel.env': 'test',
      'com.kestrel.expires': expires },
    HostConfig: {
      PortBindings: { '5432/tcp': [{ HostPort: '0' }] },
      AutoRemove: true,
    },
  });
  await docker.post(`/containers/${Id}/start`);
  const info = await docker.get(`/containers/${Id}/json`);
  const port = Number(
    info.NetworkSettings.Ports['5432/tcp'][0].HostPort);

  await waitFor(async () => ({
    done: await canConnect(port),
  }), { intervalMs: 500, timeoutMs: 30_000,
    label: 'postgres ready' });

  return {
    url: 'postgres://postgres:test@127.0.0.1:' +
      `${port}/postgres`,
    stop: () => docker.post(`/containers/${Id}/stop`,
      null, { t: 1 }),
  };
}

function canConnect(port) {
  return new Promise((resolve) => {
    const s = net.connect(port, '127.0.0.1');
    s.once('connect', () => { s.end(); resolve(true); });
    s.once('error', () => resolve(false));
  });
}

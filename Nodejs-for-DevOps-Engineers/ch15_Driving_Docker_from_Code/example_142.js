// Book: Node.js for DevOps Engineers — Example 142
// src/docker/client.js
import { Agent } from 'undici';

export function dockerClient(opts = {}) {
  const socketPath = opts.socketPath
    ?? process.env.DOCKER_SOCKET
    ?? '/var/run/docker.sock';
  const version = opts.apiVersion ?? 'v1.45';
  const dispatcher = new Agent({ connect: { socketPath } });

  async function call(method, path, body, query) {
    const url = new URL(`http://docker/${version}${path}`);
    for (const [k, v] of Object.entries(query ?? {})) {
      url.searchParams.set(k, typeof v === 'object'
        ? JSON.stringify(v) : String(v));
    }
    const res = await fetch(url, {
      method,
      dispatcher,
      headers: body
        ? { 'Content-Type': 'application/json' } : {},
      body: body ? JSON.stringify(body) : undefined,
      signal: AbortSignal.timeout(opts.timeoutMs ?? 30_000),
    });
    if (!res.ok) {
      const text = await res.text();
      throw new Error(`docker ${method} ${path}: ` +
        `${res.status} ${text}`);
    }
    const type = res.headers.get('content-type') ?? '';
    return type.includes('json') ? res.json() : res;
  }

  return {
    call,
    get: (p, q) => call('GET', p, null, q),
    post: (p, b, q) => call('POST', p, b, q),
    del: (p, q) => call('DELETE', p, null, q),
  };
}

// Book: Node.js for DevOps Engineers — Example 124
// src/release/digest.js
import { run } from '../lib/run.js';

export async function pushAndGetDigest(tag) {
  await run('docker', ['push', tag]);
  const out = await run('docker', ['buildx', 'imagetools',
    'inspect', tag, '--format', '{{json .Manifest}}']);
  return JSON.parse(out).digest;
}

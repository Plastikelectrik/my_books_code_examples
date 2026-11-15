// Book: Node.js for DevOps Engineers — Example 137
// src/docker/build.js
import { streamRun } from '../lib/stream-run.js';

export async function buildImage(o) {
  const {
    context, tags, platforms = ['linux/amd64'],
    push = false, cacheRef, labels = {},
  } = o;

  const args = ['buildx', 'build', context,
    '--platform', platforms.join(',')];
  for (const t of tags) args.push('--tag', t);
  for (const [k, v] of Object.entries(labels)) {
    args.push('--label', `${k}=${v}`);
  }
  if (cacheRef) {
    const ref = `type=registry,ref=${cacheRef}`;
    args.push('--cache-from', ref,
      '--cache-to', `${ref},mode=max`);
  }
  args.push(push ? '--push' : '--load');
  await streamRun('docker', args);
}

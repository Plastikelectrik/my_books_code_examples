// Read release history from git (Chapter 12).
import { run } from '../lib/run.js';

export async function lastTag() {
  try {
    return await run('git',
      ['describe', '--tags', '--abbrev=0',
        '--match', 'v*']);
  } catch {
    return null; // no release yet
  }
}

export async function commitsSince(tag) {
  const range = tag ? `${tag}..HEAD` : 'HEAD';
  const SEP = '\x1e';
  const out = await run('git', ['log', range,
    `--format=%H%x1f%s%x1f%b${SEP}`]);
  return out.split(SEP)
    .map((s) => s.trim())
    .filter(Boolean)
    .map((entry) => {
      const [hash, subject, body] = entry.split('\x1f');
      return { hash, subject, body: body ?? '' };
    });
}

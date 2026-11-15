// Book: Node.js for DevOps Engineers — Example 18
// examples/scan-repos.js
import { mapLimit } from '../src/lib/pool.js';

const repos = Array.from(
  { length: 40 },
  (_, i) => `kestrel/service-${i + 1}`,
);

const results = await mapLimit(repos, 5, async (repo) => {
  const res = await fetch(
    `https://api.github.com/repos/${repo}`,
    { signal: AbortSignal.timeout(5000) },
  );
  return { repo, status: res.status };
});

console.log(`${results.length} repositories checked`);

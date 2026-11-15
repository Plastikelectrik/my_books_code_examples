// Book: Node.js for DevOps Engineers — Example 01
// check-health.mjs
const services = [
  'https://api.example.com/health',
  'https://auth.example.com/health',
  'https://track.example.com/health',
];

async function check(url) {
  const started = performance.now();
  try {
    const res = await fetch(url, {
      signal: AbortSignal.timeout(3000),
    });
    const ms = Math.round(performance.now() - started);
    return { url, ok: res.ok, status: res.status, ms };
  } catch (err) {
    return { url, ok: false, error: err.name };
  }
}

const results = await Promise.all(services.map(check));
console.table(results);

const failed = results.filter((r) => !r.ok);
process.exitCode = failed.length > 0 ? 1 : 0;

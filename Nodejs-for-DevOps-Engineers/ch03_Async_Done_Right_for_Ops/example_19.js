// Book: Node.js for DevOps Engineers — Example 19
// examples/fleet-report.js
const hosts = ['web-1', 'web-2', 'web-3', 'web-4'];

async function uptime(host) {
  const res = await fetch(`http://${host}:9100/uptime`, {
    signal: AbortSignal.timeout(2000),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.text();
}

const settled = await Promise.allSettled(hosts.map(uptime));

settled.forEach((r, i) => {
  const host = hosts[i].padEnd(8);
  if (r.status === 'fulfilled') {
    console.log(`${host} up ${r.value.trim()}`);
  } else {
    console.log(`${host} FAILED ${r.reason.message}`);
  }
});

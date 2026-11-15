// Book: Node.js for DevOps Engineers — Example 96
// src/fleet/group-output.js
export function groupOutput(results) {
  const groups = new Map();
  for (const r of results) {
    const key = r.code === 0
      ? r.stdout.trim()
      : `ERROR (${r.code ?? r.error}): ${r.stderr.trim()}`;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(r.host);
  }
  const sorted = [...groups].sort(
    (a, b) => b[1].length - a[1].length);
  for (const [text, hosts] of sorted) {
    console.log(`── ${hosts.length} host(s): ` +
      summarise(hosts));
    console.log(text || '(no output)');
    console.log();
  }
}

function summarise(hosts) {
  return hosts.length <= 4
    ? hosts.join(', ')
    : `${hosts.slice(0, 3).join(', ')} ` +
      `+${hosts.length - 3}`;
}

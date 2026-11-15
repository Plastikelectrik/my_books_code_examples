// Group hosts that printed the same thing (Chapter 9).
export function groupResults(results) {
  const groups = new Map();
  for (const r of results) {
    const key = r.code === 0
      ? r.stdout.trim()
      : `ERROR (${r.code ?? r.error}): ${r.stderr.trim()}`;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(r.host);
  }
  return [...groups].sort(
    (a, b) => b[1].length - a[1].length);
}

export function printGroups(results, print = console.log) {
  for (const [text, hosts] of groupResults(results)) {
    print(`── ${hosts.length} host(s): ` + summarise(hosts));
    print(text || '(no output)');
    print('');
  }
}

function summarise(hosts) {
  return hosts.length <= 4
    ? hosts.join(', ')
    : `${hosts.slice(0, 3).join(', ')} ` +
      `+${hosts.length - 3}`;
}

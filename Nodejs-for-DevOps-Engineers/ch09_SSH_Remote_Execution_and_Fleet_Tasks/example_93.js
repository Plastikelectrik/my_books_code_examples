// Book: Node.js for DevOps Engineers — Example 93
// src/fleet/inventory.js
import { readFile } from 'node:fs/promises';
import { parse } from 'yaml';

export async function loadInventory(
  file = 'inventory.yaml',
) {
  const doc = parse(await readFile(file, 'utf8'));
  const hosts = doc.hosts.map((h) => ({
    ...doc.defaults, ...h,
    groups: h.groups ?? [],
    tags: h.tags ?? {},
  }));
  return {
    all: hosts,
    select: (query) => hosts.filter(matcher(query)),
    byName: (n) => hosts.find((h) => h.name === n),
  };
}

// query examples:
//   "db", "db,eu", "build|edge", "role=replica"
function matcher(query) {
  if (!query) return () => true;
  const alternatives = query.split('|');
  return (host) => alternatives.some((alt) =>
    alt.split(',').every((term) => {
      const [k, v] = term.split('=');
      return v === undefined
        ? host.groups.includes(k) || host.name === k
        : host.tags[k] === v;
    }));
}

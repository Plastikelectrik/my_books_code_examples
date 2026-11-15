// Book: Node.js for DevOps Engineers — Example 228
// src/catalog/load.js
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { ServiceSchema } from './schema.js';
import { cacheDir } from '../lib/dirs.js';
import { writeAtomic } from '../lib/atomic-write.js';
import { CliError } from '../lib/errors.js';

const CACHE = path.join(cacheDir, 'catalog.json');
const MAX_AGE_MS = 15 * 60_000;

export async function loadCatalog(o) {
  const { url, fetchImpl = fetch } = o;
  let raw = await readCache();
  if (!raw) {
    const res = await fetchImpl(url, {
      signal: AbortSignal.timeout(5000),
    });
    if (!res.ok) {
      throw new CliError(`catalog: HTTP ${res.status}`,
        { code: 3 });
    }
    raw = await res.text();
    await writeAtomic(CACHE, raw);
  }
  const list = JSON.parse(raw).map((s) =>
    ServiceSchema.parse(s));
  return makeCatalog(list);
}

async function readCache() {
  try {
    const { mtimeMs } = await stat(CACHE);
    if (Date.now() - mtimeMs > MAX_AGE_MS) return null;
    return await readFile(CACHE, 'utf8');
  } catch {
    return null;
  }
}

export function makeCatalog(list) {
  const byName = new Map(list.map((s) => [s.name, s]));
  return {
    all: () => list,
    get(name) {
      const s = byName.get(name);
      if (!s) {
        throw new CliError(`unknown service: ${name}`,
          { code: 2 });
      }
      return s;
    },
    byTeam: (team) =>
      list.filter((s) => s.owner.team === team),
    dependents: (name) =>
      list.filter((s) => s.dependencies.includes(name)),
  };
}

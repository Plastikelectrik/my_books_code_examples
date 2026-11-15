// Load and query the service catalogue (Chapter 26).
// The book loads a published JSON catalogue over HTTP; this
// runnable version reads a local YAML file instead.
import { readFile } from 'node:fs/promises';
import { parse } from 'yaml';
import { ServiceSchema } from './schema.js';
import { CliError } from '../lib/errors.js';

export async function loadCatalog(file) {
  let doc;
  try {
    doc = parse(await readFile(file, 'utf8'));
  } catch (err) {
    throw new CliError(`cannot read catalogue ${file}`,
      { code: 2, cause: err });
  }
  const list = (doc?.services ?? []).map((s, i) => {
    const r = ServiceSchema.safeParse(s);
    if (!r.success) {
      const why = r.error.issues
        .map((x) => `${x.path.join('.')}: ${x.message}`)
        .join('; ');
      throw new CliError(
        `invalid service #${i + 1} in ${file}: ${why}`,
        { code: 2 });
    }
    return r.data;
  });
  return makeCatalog(list);
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

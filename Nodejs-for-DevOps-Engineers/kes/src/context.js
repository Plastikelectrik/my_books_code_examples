// The shared context every command receives (Chapter 26).
import { loadConfig } from './config/load.js';
import { createOutput } from './lib/output.js';
import { envBanner } from './lib/banner.js';

function lazy(factory) {
  let value;
  let created = false;
  return async () => {
    if (!created) {
      value = await factory();
      created = true;
    }
    return value;
  };
}

export async function createContext(cmd, values) {
  const config = await loadConfig(values);
  if (!values.json) envBanner(config);
  const out = createOutput(values);
  return {
    cmd,
    config,
    out,
    runId: crypto.randomUUID(),
    catalog: lazy(async () => {
      const { loadCatalog } = await import(
        './catalog/load.js');
      return loadCatalog(config.catalogFile);
    }),
  };
}

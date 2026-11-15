// Book: Node.js for DevOps Engineers — Example 229
// src/context.js
import { loadConfig } from './config/load.js';
import { createOutput } from './lib/output.js';
import { logger } from './lib/logger.js';
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
  envBanner(config);
  const runId = crypto.randomUUID();
  return {
    config,
    out: createOutput(values),
    log: logger.child({ cmd, runId, env: config.env }),
    catalog: lazy(async () => {
      const { loadCatalog } = await import(
        './catalog/load.js');
      return loadCatalog({ url: config.catalogUrl });
    }),
    kube: lazy(async () => {
      const { kube } = await import('./kube/client.js');
      return kube({ context: config.kubeContext });
    }),
    metrics: lazy(async () => {
      const { prometheus } = await import(
        './canary/metrics.js');
      return prometheus(config.metricsUrl);
    }),
    chat: lazy(async () => {
      const { chatClient } = await import(
        './chat/client.js');
      const { resolveToken } = await import(
        './secrets/resolve.js');
      return chatClient(await resolveToken('chat'),
        config.chatApiUrl);
    }),
  };
}

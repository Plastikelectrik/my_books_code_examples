// Book: Node.js for DevOps Engineers — Example 235
// test/helpers/fake-context.js
import { makeCatalog } from '../../src/catalog/load.js';

export function fakeContext(over = {}) {
  const printed = [];
  return {
    config: { env: 'staging', ...over.config },
    out: {
      json: false,
      result: (data, render) => render(data),
      info: (m) => printed.push(m),
      debug: () => {},
      ok: (m) => `OK ${m}`,
      bad: (m) => `FAIL ${m}`,
    },
    log: { info() {}, warn() {}, error() {},
      child() { return this; } },
    catalog: async () => makeCatalog(over.services ?? []),
    kube: async () => over.kube,
    metrics: async () => over.metrics,
    chat: async () => over.chat,
    printed,
  };
}

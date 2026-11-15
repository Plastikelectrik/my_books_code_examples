// Book: Node.js for DevOps Engineers — Example 160
// src/controllers/namespace-reaper.js
import * as k8s from '@kubernetes/client-node';

const LABEL = 'kestrel.dev/expires';

export function shouldDelete(ns, now) {
  const raw = ns.metadata.labels?.[LABEL];
  if (!raw) return false;
  const at = Number(raw) * 1000;  // unix seconds
  return Number.isFinite(at) && at < now
    && ns.status?.phase !== 'Terminating';
}

export async function reconcile(core, ns, log) {
  if (!shouldDelete(ns, Date.now())) return;
  log(`deleting expired namespace ${ns.metadata.name}`);
  try {
    await core.deleteNamespace({ name: ns.metadata.name });
  } catch (err) {
    if (err.code !== 404) throw err;
  }
}

export async function startReaper(kc, log = console.log) {
  const core = kc.makeApiClient(k8s.CoreV1Api);
  const list = () =>
    core.listNamespace({ labelSelector: LABEL });
  const informer = k8s.makeInformer(kc,
    '/api/v1/namespaces', list, LABEL);

  const handle = (ns) => reconcile(core, ns, log)
    .catch((e) => log(`reconcile failed: ${e.message}`));
  informer.on('add', handle);
  informer.on('update', handle);
  informer.on('error', () =>
    setTimeout(() => informer.start(), 5000));
  await informer.start();

  // periodic resync: expiry is time-based, not event-based
  setInterval(() => {
    for (const ns of informer.list()) handle(ns);
  }, 60_000).unref();
}

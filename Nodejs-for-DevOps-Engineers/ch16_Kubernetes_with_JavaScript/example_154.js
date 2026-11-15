// Book: Node.js for DevOps Engineers — Example 154
// src/kube/apply.js
import * as k8s from '@kubernetes/client-node';

export async function apply(kc, manifest, opts = {}) {
  const client = k8s.KubernetesObjectApi.makeApiClient(kc);
  return client.patch(
    manifest,
    undefined,          // pretty
    opts.dryRun ? 'All' : undefined,
    'kes',              // field manager
    opts.force ?? false,
    k8s.PatchStrategy.ServerSideApply,
  );
}

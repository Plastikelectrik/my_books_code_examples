// Book: Node.js for DevOps Engineers — Example 151
// src/kube/client.js
import * as k8s from '@kubernetes/client-node';

export function kube(opts = {}) {
  const kc = new k8s.KubeConfig();
  kc.loadFromDefault();
  if (opts.context) kc.setCurrentContext(opts.context);
  return {
    kc,
    core: kc.makeApiClient(k8s.CoreV1Api),
    apps: kc.makeApiClient(k8s.AppsV1Api),
    net: kc.makeApiClient(k8s.NetworkingV1Api),
    batch: kc.makeApiClient(k8s.BatchV1Api),
    custom: kc.makeApiClient(k8s.CustomObjectsApi),
    context: kc.getCurrentContext(),
  };
}

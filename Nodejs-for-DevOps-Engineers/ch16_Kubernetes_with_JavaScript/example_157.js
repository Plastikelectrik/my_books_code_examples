// Book: Node.js for DevOps Engineers — Example 157
// src/kube/informer.js
import * as k8s from '@kubernetes/client-node';

export function podInformer(kc, namespace) {
  const core = kc.makeApiClient(k8s.CoreV1Api);
  const path = `/api/v1/namespaces/${namespace}/pods`;
  const informer = k8s.makeInformer(kc, path,
    () => core.listNamespacedPod({ namespace }));
  informer.on('error', () => {
    setTimeout(() => informer.start(), 5000);
  });
  return informer;
}

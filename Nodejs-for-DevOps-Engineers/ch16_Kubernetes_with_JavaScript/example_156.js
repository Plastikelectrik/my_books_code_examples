// Book: Node.js for DevOps Engineers — Example 156
// src/kube/watch-pods.js
import * as k8s from '@kubernetes/client-node';

export async function watchPods(kc, namespace, onEvent) {
  const watch = new k8s.Watch(kc);
  const path = `/api/v1/namespaces/${namespace}/pods`;
  const req = await watch.watch(path, {},
    (type, pod) => onEvent(type, pod),
    (err) => {
      if (err) console.error('watch ended:', err.message);
    });
  return () => req.abort();
}

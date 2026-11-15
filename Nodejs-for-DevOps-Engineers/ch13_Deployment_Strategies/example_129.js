// Book: Node.js for DevOps Engineers — Example 129
// src/canary/routers/nginx-ingress.js
export function nginxIngressRouter(k8s, ns, ingress) {
  return {
    async setCanary(weight) {
      const patch = { metadata: { annotations: {
        'nginx.ingress.kubernetes.io/canary': 'true',
        'nginx.ingress.kubernetes.io/canary-weight':
          String(weight),
      } } };
      await k8s.patchIngress(ns, ingress, patch);
    },
  };
}

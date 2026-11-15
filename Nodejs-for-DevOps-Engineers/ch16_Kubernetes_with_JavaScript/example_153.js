// Book: Node.js for DevOps Engineers — Example 153
// src/kube/set-image.js
import * as k8s from '@kubernetes/client-node';

export async function setImage(apps, o) {
  const { namespace, name, container, image } = o;
  const body = {
    spec: { template: { spec: { containers: [
      { name: container, image },
    ] } } },
  };
  return apps.patchNamespacedDeployment(
    { name, namespace, body },
    k8s.setHeaderOptions('Content-Type',
      k8s.PatchStrategy.StrategicMergePatch),
  );
}

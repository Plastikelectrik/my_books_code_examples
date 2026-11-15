// Book: Node.js for DevOps Engineers — Example 158
// src/kube/run-job.js
export function jobManifest(o) {
  const { name, namespace, image, command, sa } = o;
  return {
    apiVersion: 'batch/v1',
    kind: 'Job',
    metadata: { name, namespace,
      labels: { 'app.kubernetes.io/managed-by': 'kes' } },
    spec: {
      backoffLimit: 0,
      ttlSecondsAfterFinished: 3600,
      activeDeadlineSeconds: 1800,
      template: {
        spec: {
          restartPolicy: 'Never',
          serviceAccountName: sa,
          containers: [{ name: 'task', image, command }],
        },
      },
    },
  };
}

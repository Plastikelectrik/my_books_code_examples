// Book: Node.js for DevOps Engineers — Example 159
// src/kube/audit.js
export const CHECKS = [
  ['has resource requests', (c) =>
    Boolean(c.resources?.requests?.cpu
      && c.resources?.requests?.memory)],
  ['has memory limit', (c) =>
    Boolean(c.resources?.limits?.memory)],
  ['has readiness probe', (c) => Boolean(c.readinessProbe)],
  ['image pinned (no :latest)', (c) =>
    !/:latest$/.test(c.image) && c.image.includes(':')],
  ['runs as non-root', (c, pod) =>
    (c.securityContext?.runAsNonRoot
      ?? pod.securityContext?.runAsNonRoot) === true],
];

export function auditDeployment(d) {
  const pod = d.spec.template.spec;
  const failures = [];
  for (const c of pod.containers) {
    for (const [label, check] of CHECKS) {
      if (!check(c, pod)) {
        failures.push(`${c.name}: ${label}`);
      }
    }
  }
  return failures;
}

// Book: Node.js for DevOps Engineers — Example 155
// src/kube/rollout.js
import { waitFor } from '../lib/wait-for.js';

export function rolloutState(d) {
  const want = d.spec.replicas ?? 1;
  const s = d.status ?? {};
  const observed = (s.observedGeneration ?? 0)
    >= d.metadata.generation;
  const failed = s.conditions?.find((c) =>
    c.type === 'Progressing'
    && c.reason === 'ProgressDeadlineExceeded');
  if (failed) return { done: true, ok: false,
    reason: failed.message };
  const complete = observed
    && (s.updatedReplicas ?? 0) === want
    && (s.availableReplicas ?? 0) === want
    && (s.replicas ?? 0) === want;
  const upd = s.updatedReplicas ?? 0;
  const avail = s.availableReplicas ?? 0;
  return { done: complete, ok: complete,
    progress: `${upd}/${want} updated, ` +
      `${avail} available` };
}

export async function waitForRollout(apps, ns, name, o) {
  const result = await waitFor(async () => {
    const d = await apps.readNamespacedDeployment(
      { name, namespace: ns });
    const st = rolloutState(d);
    return { done: st.done, value: st, ...st };
  }, { timeoutMs: 600_000, intervalMs: 3000,
    label: `rollout of ${ns}/${name}`, ...o });
  if (!result.ok) throw new Error(result.reason);
  return result;
}

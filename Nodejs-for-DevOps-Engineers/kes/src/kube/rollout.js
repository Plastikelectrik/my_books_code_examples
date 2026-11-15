// Is a Deployment rollout complete? Pure, testable (Chapter 16).
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

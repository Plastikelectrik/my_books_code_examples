// Book: Node.js for DevOps Engineers — Example 144
// src/docker/cleanup-plan.js
const HOUR = 3_600_000;

export function planCleanup(state, opts) {
  const { now, maxStoppedHours = 24 } = opts;
  const actions = [];

  for (const c of state.containers) {
    const expires = c.Labels?.['com.kestrel.expires'];
    if (expires && Date.parse(expires) < now) {
      actions.push({ kind: 'container', id: c.Id,
        reason: `expired ${expires}`, force: true });
      continue;
    }
    const stoppedFor = now - c.finishedAt;
    if (c.State === 'exited'
      && stoppedFor > maxStoppedHours * HOUR) {
      const hours = Math.round(stoppedFor / HOUR);
      actions.push({ kind: 'container', id: c.Id,
        reason: `exited ${hours}h ago` });
    }
  }

  for (const img of state.images) {
    if (img.RepoTags?.length === 0 || !img.RepoTags) {
      actions.push({ kind: 'image', id: img.Id,
        reason: 'dangling' });
    }
  }
  return actions;
}

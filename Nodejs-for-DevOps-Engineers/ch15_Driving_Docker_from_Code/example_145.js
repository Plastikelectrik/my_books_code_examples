// Book: Node.js for DevOps Engineers — Example 145
// src/docker/cleanup.js
import { mapLimit } from '../lib/pool.js';
import { planCleanup } from './cleanup-plan.js';

export async function gatherState(docker) {
  const list = await docker.get('/containers/json',
    { all: true });
  const containers = await mapLimit(list, 8, async (c) => {
    const info = await docker.get(
      `/containers/${c.Id}/json`);
    return { ...c,
      finishedAt: Date.parse(info.State.FinishedAt) };
  });
  const images = await docker.get('/images/json',
    { filters: { dangling: ['true'] } });
  return { containers, images };
}

export async function cleanup(docker, { apply, log }) {
  const state = await gatherState(docker);
  const actions = planCleanup(state, { now: Date.now() });
  for (const a of actions) {
    log(`${apply ? 'remove' : 'would remove'} ` +
      `${a.kind} ${a.id.slice(0, 12)} (${a.reason})`);
    if (!apply) continue;
    const path = a.kind === 'container'
      ? `/containers/${a.id}` : `/images/${a.id}`;
    await docker.del(path, a.force ? { force: true } : {});
  }
  return actions;
}

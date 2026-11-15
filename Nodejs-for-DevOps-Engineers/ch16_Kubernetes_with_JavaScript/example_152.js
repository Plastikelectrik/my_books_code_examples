// Book: Node.js for DevOps Engineers — Example 152
// examples/pods-not-running.js
import { kube } from '../src/kube/client.js';

const { core, context } = kube();
console.error(`context: ${context}`);

const pods = await core.listPodForAllNamespaces({
  fieldSelector: 'status.phase!=Running,' +
    'status.phase!=Succeeded',
});

for (const p of pods.items) {
  const ns = p.metadata.namespace;
  const name = p.metadata.name;
  const reason = p.status.containerStatuses
    ?.find((c) => c.state?.waiting)?.state.waiting.reason
    ?? p.status.phase;
  console.log(`${ns}/${name}  ${reason}`);
}

// Book: Node.js for DevOps Engineers — Example 175
// examples/count-instances.js
import { enabledRegions } from
  '../src/cloud/aws/regions.js';
import { instances } from '../src/cloud/aws/instances.js';
import { mapLimit } from '../src/lib/pool.js';

const regions = await enabledRegions();
const counts = await mapLimit(regions, 6, async (r) => {
  let n = 0;
  for await (const _ of instances(r, [
    { Name: 'instance-state-name', Values: ['running'] },
  ])) n++;
  return { region: r, running: n };
});
console.table(counts.filter((c) => c.running > 0));

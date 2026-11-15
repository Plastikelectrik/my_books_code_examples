// Book: Node.js for DevOps Engineers — Example 49
// examples/running-by-team.js
import { run } from '../src/lib/run.js';

const raw = await run('aws', [
  'ec2', 'describe-instances', '--output', 'json',
]);
const { Reservations } = JSON.parse(raw);

const tag = (inst, key) =>
  inst.Tags?.find((t) => t.Key === key)?.Value ?? '-';

const rows = Reservations
  .flatMap((r) => r.Instances)
  .filter((i) => i.State.Name === 'running')
  .map((i) => ({ id: i.InstanceId, team: tag(i, 'team') }));

console.table(rows);

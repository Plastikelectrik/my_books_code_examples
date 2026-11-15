// Book: Node.js for DevOps Engineers — Example 181
// examples/gcp-instances.js
import { InstancesClient } from '@google-cloud/compute';

const client = new InstancesClient();
const iterable = client.aggregatedListAsync({
  project: 'kestrel-prod',
});
for await (const [zone, scoped] of iterable) {
  for (const vm of scoped.instances ?? []) {
    console.log(zone, vm.name, vm.status);
  }
}

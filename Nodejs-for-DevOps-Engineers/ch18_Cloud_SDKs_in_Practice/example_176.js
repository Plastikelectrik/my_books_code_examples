// Book: Node.js for DevOps Engineers — Example 176
// src/fleet/aws-inventory.js
import { instances } from '../cloud/aws/instances.js';

const tag = (i, k) =>
  i.Tags?.find((t) => t.Key === k)?.Value;

export async function awsInventory(regions) {
  const hosts = [];
  for (const region of regions) {
    for await (const i of instances(region, [
      { Name: 'instance-state-name', Values: ['running'] },
      { Name: 'tag:managed-by', Values: ['kes'] },
    ])) {
      hosts.push({
        name: tag(i, 'Name') ?? i.InstanceId,
        address: i.PrivateIpAddress,
        groups: (tag(i, 'groups') ?? '').split(',')
          .filter(Boolean),
        tags: { region, team: tag(i, 'team'),
          role: tag(i, 'role') },
      });
    }
  }
  return hosts;
}

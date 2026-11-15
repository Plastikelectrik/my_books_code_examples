// Book: Node.js for DevOps Engineers — Example 185
// functions/tag-creator/index.mjs
import {
  EC2Client, CreateTagsCommand,
} from '@aws-sdk/client-ec2';

const clients = new Map();
const ec2For = (region) => {
  if (!clients.has(region)) {
    clients.set(region, new EC2Client({ region }));
  }
  return clients.get(region);
};

export const handler = async (event) => {
  const detail = event.detail;
  if (detail.eventName !== 'RunInstances') return;

  const ids = detail.responseElements?.instancesSet?.items
    ?.map((i) => i.instanceId) ?? [];
  if (ids.length === 0) return;

  const creator = detail.userIdentity?.arn ?? 'unknown';
  await ec2For(event.region).send(new CreateTagsCommand({
    Resources: ids,
    Tags: [
      { Key: 'created-by', Value: creator.slice(0, 256) },
      { Key: 'created-at', Value: detail.eventTime },
    ],
  }));
  console.log(JSON.stringify({ tagged: ids, creator }));
};

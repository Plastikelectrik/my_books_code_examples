// Book: Node.js for DevOps Engineers — Example 173
// src/cloud/aws/instances.js
import { EC2Client, paginateDescribeInstances } from
  '@aws-sdk/client-ec2';

export async function* instances(region, filters = []) {
  const client = new EC2Client({ region });
  const pages = paginateDescribeInstances(
    { client, pageSize: 500 },
    { Filters: filters },
  );
  for await (const page of pages) {
    for (const r of page.Reservations ?? []) {
      yield* r.Instances ?? [];
    }
  }
}

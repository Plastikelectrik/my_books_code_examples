// Book: Node.js for DevOps Engineers — Example 174
// src/cloud/aws/regions.js
import { EC2Client, DescribeRegionsCommand } from
  '@aws-sdk/client-ec2';

export async function enabledRegions() {
  const ec2 = new EC2Client({ region: 'us-east-1' });
  const res = await ec2.send(new DescribeRegionsCommand({
    AllRegions: false,
  }));
  return res.Regions.map((r) => r.RegionName).sort();
}

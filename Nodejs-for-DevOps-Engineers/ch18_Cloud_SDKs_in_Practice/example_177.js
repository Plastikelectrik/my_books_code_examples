// Book: Node.js for DevOps Engineers — Example 177
// src/cloud/aws/waste.js
import {
  EC2Client,
  paginateDescribeVolumes,
  DescribeAddressesCommand,
  paginateDescribeSnapshots,
} from '@aws-sdk/client-ec2';

export async function findWaste(region, now = Date.now()) {
  const client = new EC2Client({ region });
  const findings = [];

  for await (const page of paginateDescribeVolumes(
    { client }, { Filters: [
      { Name: 'status', Values: ['available'] },
    ] })) {
    for (const v of page.Volumes ?? []) {
      findings.push({ region, kind: 'unattached-volume',
        id: v.VolumeId, sizeGb: v.Size,
        ageDays: ageDays(v.CreateTime, now) });
    }
  }

  const { Addresses } = await client.send(
    new DescribeAddressesCommand({}));
  for (const a of Addresses ?? []) {
    if (!a.AssociationId) {
      findings.push({ region, kind: 'idle-elastic-ip',
        id: a.AllocationId });
    }
  }

  for await (const page of paginateDescribeSnapshots(
    { client }, { OwnerIds: ['self'] })) {
    for (const s of page.Snapshots ?? []) {
      const age = ageDays(s.StartTime, now);
      if (age > 180) {
        findings.push({ region, kind: 'old-snapshot',
          id: s.SnapshotId, sizeGb: s.VolumeSize,
          ageDays: age });
      }
    }
  }
  return findings;
}

function ageDays(date, now) {
  return Math.floor((now - new Date(date)) / 86_400_000);
}

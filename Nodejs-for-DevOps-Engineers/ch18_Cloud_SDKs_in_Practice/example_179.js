// Book: Node.js for DevOps Engineers — Example 179
// src/cloud/aws/costs.js
import {
  CostExplorerClient, GetCostAndUsageCommand,
} from '@aws-sdk/client-cost-explorer';

export async function costByTag(tagKey, start, end) {
  const ce = new CostExplorerClient({
    region: 'us-east-1',
  });
  const res = await ce.send(new GetCostAndUsageCommand({
    TimePeriod: { Start: start, End: end },
    Granularity: 'MONTHLY',
    Metrics: ['UnblendedCost'],
    GroupBy: [{ Type: 'TAG', Key: tagKey }],
  }));
  const rows = new Map();
  for (const period of res.ResultsByTime) {
    for (const g of period.Groups) {
      const key = g.Keys[0].split('$')[1] || '(untagged)';
      const amount = Number(g.Metrics.UnblendedCost.Amount);
      rows.set(key, (rows.get(key) ?? 0) + amount);
    }
  }
  return [...rows].sort((a, b) => b[1] - a[1]);
}

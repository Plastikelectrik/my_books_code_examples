// Book: Node.js for DevOps Engineers — Example 178
// src/cloud/aws/tag-audit.js
import {
  ResourceGroupsTaggingAPIClient,
  paginateGetResources,
} from '@aws-sdk/client-resource-groups-tagging-api';

const REQUIRED = ['team', 'service', 'env'];

export async function untagged(region) {
  const client =
    new ResourceGroupsTaggingAPIClient({ region });
  const out = [];
  for await (const page of paginateGetResources(
    { client }, { ResourcesPerPage: 100 })) {
    for (const r of page.ResourceTagMappingList ?? []) {
      const keys = new Set(
        (r.Tags ?? []).map((t) => t.Key));
      const missing = REQUIRED.filter((k) => !keys.has(k));
      if (missing.length) {
        out.push({ arn: r.ResourceARN, missing });
      }
    }
  }
  return out;
}

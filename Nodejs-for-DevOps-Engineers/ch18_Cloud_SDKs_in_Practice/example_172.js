// Book: Node.js for DevOps Engineers — Example 172
// src/cloud/aws/assume.js
import { fromTemporaryCredentials } from
  '@aws-sdk/credential-providers';

export function credentialsFor(accountId, roleName) {
  return fromTemporaryCredentials({
    params: {
      RoleArn: `arn:aws:iam::${accountId}:role/${roleName}`,
      RoleSessionName: `kes-${process.env.USER ?? 'ci'}`,
      DurationSeconds: 3600,
    },
  });
}

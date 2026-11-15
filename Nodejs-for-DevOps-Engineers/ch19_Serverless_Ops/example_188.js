// Book: Node.js for DevOps Engineers — Example 188
// functions/lib/secret-cache.js
import {
  SecretsManagerClient, GetSecretValueCommand,
} from '@aws-sdk/client-secrets-manager';

const sm = new SecretsManagerClient({});
let cached;

export async function getWebhook(arn) {
  if (cached && cached.until > Date.now()) return cached.v;
  const res = await sm.send(new GetSecretValueCommand({
    SecretId: arn,
  }));
  cached = { v: res.SecretString,
    until: Date.now() + 5 * 60_000 };
  return cached.v;
}

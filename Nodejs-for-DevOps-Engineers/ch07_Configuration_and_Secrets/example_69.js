// Book: Node.js for DevOps Engineers — Example 69
// src/secrets/aws.js
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from '@aws-sdk/client-secrets-manager';

const client = new SecretsManagerClient({});
const cache = new Map();
const TTL_MS = 5 * 60_000;

export async function getSecret(name) {
  const hit = cache.get(name);
  if (hit && hit.expires > Date.now()) return hit.value;

  const res = await client.send(
    new GetSecretValueCommand({ SecretId: name }),
  );
  const value = res.SecretString;
  cache.set(name, { value, expires: Date.now() + TTL_MS });
  return value;
}

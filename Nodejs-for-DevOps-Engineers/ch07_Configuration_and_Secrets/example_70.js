// Book: Node.js for DevOps Engineers — Example 70
// src/config/resolve-secrets.js
import { getSecret } from '../secrets/aws.js';

export async function resolveSecrets(config) {
  const out = { ...config };
  for (const [key, value] of Object.entries(config)) {
    if (typeof value === 'string'
      && value.startsWith('secret://')) {
      out[key] = await getSecret(value.slice(9));
    }
  }
  return Object.freeze(out);
}

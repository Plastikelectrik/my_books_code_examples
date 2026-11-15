// Book: Node.js for DevOps Engineers — Example 219
// src/supply/verify-image.js
import { run } from '../lib/run.js';

export async function verifyImage(ref, expected) {
  try {
    await run('cosign', [
      'verify', ref,
      '--certificate-identity-regexp', expected.identity,
      '--certificate-oidc-issuer', expected.issuer,
    ], { timeoutMs: 60_000 });
    return true;
  } catch (err) {
    throw new Error(`image ${ref} failed signature ` +
      'verification', { cause: err });
  }
}

// Book: Node.js for DevOps Engineers — Example 224
// src/secrets/file-secret.js
import { readFile } from 'node:fs/promises';
import { watch } from 'node:fs';
import { Secret } from './secret.js';

export async function fileSecret(path, onChange) {
  let current = new Secret(
    (await readFile(path, 'utf8')).trim());
  watch(path, async () => {
    try {
      current = new Secret(
        (await readFile(path, 'utf8')).trim());
      onChange?.(current);
    } catch { /* file mid-update; next event retries */ }
  });
  return () => current;
}

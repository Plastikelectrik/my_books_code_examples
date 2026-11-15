// Book: Node.js for DevOps Engineers — Example 30
// src/lib/json-file.js
import { readFile } from 'node:fs/promises';

export async function readJson(path) {
  try {
    return JSON.parse(await readFile(path, 'utf8'));
  } catch (err) {
    throw new Error(`cannot read JSON from ${path}`, {
      cause: err,
    });
  }
}
